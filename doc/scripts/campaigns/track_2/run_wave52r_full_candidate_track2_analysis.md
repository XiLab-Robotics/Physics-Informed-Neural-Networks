# Run Wave 5.2R Full-Candidate Track 2 Analysis

## Purpose

`run_wave52r_full_candidate_track2_analysis.ps1` prepares and runs the bounded
forward-only `TE Curve Verification Pipeline` comparison requested after Wave
5.2R completion.

The frozen inventory contains 125 artifacts:

- 98 matrix-eligible candidates;
- 18 temporal candidates;
- 79 non-temporal candidates;
- one PF-A analytical reference;
- 27 excluded replay, calibration-only, or synthetic-oracle artifacts.

The required accepted references are included:

- periodic GRU as the temporal or windowed incumbent;
- periodic harmonic MLP as the non-temporal reference;
- PF-A as the analytical reference.

All eligible Stage 4 through Stage 12 real-data predictors are included.
Stage 11 trust calibrations and Stage 13 synthetic oracles remain documented in
the inventory but are not presented as distinct real-data TE predictors.

## Safety And Preflight

The launcher defaults to preflight-only behavior. Preflight:

1. rebuilds the inventory and matrix deterministically;
2. verifies the frozen `polished_dataset + setpoints + Fw` split;
3. checks all 97 full curves and 2048 angular samples;
4. validates archive SHA-256 identities;
5. loads all 98 candidates;
6. checks accepted GRU, periodic harmonic MLP, PF-A, H04, and K01 presence;
7. records exact duplicate prediction groups;
8. confirms that the heavy matrix has not executed.

Three groups of separately trained candidates currently produce exact duplicate
prediction matrices. They remain visible in the inventory and matrix so the
experimental record is complete; the final report must not count them as
independent predictive evidence.

## Commands

Run local preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
  -PreflightOnly
```

Run the full matrix locally:

```powershell
.\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
  -Run
```

Run remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
  -Remote `
  -PreflightOnly
```

Run the full matrix on the configured LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
  -Remote `
  -Run
```

The remote path first runs local preflight, packages the exact source and
immutable candidate artifacts, runs the same preflight remotely, executes the
matrix only with `-Run`, and synchronizes the matrix directory and generated
Markdown report back to the local repository.

## Expected Outputs

Preparation and preflight write:

```text
output/analysis/wave_5_2r/full_candidate_track2_analysis/
  candidate_inventory.yaml
  package_preflight_summary.yaml
  remote_source_path_list.txt
```

The matrix run writes:

```text
output/validation_checks/track2_reference_comparison/
  <timestamped full-candidate matrix directory>/

doc/reports/analysis/validation_checks/te_curve_verification_pipeline/
  <timestamped full-candidate matrix report>.md

output/validation_checks/track2_operator_launch_logs/
  <timestamped launcher log root>/
```

## Closeout Boundary

Do not select a winner from the launcher terminal output. After completion,
inspect the returned matrix under the multi-index curve-first policy, generate
the CVP diagnostics and visual comparisons, and report temporal and
non-temporal leaders separately before making a cross-lane recommendation.
