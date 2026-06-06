---
name: email-command-center
description: "Advanced email management, organization, draft creation, triage, summarization, and batch processing. Use when the user needs to organize their inbox, create professional email drafts, triage and prioritize emails, generate email summaries or digests, batch-process emails by category, create follow-up reminders, or manage email workflows. Also use when the user asks to draft replies, compose professional emails, create email templates, or organize emails by project/priority/sender. Triggers on any email productivity or management request."
license: Proprietary
---

# Email Command Center

Elite email management engine for organizing, triaging, drafting, summarizing, and automating email workflows.

## Rules

- Always use Outlook tools (outlook_list_emails, outlook_search_emails, outlook_create_draft) for email operations.
- When triaging, categorize emails into: URGENT, ACTION REQUIRED, FYI/INFORMATIONAL, DELEGATABLE, LOW PRIORITY.
- For draft creation, always use professional formatting with proper greeting, body structure, and closing.
- Preserve the original language of emails when summarizing — do not translate unless asked.
- When organizing, group by: sender, project/topic, urgency, date range, or action type.
- For batch operations, process all matching emails and provide a structured report.
- Always ask for user approval before sending any email — create as draft first.
- Include a confidence indicator when auto-categorizing priority.

## Workflow

### Email Triage & Organization
1. Use `outlook_list_emails` or `outlook_search_emails` to retrieve emails.
2. Analyze each email for: sender importance, keywords, deadlines, action items.
3. Categorize into priority tiers with reasoning.
4. Present organized summary table with recommended actions.

### Professional Draft Creation
1. Gather context: recipient, purpose, tone, key points.
2. Generate draft using professional email framework:
   - **Subject line**: Clear, actionable, specific
   - **Opening**: Appropriate greeting + context setter
   - **Body**: Structured with bullet points for clarity
   - **Call to Action**: Specific next steps with deadlines
   - **Closing**: Professional sign-off
3. Create draft via `outlook_create_draft`.
4. Present draft to user for review before any send action.

### Email Digest/Summary
1. Retrieve emails from specified time range or folder.
2. Group by conversation thread or topic.
3. Extract key information: decisions, action items, deadlines, FYIs.
4. Generate structured digest with priority indicators.

### Follow-up Tracking
1. Identify emails requiring follow-up.
2. Categorize by: awaiting response, action needed, deadline approaching.
3. Generate follow-up reminder list with suggested actions.
4. Optionally create follow-up draft emails.

## Email Templates

### Professional Reply Template
```
Subject: RE: [Original Subject]

[Greeting],

Thank you for your [email/message/update] regarding [topic].

[Body - address each point raised]

[Next steps / Call to action]

[Professional closing],
[Name]
```

### Status Update Template
```
Subject: Status Update: [Project/Topic] - [Date]

[Greeting],

Please find below the status update for [project/topic]:

**Completed:**
- [Item 1]
- [Item 2]

**In Progress:**
- [Item 1] - Expected completion: [Date]

**Blockers/Risks:**
- [Item if any]

**Next Steps:**
- [Action item] - [Owner] - [Deadline]

Please let me know if you have any questions.

[Closing],
[Name]
```

### Meeting Request Template
```
Subject: Meeting Request: [Topic] - [Proposed Date/Time]

[Greeting],

I would like to schedule a meeting to discuss [topic].

**Purpose:** [Brief description]
**Proposed Time:** [Date, Time, Duration]
**Attendees:** [List]
**Agenda:**
1. [Item 1]
2. [Item 2]
3. [Item 3]

Please confirm your availability.

[Closing],
[Name]
```

## Good fits

- "Organize my inbox" or "Triage my emails"
- "Draft a professional email to [person] about [topic]"
- "Summarize my emails from this week"
- "What emails need my immediate attention?"
- "Create a follow-up email for [topic]"
- "Draft a status update email"
- "Batch-categorize my unread emails"
- "Create an email digest for my manager"
- "Help me respond to this email professionally"
- "Find all emails about [project] and summarize action items"

## Avoid by default

- Sending emails without explicit user approval
- Modifying or deleting emails without confirmation
- Accessing emails from other users' mailboxes
- Translating email content unless specifically requested
