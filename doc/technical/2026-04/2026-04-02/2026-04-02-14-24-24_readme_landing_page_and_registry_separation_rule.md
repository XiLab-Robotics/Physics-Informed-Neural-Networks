# README Landing Page And Registry Separation Rule

## Overview

The repository README was recently cleaned up because it had drifted from a
GitHub-facing landing page into a long internal registry of technical notes,
historical fixes, and process artifacts.

That drift is likely to recur unless the repository rules state the intended
boundary explicitly. This document defines a stable documentation rule that
keeps `README.md` concise and public-facing, while moving internal registries
and detailed indexes into `doc/`.

## Technical Approach

The rule should formalize three separate documentation roles:

1. `README.md` as the public landing page for a new human user;
2. `doc/README.md` as the main internal documentation index;
3. narrower domain indexes such as `doc/scripts/tooling/README.md` for grouped
   operational notes.

The repository instructions should explicitly forbid re-growing the main
README into a chronological list of technical documents, bug-fix logs, or
internal artifact registries. When detailed provenance or topic-local indexes
are needed, they should be placed in the relevant `doc/` subtree instead of
the repository root.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Add a repository rule that keeps `README.md` as a concise GitHub-facing
   landing page and explicitly disallows internal registry growth there.
2. Add a companion rule that internal indexes, technical-document registries,
   and topic-local provenance summaries belong in `doc/` rather than in the
   root README.
3. Reference this rule document from `README.md` so the rationale remains
   discoverable.
