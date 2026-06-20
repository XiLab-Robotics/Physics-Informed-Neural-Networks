# Track 2 Component Offset Identification Plan

## Overview

This technical document records the next analysis gate for the observed
vertical offset in `Track 2` TE-curve predictions. The current evidence shows
that raw curve error can be strongly affected by a mean / `DC` offset, but it
does not yet prove that harmonic `a_0` / `Component 0` is the only source of
the issue.

The working hypothesis is therefore conservative:

- `a_0` / `Component 0` is a priority suspect because it is the dominant
  low-frequency or mean-like component and can strongly influence the full TE
  curve offset;
- the problem must still be identified component-by-component before future
  documentation or training plans treat `a_0` as the confirmed cause;
- experimental repeatability, preload, elastic release, protocol state, and
  hysteresis-like internal-state effects must be considered alongside model
  error.

This work is separate from the ongoing `Track 2G` campaign closure. It should
remain an analysis-only branch until the user explicitly approves further
implementation or documentation updates.

## Technical Approach

The analysis will compare curve-level offset diagnostics against explicit
harmonic/component diagnostics without assuming that they are identical.

The first pass should:

1. Reuse completed `Track 2D`, `Track 2E`, `Track 2F`, `Track 2F-bis`, and
   `Track 2G` artifacts as context, but avoid modifying their accepted results.
2. Extract experimental `a_0` / `Component 0` values where the dataset or
   paper-reference payload exposes them.
3. Plot experimental `a_0` over speed and torque, split by oil temperature and
   direction.
4. Compare `a_0` trends with curve mean / `DC` offset trends from the existing
   Track 2 diagnostics.
5. Check whether high-offset cases are explained mainly by `a_0`, by several
   harmonics/components, or by condition/regime effects.
6. Inspect available repeated operating points, if present, to estimate
   repeatability before treating the measured mean curve as a deterministic
   target.
7. Keep deployability boundaries explicit: any correction candidate must use
   causal operating information or explicitly available history, not future TE
   samples from the target curve.

## Involved Components

- `doc/running/te_model_live_backlog.md`
  Candidate destination for the approved future-work note after this plan is
  accepted.
- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`
  Current full-matrix raw / centered / offset diagnostic baseline.
- `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/track2e_offset_predictability_feasibility.md`
  Current causal offset-grouping feasibility baseline.
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report.md`
  Current completed curve-aware training closeout that must remain separate
  from this diagnostic branch.
- `data/simplified_dataset`
  Canonical dataset root for extracting operating conditions and available
  harmonic/component targets.
- `config/datasets/transmission_error_dataset.yaml`
  Canonical dataset configuration expected by Track 2 tooling.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
  Existing Track 2 reconstruction and reporting support surface that may be
  reused after approval.

## Implementation Steps

1. Inspect the canonical dataset schema and Track 2 payload exports to identify
   where `a_0` / `Component 0`, curve mean, operating direction, speed, torque,
   and oil temperature are stored.
2. Create an analysis report plan under `doc/reports/analysis/track2/` for a
   component-offset identification diagnostic.
3. Generate experimental `a_0` / `Component 0` surface plots over speed and
   torque, split by temperature and direction.
4. Generate companion plots for curve mean / `DC` offset so that `a_0` can be
   compared against the actual curve-offset symptom.
5. Produce per-condition and per-component tables that identify whether the
   offset is dominated by `a_0`, shared across multiple components, or
   condition/regime-specific.
6. Add repeatability checks for repeated operating points if the dataset
   contains repeated experiments or if external repeated-measurement data are
   imported later.
7. Update `doc/running/te_model_live_backlog.md` only after the diagnostic has
   evidence, avoiding any statement that `a_0` is the confirmed cause unless
   the data support it.
8. Use the resulting report to decide whether the next approved branch should
   be dataset filtering, robust target aggregation, explicit offset
   calibration, or a multi-head shape/offset architecture.
