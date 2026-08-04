# Wave 5.2A Full Paired Dataset Matrix

## Overview

This technical document plans the extension of the existing `Wave 5.2A`
paired-dataset diagnostic from a bounded `24`-pair sample to a full paired
matrix over all matched `simplified_dataset` and `polished_dataset`
directional records.

The goal is to determine whether the initial bounded evidence generalizes:
the first sample showed near-zero peak-to-peak and smoothness deltas while
showing condition-dependent mean / offset shifts. The full pass must classify
whether that behavior is global or whether some operating regimes contain
shape, smoothness, sampling, or harmonic changes that should alter the future
`Wave 5.2B` and `Wave 5.2C` model design.

This is a diagnostic and reporting task only. It must not launch training,
prepare a training campaign, modify the externally running full-wave
`polished_dataset` retraining package, or promote any candidate through the
`TE Curve Verification Pipeline`.

No subagent is planned for this task. If later review help is useful, the
proposed subagent name, reason, and delegated scope will be declared before
asking for approval.

## Technical Approach

The existing paired diagnostic builder should be extended rather than replaced.
The current implementation already pairs dataset records by speed, torque,
temperature, and direction, then emits Markdown plus CSV and JSON artifacts.
The full-matrix update should add classification and aggregation layers while
preserving the bounded mode for fast interactive checks.

The full pass should run with `--max-pairs 0` to include every available paired
directional record. The report should make clear that this is still a
dataset-diagnostic artifact, not a model result.

The added analysis should classify paired records into practical buckets:

- nearly identical curve surface;
- offset-shifted curve surface;
- shape-changed curve surface;
- smoothness or local-noise changed curve surface;
- harmonic-amplitude changed curve surface;
- sampling or row-count anomaly.

The classification thresholds should be explicit constants inside the script,
documented in the report, and conservative enough for roadmap decisions rather
than overfitting to one small sample.

The report should aggregate results by:

- global matrix;
- `forward` and `backward` directions;
- speed;
- torque;
- temperature.

The resulting evidence should answer what to do next:

- if offset-shifted pairs dominate, prioritize offset / mean heads,
  centered-shape loss, and within-machine dirty-to-clean offset supervision
  before a heavy first PINN;
- if shape or harmonic changes are material, keep MMT/PINN-style harmonic and
  smoothness constraints in `Wave 5.2B`;
- if sampling anomalies are frequent, handle masks and reduced-point tests
  before trusting transfer-learning conclusions;
- if simplified and polished are mostly identical except offsets, use
  `simplified_dataset` mainly as a noise-aware stress surface and
  `polished_dataset` as the final clean deployment surface.

## Involved Components

Expected read-only inputs:

- `data/simplified_dataset/`;
- `data/polished_dataset/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`;
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-10-57__wave52a_paired_dataset_diagnostics/`;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`;
- `doc/running/active_training_campaign.yaml`.

Expected implementation targets after approval:

- `scripts/reports/analysis/build_wave52a_paired_dataset_diagnostics.py`;
- a new dated full-matrix report under
  `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/[YYYY-MM-DD]/`;
- a new immutable artifact folder under
  `output/validation_checks/wave52a_paired_dataset_diagnostics/<run_instance_id>/`;
- `doc/README.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Protected or deferred components:

- `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/campaign.yaml`;
- `scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.ps1`;
- full-wave polished campaign outputs, closeouts, and registries;
- any `TE Curve Verification Pipeline` refresh package;
- model classes, training launchers, and campaign planning reports.

## Implementation Steps

1. Extend the existing paired diagnostic builder with explicit classification
   thresholds and per-pair category assignment.
2. Add aggregate summaries by global matrix, direction, speed, torque, and
   temperature.
3. Preserve the existing bounded default mode, while adding a documented
   full-matrix command using `--max-pairs 0`.
4. Run the full-matrix diagnostic into a new immutable run instance under
   `output/validation_checks/wave52a_paired_dataset_diagnostics/`.
5. Generate a full-matrix Markdown report that includes category counts,
   aggregate deltas, and next-step interpretation for `Wave 5.2B`,
   `Wave 5.2C`, and `Wave 6`.
6. Register the full-matrix report in `doc/README.md` and synchronize the live
   backlog, TE closeout ledger, and training master summary without changing
   active campaign state.
7. Run `py_compile` for the diagnostic builder.
8. Run the repository Markdown style and Markdownlint checks on the touched
   Markdown scope.
