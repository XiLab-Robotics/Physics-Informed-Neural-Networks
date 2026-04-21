# Track 1 Open-Cell Full-Matrix Closure Campaigns Relaunch After MLP

This launcher resumes the interrupted overnight `Track 1` open-cell
full-matrix campaign after the first launch completed the full `MLP` family
batch but stopped during remote artifact reconciliation.

- resumed families: `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`
- skipped family: `MLP`
- reason for resume split: remote wrapper report-path mismatch after completed
  `MLP`

Remote relaunch command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1 -Remote
```

Explicit remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1 -Remote -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" -RemoteCondaEnvironmentName "standard_ml_lan_node"
```
