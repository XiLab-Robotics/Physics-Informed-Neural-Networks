# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

`TE Curve Verification Pipeline` is the official offline verification surface for newly introduced TE
models. A model or family is not considered verified only because its training
campaign metrics improved; it must also be compared on the direction-aware
`TE Curve Verification Pipeline` curve-reconstruction matrix and reviewed against visual curve
evidence.

Current closeout verdict:

- `TE Curve Verification Pipeline` is accepted as the canonical offline model-verification report.
- `Target A` is closed as an offline direction-qualified benchmark.
- The strongest current offline paper-derived references are
  `paper_retuned_best_Fw` and `paper_retuned_best_Bw`.
- The strongest current individual reference-family candidates are
  `rcim_retuned_GBM19_Fw` and `rcim_retuned_GBM19_Bw`.
- The strongest current repository-owned static baseline remains the
  `tree` / `hist_gradient_boosting` family.
- Future `TE Curve Verification Pipeline` campaigns must update this report, the source matrix, and
  the visual companion reports before their results are treated as accepted.

## Source Package

This official report consolidates these approved `TE Curve Verification Pipeline` artifacts:

- metric matrix:
  `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- best-model collage report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.md`;
- best-model collage PDF:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.pdf`;
- multi-model curve comparison report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.md`;
- multi-model curve comparison PDF:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.pdf`.

Machine-readable and visual validation outputs are retained under:

- `output/validation_checks/track2_reference_comparison/`;
- `output/validation_checks/track2_best_model_collage_report/`;
- `output/validation_checks/track2_multi_model_curve_comparison_report/`.

## Verification Rule

The repository treats direction as a first-class verification surface:

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` / `forward` | forward only | forward curves only |
| `Bw` / `backward` | backward only | backward curves only |

The rule applies to paper-reference models, `RCIM Model-Bank Reproduction` faithful archives,
retuned reference archives, `Wave 1` exported models, and future `TE Curve Verification Pipeline`
campaign candidates.

## Pipeline Coverage

| Pipeline or Source | TE Curve Verification Pipeline Role | Current Status | Verification Artifact |
| --- | --- | --- | --- |
| recovered original RCIM archive | paper-original forward reference | included | directional matrix |
| retuned RCIM archive | current paper-derived forward and backward baseline | included | directional matrix and visual reports |
| `RCIM Model-Bank Reproduction` exact paper-faithful bank | source-faithful reproduction evidence | included | directional matrix and visual reports |
| `Wave 1` exported static baselines | repository-owned model candidates | included | directional matrix and visual reports |
| `periodic_mlp` explicit harmonic campaign | latest family-registry refresh | included in visual refresh | collage and overlay reports |
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

### Strongest Individual Reference Candidates

| Direction | Candidate | Source | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| forward | `rcim_retuned_GBM19_Fw` | `rcim_retuned` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| backward | `rcim_retuned_GBM19_Bw` | `rcim_retuned` | 0.002766 | 0.003300 | 5.398 | 12.280 |

### Repository-Owned Static Baselines

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| forward | `tree_Fw` | 0.003053 | 0.003395 | 6.731 | 11.995 |
| backward | `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| global, forward side | `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| global, backward side | `tree_global` | 0.003290 | 0.003702 | 7.118 | 13.703 |

The `tree` family is the current strongest repository-owned offline static
baseline, but deployment suitability remains a separate decision because large
tree artifacts can be PLC/TwinCAT-unfriendly.

## Visual Verification Evidence

### Best-Model Collage Evidence

The best-model collage report checks local tracking behavior candidate by
candidate. Each collage contains four deterministic held-out test curves. The
current refreshed bundle includes forward and backward reference collages,
`Wave 1` family-best collages for `feedforward`, `harmonic_regression`,
`periodic_mlp`, `residual_harmonic_mlp`, and `tree`, plus refreshed
explicit-harmonic `periodic_mlp` campaign collages for `global`, `Fw`, and
`Bw`.

The PDF companion is the official visual appendix for candidate-level curve
inspection:

`doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-05-20]/track2_best_model_collage_report.pdf`

Representative evidence from the refreshed validation output:

![Forward Wave 1 Tree Collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/tree_fw.png)

![Backward Wave 1 Tree Collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/tree_bw.png)

### Multi-Model Overlay Evidence

The multi-model curve comparison report overlays several models on the same
measured curve. This is the official visual appendix for relative curve
tracking and family screening. The current refreshed bundle includes forward
and backward reference overlays, forward and backward `Wave 1` family overlays,
and screened `RCIM Model-Bank Reproduction` versus `Wave 1` overlays for both directions.

The PDF companion is:

`doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-05-20]/track2_multi_model_curve_comparison_report.pdf`

Representative evidence from the refreshed validation output:

![Forward Wave 1 Overlay](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-05-21-14-07-16__track2_multi_model_curve_comparison_report/comparisons/forward_wave1.png)

![Backward Wave 1 Overlay](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-05-21-14-07-16__track2_multi_model_curve_comparison_report/comparisons/backward_wave1.png)

## Campaign Update Ledger

Future `TE Curve Verification Pipeline` campaigns must append a row here after the campaign result
report, matrix refresh, visual report refresh, and official PDF validation are
complete.

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-05-21 | `periodic_mlp` explicit harmonic registry refresh | `global`, `Fw`, `Bw` visual verification | source matrix unchanged; visual registry refresh included | collage and overlay PDFs refreshed | included as visual evidence, not promoted over `tree` |

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

`TE Curve Verification Pipeline` is closed as the current official offline verification report. Its
accepted baseline for future work is:

- forward paper-derived comparison: `paper_retuned_best_Fw`;
- backward paper-derived comparison: `paper_retuned_best_Bw`;
- strongest individual paper-reference family evidence:
  `rcim_retuned_GBM19_Fw` and `rcim_retuned_GBM19_Bw`;
- strongest repository-owned static baseline: `tree` /
  `hist_gradient_boosting`.

The next modeling branch can proceed to `Wave 2.1` temporal models. Online
compensation remains outside `TE Curve Verification Pipeline` and is tracked under `Track 3` /
`Target B`.
