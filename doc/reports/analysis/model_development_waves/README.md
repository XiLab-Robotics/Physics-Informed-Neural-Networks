# Model Development Waves

This folder contains narrative reports and analysis bundles for repository
model-development waves.

## Directory Map

- `wave_1/` contains baseline Wave `1` reports and early TE curve prediction
  comparisons.
- `wave_2/` contains temporal and harmonic-temporal sequence model reports.
- `wave_3/` contains hybrid structured model reports and Wave `5.1` historical
  naming material.
- `wave_4/` contains PINN, MMT, and physics-guided design reports.
  - `wave_5_2/` contains dataset-aware Wave `5.2` diagnostics, the sixteen-phase
    full-PINN program, and completed Phase 0-9 evidence. Phases 2 and 3 are
    valid negative training results. Phases 4 and 5 are completed feasibility
    and identifiability results that retain raw reversal and paired-direction
    evidence without promoting hysteresis, backlash, or lost-motion residuals.
    Phase 6 adds a causal derivative and dynamic observability rejection;
    Phase 7 retains contact mechanics as synthetic-oracle work; Phase 8 does
    the same for energy inequalities without an input-power measurement.
    Phase 9 retains geometry and MMT as synthetic or deferred work. Phase 10
    retains wear and degradation laws as synthetic-only because longitudinal
    lifecycle evidence is absent. Phase 11 preserves electromechanical coupling
    as synthetic or instrumentation-blocked work because synchronized
    electrical channels are absent. Phase 12 preserves five empirically
    trainable hybrid architectures but promotes none as a full PINN because no
    physical residual survived isolation. Phase 13 closes the tournament as no
    contest with zero eligible full-PINN candidates. Phase 14 closes
    integration because zero promoted components are available against the
    minimum of two. Phase 15 closes all sixteen phases and does not authorize
    physics-integrated Wave 6; empirical multi-task work remains a separate
    future branch.

The folder names use stable filesystem slugs. Human-facing report titles may
retain legacy wave labels when they describe completed historical work.
