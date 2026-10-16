---
name: daily-briefing-generator
description: "Generates a comprehensive daily briefing by pulling data from Outlook email, calendar, and Teams. Triggers when the user says 'morning briefing', 'daily summary', 'what's on my plate today', 'catch me up', 'what did I miss', 'daily update', or starts a new workday conversation. Also triggers when the user asks about their schedule, unread emails, or pending items."
license: Proprietary
---

# Daily Briefing Generator

Automatically compiles a structured daily briefing from all connected data sources.

## Rules

- Always load MEMORY.md first to personalize the briefing format to user preferences.
- Pull data from all available sources: Outlook emails, calendar, and Teams messages.
- Use the current datetime tool to anchor all time references.
- Prioritize actionable items over informational ones.
- Flag urgent items at the top with ⚠️ emoji.
- Keep the briefing scannable — use headers, bullets, and tables.
- Include a "Recommended Actions" section at the end.
- Save any new context discovered (new projects, deadlines, contacts) to MEMORY.md.

## Workflow

1. **Get current date/time** using the datetime tool
2. **Load memory** — Run `python auto-memory-engine/scripts/load_memory.py` (relative to this repo's root) to recall preferences
3. **Fetch calendar** — Get today's events using calendar_list_events
4. **Fetch recent emails** — Get unread/recent emails from the last 12–24 hours using outlook_list_emails or outlook_search_emails
5. **Fetch Teams activity** — Check recent Teams messages using teams_search_messages for any mentions or important conversations
6. **Compile briefing** in this structure:

```
## 🌅 Daily Briefing — [Date]

### ⚠️ Urgent / Action Required
- [items needing immediate attention]

### 📅 Today's Schedule
| Time | Event | Location | Attendees |
|------|-------|----------|----------|

### 📧 Email Highlights (Last 24h)
- [key emails summarized in 1 line each]
- [flag any requiring response]

### 💬 Teams Activity
- [important messages or mentions]

### ✅ Recommended Actions
1. [prioritized list of things to do today]
```

7. **Save new context** — If new projects, deadlines, or contacts were discovered, save them to MEMORY.md

## Good fits

- Start of workday briefings
- "What did I miss?" after time off
- Weekly planning sessions
- Preparing for a busy day

## Avoid by default

- Don't pull more than 24h of emails unless asked
- Don't read full email bodies unless specifically relevant
- Don't include spam/newsletter emails in the briefing
