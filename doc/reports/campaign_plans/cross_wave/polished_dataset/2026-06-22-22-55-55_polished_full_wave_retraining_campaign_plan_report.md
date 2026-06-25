# Polished Dataset Full Wave Retraining Campaign Plan

## Campaign Status

Prepared package. Operator execution is required; this plan does not start training.

## Objective

Retrain all non-paper model-development families visible in the current
`TE Curve Verification Pipeline` best-model collage reference using
`polished_dataset`.

The campaign uses canonical future model-family names from commit
`4dff9a28b56824da5f90e38e626e75c9348b842d`.

## Scope

- model families: `36`
- surfaces: `global`, `fw`, `bw`
- training configs: `108`
- excluded: paper-original and paper-retuned reference surfaces
- separate first campaign: `RCIM Model-Bank Reproduction` polished rerun

## Dataset Contract

- dataset: `polished_dataset`
- schema: `polished_point_v1`
- inputs: `theta`, `theta_dot`, `tau_load`, `T`
- target: `theta_TE`
- no filename-derived setpoints are used as model inputs

## Execution Policy

- Local and `-Remote` launch paths are supported.
- Campaign runner uses `--dataset polished_dataset` and the generated
  canonical config queue.
- `--stop-on-error` remains enabled by default.
- Normal closeout must happen before any separate
  `TE Curve Verification Pipeline` refresh.
