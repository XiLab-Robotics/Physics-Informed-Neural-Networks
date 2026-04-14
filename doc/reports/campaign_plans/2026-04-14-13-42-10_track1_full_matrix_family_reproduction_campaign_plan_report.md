# Track 1 Full Matrix Family Reproduction Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign under the clarified
full-matrix reproduction objective.

The campaign is not a narrow open-cell repair batch and not a single-winner
search.

Its purpose is to prepare a reproducible paper-faithful campaign program that
can answer this question:

1. for each paper model family and for each paper harmonic target, can the
   repository reproduce the paper tables through its own implementations under
   the exact-paper workflow.

The requested campaign surface is organized by:

- family;
- metric group;
- harmonic coverage.

## Current Technical Constraint

The exact-paper runner currently supports:

- exact-paper dataset reuse;
- enabled-family filtering;
- stable validation-summary serialization;
- ONNX export on the exact family bank.

It does not yet expose a clean config surface for:

- amplitude-only target runs;
- phase-only target runs;
- per-harmonic filtering.

Therefore, this campaign plan assumes one minimal workflow extension before the
campaign package itself is generated.

## Campaign Principle

The campaign should be prepared as one umbrella campaign with many explicit
sub-runs.

The most practical first prepared layer is:

- one amplitude run for each family across all amplitude harmonics;
- one phase run for each family across all phase harmonics.

This produces a first complete matrix-reproduction pass without exploding into
an immediately unmanageable number of micro-runs.

Then, if needed, a second prepared layer can add:

- targeted harmonic repair runs for families whose first pass still leaves
  materially red cells in the matrix dashboard.

## Requested Family Scope

The user requested the campaign program to cover these paper families:

- `SVM`
- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

## Requested Target Scope

The user requested both target groups:

- amplitudes;
- phases.

For campaign preparation, the natural exact-paper grouping is:

- amplitude targets:
  `A_0`, `A_1`, `A_3`, `A_39`, `A_40`, `A_78`, `A_81`, `A_156`, `A_162`,
  `A_240`
- phase targets:
  `phi_0`, `phi_1`, `phi_3`, `phi_39`, `phi_40`, `phi_78`, `phi_81`,
  `phi_156`, `phi_162`, `phi_240`

Note:

- the paper Tables `4` and `5` expose phase results only for
  `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240`;
- the exact-paper runner still carries `phase_0`, so the campaign package
  should state explicitly whether `phase_0` is included as a workflow-level
  exact target or omitted from paper-facing summary scoring.

## Candidate Campaign Structure

### Layer 1 - Base Matrix Reproduction Runs

| Config ID | Run Name | Family Scope | Target Scope | Purpose |
| --- | --- | --- | --- | --- |
| 1 | `track1_svm_amplitude_full_matrix` | `SVR` | amplitudes | Reproduce the Table `3` `SVM` row with repository-owned `SVR` models across all amplitude harmonics. |
| 2 | `track1_svm_phase_full_matrix` | `SVR` | phases | Reproduce the phase-side `SVM` row across all phase harmonics kept by the exact-paper workflow. |
| 3 | `track1_mlp_amplitude_full_matrix` | `MLP` | amplitudes | Reproduce the Table `3` `MLP` row. |
| 4 | `track1_mlp_phase_full_matrix` | `MLP` | phases | Reproduce the phase-side `MLP` row. |
| 5 | `track1_rf_amplitude_full_matrix` | `RF` | amplitudes | Reproduce the Table `3` `RF` row. |
| 6 | `track1_rf_phase_full_matrix` | `RF` | phases | Reproduce the phase-side `RF` row. |
| 7 | `track1_dt_amplitude_full_matrix` | `DT` | amplitudes | Reproduce the Table `3` `DT` row. |
| 8 | `track1_dt_phase_full_matrix` | `DT` | phases | Reproduce the phase-side `DT` row. |
| 9 | `track1_et_amplitude_full_matrix` | `ET` | amplitudes | Reproduce the Table `3` `ET` row. |
| 10 | `track1_et_phase_full_matrix` | `ET` | phases | Reproduce the phase-side `ET` row. |
| 11 | `track1_ert_amplitude_full_matrix` | `ERT` | amplitudes | Reproduce the Table `3` `ERT` row. |
| 12 | `track1_ert_phase_full_matrix` | `ERT` | phases | Reproduce the phase-side `ERT` row. |
| 13 | `track1_gbm_amplitude_full_matrix` | `GBM` | amplitudes | Reproduce the Table `3` `GBM` row. |
| 14 | `track1_gbm_phase_full_matrix` | `GBM` | phases | Reproduce the phase-side `GBM` row. |
| 15 | `track1_hgbm_amplitude_full_matrix` | `HGBM` | amplitudes | Reproduce the Table `3` `HGBM` row. |
| 16 | `track1_hgbm_phase_full_matrix` | `HGBM` | phases | Reproduce the phase-side `HGBM` row. |
| 17 | `track1_xgbm_amplitude_full_matrix` | `XGBM` | amplitudes | Reproduce the Table `3` `XGBM` row. |
| 18 | `track1_xgbm_phase_full_matrix` | `XGBM` | phases | Reproduce the phase-side `XGBM` row. |
| 19 | `track1_lgbm_amplitude_full_matrix` | `LGBM` | amplitudes | Reproduce the Table `3` `LGBM` row. |
| 20 | `track1_lgbm_phase_full_matrix` | `LGBM` | phases | Reproduce the phase-side `LGBM` row. |

### Layer 2 - Optional Follow-Up Repair Runs

This second layer should not be generated blindly unless the user wants the
larger package now.

Its role would be:

- duplicate one family/metric run with adjusted seeds or settings when the
  first pass stays materially red;
- or narrow the target set to one harmonic subset for harder rows.

For now, the planning report keeps Layer 2 conceptual only, because the user
first asked to prepare the main family-by-family campaign package.

## Candidate Configuration Table

| Campaign Layer | Run Count | Notes |
| --- | ---: | --- |
| Base matrix reproduction | `20` | One run per family x metric-group pair. |
| Optional repair follow-ups | `0+` | Add only after the first matrix pass identifies persistent red cells. |

## Why This Packaging Is Reasonable

This plan is large, but still bounded and inspectable.

It avoids two bad extremes:

- one giant all-family run that hides row-level reproduction quality;
- a fully exploded family x metric x harmonic micro-grid that would be too
  heavy to prepare and operate as the first approved package.

The prepared `20`-run base matrix gives:

- one row-faithful reproduction attempt per family;
- separate amplitude and phase readouts;
- direct updateability of the matrix dashboard in the benchmark report.

## Evaluation Rules

Each completed run must be interpreted through:

1. row-level reproduction of the corresponding paper family;
2. per-cell status against the paper matrix values;
3. number of green, yellow, and red cells in that family row;
4. whether any optional follow-up repair run is justified.

The campaign summary should explicitly report:

- row-level green/yellow/red counts;
- the worst remaining harmonics in each family row;
- whether the row is already usable for Table `3`, `4`, or `5`
  replication claims.

## Operator Deliverables

After approval, the preparation phase must generate:

1. a campaign config package under
   `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`;
2. a dedicated PowerShell launcher under `scripts/campaigns/`;
3. a matching launcher note under `doc/scripts/campaigns/`;
4. updated `doc/running/active_training_campaign.yaml`;
5. the exact terminal launch command.

## Execution Gate

Before this campaign is generated or launched:

1. the technical document must be approved;
2. this planning report must be approved;
3. the exact-paper target-scope extension must be approved because the current
   runner does not yet support the requested amplitude-only / phase-only split;
4. the config package, launcher, launcher note, and active-campaign state must
   all be created coherently.

## Next Step

After approval of this planning package, generate the target-scope workflow
extension, the campaign YAML set, the dedicated launcher, the launcher note,
and the final PowerShell command to run the umbrella family-reproduction
campaign.
