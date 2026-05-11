# 2026-05-11 Technical Notes

- [2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md](./2026-05-11-09-43-31_exact_paper_python_plus_onnx_export_alignment.md)
  Plan the exact-paper export alignment that restores recovered-original-style
  per-target Python plus ONNX export artifacts instead of ONNX-only per-target
  exports.
- [2026-05-11-09-59-51_track1_exact_paper_linear_svr_fallback_alignment.md](./2026-05-11-09-59-51_track1_exact_paper_linear_svr_fallback_alignment.md)
  Plan the Track 1 exact-paper alignment that replaces the historical
  `SVR(kernel="linear")` branch with the same pragmatic
  `StandardScaler + LinearSVR` fallback already adopted in the
  recovered-original workflow.
- [2026-05-11-10-05-21_rcim_original_elm_onnx_export_feature_shape_fix.md](./2026-05-11-10-05-21_rcim_original_elm_onnx_export_feature_shape_fix.md)
  Plan the narrow recovered-original RCIM exporter fix that restores ONNX
  export for fitted `ELMRegressor` targets without changing the existing
  training or staging protocol.
