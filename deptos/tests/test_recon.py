from __future__ import annotations

from pathlib import Path

from deptos.fixtures import ensure_fixtures
from deptos.tools.excel_recon import reconcile_training


def test_recon_finds_known_gaps(tmp_path: Path):
    fixtures = tmp_path / "fx"
    ensure_fixtures(fixtures)
    result = reconcile_training(str(fixtures / "training.xlsx"), str(fixtures / "requirements.xlsx"), str(tmp_path / "gaps.xlsx"))
    assert result["employees"] == 4
    names = {(g["employee"], g["skill"]) for g in result["gaps"]}
    assert ("Marcus Diaz", "Forklift") in names
    assert ("Marcus Diaz", "OSHA-10") in names
    assert ("Ava Chen", "OSHA-10") in names
    assert ("Jordan Blake", "ISO Internal Audit") in names
    assert result["gap_count"] >= 4
    assert 0 < result["match_rate_pct"] < 100
