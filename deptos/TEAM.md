# DeptOS team charter

This is the team. Not a metaphor. Six seats, one packet, one human.

## Seats

| Seat | Name in code | Allowed tools | Forbidden |
|---|---|---|---|
| Chief of Staff | `chief_of_staff` | `append_decision` | recon, inbox, send |
| Finance | `finance` | `reconcile_training` | inbox, email |
| Ops | `ops` | `triage_inbox`, `calendar_brief`, `draft_email` | recon |
| People | `people` | none (reads blackboard) | all tools |
| Strategy | `strategy` | `append_decision` | recon, inbox |
| Auditor | `auditor` | none | all tools |

If a seat needs a new tool, change the allowlist in `runtime.build_registry` and add a test that the other seats still cannot call it.

## Packet contract

Every run must produce findings with IDs, decisions that cite those IDs, a briefing whose match-rate equals Finance, a JSONL trace, and status `ready_for_human` or `blocked_by_auditor`.

No seat may claim production, live Outlook, or measurable customer impact.

## Human gate

`draft_email` writes a draft. `approve=True` only marks `queued_for_human_send`.

## Memory

`runs/team_memory.json` stores prior decisions. Chief reads it at start so the team does not reopen a kill without a new evidence ID.

## How Tony talks to the team

One request. One sentence. Named artifact.
