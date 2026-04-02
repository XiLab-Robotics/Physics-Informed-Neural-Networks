# Repository-Wide Markdown Warning Elimination And Policy Alignment

## Overview

The repository now contains a broad documentation surface across `README.md`,
`AGENTS.md`, `doc/`, report bundles, guide trees, and repository-owned
reference notes. The user requirement for this task is stricter than the
current task-local Markdown hygiene rule: there should be no Markdown warnings
left in any Git-tracked repository-authored `.md` file.

This task will run a repository-wide Markdown warning audit over tracked
Markdown files, excluding non-tracked artifacts, and eliminate the current
warning classes that remain in authored documentation. The target warning
classes explicitly called out are:

- `MD060/table-column-style`
- `MD035/hr-style`
- `MD009/no-trailing-spaces`
- `MD033/no-inline-html`
- `MD032/blanks-around-lists`
- `MD004/ul-style`
- `MD034/no-bare-urls`

## Technical Approach

The cleanup will use the repository-owned Markdown QA tooling first, then fix
the failing files with minimal semantic churn. The pass will target Git-tracked
Markdown files only, which keeps the scope aligned with the user's request to
exclude untracked documents and transient residue.

The fixes will prefer:

- style normalization over prose rewrites;
- repository-consistent list markers and horizontal-rule usage;
- Markdown-native constructs instead of inline HTML where possible;
- explicit links instead of bare URLs;
- compact but lint-compliant table formatting.

The final state should satisfy both:

1. the repository-owned Markdown checks; and
2. the user's stronger zero-warning expectation for tracked Markdown.

## Involved Components

- `README.md`
- `AGENTS.md`
- `doc/`
- repository-owned report bundles under `doc/reports/`
- repository-owned guides under `doc/guide/`
- repository-owned reference notes under `doc/reference_codes/`
- repository-owned Markdown QA tooling under `scripts/tooling/markdown/`

## Implementation Steps

1. Enumerate the Git-tracked Markdown files in the repository.
2. Run repository-owned Markdown QA commands against that tracked set.
3. Collect and classify the active warning instances by file and warning type.
4. Fix the warnings with minimal document churn while preserving meaning and
   repository-specific structure.
5. Re-run the repository-wide Markdown checks until the tracked Markdown set is
   warning-free.
6. Verify final newline hygiene on the touched Markdown files before closing the
   task.
