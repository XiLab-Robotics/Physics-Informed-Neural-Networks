# Track 1 Forward Original-Dataset Remote Diagnostic Campaign Plan

## Overview

This plan defines a small remote diagnostic campaign that supersedes the
interrupted `400`-run bidirectional mega-campaign long enough to validate the
current repair set on the remote workstation.

The package intentionally contains only `10` runs in total: one `forward`
training-validation run for each of the `10` exact-paper families.

## Objectives

- verify that the repaired ONNX export path no longer fails with misleading
  `NoneType` errors on the remote node;
- verify that the extended remote preflight catches missing ONNX dependencies
  before training starts;
- inspect the real warning surface emitted by one run per family on the remote
  workstation;
- confirm that the updated `MLP` iteration budget reduces the repeated
  convergence-cap warnings observed in the interrupted campaign.

## Scope

- direction: `forward`
- family count: `10`
- attempts per family: `1`
- total runs: `10`
- random seed: `42`
- launch mode: `remote_operator_launcher`
- remote host alias: `xilab-remote`
- remote conda environment: `standard_ml_lan_node`

## Queue Surface

| Family | Direction | Attempts |
| --- | --- | --- |
| `SVR` | `forward` | `1` |
| `MLP` | `forward` | `1` |
| `RF` | `forward` | `1` |
| `DT` | `forward` | `1` |
| `ET` | `forward` | `1` |
| `ERT` | `forward` | `1` |
| `GBM` | `forward` | `1` |
| `HGBM` | `forward` | `1` |
| `XGBM` | `forward` | `1` |
| `LGBM` | `forward` | `1` |

## Outputs

- campaign output root under `output/training_campaigns/track1/exact_paper/forward/`
- validation artifacts under
  `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic`
- canonical remote launcher log under `.temp/remote_training_campaigns/`

## Approval And Execution Rule

This diagnostic campaign exists only to validate the remote repair surface. If
the `10` runs complete cleanly enough, the next step is to re-prepare and
relaunch the full bidirectional mega-campaign with the same repaired launcher
and ONNX contract.
