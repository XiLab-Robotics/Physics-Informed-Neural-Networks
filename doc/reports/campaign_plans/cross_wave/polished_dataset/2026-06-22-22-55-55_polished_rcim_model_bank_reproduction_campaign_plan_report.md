# Polished Dataset RCIM Model-Bank Reproduction Campaign Plan

## Campaign Status

Prepared package. Operator execution is required; this plan does not start training.

## Objective

Rerun the old `Track 1` paper-reimplementation branch, now named
`RCIM Model-Bank Reproduction`, on `polished_dataset` measured curves.

The campaign uses the polished rows to reconstruct curve-level harmonic
targets and curve-level operating features from measured columns. It is a
polished reproduction of the RCIM model-bank workflow, not a frozen paper
original or paper-retuned reference run.

## Dataset Contract

- dataset: `polished_dataset`
- schema: `polished_point_v1`
- measured inputs: `theta`, `theta_dot`, `tau_load`, `T`
- measured target: `theta_TE`
- RCIM curve-level operating features are derived from measured curve
  medians of `theta_dot`, `tau_load`, and `T`.

## Run Matrix

| Surface | Config | Families |
| --- | --- | --- |
| `fw` | `rcim_model_bank_reproduction_polished_dataset_fw.yaml` | SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM |
| `bw` | `rcim_model_bank_reproduction_polished_dataset_bw.yaml` | SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM |

## Execution Policy

- Local and `-Remote` launch paths are supported.
- Heavy training is operator-run only.
- Normal closeout must produce campaign results and registry/status
  synchronization before any separate `TE Curve Verification Pipeline` refresh.
