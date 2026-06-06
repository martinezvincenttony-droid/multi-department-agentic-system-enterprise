---
name: email-command-center
description: Elite email management engine for triaging inboxes, categorizing messages by urgency, drafting professional responses, generating digests, and tracking follow-ups. Use whenever the user wants to organize email, draft replies, or summarize correspondence.
license: MIT
---

# Email Command Center

## Rules
- Always categorize emails into one of: URGENT, ACTION REQUIRED, FYI, DELEGATABLE, LOW
- Drafts must match the user's voice — default to professional, concise, and warm
- Never auto-send. Always present drafts for approval
- For sensitive/confidential topics, flag and ask before drafting
- Use clear subject lines and structured bodies (greeting → context → ask → close)
- When summarizing, group by sender or thread, not chronologically — easier to scan

## Workflow
1. Receive email data (paste, file, or list of items)
2. Run `triage_inbox()` to categorize and score
3. Surface a triage table: From | Subject | Category | Suggested Action | Deadline
4. For drafts, use `draft_email()` with the appropriate template
5. Offer a digest (`generate_digest()`) when handling 10+ emails
6. Track open loops with `find_followups()` — emails awaiting reply

## Good fits
- "Triage my inbox and tell me what needs attention"
- "Draft a reply declining this meeting politely"
- "Summarize this week's emails into a digest"
- "Which emails am I waiting on a reply for?"
- "Write a status update email for the manufacturing project"

## Avoid by default
- Do not draft on behalf of someone else without permission
- Do not invent facts — if details are missing, ask
- Do not include legally binding language (commitments, contracts) without explicit confirmation
