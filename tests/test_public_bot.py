"""Public bot: anyone can join, no subscriber limit, delivery scales to many."""

import json
from dataclasses import replace

from app.config import load_settings
from app.subscribers import MSG_WELCOME, process_updates

from .conftest import NOW, FakeTelegram, start_update


def test_default_settings_are_public(settings):
    assert settings.telegram.max_subscribers == 0 and settings.telegram.require_invite_code is False
    # A leftover BOT_INVITE_CODE secret is ignored while the bot is public...
    public = load_settings(env={"BOT_INVITE_CODE": "SELF-2026-old"})
    assert public.invite_code == ""
    # ...and enforced again if the owner turns the invite requirement back on.
    private = replace(public, telegram=replace(public.telegram, require_invite_code=True))
    assert private.invite_code == "SELF-2026-old"


def test_anyone_can_join_with_plain_start_and_there_is_no_limit():
    state = {}
    updates = [start_update(i, 1000 + i) for i in range(1, 251)]
    updates.append(start_update(251, 9999, text="/start SELF-2026"))  # an old invite link still works
    summary, replies = process_updates(state, updates, invite_code="", max_subscribers=0, now=NOW)
    assert len(summary.added) == 251 and summary.rejected == 0
    assert set(replies.values()) == {MSG_WELCOME}


def test_many_subscribers_get_every_message_in_order_and_one_pdf_upload(make_pipeline, settings):
    fast = replace(settings, telegram=replace(settings.telegram, max_messages_per_second=30))
    tg = FakeTelegram(subscribers=40, gone={"105"})
    pipe = make_pipeline(telegram=tg, pdf_builder=lambda html: b"%PDF-1.4 fake")
    pipe.s = fast
    r = pipe.run(now=NOW)
    assert r.outcome == "delivered"
    edition = json.loads(settings.state_path.read_text())["editions"]["2026-10-23"]
    n = len(edition["chunks"])
    per_chat: dict[str, list[str]] = {}
    for chat, text in tg.sent_to:
        per_chat.setdefault(chat, []).append(text)
    assert len(per_chat) == 39 and "105" not in per_chat  # the blocked one is skipped and removed
    first = next(iter(per_chat.values()))
    assert len(first) == n and all(v == first for v in per_chat.values())  # complete and in order for everyone
    assert len(tg.documents) == 39 and len(tg.reused) == 38  # the PDF was uploaded once
    assert edition["recipients"] == 39
    subs = json.loads(settings.state_path.read_text())["subscribers"]
    assert subs["105"]["status"] == "inactive"
