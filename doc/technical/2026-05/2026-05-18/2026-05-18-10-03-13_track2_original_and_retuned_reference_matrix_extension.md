# Track 2 Original And Retuned Reference Matrix Extension

## Overview

This technical document formalizes the next `Track 2` matrix extension after
the canonical directional comparison was populated with accepted `Track 1`
family banks and exported `Wave 1` models.

The next comparison must also include additional paper-reference archives from
`models/`:

- `rcim_original` forward reference banks from
  `models/paper_reference/rcim_original/forward/`;
- `rcim_retuned` forward reference banks from
  `models/paper_reference/rcim_retuned/forward/`;
- `rcim_retuned` backward reference banks from
  `models/paper_reference/rcim_retuned/backward/`.

Although a `models/paper_reference/rcim_original/backward/` root exists in the
local repository, this task intentionally scopes `rcim_original` to forward
models only, matching the requested comparison surface.

No subagent use is planned. If subagent use becomes useful later, this document
must be updated with the proposed subagent name, delegated task boundary, and
approval requirement before any subagent is launched.

## Technical Approach

Extend the Track 2 candidate-generation configuration so the full matrix can
include multiple paper-reference archive groups, not only the accepted
`rcim_track1` banks.

Each added archive group must declare:

- a source label, such as `rcim_original` or `rcim_retuned`;
- the allowed direction roots;
- the same eleven model families already used by Track 1:
  `SVM`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`, and
  `ELM`;
- a candidate identifier that keeps source provenance visible, for example
  `rcim_original_SVM19_Fw`, `rcim_retuned_SVM19_Fw`, and
  `rcim_retuned_SVM19_Bw`.

The direction contract remains unchanged:

| Source | Surface | Evaluation Curves |
| --- | --- | --- |
| `rcim_original` | `Fw` | forward only |
| `rcim_retuned` | `Fw` | forward only |
| `rcim_retuned` | `Bw` | backward only |
| `Wave 1 global` | `global` | forward and backward, reported separately |

The generated report must continue to start from the current full matrix and
must not reintroduce the obsolete mixed historical `LGBM-19` smoke comparison.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  - add additional paper-reference archive groups for `rcim_original` and
    `rcim_retuned`.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - generalize candidate generation to support multiple paper-reference archive
    groups with explicit source labels and direction roots.
- `doc/reports/analysis/Track 2 Directional Model Comparison.md`
  - regenerate the canonical Track 2 report with the enlarged candidate matrix.
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
  - update Track 2 status and best-row summary after the enlarged matrix is
    regenerated.
- `doc/reports/analysis/Training Results Master Summary.md`
  - update Track 2 status counts and artifact pointers.
- `doc/README.md`
  - keep the new technical document registered.
- `output/validation_checks/track2_reference_comparison/`
  - store the immutable validation artifact bundle for the enlarged matrix.

## Implementation Steps

1. Confirm the `rcim_original` and `rcim_retuned` reference inventory roots and
   the eleven family archive folders.
2. Update Track 2 candidate generation to support source-labeled archive
   groups, preserving the existing `rcim_track1` identifiers for the accepted
   Track 1 banks.
3. Add `rcim_original` forward-only archive entries to the full matrix
   configuration.
4. Add `rcim_retuned` forward and backward archive entries to the full matrix
   configuration.
5. Ensure the report candidate inventory exposes the source label, model
   family, direction surface, and model source path for each added candidate.
6. Run the full Track 2 validation matrix from the updated configuration.
7. Regenerate the canonical Track 2 report and immutable validation report.
8. Update the RCIM benchmark and Training Results Master Summary with the new
   candidate counts, artifact path, and best-row summary.
9. Run Python syntax checks for the touched Track 2 scripts.
10. Run Markdown QA on the touched Markdown files.
