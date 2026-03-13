# Running Campaign State

This folder stores persistent state for prepared or active training campaigns.

Current policy:

- one campaign may be tracked as the current campaign state file;
- `status: prepared` means the campaign files and launch command are ready but the user has not yet confirmed execution start;
- `status: running` means the user explicitly confirmed that the campaign has started;
- `status: completed` means the campaign finished and is ready for final reporting;
- `status: cancelled` means the campaign stopped before full completion and needs a partial-results decision.

Protected files listed in the state file must not be modified silently while the campaign is active.
