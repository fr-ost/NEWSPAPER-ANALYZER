"""Stage E: configurable relevance scoring rubric.

The weights are starting heuristics, not validated predictions of exam
questions. The score supports selection; it never replaces evidence checks.
"""

from __future__ import annotations

from .config import SCORE_CRITERIA


class ScoreError(ValueError):
    pass


def validate_criteria(raw: object) -> dict[str, float]:
    """Validate model-provided 0-10 sub-scores. Raises ScoreError if malformed."""
    if not isinstance(raw, dict):
        raise ScoreError("scores must be an object")
    out: dict[str, float] = {}
    for key in SCORE_CRITERIA:
        value = raw.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ScoreError(f"score {key} missing or not a number")
        if not 0 <= value <= 10:
            raise ScoreError(f"score {key}={value} outside 0-10")
        out[key] = float(value)
    return out


def weighted_score(criteria: dict[str, float], weights: dict[str, float]) -> float:
    """Weighted total on a 0-100 scale, rounded to one decimal."""
    total = sum(weights[k] * criteria[k] for k in SCORE_CRITERIA)
    return round(total * 10, 1)


def _subject(story: dict) -> str | None:
    cats = (story.get("analysis") or {}).get("categories") or []
    return cats[0] if cats else None  # the syllabus topic's subject comes first


def rank_stories(
    stories: list[dict],
    min_score: float,
    max_stories: int,
    max_per_topic: int | None = None,
    max_per_subject: int | None = None,
    reserve_subjects: tuple[str, ...] = (),
) -> list[dict]:
    """Pick the best stories. Never pads: only those meeting ``min_score``.

    ``max_per_topic`` keeps the edition diverse: once a syllabus topic has
    that many stories, lower-scoring stories on the same topic are skipped.
    ``max_per_subject`` does the same per subject (economy, international
    affairs, ...). For each subject in ``reserve_subjects`` that would
    otherwise be missing, its best eligible story takes a slot (the
    lowest-scoring pick of a subject that has more than one story makes way).
    """
    eligible = [s for s in stories if s.get("score", 0) >= min_score]
    eligible.sort(key=lambda s: (-s["score"], s.get("published_at") or "", s["event_id"]))
    picked: list[dict] = []
    per_topic: dict[str, int] = {}
    per_subject: dict[str, int] = {}

    def fits(story: dict) -> bool:
        topic, subject = (story.get("analysis") or {}).get("syllabus_topic"), _subject(story)
        if max_per_topic and topic and per_topic.get(topic, 0) >= max_per_topic:
            return False
        return not (max_per_subject and subject and per_subject.get(subject, 0) >= max_per_subject)

    def take(story: dict) -> None:
        topic, subject = (story.get("analysis") or {}).get("syllabus_topic"), _subject(story)
        picked.append(story)
        if topic:
            per_topic[topic] = per_topic.get(topic, 0) + 1
        if subject:
            per_subject[subject] = per_subject.get(subject, 0) + 1

    for story in eligible:
        if len(picked) >= max_stories:
            break
        if fits(story):
            take(story)

    for reserved in reserve_subjects:
        if per_subject.get(reserved):
            continue
        candidate = next((s for s in eligible if s not in picked and _subject(s) == reserved and fits(s)), None)
        if candidate is None:
            continue
        if len(picked) >= max_stories:
            removable = [s for s in picked if per_subject.get(_subject(s), 0) > 1 and _subject(s) not in reserve_subjects]
            if not removable:
                continue
            out = min(removable, key=lambda s: (s["score"], s["event_id"]))
            picked.remove(out)
            o_topic, o_subject = (out.get("analysis") or {}).get("syllabus_topic"), _subject(out)
            if o_topic:
                per_topic[o_topic] -= 1
            if o_subject:
                per_subject[o_subject] -= 1
        take(candidate)
    picked.sort(key=lambda s: (-s["score"], s.get("published_at") or "", s["event_id"]))
    return picked
