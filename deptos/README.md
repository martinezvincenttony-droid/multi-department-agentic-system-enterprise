# DeptOS

Deterministic multi-department agent runtime for a plant-ops Monday brief.

Six seats share a blackboard. Tools are allowlisted. Every decision cites evidence IDs from this run. The auditor rejects ungrounded claims.

This is a **portfolio demo on fixture data**. Not Outlook. Not Graph. Not production.

## Run (no API key)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m deptos
```

Expected: `status=ready_for_human`, training match rate 50%, five named gaps, two decisions with `ev_` IDs.

Frozen sample: [`sample_briefing.md`](sample_briefing.md)

Manager script: [`WALKTHROUGH.md`](WALKTHROUGH.md) · charter: [`TEAM.md`](TEAM.md)
