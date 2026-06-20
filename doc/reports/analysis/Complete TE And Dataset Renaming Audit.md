# Complete TE And Dataset Renaming Audit

## Executive Verdict

The initial audit found incomplete parity with both renaming commits. The
approved repair pass has now corrected every occurrence classified as stale.

Commit `be4d04890300e4a317ce85f6c6e66c5d69da77f1` established the canonical TE
taxonomy. The repair normalized repository-owned generators, completed queue
notes, historical textual artifacts, generated logs and summaries, and the four
imported guide PDFs.

Commit `be1eaac678caa9003b49e8bd30ff8596d40e543b` migrated active dataset
configuration to `data/simplified_dataset`. The repair also corrected the one
tracked validation payload that retained 27 serialized old source paths.

The active dataset root itself is correct:

- `data/simplified_dataset` exists;
- `data/datasets` does not exist;
- no duplicated `simplified_dataset/simplified_dataset` path was found.

## Audit Scope

The audit covered the complete current working tree rather than only Git
content.

| Measure | Result |
| --- | ---: |
| Files inspected, excluding `.git` internals | 57,048 |
| Bytes read | 47,356,507,252 |
| Git-tracked files in the repository | 31,339 |
| Git-ignored files in the preliminary inventory | 25,713 |
| Raw candidate findings | 7,579 |
| Files with raw candidate findings | 612 |
| Read or permission failures | 0 |
| PDFs semantically extracted | 198 |
| PDF extraction failures | 0 |
| PPTX containers inspected | 44 |
| ODT containers inspected | 1 |
| Notebook containers inspected | 1 |
| GZip containers inspected | 2 |

Every file was scanned as raw bytes. A second pass checked UTF-16 byte
representations. PDFs were opened and text-extracted with PyMuPDF. ZIP-based
documents were opened and their XML or text members inspected. Archive and
container inspection reported no unreadable files.

The `.git` object database was not treated as mutable working-tree content.
`git fsck --connectivity-only --no-reflogs` completed successfully. It reported
only dangling objects, which are normal unreachable historical objects and not
repository corruption.

## Dataset Renaming Findings

### Confirmed Miss

The following tracked file contains 27 old Windows-form dataset paths:

```text
output/validation_checks/track2_curve_payload_diagnostics/
2026-05-28-19-55-32__track2c_curve_payload_diagnostics/
curve_payload_samples.jsonl
```

Each occurrence is a serialized `source_file_path` beginning with:

```text
data\datasets\
```

This is a direct miss relative to the stated scope of commit `be1eaac6`,
because that migration explicitly intended to normalize tracked textual output
artifacts as well as active configuration.

### Intentional Audit References

Five forward-slash matches were produced by the current audit document,
scanner source, and its compiled cache. These are search definitions or
explicit descriptions of the removed path, not operational dataset
references.

### Dataset Conclusion

The active runtime migration is correct, but the repository-wide textual
migration is incomplete by one tracked artifact and 27 serialized paths.

## TE Taxonomy Findings

### Repository-Owned Source Misses

Three report-generator sources still emit obsolete narrative terminology:

| File | Residual terminology |
| --- | --- |
| `scripts/reports/closeout/wave1/closeout_wave1_periodic_mlp_explicit_harmonic_tracking_campaign.py` | `Track 2 curve-overlay workflow` |
| `scripts/reports/closeout/wave2/closeout_wave2b_harmonic_temporal_hybrid_campaign.py` | `Wave 2B` |
| `scripts/reports/closeout/wave2/closeout_wave2c_residual_harmonic_temporal_hybrid_campaign.py` | `Track 2 refresh` |

These are genuine misses because rerunning the generators would recreate old
terminology in newly generated reports.

### Completed Queue Metadata Misses

Nineteen completed queue YAML files retain obsolete reader-facing notes:

- sixteen Wave 2.3 residual-harmonic queue snapshots say that candidates must
  return through official `Track 2 verification`;
- three Wave 4.2 quantile queue snapshots describe the deterministic
  `Track 2 playback curve`.

The queue IDs and filenames are valid historical identifiers, but these
specific `notes` values are prose rather than required machine keys. They do
not respect the canonical terminology.

### Imported Guide PDFs

Four imported NotebookLM guide PDFs still explain the project with `Track 1`
and `Track 2`:

- English Concept Guide;
- English Project Guide;
- Italian Concept Guide;
- Italian Project Guide.

These files have no repository-authored editable source equivalent. They are
externally generated guide deliverables, so they cannot be repaired faithfully
without regenerating them through the guide export workflow.

### Historical Output Artifacts

The `output/` tree contains 7,105 raw TE findings across 284 tracked files.
They are concentrated in:

- completed campaign leaderboards;
- validation summaries;
- operator logs;
- training configuration snapshots;
- generated report HTML;
- comparison summaries.

Most of these occurrences are historical labels, completed campaign metadata,
or compatibility identifiers. They should not be changed mechanically because
doing so could alter provenance or make stored evidence diverge from the run
that produced it.

Some generated prose inside these artifacts is obsolete, but it must be
handled through an explicit historical-artifact policy rather than folded into
an unrestricted search-and-replace.

### Intentional Compatibility Surface

The following residual classes are consistent with the migration policy:

- run names such as `te_track2g_*`;
- campaign IDs and model-family keys;
- directory names under `track_1`, `track_2`, or `track2`;
- Python compatibility identifiers such as `Track2Candidate`;
- historical report filenames such as
  `Track 2 Directional Model Comparison.md`;
- paths and links that must continue to locate those historical artifacts;
- explicit “formerly called” mappings in `README.md` and `AGENTS.md`;
- migration plans and manifests that document the old-to-new mapping;
- imported RCIM reference material.

There are 198 path-name findings, primarily historical verification-plot
directories and filenames. These are artifact locators, not current narrative
taxonomy.

### Generated And Ignored Files

The ignored surface contains 79 raw findings across 22 files. They are limited
to:

- Python bytecode caches;
- generated Sphinx HTML and doctrees;
- the current audit sources and temporary audit data;
- one cached pickle.

These files are derivatives of source or temporary audit artifacts. They do
not establish additional canonical source misses. Regeneration after source
repair will update the relevant derivatives.

## PDF Findings

Semantic PDF extraction found 35 matches across 15 PDFs:

- 22 matches belong to the four imported NotebookLM guides and are genuine
  reader-facing legacy terminology;
- 13 matches belong to official verification PDFs and only reproduce the
  historical filename `Track 2 Directional Model Comparison.md`.

No PDF contains the removed dataset path.

## Complete Classification Summary

| Class | Files | Disposition |
| --- | ---: | --- |
| Stale dataset payload | 1 | Correct the 27 serialized paths |
| Stale report-generator source | 3 | Update canonical emitted prose |
| Stale completed-queue notes | 19 | Update prose without changing IDs |
| Imported guide PDFs | 4 | Regenerate through the guide workflow |
| Historical `output/` artifacts | 284 | Preserve by default; decide policy explicitly |
| Intentional names, IDs, paths, and aliases | multiple | Retain |
| Ignored generated derivatives | 22 | Regenerate from corrected sources where applicable |
| Unsupported or unreadable files | 0 | No action required |

## Recommended Repair Boundary

A safe follow-up repair should:

1. update the one JSONL validation payload to
   `data\simplified_dataset\...`;
2. fix the three report-generator sources;
3. update only the prose `notes` in the nineteen completed queue YAML files;
4. regenerate affected derived reports or HTML where their canonical sources
   exist;
5. regenerate the four NotebookLM guide PDFs only through their established
   source-package workflow;
6. retain historical IDs, filenames, directories, model keys, and run
   metadata;
7. leave historical output evidence unchanged unless the user explicitly
   approves a provenance-preserving output normalization pass.

## Repair Outcome

The approved repair completed the following work:

- replaced all 27 obsolete dataset paths in the tracked JSONL payload;
- corrected the three report-generator sources;
- corrected the nineteen completed queue notes, including labels split across
  YAML line wrapping;
- normalized reader-facing terminology in 260 historical text artifacts while
  preserving IDs and artifact paths;
- replaced 22 legacy labels across the four imported guide PDFs with the
  canonical abbreviations `RCIM-MBR` and `TE-CVP`;
- validated the four guide PDFs as readable three-page A4 deliverables;
- retained only explicit legacy aliases, migration documentation, compatibility
  identifiers, and historical filenames or paths.

## Final Assessment

Both migrations are now operationally and textually aligned within the
approved compatibility boundary.

- Active and serialized dataset references use `data/simplified_dataset`.
- Repository-owned generators no longer recreate obsolete TE terminology.
- Historical artifact prose uses the current taxonomy.
- Existing IDs, filenames, directories, and artifact locators remain stable.
- No hidden or ignored active source introduced an additional dataset-path
  defect.
- No file class was omitted from the audit, and no file failed inspection.
