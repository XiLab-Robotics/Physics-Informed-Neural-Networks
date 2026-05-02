# 2026-05-02 Technical Documents

- [2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md](./2026-05-02-11-23-22_rcim_shared_pickle_cache_stabilization.md)
  Plan the recovered RCIM workflow cache simplification that replaces the
  hashed per-source pickle cache root with one shared
  `data/original_pipeline_instances/` directory, adds an explicit
  cache-rebuild flag, and defers dataset-shrinking-aware cache partitioning to
  the backlog.
