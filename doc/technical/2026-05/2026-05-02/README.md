# 2026-05-02 Technical Documents

- [2026-05-02-12-31-12_rcim_original_reference_training_and_archive_plan.md](./2026-05-02-12-31-12_rcim_original_reference_training_and_archive_plan.md)
  Plan the operator-run retraining of the recovered original RCIM workflow
  into `models/paper_reference/rcim_original/`, including the `forward` `v18`
  replay, the `backward` `v17` retuning step, and the current manual handoff
  gap before a valid `backward` tuned replay.
- [2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md](./2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md)
  Plan the recovered RCIM workflow cache simplification that replaces the
  hashed per-source pickle cache root with one shared
  `data/original_pipeline_instances/` directory, adds an explicit
  cache-rebuild flag, and defers dataset-shrinking-aware cache partitioning to
  the backlog.
