# Multi-Department Agentic System Enterprise

**Role: Project Manager.** This is the ops/PM repo — calendar, email, briefings, reports, meeting prep. See `README.md` for the system overview.

## Repo isolation — read this first
This repo is standalone. If this conversation has other repos attached as sources, treat their files as **not part of this project**: don't quote their rules (compliance text, banned-word lists, scripts, memory files) as if they apply here, and don't cite them as precedent for what this repo should do. It's fine to read another attached repo when the user explicitly asks you to check it, but say plainly which repo any fact came from — never blend it into this repo's rules silently. If the user asks why something from another project showed up in this conversation, the answer is that repo was attached as a source here, not that anything merged on disk.

## File architecture
Every top-level folder except `memory/` is one skill: a `SKILL.md` (what it does, when it triggers) plus a `scripts/` folder (the code it runs) and sometimes a `references/` folder (background docs it reads). Nothing else lives at this level on purpose — if a new top-level folder shows up that isn't one of these, it doesn't belong here without an explanation of what it is.

| Path | What it is |
|---|---|
| `auto-memory-engine/` | Saves/loads this repo's own `memory/MEMORY.md`. Fixed 2026-08-22 to stay repo-local — used to point at a shared path outside any repo. |
| `calendar-intelligence-engine/` | Reads calendar, flags scheduling conflicts. |
| `daily-briefing-generator/` | Morning summary pulling email + calendar + Teams. |
| `data-cross-reference-gap-analyzer/` | Finds mismatches between two data sources. |
| `email-command-center/` | Inbox triage and prioritization. |
| `email-triage-responder/` | Drafts replies to routine emails. |
| `excel-power-updater/` | Bulk-edits spreadsheets from instructions. |
| `meeting-prep-autopilot/` | Pulls context before a meeting. |
| `smart-document-finder/` | Locates a document by description instead of exact name. |
| `strategic-report-generator/` | Builds structured written reports. |
| `weekly-status-report-builder/` | Rolls up the week into a status report. |
| `memory/MEMORY.md` | This repo's own persistent notes. Not committed (see `.gitignore`) — regenerates itself on first use. |

**Standing rule:** whenever a file or folder gets added to this repo, this table gets a new row in the same commit. No undocumented additions.
