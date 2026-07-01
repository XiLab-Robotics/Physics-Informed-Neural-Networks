# Wave 5.2A Paired Dataset Diagnostics

## Overview

This technical document plans the `Wave 5.2A` paired dataset diagnostic pass
for `simplified_dataset` and `polished_dataset`.

The goal is to establish an evidence base before any MMT/PINN-guided model,
dirty-to-clean model, transfer-learning backbone, or reduced-point campaign is
implemented. The diagnostic must show how the legacy simplified curve surface
and the new polished point surface differ at matched operating conditions,
directions, curve shapes, offsets, smoothness, harmonic content, and retained
or removed samples.

The externally running
`polished_dataset_full_wave_retraining_2026_06_22` campaign remains out of
scope. This work must not modify its manifest, launcher, queue configuration,
registries, output artifacts, closeout reports, or `TE Curve Verification
Pipeline` refresh path.

No training campaign or training experiment is part of this technical
document. No subagent is planned. If later review help is useful, the proposed
subagent name, reason, and delegated scope will be declared before asking for
approval.

## Technical Approach

The diagnostic pass will compare the two dataset surfaces as paired evidence,
not as interchangeable copies.

`simplified_dataset` will be treated as the legacy curve surface that exposed
dirty/noisy behavior during the earlier `Wave 4` research. It remains useful
for noise-aware modeling, robust-loss stress tests, dirty-to-clean hypotheses,
and reduced-point sensitivity.

`polished_dataset` will be treated as the clean deployment-oriented surface.
It is the expected source for final comparable results, future curve-first
promotion decisions, and deployment-oriented `Wave 5.2B` or `Wave 6`
architecture choices after the full-wave retraining evidence is available.

The diagnostic should produce a report and machine-readable artifacts that
answer these questions:

- Which operating conditions and directions align cleanly between the two
  datasets?
- How do the curve means, offsets, peak-to-peak values, smoothness, derivative
  behavior, and harmonic signatures differ after alignment?
- Which differences appear to come from row-level polishing, validity-window
  handling, zeroing correction, derivative behavior, or direction separation?
- Which polishing operations are offline-only and therefore unsafe for runtime
  inference?
- Which polishing ideas can be converted into leakage-safe train-time losses,
  auxiliary heads, masks, diagnostic metrics, or data-reduction tests?
- Whether a dirty-to-clean target is well aligned enough to justify a later
  `Wave 5.2C` multi-task model.
- Whether a backbone pretraining and fine-tuning experiment is justified for
  `Wave 6`.

The first implementation after approval should be diagnostic/reporting code,
not a training launcher. If code is needed, it should use repository-owned
paths and artifacts, write under `output/validation_checks/`, and generate a
canonical authored report under `doc/reports/analysis/`.

## Involved Components

Expected read-only inputs:

- `data/simplified_dataset/`;
- `data/polished_dataset/`;
- `data/generate_polished_dataset.py`;
- `scripts/datasets/generate_polished_transmission_error_dataset.py`;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/Training Results Master Summary.md`.

Expected future output locations after implementation approval:

- a canonical report under
  `doc/reports/analysis/wave5_2/paired_dataset_diagnostics/[YYYY-MM-DD]/`;
- machine-readable summaries under
  `output/validation_checks/wave52a_paired_dataset_diagnostics/<run_instance_id>/`;
- optional plots or collages in the same report-local dated folder, if the
  report needs visual evidence.

Protected or deferred components:

- `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/campaign.yaml`;
- `scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.ps1`;
- `doc/running/active_training_campaign.yaml`;
- full-wave polished campaign output and closeout artifacts;
- any `TE Curve Verification Pipeline` refresh launcher or acceptance package.

## Implementation Steps

1. Inspect the current dataset-family reference and the two polishing scripts
   to document the exact pairing keys, direction conventions, and offline-only
   transformations.
2. Define the matching policy for operating condition, direction, speed,
   torque, and temperature without assuming that file layout alone proves
   semantic equality.
3. Define curve-level metrics for paired comparison:
   mean offset, absolute offset, peak-to-peak range, smoothness, derivative
   spread, closure behavior, harmonic amplitude, harmonic phase, and
   row-count / sampling differences.
4. Define sample or point-level diagnostics for the polished surface:
   retained row counts, measured speed and torque ranges, temperature ranges,
   derivative excursions, and possible outlier masks.
5. Classify polishing logic into:
   offline-only diagnostic logic, train-time-safe regularization ideas,
   possible auxiliary-head targets, and runtime-unsafe leakage.
6. Draft the future analysis report structure with separate conclusions for:
   clean-polished modeling, simplified noise-aware modeling,
   dirty-to-clean modeling, transfer / fine-tuning, and reduced-point tests.
7. After explicit approval, implement the diagnostic report builder and
   artifact writer. Do not add training campaigns, launchers, model classes, or
   registry updates in this first implementation pass.
8. Run Markdown QA on any authored Markdown touched by the implementation.
   If Python scripts are added later, run the relevant compile or smoke checks
   for those scripts.
