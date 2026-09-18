from __future__ import annotations

from pathlib import Path
from typing import Any

from deptos.models import AgentId, Event, EventKind, Finding, Packet, Task, nid, utcnow


class Blackboard:
    """Shared run state + append-only JSONL audit log."""

    def __init__(self, request: str, runs_dir: Path) -> None:
        self.run_id = nid("run")
        self.request = request
        self.created_at = utcnow()
        self.tasks: list[Task] = []
        self.findings: list[Finding] = []
        self.events: list[Event] = []
        self.kv: dict[str, Any] = {}
        self.runs_dir = runs_dir
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.runs_dir / f"{self.run_id}.jsonl"
        self.emit(AgentId.CHIEF, EventKind.TASK_CREATED, f"Run opened: {request[:120]}")

    def emit(
        self,
        agent: AgentId,
        kind: EventKind,
        summary: str,
        payload: dict[str, Any] | None = None,
    ) -> Event:
        ev = Event(agent=agent, kind=kind, summary=summary, payload=payload or {})
        self.events.append(ev)
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(ev.model_dump_json() + "\n")
        return ev

    def add_task(self, task: Task) -> Task:
        self.tasks.append(task)
        self.emit(task.owner, EventKind.ROUTED, f"Task {task.id}: {task.title}")
        return task

    def add_finding(self, finding: Finding) -> Finding:
        self.findings.append(finding)
        self.emit(
            finding.agent,
            EventKind.FINDING,
            f"{finding.severity.value} {finding.title}",
            {"finding_id": finding.id, "source_ref": finding.source_ref},
        )
        return finding

    def evidence_index(self) -> dict[str, Finding]:
        return {f.id: f for f in self.findings}

    def write_packet(self, packet: Packet) -> Path:
        out = self.runs_dir / f"{self.run_id}.packet.json"
        out.write_text(packet.model_dump_json(indent=2), encoding="utf-8")
        md = self.runs_dir / f"{self.run_id}.briefing.md"
        md.write_text(packet.briefing_md, encoding="utf-8")
        return out
