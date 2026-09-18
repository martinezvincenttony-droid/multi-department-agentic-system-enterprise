# 90-second walkthrough for a hiring manager

No API key. No Outlook. One command.

## 1. Run it

```bash
cd deptos
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m deptos
```

You should see `status=ready_for_human`, match rate **50%**, five named gaps, two decisions with `ev_` IDs.

## 2. What to point at

| File | Why it matters |
|---|---|
| `src/deptos/tools/registry.py` | Ops cannot call Finance. Least privilege is code, not a slide. |
| `src/deptos/tools/excel_recon.py` | Real openpyxl join on fixture workbooks. |
| `src/deptos/agents/auditor.py` | Rejects production-ready language and uncited decisions. |
| `src/deptos/runtime.py` | Six seats, one packet. |
| `tests/test_runtime.py` | Replay + tool denial + auditor kill. |
| `sample_briefing.md` | Frozen output if you cannot run Python in the room. |

## 3. What to say

Six seats share a blackboard. Finance reconciles training against a PA matrix. Ops only sees inbox and calendar fixtures. Decisions must cite evidence IDs from this run. The auditor fails the packet if numbers are invented. This is a deterministic demo, not a live mailbox.

## 4. What not to open

Top-level `*-engine/` folders. Those are prompt skills. They are not the runtime.

## 5. If they ask where the LLM is

Routing is deterministic so a reviewer can replay the same packet. The design under review is the tool bus, the packet contract, and the auditor.
