# Wave 5.2B Offset And Harmonic Guided Preparation

## Overview

This technical document prepares the next actionable step after the approved
`Wave 5.2B` / `Wave 5.2C` model-design gate.

The selected next candidate is `Wave 5.2B`: a lightweight offset / mean and
nonzero-harmonic guided model branch. The purpose is to test the specific
signals exposed by the `Wave 5.2A` full paired-dataset matrix:

- near-zero peak-to-peak delta between `simplified_dataset` and
  `polished_dataset`;
- near-zero smoothness delta;
- mean absolute offset delta `0.003216838 deg`;
- nonzero-harmonic changes across `944` paired records;
- isolated sampling anomalies requiring masks or exclusions.

This step is preparation only. After approval, the package implementation was
completed and the campaign was marked as prepared. It still does not run
training; execution remains an explicit operator action.

No subagent is planned. If later review help is useful, the proposed subagent
name, reason, and delegated scope will be declared before asking for approval.

## Technical Approach

After approval, the next implementation package should prepare `Wave 5.2B` as
a campaign-ready but not automatically launched model branch.

The branch should test a small, auditable architecture instead of a full PINN:

| Component | Planned Role |
| --- | --- |
| Causal trunk | Reuse the repository's existing TE model input conventions and direction-surface handling. |
| TE head | Predict pointwise transmission error as the primary target. |
| Offset / mean head | Predict a condition-linked low-frequency or curve-mean component as an auxiliary target. |
| Centered-shape loss | Keep shape quality visible when offset improves. |
| Harmonic consistency metric or loss | Track nonzero-harmonic amplitude behavior highlighted by `Wave 5.2A`. |
| Sampling mask | Exclude or downweight paired dataset sampling anomalies where needed. |
| Direction surfaces | Preserve `global`, `forward`, and `backward` reporting. |

The first implementation should favor explicit, debuggable code over a large
integrated model. The goal is to determine whether offset and harmonic guidance
improves curve-first readiness without degrading raw TE prediction.

Before any library-specific PyTorch or PyTorch Lightning implementation,
Context7 documentation must be queried according to repository instructions.
The implementation should also use the repository `pytorch-training-workflows`
skill because it will touch Python training/model code.

## Involved Components

Expected read-only inputs:

- `doc/reports/analysis/wave5_2/model_design_gate/[2026-07-01]/wave52b_wave52c_model_design_gate.md`;
- `doc/reports/analysis/wave5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`;
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/`;
- `output/validation_checks/wave52_model_design_gate/2026-07-01-15-30-07__wave52b_wave52c_model_design_gate/`;
- existing model and training patterns for periodic sequence and harmonic
  residual branches;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`;
- `doc/reference_summaries/06_Programming_Style_Guide.md`;
- `doc/running/active_training_campaign.yaml`.

Prepared implementation outputs:

- model implementation:
  `scripts/models/wave52b_offset_harmonic_guided_network.py`;
- model factory and campaign-runner registration:
  `scripts/models/model_factory.py` and
  `scripts/training/run_training_campaign.py`;
- campaign package:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/`;
- campaign manifest:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/campaign.yaml`;
- package preparer:
  `scripts/campaigns/wave_5_2/prepare_wave52b_offset_harmonic_guided_campaign.py`;
- package validator:
  `scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py`;
- dedicated PowerShell launcher:
  `scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.ps1`;
- matching launcher note:
  `doc/scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.md`;
- active campaign state:
  `doc/running/active_training_campaign.yaml`.

Approved planning outputs:

- `doc/reports/analysis/wave5_2/Wave 5.2B Offset And Harmonic Guided Model.md`;
- `doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md`.

Implementation, configuration, launcher, and active-campaign-state outputs are
now prepared. Training execution, closeout, and any `TE Curve Verification
Pipeline` refresh remain deferred.

Protected or deferred components:

- the externally running full-wave `polished_dataset` retraining campaign;
- `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/campaign.yaml`;
- `scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.ps1`;
- full-wave polished output, closeout, and registry artifacts;
- any `TE Curve Verification Pipeline` refresh package;
- `Wave 5.2C` dirty-to-clean transfer implementation;
- `Wave 6` integrated multi-task / multi-head implementation.

## Implementation Steps

1. Inspect existing model and training patterns for the closest reusable causal
   trunk and loss implementation style.
2. Query Context7 for current PyTorch and PyTorch Lightning API details before
   coding library-specific changes.
3. Use the `pytorch-training-workflows` skill before editing Python model,
   dataset, loss, or training files.
4. Draft the `Wave 5.2B` explanatory model report before relying on the new
   branch.
5. Create the campaign planning report with the proposed run matrix, surfaces,
   metrics, expected artifacts, and launch policy.
6. Implement the model and loss code only after the technical document and
   campaign planning report are explicitly approved. Completed through the
   `wave52b_offset_harmonic_guided` model type and existing curve-aware loss
   terms.
7. Prepare training configurations for `global`, `forward`, and `backward`
   surfaces with small ablations:
   pointwise control, offset-head enabled, harmonic metric enabled, and
   centered-shape loss enabled.
8. Create the local and `-Remote` PowerShell launcher plus matching launcher
   note. Completed.
9. Update active campaign state with the prepared package and protected-file
   list. Completed.
10. Run compile, smoke, Markdown, and campaign-package validation checks.
11. Stop with exact launch commands; do not execute training unless explicitly
    approved.
