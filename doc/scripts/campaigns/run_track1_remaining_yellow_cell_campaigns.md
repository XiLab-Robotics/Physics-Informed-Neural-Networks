# Track 1 Remaining Yellow-Cell Campaigns Launcher

This launcher runs the overnight yellow-cell closure sequence for the six
still-open exact-paper families under the canonical Track 1 family-row
replication focus.

- family launcher count: `6`
- unresolved yellow family-target pairs: `11`
- closure attempts per pair: `60`
- total planned runs: `660`

Family order:

- `SVM`
- `MLP`
- `ET`
- `ERT`
- `HGBM`
- `XGBM`

Remote command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_remaining_yellow_cell_campaigns.ps1 -Remote
```

Explicit remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_remaining_yellow_cell_campaigns.ps1 -Remote -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" -RemoteCondaEnvironmentName "standard_ml_lan_node"
```
