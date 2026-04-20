# Targeted Remote Follow-Up Campaign Preparation

## Overview

This task prepares the next approved LAN-remote training campaign now that the
SSH-backed workflow has already been validated on the stronger workstation.

The goal is to use the stronger machine selectively instead of broadening the
search blindly. The campaign should target the three directions that still have
credible value after the first remote validation pass:

- a deeper or longer `residual_harmonic_mlp` follow-up because it remains the
  strongest neural family;
- a tighter `feedforward` follow-up around the new family best
  `te_feedforward_high_compute_remote`;
- a narrow `hist_gradient_boosting` refinement because the remote deep probe
  landed very close to the global best.

No subagent is planned for this task.

## Technical Approach

The work will stay campaign-oriented and repository-safe.

First, prepare a planning report that defines a narrow mixed campaign for the
LAN workstation. The report will explain why these families are still worth
testing, which parameter axes are being pushed, and why low-value branches such
as broad random-forest sweeps are being excluded.

Second, after approval, generate the campaign YAML package, the dedicated
PowerShell launcher, the launcher note, and the updated running-state entry in
`doc/running/active_training_campaign.yaml`.

Third, provide the exact local command and the step-by-step local and remote
operator instructions required to launch the campaign safely on the stronger
LAN workstation. Only after those preparation steps are complete and explicitly
approved should the real remote execution begin.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/README.md`
- `doc/reports/campaign_plans/`
- `config/training/feedforward/`
- `config/training/residual_harmonic_mlp/`
- `config/training/remote_validation/`
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `scripts/training/run_training_campaign.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/train_residual_harmonic_mlp.py`
- `scripts/training/train_tree_regressor.py`

## Implementation Steps

1. Write the planning report for a targeted LAN-remote follow-up campaign that
   covers `residual_harmonic_mlp`, `feedforward`, and
   `hist_gradient_boosting`.
2. After approval, generate the campaign YAML package and the dedicated remote
   launcher plus its documentation note.
3. Update `doc/running/active_training_campaign.yaml` to register the prepared
   campaign and its protected files.
4. Provide the exact execution command and the step-by-step local and remote
   setup or verification instructions.
5. Wait for explicit approval before executing the remote campaign itself.
