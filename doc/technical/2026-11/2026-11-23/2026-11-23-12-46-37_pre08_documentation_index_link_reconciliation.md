# PRE08-DOC — Canonical Documentation Index Link Reconciliation

**Prepared:** 2026-11-23 (filename timestamp is a naming convention; its wall-clock accuracy was not independently checked).
**Source baseline:** PINNs `main@1f6215eb6c89cf4bab9890476ba06446e3bdcdff`.
**Index source blob:** `2c9e2d1cd5086d1c80369f9817ab56e1db8731fd`.
**Issue evidence:** Coordinator DEC-145, `SRC-168/K-171/C-171`.
**Scope:** Documentation-only repair; no historical document deletion, relocation or content edits, no scientific or PLC operations.

## Overview

Repair the 67 unresolved relative Markdown links out of the 1,119 local links in
`doc/README.md` identified in the complete pre-HYG-08 audit. Preserve the
existing documentation architecture, visible descriptions, historic data,
scientific reports and all experiment artifacts. HYG-08 remains deferred.

## Technical Approach

Use the exact recursive `doc/` Git tree, with `truncated=false`, to resolve
all destinations by file path, contextual directory and historic report title.
The reconciliation found:

- **44** unique same-basename destinations in renamed/reorganized directories.
- **18** context-disambiguated destinations: 16 video source briefs under the
  guide-specific `assets/` directory, one dated Wave 1 result and one campaign
  results report (not the same-named technical note).
- **5** renamed historic analysis references, now pointing to the actual files:
  `Wave 4.4 Latent-State Hysteresis Probe Model.md`,
  `FeedForward Trial Analytical Report.md`,
  `Training Configuration Analysis.md` and `.pdf`, and
  `TE Model Family Analysis.md`.

The five renamed legacy paths are historically documented (March folder/name
reorganization); the Wave 4.4 path also has a corresponding visible index label.
Maintain the original visible Markdown titles/descriptions. Rewrite only the
67 URL destinations to percent-encoded local relative paths; register this
technical record as one new index entry.

Confirm the other local links as well. Nine links point outside `doc/` into
`reference/`, `output/` and `config/`; their exact files were fetched and
verified against the current `main` Git objects. Do not misclassify these as
broken merely because a CI sparse checkout omits their payloads.

## Involved Components

- `doc/README.md` — exactly 67 existing URL targets plus the new plan link.
- `doc/technical/2026-11/2026-11-23/2026-11-23-12-46-37_pre08_documentation_index_link_reconciliation.md` — documentation-first technical plan and verification record.
- Coordinator DEC-145 / Project Memory / Backlog / Source Refs — update only
  after an approved change has been published and independently rechecked.

No changes to `scripts/`, `models/`, `data/`, `output/`, `reference/`,
CI workflow, `AGENTS.md`, `requirements.txt`, TwinCAT or TestRig.

## Implementation Steps

1. Pin `main@1f6215eb6c89cf4bab9890476ba06446e3bdcdff` and read the complete DEC-145 list and current
   `doc/` tree. Verify direct and renamed path targets, never infer only from
   a matching basename when duplicates exist.
2. Prepare this technical document first, then register it in the current
   documentation index.
3. Update exactly 67 link destinations while preserving original prose and
   retaining all source documents and historic artifacts.
4. Check the new index against Git tree files/directories and the nine
   independently fetched off-`doc/` targets. Expect zero missing local links,
   67 repaired URL targets, no other existing title/prose edits, and only one
   additional technical-plan entry.
5. Run touched-scope Markdown and lint checks when the indexed contents are
   available in a suitable repository checkout. No heavy ML environment,
   training, automatic Actions dispatch or PLC build is part of this work.
6. Review the exact proposed diff and halt before any commit: the repository
   `AGENTS.md` requires explicit final owner approval after preparation.
   After approval, use a reviewable PR against protected `main` and check
   existing Quality and Pages on the exact merged SHA.
7. Re-verify main, the archived portable ref and the coordinator SRC/K/C
   registers after publication. HYG-08 stays on hold.

## Verification And Rollback

The prepared repair is **NOT COMMITTED** until the final approval gate. Git blob
or tree staging, if used, is not a branch update. Static link existence is
not an end-to-end Sphinx/Markdownlint execution receipt; those tests and their
exact-run results must be reported separately. Rollback, if ever needed,
must be a normal reviewed revert, not a Git history rewrite.
