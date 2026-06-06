---
name: excel-power-updater
description: "Advanced Excel file manipulation, updating, cross-referencing, formatting, and generation. Use when the user needs to update Excel files, add/remove/modify rows or columns, apply conditional formatting, cross-reference data between sheets or files, merge workbooks, create pivot-style summaries, or generate new Excel files from data. Also use when the user uploads Excel files and wants modifications, formula insertion, or structural changes. Do not trigger for simple read-only questions about Excel data — use the built-in Excel tool for that."
license: Proprietary
---

# Excel Power Updater

Advanced Excel file manipulation engine for updating, transforming, cross-referencing, and generating professional Excel workbooks.

## Rules

- Use `openpyxl` for all Excel operations — it is preinstalled.
- Preserve existing formatting, merged cells, and formulas when updating files unless explicitly told to change them.
- Always create a backup copy before modifying an uploaded file.
- When cross-referencing between files, load both workbooks and match on the key column specified by the user.
- Apply professional formatting by default: bold headers, auto-column-width, borders, alternating row colors.
- For large files (>10,000 rows), use `read_only=True` mode for reading and `write_only=True` for writing when possible.
- Always return the modified file as a downloadable link.
- When adding formulas, use Excel-native formulas (e.g., =SUM, =VLOOKUP) so they remain functional in Excel.

## Workflow

1. Upload the user's Excel file(s) to the sandbox using `sandbox-upload-file`.
2. Run `scripts/excel_updater.py` with appropriate arguments.
3. The script will:
   a. Load the workbook(s)
   b. Perform the requested operations (update, merge, cross-reference, format)
   c. Save the output file
4. Return the output file to the user via `sandbox-download-file`.

### Common Operations

- **Update cells**: Modify specific cells or ranges based on criteria
- **Cross-reference**: Match data between two sheets/files on a key column and pull values
- **Add columns**: Insert calculated columns with formulas or computed values
- **Format**: Apply conditional formatting, styles, colors, borders
- **Merge**: Combine multiple workbooks or sheets into one
- **Filter & Extract**: Create new sheets/files from filtered subsets
- **Pivot Summary**: Create summary tables with aggregations
- **Training Matrix**: Update operator training matrices with new certifications, dates, and status

## Good fits

- Updating training matrices with new employee data or certifications
- Cross-referencing a PA Matrix against a Training Matrix to find gaps
- Merging data from multiple Excel files into a consolidated report
- Adding conditional formatting to highlight overdue items or missing data
- Inserting formulas across ranges (SUM, VLOOKUP, COUNTIF, etc.)
- Restructuring or reformatting messy spreadsheets
- Generating new Excel reports from raw data
- Batch-updating cells based on rules (e.g., update all status fields)

## Avoid by default

- Simple read-only questions about data (use built-in Excel tool)
- Visualization/charting only (use chart tool instead)
- CSV-only operations that don't need Excel formatting
