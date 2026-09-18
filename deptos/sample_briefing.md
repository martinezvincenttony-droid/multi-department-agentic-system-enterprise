# Executive briefing — run_63a723eb9f

_Request:_ Prepare Monday exec briefing: reconcile training vs PA matrix, flag inbox items that block certification.

## Bottom line
- Training match rate: **50.0%** (5/10 required pairs).
- Open certification gaps: **5**.
- Inbox items that block ops: **3** of 4.
- Meetings needing prep: **2**.

## Critical / high findings
- `ev_581a8459fa` **HIGH** Ava Chen missing OSHA-10 — Ava Chen (Warehouse Lead) status=Expired
- `ev_206b36891a` **HIGH** Marcus Diaz missing Forklift — Marcus Diaz (Warehouse Lead) status=In Progress
- `ev_1a59bba555` **HIGH** Marcus Diaz missing OSHA-10 — Marcus Diaz (Warehouse Lead) status=NOT FOUND
- `ev_dd2d7c46aa` **HIGH** Priya Shah missing First Aid — Priya Shah (Quality) status=Missing
- `ev_2ebc9863b2` **HIGH** Jordan Blake missing ISO Internal Audit — Jordan Blake (Quality) status=Not Started
- `ev_73d8456423` **HIGH** Inbox blocker: OSHA-10 recert window closes Friday — from=qa@plant.local priority=URGENT
- `ev_7a30e387d5` **HIGH** Assign Ava Chen a certification close-out — OSHA-10
- `ev_4e1ebe1c6c` **HIGH** Assign Marcus Diaz a certification close-out — Forklift, OSHA-10
- `ev_5e2cb61acc` **HIGH** Assign Priya Shah a certification close-out — First Aid
- `ev_bbdf0fca1a` **HIGH** Assign Jordan Blake a certification close-out — ISO Internal Audit

## Decisions for the human
- `dec_d8f9b4d2d3` Require named owners to close all CRITICAL training gaps before Friday standup.
- `dec_66a7268c10` Do not send vendor replies until the human approves drafts. Queue blockers first.

## Named actions
- **Ava Chen** — Close certification gaps: OSHA-10 (due this Friday)
- **Marcus Diaz** — Close certification gaps: Forklift, OSHA-10 (due this Friday)
- **Priya Shah** — Close certification gaps: First Aid (due this Friday)
- **Jordan Blake** — Close certification gaps: ISO Internal Audit (due this Friday)

## What this packet is not
- Not a live Outlook / Graph integration.
- Not proof of production deployment.
- Claims above are bound to evidence IDs from this run's tools.
