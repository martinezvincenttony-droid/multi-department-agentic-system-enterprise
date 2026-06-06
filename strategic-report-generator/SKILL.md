---
name: strategic-report-generator
description: "Generates professional business reports, executive summaries, action item trackers, meeting minutes, project status reports, and strategic documents in Word/DOCX format. Use when the user needs formatted business documents, reports from data, executive briefings, meeting summaries with action items, project dashboards in document form, or any professional document generation. Also triggers when the user wants to convert analysis or conversation content into a downloadable professional report."
license: Proprietary
---

# Strategic Report Generator

Elite business document and report generation engine for creating professional-grade deliverables.

## Rules

- Use `python-docx` for Word document generation — it is preinstalled.
- Apply consistent professional styling: company-appropriate fonts, colors, spacing.
- Always include: title page, table of contents structure, headers, footers with date and page numbers.
- Use organization branding colors.
- Structure reports with clear hierarchy: Executive Summary → Details → Recommendations → Next Steps.
- Include tables, bullet points, and structured sections for readability.
- Always deliver as a downloadable .docx file.
- For data-driven reports, include relevant charts/tables from the source data.

## Workflow

1. Gather report requirements from the user: type, audience, key content, data sources.
2. Run `scripts/report_generator.py` in the sandbox.
3. The script creates a professionally formatted Word document with:
   - Title page with report name, date, author
   - Executive summary section
   - Detailed content sections
   - Tables and structured data
   - Recommendations and next steps
   - Professional formatting throughout
4. Return the .docx file via download link.

## Report Types

### Executive Summary
- 1-2 page high-level overview
- Key metrics, decisions needed, risks
- Targeted at leadership audience

### Project Status Report
- Current status with RAG indicators (Red/Amber/Green)
- Milestones completed and upcoming
- Risks, issues, and mitigations
- Resource and timeline updates

### Meeting Minutes
- Attendees, date, location
- Discussion points with owners
- Decisions made
- Action items with owners and deadlines
- Next meeting date

### Action Item Tracker
- Comprehensive list of all open actions
- Owner, deadline, status, priority
- Overdue items highlighted
- Summary statistics

### Training Gap Analysis Report
- Current training status overview
- Gap identification by role/area
- Priority recommendations
- Timeline for remediation

### Daily/Weekly Digest
- Summary of key activities
- Upcoming deadlines and milestones
- Items requiring attention
- Quick-reference action list

## Good fits

- "Create a status report for [project]"
- "Generate meeting minutes from our discussion"
- "Build an executive summary of [topic]"
- "Create an action item tracker"
- "Generate a training gap analysis report"
- "Turn this analysis into a professional report"
- "Create a weekly digest document"
- "Build a formal document for [purpose]"

## Avoid by default

- Presentations/slides (use PPTX skill instead)
- Simple text responses that don't need document format
- Excel/spreadsheet outputs (use Excel Power Updater)
- Charts-only outputs (use chart tool)
