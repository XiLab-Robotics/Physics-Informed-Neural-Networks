# Track 1 Remaining Family Full-Matrix Campaigns Launcher

This launcher executes the `9` remaining exact-paper `Track 1` family
campaigns in sequence:

1. `MLP`
2. `RF`
3. `DT`
4. `ET`
5. `ERT`
6. `GBM`
7. `HGBM`
8. `XGBM`
9. `LGBM`

Local command:

```powershell
.\scripts\campaigns\run_track1_remaining_family_full_matrix_campaigns.ps1
```

Remote command:

```powershell
.\scripts\campaigns\run_track1_remaining_family_full_matrix_campaigns.ps1 -Remote
```

For post-interruption recovery, prefer launching the dedicated pending-family
commands directly instead of replaying the full `9`-family aggregate wrapper
from the beginning:

```powershell
.\scripts\campaigns\run_track1_xgbm_full_matrix_campaign.ps1 -Remote
.\scripts\campaigns\run_track1_lgbm_full_matrix_campaign.ps1 -Remote
```

The shared remote exact-paper launcher now performs optional-dependency
preflight for family-specific packages such as `xgboost` and `lightgbm`
before the remote runtime begins.
