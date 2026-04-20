# `create_technical_document.py`

## Overview

`scripts/tooling/technical_documents/create_technical_document.py` creates a
new timestamped technical document under `doc/technical/` and registers it in
the two canonical technical-document indices:

- the day-local `doc/technical/YYYY-MM/YYYY-MM-DD/README.md`;
- the top-level `doc/README.md`.

The helper reads the real local system time at runtime, so the generated file
name stays aligned with the repository rule that technical documents must use
the actual machine timestamp instead of a conversation-derived estimate.

## Command

```powershell
python -B scripts/tooling/technical_documents/create_technical_document.py `
  --slug technical_document_scaffold_and_index_helper `
  --summary "Technical document for a lightweight Python helper that creates timestamped technical documents with the required section scaffold and registers them in the day-local index and doc/README.md."
```

## What The Helper Creates

The helper performs all of the following:

- reads the current local timestamp;
- creates the target month/day directory if needed;
- creates the Markdown file
  `doc/technical/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-HH-mm-SS-slug.md`;
- writes the required section scaffold:
  - `Overview`
  - `Technical Approach`
  - `Involved Components`
  - `Implementation Steps`
- creates the day-local technical `README.md` if it does not yet exist;
- inserts the new document entry at the top of the day-local technical
  `README.md`;
- inserts the new document entry near the top of the technical-document block
  in `doc/README.md`.

## Arguments

- `--slug`
  Required document suffix appended after the timestamp. The script normalizes
  the value into a lowercase underscore-separated slug.
- `--summary`
  Required short summary sentence used in the generated index entries.

## Operational Notes

- The helper is intentionally small and does not update the repository root
  `README.md`.
- The helper refuses to overwrite an already existing timestamped document path.
- The generated document body contains `TBD.` placeholders so the planning
  content can be filled in immediately after creation.
- The helper normalizes written Markdown files to one final newline.
