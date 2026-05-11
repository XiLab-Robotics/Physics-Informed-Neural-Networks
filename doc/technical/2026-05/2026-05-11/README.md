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
- [2026-05-11-15-39-02_rcim_original_lgbm_retune_log_flood_and_failure_capture_fix.md](./2026-05-11-15-39-02_rcim_original_lgbm_retune_log_flood_and_failure_capture_fix.md)
  Plan the narrow recovered-original RCIM `LGBM` retune fix that suppresses
  unusable LightGBM log flooding while preserving repository-owned progress
  lines and persistent failure capture.
- [2026-05-11-16-26-01_track1_exact_paper_elm_export_hardening_and_quiet_lgbm.md](./2026-05-11-16-26-01_track1_exact_paper_elm_export_hardening_and_quiet_lgbm.md)
  Plan the Track 1 exact-paper alignment that ports the recovered-original
  export hardening for ELM-like estimators into the shared exporter and adopts
  the quieter repository-owned `LGBMRegressor` factory for the active Track 1
  `LGBM` family.
- [2026-05-11-16-28-59_track1_exact_paper_add_elm_and_quiet_lgbm.md](./2026-05-11-16-28-59_track1_exact_paper_add_elm_and_quiet_lgbm.md)
  Superseding plan for promoting `ELM` into the canonical Track 1 exact-paper
  family bank while also adopting the quieter repository-owned
  `LGBMRegressor` factory.
