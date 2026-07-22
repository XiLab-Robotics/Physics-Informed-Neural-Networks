# Shape-First Distillation Bounded TE Curve Verification Screen Plan

## Overview

This plan prepares a bounded `TE Curve Verification Pipeline` screen for the
completed shape-first training-rule distillation pilot. The screen is required
because scalar campaign metrics selected the non-windowed harmonic MLP, while
the repository promotion rule requires curve-first evidence before any
accepted forward recommendation changes.

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
| `polished_setpoints_periodic_gru_sequence_Fw` | Polished setpoint archive | Current time-windowed forward recommendation |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | Polished setpoint archive | Current non-windowed harmonic baseline |
| `shape_first_distilled_periodic_gru_sequence_fw` | Completed pilot registry | New time-windowed training-rule candidate |
| `shape_first_distilled_periodic_mlp_harmonic_fw` | Completed pilot registry | New non-windowed training-rule candidate and scalar pilot winner |

## Execution Plan

1. Run launcher preflight locally.
2. If local preflight passes, run remote preflight if the operator wants to
   verify the LAN workstation surface.
3. Launch the full bounded screen with `-Remote` for the normal run.
4. After completion, inspect the matrix report, shape-gated reranker output,
   and generated measured-versus-predicted TE curve plots.
5. Decide whether the scalar winner is promoted, rejected, or kept as a
   controlled exploratory candidate.

## Expected Outputs

- `output/validation_checks/track2_reference_comparison/`
- `output/validation_checks/shape_gated_te_curve_reranker/`
- `output/validation_checks/track2_operator_launch_logs/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-22]/`
- `doc/reports/campaign_results/track_2/verification_plots/shape_first_distillation_bounded_track2_screen_polished_setpoints_fw/`

## Acceptance Criteria

- The launcher preflight confirms all candidate registries, model archives,
  runner scripts, and active-campaign state are present.
- The matrix evaluates exactly the four approved candidates unless the user
  explicitly approves a wider screen.
- The reranker reports raw error, centered shape behavior, offset behavior,
  harmonic/phase indicators, derivative behavior, and per-curve shape pass
  evidence where available.
- No model is promoted from scalar MAE alone.
