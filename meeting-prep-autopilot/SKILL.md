---
name: meeting-prep-autopilot
description: "Automatically prepares for upcoming meetings by gathering relevant emails, documents, past notes, and attendee context. Triggers when the user says 'prep for my meeting', 'get ready for [meeting name]', 'what do I need for my next meeting', 'meeting prep', or when the user asks about a specific upcoming calendar event. Also triggers proactively during daily briefings for important meetings."
license: Proprietary
---

# Meeting Prep Autopilot

Automatically gathers all context needed before a meeting so the user walks in fully prepared.

## Rules

- Load MEMORY.md first to check for any prior context about the meeting topic or attendees.
- Pull the meeting details from the calendar first to understand topic, attendees, and agenda.
- Search emails for recent threads with the attendees or about the meeting topic.
- Search Teams for relevant recent conversations.
- Search SharePoint/OneDrive for related documents.
- Compile everything into a concise, actionable prep brief.
- Save any new attendee/project context to MEMORY.md.

## Workflow

1. **Load memory** for prior context on the topic/attendees
2. **Get meeting details** from calendar_get_event or calendar_list_events
3. **Identify attendees** and search memory for relationship context
4. **Search recent emails** from/to attendees in the last 7 days
5. **Search Teams** for related conversations
6. **Search SharePoint** for related documents if the topic matches known projects
7. **Compile prep brief:**

```
## 🎯 Meeting Prep: {{MEETING_TITLE}}
**When:** {{DATE_TIME}}
**Where:** {{LOCATION}}
**Duration:** {{DURATION}}

### 👥 Attendees
| Name | Role/Context | Recent Interaction |
|------|-------------|-------------------|

### 📝 Agenda / Expected Topics
- [from meeting body or inferred from recent context]

### 📧 Relevant Recent Emails
- [summarized email threads with attendees]

### 📄 Related Documents
- [any SharePoint/OneDrive docs found]

### 🧠 What You Should Know
- [key context from memory about this topic/these people]

### 💬 Suggested Talking Points
1. [based on recent email threads and context]
```

8. **Update memory** with any new attendee or project information discovered

## Good fits

- Preparing for important meetings with external stakeholders
- Catching up on context for recurring meetings
- Meetings with people the user hasn't interacted with recently
- Complex cross-functional meetings

## Avoid by default

- Quick 1:1 check-ins that don't need prep
- All-hands or company-wide broadcasts
- Meetings the user is organizing (they already have context)
