# Track 1 Interrupted Remaining Yellow-Cell Artifact Sync

Use this helper after the long remote `SVM` branch of the interrupted
remaining-yellow-cell bundle has been stopped and the local repository still
has no synchronized `SVM` artifacts.

This helper performs only the manual artifact recovery step. It does not:

- update `doc/running/active_training_campaign.yaml`;
- run campaign closeout;
- refresh benchmarks or registries;
- start the forward-only asset-root migration.

## Command

```powershell
.\scripts\campaigns\track1\exact_paper\sync_track1_interrupted_remaining_yellow_cell_campaign_artifacts.ps1
```

Optional explicit remote form:

```powershell
.\scripts\campaigns\track1\exact_paper\sync_track1_interrupted_remaining_yellow_cell_campaign_artifacts.ps1 -RemoteHostAlias "xilab-remote" -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
```

Optional keep-remote-archives form:

```powershell
.\scripts\campaigns\track1\exact_paper\sync_track1_interrupted_remaining_yellow_cell_campaign_artifacts.ps1 -SkipRemoteCleanup
```

## What It Pulls

- `output/training_campaigns/track1/exact_paper/forward/remaining_yellow_cells/svm/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/*__track1_svm_*_yellow_cell_attempt_*_campaign_run`
- `doc/reports/analysis/validation_checks/*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md`

## Output Behavior

- stages downloaded tar payloads under `.temp/manual_sync_track1_svm/<timestamp>/`
- extracts the payloads into the local repository root
- prints the resulting local counts for validation directories, validation
  reports, and campaign logs

## Next Step

After the script completes successfully, run the interrupted-campaign partial
closeout from the synchronized local artifact set.
