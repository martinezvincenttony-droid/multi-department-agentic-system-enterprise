from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_memory(path: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {"decisions": [], "preferences": []}
    return json.loads(p.read_text(encoding="utf-8"))


def append_decision(path: str, statement: str, evidence_ids: list[str]) -> dict[str, Any]:
    mem = load_memory(path)
    item = {"statement": statement, "evidence_ids": evidence_ids}
    mem.setdefault("decisions", []).append(item)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(mem, indent=2), encoding="utf-8")
    return item
