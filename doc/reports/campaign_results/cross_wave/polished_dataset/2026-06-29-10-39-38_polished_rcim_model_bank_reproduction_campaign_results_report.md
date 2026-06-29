# Polished RCIM Model-Bank Reproduction Campaign Results Report

## Executive Summary

The `polished_dataset_rcim_model_bank_reproduction_2026_06_22` campaign
completed both direction-specific `RCIM Model-Bank Reproduction` runs on
`polished_dataset`.

The accepted surfaces are:

| Surface | Winner | Mean MAPE % | Mean MAE | Mean RMSE | Export |
| --- | --- | ---: | ---: | ---: | --- |
| `forward` | `ERT / ExtraTreesRegressor` | 11.939192 | 0.062217 | 0.149061 | `190` Python, `190` ONNX |
| `backward` | `ERT / ExtraTreesRegressor` | 18.399598 | 0.043815 | 0.110706 | `190` Python, `190` ONNX |

Both surfaces used `data\polished_dataset`, split `969` direction-specific
curves into `678` train, `194` validation, and `97` test rows, and exported
without ONNX failures.

This is a normal campaign closeout. It accepts the polished RCIM model-bank
reproduction artifacts and updates program status, but it does not run or
replace the official `TE Curve Verification Pipeline`. Curve-first official
promotion remains a separate operator-approved workflow.

## Campaign Scope

The campaign reran the paper-faithful RCIM model-bank reproduction workflow on
the measured `polished_dataset` schema. The source CSV measurements are the
polished point columns:

| Column | Role |
| --- | --- |
| `theta` | motor position measured in degrees |
| `theta_dot` | motor velocity derived from position |
| `tau_load` | applied load in Nm |
| `T` | oil temperature |
| `theta_TE` | measured transmission error target |

For the RCIM exact-paper workflow, each curve is transformed into the
paper-compatible feature schema:

| RCIM Feature | Source Meaning |
| --- | --- |
| `rpm` | measured curve speed |
| `deg` | oil temperature condition |
| `tor` | measured load / torque condition |

The target surface is the selected harmonic amplitude/phase bank for harmonics
`0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`.

## Execution Summary

| Surface | Run Instance | Completion Evidence |
| --- | --- | --- |
| `forward` | `2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation` | completed `2026-06-23 18:47:42`; validation summary, best-parameter summary, model bundle, Python export, and ONNX export present |
| `backward` | `2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation` | completed `2026-06-26 09:33:39`; validation summary, best-parameter summary, model bundle, Python export, and ONNX export present |

The backward run was resumed with:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1 -Surface bw
```

The final backward log ends with:

```text
Polished-dataset RCIM Model-Bank Reproduction validation complete
```

## Directional Results

### Forward

- dataset root: `data\polished_dataset`
- direction label: `forward`
- rows: `969`
- split: `678` train / `194` validation / `97` test
- winner: `ERT / ExtraTreesRegressor`
- mean component MAPE: `11.939192%`
- mean component MAE: `0.062217`
- mean component RMSE: `0.149061`
- Python exports: `190`
- ONNX exports: `190`
- ONNX failed exports: `0`

### Backward

- dataset root: `data\polished_dataset`
- direction label: `backward`
- rows: `969`
- split: `678` train / `194` validation / `97` test
- winner: `ERT / ExtraTreesRegressor`
- mean component MAPE: `18.399598%`
- mean component MAE: `0.043815`
- mean component RMSE: `0.110706`
- Python exports: `190`
- ONNX exports: `190`
- ONNX failed exports: `0`

## Artifact Paths

| Artifact | Path |
| --- | --- |
| campaign leaderboard | `output\training_campaigns\cross_wave\polished_dataset\rcim_model_bank_reproduction\polished_dataset_rcim_model_bank_reproduction_2026_06_22\campaign_leaderboard.yaml` |
| campaign best-run YAML | `output\training_campaigns\cross_wave\polished_dataset\rcim_model_bank_reproduction\polished_dataset_rcim_model_bank_reproduction_2026_06_22\campaign_best_run.yaml` |
| campaign best-run Markdown | `output\training_campaigns\cross_wave\polished_dataset\rcim_model_bank_reproduction\polished_dataset_rcim_model_bank_reproduction_2026_06_22\campaign_best_run.md` |
| forward validation summary | `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\validation_summary.yaml` |
| backward validation summary | `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\validation_summary.yaml` |
| forward validation report | `doc\reports\analysis\validation_checks\2026-06-23-18-47-42_rcim_6c4cd030_rcim_model_bank_rep_a049be30_polished_dataset_rcim_model_bank_reproduction_report.md` |
| backward validation report | `doc\reports\analysis\validation_checks\2026-06-26-09-33-39_rcim_6c4cd030_rcim_mod_4166ebbf_polished_dataset_rcim_model_bank_reproduction_report.md` |

## GitHub Artifact Boundary

The generated model bundles are intentionally not Git-tracked:

| Surface | Bundle Size | Reason |
| --- | ---: | --- |
| `forward` | `151.82 MB` | exceeds GitHub `100 MB` single-file limit |
| `backward` | `145.96 MB` | exceeds GitHub `100 MB` single-file limit |

The local generated export folders are also left as local artifacts for this
closeout. The repository records the summaries, reports, registry updates, and
campaign acceptance metadata.

## Registry And Status Effects

The program best-parameter registry was updated with the backward
`polished_dataset` RCIM model-bank entries on `2026-06-26T09:33:26`.

This closeout does not change the scalar neural program winner
`te_periodic_gru_sequence_remote_global`, and it does not replace the accepted
direction-parallel `TE Curve Verification Pipeline` leaders:

- forward curve-verified leader: `rcim_retuned_GBM19_Fw`;
- backward curve-verified leader: `periodic_gru_sequence_Bw`;
- global neural curve-verified leader: `periodic_gru_sequence_global`.

## Acceptance Decision

The campaign is accepted because:

- both directional runs completed;
- both runs used `data\polished_dataset`;
- both runs produced validation summaries and best-parameter summaries;
- both runs exported `190` Python artifacts and `190` ONNX artifacts;
- no ONNX export failures were reported;
- campaign-level winner artifacts now expose the accepted surfaces.

## Follow-Up

Recommended next steps:

1. keep the official `TE Curve Verification Pipeline` refresh separate from
   this closeout;
2. launch the already prepared full-wave polished retraining campaign only
   after this closeout is committed;
3. if RCIM polished candidates should enter official curve-first comparison,
   prepare a separate operator-approved verification launcher.
