# Track 1 LGBM Full-Matrix Campaign Launcher

This launcher runs the dedicated `Track 1` exact-paper `LGBM` family campaign.

Included configs:

1. `01_track1_lgbm_amplitude_full_matrix.yaml`
2. `02_track1_lgbm_phase_full_matrix.yaml`

Local command:

```powershell
.\scripts\campaigns\run_track1_lgbm_full_matrix_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
```

Remote preflight now checks that the target Conda environment exposes the
optional `lightgbm` Python package and `LGBMRegressor` symbol before the
actual exact-paper runtime starts. If that dependency is missing, the launcher
fails early during remote preflight instead of crashing later inside model
creation.
