from __future__ import annotations

from deptos.agents.base import Agent
from deptos.models import AgentId, Finding, Severity


class PeopleAgent(Agent):
    id = AgentId.PEOPLE

    def run(self) -> dict:
        recon = self.board.kv.get("recon") or {}
        gaps = recon.get("gaps") or []
        by_owner: dict[str, list[str]] = {}
        for g in gaps:
            by_owner.setdefault(g["employee"], []).append(g["skill"])
        actions = []
        for emp, skills in by_owner.items():
            actions.append({"owner": emp, "action": f"Close certification gaps: {', '.join(skills)}", "due": "this Friday"})
            self.board.add_finding(Finding(
                agent=self.id, severity=Severity.HIGH,
                title=f"Assign {emp} a certification close-out",
                evidence=f"{len(skills)} open skill(s): {', '.join(skills)}",
                source_tool="reconcile_training", source_ref=recon.get("report_path", "recon"), owner=emp,
            ))
        self.board.kv["people_actions"] = actions
        return {"actions": actions, "owners": list(by_owner)}
