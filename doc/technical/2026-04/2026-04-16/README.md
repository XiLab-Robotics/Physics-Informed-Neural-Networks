# 2026-04-16 Technical Documents

- [2026-04-16-22-49-22_remote_exact_paper_ssh_runtime_smoke_stabilization.md](./2026-04-16-22-49-22_remote_exact_paper_ssh_runtime_smoke_stabilization.md)
  Technical document for stabilizing the remaining SSH/noninteractive remote
  runtime path through a smoke-first exact-paper validation workflow before the
  scheduled four-run `SVR` reference-grid campaign is relaunched.
- [2026-04-16-12-06-43_remote_exact_paper_log_writer_single_owner_and_fail_fast.md](./2026-04-16-12-06-43_remote_exact_paper_log_writer_single_owner_and_fail_fast.md)
  Technical document for fixing the remote exact-paper wrapper so each per-run
  log has a single writer, logging failures fail fast, and the operator never
  sees a long silent session after the real remote child process has already
  died.
- [2026-04-16-00-22-17_remote_exact_paper_config_resolution_and_conda_stderr_fix.md](./2026-04-16-00-22-17_remote_exact_paper_config_resolution_and_conda_stderr_fix.md)
  Technical document for the residual remote exact-paper blockers: relative
  config-path resolution on the LAN node and noisy `conda` `stderr` handling in
  the remote wrapper.
- [2026-04-16-01-17-27_remote_exact_paper_runtime_observability_interruptibility_and_utilization.md](./2026-04-16-01-17-27_remote_exact_paper_runtime_observability_interruptibility_and_utilization.md)
  Technical document for the remaining operator-facing LAN issues: silent
  long-running phases, unreliable `Ctrl+C` stop behavior, and low or unclear
  remote workstation utilization during exact-paper execution.
