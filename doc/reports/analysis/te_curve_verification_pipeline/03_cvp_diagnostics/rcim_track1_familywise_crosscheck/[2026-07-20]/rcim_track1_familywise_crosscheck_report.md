# RCIM Track 1 Familywise Cross-Check Report

## Overview

This diagnostic cross-check investigates the abnormal offsets and curve
misalignment observed in the latest familywise `TE Curve Verification Pipeline`
reports for `RCIM Model-Bank Reproduction` and related retrained model families.
It compares current familywise report artifacts against historical reference
reports and bounded live replay checks.

The checked scope covers:

- paper-original reference candidates;
- paper-retuned reference candidates;
- historical simplified `rcim_track1` candidates;
- newly retrained simplified and polished familywise ONNX candidates;
- the July 4, 2026 polished forward collage report cited as a visual baseline;
- the July 15, 2026 and July 19, 2026 familywise report outputs.

## Evidence Summary

### Reference And Historical Baselines

The historical forward reference report on the simplified dataset kept the
paper-original and paper-retuned candidates in the expected low-error range:

| Candidate | Curve Count | MAE [deg] | RMSE [deg] | Mean Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `paper_original_best_Fw` | 97 | 0.002769 | 0.002951 | 6.250 |
| `paper_retuned_best_Fw` | 97 | 0.001839 | 0.002041 | 4.109 |
| `paper_original_best_Fw_original_onnx_release` | 97 | 0.002804 | 0.002987 | 6.329 |

The same historical reference support explicitly applies source-specific
`h0` compatibility for `rcim_track1` and
`polished_rcim_model_bank_reproduction` forward candidates:

| Source Label | Surface | Historical `h0` Multiplier |
| --- | --- | ---: |
| `rcim_track1` | `Fw` | -1.0 |
| `polished_rcim_model_bank_reproduction` | `Fw` | -1.0 |
| other reference combinations | any | 1.0 |

The existing RCIM paper-reference benchmark also documents that this forward
`h0` compatibility sign is required before TE-curve reconstruction.

### July 4 Polished Forward Visual Baseline

The user-cited report
`doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/dataset_surface_report/polished_dataset/forward/collage/[2026-07-04]/track2_best_model_collage_report.md`
shows the polished Wave 4.3 Mixture Density candidates as strong:

| Candidate | Source | Surface | MAE [deg] | RMSE [deg] | Mean Error [%] |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_wave4_3_mixture_density_k2_fw` | `polished_model_development_registry` | Fw | 0.001545 | 0.001890 | 3.202 |
| `polished_wave4_3_mixture_density_k3_fw` | `polished_model_development_registry` | Fw | 0.001528 | 0.001867 | 3.161 |

The matching plot asset visually confirms tight curve tracking for
`polished_wave4_3_mixture_density_k3_fw`.

### Current Familywise ONNX Results

The current familywise ONNX report for Wave 4.3 uses newer retrained archive
paths. For polished setpoints forward, the same family now appears much worse:

| Family | Dataset / Input | Surface | Curve Count | MAE [deg] | Centered MAE [deg] | Offset [deg] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2` | `simplified_dataset/setpoints` | forward | 97 | 0.010679 | 0.005742 | 0.004585 |
| `wave4_3_mixture_density_k2` | `polished_dataset/setpoints` | forward | 100 | 0.017215 | 0.015895 | 0.004753 |
| `wave4_3_mixture_density_k2` | `polished_dataset/actual_values` | forward | 100 | 0.005174 | 0.004645 | 0.001978 |
| `wave4_3_mixture_density_k3` | `simplified_dataset/setpoints` | forward | 97 | 0.024845 | 0.021185 | 0.008848 |
| `wave4_3_mixture_density_k3` | `polished_dataset/setpoints` | forward | 100 | 0.020326 | 0.019724 | 0.004207 |
| `wave4_3_mixture_density_k3` | `polished_dataset/actual_values` | forward | 100 | 0.012587 | 0.012086 | -0.004018 |

For `wave4_3_mixture_density_k3` polished setpoints forward, the source
training run reports healthy held-out metrics:

| Run Instance | Validation MAE [deg] | Test MAE [deg] | Test RMSE [deg] |
| --- | ---: | ---: | ---: |
| `2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints` | 0.001846 | 0.002151 | 0.003566 |

This means the training run itself is not enough to explain the familywise
visual failure.

## Root-Cause Findings

### Finding 1: RCIM Forward `h0` Sign Is Missing In The New Familywise Builder

The current RCIM familywise report reconstructs harmonic curves with
`coefficient_cos_h0 = amplitude_value` for every surface. It does not apply the
historical forward-only `h0` compatibility multiplier.

The current July 19 familywise RCIM outputs therefore show the exact signature
of a DC-offset sign error: the centered shape is good, while the full MAE is
almost entirely offset-driven.

| Dataset / Input | Surface | Curve Count | Current MAE [deg] | Current Centered MAE [deg] | Current Offset [deg] |
| --- | --- | ---: | ---: | ---: | ---: |
| `simplified_dataset/setpoints` | forward | 97 | 0.113298 | 0.001044 | 0.113298 |
| `simplified_dataset/setpoints` | backward | 97 | 0.004107 | 0.001066 | 0.001922 |
| `polished_dataset/setpoints` | forward | 97 | 0.115062 | 0.000850 | 0.115062 |
| `polished_dataset/setpoints` | backward | 97 | 0.003582 | 0.000970 | 0.002612 |
| `polished_dataset/actual_values` | forward | 97 | 0.114912 | 0.000872 | 0.114912 |
| `polished_dataset/actual_values` | backward | 97 | 0.004765 | 0.000920 | 0.003020 |

Live replay of the simplified/setpoints RCIM bank confirms the fix direction:

| Surface | `h0` Multiplier | MAE [deg] | RMSE [deg] | Mean Error [%] | Offset [deg] | Centered MAE [deg] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| forward | 1.0 | 0.113298 | 0.113311 | 249.235 | 0.113298 | 0.001044 |
| forward | -1.0 | 0.003223 | 0.003465 | 7.099 | 0.000370 | 0.001044 |
| backward | 1.0 | 0.004107 | 0.004324 | 9.385 | 0.001922 | 0.001066 |
| backward | -1.0 | 0.048811 | 0.048888 | 107.509 | -0.046027 | 0.001066 |

Conclusion: the new RCIM familywise report is wrong for forward RCIM curves.
The required correction is to apply the same source-specific forward `h0`
multiplier used by the historical reference pipeline.

### Finding 2: Wave 4.3 MDN Familywise ONNX Uses The Wrong Playback Channel

The new familywise ONNX report evaluates MDN models through mixture expectation.
For the retrained `wave4_3_mixture_density_k3` polished setpoints forward ONNX,
the component selected by maximum mixture weight is the accurate deterministic
curve, while the mixture expectation creates a visibly oscillatory, incorrect
intermediate curve.

Live replay on all 100 polished/setpoints forward test curves gives:

| Playback Channel | Curve Count | Mean MAE [deg] | Median MAE [deg] | P95 MAE [deg] |
| --- | ---: | ---: | ---: | ---: |
| mixture expectation | 100 | 0.020326 | 0.019143 | 0.028637 |
| component 0 | 100 | 0.036635 | 0.037301 | 0.055656 |
| component 1 | 100 | 0.001734 | 0.001098 | 0.005276 |
| component 2 | 100 | 0.066641 | 0.061552 | 0.100053 |
| maximum-weight component | 100 | 0.001734 | 0.001098 | 0.005276 |

Conclusion: the Wave 4.3 retrained model is not inherently bad in this checked
case. The current familywise plotting/evaluation path uses a deterministic MDN
playback rule that is invalid for this exported model behavior. The corrected
report should either use maximum-weight component playback for these MDN ONNX
archives or explicitly compare both deterministic channels.

### Finding 3: Gaussian NLL Setpoints Outlier Is A Training Or Selection Issue

Unlike Wave 4.3 MDN, the polished/setpoints forward Gaussian NLL archive is
bad at the checkpoint level:

| Family | Dataset / Input | Surface | Current MAE [deg] | Centered MAE [deg] | Checkpoint Validation MAE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_gaussian_nll` | `polished_dataset/setpoints` | forward | 0.084405 | 0.081161 | 0.088198 |

Conclusion: this specific outlier should be treated as a real bad run or bad
promotion, not merely a plotting bug.

### Finding 4: Code And Generated Artifact Layout Had Drifted

The previous `build_track2_familywise_onnx_report.py` resolved inventories at:

`models/<dataset_id>/<input_mode>/exported/model_development_export_inventory.yaml`

The generated July 15 summaries point to the canonical post-migration path:

`models/<dataset_id>/<input_mode>/model_development_export_inventory.yaml`

Conclusion: the source code and generated report artifacts were not fully
layout-synchronized. The resolver now uses the canonical inventory path and
only accepts a legacy `exported/` inventory when no canonical inventory exists.

## Cross-Check Matrix

| Area | Status | Evidence | Required Action |
| --- | --- | --- | --- |
| FFT target decomposition | no failure proven | Backward RCIM and centered forward RCIM shapes are good. | Keep as lower priority; re-check after `h0` fix. |
| RCIM selected harmonics | consistent | RCIM bank selects 19 components over harmonics `0,1,3,39,40,78,81,156,162,240`. | Add explicit tables matching RCIM paper Tables 2-5. |
| RCIM forward recomposition | failing | Missing forward `h0` sign produces `249.235%`; sign fix gives `7.099%`. | Patch familywise RCIM builder. |
| RCIM backward recomposition | good | Backward current MAE is `0.004107`; flipping `h0` breaks it. | Do not apply backward sign flip. |
| Wave 4.3 MDN training | mostly healthy | Checked run has test MAE `0.002151`. | Do not discard run based on current familywise plot. |
| Wave 4.3 MDN familywise playback | failing | Maximum-weight component gives `0.001734`; mixture expectation gives `0.020326`. | Patch or parameterize MDN playback channel. |
| Gaussian NLL setpoints | bad run or selection | Checkpoint validation MAE is `0.088198`. | Exclude from best selection unless a better setpoints run exists. |
| Report inventory path | fixed in loader | Current summaries reference non-`exported` inventory path. | Resolver now accepts the canonical layout and rejects ambiguous duplicates. |

## Next Implementation Steps

1. Patch `build_track2_familywise_rcim_track1_report.py` so forward RCIM banks
   use the same `h0` compatibility multiplier as the historical reference
   pipeline.
2. Patch `build_track2_familywise_onnx_report.py` to support MDN deterministic
   playback channel selection, including at least `mixture_expectation` and
   `maximum_weight_component`.
3. Repair the familywise inventory resolver so it reads the canonical current
   archive layout and fails loudly if both old and new layouts exist.
4. Regenerate the affected familywise reports and compare before/after metrics:
   `rcim_track1`, `wave4_3_mixture_density_k2`, and
   `wave4_3_mixture_density_k3`.
5. Build the polished RCIM Model-Bank Reproduction candidate tables in the style
   of the original RCIM paper Tables 2-5, including all 19 selected components
   and highlighted best candidates.

## Interim Verdict

The strange new graphs are not one single failure:

- RCIM forward is a confirmed report/recomposition bug caused by missing
  forward `h0` sign compatibility.
- Wave 4.3 MDN familywise plots are a confirmed ONNX playback-channel problem:
  maximum-weight component playback recovers good performance.
- Gaussian NLL polished/setpoints forward is a real bad checkpoint or bad
  promotion candidate.
- The familywise report builder also has path-layout drift relative to the
  reports already generated.

These findings should be fixed before using the new familywise PDFs for any
model-selection decision.
