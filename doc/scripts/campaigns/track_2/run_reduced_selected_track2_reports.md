# Reduced Selected-Model TE Curve Verification Reports Launcher

## Overview

This launcher is the active reduced `TE Curve Verification Pipeline` report
entry point after the `2026-07-06` model-family pruning decision.

It generates only four selected-model matrix reports:

- `polished_dataset` / `forward`;
- `polished_dataset` / `backward`;
- `simplified_dataset` / `forward`;
- `simplified_dataset` / `backward`.

The launcher excludes `global` by design. Collage, overlay, and
simplified-vs-polished dataset-difference reports are paused and remain
available only through their historical on-demand launchers when explicitly
requested.

## Dry Run

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1
```

The dry run prints the four planned report surfaces and exits without
evaluating model candidates.

## Local Run

Generate the four active reports:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 -Run
```

Resume from a failed surface without recomputing earlier surfaces:

```powershell
.\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 `
  -Run `
  -ResumeFromStep 01_matrix_simplified_dataset_forward
```

## Candidate Set

The candidate manifest is:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reduced_selected_track2_matrix.yaml`

The active model-development candidates are:

- `periodic_gru_sequence`;
- `periodic_mlp_harmonic`;
- `wave4_3_mixture_density_k3`;
- `wave52b_offset_centered_shape_harmonic`.

The reduced anchor candidates are:

- polished RCIM Model-Bank Reproduction `GBM19`;
- polished RCIM Model-Bank Reproduction `ET19`;
- `feedforward`;
- `tree`;
- `harmonic_regression`.

Historical `rcim_retuned_*` leaders remain documented in official reports, but
the reduced local matrix uses repository-present polished RCIM inventories.

## Expected Outputs

Final Markdown reports are moved into:

- `doc/reports/analysis/te_curve_verification_pipeline/04_selected_model_reports/[YYYY-MM-DD]/`

Validation summaries and per-condition metrics remain under:

- `output/validation_checks/track2_reference_comparison/`

Operator logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

## Paused Workflows

The following report families are paused by default:

- `global` selected-model reports;
- best-model collage reports;
- multi-model overlay reports;
- simplified-vs-polished dataset-difference reports;
- broad full-directional matrix regeneration.

Use the historical launchers only after an explicit request to regenerate one
of those paused report families.
