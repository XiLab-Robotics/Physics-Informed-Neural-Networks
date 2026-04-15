# 2026-04-15 Technical Documents

- [2026-04-15-12-03-49_exact_paper_runner_progress_logging_standardization.md](./2026-04-15-12-03-49_exact_paper_runner_progress_logging_standardization.md)
  Technical document for making the exact-paper runner emit frequent
  phase-level and per-family progress lines so long `GridSearchCV` runs become
  observable through the streaming campaign launcher.
- [2026-04-15-13-55-05_campaign_launcher_interruptible_stop_and_progress_heartbeat.md](./2026-04-15-13-55-05_campaign_launcher_interruptible_stop_and_progress_heartbeat.md)
  Technical document for hardening the shared streaming campaign launcher with
  operator-stop handling and a terminal-only heartbeat during long silent child
  phases.
- [2026-04-15-14-14-36_track1_svr_remote_lan_campaign_execution.md](./2026-04-15-14-14-36_track1_svr_remote_lan_campaign_execution.md)
  Technical document for executing the already prepared `Track 1` `SVR`
  reference-grid repair campaign on the stronger LAN workstation through the
  canonical SSH-backed remote campaign workflow.
- [2026-04-15-14-41-23_remote_campaign_launcher_stderr_tolerance_and_smoke_test.md](./2026-04-15-14-41-23_remote_campaign_launcher_stderr_tolerance_and_smoke_test.md)
  Technical document for hardening the canonical remote campaign launcher so
  benign remote `stderr` warnings do not abort local orchestration before the
  real remote exit code is known.
- [2026-04-15-16-37-03_remote_campaign_source_sync_verification.md](./2026-04-15-16-37-03_remote_campaign_source_sync_verification.md)
  Technical document for hardening the remote launcher with an explicit
  post-sync remote file-existence verification pass before the actual remote
  training command starts.
- [2026-04-15-17-32-30_remote_campaign_path_resolution_and_verification_alignment.md](./2026-04-15-17-32-30_remote_campaign_path_resolution_and_verification_alignment.md)
  Technical document for correcting the remote launcher's malformed
  post-sync verification script and aligning its remote path checks with the
  exact repository-relative source-config paths consumed by the training
  entrypoint.
- [2026-04-15-17-41-02_remote_source_sync_transport_hardening.md](./2026-04-15-17-41-02_remote_source_sync_transport_hardening.md)
  Technical document for replacing the current archive-based remote source
  sync-up transport after evidence showed that the uploaded campaign YAMLs are
  materialized as broken remote entries instead of normal files.
- [2026-04-15-18-00-22_remote_campaign_short_path_execution_for_windows_max_path.md](./2026-04-15-18-00-22_remote_campaign_short_path_execution_for_windows_max_path.md)
  Technical document for resolving the LAN-node Windows path-length failure by
  executing the remote campaign through a short temporary repository alias
  instead of the long native clone path.
- [2026-04-15-18-07-05_remote_campaign_marker_emission_and_capture_alignment.md](./2026-04-15-18-07-05_remote_campaign_marker_emission_and_capture_alignment.md)
  Technical document for fixing the final remote-run failure where the launcher
  no longer dies on source-config paths but still does not receive the expected
  `REMOTE_CAMPAIGN_*` marker lines back from the remote wrapper.
- [2026-04-15-18-25-27_remote_powershell_transport_replacement.md](./2026-04-15-18-25-27_remote_powershell_transport_replacement.md)
  Technical document for replacing the current stdin-fed remote PowerShell
  transport after evidence showed that even minimal marker scripts return no
  captured `stdout` through the existing `powershell -Command -` path.
- [2026-04-15-22-36-46_remote_aware_project_path_resolution.md](./2026-04-15-22-36-46_remote_aware_project_path_resolution.md)
  Technical document for fixing the remaining LAN-node blocker inside Python by
  preventing the canonical project-path resolver from expanding the short
  execution alias back into the long physical repository path.
- [2026-04-15-23-07-40_remote_sync_manifest_exact_paper_family_recovery.md](./2026-04-15-23-07-40_remote_sync_manifest_exact_paper_family_recovery.md)
  Technical document for fixing the latest remote blocker in
  `build_remote_training_sync_manifest.py`, where exact-paper validation output
  paths do not fit the helper's current `training_runs/<family>` assumption.
- [2026-04-15-23-32-44_remote_exact_paper_launcher_parity_restoration.md](./2026-04-15-23-32-44_remote_exact_paper_launcher_parity_restoration.md)
  Technical document for restoring strict behavioral parity between the local
  exact-paper launcher and the LAN remote wrapper so remote execution keeps the
  same per-run logging, failure semantics, and repository-relative artifact
  contract.
