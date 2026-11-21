"""Weekly revision and monthly compilation.

Events and articles are pruned after ``state.retention_days``, so every
delivered edition also leaves a compact *digest*: per story its headline,
syllabus topic, must-remember facts and verified static GK. The weekly
revision (added to that weekday's edition) and the monthly PDF (on the 1st)
are built only from these digests, so they never depend on pruned records
and never contain anything that was not already checked and sent.
"""

from __future__ import annotations

import hashlib
from datetime import date, timedelta

from .config import SUBJECTS
from .render import OPTION_LABELS, bn_date, bn_month, bn_num, esc, link

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
FACTS_PER_STORY = 3
GK_PER_STORY = 2


def digest_story(story: dict) -> dict:
    note = story["analysis"]
    facts = [f["fact"] for f in note.get("key_facts", []) if f.get("prelims")] or [f["fact"] for f in note.get("key_facts", [])][:2]
    return {
        "h": note["headline_bn"],
        "topic": note.get("syllabus_label") or note.get("syllabus_topic") or "",
        "subject": (note.get("categories") or [""])[0],
        "score": note.get("score", 0),
        "f": facts[:FACTS_PER_STORY],
        "g": [g["statement"] for g in note.get("static_gk") or []][:GK_PER_STORY],
        "q": note.get("likely_question", ""),
        "u": story.get("primary_url", ""),
        "src": story.get("primary_source", ""),
    }


def record_digest(state: dict, edition: dict, stories: list[dict], keep_days: int) -> None:
    """Store the compact record of a delivered edition and drop old ones."""
    if not stories:
        return
    day = edition.get("edition_date") or edition["date"][:10]
    digests = state.setdefault("digest", {})
    digests[edition["date"]] = {"date": day, "stories": [digest_story(s) for s in stories]}
    cutoff = (date.fromisoformat(day) - timedelta(days=keep_days)).isoformat()
    for key in [k for k, v in digests.items() if (v.get("date") or "") < cutoff]:
        del digests[key]


def entries_between(state: dict, first: date, last: date) -> list[tuple[str, dict]]:
    """(date, story digest) for editions dated first..last, oldest first."""
    out = []
    for _key, d in sorted((state.get("digest") or {}).items(), key=lambda kv: (kv[1].get("date", ""), kv[0])):
        day = d.get("date", "")
        if first.isoformat() <= day <= last.isoformat():
            out.extend((day, s) for s in d.get("stories", []))
    return out


def is_weekly_day(day: date, weekday: str) -> bool:
    return bool(weekday) and WEEKDAYS[day.weekday()] == weekday


def top_entries(entries: list[tuple[str, dict]], n: int) -> list[tuple[str, dict]]:
    """The week's most important stories (by score), shown in date order."""
    best = sorted(entries, key=lambda e: -float(e[1].get("score") or 0))[:n]
    return sorted(best, key=lambda e: e[0])


def weekly_fact_pool(entries: list[tuple[str, dict]], limit: int = 40) -> list[dict]:
    """MCQ facts from the week's digests (already verified when first sent)."""
    pool: list[dict] = []
    for depth in range(max(FACTS_PER_STORY, GK_PER_STORY)):
        for day, s in entries:
            story_id = "w" + hashlib.sha256((day + s["h"]).encode("utf-8")).hexdigest()[:10]
            for basis, items in (("article", s.get("f", [])), ("gk", s.get("g", []))):
                if depth < len(items) and len(pool) < limit:
                    pool.append(
                        {
                            "fact_id": f"f{len(pool) + 1}",
                            "story": s["h"],
                            "fact": items[depth],
                            "evidence": items[depth],
                            "basis": basis,
                            "subject": s.get("subject") if s.get("subject") in SUBJECTS else "bangladesh_affairs",
                            "event_id": story_id,
                            "url": s.get("u", ""),
                            "source_name": s.get("src", ""),
                        }
                    )
    return pool


def render_weekly(entries: list[tuple[str, dict]], first: date, last: date, mcqs: list[dict]) -> list[str]:
    """Telegram sections: the week's must-remember facts, then MCQs with
    hidden answers."""
    if not entries:
        return []
    lines = [
        f"📅 <b>সাপ্তাহিক রিভিশন</b> — {bn_date(first)} থেকে {bn_date(last)}",
        "<i>এই সপ্তাহে পাঠানো সবচেয়ে গুরুত্বপূর্ণ খবরের মনে রাখার তথ্য (প্রতিবেদন থেকে) ও 📚 প্রাসঙ্গিক সাধারণ জ্ঞান (প্রতিবেদনের বাইরে, দুইবার যাচাই করা)।</i>",
    ]
    sections = ["\n".join(lines)]
    for i, (day, s) in enumerate(entries, start=1):
        block = [f"<b>{bn_num(i)}. {esc(s['h'])}</b> <i>({bn_date(date.fromisoformat(day))})</i>"]
        block.extend(f"• {esc(f)}" for f in s.get("f", []))
        block.extend(f"• 📚 {esc(g)}" for g in s.get("g", []))
        sections.append("\n".join(block))
    if mcqs:
        q_lines = [f"<b>🧠 সাপ্তাহিক অনুশীলনী ({bn_num(len(mcqs))}টি MCQ)</b>", ""]
        for i, q in enumerate(mcqs, start=1):
            q_lines.append(f"<b>প্রশ্ন {bn_num(i)}.</b> {esc(q['question'])}")
            q_lines.extend(f"   ({OPTION_LABELS[j]}) {esc(opt)}" for j, opt in enumerate(q["options"]))
            ans = f"({OPTION_LABELS[q['answer_index']]}) {q['options'][q['answer_index']]}"
            q_lines.append(f"   ✅ <tg-spoiler>{esc(ans)}</tg-spoiler>")
            q_lines.append("")
        sections.append("\n".join(q_lines).rstrip())
    return sections


def previous_month(day: date) -> tuple[str, date, date]:
    """("YYYY-MM", first day, last day) of the month before ``day``."""
    last = day.replace(day=1) - timedelta(days=1)
    return last.strftime("%Y-%m"), last.replace(day=1), last


def render_monthly_pdf_html(month: str, entries: list[tuple[str, dict]], css: str) -> str:
    """A printable month of current affairs, grouped by subject."""
    by_subject: dict[str, list[tuple[str, dict]]] = {}
    for day, s in entries:
        by_subject.setdefault(s.get("subject") or "", []).append((day, s))
    body = [
        '<header class="masthead"><div><h1>মাসিক কারেন্ট অ্যাফেয়ার্স সংকলন</h1>'
        f'<div class="meta">{bn_month(month)} · {bn_num(len(entries))}টি খবর</div></div></header>',
        '<div class="notice info">প্রতিদিনের ব্রিফিংয়ে পাঠানো খবরের মনে রাখার তথ্য (প্রতিবেদন থেকে) ও 📚 প্রাসঙ্গিক সাধারণ জ্ঞান '
        "(প্রতিবেদনের বাইরে, দুইবার যাচাই করা)। গুরুত্বপূর্ণ তথ্য মূল সূত্রে মিলিয়ে নিন।</div>",
    ]
    order = [k for k in SUBJECTS if k in by_subject] + [k for k in by_subject if k not in SUBJECTS]
    for subject in order:
        body.append(f'<h2 class="section-title">{esc(SUBJECTS.get(subject, "অন্যান্য"))}</h2>')
        for day, s in by_subject[subject]:
            items = "".join(f"<li>{esc(f)}</li>" for f in s.get("f", [])) + "".join(f"<li>📚 {esc(g)}</li>" for g in s.get("g", []))
            source = f' · {link(s["u"], s.get("src") or "সূত্র")}' if s.get("u") else ""
            body.append(
                f'<section class="story"><h3>{esc(s["h"])}</h3>'
                f'<div class="tags">{bn_date(date.fromisoformat(day))} · {esc(s.get("topic", ""))}{source}</div>'
                f"<ul>{items}</ul></section>"
            )
    csp = "default-src 'none'; style-src 'unsafe-inline'; img-src data:; font-src data:"
    return (
        '<!doctype html><html lang="bn"><head><meta charset="utf-8">'
        f'<meta http-equiv="Content-Security-Policy" content="{csp}">'
        f"<title>মাসিক সংকলন — {bn_month(month)}</title><style>{css}</style></head><body>"
        + "\n".join(body) + "</body></html>"
    )
