# 2026-05-13 Technical Notes

- [2026-05-13-14-14-43_rcim_original_live_log_backpressure_fix.md](./2026-05-13-14-14-43_rcim_original_live_log_backpressure_fix.md)
  Plan the recovered-original RCIM launcher fix for the new live-log
  backpressure issue, where complete persisted logs now work but verbose retune
  stages can stall the integrated terminal when the mirrored stream becomes too
  heavy.
- [2026-05-13-16-10-09_rcim_retuned_archive_closeout_and_benchmark_reset.md](./2026-05-13-16-10-09_rcim_retuned_archive_closeout_and_benchmark_reset.md)
  Plan the recovered-original RCIM retuned-model closeout, archive promotion
  into `models/paper_reference/rcim_retuned`, detailed PDF report generation,
  and reset of the canonical paper-reference benchmark tables.
- [2026-05-13-16-50-46_rcim_retuned_closeout_pdf_table_layout_refinement.md](./2026-05-13-16-50-46_rcim_retuned_closeout_pdf_table_layout_refinement.md)
  Plan the narrow styled-PDF table layout refinement for the recovered-original
  RCIM retuned closeout report.
- [2026-05-13-17-33-38_track1_paper_faithful_elm_queue_completion.md](./2026-05-13-17-33-38_track1_paper_faithful_elm_queue_completion.md)
  Plan the protected Track 1 paper-faithful queue update that adds forward and
  backward `ELM` YAML entries so the existing `11`-family launcher command can
  run.
- [2026-05-13-18-22-31_track1_remote_source_sync_temp_directory_fix.md](./2026-05-13-18-22-31_track1_remote_source_sync_temp_directory_fix.md)
  Plan the protected remote launcher fix that creates the remote `.temp`
  directory before uploading the source-sync archive with `scp`.
