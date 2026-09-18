from __future__ import annotations

from pathlib import Path

from deptos.agents.base import Agent
from deptos.models import AgentId, Finding, Severity


class FinanceAgent(Agent):
    id = AgentId.FINANCE

    def run(self, training: Path, requirements: Path, out_dir: Path) -> dict:
        report = out_dir / "training_gaps.xlsx"
        result = self.tools.call(
            self.id,
            "reconcile_training",
            training_path=str(training),
            requirements_path=str(requirements),
            output_path=str(report),
        )
        self.board.kv["recon"] = result
        for gap in result["gaps"]:
            sev = Severity.CRITICAL if gap["severity"] == "CRITICAL" else Severity.HIGH
            self.board.add_finding(Finding(
                agent=self.id, severity=sev,
                title=f"{gap['employee']} missing {gap['skill']}",
                evidence=f"{gap['employee']} ({gap['role']}) status={gap['status']}",
                source_tool="reconcile_training", source_ref=result["report_path"], owner=gap["employee"],
            ))
        self.board.add_finding(Finding(
            agent=self.id, severity=Severity.INFO,
            title=f"Training match rate {result['match_rate_pct']}%",
            evidence=f"{result['compliant']}/{result['required_pairs']} required pairs complete",
            source_tool="reconcile_training", source_ref=result["report_path"],
        ))
        return result
