---
name: strategic-report-generator
description: Elite document creation engine for executive summaries, project status reports with RAG indicators, meeting minutes, action item trackers, and weekly digests. Produces polished Word (.docx) documents ready for leadership.
license: MIT
---

# Strategic Report Generator

## Rules
- Every document has: title page section (or banner), executive summary, body, next steps
- Use RAG indicators (🟢 Green / 🟡 Amber / 🔴 Red) for status reports
- Action items always include: Owner, Due Date, Status
- Default font: Calibri 11; headings: Calibri 14 bold, navy color
- All documents include the generation date and a footer
- Always return a download link to the resulting .docx file

## Workflow
1. Identify report type (executive_summary, status_report, minutes, action_tracker, weekly_digest)
2. Gather inputs: title, audience, content sections, action items
3. Run the matching function in `report_generator.py`
4. Save to `/workspace/<report_name>_<date>.docx`
5. Return file path + a brief summary of what was produced

## Good fits
- "Generate an executive summary for the Q2 manufacturing review"
- "Create a project status report — current status amber, blockers X and Y"
- "Turn these meeting notes into formal minutes"
- "Build an action item tracker from this list"
- "Produce a weekly digest of these accomplishments"

## Avoid by default
- Do not invent metrics or numbers — leave placeholders if data is missing
- Do not include confidential names without confirmation
- Do not exceed 2 pages for executive summaries (force prioritization)
