# TwinCAT ONNX Family Compatibility Matrix

## Overview

This document defines the implementation plan for a family-wide TwinCAT ONNX
compatibility audit and remediation pass. The immediate problem is that the
new TwinCAT conversion pipeline can convert some ONNX exports, such as the
RCIM MLP representative, but fails on other exported model families. The first
known failing family is the PyTorch feedforward export, which passes ONNX
checker and ONNX Runtime smoke execution but fails during Beckhoff TF38x0
`onnximport`.

The goal is to test one representative ONNX export from each implemented model
family, identify the exact incompatibility class, and extend the conversion
pipeline with deterministic family-specific preprocessing or export guidance
where needed. The final pipeline should either produce TwinCAT-compatible XML
and BML artifacts for each supported family or produce a clear unsupported
classification with the required model/export change.

No Codex subagent is planned for this work.

## Technical Approach

The work will proceed as an audit-and-fix loop driven by the current local
model family inventory. The initial family list will be rechecked against the
dataset input mode retraining campaign document and then matched against actual
ONNX artifacts in `models/` and `output/`.

The representative families to cover are:

- `rcim_track1`
- `tree`
- `residual_harmonic_mlp`
- `feedforward`
- `periodic_mlp`
- `harmonic_regression`
- `periodic_mlp_harmonic`
- `temporal_convolution`
- `gru_sequence`
- `lstm_sequence`
- `periodic_temporal_convolution`
- `periodic_gru_sequence`
- `periodic_lstm_sequence`
- `residual_harmonic_gru_sequence_sparse_rcim`
- `residual_harmonic_gru_sequence_dense240`
- `residual_harmonic_gru_sequence_dense360`
- `residual_harmonic_lstm_sequence_sparse_rcim`
- `residual_harmonic_lstm_sequence_dense240`
- `residual_harmonic_lstm_sequence_dense360`
- `wave3_1_sequential_residual_offset_probe`
- `wave3_2_clean_sequential_residual_offset`
- `wave3_2_harmonic_residual_offset`
- `wave3_3_curve_aware_pointwise_control`
- `wave3_3_raw_centered_shape_curve_aware`
- `wave3_3_raw_offset_curve_aware`
- `wave3_3_full_curve_composite`
- `wave4_1_mae_robust_loss`
- `wave4_1_smooth_l1_robust_loss`
- `wave4_1_log_cosh_robust_loss`
- `wave4_2_quantile_p10_p50_p90`
- `wave4_2_gaussian_nll`
- `wave4_3_mixture_density_k2`
- `wave4_3_mixture_density_k3`
- `wave4_4_gru_latent_offset_residual`
- `wave4_4_causal_tcn_latent_offset_residual`
- `wave5_1_harmonic_prior_pointwise_control`
- `wave5_1_harmonic_prior_smooth_l1_structured`

Each family will be tested through the existing converter. The test output will
record:

- selected representative ONNX path;
- ONNX metadata, opset, shapes, and operator histogram;
- ONNX checker status;
- optional ONNX Runtime smoke status;
- TF38x0 `onnximport`, `store`, and `info` status;
- optional TF3820 `onnxprep` status when useful;
- generated XML and BML paths when conversion succeeds;
- failure signature and proposed remediation when conversion fails.

Each family result will be classified as one of:

- `compatible_as_is`;
- `compatible_after_pipeline_postprocess`;
- `requires_exporter_change`;
- `requires_model_variant_change`;
- `tf3820_only_candidate`;
- `not_supported_for_twincat_runtime`;
- `missing_representative_export`.

The first remediation target is `feedforward`. Its current failure is different
from the earlier INT64 slice-bound issue described in the handoff document:
the failing representative uses `LayerNormalization`, `Erf`, scalar `Constant`
nodes, and opset 17. ONNX checker and ONNX Runtime accept the file, while the
Beckhoff importer fails when reading a `Constant` node. The remediation pass
will inspect whether the family can be made compatible through ONNX
post-processing, opset/export changes, or a dedicated TwinCAT-friendly
deployment variant that avoids importer-hostile operators.

Before implementing PyTorch, ONNX, ONNX Runtime, or scikit-learn specific code,
current API details will be checked through Context7 as required by the project
instructions.

## Involved Components

The primary implementation and evidence surfaces are:

- `scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py`;
- possible new family matrix runner under
  `scripts/deployment/twincat_onnx_conversion/`;
- possible converter-side ONNX preprocessing helpers under
  `scripts/deployment/twincat_onnx_conversion/`;
- `requirements-twincat-onnx-conversion.txt` if new conversion dependencies are
  introduced;
- `doc/scripts/deployment/twincat_onnx_conversion/README.md`;
- `doc/guide/project_usage_guide.md` if user-facing commands change;
- `doc/reports/analysis/twincat_onnx_conversion/` for the compatibility matrix
  summary if a canonical report is needed;
- `output/deployment/twincat_onnx_conversion/` for generated audit artifacts;
- `.temp/Beckhoff_ONNX_MLlib_Chat_Handoff.md` as prior failure context;
- `.temp/ModelManagerAPI/` and `.temp/TcMLExtension/` as recovered vendor-source
  references only;
- `reference/codes/TestRig` and the existing TestRig TwinCAT reference notes for
  PLC-side compatibility expectations.

If a fix requires modifying active campaign-protected files, the work will stop
with a `CRITICAL WARNING` and wait for explicit approval before editing those
files.

## Implementation Steps

1. Rebuild the implemented-family inventory from the campaign document and
   available ONNX archives.
2. Select one representative ONNX file per family, preferring already exported
   deployed or validation artifacts over ad hoc regenerated files.
3. Run the current TwinCAT converter on the feedforward representative first
   and capture the exact failure artifacts.
4. Inspect the feedforward model/export path and test the smallest viable
   compatibility fix.
5. Add deterministic converter support for safe ONNX post-processing only when
   it preserves model semantics and can be verified by ONNX Runtime before and
   after processing.
6. Use exporter-side or model-variant changes only when post-processing is not
   semantically safe.
7. Run the same audit loop across all listed families and update the matrix
   after each result.
8. Document every family-specific case, including unsupported operators,
   required simplifications, and whether TF3820 should be preferred.
9. Run focused Python validation for changed scripts.
10. Run the touched Markdown QA checks.
11. If user-facing command documentation changes, rebuild the Sphinx portal with
    warning-as-error enabled.
12. Report the compatibility matrix, generated artifacts, and any families that
    still require a modeling decision before TwinCAT deployment.
