# Run Wave 5.2R Offline Leader Cross-Surface Promotion

## Purpose

This launcher validates and executes the approved K01 and H08 promotion
campaign on `polished_dataset + setpoints` across `Fw`, `Bw`, and `global`.
It trains three seeds per surface for each promotion candidate and one matched
H04 anchor per surface and seed.

The campaign contains:

- 18 K01/H08 promotion runs;
- 9 internal H04 anchor runs;
- 27 total immutable runs.

The periodic GRU and periodic harmonic MLP remain frozen operational controls.
No scalar campaign winner can replace them without a later direction-separated
TE Curve Verification Pipeline decision and deployment acceptance.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 `
  -PreflightOnly
```

## Local Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 `
  -Run
```

## Remote Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 `
  -Remote -PreflightOnly
```

## Remote Run

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 `
  -Remote -Run
```

The remote path synchronizes repository source, configuration, documentation,
the frozen split and foundation evidence, and the passed local promotion
package. The remote workstation must already contain `data/polished_dataset`.
After completion it returns the campaign package, every new run directory,
preflight evidence, queue end state, and active-campaign state.

## Outputs

- `output/training_campaigns/<run_instance_id>/`
- `output/training_runs/complex_harmonic_coefficient_residuals/<run_instance_id>/`
- `output/training_runs/temporal_analytical_residual_models/<run_instance_id>/`
- `output/validation_checks/wave52r_offline_leader_cross_surface_promotion/`
- `doc/running/active_training_campaign.yaml`

## Closeout Boundary

After the launcher completes, normal campaign closeout must create the
campaign-results Markdown/PDF package and synchronize registries and status.
The heavy `Fw/Bw/global` TE Curve Verification Pipeline remains a separate
operator-launched step.
