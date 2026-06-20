# Complete TE And Dataset Renaming Audit

## Overview

This project will perform a complete repository audit against the two approved
renaming migrations:

- commit `be4d04890300e4a317ce85f6c6e66c5d69da77f1`, which established the TE
  program taxonomy;
- commit `be1eaac678caa9003b49e8bd30ff8596d40e543b`, which replaced the legacy
  `data/datasets` root with `data/simplified_dataset`.

The audit will inspect every file in the current repository working tree,
including Git-tracked files, ignored files, generated artifacts, binary
documents, archives, media metadata, and repository-local tool environments.
The preliminary filesystem inventory contains 31,339 tracked files, 25,713
ignored files, and no ordinary untracked files. The total recursive working
tree contains approximately 57,723 files.

The `.git` database will be treated as immutable repository history rather than
as migration output. Historical commits are expected to preserve the old
terminology and paths. Git metadata and object integrity will be checked, but
historical objects will not be rewritten.

This technical document authorizes an audit and subsequent repair of current
working-tree content after explicit approval. It does not authorize rewriting
Git history, external reference sources, or reproducibility-sensitive IDs
without a separate decision.

No subagent is planned. The repository instruction prohibiting silent
subagents remains in force.

## Technical Approach

### Canonical TE Taxonomy

The audit will use the mappings defined by commit `be4d0489`:

| Legacy concept | Canonical concept |
| --- | --- |
| `Track 1` | `RCIM Model-Bank Reproduction` |
| `Track 2` evaluation workflow | `TE Curve Verification Pipeline` |
| former `Track 2B` through `Track 2E` diagnostics | `CVP 1.1` through `CVP 1.5` |
| former `Track 2F` and `Track 2F-bis` models | Waves `3.1` and `3.2` |
| former `Track 2G` models | Wave `3.3` |
| former `Track 2H` and `Track 2H-L` models | Waves `4.1` through `4.4` |
| former Wave `2B` and Wave `2C` | Waves `2.2` and `2.3` |
| former Wave `3` and Wave `4` concepts | Waves `5.1` and `5.2` |

Every occurrence will be classified as reader-facing stale terminology,
machine identifier, historical artifact path, explicit legacy alias,
third-party or imported source, immutable evidence, or a missed migration.

### Canonical Dataset Path

The dataset audit will search for every representation of the removed
`data/datasets` root and confirm use of `data/simplified_dataset`. Variants
will include:

- forward and backward slashes;
- absolute paths and URI-encoded paths;
- quoted, escaped, serialized, and environment-expanded forms;
- case variants;
- split path components in scripts or structured configuration;
- embedded paths inside Markdown, HTML, PDF, Office files, notebooks, YAML,
  JSON, CSV, TOML, XML, logs, manifests, checkpoints, archives, and metadata.

The audit will also check for malformed migration results such as duplicated
`simplified_dataset` segments, stale symlinks, non-resolving active paths, and
active configuration that still points to an obsolete dataset root.

### Complete Filesystem Coverage

The audit will enumerate the working tree independently from Git so ignored and
generated files are included. Files will be divided into:

1. directly searchable text;
2. structured text requiring parsing;
3. PDFs and Office documents requiring text extraction;
4. archives requiring safe member inventory and read-only extraction;
5. databases, checkpoints, model files, images, audio, and video requiring
   metadata or embedded-string inspection;
6. unreadable, encrypted, corrupt, or unsupported files requiring explicit
   reporting.

No file class will be silently skipped. For formats where semantic extraction
is impossible, the final audit will state the inspection method and limitation.
Large files will be streamed or inspected with bounded-memory techniques.

### Historical And External Material

The user requested complete inspection, so imported `reference/` material,
generated `output/` artifacts, local caches, and tool environments will be
scanned. Findings will still respect ownership and reproducibility:

- repository-authored active content may be corrected;
- imported external sources will normally be reported, not rewritten;
- completed run IDs, model keys, campaign IDs, filenames, and artifact paths
  will remain stable when required for lookup;
- stored output evidence will only be modified when it is repository-maintained
  textual metadata and the correction does not invalidate scientific
  provenance;
- Git history will not be rewritten.

### Evidence And Repeatability

The audit will produce a machine-readable inventory under a repository-owned
audit location if persistent evidence is needed. Each finding will record the
path, file type, matched taxonomy, context class, disposition, and validation
result. Temporary extraction data will remain outside the committed scope.

Completion requires:

- every current working-tree file accounted for;
- zero unclassified TE legacy occurrences;
- zero unclassified legacy dataset-path occurrences;
- zero unresolved active references to `data/datasets`;
- an explicit list of intentional historical, external, or compatibility
  matches;
- an explicit list of files that could not be semantically inspected.

## Involved Components

- all Git-tracked repository files;
- all ignored and generated working-tree files;
- root configuration and documentation;
- `.codex/`, `config/`, `data/`, `doc/`, `output/`, `reference/`, `scripts/`,
  `site/`, and repository-local tooling roots;
- PDF, Office, notebook, archive, database, checkpoint, model, image, audio,
  and video files;
- active and historical campaign configuration and artifacts;
- repository Markdown, PDF, Python, YAML, PowerShell, shell, and Sphinx QA
  tooling;
- Git metadata for integrity and history-boundary classification.

The active campaign status is `none`, so no prepared or active campaign file
is protected at planning time.

## Implementation Steps

1. Build a complete path manifest for every current working-tree file,
   including tracked, ignored, generated, hidden, and large files.
2. Derive exact search tokens and semantic mappings from commits `be4d0489`
   and `be1eaac6`.
3. Scan all directly searchable text and structured text formats.
4. Parse notebooks, YAML, JSON, TOML, XML, CSV, SQLite, and similar structured
   containers where applicable.
5. Extract and scan text from all PDFs and Office documents.
6. Inventory archives and safely inspect their members without modifying the
   source archives.
7. Inspect binary metadata and embedded strings for model, checkpoint, image,
   audio, video, and database formats.
8. Classify every match as stale active content, intentional alias, machine
   identifier, historical path, imported source, immutable evidence, or
   unsupported/unreadable content.
9. Report the complete audit findings before applying broad or
   provenance-sensitive corrections.
10. Correct approved stale repository-owned content while preserving IDs,
    historical paths, external sources, and scientific evidence.
11. Regenerate affected maintained PDFs or generated reports from canonical
    sources rather than patching binaries.
12. Re-run the complete filesystem scan and confirm that every residual match
    is classified.
13. Validate active dataset paths and representative non-training data-loading
    entry points.
14. Run Markdown QA, final-newline checks, syntax and configuration checks,
    PDF validation, and a warning-free Sphinx build as applicable.
15. Report coverage totals, findings, repairs, retained occurrences,
    unsupported files, and all validation results.
16. Stop before creating a Git commit and wait for explicit user approval.
