# Track 1 XGBM LGBM Recovery Launcher Micro Fix Plan Report

## Overview

This planning report covers the immediate launcher-only repair needed after the
first `XGBM` and `LGBM` recovery rerun attempt failed locally before reaching
the remote workstation.

The remote Conda environment issue appears already addressed by the user
through installation of:

- `xgboost`
- `lightgbm`

The new blocker is instead a local PowerShell runtime error inside the shared
remote exact-paper launcher:

`System.ArgumentException: Argument types do not match`

Because the failure happens before the remote host preflight begins, there is
no reason to alter the campaign YAML files, run scopes, or benchmark surfaces
at this stage.

## Failure Scope

The error occurs while constructing the optional dependency specification list
for pending-family recovery:

| Layer | Status |
| --- | --- |
| Remote environment package installation | assumed repaired by user |
| Shared remote launcher | failing locally |
| `XGBM` exact-paper campaign configs | unchanged |
| `LGBM` exact-paper campaign configs | unchanged |

This confirms that the next action should be a launcher-only repair.

## Narrow Repair Rule

The micro-fix should not widen scope beyond the launcher helper itself.

Allowed scope:

- repair the helper return/build logic;
- keep the same dependency mapping and preflight behavior;
- preserve the same user-facing commands.

Disallowed scope for this step:

- changing `Track 1` model configs;
- changing family hyperparameters;
- changing exact-paper Python training logic;
- updating benchmark or closeout reports before reruns actually succeed.

## Intended Post-Fix Commands

Once the launcher micro-fix is applied, the recovery commands remain:

```powershell
.\scripts\campaigns\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
.\scripts\campaigns\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
```

## Acceptance Criteria

The launcher micro-fix step is complete only when:

1. the shared remote exact-paper launcher no longer throws the local
   `Argument types do not match` exception;
2. PowerShell parser validation succeeds on the repaired launcher;
3. the two recovery commands are ready to be re-run without changing the
   campaign package.

## Approval Gate

Implementation should begin only after explicit approval of:

1. the technical micro-fix document;
2. this launcher micro-fix plan report;
3. the narrow repair scope on the protected campaign launcher files.
