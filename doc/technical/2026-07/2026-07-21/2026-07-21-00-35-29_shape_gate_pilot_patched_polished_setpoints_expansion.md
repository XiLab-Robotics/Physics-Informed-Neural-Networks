# Shape-Gate Pilot Patched Polished Setpoints Expansion

## Overview

This technical document scopes a small post-fix `TE Curve Verification
Pipeline` expansion for the completed `shape_gate_loss_pilot` checkpoint. The
previous playback-contract audit found that the initial forward-only Track 2
failure was caused by polished input-mode drift in lightweight curve-record
construction. After propagating `dataset.input_mode`, the pilot became a
forward-only `recommended_candidate`.

The next step is a narrow patched expansion on `polished_dataset` setpoints,
covering the available `Fw` pilot and the relevant polished setpoint selected
backward comparator before any full three-dataset, three-surface Aries
campaign is prepared.

## Technical Approach

The expansion will remain diagnostic and non-training:

- preserve the fixed Track 2 lightweight input-mode contract;
- evaluate `polished_dataset` setpoint `forward` and `backward` surfaces in a
  compact selected-candidate matrix;
- keep the shape-gated reranker as the primary screen;
- regenerate only bounded verification plots needed for visual sanity checks;
- record whether the corrected `Fw` pilot remains viable when seen next to the
  current polished setpoint backward/reference comparator surface.

This is not an official full `TE Curve Verification Pipeline` refresh and does
not change accepted `global`, `Fw`, or `Bw` leaders by itself.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- `output/registries/families/shape_gate_loss_pilot_periodic_gru_sequence_fw/`
- `output/validation_checks/track2_reference_comparison/`
- `output/validation_checks/shape_gated_te_curve_reranker/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/`
- `doc/reports/campaign_results/track_2/verification_plots/`
- `doc/running/te_model_live_backlog.md`

No subagent is planned for this pass. If a subagent becomes useful, the
delegated scope and approval requirement must be recorded before launch.

## Implementation Steps

1. Create a compact patched polished-setpoint Fw/Bw evaluation config using
   existing registry-backed candidates and selected active comparators.
2. Run the compact matrix on the remote workstation if local polished CSV
   loading remains memory-limited.
3. Run the shape-gated reranker for `forward` and `backward` surfaces using the
   same patched input-mode contract.
4. Generate bounded Track 2 plots for the evaluated surfaces.
5. Recover artifacts to the local repository and update the documentation
   index and live backlog with the corrected result.
6. Run scoped Python and Markdown QA before reporting completion.
