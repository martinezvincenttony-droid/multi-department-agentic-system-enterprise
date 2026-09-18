from __future__ import annotations

from pathlib import Path

from deptos.agents.base import Agent
from deptos.models import AgentId, Finding, Severity


class OpsAgent(Agent):
    id = AgentId.OPS

    def run(self, inbox: Path, calendar: Path, keywords: list[str]) -> dict:
        triage = self.tools.call(self.id, "triage_inbox", path=str(inbox), keywords=keywords)
        week = self.tools.call(self.id, "calendar_brief", path=str(calendar))
        self.board.kv["inbox"] = triage
        self.board.kv["calendar"] = week
        for item in triage["blockers"]:
            self.board.add_finding(Finding(
                agent=self.id,
                severity=Severity.HIGH if item.get("priority") == "URGENT" else Severity.MEDIUM,
                title=f"Inbox blocker: {item.get('subject')}",
                evidence=f"from={item.get('from')} priority={item.get('priority')} hits={item.get('keyword_hits')}",
                source_tool="triage_inbox", source_ref=item.get("id", "inbox"), owner=item.get("from"),
            ))
        for ev in week["prep_required"]:
            self.board.add_finding(Finding(
                agent=self.id, severity=Severity.MEDIUM,
                title=f"Meeting needs prep: {ev.get('title')}",
                evidence=f"{ev.get('date')} {ev.get('time')} with {', '.join(ev.get('attendees') or [])}",
                source_tool="calendar_brief", source_ref=ev.get("id", "cal"),
            ))
        return {"triage": triage, "calendar": week}
