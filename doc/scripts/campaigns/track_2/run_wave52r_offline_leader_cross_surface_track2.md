# Run Wave 5.2R Offline-Leader Cross-Surface Track 2

## Purpose

This launcher evaluates the completed K01/H08 promotion campaign under the
official multi-index, curve-first policy. It keeps `Fw`, `Bw`, and
direction-aware `global` as three separate matrix runs and preserves periodic
GRU and periodic harmonic MLP as frozen incumbent controls.

The package contains 24 candidates:

- 18 K01/H08 promotion checkpoints: three seeds, three surfaces, two lanes;
- three periodic GRU incumbent surfaces;
- three periodic harmonic MLP incumbent surfaces.

## Commands

Local preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1 `
  -PreflightOnly
```

Local execution:

```powershell
.\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1 `
  -Run
```

Remote preflight only:

```powershell
.\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1 `
  -Remote `
  -PreflightOnly
```

Remote execution:

```powershell
.\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1 `
  -Remote `
  -Run
```

## Decision Boundary

The launcher produces matrix evidence but never promotes a model. After it
finishes, the returned `forward`, `backward`, and `global` packages must be
reviewed with the official policy, visual companions, robustness evidence, and
deployment-readiness gates. Neither incumbent can be deleted or overwritten by
campaign or matrix rank alone.
