# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

`TE Curve Verification Pipeline` is the official offline verification surface for newly introduced TE
models. A model or family is not considered verified only because its training
campaign metrics improved; it must also be compared on the direction-aware
`TE Curve Verification Pipeline` curve-reconstruction matrix and reviewed against visual curve
evidence.

Current closeout verdict after the `Wave 2.1` temporal refresh:

- `TE Curve Verification Pipeline` remains the canonical offline model-verification report.
- The `Wave 2.1` temporal candidates are verified in the matrix and visual
  companion reports.
- No temporal candidate is promoted over the current repository-owned `tree` /
  `hist_gradient_boosting` offline baseline.
- The strongest temporal forward candidate is `gru_sequence_Fw`.
- The strongest temporal backward candidate is `lstm_sequence_Bw`.
- The strongest temporal global candidate is `lstm_sequence_global`.
- Future work should treat the temporal models as verified exploratory
  baselines, not as the accepted offline winner.

## Source Package

This official report consolidates these approved `TE Curve Verification Pipeline` artifacts:

- metric matrix:
  `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- best-model collage report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-24]/track2_best_model_collage_report.md`;
- best-model collage PDF:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-24]/track2_best_model_collage_report.pdf`;
- multi-model curve comparison report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-24]/track2_multi_model_curve_comparison_report.md`;
- multi-model curve comparison PDF:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-24]/track2_multi_model_curve_comparison_report.pdf`.

Machine-readable and visual validation outputs are retained under:

- `output/validation_checks/track2_reference_comparison/2026-05-24-22-01-57__track2_full_directional_family_matrix_wave2_temporal_refresh/`;
- `output/validation_checks/track2_best_model_collage_report/2026-05-24-22-50-30__track2_best_model_collage_report/`;
- `output/validation_checks/track2_multi_model_curve_comparison_report/2026-05-24-23-28-22__track2_multi_model_curve_comparison_report/`.

## Verification Rule

The repository treats direction as a first-class verification surface:

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` / `forward` | forward only | forward curves only |
| `Bw` / `backward` | backward only | backward curves only |

The rule applies to paper-reference models, `RCIM Model-Bank Reproduction` faithful archives,
retuned reference archives, `Wave 1` exported models, `Wave 2.1` temporal
registry models, and future `TE Curve Verification Pipeline` campaign candidates.

## Pipeline Coverage

| Pipeline or Source | TE Curve Verification Pipeline Role | Current Status | Verification Artifact |
| --- | --- | --- | --- |
| recovered original RCIM archive | paper-original forward reference | included | directional matrix |
| retuned RCIM archive | current paper-derived forward and backward baseline | included | directional matrix and visual reports |
| `RCIM Model-Bank Reproduction` exact paper-faithful bank | source-faithful reproduction evidence | included | directional matrix and visual reports |
| `Wave 1` exported static baselines | repository-owned static candidates | included | directional matrix and visual reports |
| `periodic_mlp` explicit harmonic campaign | latest family-registry refresh | included in visual refresh | collage and overlay reports |
| `Wave 2.1` temporal entry campaign | temporal convolution, `GRU`, and `LSTM` registry candidates | included | matrix, collage, overlay, PDF |
| future `TE Curve Verification Pipeline` campaigns | new verification candidates | append here when approved | matrix, collage, overlay, PDF |

## Current Numeric Baselines

### Best Composite References

| Candidate | Source | Direction | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `paper_original_best_Fw` | `rcim_original` | forward | 0.002769 | 0.002951 | 6.250 | 13.827 |
| `paper_retuned_best_Fw` | `rcim_retuned` | forward | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `track1_best_Fw` | `rcim_track1` | forward | 0.003014 | 0.003204 | 6.819 | 11.638 |
| `paper_retuned_best_Bw` | `rcim_retuned` | backward | 0.003675 | 0.004284 | 7.572 | 15.645 |
| `track1_best_Bw` | `rcim_track1` | backward | 0.005027 | 0.005212 | 11.860 | 48.106 |

### Repository-Owned Static Baselines

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| forward | `tree_Fw` | 0.003053 | 0.003395 | 6.731 | 11.995 |
| backward | `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| global, forward side | `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| global, backward side | `tree_global` | 0.003290 | 0.003702 | 7.118 | 13.703 |

### Wave 2.1 Temporal Candidates

| Direction | Strongest Temporal Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| forward | `gru_sequence_Fw` | 0.003330 | 0.003762 | 7.378 | 13.029 |
| backward | `lstm_sequence_Bw` | 0.003555 | 0.003985 | 7.767 | 14.507 |
| global, combined | `lstm_sequence_global` | 0.003480 | 0.003903 | 7.654 | 12.430 |

The temporal family is competitive with the non-tree neural/static baselines,
but it does not beat the accepted `tree` baseline in either direction.

## Visual Verification Evidence

### Best-Model Collage Evidence

The refreshed best-model collage report now includes:

- forward and backward composite reference collages;
- `Wave 1` family-best collages;
- explicit-harmonic `periodic_mlp` refresh collages;
- `Wave 2.1` temporal collages for `temporal_convolution`, `gru_sequence`, and
  `lstm_sequence` across `global`, `Fw`, and `Bw`.

The PDF companion is:

`doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-24]/track2_best_model_collage_report.pdf`

Representative evidence from the refreshed validation output is stored at:

- `output/validation_checks/track2_best_model_collage_report/2026-05-24-22-50-30__track2_best_model_collage_report/collages/forward_wave2/gru_sequence_fw.png`;
- `output/validation_checks/track2_best_model_collage_report/2026-05-24-22-50-30__track2_best_model_collage_report/collages/backward_wave2/lstm_sequence_bw.png`.

### Multi-Model Overlay Evidence

The refreshed multi-model curve comparison report now includes dedicated
`Wave 2.1` overlays and combined reference/tree/temporal overlays for both
directions. The combined overlays show the temporal models against the current
paper-derived references, `RCIM Model-Bank Reproduction` references, and `tree` baseline on the same
curves.

The PDF companion is:

`doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-24]/track2_multi_model_curve_comparison_report.pdf`

Representative evidence from the refreshed validation output is stored at:

- `output/validation_checks/track2_multi_model_curve_comparison_report/2026-05-24-23-28-22__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_wave2.png`;
- `output/validation_checks/track2_multi_model_curve_comparison_report/2026-05-24-23-28-22__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_wave2.png`.

## Campaign Update Ledger

Future `TE Curve Verification Pipeline` campaigns must append a row here after the campaign result
report, matrix refresh, visual report refresh, and official PDF validation are
complete.

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-05-21 | `periodic_mlp` explicit harmonic registry refresh | `global`, `Fw`, `Bw` visual verification | source matrix unchanged; visual registry refresh included | collage and overlay PDFs refreshed | included as visual evidence, not promoted over `tree` |
| 2026-05-24 | `Wave 2.1` temporal-model entry campaign | `global`, `Fw`, `Bw` for TCN, `GRU`, and `LSTM` | matrix refreshed from 75 to 84 candidates | collage and overlay PDFs refreshed | verified, but not promoted over `tree` |

## Maintenance Contract

For every future `TE Curve Verification Pipeline` model-verification update:

1. refresh `Track 2 Directional Model Comparison.md` when the candidate set or
   numeric matrix changes;
2. regenerate the best-model collage report when a new family or promoted
   candidate needs local curve inspection;
3. regenerate the multi-model curve comparison report when relative visual
   screening changes;
4. append the campaign or update to this report ledger;
5. export and validate this official report PDF;
6. update `doc/running/te_model_live_backlog.md`;
7. update `Training Results Master Summary.md` when the accepted current best
   status or campaign interpretation changes.

## Closeout Decision

`TE Curve Verification Pipeline` remains closed as the current official offline verification report.
The accepted baseline for future work is unchanged:

- forward paper-derived comparison: `paper_retuned_best_Fw`;
- backward paper-derived comparison: `paper_retuned_best_Bw`;
- strongest individual paper-reference family evidence:
  `rcim_retuned_GBM19_Fw` and `rcim_retuned_GBM19_Bw`;
- strongest repository-owned static baseline: `tree` /
  `hist_gradient_boosting`.

The `Wave 2.1` temporal branch is accepted as verified exploratory evidence, not
as the promoted offline winner. The practical next branch should either tune a
compact temporal/hybrid model against the `tree` baseline or move the strongest
verified candidates into deployment-readiness checks before any TwinCAT-facing
promotion decision.
