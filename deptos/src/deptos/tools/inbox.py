from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PRIORITY = ("URGENT", "ACTION", "FYI", "LOW")


def load_inbox(path: str) -> list[dict[str, Any]]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def triage(path: str, keywords: list[str] | None = None) -> dict[str, Any]:
    items = load_inbox(path)
    keys = [k.lower() for k in (keywords or [])]
    tagged = []
    for item in items:
        blob = f"{item.get('subject','')} {item.get('body','')}".lower()
        hit = [k for k in keys if k in blob] if keys else []
        tagged.append({**item, "keyword_hits": hit, "blocks_ops": bool(hit)})
    by_pri: dict[str, int] = {p: 0 for p in PRIORITY}
    for item in tagged:
        by_pri[item.get("priority", "LOW")] = by_pri.get(item.get("priority", "LOW"), 0) + 1
    blockers = [i for i in tagged if i["blocks_ops"] or i.get("priority") == "URGENT"]
    return {"total": len(tagged), "by_priority": by_pri, "blockers": blockers, "items": tagged}


def draft_email(to: str, subject: str, body: str, approve: bool = False) -> dict[str, Any]:
    draft = {"to": to, "subject": subject, "body": body, "status": "draft"}
    if approve:
        draft["status"] = "queued_for_human_send"
    return draft
