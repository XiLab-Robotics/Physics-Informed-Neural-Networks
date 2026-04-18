# Track 1 Remaining Family Cellwise Reference Campaigns Launcher

This launcher executes the `9` remaining exact-paper `Track 1` family
cellwise reference campaigns in sequence:

1. `MLP`
2. `RF`
3. `DT`
4. `ET`
5. `ERT`
6. `GBM`
7. `HGBM`
8. `XGBM`
9. `LGBM`

Each family campaign contains `19` target-specific runs, for a total planned
surface of `171` exact-paper cellwise runs.

Local command:

```powershell
.\scripts\campaignsun_track1_remaining_family_cellwise_reference_campaigns.ps1
```

Remote command:

```powershell
.\scripts\campaignsun_track1_remaining_family_cellwise_reference_campaigns.ps1 -Remote
```

For post-interruption recovery, prefer launching the dedicated pending-family
commands directly instead of replaying the full `9`-family aggregate wrapper
from the beginning.
