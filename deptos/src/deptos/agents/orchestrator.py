from __future__ import annotations

from deptos.agents.base import Agent
from deptos.models import AgentId, EventKind, Task


class ChiefOfStaff(Agent):
    id = AgentId.CHIEF

    def plan(self) -> list[Task]:
        text = self.board.request.lower()
        tasks: list[Task] = []
        wants_recon = any(w in text for w in ("reconcil", "training", "gap", "matrix", "excel", "pa "))
        wants_ops = any(w in text for w in ("inbox", "email", "calendar", "meeting", "brief"))
        wants_people = wants_recon or "people" in text or "certif" in text
        wants_strategy = any(w in text for w in ("brief", "status", "report", "exec", "monday", "week"))
        if not any([wants_recon, wants_ops, wants_people, wants_strategy]):
            wants_recon = wants_ops = wants_people = wants_strategy = True
        if wants_recon:
            tasks.append(Task(owner=AgentId.FINANCE, title="Reconcile training matrix vs role requirements"))
        if wants_ops:
            tasks.append(Task(owner=AgentId.OPS, title="Triage inbox and calendar for blockers"))
        if wants_people:
            tasks.append(Task(owner=AgentId.PEOPLE, title="Turn reconciliation gaps into named owners", depends_on=["finance"]))
        if wants_strategy:
            tasks.append(Task(owner=AgentId.STRATEGY, title="Write exec briefing from department findings", depends_on=["ops", "people"]))
        tasks.append(Task(owner=AgentId.AUDITOR, title="Evidence-check the packet before release"))
        for t in tasks:
            self.board.add_task(t)
        self.board.emit(self.id, EventKind.ROUTED, f"Planned {len(tasks)} department tasks")
        return tasks
