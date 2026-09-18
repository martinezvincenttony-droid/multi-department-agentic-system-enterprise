# DeptOS — multi-department agent runtime

A **runnable** department team: Chief of Staff routes work, Finance reconciles workbooks, Ops triages a fixture inbox/calendar, People assigns owners, Strategy writes a briefing, Auditor blocks ungrounded claims.

This is a **deterministic demo runtime** with least-privilege tools and an append-only audit log. It is **not** a production Outlook/Excel/Graph integration and it is **not** live at a customer.

```
request
  → Chief of Staff (plan)
  → Finance (training × PA matrix)
  → Ops (inbox + calendar)
  → People (named close-outs)
  → Strategy (briefing + decisions)
  → Auditor (evidence gate)
  → packet.json + briefing.md + jsonl trace
```

## Why this is the interview artifact

Hiring managers can verify all of the following in five minutes:

1. `pytest` passes without API keys.
2. Finance cannot be called by Ops (`ToolDenied` is tested).
3. Every decision cites finding IDs that exist in the same run.
4. The auditor rejects “production-ready” / “live in production” language.
5. A gap workbook is actually written with `openpyxl`.

No model is required. Routing is explicit and logged so a reviewer can replay the graph.

## Run

```bash
cd deptos
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m deptos
```

Outputs land in `runs/`.

Open `dashboard/index.html` and paste `run_*.packet.json` to inspect a run.

## Honest limits

- No Microsoft Graph, no live mailbox, no SSO.
- No LLM in the default path. Adding a model later must not skip the auditor.
- The original skill-markdown folders in this repo are prompts, not this runtime.
