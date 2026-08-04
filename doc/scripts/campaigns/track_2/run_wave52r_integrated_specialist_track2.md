# Run Wave 5.2R Integrated-Specialist Track 2

## Purpose

This launcher evaluates the trained Wave 5.2R integrated-specialist models
under the official multi-index, curve-first policy. It runs `Fw`, `Bw`, and
direction-aware `global` as separate matrices and preserves frozen ingredient
and incumbent controls.

The package contains 29 candidates:

- 21 trained candidates: A02 through A08, each with three seeds;
- frozen K01 global and H08 forward ingredient controls;
- periodic GRU and periodic harmonic MLP controls on all three surfaces.

Campaign-gate failures remain available for diagnosis but are not authorized
for promotion. A02 is the only trained branch that passed the campaign gate.

## Commands

Local preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_integrated_specialist_track2.ps1 `
  -PreflightOnly
```

Local execution:

```powershell
.\scripts\campaigns\track_2\run_wave52r_integrated_specialist_track2.ps1 `
  -Run
```

Remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_integrated_specialist_track2.ps1 `
  -Remote `
  -PreflightOnly
```

Remote execution:

```powershell
.\scripts\campaigns\track_2\run_wave52r_integrated_specialist_track2.ps1 `
  -Remote `
  -Run
```

Recover completed remote matrices after an artifact-transfer failure without
rerunning them:

```powershell
.\scripts\campaigns\track_2\run_wave52r_integrated_specialist_track2.ps1 `
  -Remote `
  -SyncOnly
```

The recovery path selects the newest matching `forward`, `backward`, and
`global` validation directories and reports on the remote repository. It only
bundles and synchronizes those six artifacts.

## Decision Boundary

The launcher produces matrix evidence but never promotes a model. After it
finishes, the returned `forward`, `backward`, and `global` packages must be
reviewed with the official policy, visual evidence, robustness evidence, and
deployment-readiness gates. No accepted registry is changed during package
preparation or matrix execution.
