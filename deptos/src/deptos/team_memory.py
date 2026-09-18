from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def path_for(runs_dir: Path) -> Path:
    return runs_dir / "team_memory.json"


def load(runs_dir: Path) -> dict[str, Any]:
    p = path_for(runs_dir)
    if not p.exists():
        return {"runs": [], "open_actions": [], "closed_evidence": []}
    return json.loads(p.read_text(encoding="utf-8"))


def save(runs_dir: Path, packet_summary: dict[str, Any]) -> dict[str, Any]:
    mem = load(runs_dir)
    mem.setdefault("runs", []).append(packet_summary)
    mem["runs"] = mem["runs"][-20:]
    mem["open_actions"] = packet_summary.get("actions") or []
    mem.setdefault("closed_evidence", [])
    path_for(runs_dir).write_text(json.dumps(mem, indent=2), encoding="utf-8")
    return mem
