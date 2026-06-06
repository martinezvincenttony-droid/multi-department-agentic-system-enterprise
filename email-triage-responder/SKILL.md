---
name: email-triage-responder
description: "Automatically triages unread emails by urgency and category, drafts responses, and flags action items. Triggers when the user says 'check my email', 'triage my inbox', 'handle my emails', 'draft responses', 'email catchup', 'inbox zero', or when the user asks about unread emails. Reduces time spent on email management by 80%."
license: Proprietary
---

# Email Triage & Auto-Responder

Intelligently categorizes emails, drafts responses, and extracts action items.

## Rules

- Load MEMORY.md to understand communication style preferences and key contacts.
- Never send emails automatically — always create drafts for review.
- Categorize every email into: Urgent, Action Required, FYI, Delegate, or Archive.
- Match the user's communication style from memory when drafting responses.
- Extract deadlines and action items from email content.
- Flag emails from VIPs (leadership, key clients) from memory context.
- Save new contacts and their context to MEMORY.md.

## Workflow

1. **Load memory** for communication style, VIP contacts, and email preferences
2. **Fetch unread emails** using outlook_list_emails or outlook_search_emails
3. **Categorize each email:**

```
## 📧 Email Triage Results

### 🔴 Urgent (Respond Today)
| From | Subject | Why Urgent | Suggested Action |
|------|---------|-----------|------------------|

### 🟡 Action Required (This Week)
| From | Subject | Action Needed | Deadline |
|------|---------|--------------|----------|

### 🔵 FYI (No Response Needed)
| From | Subject | Key Takeaway |
|------|---------|-------------|

### ➡️ Delegate
| From | Subject | Suggested Delegate | Why |
|------|---------|-------------------|-----|

### 🗑️ Archive / Low Priority
| From | Subject | Reason |
|------|---------|--------|
```

4. **Draft responses** for urgent and action-required emails
5. **Extract action items** and compile a task list
6. **Present results** and ask user to review drafts before any action
7. **Update memory** with new contacts and context

## Good fits

- Morning email review
- After returning from meetings or PTO
- When inbox count is overwhelming
- End-of-day email cleanup

## Avoid by default

- Sending any email without explicit approval
- Responding to clearly personal emails
- Bulk-deleting emails
- Responding to automated/system notifications
