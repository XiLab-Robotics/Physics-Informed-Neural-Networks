# Track 1 XGBM LGBM Recovery V2 Plan Report

## Overview

This planning report defines the next narrow recovery step for the pending
`Track 1` families:

- `XGBM`
- `LGBM`

The latest rerun attempt confirmed that the remote environment is no longer the
only blocker. The current pending issues are:

1. remote optional-dependency preflight is malformed and does not behave as a
   reliable gate;
2. the repository-owned exact-paper `XGBM` grid builder crashes on
   `learning_rate=None`.

The already completed seven family campaigns remain untouched.

## Failure Breakdown

### Remote Preflight Layer

The remote launcher output shows:

`conda.bat : ScriptBlock should only be specified as a value of the Command parameter.`

Yet the wrapper continues into sync and remote launch. This means the preflight
is not currently acting as a real stop condition and must be repaired before it
can be trusted for `XGBM/LGBM`.

### Exact-Paper Family Builder Layer

The `XGBM` runtime now fails later inside:

- `build_exact_paper_reference_parameter_grid`

because:

- `base_estimator.get_params()["learning_rate"]` is `None`
- the code immediately applies `float(...)`

This is a compatibility/runtime robustness issue in the repository-owned
exact-paper support code, not a user environment issue.

## Narrow Recovery Scope

Allowed scope in this pass:

- shared remote exact-paper launcher repair;
- exact-paper model-bank support repair for `XGBM/LGBM` parameter fallback
  handling;
- launcher-note alignment only if wording must reflect the corrected behavior.

Out of scope:

- changing the campaign YAML files;
- changing family lists;
- changing benchmark reports before successful reruns;
- re-running the seven already closed families.

## Intended Post-Fix Commands

After this repair, the commands should remain:

```powershell
.\scripts\campaigns\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
.\scripts\campaigns\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
```

## Acceptance Criteria

This recovery v2 repair is complete only when:

1. remote preflight correctly identifies `XGBM/LGBM` optional dependencies;
2. remote preflight no longer emits the current malformed `conda.bat`
   binding error;
3. the `XGBM` exact-paper builder no longer crashes on `learning_rate=None`;
4. both recovery commands are ready for another rerun without changing the
   campaign package itself.

## Approval Gate

Implementation should begin only after explicit approval of:

1. the technical document;
2. this recovery-v2 planning report;
3. the additional edits to the protected shared launcher and exact-paper
   support script.
