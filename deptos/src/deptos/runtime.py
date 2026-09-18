from __future__ import annotations

from pathlib import Path

from deptos.agents.auditor import Auditor
from deptos.agents.finance import FinanceAgent
from deptos.agents.ops import OpsAgent
from deptos.agents.orchestrator import ChiefOfStaff
from deptos.agents.people import PeopleAgent
from deptos.agents.strategy import StrategyAgent
from deptos.blackboard import Blackboard
from deptos.models import AgentId, Decision, EventKind, Packet
from deptos.tools import calendar as calendar_tool
from deptos.tools import excel_recon, inbox, memory
from deptos.tools.registry import ToolRegistry


def build_registry(board: Blackboard) -> ToolRegistry:
    reg = ToolRegistry(board)
    reg.register("reconcile_training", excel_recon.reconcile_training, allowed=[AgentId.FINANCE])
    reg.register("triage_inbox", inbox.triage, allowed=[AgentId.OPS])
    reg.register("draft_email", inbox.draft_email, allowed=[AgentId.OPS])
    reg.register("calendar_brief", calendar_tool.brief_week, allowed=[AgentId.OPS])
    reg.register("append_decision", memory.append_decision, allowed=[AgentId.STRATEGY, AgentId.CHIEF])
    return reg


class DeptOS:
    def __init__(self, fixtures: Path, runs_dir: Path) -> None:
        self.fixtures = fixtures
        self.runs_dir = runs_dir

    def handle(self, request: str) -> Packet:
        board = Blackboard(request, self.runs_dir)
        tools = build_registry(board)
        ChiefOfStaff(board, tools).plan()
        keywords = ["training", "certif", "osha", "forklift", "audit", "matrix"]
        FinanceAgent(board, tools).run(
            self.fixtures / "training.xlsx",
            self.fixtures / "requirements.xlsx",
            self.runs_dir,
        )
        OpsAgent(board, tools).run(self.fixtures / "inbox.json", self.fixtures / "calendar.json", keywords)
        PeopleAgent(board, tools).run()
        StrategyAgent(board, tools).run()
        notes = Auditor(board, tools).run()
        packet = Packet(
            run_id=board.run_id,
            request=request,
            status="blocked_by_auditor" if notes else "ready_for_human",
            findings=board.findings,
            decisions=[Decision(**d) for d in board.kv.get("decisions") or []],
            briefing_md=board.kv.get("briefing_md") or "",
            audit_notes=notes,
            events=board.events,
        )
        board.emit(AgentId.CHIEF, EventKind.PACKET_READY, f"status={packet.status}")
        board.write_packet(packet)
        return packet
