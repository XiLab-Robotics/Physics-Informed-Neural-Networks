# Track 1 XGBM Full-Matrix Campaign Launcher

This launcher runs the dedicated `Track 1` exact-paper `XGBM` family campaign.

Included configs:

1. `01_track1_xgbm_amplitude_full_matrix.yaml`
2. `02_track1_xgbm_phase_full_matrix.yaml`

Local command:

```powershell
.\scripts\campaigns\run_track1_xgbm_full_matrix_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
```

Remote preflight now checks that the target Conda environment exposes the
optional `xgboost` Python package and `XGBRegressor` symbol before the actual
exact-paper runtime starts. If that dependency is missing, the launcher fails
early during remote preflight instead of crashing later inside model creation.
