# RCIM Original Sparse ONNX Track 2 Variants

## Overview

This technical document plans two non-training `Track 2` forward evaluations
that reuse only the recovered paper-original `ONNX` models from:

`reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`

The work will not train new models. It will create two explicit sparse
reconstruction candidates and pass both through the same held-out forward
`Track 2` curve evaluation contract used by the existing full original `ONNX`
report:

- `rcim_original_simplified_onnx_Fw`: sparse paper-inspired reconstruction
  using harmonics `0`, `1`, `39`, and `40` with selected original `ONNX`
  families per component.
- `rcim_original_plc_hgbm_onnx_Fw`: PLC-oriented sparse reconstruction using
  `HGBM` original `ONNX` models for all available targets in harmonics `0`,
  `1`, `39`, and `40`.

The request explicitly requires the original recovered `ONNX` models for both
probes. Therefore the implementation will not use `PKL` archives,
repository-retuned models, Track 1 reimplemented banks, or `models/paper_reference`
candidate archives as prediction sources.

## Technical Approach

The paper reference extraction confirms that Section `2.2` identifies the TE
function harmonic components and that the compensation discussion later focuses
on components `0`, `1`, `39`, and `40` as the most influential set for practical
compensation. The extracted PDF text also states that the PLC compensation path
uses ML predictions of harmonic amplitudes and phases combined through the
paper harmonic reconstruction equation.

There is one source-boundary detail to keep explicit: the extracted PDF text
around the compensation section states that `SVM` is chosen for component `0`.
The current user request specifies `ET` for component `0`. This implementation
will follow the user-requested `ET` selection and label the result as the
repository `rcim_original_simplified_onnx_Fw` probe, not as a verbatim Table 6
claim.

The sparse simplified candidate will load these original `ONNX` targets:

| Harmonic | Target | Family | Original ONNX Path |
| ---: | --- | --- | --- |
| 0 | amplitude | ET | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ET/ampl/ExtraTreeRegressor_ampl0.onnx` |
| 1 | amplitude | RF | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl1.onnx` |
| 1 | phase | LGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/LGBM/phase/LGBMRegressor_phase1.onnx` |
| 39 | amplitude | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx` |
| 39 | phase | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx` |
| 40 | amplitude | ERT | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl40.onnx` |
| 40 | phase | GBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/GBM/phase/GradientBoostingRegressor_phase40.onnx` |

The PLC-oriented `HGBM` candidate will load these original `ONNX` targets:

| Harmonic | Target | Family | Original ONNX Path |
| ---: | --- | --- | --- |
| 0 | amplitude | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl0.onnx` |
| 1 | amplitude | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl1.onnx` |
| 1 | phase | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase1.onnx` |
| 39 | amplitude | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx` |
| 39 | phase | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx` |
| 40 | amplitude | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl40.onnx` |
| 40 | phase | HGBM | `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase40.onnx` |

For both sparse candidates, harmonic `0` is treated as a DC amplitude term and
does not require a phase target. Harmonics `1`, `39`, and `40` require both
amplitude and phase. Curve reconstruction will call the same
`harmonic_wise_support.reconstruct_curve_from_coefficients` contract already
used by the full original `ONNX` evaluator, but with the selected harmonic list
restricted to `[0, 1, 39, 40]`.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`: source paper for harmonic-selection and
  PLC-compensation context.
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`:
  repository summary of the paper's PLC-oriented ML compensation approach.
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`:
  repository summary of recovered exact `ONNX` model availability and harmonic
  target structure.
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`:
  the only model source for both requested probes.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/plot_original_onnx_fw_track2_curves.py`:
  current hardcoded original `ONNX` loader and reconstruction helper.
- `scripts/reports/analysis/build_track2_original_onnx_fw_collage_report.py`:
  current simple original `ONNX` Track 2 report builder.
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py`:
  canonical harmonic curve reconstruction and curve metric helpers.
- `scripts/reports/pdf/run_report_pipeline.py` and
  `scripts/reports/pdf/generate_styled_report_pdf.py`: styled PDF export and
  validation entry points if a report bundle is generated.

## Implementation Steps

1. Refactor the original `ONNX` plotter support just enough to accept named
   target configurations and named selected-harmonic lists while preserving the
   current full `19`-target behavior.
2. Add two hardcoded sparse target configurations:
   `rcim_original_simplified_onnx_Fw` and
   `rcim_original_plc_hgbm_onnx_Fw`.
3. Evaluate both sparse candidates on the canonical forward `Track 2`
   held-out curves using only original recovered `ONNX` sessions and the
   restricted harmonic list `[0, 1, 39, 40]`.
4. Save per-curve metrics, aggregate metrics, target inventory, and a
   deterministic four-curve collage for each sparse candidate.
5. Compare both sparse candidates against the existing full
   `paper_original_best_Fw_original_onnx_release` metrics and, where useful,
   against the `paper_original_best_Fw` / `paper_retuned_best_Fw` metrics from
   the `2026-05-28` best-model collage report.
6. Generate a concise Markdown report and styled PDF under a dated
   `doc/reports/analysis/track2/` topic folder if the evaluation is accepted as
   a repository report artifact.
7. Run Python compilation checks, the Track 2 evaluation command, PDF
   rasterization validation if a PDF is produced, scoped Markdown QA, and
   Sphinx `-W` if new public script/API documentation is added.

No subagent is planned for this implementation.
