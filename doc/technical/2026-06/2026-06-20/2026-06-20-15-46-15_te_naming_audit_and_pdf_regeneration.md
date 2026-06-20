# TE Naming Audit And PDF Regeneration

## Overview

The TE program naming migration introduced the canonical terms
`RCIM Model-Bank Reproduction`, `TE Curve Verification Pipeline`, numbered
`CVP` verification modules, and model-development Waves. This follow-up project
will verify that the migration reached all repository-authored documents,
scripts, configuration files, generated reports, and maintained report PDFs.

The audit will distinguish stale narrative terminology from intentional legacy
machine identifiers. Existing campaign IDs, run names, artifact paths, script
filenames, and historical output keys will remain stable when renaming them
would break reproducibility or lookup. Maintained report PDFs that still show
stale terminology will instead be regenerated from their canonical sources at
the same repository paths.

The preliminary inventory found 190 Git-tracked report or guide PDFs, 4,594
Git-tracked Markdown files in the same documentation roots, and 114 direct
same-stem Markdown/PDF pairs. It also found 145 candidate legacy-term lines in
73 tracked textual files outside imported references, generated portal output,
and training-output roots. These are candidates for classification, not an
assumption that every match must be replaced.

No subagent is planned for this work. Any later proposal to delegate part of
the audit will require an updated task boundary and explicit user approval
before launch.

## Technical Approach

### Textual Naming Audit

The audit will search Git-tracked Markdown, reStructuredText, YAML, JSON, TOML,
Python, and PowerShell files for legacy labels such as `Track 1`, `Track 2`,
the former lettered Track 2 branches, and obsolete Wave numbering.

Every remaining occurrence will be assigned to one of these classes:

1. stale repository-authored prose or generated display text that must change;
2. an intentional compatibility identifier, path, command, or artifact name;
3. a historical citation that needs an explicit legacy-name explanation;
4. imported reference material or immutable output evidence that must remain
   unchanged;
5. a generated artifact whose source or generator must be corrected first.

Completion requires zero unclassified legacy terminology in the audited
repository-owned scope. It does not require deleting valid historical strings
such as existing `te_track2g_*` model-family keys.

### PDF Source Mapping And Regeneration

Each Git-tracked PDF under `doc/reports/` and `doc/guide/` will be text-scanned
for stale reader-facing terminology. Direct same-stem Markdown/PDF pairs will
be mapped first. Remaining PDFs will be traced through report indices,
repository exporters, generation scripts, or topic-local source bundles.

Only PDFs containing stale reader-facing terminology will be regenerated.
Their paths and filenames will remain unchanged. The preferred export route is
the repository-owned report pipeline:

```text
python -B scripts/reports/pdf/run_report_pipeline.py
```

Where a report has a dedicated generator, that generator will be updated and
used so future reruns preserve the canonical terminology. Binary PDFs will not
be patched directly.

Regeneration cannot produce byte-identical files because PDF metadata and
layout serialization may change. The target is content, styling, dimensions,
and visual structure identical to the existing report except for the approved
terminology and any unavoidable line wrapping or pagination caused by the new
labels.

### PDF Quality Assurance

Every regenerated PDF will be checked against its previous deliverable and
validated as a real PDF. Checks will include:

- successful opening and a nonzero page count;
- page-size parity and page-count comparison;
- extracted-text confirmation that stale reader-facing terminology is gone;
- preservation of intentional legacy identifiers and paths;
- rasterization of every page through the repository validator;
- visual inspection for clipping, broken headers, table overflow, malformed
  identifiers, and unintended blank or sparse pages;
- representative comparison with the styled analytical PDF golden standard.

Unexpected page-count or layout changes will be investigated rather than
accepted automatically.

### Validation Scope

After corrections and PDF regeneration, the task will run:

- repository Markdown style and markdownlint checks;
- final-newline checks for touched Markdown;
- Python compilation for touched Python;
- YAML parsing for touched YAML;
- PowerShell parsing for touched PowerShell;
- a warning-free Sphinx portal build when portal sources are affected;
- a final Git-tracked legacy-term inventory with retained matches classified;
- PDF export validation for every regenerated deliverable.

## Involved Components

- canonical project entry points such as `README.md`, `AGENTS.md`, and
  `doc/README.md`;
- repository-authored documentation under `doc/`;
- Sphinx source documentation under `site/`;
- user-facing labels, comments, and report text under `scripts/`;
- YAML, JSON, and TOML configuration or registry descriptions;
- maintained PDFs under `doc/reports/` and `doc/guide/`;
- report generators and PDF tooling under `scripts/reports/`;
- Markdown QA tooling under `scripts/tooling/markdown/`.

Imported material under `reference/`, generated Sphinx build output, and
training artifacts under `output/` are outside bulk-rewrite scope. They will
only be used to understand or classify historical names.

The active campaign state is `none`, so no prepared or active campaign files
are protected at planning time.

## Implementation Steps

1. Produce a complete Git-tracked inventory of legacy terms across textual
   documents, scripts, configuration files, and report sources.
2. Classify every match as stale prose, intentional identifier, historical
   citation, imported evidence, or generator-derived output.
3. Correct stale terminology in canonical textual sources while preserving
   reproducibility-sensitive names and paths.
4. Update report generators or templates that can recreate obsolete labels.
5. Extract text from all 190 tracked report and guide PDFs and identify the
   subset containing stale reader-facing terminology.
6. Map each affected PDF to its canonical Markdown source or dedicated
   repository generator.
7. Regenerate affected PDFs at their existing paths with the established
   styles and assets.
8. Compare page dimensions, page counts, extracted text, and visual structure
   with the previous PDFs, investigating any unexpected differences.
9. Run the repository PDF validator on every page of every regenerated PDF.
10. Re-run the textual and PDF legacy-term scans and classify all intentional
    retained matches.
11. Run Markdown QA, final-newline checks, language-specific syntax checks, and
    the warning-free Sphinx build where applicable.
12. Report the corrected files, regenerated PDFs, retained legacy identifiers,
    and validation evidence.
13. Stop before creating a Git commit and wait for explicit user approval.
