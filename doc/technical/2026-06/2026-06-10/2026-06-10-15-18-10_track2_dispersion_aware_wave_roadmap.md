# Track 2 Dispersion-Aware Wave Roadmap

## Overview

This technical note records the approved documentation update for the next
`Track 2` modeling plan after the completed component-offset diagnostics. The
current evidence keeps `h0` / `a_0` as the strongest offset-channel suspect,
but it does not prove that harmonic zero is the only source of the observed TE
curve-offset failures.

The planning update therefore inserts dispersion-aware model probes, `Wave 3`
hybrid structured models, and `Wave 4` first-PINN work before the integrated
multi-task / multi-head architecture. The purpose is to test the available
robust, probabilistic, mixture, latent-state, hybrid, and physics-informed
tools separately before combining them into a larger architecture.

## Technical Approach

The documentation update will:

- record the evidence boundary from the measured `h0` diagnostic, the
  `Track 2D` h0/error cross-check, and the predicted-mean h0 surface
  diagnostic;
- add a `Track 2H` dispersion-aware modeling probe stage covering robust
  regression losses, quantile or probabilistic regression, mixture-density
  heads, and latent-state or hysteresis-aware features;
- move `Wave 3` hybrid structured models and `Wave 4` first-PINN formulation
  ahead of the integrated multi-task / multi-head model stage;
- keep PLC-friendly export constraints out of the immediate Python research
  phase while preserving causal inputs and no target leakage;
- update canonical planning documents so future campaign plans start from the
  same staged roadmap.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/track2/component_offset_identification_plan/[2026-06-09]/track2_component_offset_identification_plan.md`
- `doc/reports/analysis/track2/dispersion_aware_wave_roadmap/[2026-06-10]/track2_dispersion_aware_wave_roadmap.md`
- `doc/README.md`

## Implementation Steps

1. Create the `Track 2` dispersion-aware wave roadmap report.
2. Register the roadmap report and this technical note from `doc/README.md`.
3. Update the `Track 2` component-offset plan with the completed diagnostic
   outcomes and the new decision gate.
4. Update the TE live backlog so the next modeling order is `Track 2H`,
   `Wave 3`, `Wave 4`, then integrated multi-task / multi-head modeling.
5. Update the training master summary snapshot with the revised roadmap
   status.
6. Run Markdown QA on all touched Markdown files.
