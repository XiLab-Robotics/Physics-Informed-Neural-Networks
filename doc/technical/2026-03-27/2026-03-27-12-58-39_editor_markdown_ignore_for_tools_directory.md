# Editor Markdown Ignore For Tools Directory

## Overview

The repository-owned Markdown validation runner already excludes:

- `.tools/**`

from the canonical `markdownlint-cli2` scan.

However, the user still sees Markdown warnings coming from files under
`.tools/`, which indicates that an editor-integrated Markdown checker is likely
scanning those files independently of the repository runner.

This creates low-value warning noise because `.tools/` contains local helper
environments and vendored third-party files rather than canonical
project-authored documentation.

## Technical Approach

The repository should add a lightweight editor-facing configuration that keeps
`.tools/` out of interactive Markdown warning noise.

The intended effect is:

- preserve canonical repository lint behavior exactly as it is;
- reduce editor-side warning noise from vendored files under `.tools/`;
- keep attention focused on repository-owned Markdown such as:
  - `README.md`
  - `AGENTS.md`
  - `doc/**/*.md`
  - `config/**/*.md`
  - `models/**/*.md`
  - `site/**/*.md`

The implementation will likely need a workspace-level editor settings file, for
example under `.vscode/`, that excludes `.tools/` from file watching, searching,
or Markdown extension processing where appropriate.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `.markdownlint-cli2.jsonc`
  Existing canonical Markdownlint configuration that already ignores `.tools/`.
- future workspace editor settings file
  The likely place to express editor-local ignore behavior for `.tools/`.
- `.tools/`
  Local helper root that should not generate interactive Markdown noise.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before adding or modifying workspace editor
   settings.
3. After approval, add a repository-owned editor/workspace setting that reduces
   Markdown warning noise from `.tools/`.
4. Keep the canonical Markdownlint runner behavior unchanged, because it already
   ignores `.tools/`.
5. Verify that the change reduces editor-side noise without hiding canonical
   project-authored Markdown files.
