---
name: auto-memory-engine
description: "Automatically captures and persists user preferences, decisions, context, and learnings to a MEMORY.md file. Triggers at the end of every significant conversation or when the user shares preferences, makes decisions, or provides context that should be remembered. Also triggers at the START of every conversation to load existing memory. Use this skill whenever the user interacts with the assistant — it runs silently in the background."
license: Proprietary
---

# Auto-Memory Engine

Persistent memory system that learns and improves across all chats by maintaining a structured MEMORY.md file.

## Rules

- ALWAYS read MEMORY.md at the start of any task to recall user context.
- ALWAYS scan the conversation for memorable items before finishing a significant task.
- Memorable items include: preferences, decisions, project context, team info, recurring requests, formatting preferences, tool preferences, communication style, deadlines, and corrections.
- Never store sensitive data (passwords, API keys, financial details, personal health info).
- Append new memories — never overwrite or delete existing ones unless the user explicitly corrects old info.
- Use clear markdown structure with timestamps so memories are searchable.
- Keep each memory entry concise (1-3 lines max).
- Group memories by category for easy scanning.
- The memory file lives at `/workspace/MEMORY.md` in the sandbox.

## Workflow

### At the START of every conversation:
1. Run `scripts/load_memory.py` to read the current MEMORY.md
2. Use the content to personalize your responses
3. Reference relevant memories naturally (don't list them unless asked)

### During the conversation:
1. Watch for statements that reveal preferences, decisions, or context
2. When you detect something worth remembering, note it internally

### At the END of a significant conversation:
1. Run `scripts/save_memory.py` with the new memories as arguments
2. Briefly mention what you saved: "I've noted your preference for [X] — I'll remember that next time."
3. If nothing new was learned, skip silently

### When the user says "show my memory" or "what do you know about me":
1. Run `scripts/load_memory.py` and display the full contents

### When the user says "forget [X]" or "update [X]":
1. Run `scripts/update_memory.py` to modify or remove specific entries

## Memory Categories

- **Identity** — Name, role, department, location, team
- **Preferences** — Communication style, report format, language, tools
- **Projects** — Active projects, deadlines, stakeholders
- **Decisions** — Key decisions made with rationale
- **Patterns** — Recurring requests, common tasks, workflows used
- **Corrections** — Things the user corrected (important to not repeat mistakes)
- **Team Context** — Key people, roles, relationships
- **Technical** — Systems used, data sources, file locations

## Good fits

- Any conversation where the user reveals preferences or context
- End of task completions where decisions were made
- When the user explicitly asks to remember something
- Start of every new chat (to load context)

## Avoid by default

- Storing trivial one-off questions with no future value
- Storing sensitive/confidential data
- Overwriting existing memories without confirmation
- Storing exact file contents (store references instead)
