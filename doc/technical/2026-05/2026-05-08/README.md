# 2026-05-08 Technical Notes

- [2026-05-08-16-58-27_track1_exact_paper_write_progress_completed_activity_fix.md](./2026-05-08-16-58-27_track1_exact_paper_write_progress_completed_activity_fix.md)
  Plan the narrow exact-paper wrapper fix that adds the missing `-Activity`
  argument to sub-progress `Write-Progress -Completed` calls so remote
  launchers stop prompting interactively.
- [2026-05-08-15-40-54_track1_exact_paper_families_alias_and_csv_support.md](./2026-05-08-15-40-54_track1_exact_paper_families_alias_and_csv_support.md)
  Plan the narrow follow-up that keeps the new exact-paper `-Family` launcher
  surface but also adds a recovered-original-style `-Families` alias that
  accepts either one value or a CSV family list.
- [2026-05-08-15-16-17_track1_exact_paper_family_stage_launcher_and_live_progress_rework.md](./2026-05-08-15-16-17_track1_exact_paper_family_stage_launcher_and_live_progress_rework.md)
  Plan the exact-paper launcher rework that records the interrupted
  paper-faithful campaign, adds a family-and-stage operator surface analogous
  to the recovered-original launcher, and greatly improves live progress
  visibility during search and historical cross-validation.
- [2026-05-08-11-49-11_rcim_original_launcher_foreground_console_and_transcript_fix.md](./2026-05-08-11-49-11_rcim_original_launcher_foreground_console_and_transcript_fix.md)
  Plan the next recovered-original RCIM launcher repair that removes the
  still-interfering relay layer, restores native foreground-console
  `GridSearchCV` verbosity, and re-establishes a clean `Ctrl+C` contract while
  keeping persistent stage logs.
- [2026-05-08-00-57-25_rcim_original_launcher_process_relay_and_console_attachment_fix.md](./2026-05-08-00-57-25_rcim_original_launcher_process_relay_and_console_attachment_fix.md)
  Plan the second recovered-original RCIM launcher fix that keeps the
  PowerShell wrapper attached to the real training process and preserves the
  same live console output contract as the direct Python command.
- [2026-05-08-00-39-20_rcim_original_launcher_live_output_and_ctrl_c_fix.md](./2026-05-08-00-39-20_rcim_original_launcher_live_output_and_ctrl_c_fix.md)
  Plan the shared recovered-original RCIM launcher fix that restores full
  high-verbosity live retune output and clean `Ctrl+C` interruption behavior
  from the PowerShell wrapper.
