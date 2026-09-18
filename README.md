# Multi-department agentic system

Two layers live in this repository:

1. **`deptos/` — the thing to review.** A runnable Python runtime: Chief of Staff, Finance, Ops, People, Strategy, Auditor. Least-privilege tools, JSONL audit log, pytest, fixture workbooks. No API key required.
2. **Top-level `*-engine/` folders — prompt skills.** Markdown playbooks plus helper scripts. Useful as agent instructions. Not a multi-agent platform by themselves.

Start here:

```bash
cd deptos
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m deptos
```

What a reviewer should see after one command: a briefing whose numbers match the Excel recon tool, decisions that cite evidence IDs, and an auditor that would reject “production-ready” language.

This runtime is a **portfolio demo**. It is not deployed to a customer and it does not talk to live Outlook.

Full notes: [`deptos/README.md`](deptos/README.md)
