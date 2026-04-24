# Track 1 Interrupted Remaining Yellow-Cell Manual Sync Checklist

## Campaign Snapshot

- Campaign name: `track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43`
- Canonical local status before closeout: `running`
- Local start timestamp: `2026-04-22T09:14:36+02:00`
- Remote host alias: `xilab-remote`
- Remote repository path: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
- Remote Conda environment: `standard_ml_lan_node`
- Scope for this manual sync: `SVM` only
- Closeout gate: do not update the canonical campaign state, benchmark, or forward-only asset-root migration until the artifact copy below has completed

## Current Local Evidence

- Local SVM campaign output directory present: `False`
- Local SVM validation directory count: `0`
- Local SVM validation report count: `0`
- Interpretation: the interrupted remote wave has not yet been synchronized back into the local repository

## Local Wrapper Logs To Preserve

- `.temp/remote_training_campaigns/2026-04-22-01-49-50_track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43/remote_training_campaign.log`
- `.temp/remote_training_campaigns/2026-04-22-09-13-02_track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43/remote_training_campaign.log`

## Remote Copy Targets

- Copy the full remote SVM campaign output directory first so the run logs, launcher-level bookkeeping, and any partial manifest fragments are preserved together.
- Then copy every exact-paper validation directory created by the interrupted SVM yellow-cell wave.
- Then copy every per-run exact-paper analysis report tied to those validation directories.

- `output/training_campaigns/track1/exact_paper/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/*__track1_svm_*_yellow_cell_attempt_*_campaign_run`
- `doc/reports/analysis/validation_checks/*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md`

## Remote Copy Notes

- The validation directory pattern is intentionally glob-based because the local wrapper log stopped before the remote workstation finished its long autonomous execution.
- The report pattern is also glob-based because the per-run report filenames include remote timestamps that are unknown locally until the files are copied.
- If the remote campaign output directory contains `campaign_manifest.yaml`, keep it with the rest of the campaign directory even if the wrapper never emitted a final sync marker.
- Do not attempt benchmark refresh or artifact pruning during the copy step.

## Family Queue Scope

- Config count expected for the interrupted `SVM` family wave: `180`
- Queue family branches not to copy now: `MLP`, `ET`, `ERT`, `HGBM`, `XGBM`

## Immediate Post-Sync Local Verification

```powershell
Get-ChildItem -LiteralPath 'output\validation_checks\paper_reimplementation_rcim_exact_model_bank' -Directory |
  Where-Object { $_.Name -like '*__track1_svm_*_yellow_cell_attempt_*_campaign_run' } |
  Sort-Object Name |
  Select-Object Name, LastWriteTime
```

```powershell
Get-ChildItem -LiteralPath 'doc\reports\analysis\validation_checks' -File |
  Where-Object { $_.Name -like '*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md' } |
  Sort-Object Name |
  Select-Object Name, LastWriteTime
```

```powershell
Get-ChildItem -LiteralPath 'output\training_campaigns\track1\exact_paper\track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43\logs' -File |
  Sort-Object Name |
  Select-Object -Last 20 Name, LastWriteTime, Length
```

```powershell
Get-ChildItem -LiteralPath 'output\validation_checks\paper_reimplementation_rcim_exact_model_bank' -Directory |
  Where-Object { $_.Name -like '*__track1_svm_*_yellow_cell_attempt_*_campaign_run' } |
  Group-Object { $_.Name -replace '^[0-9-]+__', '' } |
  Where-Object { $_.Count -gt 1 } |
  Select-Object Name, Count
```

## Next Step After Successful Manual Sync

- Run the interrupted-campaign partial closeout from the newly synchronized local artifact set.
- Only after that closeout is completed should the workflow continue with `2026-04-23-23-15-55_post_closeout_forward_asset_root_migration_workflow.md`.
