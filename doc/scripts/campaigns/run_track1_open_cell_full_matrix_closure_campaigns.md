# Track 1 Open-Cell Full-Matrix Closure Campaigns Launcher

This launcher runs the full overnight open-cell closure sequence for all
nine non-`SVM` exact-paper families under the canonical `Track 1` table
replication focus.

- family launcher count: `9`
- unresolved family-target pairs: `28`
- closure attempts per unresolved pair: `27`
- total planned runs: `756`

If the first launch already completed `MLP` and only the remote wrapper failed
during artifact reconciliation, use the dedicated resume launcher instead of
replaying the full sequence:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1 -Remote
```

Remote command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns.ps1 -Remote
```

Explicit remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns.ps1 -Remote -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" -RemoteCondaEnvironmentName "standard_ml_lan_node"
```
