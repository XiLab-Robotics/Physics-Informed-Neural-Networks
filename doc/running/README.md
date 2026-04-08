# Running Campaign State

This folder stores persistent operational state for ongoing TE model work.

It now has two distinct roles:

- persistent prepared or active training-campaign state;
- the privileged live backlog for the TE model implementation program.
- temporary live state for active or resumable TwinCAT/TestRig video reruns.

Primary operational entry points:

- `running/te_model_live_backlog.md`
  Canonical operational backlog for current status, completed waves, next steps, and deferred branches.
- `running/active_training_campaign.yaml`
  Persistent prepared or active campaign state, including protected files and launch commands.

Current policy:

- one campaign may be tracked as the current campaign state file;
- `status: prepared` means the campaign files and launch command are ready but the user has not yet confirmed execution start;
- `status: running` means the user explicitly confirmed that the campaign has started;
- `status: completed` means the campaign finished and is ready for final reporting;
- `status: cancelled` means the campaign stopped before full completion and needs a partial-results decision.
- `launch_command_list` is the canonical operator handoff surface for prepared campaigns, including LAN-remote campaigns that are executed manually by the user from the terminal after Codex prepares the launcher bundle.

Protected files listed in the state file must not be modified silently while the campaign is active.

Operational guidance:

- treat `running/te_model_live_backlog.md` as the day-to-day source of truth for the TE program execution order;
- keep future TwinCAT deployment-track decisions in that live backlog rather than only in historical technical notes;
- treat the related `doc/technical/` backlog documents as historical planning references rather than as the main operational checklist.
- keep completed video-pipeline tracking files out of the `doc/running/` tree once the rerun is closed; archive them inside the corresponding dated `doc/reports/analysis/` bundle instead.
