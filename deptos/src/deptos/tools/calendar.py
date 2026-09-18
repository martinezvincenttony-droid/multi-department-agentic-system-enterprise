from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_calendar(path: str) -> list[dict[str, Any]]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def brief_week(path: str) -> dict[str, Any]:
    events = load_calendar(path)
    prep = []
    conflicts = []
    by_day: dict[str, list[str]] = {}
    for ev in events:
        day = ev.get("date", "unknown")
        by_day.setdefault(day, []).append(ev.get("title", ""))
        if ev.get("needs_prep"):
            prep.append(ev)
    for day, titles in by_day.items():
        if len(titles) >= 4:
            conflicts.append({"date": day, "count": len(titles), "titles": titles})
    return {"event_count": len(events), "days": by_day, "prep_required": prep, "dense_days": conflicts}
