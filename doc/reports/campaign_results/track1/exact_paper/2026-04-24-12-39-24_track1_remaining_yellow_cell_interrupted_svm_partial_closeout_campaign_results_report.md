# Track 1 Remaining Yellow-Cell Interrupted SVM Partial Closeout Campaign Results Report

## Overview

This report closes the synchronized local subset of the interrupted
remaining-yellow-cell exact-paper bundle prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-22-01-40-43_track1_remaining_yellow_cell_multi_family_campaign_bundle_plan_report.md`

The local workstation crashed while the remote `SVM` branch was still running.
The remote process continued autonomously for an extended period, was later
stopped manually, and the produced artifacts were then synchronized back into
the local repository with the dedicated manual recovery helper.

This is therefore an interrupted partial closeout, not a full closeout of the
six-family overnight bundle.

- synchronized family scope: `SVM` only
- expected `SVM` queue size: `180`
- synchronized validation directories: `81`
- synchronized distinct run names: `80`
- synchronized per-run reports: `79`
- synchronized campaign logs: `80`
- completed report-backed runs: `79`
- known duplicate retry groups: `1`
- interrupted tail runs without final report: `1`

## Manual Sync Outcome

- local sync helper:
  `scripts/campaigns/track1/exact_paper/sync_track1_interrupted_remaining_yellow_cell_campaign_artifacts.ps1`
- sync staging root:
  `.temp/manual_sync_track1_svm/2026-04-24-12-30-27/`
- synchronized campaign output root:
  `output/training_campaigns/track1/exact_paper/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43/`

The manual sync recovered the interrupted `SVM` branch cleanly enough for a
formal partial closeout:

- the `SVM` campaign log surface is present locally;
- the completed exact-paper validation directories are present locally;
- the completed per-run Markdown validation reports are present locally;
- the batch tail can be classified precisely from the synchronized logs and
  artifact shapes.

## Run Inventory

### Completed Report-Backed Runs

- `79` synchronized run instances reached the normal exact-paper reporting
  stage and expose:
  - `validation_summary.yaml`
  - `paper_family_model_bank.pkl`
  - per-run Markdown validation report

The completed subset covers:

- `A40` attempts `01-60`
- `A240` attempts `01-19`

### Duplicate Early Retry

The synchronized validation surface contains one known duplicate retry group:

- `track1_svm_amplitude_40_yellow_cell_attempt_01_campaign_run`

The earlier instance:

- `2026-04-22-01-51-11__track1_svm_amplitude_40_yellow_cell_attempt_01_campaign_run`

is the pre-alias-fix remote start and contains only:

- `run_metadata.yaml`
- `training_config.yaml`

The accepted rerun instance:

- `2026-04-22-09-14-36__track1_svm_amplitude_40_yellow_cell_attempt_01_campaign_run`

is the valid post-fix branch member and has the normal campaign log plus full
reported output shape.

### Interrupted Tail

The final synchronized `SVM` tail member is:

- `080_track1_svm_amplitude_240_yellow_cell_attempt_20`

Its validation directory:

- `2026-04-24-07-20-37__track1_svm_amplitude_240_yellow_cell_attempt_20_campaign_run`

contains only:

- `run_metadata.yaml`
- `training_config.yaml`

It does not contain:

- `validation_summary.yaml`
- `paper_family_model_bank.pkl`
- final Markdown validation report

The corresponding campaign log ends with a non-zero `conda run` failure from
the exact-paper validation entrypoint, so this tail member must be classified
as interrupted and not as a completed scientific result.

## Candidate Scientific Gains

The synchronized completed subset materially improved the two `SVM`
amplitude-side yellow targets that were actually executed before the stop.

### Harmonic 40

Current accepted canonical baseline:

- accepted `MAE`: `8.20e-05`
- accepted `RMSE`: `9.63e-05`
- current accepted source run:
  `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro`

Best synchronized candidates:

| Candidate | Run Instance | MAE | RMSE | Notes |
| --- | --- | ---: | ---: | --- |
| Best MAE | `2026-04-22-09-14-50__track1_svm_amplitude_40_yellow_cell_attempt_02_campaign_run` | `7.20078e-05` | `9.22599e-05` | beats current baseline on both metrics |
| Best RMSE | `2026-04-22-09-19-50__track1_svm_amplitude_40_yellow_cell_attempt_23_campaign_run` | `7.56487e-05` | `9.04386e-05` | beats current baseline on both metrics |

### Harmonic 240

Current accepted canonical baseline:

- accepted `MAE`: `2.52e-04`
- accepted `RMSE`: `4.86e-04`
- current accepted source run:
  `2026-04-14-17-31-04__track1_svm_amplitude_repair_seed23_campaign_run`

Best synchronized candidates:

| Candidate | Run Instance | MAE | RMSE | Notes |
| --- | --- | ---: | ---: | --- |
| Best MAE | `2026-04-23-12-12-12__track1_svm_amplitude_240_yellow_cell_attempt_12_campaign_run` | `2.49252e-04` | `4.62395e-04` | beats current baseline on both metrics |
| Best RMSE | `2026-04-22-14-43-54__track1_svm_amplitude_240_yellow_cell_attempt_03_campaign_run` | `2.80127e-04` | `4.04452e-04` | improves RMSE strongly but regresses MAE against the current accepted baseline |

## Promotion Decision

This partial closeout intentionally stops before any benchmark or reference
archive promotion.

The synchronized `SVM` branch clearly produced numerically stronger candidates
for `A40` and `A240`, but the batch does not yet satisfy the promotion
requirements for a clean canonical benchmark refresh because:

- the `SVM phase 162` yellow target was never reached;
- the interrupted tail means the branch did not complete the intended `SVM`
  sub-campaign;
- the completed candidate runs did not produce the normal promoted reference
  export surface expected by the existing `SVM` archive bookkeeping;
- for `A40`, the best `MAE` and best `RMSE` come from different attempts, so
  winner promotion should be decided in one explicit follow-up promotion step
  instead of being coupled implicitly to this interrupted batch closeout.

Repository consequence for this closeout:

- campaign state: close the interrupted bundle bookkeeping;
- benchmark state: unchanged in this step;
- `SVM` reference archive state: unchanged in this step;
- candidate gains: preserved and documented for the next explicit promotion or
  follow-up wave.

## Remaining Open Scope

The interrupted overnight bundle still has no synchronized executed artifacts
for:

- `SVM phase 162`
- `MLP`
- `ET`
- `ERT`
- `HGBM`
- `XGBM`

Therefore the six-family overnight bundle remains scientifically incomplete and
this report must be read as `SVM-only partial closeout`.

## Next Step

This interrupted partial closeout completes the artifact recovery and
bookkeeping phase needed to release the campaign protection lock.

The next repository step can now move to the deferred post-closeout workflow
documented in:

- `doc/technical/2026-04/2026-04-23/2026-04-23-23-15-55_post_closeout_forward_asset_root_migration_workflow.md`

Any later decision to promote the `SVM A40` and `SVM A240` candidate gains
should be handled as a separate explicit promotion step after that migration or
in a dedicated `SVM` follow-up closeout.
