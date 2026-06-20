# TE Curve Verification Pipeline Full Directional Matrix Report

## Overview

This technical document formalizes the next `TE Curve Verification Pipeline` implementation step:
replace the obsolete mixed historical `LGBM-19` versus `feedforward`
comparison with a fresh full directional comparison matrix built directly from
the saved model artifacts under `models/`.

The new `TE Curve Verification Pipeline` report must be a standalone canonical analysis report,
parallel in role to `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`,
but focused only on direct offline curve comparisons between:

- the accepted `RCIM Model-Bank Reproduction` paper-reference family banks;
- the exported `Wave 1` family models;
- the same canonical held-out TE curves loaded from `data/simplified_dataset`.

The historical mixed comparison will remain recoverable through Git history and
existing historical validation artifacts, but it must not appear in the new
canonical TE curve-verification report.

No subagent use is planned. If subagent use becomes useful later, this document
must be updated with the proposed subagent name, delegated task boundary, and
approval requirement before any subagent is launched.

## Technical Approach

The implementation should extend the existing direction-aware TE Curve Verification Pipeline runner
from the current limited candidate set into a complete matrix built from model
files under `models/`.

### Candidate Surface

The RCIM Model-Bank Reproduction families are fixed to the eleven accepted exact-paper families:

| RCIM Model-Bank Reproduction Family |
| --- |
| `SVM` |
| `MLP` |
| `RF` |
| `DT` |
| `ET` |
| `ERT` |
| `GBM` |
| `HGBM` |
| `XGBM` |
| `LGBM` |
| `ELM` |

For RCIM Model-Bank Reproduction, the runner must evaluate:

- every forward family bank under `models/paper_reference/rcim_track1/forward/`
  only on forward curves;
- every backward family bank under
  `models/paper_reference/rcim_track1/backward/` only on backward curves;
- each family's saved Python model files, using the family inventory to map
  amplitude and phase target models into reconstructed TE curves.

For Wave 1, the runner must evaluate exported model artifacts under
`models/exported/`:

- forward Wave 1 models only on forward curves;
- backward Wave 1 models only on backward curves;
- global Wave 1 models on both forward and backward curves, with metrics
  reported separately by direction.

### Report Structure

Create a new canonical report under `doc/reports/analysis/`, with a readable
title-based filename such as:

```text
doc/reports/analysis/track2/TE Curve Verification Pipeline Directional Model Comparison.md
```

The report must start from the new comparison only and must not include the
obsolete historical mixed `LGBM-19` comparison. Required sections:

- `Overview`
- `Dataset And Split`
- `Candidate Inventory`
- `Forward Comparison`
- `Backward Comparison`
- `Global Model Direction Breakdown`
- `Artifacts`
- `Interpretation`
- `Open Gaps`

The `Forward Comparison` section must compare:

- every `RCIM Model-Bank Reproduction` forward model bank;
- every `Wave 1` forward model;
- every `Wave 1` global model evaluated on forward curves.

The `Backward Comparison` section must compare:

- every `RCIM Model-Bank Reproduction` backward model bank;
- every `Wave 1` backward model;
- every `Wave 1` global model evaluated on backward curves.

The `Global Model Direction Breakdown` section must isolate global Wave 1
models and show their forward, backward, and combined scores without mixing
them into direction-invalid comparisons.

### Dataset Contract

All comparisons must load the test curves through the canonical dataset
configuration and data root:

```text
config/datasets/transmission_error_dataset.yaml
data/simplified_dataset
```

The implementation must not use copied recovered-original datasets or archived
prediction CSVs as the primary evaluation source. Archived model-bundle data can
remain provenance evidence only.

## Involved Components

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - new canonical TE curve-verification report with forward, backward, and global sections;
  - no historical mixed-comparison section.
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
  - remove the obsolete historical mixed TE Curve Verification Pipeline subsection from the canonical
    benchmark text;
  - keep only a concise pointer to the new TE curve-verification report if useful.
- `doc/reports/analysis/Training Results Master Summary.md`
  - update TE Curve Verification Pipeline status after the full matrix is generated.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  - add or revise configuration for the complete curve-verification matrix.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  - extend candidate discovery and report generation to cover RCIM Model-Bank Reproduction and Wave
    1 models from `models/`.
- `models/paper_reference/rcim_track1/forward/`
  - source root for RCIM Model-Bank Reproduction forward family banks.
- `models/paper_reference/rcim_track1/backward/`
  - source root for RCIM Model-Bank Reproduction backward family banks.
- `models/exported/`
  - source root for Wave 1 global, forward, and backward exported models.
- `output/validation_checks/track2_reference_comparison/`
  - immutable output root for the generated full-matrix validation artifacts.

## Implementation Steps

1. Inspect the existing TE Curve Verification Pipeline runner and support utilities to identify the
   current assumptions left from the limited `LGBM19` and `feedforward`
   comparison.
2. Inspect the RCIM Model-Bank Reproduction model inventories under
   `models/paper_reference/rcim_track1/{forward,backward}/` and confirm the
   eleven family roots and their amplitude/phase target mappings.
3. Inspect Wave 1 export inventories under `models/exported/` and confirm the
   global, forward, and backward model artifacts available for each exported
   family.
4. Update the TE Curve Verification Pipeline configuration surface so the full candidate matrix is
   generated from `models/` rather than from output registries alone.
5. Extend the runner so every candidate row records:
   - family;
   - source track (`RCIM Model-Bank Reproduction` or `Wave 1`);
   - surface (`forward`, `backward`, or `global`);
   - source model path;
   - valid evaluation direction;
   - dataset config and dataset root.
6. Remove the obsolete historical mixed-comparison section from
   `RCIM Paper Reference Benchmark.md` and replace it with a concise link to
   the new TE curve-verification report.
7. Generate the full curve-verification comparison artifacts under
   `output/validation_checks/track2_reference_comparison/`.
8. Create the new `Track 2 Directional Model Comparison.md` report with
   forward, backward, and global sections and tables for all evaluated
   candidates.
9. Update `Training Results Master Summary.md` with the new TE Curve Verification Pipeline status and
   artifact pointers.
10. Run Python syntax checks and the TE Curve Verification Pipeline validation run.
11. Run Markdown QA on touched Markdown files with the repository-owned tools.
