# Track 1 Forward Remote Micro Runner Mismatch Repair And Remote Bringup

## Overview

The prepared `Track 1` forward-only remote micro-campaign currently fails at
the first `SVR` run because the campaign launcher still invokes the legacy
exact-paper validation entrypoint:
`scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`.

The micro-campaign YAML package is instead built on top of the
`original_dataset_exact_model_bank` branch and therefore only provides
`dataset_config_path`, not the legacy recovered-CSV field
`paths.source_dataframe_path`.

This document formalizes the repair needed to make the remote micro-campaign
actually execute on the intended original-dataset branch, then keep iterating
on remote-only fixes until the `10`-run gate campaign completes successfully.

## Technical Approach

The repair must keep the campaign surface narrow and canonical:

1. fix the local and remote launch path so the forward remote micro-campaign
   invokes
   `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`;
2. verify that the active campaign YAML, launcher note, and planning surfaces
   remain aligned with the original-dataset intent;
3. run the repaired micro-campaign on the remote workstation only;
4. if additional failures appear, keep fixing the remote campaign pipeline in
   place until the micro-campaign reaches clean completion;
5. only after the remote gate is green, hand the user the exact launch command
   to reproduce the working flow.

Because the currently prepared campaign protects its launcher and state files,
the implementation requires explicit approval before touching those files.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/run_track1_forward_original_dataset_remote_micro_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.ps1`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/campaigns/track1/exact_paper/prepare_track1_forward_original_dataset_remote_micro_campaign.py`
- `doc/scripts/campaigns/run_track1_forward_original_dataset_remote_micro_campaign.md`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-25-23-00-02_track1_forward_remote_micro_runner_repair_and_remote_bringup_plan_report.md`

## Implementation Steps

1. Confirm the exact mismatch between the prepared micro-campaign YAML schema
   and the runner currently invoked by the local/remote campaign launcher.
2. Repair the launcher path so original-dataset micro-campaign runs execute the
   original-dataset validation entrypoint instead of the legacy recovered-CSV
   entrypoint.
3. Re-prepare the micro-campaign package and keep `active_training_campaign`
   consistent with the repaired launcher contract.
4. Execute the micro-campaign remotely and inspect every failure or warning
   until the `10` prepared runs complete end to end.
5. Update the launcher note and campaign plan if the remote operator contract
   changes during repair.
6. Run the required QA on touched Markdown and the warning-free Sphinx build.
7. Stop before any commit and wait for explicit user approval.
