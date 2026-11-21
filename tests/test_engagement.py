"""Quiz polls, feedback poll, channel, weekly/monthly revision, owner report,
daytime collection, topic balance and the second static-GK round."""

import json
from dataclasses import replace
from datetime import datetime, timedelta, timezone

import pytest

from app.__main__ import SAMPLE_DIR, offline_article_fetcher
from app.enrichment import enrich_static_gk
from app.llm import build_client
from app.llm.mock import MockProvider, ScriptedProvider
from app.pipeline import Pipeline, health_report, poll_results
from app.revision import record_digest
from app.schedule_gate import decide
from app.scoring import rank_stories
from app.sources import load_sources
from app.state import StateStore
from app.subscribers import process_updates

from .conftest import NOW, FakeTelegram, no_sleep

OWNER = "999000"
FAKE_PDF = b"%PDF-1.4 fake"


@pytest.fixture
def full(full_settings):
    return replace(full_settings, telegram=replace(full_settings.telegram, owner_chat_id=OWNER, channel_id=""))


def make(settings, telegram=None, provider=None, pdf=None):
    store = StateStore(settings.state_path, settings.state.retention_days, settings.state.max_run_history)
    return Pipeline(
        settings, load_sources(settings.config_dir), store, build_client(settings, provider or MockProvider(), sleep=no_sleep),
        offline_article_fetcher(settings, SAMPLE_DIR / "articles"), telegram=telegram,
        offline_feed_dir=SAMPLE_DIR / "feeds", pdf_builder=pdf,
    )


def state_of(settings):
    return json.loads(settings.state_path.read_text(encoding="utf-8"))


def test_mcqs_go_out_as_quiz_polls_then_feedback_poll_then_pdf(full):
    tg = FakeTelegram()
    r = make(full, tg, pdf=lambda html: FAKE_PDF).run(now=NOW)
    assert r.outcome == "delivered" and r.mcqs == 3
    quizzes = [p for _, p in tg.polls if "correct_option_id" in p]
    feedback = [p for _, p in tg.polls if p.get("allows_multiple_answers")]
    assert len(quizzes) == 3 and len(feedback) == 1
    assert all(q["question"].startswith("প্রশ্ন ") and len(q["options"]) == 4 for q in quizzes)
    assert feedback[0]["options"][-1] == "কোনোটিই নয়" and len(feedback[0]["options"]) == r.stories + 1
    text = "\n".join(t for c, t in tg.sent_to if c == "101")
    assert "নিচে ৩টি কুইজ" in text and "আজকের অনুশীলনী (৩টি MCQ)" not in text  # no duplicate text quiz
    assert tg.documents and tg.documents[0][0] == "101"
    state = state_of(full)
    assert len(state["polls"]) == 4 and {p["k"] for p in state["polls"].values()} == {"quiz", "poll"}


def test_poll_votes_are_recorded_and_reported(full):
    tg = FakeTelegram()
    make(full, tg).run(now=NOW)
    state = state_of(full)
    ed = state["editions"]["2026-10-23"]
    quiz = next(i for i in ed["chunks"] if i["kind"] == "quiz")
    fb = next(i for i in ed["chunks"] if i["kind"] == "poll")
    quiz_id = next(k for k, v in state["polls"].items() if v["i"] == quiz["index"])
    fb_id = next(k for k, v in state["polls"].items() if v["i"] == fb["index"])
    correct = quiz["poll"]["correct_option_id"]
    q_counts = [0, 0, 0, 0]
    q_counts[correct] = 3
    q_counts[(correct + 1) % 4] = 1
    updates = [
        {"update_id": 50, "poll": {"id": quiz_id, "total_voter_count": 4, "options": [{"voter_count": c} for c in q_counts]}},
        {"update_id": 51, "poll": {"id": fb_id, "total_voter_count": 2, "options": [{"voter_count": 2}] + [{"voter_count": 0}] * (len(fb["poll"]["options"]) - 1)}},
        {"update_id": 52, "poll": {"id": "someone-elses-poll", "options": []}},
    ]
    process_updates(state, updates, "", 0, NOW)
    assert poll_results(state, "2026-10-23", quiz["index"]) == (q_counts, 4)
    report = health_report(state, NOW.date(), full)
    assert "Quiz: 3/4 answers correct (75%)" in report and "Most useful" in report and "2 — ১." in report


def test_channel_gets_every_item_and_its_failure_never_blocks_subscribers(full):
    with_channel = replace(full, telegram=replace(full.telegram, channel_id="@bcs_test_ch"))
    tg = FakeTelegram(subscribers=2)
    r = make(with_channel, tg).run(now=NOW)
    assert r.outcome == "delivered"
    assert {c for c, _ in tg.sent_to} >= {"@bcs_test_ch", "101", "102"} and any(c == "@bcs_test_ch" for c, _ in tg.polls)
    ed = state_of(with_channel)["editions"]["2026-10-23"]
    assert ed["recipients"] == 2 and ed["channel_posted"] is True

    class NotAdmin(FakeTelegram):
        def send_message(self, chat_id, text):
            if str(chat_id) == "@other_ch":
                from app.telegram_delivery import TelegramError

                raise TelegramError("Bad Request: chat not found", permanent=True)
            return super().send_message(chat_id, text)

    other = replace(with_channel, state=replace(with_channel.state, path=str(with_channel.state_path) + ".2"),
                    telegram=replace(with_channel.telegram, channel_id="@other_ch"))
    tg2 = NotAdmin(subscribers=1)
    r2 = make(other, tg2).run(now=NOW)
    assert r2.outcome == "delivered" and any("channel @other_ch" in e for e in r2.errors)
    assert {c for c, _ in tg2.sent_to} >= {"101"}
    assert json.loads(other.state_path.read_text())["editions"]["2026-10-23"]["channel_posted"] is False


def seed_digest(settings, days):
    """Earlier delivered editions, as the digest keeps them."""
    settings.state_path.parent.mkdir(parents=True, exist_ok=True)
    store = StateStore(settings.state_path)
    state = store.load()
    for i, day in enumerate(days):
        story = {"event_id": f"old{i}", "primary_url": f"https://example.com/{i}", "primary_source": "The Daily Star",
                 "analysis": {"headline_bn": f"পুরোনো খবর {i}: বাজেট ঘাটতি {4000 + i} কোটি টাকা", "categories": ["economy"],
                              "score": 80 - i, "syllabus_label": "বাজেট", "likely_question": "?",
                              "key_facts": [{"fact": f"ঘাটতি {4000 + i} কোটি টাকা", "evidence": "x", "prelims": True}],
                              "static_gk": [{"statement": f"জাতীয় রাজস্ব বোর্ড ১৯৭২ সালে গঠিত হয় ({i})"}]}}
        record_digest(state, {"date": day, "edition_date": day}, [story], 40)
    store.save(state)


def test_friday_edition_adds_the_weekly_revision(full):
    seed_digest(full, ["2026-10-19", "2026-10-21", "2026-10-15"])  # the 15th is outside the week
    tg = FakeTelegram()
    make(full, tg).run(now=NOW)  # 2026-10-23 is a Friday
    text = "\n".join(t for c, t in tg.sent_to if c == "101")
    assert "সাপ্তাহিক রিভিশন" in text and "পুরোনো খবর 0" in text and "পুরোনো খবর 1" in text
    assert "পুরোনো খবর 2" not in text
    weekly = state_of(full)["editions"]["2026-10-23"]["weekly"]
    assert weekly["from"] == "2026-10-17" and len(weekly["entries"]) >= 3  # 2 earlier days + today's stories


def test_first_of_month_brings_last_months_pdf(full):
    seed_digest(full, ["2026-11-03", "2026-11-20", "2026-10-30"])
    built = []

    def builder(html):
        built.append(html)
        return FAKE_PDF

    tg = FakeTelegram()
    dec1 = datetime(2026, 12, 1, 2, 0, tzinfo=timezone.utc)
    make(full, tg, pdf=builder).run(now=dec1)
    names = [d[1] for d in tg.documents]
    assert "BCS-Monthly-2026-11.pdf" in names
    monthly_html = next(h for h in built if "মাসিক কারেন্ট অ্যাফেয়ার্স" in h)
    assert "পুরোনো খবর 0" in monthly_html and "পুরোনো খবর 1" in monthly_html and "পুরোনো খবর 2" not in monthly_html


def test_owner_gets_the_weekly_report_once(full):
    tg = FakeTelegram()
    make(full, tg).run(now=NOW)
    owner_msgs = [t for c, t in tg.sent_to if c == OWNER]
    assert len(owner_msgs) == 1 and "Weekly health report" in owner_msgs[0]
    tg2 = FakeTelegram()
    make(full, tg2).run(now=NOW + timedelta(hours=1))  # already delivered; no second report
    assert not [t for c, t in tg2.sent_to if c == OWNER]


def test_crash_notice_goes_only_to_the_owner(monkeypatch, tmp_path):
    from app import __main__ as cli

    sent = []

    class Client:
        def send_message(self, chat_id, text):
            sent.append(str(chat_id))

    monkeypatch.setenv("BCS_STATE_PATH", str(tmp_path / "state.json"))
    monkeypatch.setenv("BCS_OUTPUT_DIR", str(tmp_path / "out"))
    monkeypatch.setenv("TELE_BOT_TOKEN", "123:abc")
    monkeypatch.setenv("TELE_OWNER_CHAT_ID", OWNER)
    monkeypatch.setattr(cli, "make_telegram", lambda settings: Client())
    assert cli.main(["notify-failure"]) == 0
    assert sent == [OWNER]


def test_collect_only_reads_feeds_and_start_messages_without_ai(full):
    class NoAI(MockProvider):
        def generate_raw(self, request):
            raise AssertionError("collect must not call the model")

    tg = FakeTelegram(subscribers=2)
    stats = make(full, tg, provider=NoAI()).collect_only(now=NOW)
    assert stats["new_articles"] > 0 and stats["sources_ok"] >= 1
    state = state_of(full)
    assert state["collection"]["last_at"] and len([s for s in state["subscribers"].values() if s["status"] == "active"]) == 2
    assert tg.sent == [] and len(tg.replies) == 2  # welcomes only
    # The next briefing screens what was collected.
    assert any(e["status"] == "new" for e in state["events"].values())


def test_gate_collects_between_briefings(full):
    def dhaka(h, m=0):
        return datetime(2026, 11, 21, h, m, tzinfo=timezone.utc) - timedelta(hours=6)

    delivered = {"schema_version": 2, "editions": {"2026-11-21": {"date": "2026-11-21", "status": "delivered"}}}
    d = decide(delivered, dhaka(14), full)
    assert d.run is False and d.collect is True and "never collected" in d.reason
    recent = {**delivered, "collection": {"last_at": (dhaka(12)).isoformat()}}
    assert decide(recent, dhaka(14), full).collect is False  # collected 2 h ago
    assert decide(recent, dhaka(16, 30), full).collect is True  # 4.5 h ago
    # Briefing work always wins over collecting.
    building = {"schema_version": 2, "editions": {}}
    d = decide(building, dhaka(8, 10), full)
    assert d.run is True and d.collect is False


def story(eid, score, subject, topic):
    return {"event_id": eid, "score": score, "analysis": {"syllabus_topic": topic, "categories": [subject]}}


def test_ranking_keeps_a_slot_for_science_and_caps_a_subject():
    stories = [story(f"e{i}", 90 - i, "economy", f"t{i}") for i in range(6)] + [story("sci", 70, "science_technology", "sci_space")]
    picked = rank_stories(stories, 65, 5, 1, 3, ("science_technology",))
    ids = [s["event_id"] for s in picked]
    assert "sci" in ids and sum(1 for s in picked if s["analysis"]["categories"] == ["economy"]) == 3
    # No eligible science story: nothing is forced in.
    low = [story(f"e{i}", 90 - i, "economy", f"t{i}") for i in range(4)] + [story("sci", 50, "science_technology", "sci_space")]
    assert "sci" not in [s["event_id"] for s in rank_stories(low, 65, 5, 1, 0, ("science_technology",))]


def test_second_gk_round_fills_stories_left_without(settings):
    def st(eid, h):
        return {"event_id": eid, "primary_url": "https://example.com", "primary_source": "X",
                "analysis": {"headline_bn": h, "what_happened": "", "categories": ["economy"], "key_facts": []}}

    item = {"statement": "জাতিসংঘ ১৯৪৫ সালে প্রতিষ্ঠিত হয়।", "question": "জাতিসংঘ কোন সালে প্রতিষ্ঠিত হয়?", "answer": "১৯৪৫", "answer_en": "1945", "kind": "year"}
    item2 = {"statement": "বিশ্বব্যাংকের সদর দপ্তর ওয়াশিংটন ডিসিতে।", "question": "বিশ্বব্যাংকের সদর দপ্তর কোথায়?", "answer": "ওয়াশিংটন ডিসি", "answer_en": "Washington", "kind": "place"}
    prov = ScriptedProvider([
        {"items": [{**item, "story": "s1"}]}, {"answers": [{"id": "g1", "answer_en": "1945", "sure": True}]},
        {"items": [{**item2, "story": "s1"}]}, {"answers": [{"id": "g1", "answer_en": "Washington", "sure": True}]},
    ])
    out = enrich_static_gk(build_client(settings, prov, sleep=no_sleep), [st("a", "জাতিসংঘের অধিবেশন"), st("b", "বিশ্বব্যাংকের ঋণ")])
    assert [r.task for r in prov.requests] == ["static_gk", "static_gk_check", "static_gk", "static_gk_check"]
    assert "SECOND TRY" in prov.requests[2].prompt and "জাতিসংঘের অধিবেশন" not in prov.requests[2].prompt
    assert set(out.items) == {"a", "b"}


def test_cost_estimate_counts_cached_input_cheaper(make_pipeline):
    pipe = make_pipeline()
    full_price = pipe._estimated_cost({"openai": {"input_tokens": 1_000_000, "cached_input_tokens": 0, "output_tokens": 0}})
    cached = pipe._estimated_cost({"openai": {"input_tokens": 1_000_000, "cached_input_tokens": 800_000, "output_tokens": 0}})
    assert full_price == 0.75 and cached == round(0.2 * 0.75 + 0.8 * 0.075, 4)


def test_disabled_sources_leave_source_health(make_pipeline, settings):
    pipe = make_pipeline(telegram=FakeTelegram())
    pipe.state = pipe.store.load()
    pipe.state["source_health"]["dhakatribune"] = {"consecutive_failures": 2}
    pipe._update_source_health([], NOW)
    assert "dhakatribune" not in pipe.state["source_health"]
