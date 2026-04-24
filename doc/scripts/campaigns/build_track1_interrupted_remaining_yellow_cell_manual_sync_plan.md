# Build Track 1 Interrupted Remaining Yellow-Cell Manual Sync Plan

Use this helper when the remote `Track 1` remaining-yellow-cell bundle was
interrupted after a long autonomous `SVM` run and the local repository still
has no synchronized `SVM` artifacts.

## Command

```powershell
python -B scripts/training/build_track1_interrupted_remaining_yellow_cell_manual_sync_plan.py
```

## Output

- `doc/running/track1_interrupted_remaining_yellow_cell_manual_sync_checklist.md`

## Purpose

- reads the canonical campaign state from `doc/running/active_training_campaign.yaml`;
- confirms the interrupted bundle identity;
- emits the remote copy targets that must be synchronized before partial
  closeout;
- records the local wrapper logs that should be preserved as bookkeeping
  evidence;
- provides the post-sync local verification commands needed before closeout.
