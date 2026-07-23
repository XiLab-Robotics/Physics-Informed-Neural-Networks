# Causal Offset Bounded TE Curve Verification Screen Plan

## Overview

This plan prepares a bounded `TE Curve Verification Pipeline` screen for the
completed causal offset / mean calibration pilot. The screen is required
because the pilot's scalar winner is useful but not promotion-ready:
`causal_offset_mean_periodic_mlp_harmonic_fw` improves the non-windowed
harmonic comparator but does not beat the accepted forward GRU scalar baseline
or the prior shape-objective scalar high-water mark.

## Scope

The screen is intentionally narrow:

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- surface: `Fw`;
- evaluation scope: forward held-out curves only;
- execution mode: operator-launchable local or remote;
- promotion from scalar metrics: disallowed.

## Candidate Matrix

| Candidate | Source | Purpose |
| --- | --- | --- |
| `polished_setpoints_periodic_gru_sequence_Fw` | Polished setpoint archive | Current accepted model-development forward baseline |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | Polished setpoint archive | Required non-windowed harmonic comparator |
| `causal_offset_mean_periodic_mlp_harmonic_fw` | Completed pilot output | New non-windowed scalar pilot winner |
| `causal_offset_mean_gru_sequence_fw` | Completed pilot output | Time-windowed residual-offset control |
| `shape_objective_periodic_mlp_harmonic_Fw` | Prior completed screen candidate | Optional scalar high-water reference if available without widening the screen |

## Execution Plan

1. Create the compact matrix YAML and dedicated launcher.
2. Run launcher preflight locally.
3. If local preflight passes, provide the operator with the local and `-Remote`
   launch commands.
4. Wait for the operator to run the bounded screen and report completion.
5. Inspect the generated matrix report, shape-gated reranker output, and
   measured-versus-predicted TE curve plots.
6. Decide whether the scalar winner is promoted, rejected, or kept as a
   controlled exploratory candidate.

## Expected Outputs

- `output/validation_checks/track2_reference_comparison/`
- `output/validation_checks/shape_gated_te_curve_reranker/`
- `output/validation_checks/track2_operator_launch_logs/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-22]/`
- `doc/reports/campaign_results/track_2/verification_plots/causal_offset_bounded_track2_screen_polished_setpoints_fw/`

## Acceptance Criteria

- The launcher preflight confirms all candidate outputs, model archives,
  runner scripts, and active-campaign state are present.
- The matrix evaluates the required causal offset candidates and the two
  required polished-setpoint forward baselines.
- The screen keeps time-windowed and non-windowed candidates visible in the
  same result surface.
- The reranker reports raw error, centered shape behavior, offset behavior,
  harmonic / phase indicators, derivative behavior, and per-curve shape pass
  evidence where available.
- No model is promoted from scalar MAE alone.
