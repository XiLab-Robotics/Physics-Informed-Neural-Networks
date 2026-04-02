# Overview

This document tightens the repository Markdown policy so that newly created or
modified Git-tracked Markdown files must be brought to zero warnings before a
task is considered complete. The goal is to remove ambiguity between
"check the warnings" and "actually resolve the warnings".

## Technical Approach

The policy change will refine the existing Markdown QA rules in `AGENTS.md`
without changing the broader repository structure. The updated wording will:

* keep the touched-file scope for normal tasks;
* make zero warnings the mandatory outcome for newly created or modified
  Git-tracked Markdown files;
* require explicit analysis and resolution of any warning emitted by the
  repository Markdown QA pass or the broader Markdownlint pass on the intended
  scope;
* keep repository-wide audits as a separate explicit workflow when requested by
  the user.

## Involved Components

* `AGENTS.md`
* `doc/README.md`
* This technical document

## Implementation Steps

1. Update `AGENTS.md` so the Markdown policy clearly requires zero warnings on
   newly created or modified Git-tracked Markdown files before task closure.
2. Make the wording explicit that warnings must be analyzed and resolved, not
   only checked.
3. Register this policy-tightening document from `doc/README.md`.
4. Run the Markdown warning checks on the touched Markdown files after the rule
   update.
