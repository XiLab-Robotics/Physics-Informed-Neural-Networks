# Track 1 Forward Open-Cell Repair Remote Artifact Sync Length Fix

## Overview

The remote `Track 1` forward open-cell repair campaign
`track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10` completed all
`300/300` exact-paper runs successfully, but the wrapper failed during the
final remote-to-local artifact synchronization phase. The failure happened
after the campaign-level success marker was emitted, while the wrapper was
building temporary `.tar` archives on the remote workstation for validation
report artifacts under `doc/reports/analysis/validation_checks/`.

The current evidence indicates that the remote temporary archive filename is
derived from the full slugged relative artifact path, producing an excessively
long staging path under `C:\Temp\standardml_remote_training\...`. The repair
therefore targets the post-run artifact packaging helper rather than the model
training logic.

## Technical Approach

The fix will narrow the remote staging archive naming strategy inside the
shared remote exact-paper campaign wrapper. Instead of materializing temporary
archive names from the full slugged relative path, the wrapper will use a
short deterministic archive name composed from the item index plus a bounded
path hash. This keeps the remote staging path safely below Windows path-length
constraints while preserving deterministic traceability during the sync step.

After the packaging fix, the wrapper will be re-run against the completed
campaign so the missing local artifacts can be synchronized and the campaign
state can be reconciled from `running` to the appropriate final closeout
status. The implementation will keep the fix tightly scoped to the remote
artifact sync phase and will not reinterpret the completed training results.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `doc/running/active_training_campaign.yaml`
- `doc/scripts/campaigns/run_track1_forward_open_cell_repair_campaign.md`
- `output/training_campaigns/track1/exact_paper/forward_open_cell_repair/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/`
- `doc/reports/analysis/validation_checks/`

## Implementation Steps

1. Confirm the completed-run evidence and isolate the failing sync helper in
   the shared remote wrapper.
2. Replace the long remote temporary archive naming scheme with a short,
   deterministic, collision-safe scheme.
3. Verify the updated PowerShell script parses cleanly and that the launcher
   note stays aligned with the real behavior.
4. Re-run the remote synchronization and campaign completion path for the
   already completed `300/300` campaign.
5. Reconcile `doc/running/active_training_campaign.yaml` and any resulting
   closeout surfaces only after the artifact sync succeeds.
