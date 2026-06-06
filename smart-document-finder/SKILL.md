---
name: smart-document-finder
description: "Intelligently searches across SharePoint, OneDrive, email attachments, Teams files, and Data Pools to find and analyze documents. Triggers when the user says 'find the document about', 'where is the file for', 'search for', 'locate', 'pull up', or asks about any specific document, report, presentation, or spreadsheet. Cross-references multiple sources to find the most relevant version."
license: Proprietary
---

# Smart Document Finder

Cross-source document discovery and analysis engine.

## Rules

- Load MEMORY.md to check if the document or its location has been referenced before.
- Search ALL available sources in parallel: SharePoint, OneDrive, email attachments, Data Pools.
- Rank results by relevance, recency, and source reliability.
- When multiple versions exist, highlight the most recent one.
- After finding a document, offer to load it into chat for analysis.
- Save document locations to MEMORY.md for faster future retrieval.

## Workflow

1. **Load memory** to check for known file locations or prior references
2. **Parse the request** to identify: document type, topic, author, date range, project
3. **Search in parallel:**
   - `sharepoint_search` for SharePoint/OneDrive content
   - `onedrive_search_files` for personal OneDrive
   - `outlook_search_emails` for email attachments
   - `datapool_search` for Data Pool content
4. **Compile results:**

```
## 📄 Document Search Results: "{{QUERY}}"

### Best Match
- **File:** [name]
- **Location:** [source + path]
- **Modified:** [date]
- **Why:** [relevance explanation]

### Other Matches
| # | File Name | Source | Modified | Relevance |
|---|-----------|--------|----------|----------|
| 1 | ... | SharePoint | ... | High |
| 2 | ... | OneDrive | ... | Medium |
| 3 | ... | Email attachment | ... | Medium |
```

5. **Ask:** "Would you like me to open and analyze any of these?"
6. **If yes:** Load the file using the appropriate load_file_to_chat tool
7. **Save location** to MEMORY.md for future quick access

## Good fits

- Finding reports, templates, or presentations
- Locating the latest version of a frequently-used document
- Searching for documents shared by a specific person
- Cross-referencing multiple sources for completeness

## Avoid by default

- Loading every search result into chat (expensive on credits)
- Searching when the user has already provided the file
- Downloading large files without confirming first
