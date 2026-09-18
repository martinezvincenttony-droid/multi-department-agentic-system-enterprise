from __future__ import annotations

from deptos.agents.base import Agent
from deptos.models import AgentId, Decision, Finding, Severity


class StrategyAgent(Agent):
    id = AgentId.STRATEGY

    def run(self) -> str:
        recon = self.board.kv.get("recon") or {}
        inbox = self.board.kv.get("inbox") or {}
        cal = self.board.kv.get("calendar") or {}
        actions = self.board.kv.get("people_actions") or []
        findings = self.board.findings

        crit = [f for f in findings if f.severity.value == "CRITICAL"]
        high = [f for f in findings if f.severity.value == "HIGH"]

        lines = [
            f"# Executive briefing — {self.board.run_id}",
            "",
            f"_Request:_ {self.board.request}",
            "",
            "## Bottom line",
            f"- Training match rate: **{recon.get('match_rate_pct', 'n/a')}%** "
            f"({recon.get('compliant', 0)}/{recon.get('required_pairs', 0)} required pairs).",
            f"- Open certification gaps: **{recon.get('gap_count', 0)}**.",
            f"- Inbox items that block ops: **{len(inbox.get('blockers') or [])}** "
            f"of {inbox.get('total', 0)}.",
            f"- Meetings needing prep: **{len(cal.get('prep_required') or [])}**.",
            "",
            "## Critical / high findings",
        ]
        for f in (crit + high)[:12]:
            lines.append(f"- `{f.id}` **{f.severity.value}** {f.title} — {f.evidence}")
        if not (crit or high):
            lines.append("- None.")

        lines += ["", "## Decisions for the human"]
        decisions: list[Decision] = []
        ev_ids = [f.id for f in findings if f.severity.value in {"CRITICAL", "HIGH"}]
        if recon.get("gap_count"):
            dec = Decision(
                statement="Require named owners to close all CRITICAL training gaps before Friday standup.",
                evidence_ids=ev_ids[:8],
                owner="People + department leads",
                due="Friday",
            )
            decisions.append(dec)
            lines.append(f"- `{dec.id}` {dec.statement} (evidence: {', '.join(dec.evidence_ids) or 'none'})")
        if inbox.get("blockers"):
            dec = Decision(
                statement="Do not send vendor replies until the human approves drafts. Queue blockers first.",
                evidence_ids=[f.id for f in findings if f.source_tool == "triage_inbox"][:6],
                owner="Ops",
            )
            decisions.append(dec)
            lines.append(f"- `{dec.id}` {dec.statement}")

        lines += ["", "## Named actions"]
        for a in actions:
            lines.append(f"- **{a['owner']}** — {a['action']} (due {a['due']})")
        if not actions:
            lines.append("- No people actions.")

        prior = self.board.kv.get("prior_memory") or {}
        prior_runs = prior.get("runs") or []
        if prior_runs:
            last = prior_runs[-1]
            lines += [
                "",
                "## Memory from last run",
                (
                    f"- Last run `{last.get('run_id')}` status={last.get('status')} "
                    f"match={last.get('match_rate_pct')}% gaps={last.get('gap_count')}."
                ),
                "- Do not reopen a kill unless new evidence IDs appear in this packet.",
            ]
        lines += [
            "",
            "## What this packet is not",
            "- Not a live Outlook / Graph integration.
            "- Not proof of production deployment.",
            "- Claims above are bound to evidence IDs from this run's tools.",
        ]
        md = "\n".join(lines) + "\n"
        self.board.kv["briefing_md"] = md
        self.board.kv["decisions"] = [d.model_dump() for d in decisions]
        self.board.add_finding(
            Finding(
                agent=self.id,
                severity=Severity.INFO,
                title="Briefing drafted",
                evidence=f"{len(decisions)} decisions, {len(findings)} findings cited",
                source_tool="blackboard",
                source_ref=self.board.run_id,
            )
        )
        return md
