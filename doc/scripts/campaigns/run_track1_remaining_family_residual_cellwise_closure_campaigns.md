# Track 1 Remaining Family Residual Cellwise Closure Campaigns Launcher

This launcher runs the full overnight residual-cell closure sequence for all nine non-`SVM` exact-paper families.

- family launcher count: `9`
- closure attempts per residual target pair: `6`
- total planned runs: `1026`

Remote command:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1 -Remote
```

Explicit remote form:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_track1_remaining_family_residual_cellwise_closure_campaigns.ps1 -Remote -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" -RemoteCondaEnvironmentName "standard_ml_lan_node"
```
