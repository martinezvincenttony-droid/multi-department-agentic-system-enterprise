---
name: data-cross-reference-gap-analyzer
description: "Cross-references data across multiple Excel files, training matrices, compliance trackers, and PA matrices to identify gaps, mismatches, and discrepancies. Use when the user needs to compare two or more data sources, identify missing training certifications, find compliance gaps, reconcile employee lists, match PA matrix items against training records, audit data completeness, or generate gap analysis reports. Especially relevant for Quality Operator Training Matrix vs PA Matrix comparisons, certification tracking, and regulatory compliance auditing at the organization's facilities."
license: Proprietary
---

# Data Cross-Reference & Gap Analyzer

Elite data reconciliation and gap analysis engine for cross-referencing training matrices, compliance trackers, and operational data across multiple sources.

## Rules

- Use `openpyxl` for all Excel operations — it is preinstalled.
- Use `python-docx` for generating gap analysis reports — it is preinstalled.
- Always upload source files to the sandbox first using `sandbox-upload-file`.
- Present gap analysis results in both: (1) formatted Excel output, and (2) summary in chat.
- Color-code gap severity: RED = critical gap, AMBER = partial gap, GREEN = fully compliant.
- When comparing training matrices, match on employee name/ID AND skill/process area.
- Generate actionable remediation plans with priorities and timelines.
- Always provide statistics: total items, matched, gaps found, compliance percentage.

## Workflow

### Standard Cross-Reference
1. Upload both/all source files to sandbox.
2. Run `scripts/gap_analyzer.py` with source files and key columns.
3. The script will:
   a. Load all source workbooks
   b. Extract and normalize key data
   c. Perform matching/comparison
   d. Identify gaps, mismatches, and discrepancies
   e. Generate color-coded output Excel file
   f. Generate summary statistics
4. Return results: gap report Excel + chat summary.

### Training Matrix vs PA Matrix Analysis
1. Upload Quality Operator Training Matrix and PA Matrix.
2. Script extracts:
   - From Training Matrix: employees, skills, certification status, dates
   - From PA Matrix: required skills/processes per role/area
3. Cross-reference to identify:
   - Employees missing required certifications
   - Expired or soon-to-expire certifications
   - Skills with no trained backup personnel
   - Over-certified areas (resources for redeployment)
4. Generate priority-ranked remediation plan.

### Multi-File Reconciliation
1. Upload all source files.
2. Define primary key(s) for matching across files.
3. Script performs:
   - Full outer join across all sources
   - Identifies records present in one source but missing in others
   - Flags value discrepancies for matching records
   - Generates reconciliation report with drill-down detail

## Gap Severity Classification

| Severity | Criteria | Color | Action |
|----------|----------|-------|--------|
| CRITICAL | Required cert missing, no backup, safety-related | Red #C0392B | Immediate training needed |
| HIGH | Required cert expired <30 days, single person coverage | Orange #E67E22 | Schedule within 2 weeks |
| MEDIUM | Cert expiring in 30-90 days, limited backup | Amber #F39C12 | Plan within 30 days |
| LOW | Nice-to-have cert missing, adequate coverage exists | Yellow #F1C40F | Include in next training cycle |
| COMPLIANT | All requirements met, current certification | Green #27AE60 | No action needed |

## Output Format

The gap analysis Excel output includes:
1. **Summary Dashboard** sheet — high-level metrics, compliance %, charts data
2. **Detailed Gaps** sheet — every gap with severity, owner, recommended action
3. **Compliance Matrix** sheet — employee x skill matrix with RAG status
4. **Remediation Plan** sheet — prioritized action items with timelines
5. **Source Data** sheets — original data preserved for reference

## Good fits

- "Compare my Training Matrix against the PA Matrix"
- "Find training gaps for our operators"
- "Which employees are missing certifications?"
- "Cross-reference these two Excel files"
- "Generate a compliance gap analysis"
- "Who needs retraining before their certs expire?"
- "Reconcile employee lists across these files"
- "Audit our training coverage for [process/area]"
- "Identify single points of failure in our training coverage"
- "Create a remediation plan for training gaps"

## Avoid by default

- Simple data lookups that don't involve comparison (use Excel tool)
- Modifying source data without explicit instruction
- Making assumptions about required certifications — ask the user
- Generating compliance reports without verifying the gap criteria with the user
