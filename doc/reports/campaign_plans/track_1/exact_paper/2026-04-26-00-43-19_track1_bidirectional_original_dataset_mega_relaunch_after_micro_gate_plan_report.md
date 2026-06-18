# Track 1 Bidirectional Original-Dataset Mega Relaunch After Micro Gate Plan Report

## Overview

This planning report covers the fresh relaunch of the full bidirectional
original-dataset Track 1 mega-campaign after the successful completion of the
forward-only remote micro gate.

The validated micro gate demonstrated that the current remote original-dataset
campaign stack can:

- start successfully on the remote workstation;
- complete one run per exact-paper family;
- export ONNX artifacts under the current dependency preflight;
- synchronize validation outputs and reports back to the local repository.

## Gate Evidence

The repository currently contains two completed forward-only micro waves under:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/`

The second completed wave spans the following `10` runs:

- `2026-04-25-23-55-58__track1_original_dataset_forward_svr_remote_micro_campaign_run`
- `2026-04-25-23-56-39__track1_original_dataset_forward_mlp_remote_micro_campaign_run`
- `2026-04-25-23-58-40__track1_original_dataset_forward_rf_remote_micro_campaign_run`
- `2026-04-26-00-01-54__track1_original_dataset_forward_dt_remote_micro_campaign_run`
- `2026-04-26-00-02-47__track1_original_dataset_forward_et_remote_micro_campaign_run`
- `2026-04-26-00-03-39__track1_original_dataset_forward_ert_remote_micro_campaign_run`
- `2026-04-26-00-06-45__track1_original_dataset_forward_gbm_remote_micro_campaign_run`
- `2026-04-26-00-08-45__track1_original_dataset_forward_hgbm_remote_micro_campaign_run`
- `2026-04-26-00-10-19__track1_original_dataset_forward_xgbm_remote_micro_campaign_run`
- `2026-04-26-00-11-16__track1_original_dataset_forward_lgbm_remote_micro_campaign_run`

## Relaunch Objective

Prepare a new full-surface remote mega-campaign from zero.

The campaign remains the approved exact target surface:

- `10` families;
- `2` directions: `forward` and `backward`;
- `20` attempts per family-direction surface;
- `400` total YAML campaign runs.

## Campaign Grid

| Dimension | Value |
| --- | ---: |
| Families | `10` |
| Directions | `2` |
| Attempts per family-direction pair | `20` |
| Total YAML runs | `400` |
| Final family-bank surfaces | `20` |
| Final accepted harmonic models if every surface succeeds | `380` |

## Runtime Policy

| Setting | Value |
| --- | --- |
| Dataset Root | `data/datasets` |
| Split Policy | file-level `70 / 20 / 10` |
| Feature Schema | `rpm`, `deg`, `tor` |
| Runner Branch | `run_original_dataset_exact_model_bank_validation.py` |
| Launch Mode | remote operator launcher |
| `SVR` Search Policy | grid search disabled |
| Other Family Search Policy | paper-reference grid search enabled |

## Artifact Policy

| Surface | Policy |
| --- | --- |
| Old interrupted mega-campaign | discard and never resume |
| Completed micro-campaign | keep as operational gate evidence |
| New mega-campaign identity | fresh campaign name and output root |
| Benchmark promotion | only after later closeout, not at preparation time |

## Expected Outputs

Preparation should generate:

- one micro-campaign completion results report;
- one fresh `400`-run mega-campaign package;
- one refreshed active campaign state payload;
- one exact remote launch command for the new mega-campaign.
