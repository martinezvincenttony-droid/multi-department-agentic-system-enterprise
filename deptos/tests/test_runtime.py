from __future__ import annotations

from pathlib import Path

import pytest

from deptos.blackboard import Blackboard
from deptos.fixtures import ensure_fixtures
from deptos.models import AgentId
from deptos.runtime import DeptOS, build_registry
from deptos.tools.registry import ToolDenied


@pytest.fixture()
def env(tmp_path: Path) -> tuple[Path, Path]:
    fixtures = tmp_path / "fixtures"
    runs = tmp_path / "runs"
    ensure_fixtures(fixtures)
    return fixtures, runs


def test_full_run_produces_grounded_packet(env):
    fixtures, runs = env
    packet = DeptOS(fixtures, runs).handle(
        "Prepare Monday exec briefing: reconcile training vs PA matrix and flag inbox certification blockers."
    )
    assert packet.status == "ready_for_human"
    assert packet.findings
    assert packet.decisions
    ev_ids = {f.id for f in packet.findings}
    for dec in packet.decisions:
        assert dec.evidence_ids
        assert set(dec.evidence_ids) <= ev_ids
    assert "Training match rate" in packet.briefing_md
    assert "production-ready" not in packet.briefing_md.lower()
    assert (runs / f"{packet.run_id}.jsonl").exists()
    assert list(runs.glob("*.xlsx"))


def test_ops_cannot_call_finance_tool(env):
    fixtures, runs = env
    board = Blackboard("x", runs)
    tools = build_registry(board)
    with pytest.raises(ToolDenied):
        tools.call(AgentId.OPS, "reconcile_training", training_path="a", requirements_path="b", output_path="c")
    assert "tool_denied" in [e.kind.value for e in board.events]


def test_auditor_kills_ungrounded_marketing(env):
    from deptos.agents.auditor import Auditor

    fixtures, runs = env
    board = Blackboard("brief", runs)
    board.kv["briefing_md"] = "This is production-ready and live in production. Match rate 12%."
    board.kv["decisions"] = [{"statement": "Ship it", "evidence_ids": [], "owner": "me"}]
    notes = Auditor(board, build_registry(board)).run()
    assert any("BANNED" in n for n in notes)
    assert any("no evidence" in n.lower() for n in notes)


def test_second_run_writes_team_memory(env):
    fixtures, runs = env
    first = DeptOS(fixtures, runs).handle("weekly status brief reconcile training")
    second = DeptOS(fixtures, runs).handle("weekly status brief reconcile training")
    assert (runs / "team_memory.json").exists()
    assert "Memory from last run" in second.briefing_md
    assert first.run_id in second.briefing_md
