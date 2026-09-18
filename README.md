# DeptOS — multi-department agent runtime

**Review `deptos/`.** That is the product.

Six seats (Chief of Staff, Finance, Ops, People, Strategy, Auditor) share a blackboard. Tools are allowlisted. Every decision cites evidence IDs from this run. The auditor rejects ungrounded claims. No API key.

This is a **portfolio demo on fixture plant data**. It is not Outlook, not Microsoft Graph, not a production deployment.

## 90-second demo

```bash
cd deptos
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m deptos
```

You should see `status=ready_for_human`, training match rate **50%**, five named certification gaps, two decisions with `ev_` IDs.

Cannot run Python in the room? Read [`deptos/sample_briefing.md`](deptos/sample_briefing.md).

Walkthrough for the meeting: [`deptos/WALKTHROUGH.md`](deptos/WALKTHROUGH.md)

## What a reviewer should open

| File | Why |
|---|---|
| [`deptos/src/deptos/tools/registry.py`](deptos/src/deptos/tools/registry.py) | Ops cannot call Finance |
| [`deptos/src/deptos/tools/excel_recon.py`](deptos/src/deptos/tools/excel_recon.py) | openpyxl join on training × PA matrix |
| [`deptos/src/deptos/agents/auditor.py`](deptos/src/deptos/agents/auditor.py) | kills “production-ready” and uncited decisions |
| [`deptos/tests/test_runtime.py`](deptos/tests/test_runtime.py) | packet contract + tool denial |

## What not to treat as the product

Top-level `*-engine/` folders are prompt skills from an earlier pass. Leave them closed in the interview.
