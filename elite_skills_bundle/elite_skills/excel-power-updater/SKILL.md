---
name: excel-power-updater
description: Elite Excel manipulation engine for updating cells, cross-referencing data across files, adding formula columns, merging workbooks, and applying professional formatting. Use whenever the user wants to update, transform, analyze, or generate Excel files (.xlsx).
license: MIT
---

# Excel Power Updater

## Rules
- Always preserve the original file unless the user explicitly says to overwrite
- Default output naming: `<original>_updated_<YYYYMMDD>.xlsx`
- Confirm sheet names and column headers before bulk updates
- Apply professional formatting (frozen header row, bold headers, auto-width, alternating row colors) to every output workbook
- Never silently drop columns or rows — log any skipped entries
- For formula columns, use Excel-native formulas (not pre-computed values) so the workbook stays dynamic
- Always provide a download link for the resulting file

## Workflow
1. Upload the source Excel file(s) into the sandbox
2. Inspect structure: list sheets, headers, and row counts
3. Confirm intent with the user if the request is ambiguous
4. Run the appropriate operation from `excel_power.py`:
   - `update_cells` — update values matching criteria
   - `add_formula_column` — append calculated columns
   - `cross_reference` — VLOOKUP-style merging across files
   - `merge_workbooks` — consolidate multiple files into one
   - `pivot_summary` — generate aggregated summary sheets
   - `update_training_matrix` — specialized matrix updates with dates
5. Apply professional formatting via `apply_formatting()`
6. Save and return a download link

## Good fits
- "Update the Training Matrix — mark John as certified on Process 5"
- "Cross-reference these two Excel files on Employee ID"
- "Add a column that sums B and C for every row"
- "Merge these 4 monthly reports into one workbook"
- "Make this Excel file look professional"

## Avoid by default
- Do not modify Excel files with macros (.xlsm) — warn the user first
- Do not perform irreversible deletions without explicit confirmation
- Do not auto-format if the user has supplied a styled template — preserve their styling
