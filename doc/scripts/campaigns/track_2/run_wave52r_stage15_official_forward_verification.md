# Run Wave 5.2R Stage 15 Official Forward Verification

## Purpose

`run_wave52r_stage15_official_forward_verification.ps1` runs the separate
forward-only `TE Curve Verification Pipeline` matrix required by Wave 5.2R
Stage 15. It compares:

- the nominated `H04` bounded coefficient-residual model;
- its frozen Polynomial-Fourier `PF-A` analytical anchor;
- the accepted forward periodic harmonic MLP;
- the accepted forward periodic GRU incumbent.

The launcher does not accept or register `H04`. It generates the common-surface
evidence that must be inspected before any acceptance decision.

## Safety And Preflight

The default invocation runs preflight only. The preflight:

- verifies every required path;
- checks SHA-256 identities for the H04 checkpoint, training configuration, and
  PF-A anchor;
- reloads H04 through the production comparison adapter;
- reproduces all 97 frozen Stage 5 test curves;
- requires a maximum replay difference no larger than `1e-6 deg`;
- confirms that the accepted reference inventories exist.

Native Conda/PyTorch warnings written to `stderr` are preserved in the launcher
log but are not treated as failures by themselves. The launcher fails only
when the real Conda process exit code is non-zero.

Pass `-Run` explicitly to execute the heavy matrix.

## Commands

Run local preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1 `
    -PreflightOnly
```

Run the official matrix locally:

```powershell
.\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1 `
    -Run
```

Run remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1 `
    -Remote `
    -PreflightOnly
```

Run the official matrix on the remote LAN workstation:

```powershell
.\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1 `
    -Remote `
    -Run
```

The remote path synchronizes the required source, configuration, documentation,
checkpoint, analytical anchor, split manifest, and accepted model inventories
before execution. It synchronizes the generated matrix directory and Markdown
matrix report back into the local repository after successful completion.

## Expected Outputs

Preflight writes:

```text
output/analysis/wave_5_2r/stage15_official_forward_verification/
  stage15_package_preflight.yaml
```

The official run writes:

```text
output/validation_checks/track2_reference_comparison/
  <immutable Stage 15 run instance>/

doc/reports/analysis/validation_checks/te_curve_verification_pipeline/
  <timestamped Stage 15 matrix report>.md

output/validation_checks/track2_operator_launch_logs/
  <timestamped Stage 15 launcher log root>/
```

## Closeout Boundary

After the launcher reports success, do not select a winner from the terminal
summary alone. The returned payload must be inspected under the canonical
multi-index curve-first policy. Stage 15 then generates the dedicated overlays,
collages, official decision report, validated PDF, deployment parity evidence,
and any justified registry/status updates.
