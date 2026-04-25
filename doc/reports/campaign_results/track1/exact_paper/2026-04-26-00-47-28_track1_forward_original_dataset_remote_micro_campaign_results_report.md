# Track 1 Forward Original-Dataset Remote Micro Campaign Results Report

## Overview

This report closes the forward-only remote micro-campaign prepared as the
mandatory relaunch gate after the discarded interrupted bidirectional mega
campaign.

Planned source:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-25-22-43-25_track1_forward_remote_micro_campaign_and_mega_relaunch_gate_plan_report.md`

Prepared campaign identity:

- campaign name:
  `track1_forward_original_dataset_remote_micro_campaign_2026-04-25_23_48_53`
- intended queue size: `10`
- surface: `forward` only, `1` run per exact-paper family

## Objective

The micro-campaign existed only to validate the repaired remote
original-dataset campaign stack before relaunching the full bidirectional mega
campaign.

It was not intended as a benchmark-promotion wave.

## Final Outcome

The gate passed successfully.

Verified outcome:

- the remote launcher stack completed all `10` family runs;
- validation bundles were synchronized back to the local repository;
- ONNX export completed under the active preflight contract;
- no runner-schema mismatch remained;
- no remote bootstrap or synchronization crash remained.

## Verified Evidence

The repository currently contains two successful forward-only micro waves under:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/`

The first successful wave was the engineering bringup run launched during the
repair session.

The second successful wave is the operator-confirmed replay and is treated as
the canonical gate-completion evidence for this report.

### Canonical Completed Wave

| Order | Run Instance |
| --- | --- |
| `1` | `2026-04-25-23-55-58__track1_original_dataset_forward_svr_remote_micro_campaign_run` |
| `2` | `2026-04-25-23-56-39__track1_original_dataset_forward_mlp_remote_micro_campaign_run` |
| `3` | `2026-04-25-23-58-40__track1_original_dataset_forward_rf_remote_micro_campaign_run` |
| `4` | `2026-04-26-00-01-54__track1_original_dataset_forward_dt_remote_micro_campaign_run` |
| `5` | `2026-04-26-00-02-47__track1_original_dataset_forward_et_remote_micro_campaign_run` |
| `6` | `2026-04-26-00-03-39__track1_original_dataset_forward_ert_remote_micro_campaign_run` |
| `7` | `2026-04-26-00-06-45__track1_original_dataset_forward_gbm_remote_micro_campaign_run` |
| `8` | `2026-04-26-00-08-45__track1_original_dataset_forward_hgbm_remote_micro_campaign_run` |
| `9` | `2026-04-26-00-10-19__track1_original_dataset_forward_xgbm_remote_micro_campaign_run` |
| `10` | `2026-04-26-00-11-16__track1_original_dataset_forward_lgbm_remote_micro_campaign_run` |

## Queue Accounting

| Quantity | Count |
| --- | ---: |
| Intended queue size | `10` |
| Verified completed runs in canonical gate wave | `10` |
| Missing runs | `0` |
| Directions covered | `forward` only |
| Families covered | `10 / 10` |

## Gate Interpretation

The micro-campaign is accepted as an operational gate because it confirms:

1. the original-dataset runner path is wired correctly;
2. the remote preflight covers the ONNX dependency surface needed by the queue;
3. the remote artifact synchronization path works end to end;
4. the operator-facing progress/log stream is usable enough for large relaunch.

## Canonical Impact

This report does **not** promote the micro-campaign metrics into:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- family or program best-run registries

The micro wave is a workflow-validation gate, not a scientific closeout.

## Next Step

The next canonical step is to regenerate the full bidirectional original-dataset
mega-campaign from zero and expose the fresh remote launch command.
