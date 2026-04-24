# Track 1 Remaining Yellow-Cell Campaign Progress Monitor

This read-only monitor reports the real aggregate progress of the current
remote exact-paper `Track 1` remaining-yellow-cell bundle.

It is intended for the specific bundle launched through:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_remaining_yellow_cell_campaigns.ps1 -Remote
```

Reported sections:

- family-by-family completed validation count versus expected count;
- total completed validations versus the full `660`-run bundle;
- active remote config path if one validation process is still running;
- latest produced validation directory and latest campaign log;
- duplicate run-name warning, useful for the known early `SVM` retry edge case.

Local SSH form:

```powershell
.\scripts\campaigns\track1\exact_paper\watch_track1_remaining_yellow_cell_campaign_progress.ps1
```

Direct form on the remote workstation:

```powershell
.\scripts\campaigns\track1\exact_paper\watch_track1_remaining_yellow_cell_campaign_progress.ps1 -DirectOnRemote
```

Optional explicit host and repository form:

```powershell
.\scripts\campaigns\track1\exact_paper\watch_track1_remaining_yellow_cell_campaign_progress.ps1 -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
```
