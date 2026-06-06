---
name: data-cross-reference-gap-analyzer
description: Multi-file reconciliation and compliance gap analysis engine. Cross-references datasets (e.g., Training Matrix vs PA Matrix), classifies gaps by severity, and produces color-coded Excel reports with summary dashboard, detailed gaps, and remediation plan.
license: MIT
---

# Data Cross-Reference & Gap Analyzer

## Rules
- Severity scale: CRITICAL (compliance-breaking) → HIGH → MEDIUM → LOW → COMPLIANT
- Always produce a 3-sheet output: Summary Dashboard, Detailed Gaps, Remediation Plan
- Color-code rows: Red (Critical), Orange (High), Yellow (Medium), Light Blue (Low), Green (Compliant)
- Identify single-points-of-failure (only one person certified for a critical process)
- Flag expired certifications (>1 year old by default)
- Always provide a summary count and top-3 priority actions

## Workflow
1. Receive primary file (e.g., Training Matrix) and reference file (e.g., PA Matrix)
2. Identify the join key (usually employee ID or process name)
3. Run `cross_reference_files()` to find mismatches
4. Run `classify_gaps()` to assign severity
5. Run `build_remediation_plan()` to generate action items
6. Run `export_gap_report()` to produce the Excel output
7. Return file path + executive summary

## Good fits
- "Cross-reference my Training Matrix against the PA Matrix"
- "Find compliance gaps between these two files"
- "Who's expired on their certifications?"
- "Generate a gap analysis report"
- "Where do I have single-point-of-failure risks?"

## Avoid by default
- Do not auto-classify severity without confirming what 'critical' means in context
- Do not name-and-shame individuals — focus on systemic gaps
- Do not delete or modify source files
