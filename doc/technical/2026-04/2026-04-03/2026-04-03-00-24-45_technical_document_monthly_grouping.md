# Technical Document Monthly Grouping

## Overview

The current technical-document tree uses a day-only grouping under
`doc/technical/YYYY-MM-DD/`.

That layout was sufficient while the repository contained only a limited number
of workdays. It is now becoming dense enough that browsing and maintaining the
technical-document history is slower than it should be.

This change proposes a lightweight structural refinement:

- add a month-level grouping folder under `doc/technical/`;
- keep the existing day-level grouping inside each month;
- preserve the full timestamped filename convention already used for every
  technical document.

The intended result is a cleaner documentation tree with lower navigation noise
and no loss of chronological precision.

## Technical Approach

The repository should move from:

- `doc/technical/YYYY-MM-DD/`

to:

- `doc/technical/YYYY-MM/YYYY-MM-DD/`

The filename format should remain unchanged:

- `YYYY-MM-DD-HH-mm-SS-feature_name.md`

This keeps the current naming discipline intact while reducing the number of
top-level day folders under `doc/technical/`.

The implementation should include:

1. updating the repository rules in `AGENTS.md` so future technical documents
   are created directly in the new month/day structure;
2. moving the existing `doc/technical/YYYY-MM-DD/` day folders into matching
   `doc/technical/YYYY-MM/` month roots;
3. updating `doc/README.md` links so they point to the moved locations;
4. updating any other tracked references that still point to the legacy
   day-only technical-document paths.

The report and guide structures outside `doc/technical/` should remain
unchanged.

## Involved Components

- `AGENTS.md`
- `doc/README.md`
- `doc/technical/`
- any repository-authored Markdown files that still reference
  `doc/technical/YYYY-MM-DD/...`

## Implementation Steps

1. Audit the current `doc/technical/` tree and map each day folder to its month
   root.
2. Move the existing day folders into `doc/technical/YYYY-MM/`.
3. Update the technical-document creation rule in `AGENTS.md`.
4. Rewrite `doc/README.md` references to the new month/day paths.
5. Search for other tracked links to the old technical-document paths and
   update them where needed.
6. Run Markdown warning checks on all touched Markdown files.
7. Stop for final review and wait for explicit approval before committing.
