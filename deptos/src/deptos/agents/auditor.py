from __future__ import annotations

import re

from deptos.agents.base import Agent
from deptos.models import AgentId, EventKind

BANNED = (
    "production-ready", "live in production", "measurable impact",
    "enterprise-grade", "real-time dashboard", "seamless integration",
)
UNGROUNDED = re.compile(r"\b(studies show|many companies|industry leading|guaranteed)\b", re.I)


class Auditor(Agent):
    id = AgentId.AUDITOR

    def run(self) -> list[str]:
        notes: list[str] = []
        md = self.board.kv.get("briefing_md") or ""
        decisions = self.board.kv.get("decisions") or []
        index = self.board.evidence_index()
        for phrase in BANNED:
            if phrase in md.lower():
                notes.append(f"BANNED CLAIM in briefing: '{phrase}'")
        if UNGROUNDED.search(md):
            notes.append("Unsourced marketing language in briefing.")
        if not self.board.findings:
            notes.append("Packet has zero findings — nothing to release.")
        for dec in decisions:
            eids = dec.get("evidence_ids") or []
            if not eids:
                notes.append(f"Decision has no evidence IDs: {dec.get('statement')}")
            missing = [eid for eid in eids if eid not in index]
            if missing:
                notes.append(f"Decision cites unknown evidence: {missing}")
        recon = self.board.kv.get("recon")
        if recon and "match_rate_pct" in recon:
            claimed = re.search(r"Training match rate:\s+\*\*([0-9.]+)%\*\*", md)
            if claimed and float(claimed.group(1)) != float(recon["match_rate_pct"]):
                notes.append("Briefing match-rate does not match finance tool output.")
        if notes:
            self.board.emit(self.id, EventKind.AUDIT_FAIL, f"{len(notes)} audit failures", {"notes": notes})
        else:
            self.board.emit(self.id, EventKind.AUDIT_PASS, "Packet cleared evidence gate")
        self.board.kv["audit_notes"] = notes
        return notes
