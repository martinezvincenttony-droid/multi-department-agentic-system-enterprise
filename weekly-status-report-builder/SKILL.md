---
name: weekly-status-report-builder
description: "Automatically generates a weekly status report by analyzing the past week's emails, calendar events, Teams activity, and completed tasks. Triggers when the user says 'weekly report', 'weekly summary', 'what did I do this week', 'status update', 'weekly recap', or at the end of the work week. Outputs a professional report ready to send to leadership."
license: Proprietary
---

# Weekly Status Report Builder

Auto-generates a professional weekly status report from all activity data.

## Rules

- Load MEMORY.md to know the user's active projects and reporting preferences.
- Cover the last 7 calendar days unless otherwise specified.
- Pull from calendar, emails, and Teams to reconstruct the week.
- Group accomplishments by project/category from memory.
- Include metrics where possible (emails sent, meetings attended, documents produced).
- Format for leadership readability (executive summary first).
- Save any new project milestones or decisions to MEMORY.md.

## Workflow

1. **Get current date** and calculate the week range (Monday–Friday or last 7 days)
2. **Load memory** for active projects and reporting format preferences
3. **Fetch calendar events** for the entire week
4. **Search emails** sent by the user this week (sentitems) for key accomplishments
5. **Search Teams** for significant conversations and decisions
6. **Compile report:**

```
## 📊 Weekly Status Report
**Period:** {{WEEK_START}} – {{WEEK_END}}
**Prepared by:** {{USER_NAME}}

### Executive Summary
[2-3 sentence overview of the week]

### ✅ Accomplishments
#### Project A
- [what was done]
#### Project B
- [what was done]

### 📅 Meetings & Collaboration
- {{MEETING_COUNT}} meetings attended
- Key meetings: [list important ones]

### ⚠️ Blockers & Risks
- [any issues identified from emails/Teams]

### 🎯 Next Week Priorities
- [inferred from calendar and pending items]

### 📊 Metrics
| Metric | Count |
|--------|-------|
| Meetings attended | {{NUM}} |
| Emails sent | {{NUM}} |
| Documents shared | {{NUM}} |
```

7. **Offer to export** as Word document or email draft
8. **Update memory** with completed milestones

## Good fits

- End-of-week status reporting
- Monthly rollup summaries
- Preparation for 1:1s with manager
- Performance review evidence gathering

## Avoid by default

- Mid-week unless asked
- Including personal calendar items
- Including confidential HR or legal conversations
