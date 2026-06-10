"""Styled Markdown-to-PDF report exporter for repository analysis artifacts."""

from __future__ import annotations

# Import Python Utilities
import argparse, html
import re, shutil, subprocess, sys, time
from pathlib import Path
from typing import Sequence

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support

REPORT_PIPELINE_TEMP_ROOT = PROJECT_PATH / ".temp" / "report_pipeline"
HTML_PREVIEW_TEMP_ROOT = REPORT_PIPELINE_TEMP_ROOT / "html_previews"
BROWSER_PROFILE_TEMP_ROOT = REPORT_PIPELINE_TEMP_ROOT / "browser_profiles"

# Browser And Report Constants
WINDOWS_BROWSER_EXECUTABLE_CANDIDATE_PATHS = (
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
    Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
)
LINUX_BROWSER_EXECUTABLE_CANDIDATE_PATHS = (
    Path("/usr/bin/google-chrome"),
    Path("/usr/bin/google-chrome-stable"),
    Path("/usr/bin/chromium"),
    Path("/usr/bin/chromium-browser"),
    Path("/snap/bin/chromium"),
    Path("/opt/google/chrome/chrome"),
)

# Report Constants
DEFAULT_REPORT_SUBTITLE = "Feedforward Transmission Error Baseline"
DEFAULT_REPORT_CATEGORY = "Analysis Report"
HERO_NOTE_TEXT = (
    "Styled PDF edition generated from the canonical Markdown analysis report "
    "for improved readability, section hierarchy, and table presentation."
)
REPORT_SPECIFIC_SUBTITLE_DICTIONARY = {
    "2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report": "Track 2 Campaign Closeout",
    "2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report": "Track 2 Campaign Closeout",
    "2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report": "Track 2 Campaign Closeout",
}

# Report Styles
ALIGN_LEFT = "align-left"
ALIGN_CENTER = "align-center"
ALIGN_RIGHT = "align-right"

# Report Tables
GENERIC_TABLE_CLASS_NAME = "report-table report-table-generic"
HISTORICAL_REFERENCE_TABLE_CLASS_NAME = "report-table report-table-historical-results"
PHASE_RESULTS_TABLE_CLASS_NAME = "report-table report-table-phase-results"
RANKING_RESULTS_TABLE_CLASS_NAME = "report-table report-table-ranking-results"
DECISION_MATRIX_TABLE_CLASS_NAME = "report-table report-table-decision-matrix"
COMPARATIVE_EXAMPLE_TABLE_CLASS_NAME = "report-table report-table-comparative-example"
WAVE1_RECOVERY_TEST_RANKING_TABLE_CLASS_NAME = "report-table report-table-wave1-recovery-test-ranking"
WAVE1_RECOVERY_VALIDATION_SNAPSHOT_TABLE_CLASS_NAME = "report-table report-table-wave1-recovery-validation-snapshot"
WAVE1_RECOVERY_RESIDUAL_TABLE_CLASS_NAME = "report-table report-table-wave1-recovery-residual-family"
WAVE1_RECOVERY_HARMONIC_TABLE_CLASS_NAME = "report-table report-table-wave1-recovery-harmonic-family"
WAVE1_RESIDUAL_FAMILY_TEST_RANKING_TABLE_CLASS_NAME = "report-table report-table-wave1-residual-family-test-ranking"
WAVE1_RESIDUAL_FAMILY_VALIDATION_SNAPSHOT_TABLE_CLASS_NAME = "report-table report-table-wave1-residual-family-validation-snapshot"
WAVE1_RESIDUAL_FAMILY_CAPACITY_TABLE_CLASS_NAME = "report-table report-table-wave1-residual-family-capacity"
WAVE1_RESIDUAL_FAMILY_DENSE_REGIME_TABLE_CLASS_NAME = "report-table report-table-wave1-residual-family-dense-regime"
WAVE1_RESIDUAL_FAMILY_TRAINING_MODE_TABLE_CLASS_NAME = "report-table report-table-wave1-residual-family-training-mode"
REMOTE_TRAINING_VALIDATION_COMPLETED_TABLE_CLASS_NAME = "report-table report-table-remote-training-validation-completed"
REMOTE_TRAINING_VALIDATION_FAILED_TABLE_CLASS_NAME = "report-table report-table-remote-training-validation-failed"
TARGETED_REMOTE_FOLLOWUP_COMPLETED_TABLE_CLASS_NAME = "report-table report-table-targeted-remote-followup-completed"
TARGETED_REMOTE_FOLLOWUP_FAMILY_BESTS_TABLE_CLASS_NAME = "report-table report-table-targeted-remote-followup-family-bests"
TRACK1_SECOND_ITERATION_COMPLETED_TABLE_CLASS_NAME = "report-table report-table-track1-second-iteration-completed"
WIDE_IDENTIFIER_RANKING_TABLE_CLASS_NAME = "report-table report-table-wide-identifier-ranking"
IDENTIFIER_METRIC_SUMMARY_TABLE_CLASS_NAME = "report-table report-table-identifier-metric-summary"
FAMILY_METRIC_RANKING_TABLE_CLASS_NAME = "report-table report-table-family-metric-ranking"
FAMILY_ESTIMATOR_METRIC_RANKING_TABLE_CLASS_NAME = "report-table report-table-family-estimator-metric-ranking"
EXACT_PAPER_COMPLETED_RANKING_TABLE_CLASS_NAME = WIDE_IDENTIFIER_RANKING_TABLE_CLASS_NAME
EXACT_PAPER_EXPORT_SUMMARY_TABLE_CLASS_NAME = IDENTIFIER_METRIC_SUMMARY_TABLE_CLASS_NAME
EXACT_PAPER_TOP_FAMILY_TABLE_CLASS_NAME = FAMILY_METRIC_RANKING_TABLE_CLASS_NAME
CAMPAIGN_SHARED_OFFLINE_RANKING_TABLE_CLASS_NAME = "report-table report-table-campaign-shared-offline-ranking"
CAMPAIGN_SHARED_OFFLINE_PLAYBACK_TABLE_CLASS_NAME = "report-table report-table-campaign-shared-offline-playback"
CAMPAIGN_EXACT_SUPPORT_RANKING_TABLE_CLASS_NAME = "report-table report-table-campaign-exact-support-ranking"
CAMPAIGN_EXACT_SUPPORT_EXPORT_TABLE_CLASS_NAME = "report-table report-table-campaign-exact-support-export"
TRACK1_OVERNIGHT_COMPLETED_TABLE_CLASS_NAME = "report-table report-table-track1-overnight-completed"
TRACK1_OVERNIGHT_DELTA_TABLE_CLASS_NAME = "report-table report-table-track1-overnight-delta"
TRACK1_OVERNIGHT_BLOCK_WINNER_TABLE_CLASS_NAME = "report-table report-table-track1-overnight-block-winner"
TRACK1_EXACT_OPEN_CELL_RANKING_TABLE_CLASS_NAME = "report-table report-table-track1-exact-open-cell-ranking"
TRACK1_EXACT_OPEN_CELL_EXPORT_TABLE_CLASS_NAME = "report-table report-table-track1-exact-open-cell-export"
TRACK1_FULL_MATRIX_RANKING_TABLE_CLASS_NAME = "report-table report-table-track1-full-matrix-ranking"
TRACK1_FULL_MATRIX_CELL_TOTALS_TABLE_CLASS_NAME = "report-table report-table-track1-full-matrix-cell-totals"
TRACK1_PARTIAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME = "report-table report-table-track1-partial-closeout-family"
TRACK1_PARTIAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME = "report-table report-table-track1-partial-closeout-aggregate"
TRACK1_FINAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME = "report-table report-table-track1-final-closeout-family"
TRACK1_FINAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME = "report-table report-table-track1-final-closeout-aggregate"
TRACK1_OPEN_CELL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME = "report-table report-table-track1-open-cell-closeout-family"
TRACK1_OPEN_CELL_CLOSEOUT_BENCHMARK_TABLE_CLASS_NAME = "report-table report-table-track1-open-cell-closeout-benchmark"
TRACK1_MLP_CLOSEOUT_TARGETED_PAIR_TABLE_CLASS_NAME = "report-table report-table-track1-mlp-closeout-targeted-pair"
TRACK1_INTERRUPTED_SVM_CANDIDATE_GAINS_TABLE_CLASS_NAME = "report-table report-table-track1-interrupted-svm-candidate-gains"
TRACK1_SVM_REPAIR_RANKING_TABLE_CLASS_NAME = "report-table report-table-track1-svm-repair-ranking"
TRACK1_SVM_REPAIR_BEFORE_AFTER_TABLE_CLASS_NAME = "report-table report-table-track1-svm-repair-before-after"
TRACK1_BIDIRECTIONAL_MEGA_BENCHMARK_SURFACE_TABLE_CLASS_NAME = "report-table report-table-track1-bidirectional-mega-benchmark-surface"
TRACK1_BIDIRECTIONAL_MEGA_REFERENCE_ARCHIVE_TABLE_CLASS_NAME = "report-table report-table-track1-bidirectional-mega-reference-archive"
TRACK1_FORWARD_CLOSEOUT_FAMILY_RESULTS_TABLE_CLASS_NAME = "report-table report-table-track1-forward-closeout-family-results"
TRACK1_FORWARD_CLOSEOUT_BENCHMARK_STATUS_TABLE_CLASS_NAME = "report-table report-table-track1-forward-closeout-benchmark-status"
TRACK1_FORWARD_CLOSEOUT_REFERENCE_ARCHIVE_TABLE_CLASS_NAME = "report-table report-table-track1-forward-closeout-reference-archive"
RCIM_RETUNED_ARCHIVE_COMPLETENESS_TABLE_CLASS_NAME = "report-table report-table-rcim-retuned-archive-completeness"
RCIM_RETUNED_MEAN_EVALUATION_METRICS_TABLE_CLASS_NAME = "report-table report-table-rcim-retuned-mean-evaluation-metrics"
RCIM_RETUNED_HARMONIC_METRIC_TABLE_CLASS_NAME = "report-table report-table-rcim-retuned-harmonic-metric"
TRACK1_FORWARD_OPEN_CELL_REPAIR_FAMILY_TABLE_CLASS_NAME = "report-table report-table-track1-forward-open-cell-repair-family"
TRACK1_FORWARD_OPEN_CELL_REPAIR_DELTA_TABLE_CLASS_NAME = "report-table report-table-track1-forward-open-cell-repair-delta"
TRACK1_FORWARD_DT_HISTORICAL_REPLAY_OUTCOME_TABLE_CLASS_NAME = "report-table report-table-track1-forward-dt-historical-replay-outcome"
FAMILY_BEST_RETRY_OUTCOME_TABLE_CLASS_NAME = TRACK1_FORWARD_OPEN_CELL_REPAIR_FAMILY_TABLE_CLASS_NAME
SURFACE_DELTA_SUMMARY_TABLE_CLASS_NAME = TRACK1_FORWARD_OPEN_CELL_REPAIR_DELTA_TABLE_CLASS_NAME
SVR_REFERENCE_GRID_RANKING_TABLE_CLASS_NAME = "report-table report-table-svr-reference-grid-ranking"
SVR_REFERENCE_GRID_EXPORT_SURFACE_TABLE_CLASS_NAME = "report-table report-table-svr-reference-grid-export-surface"
SVR_REFERENCE_GRID_GAP_VS_PAPER_TABLE_CLASS_NAME = "report-table report-table-svr-reference-grid-gap-vs-paper"
CAMPAIGN_CELL_REPAIR_RANKING_TABLE_CLASS_NAME = TRACK1_SVM_REPAIR_RANKING_TABLE_CLASS_NAME
SURFACE_BEFORE_AFTER_SUMMARY_TABLE_CLASS_NAME = TRACK1_SVM_REPAIR_BEFORE_AFTER_TABLE_CLASS_NAME
WAVE1_HIGH_ORDER_ARTIFACT_TABLE_CLASS_NAME = "report-table report-table-wave1-high-order-artifact"
WAVE1_HIGH_ORDER_KEY_VALUE_TABLE_CLASS_NAME = "report-table report-table-wave1-high-order-key-value"
WAVE1_HIGH_ORDER_LEADERBOARD_TABLE_CLASS_NAME = "report-table report-table-wave1-high-order-leaderboard"
WAVE1_HIGH_ORDER_REGISTRY_TABLE_CLASS_NAME = "report-table report-table-wave1-high-order-registry"
WAVE1_PERIODIC_MLP_LEADERBOARD_TABLE_CLASS_NAME = "report-table report-table-wave1-periodic-mlp-leaderboard"
WAVE1_PERIODIC_MLP_REGISTRY_TABLE_CLASS_NAME = "report-table report-table-wave1-periodic-mlp-registry"
WAVE2_TEMPORAL_ARTIFACT_TABLE_CLASS_NAME = "report-table report-table-wave2-temporal-artifact"
WAVE2_TEMPORAL_LEADERBOARD_TABLE_CLASS_NAME = "report-table report-table-wave2-temporal-leaderboard"
WAVE2_TEMPORAL_REGISTRY_TABLE_CLASS_NAME = "report-table report-table-wave2-temporal-registry"
TRACK2F_BRANCH_RESULTS_TABLE_CLASS_NAME = "report-table report-table-track2f-branch-results"
TRACK2F_SCALAR_LEADERBOARD_TABLE_CLASS_NAME = "report-table report-table-track2f-scalar-leaderboard"
TRACK2G_BRANCH_RESULTS_TABLE_CLASS_NAME = "report-table report-table-track2g-branch-results"
TRACK2G_LOSS_LEADERBOARD_TABLE_CLASS_NAME = "report-table report-table-track2g-loss-leaderboard"
TRACK2G_BASELINE_COMPARISON_TABLE_CLASS_NAME = "report-table report-table-track2g-baseline-comparison"
TRACK2G_REGISTRY_EFFECTS_TABLE_CLASS_NAME = "report-table report-table-track2g-registry-effects"
TRACK2_BEST_MODEL_COLLAGE_TABLE_CLASS_NAME = "report-table report-table-track2-best-model-collage"
TRACK2_OFFICIAL_VERIFICATION_RULE_TABLE_CLASS_NAME = "report-table report-table-track2-official-verification-rule"
TRACK2_OFFICIAL_PIPELINE_COVERAGE_TABLE_CLASS_NAME = "report-table report-table-track2-official-pipeline-coverage"
TRACK2_OFFICIAL_BEST_COMPOSITE_TABLE_CLASS_NAME = "report-table report-table-track2-official-best-composite"
TRACK2_OFFICIAL_STATIC_BASELINE_TABLE_CLASS_NAME = "report-table report-table-track2-official-static-baseline"
TRACK2_OFFICIAL_CAMPAIGN_LEDGER_TABLE_CLASS_NAME = "report-table report-table-track2-official-campaign-ledger"
TRACK2_OFFICIAL_CANDIDATE_REFRESH_TABLE_CLASS_NAME = "report-table report-table-track2-official-candidate-refresh"
TRACK2_OFFICIAL_TRACK2FBIS_RESULT_TABLE_CLASS_NAME = "report-table report-table-track2-official-track2fbis-result"
TRACK2_CURVE_FIRST_RANKING_TABLE_CLASS_NAME = "report-table report-table-track2-curve-first-ranking"
TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_TABLE_CLASS_NAME = "report-table report-table-track2-curve-payload-diagnostics"
TRACK2_SURFACE_LEADER_TABLE_CLASS_NAME = "report-table report-table-track2-surface-leader"
TRACK2_MEAN_CENTERED_TOP_TABLE_CLASS_NAME = "report-table report-table-track2-mean-centered-top"
TRACK2_MEAN_CENTERED_GROUP_TABLE_CLASS_NAME = "report-table report-table-track2-mean-centered-group"
TRACK2D_MEAN_OFFSET_TABLE_CLASS_NAME = "report-table report-table-track2d-mean-offset"
TRACK2E_OFFSET_FEASIBILITY_TABLE_CLASS_NAME = "report-table report-table-track2e-offset-feasibility"
TRACK2_COMPONENT_HARMONIC_SUMMARY_TABLE_CLASS_NAME = "report-table report-table-track2-component-harmonic-summary"
TRACK2_COMPONENT_TEMPERATURE_DIRECTION_TABLE_CLASS_NAME = "report-table report-table-track2-component-temperature-direction"
TRACK2_COMPONENT_H0_EXTREME_TABLE_CLASS_NAME = "report-table report-table-track2-component-h0-extreme"
TRACK2D_H0_SURFACE_SUMMARY_TABLE_CLASS_NAME = "report-table report-table-track2d-h0-surface-summary"
TRACK2D_H0_CANDIDATE_METRIC_TABLE_CLASS_NAME = "report-table report-table-track2d-h0-candidate-metric"
TRACK2D_H0_CANDIDATE_OVERLAP_TABLE_CLASS_NAME = "report-table report-table-track2d-h0-candidate-overlap"
TRACK2D_H0_QUADRANT_TABLE_CLASS_NAME = "report-table report-table-track2d-h0-quadrant"
TRACK2D_PREDICTED_MEAN_CANDIDATE_TABLE_CLASS_NAME = "report-table report-table-track2d-predicted-mean-candidate"
TRACK2D_PREDICTED_MEAN_DIRECTION_TABLE_CLASS_NAME = "report-table report-table-track2d-predicted-mean-direction"
TRACK2_ORIGINAL_ONNX_TARGET_TABLE_CLASS_NAME = "report-table report-table-track2-original-onnx-targets"
TRACK2_ORIGINAL_ONNX_METRICS_TABLE_CLASS_NAME = "report-table report-table-track2-original-onnx-metrics"
TRACK2_ORIGINAL_ONNX_CURVES_TABLE_CLASS_NAME = "report-table report-table-track2-original-onnx-curves"
TRACK2_FORWARD_REFERENCE_PAIRWISE_TABLE_CLASS_NAME = "report-table report-table-track2-forward-reference-pairwise"
TRACK2_FORWARD_REFERENCE_COLLAGE_METRICS_TABLE_CLASS_NAME = "report-table report-table-track2-forward-reference-collage-metrics"
TRACK2_FORWARD_REFERENCE_COLLAGE_DELTAS_TABLE_CLASS_NAME = "report-table report-table-track2-forward-reference-collage-deltas"
REPOSITORY_STATUS_SCALAR_WINNER_TABLE_CLASS_NAME = "report-table report-table-repository-status-scalar-winner"
REPOSITORY_STATUS_HPO_LEADER_TABLE_CLASS_NAME = "report-table report-table-repository-status-hpo-leader"
REPOSITORY_STATUS_HARMONIC_RESULTS_TABLE_CLASS_NAME = "report-table report-table-repository-status-harmonic-results"
REPOSITORY_STATUS_TEMPORAL_WINNER_TABLE_CLASS_NAME = "report-table report-table-repository-status-temporal-winner"
REPOSITORY_STATUS_TEMPORAL_SURFACES_TABLE_CLASS_NAME = "report-table report-table-repository-status-temporal-surfaces"
REPOSITORY_STATUS_WAVE2B_SCALAR_TABLE_CLASS_NAME = "report-table report-table-repository-status-wave2b-scalar"
REPOSITORY_STATUS_WAVE2B_TRACK2_TABLE_CLASS_NAME = "report-table report-table-repository-status-wave2b-track2"
REPOSITORY_STATUS_WAVE2C_SCALAR_TABLE_CLASS_NAME = "report-table report-table-repository-status-wave2c-scalar"
REPOSITORY_STATUS_WAVE2C_TRACK2_TABLE_CLASS_NAME = "report-table report-table-repository-status-wave2c-track2"
REPOSITORY_STATUS_WAVE2C_DENSE_TABLE_CLASS_NAME = "report-table report-table-repository-status-wave2c-dense"
REPOSITORY_STATUS_TRACK2_CURRENT_TABLE_CLASS_NAME = "report-table report-table-repository-status-track2-current"
REPOSITORY_STATUS_HARMONIC_BANK_TABLE_CLASS_NAME = "report-table report-table-repository-status-harmonic-bank"

# Table Header Cells
CONFIGURATION_TABLE_HEADER_CELLS = (
    "Config",
    "Status",
    "Main Intent",
    "Curve Batch",
    "Point Stride",
    "Max Points/Curve",
    "Workers",
    "Pin Memory",
    "Hidden Layers",
    "Epoch Budget",
    "Patience",
)

# Table Row Alignments
CAMPAIGN_SUMMARY_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)
DATA_PIPELINE_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)
MODEL_AND_SCHEDULE_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)

# Table Header Cells
HISTORICAL_REFERENCE_TABLE_HEADER_CELLS = (
    "Config",
    "Status",
    "Best Epoch",
    "Approx. Wall Time",
    "Val MAE [deg]",
    "Val RMSE [deg]",
    "Test MAE [deg]",
    "Test RMSE [deg]",
)

# Table Header Cells
PHASE_RESULTS_TABLE_HEADER_CELLS = (
    "Config",
    "Best Epoch",
    "Wall Time",
    "Val MAE [deg]",
    "Val RMSE [deg]",
    "Test MAE [deg]",
    "Test RMSE [deg]",
)

# Table Header Cells
RANKING_TABLE_HEADER_CELL_GROUPS = (
    ("Config", "Test MAE [deg]", "Test RMSE [deg]", "Runtime"),
    ("Config", "Test RMSE [deg]", "Test MAE [deg]", "Runtime"),
)
CAMPAIGN_CELL_REPAIR_RANKING_TABLE_HEADER_CELLS = (
    "Rank",
    "Run",
    "Scope",
    "Cells",
    "Met",
    "Near",
    "Open",
    "Closure Score",
    "Improved",
    "Upgrades",
)
SURFACE_BEFORE_AFTER_SUMMARY_TABLE_HEADER_CELLS = (
    "Surface",
    "Before",
    "After",
)
FAMILY_BEST_RETRY_OUTCOME_TABLE_HEADER_CELLS = (
    "Family",
    "Best Run",
    "Scope",
    "Harmonic",
    "Closure Score",
    "Met",
    "Near",
    "Open",
)
SURFACE_DELTA_SUMMARY_TABLE_HEADER_CELLS = (
    "Surface",
    "Before",
    "After",
    "Delta",
)
SVR_REFERENCE_GRID_RANKING_TABLE_HEADER_CELLS = (
    "Rank",
    "Run",
    "Scope",
    "Paper Cells",
    "Mean Gap Ratio",
    "Max Gap Ratio",
    "Failed Exports",
)
SVR_REFERENCE_GRID_EXPORT_SURFACE_TABLE_HEADER_CELLS = (
    "Completed Runs",
    "Exported ONNX Files",
    "Failed Exports",
    "Surrogate Exports",
)
SVR_REFERENCE_GRID_GAP_VS_PAPER_TABLE_HEADER_CELLS = (
    "Harmonic / Metric",
    "Paper Target",
    "Repository Result",
    "Gap",
    "Status",
)
TRACK1_FORWARD_CLOSEOUT_FAMILY_RESULTS_TABLE_HEADER_CELLS = (
    "Family",
    "Run Instance",
    "Mean MAE",
    "Mean RMSE",
    "Mean MAPE %",
    "Exported ONNX",
    "Exported PKL",
)
TRACK1_FORWARD_CLOSEOUT_BENCHMARK_STATUS_TABLE_HEADER_CELLS = (
    "Table",
    "Green",
    "Yellow",
    "Red",
    "Total",
)
TRACK1_FORWARD_CLOSEOUT_REFERENCE_ARCHIVE_TABLE_HEADER_CELLS = (
    "Family",
    "Archived Targets",
    "Source Runs",
    "Archive Root",
)

TRACK2_CURVE_FIRST_RANKING_TABLE_HEADER_CELLS = (
    "Rank",
    "Candidate",
    "Family",
    "Source",
    "Surface",
    "Direction",
    "Curves",
    "Mean MPE [%]",
    "P95 MPE [%]",
    "Worst MPE [%]",
    "Mean Curve MAE [deg]",
)

TRACK2_CURVE_FIRST_RANKING_PDF_COLUMN_INDEXES = (0, 1, 2, 4, 5, 6, 7, 8, 9)

TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_TABLE_HEADER_CELLS = (
    "Rank",
    "Candidate",
    "Family",
    "Surface",
    "Directions",
    "Curves",
    "Mean MPE [%]",
    "Mean Harmonic Amp Error [%]",
    "Mean Harmonic Phase Error [deg]",
    "Mean P2P Error [%]",
    "Derivative RMSE",
    "Closure Mismatch [deg]",
    "Diagnostic Score",
)

TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_PDF_COLUMN_INDEXES = (0, 1, 3, 4, 6, 7, 8, 9, 12)

TRACK2_SURFACE_LEADER_TABLE_HEADER_CELLS = (
    "Surface",
    "Leader",
    "Family",
    "Source",
    "Curves",
    "Mean MPE [%]",
    "P95 MPE [%]",
    "Mean Curve MAE [deg]",
)

TRACK2_MEAN_CENTERED_TOP_TABLE_HEADER_CELLS = (
    "Rank",
    "Candidate",
    "Surface",
    "Raw MAE",
    "Centered MAE",
    "Improvement",
    "Offset",
)

TRACK2_MEAN_CENTERED_GROUP_TABLE_HEADER_CELLS = (
    "Candidate",
    "Surface",
    "Raw MAE",
    "Centered MAE",
    "Improvement",
    "Offset",
)

TRACK2D_MEAN_OFFSET_TABLE_HEADER_CELLS = (
    "Rank",
    "Candidate",
    "Surface",
    "Raw MAE",
    "Centered MAE",
    "Offset",
    "Gain [%]",
    "Label",
)

TRACK2E_OFFSET_FEASIBILITY_TABLE_HEADER_CELLS = (
    "Rank",
    "Candidate",
    "Surface",
    "Interv.",
    "Raw MAE",
    "Corr. MAE",
    "Gain [%]",
    "Explain [%]",
    "Best Group",
)

TRACK2_COMPONENT_HARMONIC_SUMMARY_TABLE_HEADER_CELLS = (
    "Harmonic",
    "Mean Abs Amp [deg]",
    "P95 Abs Amp [deg]",
    "Max Abs Amp [deg]",
)

TRACK2_COMPONENT_TEMPERATURE_DIRECTION_TABLE_HEADER_CELLS = (
    "Direction",
    "Temp",
    "Curves",
    "Mean h0",
    "Std h0",
    "Min h0",
    "Max h0",
)

TRACK2_COMPONENT_H0_EXTREME_TABLE_HEADER_CELLS = (
    "Rank",
    "Direction",
    "Speed",
    "Torque",
    "Temp",
    "h0",
    "P2P",
    "File",
)

TRACK2D_H0_SURFACE_SUMMARY_TABLE_HEADER_CELLS = (
    "Surface",
    "Rows",
    "Mean Abs Offset",
    "Mean Abs h0",
    "Abs Corr",
    "Overlap Lift",
    "Max Delta",
)

TRACK2D_H0_LARGEST_OFFSET_TABLE_HEADER_CELLS = (
    "Candidate",
    "Rows",
    "Mean Abs Offset",
    "Mean Abs h0",
    "Abs Corr",
    "Overlap Lift",
)

TRACK2D_H0_OVERLAP_TABLE_HEADER_CELLS = (
    "Candidate",
    "Rows",
    "Abs Corr",
    "High Error",
    "High h0",
    "Overlap",
    "Lift",
)

TRACK2D_H0_ABSOLUTE_CORRELATION_TABLE_HEADER_CELLS = (
    "Candidate",
    "Rows",
    "Abs Corr",
    "Signed Corr",
    "Mean Abs Offset",
    "Mean Abs h0",
)

TRACK2D_H0_QUADRANT_TABLE_HEADER_CELLS = (
    "Candidate",
    "High Error + High h0",
    "High Error + Normal h0",
    "Normal Error + High h0",
)

TRACK2D_PREDICTED_MEAN_CANDIDATE_TABLE_HEADER_CELLS = (
    "Candidate",
    "Surface",
    "Bias",
    "Mean AE",
    "P90 AE",
    "Corr",
    "Slope",
    "Intercept",
)

TRACK2D_PREDICTED_MEAN_DIRECTION_TABLE_HEADER_CELLS = (
    "Candidate",
    "Direction",
    "Bias",
    "Mean AE",
    "Corr",
    "Slope",
)

TRACK2_ORIGINAL_ONNX_TARGET_TABLE_HEADER_CELLS = (
    "Target",
    "Harmonic",
    "Family",
    "Original ONNX Files",
)

TRACK2_ORIGINAL_ONNX_METRICS_TABLE_HEADER_CELLS = (
    "Candidate",
    "Curves",
    "MAE [deg]",
    "RMSE [deg]",
    "Mean Error [%]",
    "P95 Error [%]",
)

TRACK2_ORIGINAL_ONNX_CURVES_TABLE_HEADER_CELLS = (
    "Curve",
    "Speed [rpm]",
    "Torque [Nm]",
    "Oil [C]",
    "MAE [deg]",
    "Mean Error [%]",
)

TRACK2_FORWARD_REFERENCE_PAIRWISE_TABLE_HEADER_CELLS = (
    "Pair",
    "Mean MAE [deg]",
    "P95 [deg]",
    "Max [deg]",
    "RMSE [deg]",
    "Corr.",
)

TRACK2_FORWARD_REFERENCE_COLLAGE_METRICS_TABLE_HEADER_CELLS = (
    "Curve",
    "Operating Point",
    "Original",
    "Retuned",
    "Full ONNX",
    "Sparse",
    "PLC HGBM",
)

TRACK2_FORWARD_REFERENCE_COLLAGE_DELTAS_TABLE_HEADER_CELLS = (
    "Curve",
    "Operating Point",
    "Full ONNX",
    "Sparse",
    "PLC",
    "PLC-Full",
)

DECISION_MATRIX_TABLE_HEADER_CELLS = (
    "Platform",
    "Python API Docs",
    "Markdown Integration",
    "Automation",
    "Visual Quality",
    "Import Risk",
    "Repository Fit",
)

COMPARATIVE_EXAMPLE_TABLE_HEADER_CELLS = (
    "Platform",
    "Example Module Result",
    "Example Guide Result",
    "Integration Quality For This Repo",
)

# Report Section Identifiers
SEMANTIC_IDENTIFIER_TOKEN_PAIRS = {
    ("large", "batch"),
    ("big", "model"),
}

# Report Page Breaks
FORCED_PAGE_BREAK_SECTION_SLUGS = {
    "operating-principle",
    "advantages",
    "phase-2-results",
    "comparative-example-summary",
    "cross-campaign-ranking",
}

REPORT_SPECIFIC_FORCED_PAGE_BREAK_SECTION_SLUGS = {
    "track2d_mean_offset_full_matrix_audit": {
        "diagnostic-label-counts",
    },
    "track2e_offset_predictability_feasibility": {
        "intervention-counts",
    },
    "track2_curve_first_reranking_report": {
        "backward-curve-first-leaders",
        "overall-curve-first-leaders",
    },
    "track2_curve_payload_diagnostics_report": {
        "candidate-diagnostic-ranking",
    },
    "2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report": {
        "baseline-comparison",
        "execution-summary",
        "registry-effects",
    },
    "track2_forward_reference_curve_comparison_report": {
        "pairwise-predicted-curve-differences",
    },
    "2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report": {
        "recovery-campaign-ranking",
        "campaign-winner",
        "main-conclusions",
    },
    "2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report": {
        "program-level-context",
        "recommended-next-actions",
    },
    "2026-03-27-18-13-19_project_status_report": {
        "why-the-work-was-done-in-this-order",
        "high-level-future-roadmap",
    },
    "2026-04-03-22-35-07_remote_training_validation_campaign_results_report": {
        "campaign-winner",
        "recommended-next-actions",
    },
    "2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report": {
        "main-conclusions",
        "artifact-references",
    },
    "2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report": {
        "ranked-completed-runs",
    },
    "2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report": {
        "ranked-completed-runs",
    },
    "2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report": {
        "open-numeric-gaps-after-the-best-run",
    },
    "2026-04-14-14-35-29_track1_full_matrix_family_reproduction_campaign_results_report": {
        "main-conclusions",
    },
    "2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report": {
        "completed-family-closeout",
    },
    "2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report": {
        "family-recovery-outcome",
    },
    "2026-04-19-00-43-47_track1_remaining_family_cellwise_final_closeout_campaign_results_report": {
        "family-recovery-outcome",
    },
    "2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report": {
        "family-recovery-outcome",
    },
    "Harmonic-Wise Paper Reimplementation Pipeline": {
        "stage-6-reconstruct-the-te-curve",
    },
    "2026-04-21-22-19-09_track1_mlp_family_full_matrix_repair_campaign_results_report": {
        "targeted-pair-outcome",
    },
    "2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report": {
        "targeted-pair-outcome",
    },
    "track2_best_model_collage_report": {
        "collage-gallery-forward-reference-best-models",
        "collage-gallery-forward-reference-best-models-continued",
        "collage-gallery-forward-wave-1-family-best-models",
        "collage-gallery-forward-wave-1-family-best-models-continued",
        "collage-gallery-forward-wave-1-family-best-models-continued-2",
        "collage-gallery-backward-reference-best-models",
        "collage-gallery-backward-wave-1-family-best-models",
        "collage-gallery-backward-wave-1-family-best-models-continued",
        "collage-gallery-backward-wave-1-family-best-models-continued-2",
        "collage-gallery-global-wave-1-family-best-models",
        "collage-gallery-global-wave-1-family-best-models-continued",
        "collage-gallery-global-wave-1-family-best-models-continued-2",
        "output-artifacts",
    },
    "track2_multi_model_curve_comparison_report": {
        "comparison-gallery-forward-reference-model-overlay",
        "comparison-gallery-forward-wave-1-family-model-overlay",
        "comparison-gallery-backward-reference-model-overlay",
        "comparison-gallery-backward-wave-1-family-model-overlay",
        "comparison-gallery-forward-track-1-and-screened-wave-1-overlay",
        "comparison-gallery-backward-track-1-and-screened-wave-1-overlay",
        "output-artifacts",
    },
    "2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report": {
        "execution-summary",
        "leaderboard",
    },
    "2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report": {
        "execution-summary",
    },
    "2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report": {
        "execution-summary",
    },
}

# Browser And Report Constants
BROWSER_PDF_EXPORT_ARGUMENTS = (
    "--headless",
    "--disable-gpu",
    "--disable-breakpad",
    "--disable-crash-reporter",
    "--allow-file-access-from-files",
    "--no-pdf-header-footer",
)

CLEANUP_RETRY_COUNT = 6
CLEANUP_RETRY_DELAY_SECONDS = 0.5

# Report Styles
REPORT_STYLESHEET = """
    @page {
      size: A4;
      margin: 14mm 15mm 16mm 15mm;
    }

    * {
      box-sizing: border-box;
    }

    html {
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
      background: #ffffff;
    }

    body {
      margin: 0;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      color: #16193B;
      background: #ffffff;
      line-height: 1.48;
      font-size: 9.35pt;
    }

    .page-shell {
      width: 100%;
      max-width: 174mm;
      margin: 0 auto;
    }

    .hero {
      padding: 16px 18px 15px 18px;
      border-radius: 14px;
      border: 1px solid #7FB2F0;
      background: linear-gradient(180deg, #35478C 0%, #16193B 100%);
      color: #ffffff;
      margin-bottom: 14px;
    }

    .hero-badge {
      display: inline-block;
      padding: 4px 9px;
      border-radius: 999px;
      background: rgba(173, 213, 247, 0.16);
      border: 1px solid rgba(173, 213, 247, 0.36);
      font-size: 7.6pt;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }

    .hero h1 {
      margin: 0 0 5px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 19pt;
      line-height: 1.12;
      letter-spacing: -0.01em;
    }

    .hero-subtitle {
      margin: 0 0 8px 0;
      font-size: 9.2pt;
      color: rgba(255, 255, 255, 0.86);
    }

    .hero-note {
      margin: 0;
      max-width: 88%;
      font-size: 8.2pt;
      color: rgba(255, 255, 255, 0.76);
    }

    .section-card {
      break-inside: auto;
      margin: 0 0 10px 0;
      padding: 11px 12px 10px 12px;
      border-radius: 12px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
      max-width: 100%;
    }

    .section-keep-together {
      break-inside: avoid-page;
      page-break-inside: avoid;
    }

    .section-force-page-break {
      break-before: page;
      page-break-before: always;
    }

    .explicit-page-break {
      break-before: page;
      page-break-before: always;
      height: 0;
      margin: 0;
      padding: 0;
      border: none;
    }

    h2 {
      margin: 0 0 10px 0;
      padding-bottom: 6px;
      border-bottom: 1.5px solid #7FB2F0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 13.1pt;
      line-height: 1.2;
      color: #16193B;
      break-after: avoid-page;
    }

    h3 {
      margin: 0 0 6px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 10.3pt;
      color: #35478C;
      break-after: avoid-page;
    }

    p {
      margin: 5px 0;
      orphans: 3;
      widows: 3;
    }

    .block-label {
      margin: 8px 0 4px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 8pt;
      letter-spacing: 0;
      text-transform: none;
      color: #4E7AC7;
    }

    .report-figure {
      margin: 10px auto 12px auto;
      padding: 4px 0 8px 0;
      border-radius: 10px;
      border: none;
      background: #ffffff;
      text-align: center;
      break-inside: avoid-page;
      page-break-inside: avoid;
      width: 100%;
    }

    .report-figure img {
      display: block;
      width: 100%;
      max-width: 150mm;
      height: auto;
      margin: 0 auto;
      border-radius: 0;
      background: transparent;
    }

    .report-figure-caption {
      margin: 9px auto 0 auto;
      max-width: 150mm;
      font-size: 8pt;
      color: #35478C;
      line-height: 1.34;
      text-align: center;
    }

    .subsection-block {
      break-inside: avoid-page;
      margin: 10px 0 0 0;
      padding: 9px 10px 8px 10px;
      border-radius: 10px;
      border: 1px solid rgba(173, 213, 247, 0.9);
      background: #ffffff;
      max-width: 100%;
    }

    .report-list {
      margin: 4px 0 7px 0;
      padding-left: 18px;
    }

    .report-list li {
      margin: 3px 0;
      padding-left: 2px;
    }

    .report-list ul,
    .report-list ol {
      margin-top: 4px;
      padding-left: 16px;
    }

    .li-body {
      display: inline;
    }

    .list-continuation {
      margin-top: 4px;
      margin-bottom: 0;
      color: #35478C;
    }

    code {
      padding: 1px 5px 2px 5px;
      border-radius: 5px;
      background: #F4F8FE;
      color: #16193B;
      font-family: "Consolas", "Cascadia Mono", "Courier New", monospace;
      font-size: 8.2pt;
      word-break: break-word;
    }

    strong {
      color: #16193B;
    }

    .table-wrap {
      margin: 9px 0 10px 0;
      overflow: hidden;
      border-radius: 10px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
      max-width: 100%;
    }

    .report-table {
      width: 100%;
      table-layout: fixed;
      border-collapse: collapse;
      font-size: 7.2pt;
      line-height: 1.26;
    }

    .report-table thead {
      background: #35478C;
      color: #ffffff;
    }

    .report-table thead tr {
      height: 30px;
    }

    .report-table th,
    .report-table td {
      padding: 5px 5px;
      border-bottom: 1px solid #D8E8FA;
      vertical-align: middle;
      overflow-wrap: anywhere;
      word-break: break-word;
      hyphens: auto;
    }

    .report-table tbody tr:nth-child(even) {
      background: #F7FBFF;
    }

    .report-table th {
      text-align: center;
      vertical-align: middle;
      white-space: nowrap;
      border-right: 1px solid rgba(255, 255, 255, 0.46);
      font-weight: 700;
    }

    .report-table th:last-child {
      border-right: none;
    }

    .report-table-generic th:nth-child(1), .report-table-generic td:nth-child(1) { width: 8%; }
    .report-table-generic th:nth-child(2), .report-table-generic td:nth-child(2) { width: 9%; }
    .report-table-generic th:nth-child(3), .report-table-generic td:nth-child(3) { width: 18%; }
    .report-table-generic th:nth-child(4), .report-table-generic td:nth-child(4) { width: 7%; }
    .report-table-generic th:nth-child(5), .report-table-generic td:nth-child(5) { width: 7%; }
    .report-table-generic th:nth-child(6), .report-table-generic td:nth-child(6) { width: 10%; }
    .report-table-generic th:nth-child(7), .report-table-generic td:nth-child(7) { width: 6%; }
    .report-table-generic th:nth-child(8), .report-table-generic td:nth-child(8) { width: 8%; }
    .report-table-generic th:nth-child(9), .report-table-generic td:nth-child(9) { width: 15%; }
    .report-table-generic th:nth-child(10), .report-table-generic td:nth-child(10) { width: 7%; }
    .report-table-generic th:nth-child(11), .report-table-generic td:nth-child(11) { width: 5%; }

    .report-table-track2-component-harmonic-summary th,
    .report-table-track2-component-harmonic-summary td { width: 25%; }

    .report-table-track2-component-temperature-direction th,
    .report-table-track2-component-temperature-direction td { width: 14.2857%; }

    .report-table-track2-component-h0-extreme th:nth-child(1), .report-table-track2-component-h0-extreme td:nth-child(1) { width: 5%; }
    .report-table-track2-component-h0-extreme th:nth-child(2), .report-table-track2-component-h0-extreme td:nth-child(2) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(3), .report-table-track2-component-h0-extreme td:nth-child(3) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(4), .report-table-track2-component-h0-extreme td:nth-child(4) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(5), .report-table-track2-component-h0-extreme td:nth-child(5) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(6), .report-table-track2-component-h0-extreme td:nth-child(6) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(7), .report-table-track2-component-h0-extreme td:nth-child(7) { width: 10%; }
    .report-table-track2-component-h0-extreme th:nth-child(8), .report-table-track2-component-h0-extreme td:nth-child(8) { width: 35%; }

    .report-table-track2d-h0-surface-summary th,
    .report-table-track2d-h0-surface-summary td { width: 14.2857%; }

    .report-table-track2d-h0-candidate-metric,
    .report-table-track2d-h0-candidate-overlap,
    .report-table-track2d-h0-quadrant {
      font-size: 6.45pt;
      line-height: 1.12;
    }

    .report-table-track2d-h0-candidate-metric th,
    .report-table-track2d-h0-candidate-metric td,
    .report-table-track2d-h0-candidate-overlap th,
    .report-table-track2d-h0-candidate-overlap td,
    .report-table-track2d-h0-quadrant th,
    .report-table-track2d-h0-quadrant td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2d-h0-candidate-metric th:nth-child(1),
    .report-table-track2d-h0-candidate-metric td:nth-child(1) { width: 40%; }
    .report-table-track2d-h0-candidate-metric th:nth-child(2),
    .report-table-track2d-h0-candidate-metric td:nth-child(2),
    .report-table-track2d-h0-candidate-metric th:nth-child(3),
    .report-table-track2d-h0-candidate-metric td:nth-child(3),
    .report-table-track2d-h0-candidate-metric th:nth-child(4),
    .report-table-track2d-h0-candidate-metric td:nth-child(4),
    .report-table-track2d-h0-candidate-metric th:nth-child(5),
    .report-table-track2d-h0-candidate-metric td:nth-child(5),
    .report-table-track2d-h0-candidate-metric th:nth-child(6),
    .report-table-track2d-h0-candidate-metric td:nth-child(6) { width: 12%; }

    .report-table-track2d-h0-candidate-overlap th:nth-child(1),
    .report-table-track2d-h0-candidate-overlap td:nth-child(1) { width: 40%; }
    .report-table-track2d-h0-candidate-overlap th:nth-child(2),
    .report-table-track2d-h0-candidate-overlap td:nth-child(2),
    .report-table-track2d-h0-candidate-overlap th:nth-child(3),
    .report-table-track2d-h0-candidate-overlap td:nth-child(3),
    .report-table-track2d-h0-candidate-overlap th:nth-child(4),
    .report-table-track2d-h0-candidate-overlap td:nth-child(4),
    .report-table-track2d-h0-candidate-overlap th:nth-child(5),
    .report-table-track2d-h0-candidate-overlap td:nth-child(5),
    .report-table-track2d-h0-candidate-overlap th:nth-child(6),
    .report-table-track2d-h0-candidate-overlap td:nth-child(6),
    .report-table-track2d-h0-candidate-overlap th:nth-child(7),
    .report-table-track2d-h0-candidate-overlap td:nth-child(7) { width: 10%; }

    .report-table-track2d-h0-quadrant th:nth-child(1),
    .report-table-track2d-h0-quadrant td:nth-child(1) { width: 40%; }
    .report-table-track2d-h0-quadrant th:nth-child(2),
    .report-table-track2d-h0-quadrant td:nth-child(2),
    .report-table-track2d-h0-quadrant th:nth-child(3),
    .report-table-track2d-h0-quadrant td:nth-child(3),
    .report-table-track2d-h0-quadrant th:nth-child(4),
    .report-table-track2d-h0-quadrant td:nth-child(4) { width: 20%; }

    .report-table-track2d-predicted-mean-candidate,
    .report-table-track2d-predicted-mean-direction {
      font-size: 6.55pt;
      line-height: 1.12;
    }

    .report-table-track2d-predicted-mean-candidate th,
    .report-table-track2d-predicted-mean-candidate td,
    .report-table-track2d-predicted-mean-direction th,
    .report-table-track2d-predicted-mean-direction td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2d-predicted-mean-candidate th:nth-child(1),
    .report-table-track2d-predicted-mean-candidate td:nth-child(1) { width: 31%; }
    .report-table-track2d-predicted-mean-candidate th:nth-child(2),
    .report-table-track2d-predicted-mean-candidate td:nth-child(2) { width: 9%; }
    .report-table-track2d-predicted-mean-candidate th:nth-child(3),
    .report-table-track2d-predicted-mean-candidate td:nth-child(3),
    .report-table-track2d-predicted-mean-candidate th:nth-child(4),
    .report-table-track2d-predicted-mean-candidate td:nth-child(4),
    .report-table-track2d-predicted-mean-candidate th:nth-child(5),
    .report-table-track2d-predicted-mean-candidate td:nth-child(5),
    .report-table-track2d-predicted-mean-candidate th:nth-child(6),
    .report-table-track2d-predicted-mean-candidate td:nth-child(6),
    .report-table-track2d-predicted-mean-candidate th:nth-child(7),
    .report-table-track2d-predicted-mean-candidate td:nth-child(7),
    .report-table-track2d-predicted-mean-candidate th:nth-child(8),
    .report-table-track2d-predicted-mean-candidate td:nth-child(8) { width: 10%; }

    .report-table-track2d-predicted-mean-direction th:nth-child(1),
    .report-table-track2d-predicted-mean-direction td:nth-child(1) { width: 34%; }
    .report-table-track2d-predicted-mean-direction th:nth-child(2),
    .report-table-track2d-predicted-mean-direction td:nth-child(2) { width: 16%; }
    .report-table-track2d-predicted-mean-direction th:nth-child(3),
    .report-table-track2d-predicted-mean-direction td:nth-child(3),
    .report-table-track2d-predicted-mean-direction th:nth-child(4),
    .report-table-track2d-predicted-mean-direction td:nth-child(4),
    .report-table-track2d-predicted-mean-direction th:nth-child(5),
    .report-table-track2d-predicted-mean-direction td:nth-child(5),
    .report-table-track2d-predicted-mean-direction th:nth-child(6),
    .report-table-track2d-predicted-mean-direction td:nth-child(6) { width: 12.5%; }

    .report-table-wave1-high-order-artifact th:nth-child(1), .report-table-wave1-high-order-artifact td:nth-child(1) { width: 20%; }
    .report-table-wave1-high-order-artifact th:nth-child(2), .report-table-wave1-high-order-artifact td:nth-child(2) { width: 80%; }

    .report-table-wave1-high-order-key-value th:nth-child(1), .report-table-wave1-high-order-key-value td:nth-child(1) { width: 20%; }
    .report-table-wave1-high-order-key-value th:nth-child(2), .report-table-wave1-high-order-key-value td:nth-child(2) { width: 80%; }

    .report-table-wave1-high-order-leaderboard th:nth-child(1), .report-table-wave1-high-order-leaderboard td:nth-child(1) { width: 5%; }
    .report-table-wave1-high-order-leaderboard th:nth-child(2), .report-table-wave1-high-order-leaderboard td:nth-child(2) { width: 41%; }
    .report-table-wave1-high-order-leaderboard th:nth-child(3), .report-table-wave1-high-order-leaderboard td:nth-child(3) { width: 8%; }
    .report-table-wave1-high-order-leaderboard th:nth-child(4), .report-table-wave1-high-order-leaderboard td:nth-child(4) { width: 16%; }
    .report-table-wave1-high-order-leaderboard th:nth-child(5), .report-table-wave1-high-order-leaderboard td:nth-child(5) { width: 15%; }
    .report-table-wave1-high-order-leaderboard th:nth-child(6), .report-table-wave1-high-order-leaderboard td:nth-child(6) { width: 15%; }

    .report-table-wave1-high-order-registry th:nth-child(1), .report-table-wave1-high-order-registry td:nth-child(1) { width: 25%; }
    .report-table-wave1-high-order-registry th:nth-child(2), .report-table-wave1-high-order-registry td:nth-child(2) { width: 36%; }
    .report-table-wave1-high-order-registry th:nth-child(3), .report-table-wave1-high-order-registry td:nth-child(3) { width: 11%; }
    .report-table-wave1-high-order-registry th:nth-child(4), .report-table-wave1-high-order-registry td:nth-child(4) { width: 28%; }

    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(1), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(1) { width: 4%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(2), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(2) { width: 42%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(3), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(3) { width: 6%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(4), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(4) { width: 12%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(5), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(5) { width: 12%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(6), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(6) { width: 12%; }
    .report-table-wave1-periodic-mlp-leaderboard th:nth-child(7), .report-table-wave1-periodic-mlp-leaderboard td:nth-child(7) { width: 12%; }

    .report-table-wave1-periodic-mlp-registry th:nth-child(1), .report-table-wave1-periodic-mlp-registry td:nth-child(1) { width: 16%; }
    .report-table-wave1-periodic-mlp-registry th:nth-child(2), .report-table-wave1-periodic-mlp-registry td:nth-child(2) { width: 43%; }
    .report-table-wave1-periodic-mlp-registry th:nth-child(3), .report-table-wave1-periodic-mlp-registry td:nth-child(3) { width: 8%; }
    .report-table-wave1-periodic-mlp-registry th:nth-child(4), .report-table-wave1-periodic-mlp-registry td:nth-child(4) { width: 33%; }

    .report-table-wave2-temporal-artifact th:nth-child(1), .report-table-wave2-temporal-artifact td:nth-child(1) { width: 15%; }
    .report-table-wave2-temporal-artifact th:nth-child(2), .report-table-wave2-temporal-artifact td:nth-child(2) { width: 85%; }

    .report-table-wave2-temporal-leaderboard {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-wave2-temporal-leaderboard th,
    .report-table-wave2-temporal-leaderboard td,
    .report-table-wave2-temporal-registry th,
    .report-table-wave2-temporal-registry td {
      padding: 4px 4px;
      vertical-align: middle;
    }

    .report-table-wave2-temporal-leaderboard th:nth-child(1), .report-table-wave2-temporal-leaderboard td:nth-child(1) { width: 5%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(2), .report-table-wave2-temporal-leaderboard td:nth-child(2) { width: 25%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(3), .report-table-wave2-temporal-leaderboard td:nth-child(3) { width: 25%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(4), .report-table-wave2-temporal-leaderboard td:nth-child(4) { width: 9%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(5), .report-table-wave2-temporal-leaderboard td:nth-child(5) { width: 9%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(6), .report-table-wave2-temporal-leaderboard td:nth-child(6) { width: 9%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(7), .report-table-wave2-temporal-leaderboard td:nth-child(7) { width: 9%; }
    .report-table-wave2-temporal-leaderboard th:nth-child(8), .report-table-wave2-temporal-leaderboard td:nth-child(8) { width: 9%; }

    .report-table-wave2-temporal-registry {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-wave2-temporal-registry th:nth-child(1), .report-table-wave2-temporal-registry td:nth-child(1) { width: 31%; }
    .report-table-wave2-temporal-registry th:nth-child(2), .report-table-wave2-temporal-registry td:nth-child(2) { width: 42%; }
    .report-table-wave2-temporal-registry th:nth-child(3), .report-table-wave2-temporal-registry td:nth-child(3) {
      width: 8.5%;
      white-space: nowrap;
      word-break: normal;
      overflow-wrap: normal;
    }
    .report-table-wave2-temporal-registry th:nth-child(4), .report-table-wave2-temporal-registry td:nth-child(4) { width: 18.5%; }

    .report-table-track2f-branch-results,
    .report-table-track2f-scalar-leaderboard {
      font-size: 6.55pt;
      line-height: 1.15;
    }

    .report-table-track2f-branch-results th,
    .report-table-track2f-branch-results td,
    .report-table-track2f-scalar-leaderboard th,
    .report-table-track2f-scalar-leaderboard td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2f-branch-results th:nth-child(1), .report-table-track2f-branch-results td:nth-child(1) { width: 7%; }
    .report-table-track2f-branch-results th:nth-child(2), .report-table-track2f-branch-results td:nth-child(2) { width: 11%; }
    .report-table-track2f-branch-results th:nth-child(3), .report-table-track2f-branch-results td:nth-child(3) { width: 29%; }
    .report-table-track2f-branch-results th:nth-child(4), .report-table-track2f-branch-results td:nth-child(4) { width: 23%; }
    .report-table-track2f-branch-results th:nth-child(5), .report-table-track2f-branch-results td:nth-child(5) { width: 8%; }
    .report-table-track2f-branch-results th:nth-child(6), .report-table-track2f-branch-results td:nth-child(6) { width: 8%; }
    .report-table-track2f-branch-results th:nth-child(7), .report-table-track2f-branch-results td:nth-child(7) { width: 8%; }
    .report-table-track2f-branch-results th:nth-child(8), .report-table-track2f-branch-results td:nth-child(8) { width: 6%; }

    .report-table-track2f-scalar-leaderboard th:nth-child(1), .report-table-track2f-scalar-leaderboard td:nth-child(1) { width: 5%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(2), .report-table-track2f-scalar-leaderboard td:nth-child(2) { width: 7%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(3), .report-table-track2f-scalar-leaderboard td:nth-child(3) { width: 30%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(4), .report-table-track2f-scalar-leaderboard td:nth-child(4) { width: 24%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(5), .report-table-track2f-scalar-leaderboard td:nth-child(5) { width: 8%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(6), .report-table-track2f-scalar-leaderboard td:nth-child(6) { width: 8%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(7), .report-table-track2f-scalar-leaderboard td:nth-child(7) { width: 8%; }
    .report-table-track2f-scalar-leaderboard th:nth-child(8), .report-table-track2f-scalar-leaderboard td:nth-child(8) { width: 10%; }

    .report-table-track2g-branch-results,
    .report-table-track2g-loss-leaderboard,
    .report-table-track2g-baseline-comparison,
    .report-table-track2g-registry-effects {
      font-size: 6.65pt;
      line-height: 1.15;
    }

    .report-table-track2g-branch-results th,
    .report-table-track2g-branch-results td,
    .report-table-track2g-loss-leaderboard th,
    .report-table-track2g-loss-leaderboard td,
    .report-table-track2g-baseline-comparison th,
    .report-table-track2g-baseline-comparison td,
    .report-table-track2g-registry-effects th,
    .report-table-track2g-registry-effects td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2g-branch-results th:nth-child(1), .report-table-track2g-branch-results td:nth-child(1) { width: 9%; }
    .report-table-track2g-branch-results th:nth-child(2), .report-table-track2g-branch-results td:nth-child(2) { width: 37%; }
    .report-table-track2g-branch-results th:nth-child(3), .report-table-track2g-branch-results td:nth-child(3) { width: 18%; }
    .report-table-track2g-branch-results th:nth-child(4), .report-table-track2g-branch-results td:nth-child(4) { width: 12%; }
    .report-table-track2g-branch-results th:nth-child(5), .report-table-track2g-branch-results td:nth-child(5) { width: 12%; }
    .report-table-track2g-branch-results th:nth-child(6), .report-table-track2g-branch-results td:nth-child(6) { width: 12%; }

    .report-table-track2g-loss-leaderboard th:nth-child(1), .report-table-track2g-loss-leaderboard td:nth-child(1) { width: 5%; }
    .report-table-track2g-loss-leaderboard th:nth-child(2), .report-table-track2g-loss-leaderboard td:nth-child(2) { width: 8%; }
    .report-table-track2g-loss-leaderboard th:nth-child(3), .report-table-track2g-loss-leaderboard td:nth-child(3) { width: 25.5%; }
    .report-table-track2g-loss-leaderboard th:nth-child(4), .report-table-track2g-loss-leaderboard td:nth-child(4) { width: 25.5%; }
    .report-table-track2g-loss-leaderboard th:nth-child(5), .report-table-track2g-loss-leaderboard td:nth-child(5) { width: 12%; }
    .report-table-track2g-loss-leaderboard th:nth-child(6), .report-table-track2g-loss-leaderboard td:nth-child(6) { width: 12%; }
    .report-table-track2g-loss-leaderboard th:nth-child(7), .report-table-track2g-loss-leaderboard td:nth-child(7) { width: 12%; }

    .report-table-track2g-baseline-comparison th:nth-child(1), .report-table-track2g-baseline-comparison td:nth-child(1) { width: 8%; }
    .report-table-track2g-baseline-comparison th:nth-child(2), .report-table-track2g-baseline-comparison td:nth-child(2) { width: 27%; }
    .report-table-track2g-baseline-comparison th:nth-child(3), .report-table-track2g-baseline-comparison td:nth-child(3) { width: 11%; }
    .report-table-track2g-baseline-comparison th:nth-child(4), .report-table-track2g-baseline-comparison td:nth-child(4) { width: 32%; }
    .report-table-track2g-baseline-comparison th:nth-child(5), .report-table-track2g-baseline-comparison td:nth-child(5) { width: 11%; }
    .report-table-track2g-baseline-comparison th:nth-child(6), .report-table-track2g-baseline-comparison td:nth-child(6) { width: 11%; }

    .report-table-track2g-registry-effects th:nth-child(1), .report-table-track2g-registry-effects td:nth-child(1) { width: 33.333%; }
    .report-table-track2g-registry-effects th:nth-child(2), .report-table-track2g-registry-effects td:nth-child(2) { width: 33.333%; }
    .report-table-track2g-registry-effects th:nth-child(3), .report-table-track2g-registry-effects td:nth-child(3) { width: 33.333%; }

    .report-table-track2-best-model-collage {
      font-size: 6.85pt;
      line-height: 1.18;
    }

    .report-table-track2-best-model-collage th,
    .report-table-track2-best-model-collage td {
      padding: 3px 4px;
      vertical-align: middle;
    }

    .report-table-track2-best-model-collage th:nth-child(1), .report-table-track2-best-model-collage td:nth-child(1) { width: 27%; }
    .report-table-track2-best-model-collage th:nth-child(2), .report-table-track2-best-model-collage td:nth-child(2) { width: 25%; }
    .report-table-track2-best-model-collage th:nth-child(3), .report-table-track2-best-model-collage td:nth-child(3) { width: 7%; }
    .report-table-track2-best-model-collage th:nth-child(4), .report-table-track2-best-model-collage td:nth-child(4) { width: 13.666%; }
    .report-table-track2-best-model-collage th:nth-child(5), .report-table-track2-best-model-collage td:nth-child(5) { width: 13.666%; }
    .report-table-track2-best-model-collage th:nth-child(6), .report-table-track2-best-model-collage td:nth-child(6) { width: 13.666%; }

    .report-table-track2-official-verification-rule,
    .report-table-track2-official-pipeline-coverage,
    .report-table-track2-official-best-composite,
    .report-table-track2-official-static-baseline,
    .report-table-track2-official-campaign-ledger,
    .report-table-track2-official-candidate-refresh,
    .report-table-track2-official-track2fbis-result {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-track2-official-verification-rule th,
    .report-table-track2-official-verification-rule td,
    .report-table-track2-official-pipeline-coverage th,
    .report-table-track2-official-pipeline-coverage td,
    .report-table-track2-official-best-composite th,
    .report-table-track2-official-best-composite td,
    .report-table-track2-official-static-baseline th,
    .report-table-track2-official-static-baseline td,
    .report-table-track2-official-campaign-ledger th,
    .report-table-track2-official-campaign-ledger td,
    .report-table-track2-official-candidate-refresh th,
    .report-table-track2-official-candidate-refresh td,
    .report-table-track2-official-track2fbis-result th,
    .report-table-track2-official-track2fbis-result td {
      padding: 4px 4px;
      vertical-align: middle;
    }

    .report-table-track2-official-verification-rule th:nth-child(1), .report-table-track2-official-verification-rule td:nth-child(1) { width: 18%; }
    .report-table-track2-official-verification-rule th:nth-child(2), .report-table-track2-official-verification-rule td:nth-child(2) { width: 41%; }
    .report-table-track2-official-verification-rule th:nth-child(3), .report-table-track2-official-verification-rule td:nth-child(3) { width: 41%; }

    .report-table-track2-official-pipeline-coverage th:nth-child(1), .report-table-track2-official-pipeline-coverage td:nth-child(1) { width: 25%; }
    .report-table-track2-official-pipeline-coverage th:nth-child(2), .report-table-track2-official-pipeline-coverage td:nth-child(2) { width: 31%; }
    .report-table-track2-official-pipeline-coverage th:nth-child(3), .report-table-track2-official-pipeline-coverage td:nth-child(3) { width: 13%; }
    .report-table-track2-official-pipeline-coverage th:nth-child(4), .report-table-track2-official-pipeline-coverage td:nth-child(4) { width: 31%; }

    .report-table-track2-official-best-composite th:nth-child(1), .report-table-track2-official-best-composite td:nth-child(1) { width: 26%; }
    .report-table-track2-official-best-composite th:nth-child(2), .report-table-track2-official-best-composite td:nth-child(2) { width: 20%; }
    .report-table-track2-official-best-composite th:nth-child(3), .report-table-track2-official-best-composite td:nth-child(3) { width: 10%; }
    .report-table-track2-official-best-composite th:nth-child(4), .report-table-track2-official-best-composite td:nth-child(4) { width: 11%; }
    .report-table-track2-official-best-composite th:nth-child(5), .report-table-track2-official-best-composite td:nth-child(5) { width: 11%; }
    .report-table-track2-official-best-composite th:nth-child(6), .report-table-track2-official-best-composite td:nth-child(6) { width: 11%; }
    .report-table-track2-official-best-composite th:nth-child(7), .report-table-track2-official-best-composite td:nth-child(7) { width: 11%; }

    .report-table-track2-official-static-baseline th:nth-child(1), .report-table-track2-official-static-baseline td:nth-child(1) { width: 24%; }
    .report-table-track2-official-static-baseline th:nth-child(2), .report-table-track2-official-static-baseline td:nth-child(2) { width: 28%; }
    .report-table-track2-official-static-baseline th:nth-child(3), .report-table-track2-official-static-baseline td:nth-child(3) { width: 12%; }
    .report-table-track2-official-static-baseline th:nth-child(4), .report-table-track2-official-static-baseline td:nth-child(4) { width: 12%; }
    .report-table-track2-official-static-baseline th:nth-child(5), .report-table-track2-official-static-baseline td:nth-child(5) { width: 12%; }
    .report-table-track2-official-static-baseline th:nth-child(6), .report-table-track2-official-static-baseline td:nth-child(6) { width: 12%; }

    .report-table-track2-official-campaign-ledger th:nth-child(1), .report-table-track2-official-campaign-ledger td:nth-child(1) { width: 9%; }
    .report-table-track2-official-campaign-ledger th:nth-child(2), .report-table-track2-official-campaign-ledger td:nth-child(2) { width: 27%; }
    .report-table-track2-official-campaign-ledger th:nth-child(3), .report-table-track2-official-campaign-ledger td:nth-child(3) { width: 13%; }
    .report-table-track2-official-campaign-ledger th:nth-child(4), .report-table-track2-official-campaign-ledger td:nth-child(4) { width: 17%; }
    .report-table-track2-official-campaign-ledger th:nth-child(5), .report-table-track2-official-campaign-ledger td:nth-child(5) { width: 17%; }
    .report-table-track2-official-campaign-ledger th:nth-child(6), .report-table-track2-official-campaign-ledger td:nth-child(6) { width: 17%; }

    .report-table-track2-official-candidate-refresh th:nth-child(1), .report-table-track2-official-candidate-refresh td:nth-child(1) { width: 8%; }
    .report-table-track2-official-candidate-refresh th:nth-child(2), .report-table-track2-official-candidate-refresh td:nth-child(2) { width: 22%; }
    .report-table-track2-official-candidate-refresh th:nth-child(3), .report-table-track2-official-candidate-refresh td:nth-child(3) { width: 43%; }
    .report-table-track2-official-candidate-refresh th:nth-child(4), .report-table-track2-official-candidate-refresh td:nth-child(4) { width: 27%; }

    .report-table-track2-official-track2fbis-result th:nth-child(1), .report-table-track2-official-track2fbis-result td:nth-child(1) { width: 14%; }
    .report-table-track2-official-track2fbis-result th:nth-child(2), .report-table-track2-official-track2fbis-result td:nth-child(2) { width: 36%; }
    .report-table-track2-official-track2fbis-result th:nth-child(3), .report-table-track2-official-track2fbis-result td:nth-child(3) { width: 23%; }
    .report-table-track2-official-track2fbis-result th:nth-child(4), .report-table-track2-official-track2fbis-result td:nth-child(4) { width: 9%; }
    .report-table-track2-official-track2fbis-result th:nth-child(5), .report-table-track2-official-track2fbis-result td:nth-child(5) { width: 9%; }
    .report-table-track2-official-track2fbis-result th:nth-child(6), .report-table-track2-official-track2fbis-result td:nth-child(6) { width: 9%; }

    .report-table-track2-curve-first-ranking,
    .report-table-track2-curve-payload-diagnostics,
    .report-table-track2-surface-leader {
      font-size: 6.55pt;
      line-height: 1.16;
    }

    .report-table-track2-curve-first-ranking th,
    .report-table-track2-curve-first-ranking td,
    .report-table-track2-curve-payload-diagnostics th,
    .report-table-track2-curve-payload-diagnostics td,
    .report-table-track2-surface-leader th,
    .report-table-track2-surface-leader td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2-curve-first-ranking th:nth-child(1), .report-table-track2-curve-first-ranking td:nth-child(1) { width: 5%; }
    .report-table-track2-curve-first-ranking th:nth-child(2), .report-table-track2-curve-first-ranking td:nth-child(2) { width: 22%; }
    .report-table-track2-curve-first-ranking th:nth-child(3), .report-table-track2-curve-first-ranking td:nth-child(3) { width: 16%; }
    .report-table-track2-curve-first-ranking th:nth-child(4), .report-table-track2-curve-first-ranking td:nth-child(4) { width: 7%; }
    .report-table-track2-curve-first-ranking th:nth-child(5), .report-table-track2-curve-first-ranking td:nth-child(5) { width: 7%; }
    .report-table-track2-curve-first-ranking th:nth-child(6), .report-table-track2-curve-first-ranking td:nth-child(6) { width: 6%; }
    .report-table-track2-curve-first-ranking th:nth-child(7), .report-table-track2-curve-first-ranking td:nth-child(7) { width: 12%; }
    .report-table-track2-curve-first-ranking th:nth-child(8), .report-table-track2-curve-first-ranking td:nth-child(8) { width: 12%; }
    .report-table-track2-curve-first-ranking th:nth-child(9), .report-table-track2-curve-first-ranking td:nth-child(9) { width: 13%; }

    .report-table-track2-curve-payload-diagnostics th:nth-child(1), .report-table-track2-curve-payload-diagnostics td:nth-child(1) { width: 5%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(2), .report-table-track2-curve-payload-diagnostics td:nth-child(2) { width: 23%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(3), .report-table-track2-curve-payload-diagnostics td:nth-child(3) { width: 7%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(4), .report-table-track2-curve-payload-diagnostics td:nth-child(4) { width: 10%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(5), .report-table-track2-curve-payload-diagnostics td:nth-child(5) { width: 10%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(6), .report-table-track2-curve-payload-diagnostics td:nth-child(6) { width: 12%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(7), .report-table-track2-curve-payload-diagnostics td:nth-child(7) { width: 13%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(8), .report-table-track2-curve-payload-diagnostics td:nth-child(8) { width: 10%; }
    .report-table-track2-curve-payload-diagnostics th:nth-child(9), .report-table-track2-curve-payload-diagnostics td:nth-child(9) { width: 10%; }

    .report-table-track2-surface-leader th:nth-child(1), .report-table-track2-surface-leader td:nth-child(1) { width: 7%; }
    .report-table-track2-surface-leader th:nth-child(2), .report-table-track2-surface-leader td:nth-child(2) { width: 24%; }
    .report-table-track2-surface-leader th:nth-child(3), .report-table-track2-surface-leader td:nth-child(3) { width: 22%; }
    .report-table-track2-surface-leader th:nth-child(4), .report-table-track2-surface-leader td:nth-child(4) { width: 13%; }
    .report-table-track2-surface-leader th:nth-child(5), .report-table-track2-surface-leader td:nth-child(5) { width: 7%; }
    .report-table-track2-surface-leader th:nth-child(6), .report-table-track2-surface-leader td:nth-child(6) { width: 9%; }
    .report-table-track2-surface-leader th:nth-child(7), .report-table-track2-surface-leader td:nth-child(7) { width: 9%; }
    .report-table-track2-surface-leader th:nth-child(8), .report-table-track2-surface-leader td:nth-child(8) { width: 9%; }

    .report-table-track2-mean-centered-top,
    .report-table-track2-mean-centered-group {
      font-size: 6.55pt;
      line-height: 1.16;
    }

    .report-table-track2-mean-centered-top th,
    .report-table-track2-mean-centered-top td,
    .report-table-track2-mean-centered-group th,
    .report-table-track2-mean-centered-group td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2-mean-centered-top th,
    .report-table-track2-mean-centered-group th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track2-mean-centered-top th:nth-child(1), .report-table-track2-mean-centered-top td:nth-child(1) { width: 4%; }
    .report-table-track2-mean-centered-top th:nth-child(2), .report-table-track2-mean-centered-top td:nth-child(2) { width: 42%; }
    .report-table-track2-mean-centered-top th:nth-child(3), .report-table-track2-mean-centered-top td:nth-child(3) { width: 8%; }
    .report-table-track2-mean-centered-top th:nth-child(4), .report-table-track2-mean-centered-top td:nth-child(4) { width: 11.5%; }
    .report-table-track2-mean-centered-top th:nth-child(5), .report-table-track2-mean-centered-top td:nth-child(5) { width: 11.5%; }
    .report-table-track2-mean-centered-top th:nth-child(6), .report-table-track2-mean-centered-top td:nth-child(6) { width: 11.5%; }
    .report-table-track2-mean-centered-top th:nth-child(7), .report-table-track2-mean-centered-top td:nth-child(7) { width: 11.5%; }

    .report-table-track2-mean-centered-group th:nth-child(1), .report-table-track2-mean-centered-group td:nth-child(1) { width: 42%; }
    .report-table-track2-mean-centered-group th:nth-child(2), .report-table-track2-mean-centered-group td:nth-child(2) { width: 8%; }
    .report-table-track2-mean-centered-group th:nth-child(3), .report-table-track2-mean-centered-group td:nth-child(3) { width: 12.5%; }
    .report-table-track2-mean-centered-group th:nth-child(4), .report-table-track2-mean-centered-group td:nth-child(4) { width: 12.5%; }
    .report-table-track2-mean-centered-group th:nth-child(5), .report-table-track2-mean-centered-group td:nth-child(5) { width: 12.5%; }
    .report-table-track2-mean-centered-group th:nth-child(6), .report-table-track2-mean-centered-group td:nth-child(6) { width: 12.5%; }

    .report-table-track2d-mean-offset {
      font-size: 6.45pt;
      line-height: 1.14;
    }

    .report-table-track2d-mean-offset th,
    .report-table-track2d-mean-offset td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2d-mean-offset th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track2d-mean-offset th:nth-child(1), .report-table-track2d-mean-offset td:nth-child(1) { width: 4%; }
    .report-table-track2d-mean-offset th:nth-child(2), .report-table-track2d-mean-offset td:nth-child(2) { width: 36%; }
    .report-table-track2d-mean-offset th:nth-child(3), .report-table-track2d-mean-offset td:nth-child(3) { width: 6%; }
    .report-table-track2d-mean-offset th:nth-child(4), .report-table-track2d-mean-offset td:nth-child(4) { width: 10.8%; }
    .report-table-track2d-mean-offset th:nth-child(5), .report-table-track2d-mean-offset td:nth-child(5) { width: 10.8%; }
    .report-table-track2d-mean-offset th:nth-child(6), .report-table-track2d-mean-offset td:nth-child(6) { width: 10.8%; }
    .report-table-track2d-mean-offset th:nth-child(7), .report-table-track2d-mean-offset td:nth-child(7) { width: 10.8%; }
    .report-table-track2d-mean-offset th:nth-child(8), .report-table-track2d-mean-offset td:nth-child(8) { width: 10.8%; }

    .report-table-track2e-offset-feasibility {
      font-size: 6.35pt;
      line-height: 1.13;
    }

    .report-table-track2e-offset-feasibility th,
    .report-table-track2e-offset-feasibility td {
      padding: 3px 3px;
      vertical-align: middle;
    }

    .report-table-track2e-offset-feasibility th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track2e-offset-feasibility th:nth-child(1), .report-table-track2e-offset-feasibility td:nth-child(1) { width: 4%; }
    .report-table-track2e-offset-feasibility th:nth-child(2), .report-table-track2e-offset-feasibility td:nth-child(2) { width: 30%; }
    .report-table-track2e-offset-feasibility th:nth-child(3), .report-table-track2e-offset-feasibility td:nth-child(3) { width: 6%; }
    .report-table-track2e-offset-feasibility th:nth-child(4), .report-table-track2e-offset-feasibility td:nth-child(4) { width: 7%; }
    .report-table-track2e-offset-feasibility th:nth-child(5), .report-table-track2e-offset-feasibility td:nth-child(5) { width: 10%; }
    .report-table-track2e-offset-feasibility th:nth-child(6), .report-table-track2e-offset-feasibility td:nth-child(6) { width: 10%; }
    .report-table-track2e-offset-feasibility th:nth-child(7), .report-table-track2e-offset-feasibility td:nth-child(7) { width: 9%; }
    .report-table-track2e-offset-feasibility th:nth-child(8), .report-table-track2e-offset-feasibility td:nth-child(8) { width: 9%; }
    .report-table-track2e-offset-feasibility th:nth-child(9), .report-table-track2e-offset-feasibility td:nth-child(9) { width: 15%; }

    .report-table-track2-original-onnx-targets,
    .report-table-track2-original-onnx-metrics,
    .report-table-track2-original-onnx-curves {
      font-size: 7.0pt;
      line-height: 1.18;
    }

    .report-table-track2-original-onnx-targets th,
    .report-table-track2-original-onnx-targets td,
    .report-table-track2-original-onnx-metrics th,
    .report-table-track2-original-onnx-metrics td,
    .report-table-track2-original-onnx-curves th,
    .report-table-track2-original-onnx-curves td {
      padding: 4px 4px;
      text-align: center;
    }

    .report-table-track2-original-onnx-targets th,
    .report-table-track2-original-onnx-metrics th,
    .report-table-track2-original-onnx-curves th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track2-original-onnx-targets th:nth-child(1), .report-table-track2-original-onnx-targets td:nth-child(1) { width: 14%; }
    .report-table-track2-original-onnx-targets th:nth-child(2), .report-table-track2-original-onnx-targets td:nth-child(2) { width: 8%; }
    .report-table-track2-original-onnx-targets th:nth-child(3), .report-table-track2-original-onnx-targets td:nth-child(3) { width: 8%; }
    .report-table-track2-original-onnx-targets th:nth-child(4), .report-table-track2-original-onnx-targets td:nth-child(4) { width: 70%; }

    .report-table-track2-original-onnx-metrics th:nth-child(1), .report-table-track2-original-onnx-metrics td:nth-child(1) { width: 28%; }
    .report-table-track2-original-onnx-metrics th:nth-child(2), .report-table-track2-original-onnx-metrics td:nth-child(2) { width: 8%; }
    .report-table-track2-original-onnx-metrics th:nth-child(3), .report-table-track2-original-onnx-metrics td:nth-child(3) { width: 16%; }
    .report-table-track2-original-onnx-metrics th:nth-child(4), .report-table-track2-original-onnx-metrics td:nth-child(4) { width: 16%; }
    .report-table-track2-original-onnx-metrics th:nth-child(5), .report-table-track2-original-onnx-metrics td:nth-child(5) { width: 16%; }
    .report-table-track2-original-onnx-metrics th:nth-child(6), .report-table-track2-original-onnx-metrics td:nth-child(6) { width: 16%; }

    .report-table-track2-original-onnx-curves th,
    .report-table-track2-original-onnx-curves td {
      width: 16.666%;
    }

    .report-table-track2-forward-reference-pairwise,
    .report-table-track2-forward-reference-collage-metrics,
    .report-table-track2-forward-reference-collage-deltas {
      font-size: 7.05pt;
      line-height: 1.18;
    }

    .report-table-track2-forward-reference-pairwise th,
    .report-table-track2-forward-reference-pairwise td,
    .report-table-track2-forward-reference-collage-metrics th,
    .report-table-track2-forward-reference-collage-metrics td,
    .report-table-track2-forward-reference-collage-deltas th,
    .report-table-track2-forward-reference-collage-deltas td {
      padding: 4px 4px;
      text-align: center;
      vertical-align: middle;
    }

    .report-table-track2-forward-reference-pairwise th,
    .report-table-track2-forward-reference-collage-metrics th,
    .report-table-track2-forward-reference-collage-deltas th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track2-forward-reference-pairwise th:nth-child(1),
    .report-table-track2-forward-reference-pairwise td:nth-child(1) { width: 30%; }
    .report-table-track2-forward-reference-pairwise th:nth-child(n+2),
    .report-table-track2-forward-reference-pairwise td:nth-child(n+2) { width: 14%; }

    .report-table-track2-forward-reference-collage-metrics th:nth-child(1),
    .report-table-track2-forward-reference-collage-metrics td:nth-child(1) { width: 10%; }
    .report-table-track2-forward-reference-collage-metrics th:nth-child(2),
    .report-table-track2-forward-reference-collage-metrics td:nth-child(2) { width: 30%; }
    .report-table-track2-forward-reference-collage-metrics th:nth-child(n+3),
    .report-table-track2-forward-reference-collage-metrics td:nth-child(n+3) { width: 12%; }

    .report-table-track2-forward-reference-collage-deltas th:nth-child(1),
    .report-table-track2-forward-reference-collage-deltas td:nth-child(1) { width: 10%; }
    .report-table-track2-forward-reference-collage-deltas th:nth-child(2),
    .report-table-track2-forward-reference-collage-deltas td:nth-child(2) { width: 30%; }
    .report-table-track2-forward-reference-collage-deltas th:nth-child(n+3),
    .report-table-track2-forward-reference-collage-deltas td:nth-child(n+3) { width: 15%; }

    .report-table-repository-status-scalar-winner,
    .report-table-repository-status-hpo-leader,
    .report-table-repository-status-harmonic-results,
    .report-table-repository-status-temporal-winner,
    .report-table-repository-status-temporal-surfaces,
    .report-table-repository-status-wave2b-scalar,
    .report-table-repository-status-wave2b-track2,
    .report-table-repository-status-wave2c-scalar,
    .report-table-repository-status-wave2c-track2,
    .report-table-repository-status-wave2c-dense,
    .report-table-repository-status-track2-current,
    .report-table-repository-status-harmonic-bank {
      font-size: 6.7pt;
      line-height: 1.17;
    }

    .report-table-repository-status-scalar-winner th,
    .report-table-repository-status-scalar-winner td,
    .report-table-repository-status-hpo-leader th,
    .report-table-repository-status-hpo-leader td,
    .report-table-repository-status-harmonic-results th,
    .report-table-repository-status-harmonic-results td,
    .report-table-repository-status-temporal-winner th,
    .report-table-repository-status-temporal-winner td,
    .report-table-repository-status-temporal-surfaces th,
    .report-table-repository-status-temporal-surfaces td,
    .report-table-repository-status-wave2b-scalar th,
    .report-table-repository-status-wave2b-scalar td,
    .report-table-repository-status-wave2b-track2 th,
    .report-table-repository-status-wave2b-track2 td,
    .report-table-repository-status-wave2c-scalar th,
    .report-table-repository-status-wave2c-scalar td,
    .report-table-repository-status-wave2c-track2 th,
    .report-table-repository-status-wave2c-track2 td,
    .report-table-repository-status-wave2c-dense th,
    .report-table-repository-status-wave2c-dense td,
    .report-table-repository-status-track2-current th,
    .report-table-repository-status-track2-current td,
    .report-table-repository-status-harmonic-bank th,
    .report-table-repository-status-harmonic-bank td {
      padding: 3px 4px;
      vertical-align: middle;
    }

    .report-table-repository-status-scalar-winner th,
    .report-table-repository-status-hpo-leader th,
    .report-table-repository-status-harmonic-results th,
    .report-table-repository-status-temporal-winner th,
    .report-table-repository-status-temporal-surfaces th,
    .report-table-repository-status-wave2b-scalar th,
    .report-table-repository-status-wave2b-track2 th,
    .report-table-repository-status-wave2c-scalar th,
    .report-table-repository-status-wave2c-track2 th,
    .report-table-repository-status-wave2c-dense th,
    .report-table-repository-status-track2-current th,
    .report-table-repository-status-harmonic-bank th {
      line-height: 1.08;
    }

    .report-table-repository-status-scalar-winner th:nth-child(1), .report-table-repository-status-scalar-winner td:nth-child(1) { width: 7%; }
    .report-table-repository-status-scalar-winner th:nth-child(2), .report-table-repository-status-scalar-winner td:nth-child(2) { width: 42%; }
    .report-table-repository-status-scalar-winner th:nth-child(3), .report-table-repository-status-scalar-winner td:nth-child(3) { width: 25%; }
    .report-table-repository-status-scalar-winner th:nth-child(4), .report-table-repository-status-scalar-winner td:nth-child(4) { width: 13%; }
    .report-table-repository-status-scalar-winner th:nth-child(5), .report-table-repository-status-scalar-winner td:nth-child(5) { width: 13%; }

    .report-table-repository-status-hpo-leader th:nth-child(1), .report-table-repository-status-hpo-leader td:nth-child(1) { width: 5%; }
    .report-table-repository-status-hpo-leader th:nth-child(2), .report-table-repository-status-hpo-leader td:nth-child(2) { width: 20%; }
    .report-table-repository-status-hpo-leader th:nth-child(3), .report-table-repository-status-hpo-leader td:nth-child(3) { width: 20%; }
    .report-table-repository-status-hpo-leader th:nth-child(4), .report-table-repository-status-hpo-leader td:nth-child(4) { width: 20%; }
    .report-table-repository-status-hpo-leader th:nth-child(5), .report-table-repository-status-hpo-leader td:nth-child(5) { width: 17.5%; }
    .report-table-repository-status-hpo-leader th:nth-child(6), .report-table-repository-status-hpo-leader td:nth-child(6) { width: 17.5%; }

    .report-table-repository-status-harmonic-results th:nth-child(1), .report-table-repository-status-harmonic-results td:nth-child(1) { width: 30%; }
    .report-table-repository-status-harmonic-results th:nth-child(2), .report-table-repository-status-harmonic-results td:nth-child(2) { width: 40%; }
    .report-table-repository-status-harmonic-results th:nth-child(3), .report-table-repository-status-harmonic-results td:nth-child(3) { width: 14%; }
    .report-table-repository-status-harmonic-results th:nth-child(4), .report-table-repository-status-harmonic-results td:nth-child(4) { width: 16%; }

    .report-table-repository-status-temporal-winner th:nth-child(1), .report-table-repository-status-temporal-winner td:nth-child(1) { width: 43%; }
    .report-table-repository-status-temporal-winner th:nth-child(2), .report-table-repository-status-temporal-winner td:nth-child(2) { width: 25%; }
    .report-table-repository-status-temporal-winner th:nth-child(3), .report-table-repository-status-temporal-winner td:nth-child(3) { width: 6%; }
    .report-table-repository-status-temporal-winner th:nth-child(4), .report-table-repository-status-temporal-winner td:nth-child(4) { width: 13%; }
    .report-table-repository-status-temporal-winner th:nth-child(5), .report-table-repository-status-temporal-winner td:nth-child(5) { width: 13%; }

    .report-table-repository-status-temporal-surfaces th:nth-child(1), .report-table-repository-status-temporal-surfaces td:nth-child(1) { width: 8%; }
    .report-table-repository-status-temporal-surfaces th:nth-child(2), .report-table-repository-status-temporal-surfaces td:nth-child(2) { width: 48%; }
    .report-table-repository-status-temporal-surfaces th:nth-child(3), .report-table-repository-status-temporal-surfaces td:nth-child(3) { width: 27%; }
    .report-table-repository-status-temporal-surfaces th:nth-child(4), .report-table-repository-status-temporal-surfaces td:nth-child(4) { width: 17%; }

    .report-table-repository-status-wave2b-scalar th:nth-child(1), .report-table-repository-status-wave2b-scalar td:nth-child(1) { width: 39%; }
    .report-table-repository-status-wave2b-scalar th:nth-child(2), .report-table-repository-status-wave2b-scalar td:nth-child(2) { width: 27%; }
    .report-table-repository-status-wave2b-scalar th:nth-child(3), .report-table-repository-status-wave2b-scalar td:nth-child(3) { width: 10%; }
    .report-table-repository-status-wave2b-scalar th:nth-child(4), .report-table-repository-status-wave2b-scalar td:nth-child(4) { width: 12%; }
    .report-table-repository-status-wave2b-scalar th:nth-child(5), .report-table-repository-status-wave2b-scalar td:nth-child(5) { width: 12%; }

    .report-table-repository-status-wave2b-track2 th:nth-child(1), .report-table-repository-status-wave2b-track2 td:nth-child(1) { width: 40%; }
    .report-table-repository-status-wave2b-track2 th:nth-child(2), .report-table-repository-status-wave2b-track2 td:nth-child(2) { width: 11%; }
    .report-table-repository-status-wave2b-track2 th:nth-child(3), .report-table-repository-status-wave2b-track2 td:nth-child(3) { width: 16.333%; }
    .report-table-repository-status-wave2b-track2 th:nth-child(4), .report-table-repository-status-wave2b-track2 td:nth-child(4) { width: 16.333%; }
    .report-table-repository-status-wave2b-track2 th:nth-child(5), .report-table-repository-status-wave2b-track2 td:nth-child(5) { width: 16.333%; }

    .report-table-repository-status-wave2c-scalar th:nth-child(1), .report-table-repository-status-wave2c-scalar td:nth-child(1) { width: 29%; }
    .report-table-repository-status-wave2c-scalar th:nth-child(2), .report-table-repository-status-wave2c-scalar td:nth-child(2) { width: 29%; }
    .report-table-repository-status-wave2c-scalar th:nth-child(3), .report-table-repository-status-wave2c-scalar td:nth-child(3) { width: 10%; }
    .report-table-repository-status-wave2c-scalar th:nth-child(4), .report-table-repository-status-wave2c-scalar td:nth-child(4) { width: 7%; }
    .report-table-repository-status-wave2c-scalar th:nth-child(5), .report-table-repository-status-wave2c-scalar td:nth-child(5) { width: 12.5%; }
    .report-table-repository-status-wave2c-scalar th:nth-child(6), .report-table-repository-status-wave2c-scalar td:nth-child(6) { width: 12.5%; }

    .report-table-repository-status-wave2c-track2 th:nth-child(1), .report-table-repository-status-wave2c-track2 td:nth-child(1) { width: 8%; }
    .report-table-repository-status-wave2c-track2 th:nth-child(2), .report-table-repository-status-wave2c-track2 td:nth-child(2) { width: 39%; }
    .report-table-repository-status-wave2c-track2 th:nth-child(3), .report-table-repository-status-wave2c-track2 td:nth-child(3) { width: 14%; }
    .report-table-repository-status-wave2c-track2 th:nth-child(4), .report-table-repository-status-wave2c-track2 td:nth-child(4) { width: 13%; }
    .report-table-repository-status-wave2c-track2 th:nth-child(5), .report-table-repository-status-wave2c-track2 td:nth-child(5) { width: 13%; }
    .report-table-repository-status-wave2c-track2 th:nth-child(6), .report-table-repository-status-wave2c-track2 td:nth-child(6) { width: 13%; }

    .report-table-repository-status-wave2c-dense th:nth-child(1), .report-table-repository-status-wave2c-dense td:nth-child(1) { width: 8%; }
    .report-table-repository-status-wave2c-dense th:nth-child(2), .report-table-repository-status-wave2c-dense td:nth-child(2) { width: 47%; }
    .report-table-repository-status-wave2c-dense th:nth-child(3), .report-table-repository-status-wave2c-dense td:nth-child(3) { width: 17%; }
    .report-table-repository-status-wave2c-dense th:nth-child(4), .report-table-repository-status-wave2c-dense td:nth-child(4) { width: 14%; }
    .report-table-repository-status-wave2c-dense th:nth-child(5), .report-table-repository-status-wave2c-dense td:nth-child(5) { width: 14%; }

    .report-table-repository-status-track2-current th:nth-child(1), .report-table-repository-status-track2-current td:nth-child(1) { width: 18%; }
    .report-table-repository-status-track2-current th:nth-child(2), .report-table-repository-status-track2-current td:nth-child(2) { width: 43%; }
    .report-table-repository-status-track2-current th:nth-child(3), .report-table-repository-status-track2-current td:nth-child(3) { width: 13%; }
    .report-table-repository-status-track2-current th:nth-child(4), .report-table-repository-status-track2-current td:nth-child(4) { width: 13%; }
    .report-table-repository-status-track2-current th:nth-child(5), .report-table-repository-status-track2-current td:nth-child(5) { width: 13%; }

    .report-table-repository-status-harmonic-bank th:nth-child(1), .report-table-repository-status-harmonic-bank td:nth-child(1) { width: 34%; }
    .report-table-repository-status-harmonic-bank th:nth-child(2), .report-table-repository-status-harmonic-bank td:nth-child(2) { width: 36%; }
    .report-table-repository-status-harmonic-bank th:nth-child(3), .report-table-repository-status-harmonic-bank td:nth-child(3) { width: 30%; }

    .report-table-historical-results,
    .report-table-phase-results,
    .report-table-ranking-results {
      font-size: 7.05pt;
      line-height: 1.22;
    }

    .report-table-historical-results th,
    .report-table-historical-results td,
    .report-table-phase-results th,
    .report-table-phase-results td,
    .report-table-ranking-results th,
    .report-table-ranking-results td {
      padding: 4px 4px;
    }

    .report-table-historical-results th,
    .report-table-phase-results th,
    .report-table-ranking-results th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.16;
    }

    .report-table-historical-results th:nth-child(1), .report-table-historical-results td:nth-child(1) { width: 12%; }
    .report-table-historical-results th:nth-child(2), .report-table-historical-results td:nth-child(2) { width: 13%; }
    .report-table-historical-results th:nth-child(3), .report-table-historical-results td:nth-child(3) { width: 9%; }
    .report-table-historical-results th:nth-child(4), .report-table-historical-results td:nth-child(4) { width: 12%; }
    .report-table-historical-results th:nth-child(5), .report-table-historical-results td:nth-child(5) { width: 13.5%; }
    .report-table-historical-results th:nth-child(6), .report-table-historical-results td:nth-child(6) { width: 13.5%; }
    .report-table-historical-results th:nth-child(7), .report-table-historical-results td:nth-child(7) { width: 13.5%; }
    .report-table-historical-results th:nth-child(8), .report-table-historical-results td:nth-child(8) { width: 13.5%; }

    .report-table-phase-results th:nth-child(1), .report-table-phase-results td:nth-child(1) { width: 27%; }
    .report-table-phase-results th:nth-child(2), .report-table-phase-results td:nth-child(2) { width: 10%; }
    .report-table-phase-results th:nth-child(3), .report-table-phase-results td:nth-child(3) { width: 11%; }
    .report-table-phase-results th:nth-child(4), .report-table-phase-results td:nth-child(4) { width: 13%; }
    .report-table-phase-results th:nth-child(5), .report-table-phase-results td:nth-child(5) { width: 13%; }
    .report-table-phase-results th:nth-child(6), .report-table-phase-results td:nth-child(6) { width: 13%; }
    .report-table-phase-results th:nth-child(7), .report-table-phase-results td:nth-child(7) { width: 13%; }

    .report-table-ranking-results th:nth-child(1), .report-table-ranking-results td:nth-child(1) { width: 42%; }
    .report-table-ranking-results th:nth-child(2), .report-table-ranking-results td:nth-child(2) { width: 20%; }
    .report-table-ranking-results th:nth-child(3), .report-table-ranking-results td:nth-child(3) { width: 20%; }
    .report-table-ranking-results th:nth-child(4), .report-table-ranking-results td:nth-child(4) { width: 18%; }

    .report-table-track1-full-matrix-ranking {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-track1-full-matrix-ranking th,
    .report-table-track1-full-matrix-ranking td {
      padding: 4px 4px;
    }

    .report-table-track1-full-matrix-ranking th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-track1-full-matrix-ranking th:nth-child(1), .report-table-track1-full-matrix-ranking td:nth-child(1) { width: 6%; }
    .report-table-track1-full-matrix-ranking th:nth-child(2), .report-table-track1-full-matrix-ranking td:nth-child(2) { width: 29%; }
    .report-table-track1-full-matrix-ranking th:nth-child(3), .report-table-track1-full-matrix-ranking td:nth-child(3) { width: 8%; }
    .report-table-track1-full-matrix-ranking th:nth-child(4), .report-table-track1-full-matrix-ranking td:nth-child(4) { width: 16%; }
    .report-table-track1-full-matrix-ranking th:nth-child(5), .report-table-track1-full-matrix-ranking td:nth-child(5) { width: 7%; }
    .report-table-track1-full-matrix-ranking th:nth-child(6), .report-table-track1-full-matrix-ranking td:nth-child(6) { width: 8%; }
    .report-table-track1-full-matrix-ranking th:nth-child(7), .report-table-track1-full-matrix-ranking td:nth-child(7) { width: 6%; }
    .report-table-track1-full-matrix-ranking th:nth-child(8), .report-table-track1-full-matrix-ranking td:nth-child(8) { width: 8%; }
    .report-table-track1-full-matrix-ranking th:nth-child(9), .report-table-track1-full-matrix-ranking td:nth-child(9) { width: 12%; }

    .report-table-track1-full-matrix-cell-totals {
      font-size: 7.1pt;
      line-height: 1.2;
    }

    .report-table-track1-full-matrix-cell-totals th,
    .report-table-track1-full-matrix-cell-totals td {
      padding: 5px 5px;
    }

    .report-table-track1-full-matrix-cell-totals th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-track1-full-matrix-cell-totals th:nth-child(1), .report-table-track1-full-matrix-cell-totals td:nth-child(1) { width: 58%; }
    .report-table-track1-full-matrix-cell-totals th:nth-child(2), .report-table-track1-full-matrix-cell-totals td:nth-child(2) { width: 14%; }
    .report-table-track1-full-matrix-cell-totals th:nth-child(3), .report-table-track1-full-matrix-cell-totals td:nth-child(3) { width: 14%; }
    .report-table-track1-full-matrix-cell-totals th:nth-child(4), .report-table-track1-full-matrix-cell-totals td:nth-child(4) { width: 14%; }

    .report-table-track1-partial-closeout-family,
    .report-table-track1-partial-closeout-aggregate,
    .report-table-track1-final-closeout-family,
    .report-table-track1-final-closeout-aggregate {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-track1-partial-closeout-family th,
    .report-table-track1-partial-closeout-family td,
    .report-table-track1-partial-closeout-aggregate th,
    .report-table-track1-partial-closeout-aggregate td,
    .report-table-track1-final-closeout-family th,
    .report-table-track1-final-closeout-family td,
    .report-table-track1-final-closeout-aggregate th,
    .report-table-track1-final-closeout-aggregate td {
      padding: 4px 4px;
    }

    .report-table-track1-partial-closeout-family th,
    .report-table-track1-partial-closeout-aggregate th,
    .report-table-track1-final-closeout-family th,
    .report-table-track1-final-closeout-aggregate th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-track1-partial-closeout-family th:nth-child(1), .report-table-track1-partial-closeout-family td:nth-child(1) { width: 8%; }
    .report-table-track1-partial-closeout-family th:nth-child(2), .report-table-track1-partial-closeout-family td:nth-child(2) { width: 24%; }
    .report-table-track1-partial-closeout-family th:nth-child(3), .report-table-track1-partial-closeout-family td:nth-child(3) { width: 18%; }
    .report-table-track1-partial-closeout-family th:nth-child(4), .report-table-track1-partial-closeout-family td:nth-child(4) { width: 24%; }
    .report-table-track1-partial-closeout-family th:nth-child(5), .report-table-track1-partial-closeout-family td:nth-child(5) { width: 12%; }
    .report-table-track1-partial-closeout-family th:nth-child(6), .report-table-track1-partial-closeout-family td:nth-child(6) { width: 9%; }
    .report-table-track1-partial-closeout-family th:nth-child(7), .report-table-track1-partial-closeout-family td:nth-child(7) { width: 5%; }

    .report-table-track1-partial-closeout-aggregate th:nth-child(1), .report-table-track1-partial-closeout-aggregate td:nth-child(1) { width: 4%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(2), .report-table-track1-partial-closeout-aggregate td:nth-child(2) { width: 33%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(3), .report-table-track1-partial-closeout-aggregate td:nth-child(3) { width: 6%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(4), .report-table-track1-partial-closeout-aggregate td:nth-child(4) { width: 16%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(5), .report-table-track1-partial-closeout-aggregate td:nth-child(5) { width: 7%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(6), .report-table-track1-partial-closeout-aggregate td:nth-child(6) { width: 6%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(7), .report-table-track1-partial-closeout-aggregate td:nth-child(7) { width: 6%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(8), .report-table-track1-partial-closeout-aggregate td:nth-child(8) { width: 6%; }
    .report-table-track1-partial-closeout-aggregate th:nth-child(9), .report-table-track1-partial-closeout-aggregate td:nth-child(9) { width: 16%; }

    .report-table-track1-final-closeout-family th:nth-child(1), .report-table-track1-final-closeout-family td:nth-child(1) { width: 8%; }
    .report-table-track1-final-closeout-family th:nth-child(2), .report-table-track1-final-closeout-family td:nth-child(2) { width: 21%; }
    .report-table-track1-final-closeout-family th:nth-child(3), .report-table-track1-final-closeout-family td:nth-child(3) { width: 21%; }
    .report-table-track1-final-closeout-family th:nth-child(4), .report-table-track1-final-closeout-family td:nth-child(4) { width: 21%; }
    .report-table-track1-final-closeout-family th:nth-child(5), .report-table-track1-final-closeout-family td:nth-child(5) { width: 15%; }
    .report-table-track1-final-closeout-family th:nth-child(6), .report-table-track1-final-closeout-family td:nth-child(6) { width: 9%; }
    .report-table-track1-final-closeout-family th:nth-child(7), .report-table-track1-final-closeout-family td:nth-child(7) { width: 5%; }

    .report-table-track1-final-closeout-aggregate th:nth-child(1), .report-table-track1-final-closeout-aggregate td:nth-child(1) { width: 5%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(2), .report-table-track1-final-closeout-aggregate td:nth-child(2) { width: 32%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(3), .report-table-track1-final-closeout-aggregate td:nth-child(3) { width: 6%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(4), .report-table-track1-final-closeout-aggregate td:nth-child(4) { width: 16%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(5), .report-table-track1-final-closeout-aggregate td:nth-child(5) { width: 7%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(6), .report-table-track1-final-closeout-aggregate td:nth-child(6) { width: 6%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(7), .report-table-track1-final-closeout-aggregate td:nth-child(7) { width: 6%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(8), .report-table-track1-final-closeout-aggregate td:nth-child(8) { width: 6%; }
    .report-table-track1-final-closeout-aggregate th:nth-child(9), .report-table-track1-final-closeout-aggregate td:nth-child(9) { width: 16%; }

    .report-table-track1-open-cell-closeout-family {
      font-size: 6.85pt;
      line-height: 1.16;
    }

    .report-table-track1-open-cell-closeout-family th,
    .report-table-track1-open-cell-closeout-family td,
    .report-table-track1-open-cell-closeout-benchmark th,
    .report-table-track1-open-cell-closeout-benchmark td {
      padding: 4px 4px;
    }

    .report-table-track1-open-cell-closeout-family th,
    .report-table-track1-open-cell-closeout-benchmark th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-open-cell-closeout-family th:nth-child(1), .report-table-track1-open-cell-closeout-family td:nth-child(1) { width: 8%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(2), .report-table-track1-open-cell-closeout-family td:nth-child(2) { width: 40%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(3), .report-table-track1-open-cell-closeout-family td:nth-child(3) { width: 12%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(4), .report-table-track1-open-cell-closeout-family td:nth-child(4) { width: 16%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(5), .report-table-track1-open-cell-closeout-family td:nth-child(5) { width: 8%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(6), .report-table-track1-open-cell-closeout-family td:nth-child(6) { width: 8%; }
    .report-table-track1-open-cell-closeout-family th:nth-child(7), .report-table-track1-open-cell-closeout-family td:nth-child(7) { width: 8%; }

    .report-table-track1-open-cell-closeout-benchmark {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-track1-open-cell-closeout-benchmark th:nth-child(1), .report-table-track1-open-cell-closeout-benchmark td:nth-child(1) { width: 25%; }
    .report-table-track1-open-cell-closeout-benchmark th:nth-child(2), .report-table-track1-open-cell-closeout-benchmark td:nth-child(2) { width: 25%; }
    .report-table-track1-open-cell-closeout-benchmark th:nth-child(3), .report-table-track1-open-cell-closeout-benchmark td:nth-child(3) { width: 25%; }
    .report-table-track1-open-cell-closeout-benchmark th:nth-child(4), .report-table-track1-open-cell-closeout-benchmark td:nth-child(4) { width: 25%; }

    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(1), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(1) { width: 9%; }
    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(2), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(2) { width: 23%; }
    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(3), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(3) { width: 23%; }
    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(4), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(4) { width: 23%; }
    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(5), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(5) { width: 10%; }
    .report-table-track1-mlp-closeout-targeted-pair th:nth-child(6), .report-table-track1-mlp-closeout-targeted-pair td:nth-child(6) { width: 14%; }

    .report-table-track1-interrupted-svm-candidate-gains {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-track1-interrupted-svm-candidate-gains th,
    .report-table-track1-interrupted-svm-candidate-gains td {
      padding: 4px 4px;
    }

    .report-table-track1-interrupted-svm-candidate-gains th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-interrupted-svm-candidate-gains th:nth-child(1), .report-table-track1-interrupted-svm-candidate-gains td:nth-child(1) { width: 9%; }
    .report-table-track1-interrupted-svm-candidate-gains th:nth-child(2), .report-table-track1-interrupted-svm-candidate-gains td:nth-child(2) { width: 40%; }
    .report-table-track1-interrupted-svm-candidate-gains th:nth-child(3), .report-table-track1-interrupted-svm-candidate-gains td:nth-child(3) { width: 14%; }
    .report-table-track1-interrupted-svm-candidate-gains th:nth-child(4), .report-table-track1-interrupted-svm-candidate-gains td:nth-child(4) { width: 14%; }
    .report-table-track1-interrupted-svm-candidate-gains th:nth-child(5), .report-table-track1-interrupted-svm-candidate-gains td:nth-child(5) { width: 23%; }

    .report-table-track1-forward-dt-historical-replay-outcome {
      font-size: 10.4px;
    }

    .report-table-track1-forward-dt-historical-replay-outcome th,
    .report-table-track1-forward-dt-historical-replay-outcome td {
      font-size: 10.4px;
      line-height: 1.3;
    }

    .report-table-track1-forward-dt-historical-replay-outcome th {
      white-space: nowrap;
    }

    .report-table-track1-forward-dt-historical-replay-outcome th:nth-child(1), .report-table-track1-forward-dt-historical-replay-outcome td:nth-child(1) { width: 43%; }
    .report-table-track1-forward-dt-historical-replay-outcome th:nth-child(2), .report-table-track1-forward-dt-historical-replay-outcome td:nth-child(2) { width: 19%; }
    .report-table-track1-forward-dt-historical-replay-outcome th:nth-child(3), .report-table-track1-forward-dt-historical-replay-outcome td:nth-child(3) { width: 19%; }
    .report-table-track1-forward-dt-historical-replay-outcome th:nth-child(4), .report-table-track1-forward-dt-historical-replay-outcome td:nth-child(4) { width: 19%; }

    /* Reusable Cell-Repair Ranking Table Profile */
    .report-table-track1-svm-repair-ranking {
      font-size: 6.7pt;
      line-height: 1.16;
    }

    .report-table-track1-svm-repair-ranking th,
    .report-table-track1-svm-repair-ranking td {
      padding: 4px 4px;
    }

    .report-table-track1-svm-repair-ranking th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-svm-repair-ranking th:nth-child(1), .report-table-track1-svm-repair-ranking td:nth-child(1) { width: 5%; }
    .report-table-track1-svm-repair-ranking th:nth-child(2), .report-table-track1-svm-repair-ranking td:nth-child(2) { width: 24%; }
    .report-table-track1-svm-repair-ranking th:nth-child(3), .report-table-track1-svm-repair-ranking td:nth-child(3) { width: 16%; }
    .report-table-track1-svm-repair-ranking th:nth-child(4), .report-table-track1-svm-repair-ranking td:nth-child(4) { width: 7%; }
    .report-table-track1-svm-repair-ranking th:nth-child(5), .report-table-track1-svm-repair-ranking td:nth-child(5) { width: 6%; }
    .report-table-track1-svm-repair-ranking th:nth-child(6), .report-table-track1-svm-repair-ranking td:nth-child(6) { width: 6%; }
    .report-table-track1-svm-repair-ranking th:nth-child(7), .report-table-track1-svm-repair-ranking td:nth-child(7) { width: 6%; }
    .report-table-track1-svm-repair-ranking th:nth-child(8), .report-table-track1-svm-repair-ranking td:nth-child(8) { width: 11%; }
    .report-table-track1-svm-repair-ranking th:nth-child(9), .report-table-track1-svm-repair-ranking td:nth-child(9) { width: 9%; }
    .report-table-track1-svm-repair-ranking th:nth-child(10), .report-table-track1-svm-repair-ranking td:nth-child(10) { width: 10%; }

    /* Reusable Surface Before/After Summary Profile */
    .report-table-track1-svm-repair-before-after {
      font-size: 7.2pt;
      line-height: 1.18;
    }

    .report-table-track1-svm-repair-before-after th,
    .report-table-track1-svm-repair-before-after td {
      padding: 5px 5px;
    }

    .report-table-track1-svm-repair-before-after th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-svm-repair-before-after th:nth-child(1), .report-table-track1-svm-repair-before-after td:nth-child(1) { width: 38%; }
    .report-table-track1-svm-repair-before-after th:nth-child(2), .report-table-track1-svm-repair-before-after td:nth-child(2) { width: 31%; }
    .report-table-track1-svm-repair-before-after th:nth-child(3), .report-table-track1-svm-repair-before-after td:nth-child(3) { width: 31%; }

    .report-table-track1-bidirectional-mega-benchmark-surface,
    .report-table-track1-bidirectional-mega-reference-archive {
      font-size: 6.9pt;
      line-height: 1.17;
    }

    .report-table-track1-bidirectional-mega-benchmark-surface th,
    .report-table-track1-bidirectional-mega-benchmark-surface td,
    .report-table-track1-bidirectional-mega-reference-archive th,
    .report-table-track1-bidirectional-mega-reference-archive td {
      padding: 4px 4px;
    }

    .report-table-track1-bidirectional-mega-benchmark-surface th,
    .report-table-track1-bidirectional-mega-reference-archive th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(1), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(1) { width: 42%; }
    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(2), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(2) { width: 14%; }
    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(3), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(3) { width: 11%; }
    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(4), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(4) { width: 11%; }
    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(5), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(5) { width: 11%; }
    .report-table-track1-bidirectional-mega-benchmark-surface th:nth-child(6), .report-table-track1-bidirectional-mega-benchmark-surface td:nth-child(6) { width: 11%; }

    .report-table-track1-bidirectional-mega-reference-archive {
      font-size: 6.45pt;
      line-height: 1.14;
    }

    .report-table-track1-bidirectional-mega-reference-archive th,
    .report-table-track1-bidirectional-mega-reference-archive td {
      padding: 3px 4px;
    }

    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(1), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(1) { width: 9%; }
    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(2), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(2) { width: 9%; }
    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(3), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(3) { width: 12%; }
    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(4), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(4) { width: 12%; }
    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(5), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(5) { width: 12%; }
    .report-table-track1-bidirectional-mega-reference-archive th:nth-child(6), .report-table-track1-bidirectional-mega-reference-archive td:nth-child(6) { width: 46%; }

    .report-table-track1-forward-closeout-family-results,
    .report-table-track1-forward-closeout-benchmark-status,
    .report-table-track1-forward-closeout-reference-archive {
      font-size: 6.55pt;
      line-height: 1.14;
    }

    .report-table-track1-forward-closeout-family-results th,
    .report-table-track1-forward-closeout-family-results td,
    .report-table-track1-forward-closeout-benchmark-status th,
    .report-table-track1-forward-closeout-benchmark-status td,
    .report-table-track1-forward-closeout-reference-archive th,
    .report-table-track1-forward-closeout-reference-archive td {
      padding: 3px 4px;
    }

    .report-table-track1-forward-closeout-family-results th,
    .report-table-track1-forward-closeout-benchmark-status th,
    .report-table-track1-forward-closeout-reference-archive th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-forward-closeout-family-results th:nth-child(1), .report-table-track1-forward-closeout-family-results td:nth-child(1) { width: 7%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(2), .report-table-track1-forward-closeout-family-results td:nth-child(2) { width: 37%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(3), .report-table-track1-forward-closeout-family-results td:nth-child(3) { width: 12%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(4), .report-table-track1-forward-closeout-family-results td:nth-child(4) { width: 12%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(5), .report-table-track1-forward-closeout-family-results td:nth-child(5) { width: 12%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(6), .report-table-track1-forward-closeout-family-results td:nth-child(6) { width: 10%; }
    .report-table-track1-forward-closeout-family-results th:nth-child(7), .report-table-track1-forward-closeout-family-results td:nth-child(7) { width: 10%; }

    .report-table-track1-forward-closeout-benchmark-status th:nth-child(1), .report-table-track1-forward-closeout-benchmark-status td:nth-child(1) { width: 52%; }
    .report-table-track1-forward-closeout-benchmark-status th:nth-child(2), .report-table-track1-forward-closeout-benchmark-status td:nth-child(2) { width: 12%; }
    .report-table-track1-forward-closeout-benchmark-status th:nth-child(3), .report-table-track1-forward-closeout-benchmark-status td:nth-child(3) { width: 12%; }
    .report-table-track1-forward-closeout-benchmark-status th:nth-child(4), .report-table-track1-forward-closeout-benchmark-status td:nth-child(4) { width: 12%; }
    .report-table-track1-forward-closeout-benchmark-status th:nth-child(5), .report-table-track1-forward-closeout-benchmark-status td:nth-child(5) { width: 12%; }

    .report-table-track1-forward-closeout-reference-archive th:nth-child(1), .report-table-track1-forward-closeout-reference-archive td:nth-child(1) { width: 8%; }
    .report-table-track1-forward-closeout-reference-archive th:nth-child(2), .report-table-track1-forward-closeout-reference-archive td:nth-child(2) { width: 12%; }
    .report-table-track1-forward-closeout-reference-archive th:nth-child(3), .report-table-track1-forward-closeout-reference-archive td:nth-child(3) { width: 10%; }
    .report-table-track1-forward-closeout-reference-archive th:nth-child(4), .report-table-track1-forward-closeout-reference-archive td:nth-child(4) { width: 70%; }

    .report-table-rcim-retuned-archive-completeness,
    .report-table-rcim-retuned-mean-evaluation-metrics,
    .report-table-rcim-retuned-harmonic-metric {
      font-size: 6.55pt;
      line-height: 1.14;
    }

    .report-table-rcim-retuned-archive-completeness th,
    .report-table-rcim-retuned-archive-completeness td,
    .report-table-rcim-retuned-mean-evaluation-metrics th,
    .report-table-rcim-retuned-mean-evaluation-metrics td,
    .report-table-rcim-retuned-harmonic-metric th,
    .report-table-rcim-retuned-harmonic-metric td {
      padding: 3px 4px;
    }

    .report-table-rcim-retuned-archive-completeness th,
    .report-table-rcim-retuned-mean-evaluation-metrics th,
    .report-table-rcim-retuned-harmonic-metric th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-rcim-retuned-archive-completeness th:nth-child(1), .report-table-rcim-retuned-archive-completeness td:nth-child(1) { width: 10%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(2), .report-table-rcim-retuned-archive-completeness td:nth-child(2) { width: 7%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(3), .report-table-rcim-retuned-archive-completeness td:nth-child(3) { width: 20.33%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(4), .report-table-rcim-retuned-archive-completeness td:nth-child(4) { width: 20.33%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(5), .report-table-rcim-retuned-archive-completeness td:nth-child(5) { width: 20.33%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(6), .report-table-rcim-retuned-archive-completeness td:nth-child(6) { width: 7.33%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(7), .report-table-rcim-retuned-archive-completeness td:nth-child(7) { width: 7.33%; }
    .report-table-rcim-retuned-archive-completeness th:nth-child(8), .report-table-rcim-retuned-archive-completeness td:nth-child(8) { width: 7.33%; }

    .report-table-rcim-retuned-archive-completeness td:nth-child(1) code,
    .report-table-rcim-retuned-archive-completeness td:nth-child(2) code {
      white-space: nowrap;
    }

    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(1), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(1) { width: 12%; }
    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(2), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(2) { width: 12%; }
    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(3), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(3) { width: 19%; }
    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(4), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(4) { width: 19%; }
    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(5), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(5) { width: 19%; }
    .report-table-rcim-retuned-mean-evaluation-metrics th:nth-child(6), .report-table-rcim-retuned-mean-evaluation-metrics td:nth-child(6) { width: 19%; }

    .report-table-rcim-retuned-harmonic-metric th:first-child,
    .report-table-rcim-retuned-harmonic-metric td:first-child {
      width: 10%;
    }

    .report-table-rcim-retuned-harmonic-metric thead code {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.14);
    }

    .report-table-track1-forward-open-cell-repair-family,
    .report-table-track1-forward-open-cell-repair-delta {
      font-size: 6.9pt;
      line-height: 1.17;
    }

    .report-table-track1-forward-open-cell-repair-family th,
    .report-table-track1-forward-open-cell-repair-family td,
    .report-table-track1-forward-open-cell-repair-delta th,
    .report-table-track1-forward-open-cell-repair-delta td {
      padding: 4px 4px;
    }

    .report-table-track1-forward-open-cell-repair-family th,
    .report-table-track1-forward-open-cell-repair-delta th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-track1-forward-open-cell-repair-family th:nth-child(1), .report-table-track1-forward-open-cell-repair-family td:nth-child(1) { width: 9%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(2), .report-table-track1-forward-open-cell-repair-family td:nth-child(2) { width: 40%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(3), .report-table-track1-forward-open-cell-repair-family td:nth-child(3) { width: 11%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(4), .report-table-track1-forward-open-cell-repair-family td:nth-child(4) { width: 9%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(5), .report-table-track1-forward-open-cell-repair-family td:nth-child(5) { width: 11%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(6), .report-table-track1-forward-open-cell-repair-family td:nth-child(6) { width: 7%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(7), .report-table-track1-forward-open-cell-repair-family td:nth-child(7) { width: 7%; }
    .report-table-track1-forward-open-cell-repair-family th:nth-child(8), .report-table-track1-forward-open-cell-repair-family td:nth-child(8) { width: 6%; }

    .report-table-track1-forward-open-cell-repair-delta th:nth-child(1), .report-table-track1-forward-open-cell-repair-delta td:nth-child(1) { width: 43%; }
    .report-table-track1-forward-open-cell-repair-delta th:nth-child(2), .report-table-track1-forward-open-cell-repair-delta td:nth-child(2) { width: 19%; }
    .report-table-track1-forward-open-cell-repair-delta th:nth-child(3), .report-table-track1-forward-open-cell-repair-delta td:nth-child(3) { width: 19%; }
    .report-table-track1-forward-open-cell-repair-delta th:nth-child(4), .report-table-track1-forward-open-cell-repair-delta td:nth-child(4) { width: 19%; }

    .report-table-svr-reference-grid-ranking,
    .report-table-svr-reference-grid-export-surface,
    .report-table-svr-reference-grid-gap-vs-paper {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-svr-reference-grid-ranking th,
    .report-table-svr-reference-grid-ranking td,
    .report-table-svr-reference-grid-export-surface th,
    .report-table-svr-reference-grid-export-surface td,
    .report-table-svr-reference-grid-gap-vs-paper th,
    .report-table-svr-reference-grid-gap-vs-paper td {
      padding: 4px 4px;
    }

    .report-table-svr-reference-grid-ranking th,
    .report-table-svr-reference-grid-export-surface th,
    .report-table-svr-reference-grid-gap-vs-paper th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-svr-reference-grid-ranking th:nth-child(1), .report-table-svr-reference-grid-ranking td:nth-child(1) { width: 5%; }
    .report-table-svr-reference-grid-ranking th:nth-child(2), .report-table-svr-reference-grid-ranking td:nth-child(2) { width: 32%; }
    .report-table-svr-reference-grid-ranking th:nth-child(3), .report-table-svr-reference-grid-ranking td:nth-child(3) { width: 15%; }
    .report-table-svr-reference-grid-ranking th:nth-child(4), .report-table-svr-reference-grid-ranking td:nth-child(4) { width: 9%; }
    .report-table-svr-reference-grid-ranking th:nth-child(5), .report-table-svr-reference-grid-ranking td:nth-child(5) { width: 14%; }
    .report-table-svr-reference-grid-ranking th:nth-child(6), .report-table-svr-reference-grid-ranking td:nth-child(6) { width: 14%; }
    .report-table-svr-reference-grid-ranking th:nth-child(7), .report-table-svr-reference-grid-ranking td:nth-child(7) { width: 11%; }

    .report-table-svr-reference-grid-export-surface th:nth-child(1), .report-table-svr-reference-grid-export-surface td:nth-child(1) { width: 20%; }
    .report-table-svr-reference-grid-export-surface th:nth-child(2), .report-table-svr-reference-grid-export-surface td:nth-child(2) { width: 28%; }
    .report-table-svr-reference-grid-export-surface th:nth-child(3), .report-table-svr-reference-grid-export-surface td:nth-child(3) { width: 24%; }
    .report-table-svr-reference-grid-export-surface th:nth-child(4), .report-table-svr-reference-grid-export-surface td:nth-child(4) { width: 28%; }

    .report-table-svr-reference-grid-gap-vs-paper th:nth-child(1), .report-table-svr-reference-grid-gap-vs-paper td:nth-child(1) { width: 28%; }
    .report-table-svr-reference-grid-gap-vs-paper th:nth-child(2), .report-table-svr-reference-grid-gap-vs-paper td:nth-child(2) { width: 16%; }
    .report-table-svr-reference-grid-gap-vs-paper th:nth-child(3), .report-table-svr-reference-grid-gap-vs-paper td:nth-child(3) { width: 18%; }
    .report-table-svr-reference-grid-gap-vs-paper th:nth-child(4), .report-table-svr-reference-grid-gap-vs-paper td:nth-child(4) { width: 14%; }
    .report-table-svr-reference-grid-gap-vs-paper th:nth-child(5), .report-table-svr-reference-grid-gap-vs-paper td:nth-child(5) { width: 24%; }

    .report-table-decision-matrix {
      font-size: 6.9pt;
      line-height: 1.18;
    }

    .report-table-decision-matrix th,
    .report-table-decision-matrix td {
      padding: 4px 4px;
      text-align: center;
    }

    .report-table-decision-matrix th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-decision-matrix th:nth-child(1), .report-table-decision-matrix td:nth-child(1) { width: 18%; }
    .report-table-decision-matrix th:nth-child(2), .report-table-decision-matrix td:nth-child(2) { width: 13%; }
    .report-table-decision-matrix th:nth-child(3), .report-table-decision-matrix td:nth-child(3) { width: 14%; }
    .report-table-decision-matrix th:nth-child(4), .report-table-decision-matrix td:nth-child(4) { width: 11%; }
    .report-table-decision-matrix th:nth-child(5), .report-table-decision-matrix td:nth-child(5) { width: 14%; }
    .report-table-decision-matrix th:nth-child(6), .report-table-decision-matrix td:nth-child(6) { width: 12%; }
    .report-table-decision-matrix th:nth-child(7), .report-table-decision-matrix td:nth-child(7) { width: 18%; }

    .report-table-comparative-example {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-comparative-example th,
    .report-table-comparative-example td {
      padding: 4px 4px;
      text-align: center;
    }

    .report-table-comparative-example th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.12;
    }

    .report-table-comparative-example th:nth-child(1), .report-table-comparative-example td:nth-child(1) { width: 17%; }
    .report-table-comparative-example th:nth-child(2), .report-table-comparative-example td:nth-child(2) { width: 25%; }
    .report-table-comparative-example th:nth-child(3), .report-table-comparative-example td:nth-child(3) { width: 19%; }
    .report-table-comparative-example th:nth-child(4), .report-table-comparative-example td:nth-child(4) { width: 39%; }

    .report-table-wave1-recovery-test-ranking {
      font-size: 6.95pt;
      line-height: 1.2;
    }

    .report-table-wave1-recovery-test-ranking th,
    .report-table-wave1-recovery-test-ranking td,
    .report-table-wave1-recovery-validation-snapshot th,
    .report-table-wave1-recovery-validation-snapshot td,
    .report-table-wave1-recovery-residual-family th,
    .report-table-wave1-recovery-residual-family td,
    .report-table-wave1-recovery-harmonic-family th,
    .report-table-wave1-recovery-harmonic-family td {
      padding: 4px 4px;
    }

    .report-table-wave1-recovery-test-ranking th,
    .report-table-wave1-recovery-validation-snapshot th,
    .report-table-wave1-recovery-residual-family th,
    .report-table-wave1-recovery-harmonic-family th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-wave1-recovery-test-ranking th:nth-child(1), .report-table-wave1-recovery-test-ranking td:nth-child(1) { width: 7%; }
    .report-table-wave1-recovery-test-ranking th:nth-child(2), .report-table-wave1-recovery-test-ranking td:nth-child(2) { width: 34%; }
    .report-table-wave1-recovery-test-ranking th:nth-child(3), .report-table-wave1-recovery-test-ranking td:nth-child(3) { width: 16%; }
    .report-table-wave1-recovery-test-ranking th:nth-child(4), .report-table-wave1-recovery-test-ranking td:nth-child(4) { width: 10%; }
    .report-table-wave1-recovery-test-ranking th:nth-child(5), .report-table-wave1-recovery-test-ranking td:nth-child(5) { width: 17%; }
    .report-table-wave1-recovery-test-ranking th:nth-child(6), .report-table-wave1-recovery-test-ranking td:nth-child(6) { width: 16%; }

    .report-table-wave1-recovery-validation-snapshot th:nth-child(1), .report-table-wave1-recovery-validation-snapshot td:nth-child(1) { width: 44%; }
    .report-table-wave1-recovery-validation-snapshot th:nth-child(2), .report-table-wave1-recovery-validation-snapshot td:nth-child(2) { width: 26%; }
    .report-table-wave1-recovery-validation-snapshot th:nth-child(3), .report-table-wave1-recovery-validation-snapshot td:nth-child(3) { width: 13%; }
    .report-table-wave1-recovery-validation-snapshot th:nth-child(4), .report-table-wave1-recovery-validation-snapshot td:nth-child(4) { width: 17%; }

    .report-table-wave1-recovery-residual-family th:nth-child(1), .report-table-wave1-recovery-residual-family td:nth-child(1) { width: 32%; }
    .report-table-wave1-recovery-residual-family th:nth-child(2), .report-table-wave1-recovery-residual-family td:nth-child(2) { width: 28%; }
    .report-table-wave1-recovery-residual-family th:nth-child(3), .report-table-wave1-recovery-residual-family td:nth-child(3) { width: 12%; }
    .report-table-wave1-recovery-residual-family th:nth-child(4), .report-table-wave1-recovery-residual-family td:nth-child(4) { width: 14%; }
    .report-table-wave1-recovery-residual-family th:nth-child(5), .report-table-wave1-recovery-residual-family td:nth-child(5) { width: 14%; }

    .report-table-wave1-recovery-harmonic-family th:nth-child(1), .report-table-wave1-recovery-harmonic-family td:nth-child(1) { width: 33%; }
    .report-table-wave1-recovery-harmonic-family th:nth-child(2), .report-table-wave1-recovery-harmonic-family td:nth-child(2) { width: 25%; }
    .report-table-wave1-recovery-harmonic-family th:nth-child(3), .report-table-wave1-recovery-harmonic-family td:nth-child(3) { width: 12%; }
    .report-table-wave1-recovery-harmonic-family th:nth-child(4), .report-table-wave1-recovery-harmonic-family td:nth-child(4) { width: 15%; }
    .report-table-wave1-recovery-harmonic-family th:nth-child(5), .report-table-wave1-recovery-harmonic-family td:nth-child(5) { width: 15%; }

    .report-table-wave1-residual-family-test-ranking,
    .report-table-wave1-residual-family-validation-snapshot,
    .report-table-wave1-residual-family-capacity,
    .report-table-wave1-residual-family-dense-regime,
    .report-table-wave1-residual-family-training-mode {
      font-size: 6.9pt;
      line-height: 1.18;
    }

    .report-table-wave1-residual-family-test-ranking th,
    .report-table-wave1-residual-family-test-ranking td,
    .report-table-wave1-residual-family-validation-snapshot th,
    .report-table-wave1-residual-family-validation-snapshot td,
    .report-table-wave1-residual-family-capacity th,
    .report-table-wave1-residual-family-capacity td,
    .report-table-wave1-residual-family-dense-regime th,
    .report-table-wave1-residual-family-dense-regime td,
    .report-table-wave1-residual-family-training-mode th,
    .report-table-wave1-residual-family-training-mode td {
      padding: 4px 4px;
    }

    .report-table-wave1-residual-family-test-ranking th,
    .report-table-wave1-residual-family-validation-snapshot th,
    .report-table-wave1-residual-family-capacity th,
    .report-table-wave1-residual-family-dense-regime th,
    .report-table-wave1-residual-family-training-mode th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-wave1-residual-family-test-ranking th:nth-child(1), .report-table-wave1-residual-family-test-ranking td:nth-child(1) { width: 5%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(2), .report-table-wave1-residual-family-test-ranking td:nth-child(2) { width: 34%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(3), .report-table-wave1-residual-family-test-ranking td:nth-child(3) { width: 11%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(4), .report-table-wave1-residual-family-test-ranking td:nth-child(4) { width: 9%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(5), .report-table-wave1-residual-family-test-ranking td:nth-child(5) { width: 14%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(6), .report-table-wave1-residual-family-test-ranking td:nth-child(6) { width: 14%; }
    .report-table-wave1-residual-family-test-ranking th:nth-child(7), .report-table-wave1-residual-family-test-ranking td:nth-child(7) { width: 13%; }

    .report-table-wave1-residual-family-validation-snapshot th:nth-child(1), .report-table-wave1-residual-family-validation-snapshot td:nth-child(1) { width: 46%; }
    .report-table-wave1-residual-family-validation-snapshot th:nth-child(2), .report-table-wave1-residual-family-validation-snapshot td:nth-child(2) { width: 13%; }
    .report-table-wave1-residual-family-validation-snapshot th:nth-child(3), .report-table-wave1-residual-family-validation-snapshot td:nth-child(3) { width: 13%; }
    .report-table-wave1-residual-family-validation-snapshot th:nth-child(4), .report-table-wave1-residual-family-validation-snapshot td:nth-child(4) { width: 28%; }

    .report-table-wave1-residual-family-capacity th:nth-child(1), .report-table-wave1-residual-family-capacity td:nth-child(1) { width: 36%; }
    .report-table-wave1-residual-family-capacity th:nth-child(2), .report-table-wave1-residual-family-capacity td:nth-child(2) { width: 36%; }
    .report-table-wave1-residual-family-capacity th:nth-child(3), .report-table-wave1-residual-family-capacity td:nth-child(3) { width: 11%; }
    .report-table-wave1-residual-family-capacity th:nth-child(4), .report-table-wave1-residual-family-capacity td:nth-child(4) { width: 17%; }

    .report-table-wave1-residual-family-dense-regime th:nth-child(1), .report-table-wave1-residual-family-dense-regime td:nth-child(1) { width: 36%; }
    .report-table-wave1-residual-family-dense-regime th:nth-child(2), .report-table-wave1-residual-family-dense-regime td:nth-child(2) { width: 36%; }
    .report-table-wave1-residual-family-dense-regime th:nth-child(3), .report-table-wave1-residual-family-dense-regime td:nth-child(3) { width: 11%; }
    .report-table-wave1-residual-family-dense-regime th:nth-child(4), .report-table-wave1-residual-family-dense-regime td:nth-child(4) { width: 17%; }

    .report-table-wave1-residual-family-training-mode th:nth-child(1), .report-table-wave1-residual-family-training-mode td:nth-child(1) { width: 36%; }
    .report-table-wave1-residual-family-training-mode th:nth-child(2), .report-table-wave1-residual-family-training-mode td:nth-child(2) { width: 36%; }
    .report-table-wave1-residual-family-training-mode th:nth-child(3), .report-table-wave1-residual-family-training-mode td:nth-child(3) { width: 11%; }
    .report-table-wave1-residual-family-training-mode th:nth-child(4), .report-table-wave1-residual-family-training-mode td:nth-child(4) { width: 17%; }

    .report-table-campaign-shared-offline-ranking,
    .report-table-campaign-shared-offline-playback,
    .report-table-campaign-exact-support-ranking,
    .report-table-campaign-exact-support-export,
    .report-table-track1-overnight-completed,
    .report-table-track1-overnight-delta,
    .report-table-track1-overnight-block-winner,
    .report-table-track1-exact-open-cell-ranking,
    .report-table-track1-exact-open-cell-export {
      font-size: 6.9pt;
      line-height: 1.18;
    }

    .report-table-campaign-shared-offline-ranking th,
    .report-table-campaign-shared-offline-ranking td,
    .report-table-campaign-shared-offline-playback th,
    .report-table-campaign-shared-offline-playback td,
    .report-table-campaign-exact-support-ranking th,
    .report-table-campaign-exact-support-ranking td,
    .report-table-campaign-exact-support-export th,
    .report-table-campaign-exact-support-export td,
    .report-table-track1-overnight-completed th,
    .report-table-track1-overnight-completed td,
    .report-table-track1-overnight-delta th,
    .report-table-track1-overnight-delta td,
    .report-table-track1-overnight-block-winner th,
    .report-table-track1-overnight-block-winner td,
    .report-table-track1-exact-open-cell-ranking th,
    .report-table-track1-exact-open-cell-ranking td,
    .report-table-track1-exact-open-cell-export th,
    .report-table-track1-exact-open-cell-export td {
      padding: 4px 4px;
    }

    .report-table-campaign-shared-offline-ranking th,
    .report-table-campaign-shared-offline-playback th,
    .report-table-campaign-exact-support-ranking th,
    .report-table-campaign-exact-support-export th,
    .report-table-track1-overnight-completed th,
    .report-table-track1-overnight-delta th,
    .report-table-track1-overnight-block-winner th,
    .report-table-track1-exact-open-cell-ranking th,
    .report-table-track1-exact-open-cell-export th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-campaign-shared-offline-ranking th:nth-child(1), .report-table-campaign-shared-offline-ranking td:nth-child(1) { width: 6%; }
    .report-table-campaign-shared-offline-ranking th:nth-child(2), .report-table-campaign-shared-offline-ranking td:nth-child(2) { width: 34%; }
    .report-table-campaign-shared-offline-ranking th:nth-child(3), .report-table-campaign-shared-offline-ranking td:nth-child(3) { width: 13%; }
    .report-table-campaign-shared-offline-ranking th:nth-child(4), .report-table-campaign-shared-offline-ranking td:nth-child(4) { width: 13%; }
    .report-table-campaign-shared-offline-ranking th:nth-child(5), .report-table-campaign-shared-offline-ranking td:nth-child(5) { width: 16%; }
    .report-table-campaign-shared-offline-ranking th:nth-child(6), .report-table-campaign-shared-offline-ranking td:nth-child(6) { width: 18%; }

    .report-table-campaign-shared-offline-playback th:nth-child(1), .report-table-campaign-shared-offline-playback td:nth-child(1) { width: 36%; }
    .report-table-campaign-shared-offline-playback th:nth-child(2), .report-table-campaign-shared-offline-playback td:nth-child(2) { width: 13%; }
    .report-table-campaign-shared-offline-playback th:nth-child(3), .report-table-campaign-shared-offline-playback td:nth-child(3) { width: 22%; }
    .report-table-campaign-shared-offline-playback th:nth-child(4), .report-table-campaign-shared-offline-playback td:nth-child(4) { width: 29%; }

    .report-table-campaign-exact-support-ranking th:nth-child(1), .report-table-campaign-exact-support-ranking td:nth-child(1) { width: 8%; }
    .report-table-campaign-exact-support-ranking th:nth-child(2), .report-table-campaign-exact-support-ranking td:nth-child(2) { width: 32%; }
    .report-table-campaign-exact-support-ranking th:nth-child(3), .report-table-campaign-exact-support-ranking td:nth-child(3) { width: 9%; }
    .report-table-campaign-exact-support-ranking th:nth-child(4), .report-table-campaign-exact-support-ranking td:nth-child(4) { width: 7%; }
    .report-table-campaign-exact-support-ranking th:nth-child(5), .report-table-campaign-exact-support-ranking td:nth-child(5) { width: 22%; }
    .report-table-campaign-exact-support-ranking th:nth-child(6), .report-table-campaign-exact-support-ranking td:nth-child(6) { width: 22%; }

    .report-table-campaign-exact-support-export th:nth-child(1), .report-table-campaign-exact-support-export td:nth-child(1) { width: 44%; }
    .report-table-campaign-exact-support-export th:nth-child(2), .report-table-campaign-exact-support-export td:nth-child(2) { width: 22%; }
    .report-table-campaign-exact-support-export th:nth-child(3), .report-table-campaign-exact-support-export td:nth-child(3) { width: 18%; }
    .report-table-campaign-exact-support-export th:nth-child(4), .report-table-campaign-exact-support-export td:nth-child(4) { width: 16%; }

    .report-table-track1-overnight-completed th:nth-child(1), .report-table-track1-overnight-completed td:nth-child(1) { width: 5%; }
    .report-table-track1-overnight-completed th:nth-child(2), .report-table-track1-overnight-completed td:nth-child(2) { width: 41%; }
    .report-table-track1-overnight-completed th:nth-child(3), .report-table-track1-overnight-completed td:nth-child(3) { width: 7%; }
    .report-table-track1-overnight-completed th:nth-child(4), .report-table-track1-overnight-completed td:nth-child(4) { width: 13%; }
    .report-table-track1-overnight-completed th:nth-child(5), .report-table-track1-overnight-completed td:nth-child(5) { width: 17%; }
    .report-table-track1-overnight-completed th:nth-child(6), .report-table-track1-overnight-completed td:nth-child(6) { width: 17%; }

    .report-table-track1-overnight-delta th:nth-child(1), .report-table-track1-overnight-delta td:nth-child(1) { width: 47%; }
    .report-table-track1-overnight-delta th:nth-child(2), .report-table-track1-overnight-delta td:nth-child(2) { width: 17%; }
    .report-table-track1-overnight-delta th:nth-child(3), .report-table-track1-overnight-delta td:nth-child(3) { width: 14%; }
    .report-table-track1-overnight-delta th:nth-child(4), .report-table-track1-overnight-delta td:nth-child(4) { width: 22%; }

    .report-table-track1-overnight-block-winner th:nth-child(1), .report-table-track1-overnight-block-winner td:nth-child(1) { width: 7%; }
    .report-table-track1-overnight-block-winner th:nth-child(2), .report-table-track1-overnight-block-winner td:nth-child(2) { width: 30%; }
    .report-table-track1-overnight-block-winner th:nth-child(3), .report-table-track1-overnight-block-winner td:nth-child(3) { width: 10%; }
    .report-table-track1-overnight-block-winner th:nth-child(4), .report-table-track1-overnight-block-winner td:nth-child(4) { width: 53%; }

    .report-table-track1-exact-open-cell-ranking th:nth-child(1), .report-table-track1-exact-open-cell-ranking td:nth-child(1) { width: 7%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(2), .report-table-track1-exact-open-cell-ranking td:nth-child(2) { width: 31%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(3), .report-table-track1-exact-open-cell-ranking td:nth-child(3) { width: 13%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(4), .report-table-track1-exact-open-cell-ranking td:nth-child(4) { width: 11%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(5), .report-table-track1-exact-open-cell-ranking td:nth-child(5) { width: 12%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(6), .report-table-track1-exact-open-cell-ranking td:nth-child(6) { width: 9%; }
    .report-table-track1-exact-open-cell-ranking th:nth-child(7), .report-table-track1-exact-open-cell-ranking td:nth-child(7) { width: 17%; }

    .report-table-track1-exact-open-cell-export th:nth-child(1), .report-table-track1-exact-open-cell-export td:nth-child(1) { width: 38%; }
    .report-table-track1-exact-open-cell-export th:nth-child(2), .report-table-track1-exact-open-cell-export td:nth-child(2) { width: 8%; }
    .report-table-track1-exact-open-cell-export th:nth-child(3), .report-table-track1-exact-open-cell-export td:nth-child(3) { width: 17%; }
    .report-table-track1-exact-open-cell-export th:nth-child(4), .report-table-track1-exact-open-cell-export td:nth-child(4) { width: 14%; }
    .report-table-track1-exact-open-cell-export th:nth-child(5), .report-table-track1-exact-open-cell-export td:nth-child(5) { width: 15%; }
    .report-table-track1-exact-open-cell-export th:nth-child(6), .report-table-track1-exact-open-cell-export td:nth-child(6) { width: 8%; }

    .report-table-remote-training-validation-completed,
    .report-table-remote-training-validation-failed,
    .report-table-targeted-remote-followup-completed,
    .report-table-targeted-remote-followup-family-bests,
    .report-table-track1-second-iteration-completed,
    .report-table-wide-identifier-ranking,
    .report-table-identifier-metric-summary,
    .report-table-family-metric-ranking,
    .report-table-family-estimator-metric-ranking {
      font-size: 6.95pt;
      line-height: 1.18;
    }

    .report-table-remote-training-validation-completed th,
    .report-table-remote-training-validation-completed td,
    .report-table-remote-training-validation-failed th,
    .report-table-remote-training-validation-failed td,
    .report-table-targeted-remote-followup-completed th,
    .report-table-targeted-remote-followup-completed td,
    .report-table-targeted-remote-followup-family-bests th,
    .report-table-targeted-remote-followup-family-bests td,
    .report-table-track1-second-iteration-completed th,
    .report-table-track1-second-iteration-completed td,
    .report-table-wide-identifier-ranking th,
    .report-table-wide-identifier-ranking td,
    .report-table-identifier-metric-summary th,
    .report-table-identifier-metric-summary td,
    .report-table-family-metric-ranking th,
    .report-table-family-metric-ranking td,
    .report-table-family-estimator-metric-ranking th,
    .report-table-family-estimator-metric-ranking td {
      padding: 4px 4px;
    }

    .report-table-remote-training-validation-completed th,
    .report-table-remote-training-validation-failed th,
    .report-table-targeted-remote-followup-completed th,
    .report-table-targeted-remote-followup-family-bests th,
    .report-table-track1-second-iteration-completed th,
    .report-table-wide-identifier-ranking th,
    .report-table-identifier-metric-summary th,
    .report-table-family-metric-ranking th,
    .report-table-family-estimator-metric-ranking th {
      white-space: normal;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
      line-height: 1.14;
    }

    .report-table-remote-training-validation-completed th:nth-child(1), .report-table-remote-training-validation-completed td:nth-child(1) { width: 5%; }
    .report-table-remote-training-validation-completed th:nth-child(2), .report-table-remote-training-validation-completed td:nth-child(2) { width: 35%; }
    .report-table-remote-training-validation-completed th:nth-child(3), .report-table-remote-training-validation-completed td:nth-child(3) { width: 13%; }
    .report-table-remote-training-validation-completed th:nth-child(4), .report-table-remote-training-validation-completed td:nth-child(4) { width: 9%; }
    .report-table-remote-training-validation-completed th:nth-child(5), .report-table-remote-training-validation-completed td:nth-child(5) { width: 12%; }
    .report-table-remote-training-validation-completed th:nth-child(6), .report-table-remote-training-validation-completed td:nth-child(6) { width: 13%; }
    .report-table-remote-training-validation-completed th:nth-child(7), .report-table-remote-training-validation-completed td:nth-child(7) { width: 13%; }

    .report-table-remote-training-validation-failed th:nth-child(1), .report-table-remote-training-validation-failed td:nth-child(1) { width: 35%; }
    .report-table-remote-training-validation-failed th:nth-child(2), .report-table-remote-training-validation-failed td:nth-child(2) { width: 9%; }
    .report-table-remote-training-validation-failed th:nth-child(3), .report-table-remote-training-validation-failed td:nth-child(3) { width: 9%; }
    .report-table-remote-training-validation-failed th:nth-child(4), .report-table-remote-training-validation-failed td:nth-child(4) { width: 47%; }

    .report-table-targeted-remote-followup-completed th:nth-child(1), .report-table-targeted-remote-followup-completed td:nth-child(1) { width: 5%; }
    .report-table-targeted-remote-followup-completed th:nth-child(2), .report-table-targeted-remote-followup-completed td:nth-child(2) { width: 37%; }
    .report-table-targeted-remote-followup-completed th:nth-child(3), .report-table-targeted-remote-followup-completed td:nth-child(3) { width: 13%; }
    .report-table-targeted-remote-followup-completed th:nth-child(4), .report-table-targeted-remote-followup-completed td:nth-child(4) { width: 9%; }
    .report-table-targeted-remote-followup-completed th:nth-child(5), .report-table-targeted-remote-followup-completed td:nth-child(5) { width: 11%; }
    .report-table-targeted-remote-followup-completed th:nth-child(6), .report-table-targeted-remote-followup-completed td:nth-child(6) { width: 12%; }
    .report-table-targeted-remote-followup-completed th:nth-child(7), .report-table-targeted-remote-followup-completed td:nth-child(7) { width: 13%; }

    .report-table-targeted-remote-followup-family-bests th:nth-child(1), .report-table-targeted-remote-followup-family-bests td:nth-child(1) { width: 22%; }
    .report-table-targeted-remote-followup-family-bests th:nth-child(2), .report-table-targeted-remote-followup-family-bests td:nth-child(2) { width: 48%; }
    .report-table-targeted-remote-followup-family-bests th:nth-child(3), .report-table-targeted-remote-followup-family-bests td:nth-child(3) { width: 10%; }
    .report-table-targeted-remote-followup-family-bests th:nth-child(4), .report-table-targeted-remote-followup-family-bests td:nth-child(4) { width: 20%; }

    .report-table-track1-second-iteration-completed th:nth-child(1), .report-table-track1-second-iteration-completed td:nth-child(1) { width: 5%; }
    .report-table-track1-second-iteration-completed th:nth-child(2), .report-table-track1-second-iteration-completed td:nth-child(2) { width: 32%; }
    .report-table-track1-second-iteration-completed th:nth-child(3), .report-table-track1-second-iteration-completed td:nth-child(3) { width: 11%; }
    .report-table-track1-second-iteration-completed th:nth-child(4), .report-table-track1-second-iteration-completed td:nth-child(4) { width: 16%; }
    .report-table-track1-second-iteration-completed th:nth-child(5), .report-table-track1-second-iteration-completed td:nth-child(5) { width: 11%; }
    .report-table-track1-second-iteration-completed th:nth-child(6), .report-table-track1-second-iteration-completed td:nth-child(6) { width: 11%; }
    .report-table-track1-second-iteration-completed th:nth-child(7), .report-table-track1-second-iteration-completed td:nth-child(7) { width: 14%; }

    .report-table-wide-identifier-ranking th:nth-child(1), .report-table-wide-identifier-ranking td:nth-child(1) { width: 5%; }
    .report-table-wide-identifier-ranking th:nth-child(2), .report-table-wide-identifier-ranking td:nth-child(2) { width: 35%; }
    .report-table-wide-identifier-ranking th:nth-child(3), .report-table-wide-identifier-ranking td:nth-child(3) { width: 15%; }
    .report-table-wide-identifier-ranking th:nth-child(4), .report-table-wide-identifier-ranking td:nth-child(4) { width: 11%; }
    .report-table-wide-identifier-ranking th:nth-child(5), .report-table-wide-identifier-ranking td:nth-child(5) { width: 17%; }
    .report-table-wide-identifier-ranking th:nth-child(6), .report-table-wide-identifier-ranking td:nth-child(6) { width: 17%; }

    .report-table-identifier-metric-summary th:nth-child(1), .report-table-identifier-metric-summary td:nth-child(1) { width: 44%; }
    .report-table-identifier-metric-summary th:nth-child(2), .report-table-identifier-metric-summary td:nth-child(2) { width: 22%; }
    .report-table-identifier-metric-summary th:nth-child(3), .report-table-identifier-metric-summary td:nth-child(3) { width: 14%; }
    .report-table-identifier-metric-summary th:nth-child(4), .report-table-identifier-metric-summary td:nth-child(4) { width: 10%; }
    .report-table-identifier-metric-summary th:nth-child(5), .report-table-identifier-metric-summary td:nth-child(5) { width: 10%; }

    .report-table-family-metric-ranking th:nth-child(1), .report-table-family-metric-ranking td:nth-child(1) { width: 6%; }
    .report-table-family-metric-ranking th:nth-child(2), .report-table-family-metric-ranking td:nth-child(2) { width: 12%; }
    .report-table-family-metric-ranking th:nth-child(3), .report-table-family-metric-ranking td:nth-child(3) { width: 30%; }
    .report-table-family-metric-ranking th:nth-child(4), .report-table-family-metric-ranking td:nth-child(4) { width: 26%; }
    .report-table-family-metric-ranking th:nth-child(5), .report-table-family-metric-ranking td:nth-child(5) { width: 26%; }

    .report-table-family-estimator-metric-ranking th:nth-child(1), .report-table-family-estimator-metric-ranking td:nth-child(1) { width: 6%; }
    .report-table-family-estimator-metric-ranking th:nth-child(2), .report-table-family-estimator-metric-ranking td:nth-child(2) { width: 10%; }
    .report-table-family-estimator-metric-ranking th:nth-child(3), .report-table-family-estimator-metric-ranking td:nth-child(3) { width: 24%; }
    .report-table-family-estimator-metric-ranking th:nth-child(4), .report-table-family-estimator-metric-ranking td:nth-child(4) { width: 20%; }
    .report-table-family-estimator-metric-ranking th:nth-child(5), .report-table-family-estimator-metric-ranking td:nth-child(5) { width: 20%; }
    .report-table-family-estimator-metric-ranking th:nth-child(6), .report-table-family-estimator-metric-ranking td:nth-child(6) { width: 20%; }

    .report-table-targeted-remote-followup-completed .metric-unit,
    .report-table-targeted-remote-followup-family-bests .metric-unit,
    .report-table-track1-second-iteration-completed .metric-unit,
    .report-table-track1-partial-closeout-family .metric-unit,
    .report-table-track1-partial-closeout-aggregate .metric-unit,
    .report-table-track1-final-closeout-family .metric-unit,
    .report-table-track1-final-closeout-aggregate .metric-unit,
    .report-table-track1-open-cell-closeout-family .metric-unit,
    .report-table-wide-identifier-ranking .metric-unit,
    .report-table-identifier-metric-summary .metric-unit,
    .report-table-family-metric-ranking .metric-unit,
    .report-table-family-estimator-metric-ranking .metric-unit,
    .report-table-campaign-shared-offline-ranking .metric-unit,
    .report-table-campaign-shared-offline-playback .metric-unit,
    .report-table-campaign-exact-support-ranking .metric-unit,
    .report-table-campaign-exact-support-export .metric-unit,
    .report-table-track1-overnight-completed .metric-unit,
    .report-table-track1-overnight-delta .metric-unit,
    .report-table-track1-overnight-block-winner .metric-unit,
    .report-table-track1-exact-open-cell-ranking .metric-unit,
    .report-table-track1-exact-open-cell-export .metric-unit,
    .report-table-track2-best-model-collage .metric-unit,
    .report-table-track2-official-track2fbis-result .metric-unit,
    .report-table-repository-status-scalar-winner .metric-unit,
    .report-table-repository-status-hpo-leader .metric-unit,
    .report-table-repository-status-harmonic-results .metric-unit,
    .report-table-repository-status-temporal-winner .metric-unit,
    .report-table-repository-status-temporal-surfaces .metric-unit,
    .report-table-repository-status-wave2b-scalar .metric-unit,
    .report-table-repository-status-wave2b-track2 .metric-unit,
    .report-table-repository-status-wave2c-scalar .metric-unit,
    .report-table-repository-status-wave2c-track2 .metric-unit,
    .report-table-repository-status-wave2c-dense .metric-unit,
    .report-table-repository-status-track2-current .metric-unit,
    .report-table-repository-status-harmonic-bank .metric-unit {
      display: block;
    }

    .report-table code {
      background: rgba(173, 213, 247, 0.18);
      font-size: 7.1pt;
    }

    .semantic-wrap-code {
      word-break: normal;
      overflow-wrap: normal;
      hyphens: none;
    }

    .split-table-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      width: 100%;
      max-width: 100%;
    }

    .table-wrap-split {
      break-inside: avoid-page;
    }

    .table-caption {
      padding: 8px 10px 7px 10px;
      border-bottom: 1px solid #ADD5F7;
      background: #F7FBFF;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 8.5pt;
      color: #16193B;
    }

    .report-table-summary {
      font-size: 8pt;
    }

    .report-table-summary th:nth-child(1), .report-table-summary td:nth-child(1) { width: 20%; }
    .report-table-summary th:nth-child(2), .report-table-summary td:nth-child(2) { width: 22%; }
    .report-table-summary th:nth-child(3), .report-table-summary td:nth-child(3) { width: 58%; }

    .report-table-technical-data,
    .report-table-technical-schedule {
      font-size: 7.55pt;
    }

    .report-table-technical-data th,
    .report-table-technical-data td,
    .report-table-technical-schedule th,
    .report-table-technical-schedule td {
      padding: 5px 4px;
    }

    .report-table-summary th,
    .report-table-summary td,
    .report-table-technical-data th,
    .report-table-technical-data td,
    .report-table-technical-schedule th,
    .report-table-technical-schedule td {
      text-align: center;
    }

    .report-table-technical-data th:nth-child(1), .report-table-technical-data td:nth-child(1) { width: 16%; }
    .report-table-technical-data th:nth-child(2), .report-table-technical-data td:nth-child(2) { width: 17%; }
    .report-table-technical-data th:nth-child(3), .report-table-technical-data td:nth-child(3) { width: 17%; }
    .report-table-technical-data th:nth-child(4), .report-table-technical-data td:nth-child(4) { width: 18%; }
    .report-table-technical-data th:nth-child(5), .report-table-technical-data td:nth-child(5) { width: 16%; }
    .report-table-technical-data th:nth-child(6), .report-table-technical-data td:nth-child(6) { width: 16%; }

    .report-table-technical-schedule th:nth-child(1), .report-table-technical-schedule td:nth-child(1) { width: 18%; }
    .report-table-technical-schedule th:nth-child(2), .report-table-technical-schedule td:nth-child(2) { width: 34%; }
    .report-table-technical-schedule th:nth-child(3), .report-table-technical-schedule td:nth-child(3) { width: 24%; }
    .report-table-technical-schedule th:nth-child(4), .report-table-technical-schedule td:nth-child(4) { width: 24%; }

    .report-table-technical-data td,
    .report-table-technical-schedule td,
    .report-table-summary td {
      vertical-align: middle;
    }

    .align-right {
      text-align: right;
    }

    .align-center {
      text-align: center;
    }

    .align-left {
      text-align: left;
    }

    .section-final-recommendation {
      border-color: #7FB2F0;
    }

    .section-comparing-trial-baseline-and-workstation-variants .table-wrap {
      margin-bottom: 12px;
    }
"""

def build_argument_parser() -> argparse.ArgumentParser:

    """Build the exporter command-line parser.

    Returns:
        argparse.ArgumentParser: Parser configured for Markdown input, HTML
        preview handling, PDF output, report labels, and browser resolution.
    """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description="Generate a styled HTML and PDF report from a Markdown source.")

    # Configure Report Paths
    argument_parser.add_argument("--input-markdown-path", required=True, help="Path to the Markdown source report.")
    argument_parser.add_argument("--output-html-path", default="", help="Optional path to a generated styled HTML preview file.")
    argument_parser.add_argument("--output-pdf-path", required=True, help="Path to the generated styled PDF file.")

    # Configure Report Labels
    argument_parser.add_argument("--report-subtitle", default=DEFAULT_REPORT_SUBTITLE, help="Subtitle displayed below the report title.")
    argument_parser.add_argument("--report-category", default=DEFAULT_REPORT_CATEGORY, help="Category badge displayed in the cover block.")

    # Configure Export Environment
    argument_parser.add_argument("--chrome-executable-path", default="", help="Optional explicit Chrome or Edge executable path.")
    argument_parser.add_argument("--keep-html", action="store_true", help="Keep the generated HTML file after PDF export.")

    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser

def remove_temporary_directory(directory_path: Path) -> None:

    """ Remove Temporary Directory """

    # Skip Missing Directory
    if not directory_path.exists():
        return

    # Retry Directory Cleanup
    for cleanup_attempt_index in range(CLEANUP_RETRY_COUNT):
        try:
            shutil.rmtree(directory_path)
            return
        except OSError:
            if cleanup_attempt_index == CLEANUP_RETRY_COUNT - 1:
                print(f"[WARN] Temporary directory cleanup skipped | {directory_path}")
                return
            time.sleep(CLEANUP_RETRY_DELAY_SECONDS)

def remove_temporary_file(file_path: Path) -> None:

    """ Remove Temporary File """

    # Skip Missing File
    if not file_path.exists():
        return

    # Retry File Cleanup
    for cleanup_attempt_index in range(CLEANUP_RETRY_COUNT):
        try:
            file_path.unlink()
            return
        except OSError:
            if cleanup_attempt_index == CLEANUP_RETRY_COUNT - 1:
                print(f"[WARN] Temporary file cleanup skipped | {file_path}")
                return
            time.sleep(CLEANUP_RETRY_DELAY_SECONDS)

def create_workspace_temp_directory(parent_directory_path: Path, prefix: str) -> Path:

    """ Create Workspace Temp Directory """

    # Create Temporary Directory
    parent_directory_path.mkdir(parents=True, exist_ok=True)
    directory_name = f"{prefix}_{time.time_ns()}"
    temporary_directory_path = (parent_directory_path / directory_name).resolve()
    temporary_directory_path.mkdir(parents=True, exist_ok=True)
    return temporary_directory_path

def resolve_report_path(path_value: str | Path, allow_absolute: bool = True) -> Path:

    """Resolve a report path against the repository root."""

    return repository_path_support.resolve_repository_path(
        path_value,
        PROJECT_PATH,
        allow_absolute=allow_absolute,
    )


def resolve_output_html_path(output_html_path: str, output_pdf_path: Path, keep_html: bool) -> tuple[Path, bool]:

    """ Resolve Output HTML Path """

    # Use Explicit Preview Path
    if output_html_path:
        return resolve_report_path(output_html_path), False

    # Always Use The Stable Sibling Preview Path
    persistent_output_html_path = output_pdf_path.with_name(f"{output_pdf_path.stem}_preview.html")
    return persistent_output_html_path, not keep_html

def detect_browser_executable(explicit_path: str, platform_name: str) -> Path:

    """Resolve the browser executable used for headless PDF export.

    Args:
        explicit_path: Optional browser path provided by the caller.

    Returns:
        Path: Resolved Chrome or Edge executable path.

    Raises:
        FileNotFoundError: If no valid explicit path is provided and no known
            local Chrome or Edge installation can be detected.
    """

    # Resolve Explicit Browser Path
    if explicit_path:

        explicit_browser_path = Path(explicit_path).expanduser()

        if not explicit_browser_path.exists():
            raise FileNotFoundError(f"Browser executable not found: {explicit_browser_path}")

        return explicit_browser_path

    # Probe Known Browser Installations
    if platform_name == repository_path_support.LINUX_PLATFORM_NAME:
        candidate_browser_path_list = LINUX_BROWSER_EXECUTABLE_CANDIDATE_PATHS
    else:
        candidate_browser_path_list = WINDOWS_BROWSER_EXECUTABLE_CANDIDATE_PATHS

    for candidate_browser_path in candidate_browser_path_list:
        if candidate_browser_path.exists():
            return candidate_browser_path

    raise FileNotFoundError(
        "Could not detect a local Chrome/Edge executable for headless PDF export. "
        "Pass --chrome-executable-path explicitly for this host."
    )

def slugify(raw_text: str) -> str:

    """ Slugify Heading Text """

    # Normalize Heading Slug
    normalized_text = re.sub(r"[^a-zA-Z0-9]+", "-", raw_text.strip().lower())

    return normalized_text.strip("-") or "section"

def parse_markdown_image(markdown_text: str) -> tuple[str, str] | None:

    """ Parse Markdown Image """

    # Validate Markdown Text
    image_match = re.fullmatch(r"!\[(.*?)\]\((.+?)\)", markdown_text.strip())
    if image_match is None:
        return None

    # Extract Markdown Image Fields
    image_alt_text = image_match.group(1).strip()
    image_path = image_match.group(2).strip()
    return image_alt_text, image_path

def render_markdown_image(markdown_text: str, markdown_directory: Path) -> str:

    """ Render Markdown Image """

    # Validate Markdown Text
    parsed_image = parse_markdown_image(markdown_text)
    if parsed_image is None:
        raise ValueError(f"Markdown text is not an image block | {markdown_text}")

    # Resolve Markdown Image Path
    image_alt_text, image_path = parsed_image
    resolved_image_path = (markdown_directory / image_path).resolve()
    assert resolved_image_path.exists(), f"Markdown image path does not exist | {resolved_image_path}"

    # Get Markdown Image HTML
    image_uri = resolved_image_path.as_uri()
    escaped_alt_text = html.escape(image_alt_text)
    caption_html = f'<figcaption class="report-figure-caption">{escaped_alt_text}</figcaption>' if escaped_alt_text else ""

    return (
        '<figure class="report-figure">'
        f'<img src="{html.escape(image_uri)}" alt="{escaped_alt_text}" />'
        f"{caption_html}"
        "</figure>"
    )

def convert_inline_markup(raw_text: str) -> str:

    """ Convert Inline Markup """

    # Split Inline Code Segments
    code_split_tokens = re.split(r"(`[^`]+`)", raw_text)
    html_tokens: list[str] = []

    for code_split_token in code_split_tokens:
        if not code_split_token:
            continue

        # Render Inline Code Token
        if code_split_token.startswith("`") and code_split_token.endswith("`"):
            html_tokens.append(f"<code>{html.escape(code_split_token[1:-1])}</code>")
            continue

        # Render Plain Text Token
        escaped_token = html.escape(code_split_token)
        escaped_token = re.sub(
            r"\*\*(.+?)\*\*",
            lambda match_object: f"<strong>{match_object.group(1)}</strong>",
            escaped_token,
        )

        # Append Escaped Text Token
        html_tokens.append(escaped_token)

    return "".join(html_tokens)

def group_identifier_tokens(raw_identifier_text: str) -> list[str]:

    """ Group Identifier Tokens """

    grouped_tokens: list[str] = []
    identifier_tokens = raw_identifier_text.split("_")
    token_index = 0

    while token_index < len(identifier_tokens):

        # Resolve Compound Token
        if (
            token_index + 1 < len(identifier_tokens)
            and (identifier_tokens[token_index], identifier_tokens[token_index + 1]) in SEMANTIC_IDENTIFIER_TOKEN_PAIRS
        ):
            grouped_tokens.append(f"{identifier_tokens[token_index]}_{identifier_tokens[token_index + 1]}")
            token_index += 2
            continue

        grouped_tokens.append(identifier_tokens[token_index])
        token_index += 1

    return grouped_tokens

def render_inline_code(raw_code_text: str, use_semantic_identifier_wrap: bool = False) -> str:

    """ Render Inline Code """

    # Render Default Inline Code
    if not use_semantic_identifier_wrap or "_" not in raw_code_text:
        return f"<code>{html.escape(raw_code_text)}</code>"

    # Group Identifier Tokens
    grouped_tokens = group_identifier_tokens(raw_code_text)
    grouped_tokens_html = html.escape(grouped_tokens[0]) if grouped_tokens else ""

    # Render Grouped Identifier Tokens
    for grouped_token in grouped_tokens[1:]:
        grouped_tokens_html += f"_<wbr>{html.escape(grouped_token)}"

    return f'<code class="semantic-wrap-code">{grouped_tokens_html}</code>'

def convert_inline_markup_with_semantic_identifier_wrap(raw_text: str) -> str:

    """ Convert Inline Markup With Semantic Identifier Wrap """

    # Split Inline Code Segments
    code_split_tokens = re.split(r"(`[^`]+`)", raw_text)
    html_tokens: list[str] = []

    for code_split_token in code_split_tokens:
        if not code_split_token:
            continue

        # Render Inline Code Token
        if code_split_token.startswith("`") and code_split_token.endswith("`"):
            html_tokens.append(render_inline_code(code_split_token[1:-1], use_semantic_identifier_wrap=True))
            continue

        # Render Plain Text Token
        escaped_token = html.escape(code_split_token)
        escaped_token = re.sub(
            r"\*\*(.+?)\*\*",
            lambda match_object: f"<strong>{match_object.group(1)}</strong>",
            escaped_token,
        )
        html_tokens.append(escaped_token)

    return "".join(html_tokens)

def split_table_row(markdown_row: str) -> list[str]:

    """ Split Table Row """

    # Trim Table Row Borders
    normalized_row = markdown_row.strip().strip("|")

    # Split Row Into Cells And Trim Cell Padding
    return [cell.strip() for cell in normalized_row.split("|")]

def extract_table_alignments(separator_row: str) -> list[str]:

    """ Extract Table Alignments """

    alignments: list[str] = []

    for separator_cell in split_table_row(separator_row):

        # Normalize Cell Marker
        stripped_separator_cell = separator_cell.strip()

        # Resolve Cell Alignment
        if stripped_separator_cell.startswith(":") and stripped_separator_cell.endswith(":"): alignments.append(ALIGN_CENTER)
        elif stripped_separator_cell.endswith(":"): alignments.append(ALIGN_RIGHT)
        else: alignments.append(ALIGN_LEFT)

    return alignments

def is_heading(markdown_line: str) -> bool:

    """ Check Heading Line """

    # Match Heading Prefix
    return markdown_line.startswith("#")

def is_table_row(markdown_line: str) -> bool:

    """ Check Table Row """

    # Match Markdown Table Prefix
    return markdown_line.strip().startswith("|")

def is_html_comment_line(markdown_line: str) -> bool:

    """ Report Whether The Markdown Line Is A Standalone HTML Comment """

    stripped_line = markdown_line.strip()
    return stripped_line.startswith("<!--") and stripped_line.endswith("-->")

def is_list_item(markdown_line: str) -> bool:

    """ Check List Item """

    # Match Bullet Or Numbered Item
    return bool(re.match(r"^(\s*)([-*]|\d+\.)\s+.+$", markdown_line))

def get_list_item_metadata(markdown_line: str) -> tuple[int, str, str]:

    """ Get List Item Metadata """

    # Match List Item Structure
    match_object = re.match(r"^(\s*)([-*]|\d+\.)\s+(.+)$", markdown_line)

    # Validate Match Result
    if match_object is None: raise ValueError(f"Line is not a list item: {markdown_line}")

    # Parse List Item Fields
    indentation_width = len(match_object.group(1).replace("\t", "    "))
    bullet_token = match_object.group(2)
    item_content = match_object.group(3).strip()
    list_tag = "ol" if bullet_token.endswith(".") else "ul"

    return indentation_width, list_tag, item_content

def collect_table_lines(markdown_lines: Sequence[str], start_index: int) -> tuple[list[str], int]:

    """ Collect Table Lines """

    table_lines: list[str] = []
    current_index = start_index

    # Collect Consecutive Table Rows
    while current_index < len(markdown_lines) and is_table_row(markdown_lines[current_index]):
        table_lines.append(markdown_lines[current_index])
        current_index += 1

    return table_lines, current_index

def is_mean_component_metric_header(header_cell: str) -> bool:

    """ Report Whether The Header Is A Mean-Component Metric """

    return header_cell.startswith("Mean Component ")

def normalize_common_metric_header_cell(header_cell: str) -> str | None:

    """ Normalize Common Long Metric Header Cells """

    # Wrap Repository Mean-Component Metrics
    if is_mean_component_metric_header(header_cell):
        metric_suffix = html.escape(header_cell.removeprefix("Mean Component ").strip())
        return f"Mean Component<span class=\"metric-unit\">{metric_suffix}</span>"

    # Wrap Common Val/Test Metric Headers With Units
    unit_metric_match = re.fullmatch(r"((?:Test|Val) (?:MAE|RMSE)) (\[[^\]]+\])", header_cell)
    if unit_metric_match is not None:
        metric_label, metric_unit = unit_metric_match.groups()
        return f"{html.escape(metric_label)}<span class=\"metric-unit\">{html.escape(metric_unit)}</span>"

    # Wrap Generic Metric Headers With Compact Units
    generic_unit_metric_match = re.fullmatch(r"(.+?) (\[[^\]]+\])", header_cell)
    if generic_unit_metric_match is not None:
        metric_label, metric_unit = generic_unit_metric_match.groups()
        return f"{html.escape(metric_label)}<span class=\"metric-unit\">{html.escape(metric_unit)}</span>"

    return None

def is_wide_identifier_ranking_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches A Wide-Identifier Ranking Table """

    normalized_header_cells = tuple(header_cells)
    return (
        len(normalized_header_cells) == 6
        and normalized_header_cells[0] == "Rank"
        and normalized_header_cells[1] == "Config"
        and any(is_mean_component_metric_header(header_cell) for header_cell in normalized_header_cells)
    )

def is_identifier_metric_summary_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches An Identifier-Metric Summary Table """

    normalized_header_cells = tuple(header_cells)
    return (
        len(normalized_header_cells) == 5
        and normalized_header_cells[0] == "Config"
        and any(is_mean_component_metric_header(header_cell) for header_cell in normalized_header_cells)
        and any(header_cell in {"ONNX Exported", "Failed Exports", "Surrogates"} for header_cell in normalized_header_cells)
    )

def is_family_metric_ranking_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches A Family-Metric Ranking Table """

    normalized_header_cells = tuple(header_cells)
    return (
        len(normalized_header_cells) == 5
        and normalized_header_cells[0] == "Rank"
        and normalized_header_cells[1] == "Family"
        and all(is_mean_component_metric_header(header_cell) for header_cell in normalized_header_cells[2:])
    )

def is_family_estimator_metric_ranking_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches A Family-Estimator Metric Ranking Table """

    normalized_header_cells = tuple(header_cells)
    return (
        len(normalized_header_cells) == 6
        and normalized_header_cells[0] == "Rank"
        and normalized_header_cells[1] == "Family"
        and normalized_header_cells[2] == "Estimator"
        and all(is_mean_component_metric_header(header_cell) for header_cell in normalized_header_cells[3:])
    )

def is_campaign_cell_repair_ranking_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches A Cell-Repair Ranking Table """

    return tuple(header_cells) == CAMPAIGN_CELL_REPAIR_RANKING_TABLE_HEADER_CELLS

def is_surface_before_after_summary_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches A Surface Before/After Summary Table """

    return tuple(header_cells) == SURFACE_BEFORE_AFTER_SUMMARY_TABLE_HEADER_CELLS

def is_family_best_retry_outcome_table(header_cells: Sequence[str]) -> bool:

    """Report whether the table matches the shared family-best retry outcome profile."""

    return tuple(header_cells) == FAMILY_BEST_RETRY_OUTCOME_TABLE_HEADER_CELLS

def is_surface_delta_summary_table(header_cells: Sequence[str]) -> bool:

    """Report whether the table matches the shared surface delta summary profile."""

    return tuple(header_cells) == SURFACE_DELTA_SUMMARY_TABLE_HEADER_CELLS

def is_svr_reference_grid_ranking_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches The SVR Reference-Grid Ranking Table """

    return tuple(header_cells) == SVR_REFERENCE_GRID_RANKING_TABLE_HEADER_CELLS

def is_svr_reference_grid_export_surface_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches The SVR Reference-Grid Export Surface Table """

    return tuple(header_cells) == SVR_REFERENCE_GRID_EXPORT_SURFACE_TABLE_HEADER_CELLS

def is_svr_reference_grid_gap_vs_paper_table(header_cells: Sequence[str]) -> bool:

    """ Report Whether The Header Set Matches The SVR Reference-Grid Gap-Vs-Paper Table """

    return tuple(header_cells) == SVR_REFERENCE_GRID_GAP_VS_PAPER_TABLE_HEADER_CELLS

def is_track1_forward_closeout_family_results_table(header_cells: Sequence[str]) -> bool:

    """Report whether the table matches the Track 1 forward closeout family result profile."""

    return tuple(header_cells) == TRACK1_FORWARD_CLOSEOUT_FAMILY_RESULTS_TABLE_HEADER_CELLS

def is_track1_forward_closeout_benchmark_status_table(header_cells: Sequence[str]) -> bool:

    """Report whether the table matches the Track 1 forward closeout benchmark status profile."""

    return tuple(header_cells) == TRACK1_FORWARD_CLOSEOUT_BENCHMARK_STATUS_TABLE_HEADER_CELLS

def is_track1_forward_closeout_reference_archive_table(header_cells: Sequence[str]) -> bool:

    """Report whether the table matches the Track 1 forward closeout reference archive profile."""

    return tuple(header_cells) == TRACK1_FORWARD_CLOSEOUT_REFERENCE_ARCHIVE_TABLE_HEADER_CELLS

def normalize_report_specific_header_cell(header_cell: str, table_class_name: str) -> str:

    """ Normalize Report-Specific Header Cell Content """

    wrapped_common_metric_header = normalize_common_metric_header_cell(header_cell)

    if table_class_name in {
        HISTORICAL_REFERENCE_TABLE_CLASS_NAME,
        PHASE_RESULTS_TABLE_CLASS_NAME,
        TARGETED_REMOTE_FOLLOWUP_COMPLETED_TABLE_CLASS_NAME,
        TARGETED_REMOTE_FOLLOWUP_FAMILY_BESTS_TABLE_CLASS_NAME,
        TRACK1_SECOND_ITERATION_COMPLETED_TABLE_CLASS_NAME,
        WIDE_IDENTIFIER_RANKING_TABLE_CLASS_NAME,
        IDENTIFIER_METRIC_SUMMARY_TABLE_CLASS_NAME,
        FAMILY_METRIC_RANKING_TABLE_CLASS_NAME,
        FAMILY_ESTIMATOR_METRIC_RANKING_TABLE_CLASS_NAME,
        CAMPAIGN_SHARED_OFFLINE_RANKING_TABLE_CLASS_NAME,
        CAMPAIGN_SHARED_OFFLINE_PLAYBACK_TABLE_CLASS_NAME,
        CAMPAIGN_EXACT_SUPPORT_RANKING_TABLE_CLASS_NAME,
        CAMPAIGN_EXACT_SUPPORT_EXPORT_TABLE_CLASS_NAME,
        TRACK1_OVERNIGHT_COMPLETED_TABLE_CLASS_NAME,
        TRACK1_OVERNIGHT_DELTA_TABLE_CLASS_NAME,
        TRACK1_OVERNIGHT_BLOCK_WINNER_TABLE_CLASS_NAME,
        TRACK2G_BRANCH_RESULTS_TABLE_CLASS_NAME,
        TRACK2G_LOSS_LEADERBOARD_TABLE_CLASS_NAME,
        TRACK2G_BASELINE_COMPARISON_TABLE_CLASS_NAME,
        TRACK2G_REGISTRY_EFFECTS_TABLE_CLASS_NAME,
        TRACK2_BEST_MODEL_COLLAGE_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_SCALAR_WINNER_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_HPO_LEADER_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_HARMONIC_RESULTS_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_TEMPORAL_WINNER_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_TEMPORAL_SURFACES_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_WAVE2B_SCALAR_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_WAVE2B_TRACK2_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_WAVE2C_SCALAR_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_WAVE2C_TRACK2_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_WAVE2C_DENSE_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_TRACK2_CURRENT_TABLE_CLASS_NAME,
        REPOSITORY_STATUS_HARMONIC_BANK_TABLE_CLASS_NAME,
    } and wrapped_common_metric_header is not None:
        return wrapped_common_metric_header

    if table_class_name == TRACK2_ORIGINAL_ONNX_METRICS_TABLE_CLASS_NAME:
        if header_cell == "MAE [deg]":
            return "MAE<br><span class=\"metric-unit\">[deg]</span>"
        if header_cell == "RMSE [deg]":
            return "RMSE<br><span class=\"metric-unit\">[deg]</span>"
        if header_cell == "Mean Error [%]":
            return "Mean Error<br><span class=\"metric-unit\">[%]</span>"
        if header_cell == "P95 Error [%]":
            return "P95 Error<br><span class=\"metric-unit\">[%]</span>"

    if (
        table_class_name == TRACK1_OVERNIGHT_DELTA_TABLE_CLASS_NAME
        and header_cell.startswith("Delta Vs `")
        and header_cell.endswith("` Baseline")
    ):
        baseline_value = header_cell[len("Delta Vs `") : -len("` Baseline")]
        return f"Delta Vs<span class=\"metric-unit\"><code>{html.escape(baseline_value)}</code> Baseline</span>"

    if table_class_name == TRACK1_EXACT_OPEN_CELL_RANKING_TABLE_CLASS_NAME:
        if header_cell == "Harmonics Open":
            return "Harmonics<span class=\"metric-unit\">Open</span>"
        if header_cell == "Harmonics Partial":
            return "Harmonics<span class=\"metric-unit\">Partial</span>"
        if header_cell == "Met Cells":
            return "Met<span class=\"metric-unit\">Cells</span>"

    if table_class_name == TRACK1_EXACT_OPEN_CELL_EXPORT_TABLE_CLASS_NAME:
        if header_cell == "Failed":
            return "Fail."

    if table_class_name == TRACK1_OPEN_CELL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME:
        if header_cell == "Closure Score":
            return "Closure<br><span class=\"metric-unit\">Score</span>"

    if table_class_name == RCIM_RETUNED_ARCHIVE_COMPLETENESS_TABLE_CLASS_NAME:
        if header_cell == "Exported Errors":
            return "Exported<br>Errors"

    if table_class_name == TRACK2_OFFICIAL_STATIC_BASELINE_TABLE_CLASS_NAME:
        if header_cell == "Current Strongest Candidate":
            return "Current Strongest<br>Candidate"

    if table_class_name == TRACK2_OFFICIAL_CAMPAIGN_LEDGER_TABLE_CLASS_NAME:
        if header_cell == "Campaign or Update":
            return "Campaign or<br>Update"
        if header_cell == "Candidate Scope":
            return "Candidate<br>Scope"

    if table_class_name in {
        TRACK2G_BRANCH_RESULTS_TABLE_CLASS_NAME,
        TRACK2G_LOSS_LEADERBOARD_TABLE_CLASS_NAME,
        TRACK2G_BASELINE_COMPARISON_TABLE_CLASS_NAME,
        TRACK2G_REGISTRY_EFFECTS_TABLE_CLASS_NAME,
    }:
        if header_cell == "Loss Profile":
            return "Loss<br>Profile"
        if header_cell == "Track 2G MAE":
            return "Track 2G<br><span class=\"metric-unit\">MAE</span>"
        if table_class_name == TRACK2G_REGISTRY_EFFECTS_TABLE_CLASS_NAME and header_cell == "Best Run":
            return "Best Run"

    if table_class_name in {
        TRACK2_CURVE_FIRST_RANKING_TABLE_CLASS_NAME,
        TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_TABLE_CLASS_NAME,
        TRACK2_SURFACE_LEADER_TABLE_CLASS_NAME,
        TRACK2_MEAN_CENTERED_TOP_TABLE_CLASS_NAME,
        TRACK2_MEAN_CENTERED_GROUP_TABLE_CLASS_NAME,
        TRACK2D_MEAN_OFFSET_TABLE_CLASS_NAME,
        TRACK2E_OFFSET_FEASIBILITY_TABLE_CLASS_NAME,
    }:
        if header_cell == "Raw MAE":
            return "Raw<br><span class=\"metric-unit\">MAE</span>"
        if header_cell == "Corr. MAE":
            return "Corr.<br><span class=\"metric-unit\">MAE</span>"
        if header_cell == "Centered MAE":
            return "Centered<br><span class=\"metric-unit\">MAE</span>"
        if header_cell == "Mean MPE [%]":
            return "Mean<br><span class=\"metric-unit\">MPE [%]</span>"
        if header_cell == "P95 MPE [%]":
            return "P95<br><span class=\"metric-unit\">MPE [%]</span>"
        if header_cell == "Worst MPE [%]":
            return "Worst<br><span class=\"metric-unit\">MPE [%]</span>"
        if header_cell == "Mean Harmonic Amp Error [%]":
            return "Harm. Amp<br><span class=\"metric-unit\">Err. [%]</span>"
        if header_cell == "Mean Harmonic Phase Error [deg]":
            return "Harm. Phase<br><span class=\"metric-unit\">Err. [deg]</span>"
        if header_cell == "Mean P2P Error [%]":
            return "P2P<br><span class=\"metric-unit\">Err. [%]</span>"
        if header_cell == "Diagnostic Score":
            return "Diag.<br><span class=\"metric-unit\">Score</span>"
        if header_cell == "Gain [%]":
            return "Gain<br><span class=\"metric-unit\">[%]</span>"
        if header_cell == "Explain [%]":
            return "Explain<br><span class=\"metric-unit\">[%]</span>"
        if header_cell == "Mean Curve MAE [deg]":
            return "Mean Curve<br><span class=\"metric-unit\">MAE [deg]</span>"

    if table_class_name == TRACK1_FORWARD_CLOSEOUT_FAMILY_RESULTS_TABLE_CLASS_NAME:
        if header_cell == "Exported ONNX":
            return "Exported<br>ONNX"
        if header_cell == "Exported PKL":
            return "Exported<br>PKL"

    if header_cell == "Paper Cell":
        return "Paper<span class=\"metric-unit\">Cell</span>"
    if header_cell == "Amplitude Run":
        return "Amplitude<span class=\"metric-unit\">Run</span>"
    if header_cell == "Phase Run":
        return "Phase<span class=\"metric-unit\">Run</span>"
    if (
        table_class_name == REPOSITORY_STATUS_HARMONIC_RESULTS_TABLE_CLASS_NAME
        and header_cell == "Best Run"
    ):
        return "Best Run"

    if header_cell == "Best Run":
        return "Best<span class=\"metric-unit\">Run</span>"
    if header_cell == "Open Cells":
        return "Open<span class=\"metric-unit\">Cells</span>"
    if header_cell == "Closure Score":
        return "Closure<span class=\"metric-unit\">Score</span>"
    if header_cell == "Best Closure Score":
        return "Best Closure<span class=\"metric-unit\">Score</span>"

    return convert_inline_markup(header_cell)

def is_identifier_column_header(header_cell: str) -> bool:

    """ Report Whether The Header Represents An Identifier-Style Column """

    return header_cell in {
        "Config",
        "Best Config",
        "Best Run After This Campaign",
        "Candidate",
        "Leader",
        "Run",
        "Amplitude Run",
        "Phase Run",
        "Best Run",
    }

def render_table_header_cells(header_cells: Sequence[str], alignments: Sequence[str], table_class_name: str = GENERIC_TABLE_CLASS_NAME) -> str:

    """ Render Table Header Cells """

    header_html_tokens: list[str] = []

    for header_index, header_cell in enumerate(header_cells):

        # Resolve Header Alignment
        alignment_class = alignments[header_index] if header_index < len(alignments) else ALIGN_LEFT
        normalized_header_cell = normalize_report_specific_header_cell(header_cell, table_class_name)
        header_html_tokens.append(f'<th class="{alignment_class}">{normalized_header_cell}</th>')

    return "".join(header_html_tokens)

def render_table_body_rows(body_rows: Sequence[str], header_cells: Sequence[str], alignments: Sequence[str]) -> str:

    """ Render Table Body Rows """

    body_html_tokens: list[str] = []

    for body_row in body_rows:

        body_html_tokens.append("<tr>")

        for cell_index, body_cell in enumerate(split_table_row(body_row)):

            # Resolve Cell Alignment
            alignment_class = alignments[cell_index] if cell_index < len(alignments) else ALIGN_LEFT
            use_identifier_wrap = (
                cell_index < len(header_cells)
                and is_identifier_column_header(header_cells[cell_index])
            )
            body_html_tokens.append(
                f'<td class="{alignment_class}">{convert_inline_markup_with_semantic_identifier_wrap(body_cell) if use_identifier_wrap else convert_inline_markup(body_cell)}</td>'
            )

        body_html_tokens.append("</tr>")

    return "".join(body_html_tokens)

def render_split_table_body_rows(body_rows: Sequence[str], alignments: Sequence[str], selected_indexes: Sequence[int]) -> str:

    """ Render Split Table Body Rows """

    body_html_tokens: list[str] = []

    for body_row in body_rows:

        # Split Row Cells
        row_cells = split_table_row(body_row)
        body_html_tokens.append("<tr>")

        for output_index, source_index in enumerate(selected_indexes):

            # Resolve Cell Alignment
            body_cell = row_cells[source_index]
            alignment_class = alignments[output_index] if output_index < len(alignments) else ALIGN_LEFT
            body_html_tokens.append(
                f'<td class="{alignment_class}">{convert_inline_markup_with_semantic_identifier_wrap(body_cell) if output_index == 0 else convert_inline_markup(body_cell)}</td>'
            )

        body_html_tokens.append("</tr>")

    return "".join(body_html_tokens)

def render_column_subset_table_body_rows(
    body_rows: Sequence[str],
    selected_header_cells: Sequence[str],
    selected_alignments: Sequence[str],
    selected_indexes: Sequence[int],
) -> str:

    """Render table rows after selecting a PDF-readable subset of columns."""

    body_html_tokens: list[str] = []

    for body_row in body_rows:

        # Split Row Cells
        row_cells = split_table_row(body_row)
        body_html_tokens.append("<tr>")

        for output_index, source_index in enumerate(selected_indexes):

            # Resolve Cell Rendering
            body_cell = row_cells[source_index]
            alignment_class = selected_alignments[output_index] if output_index < len(selected_alignments) else ALIGN_LEFT
            use_identifier_wrap = (
                output_index < len(selected_header_cells)
                and is_identifier_column_header(selected_header_cells[output_index])
            )
            body_html_tokens.append(
                f'<td class="{alignment_class}">{convert_inline_markup_with_semantic_identifier_wrap(body_cell) if use_identifier_wrap else convert_inline_markup(body_cell)}</td>'
            )

        body_html_tokens.append("</tr>")

    return "".join(body_html_tokens)

def render_column_subset_table(
    header_cells: Sequence[str],
    alignments: Sequence[str],
    body_rows: Sequence[str],
    selected_indexes: Sequence[int],
    table_class_name: str,
) -> str:

    """Render a PDF-readable subset of a wide analytical table."""

    # Select Columns
    selected_header_cells = tuple(header_cells[index] for index in selected_indexes)
    selected_alignments = tuple(alignments[index] if index < len(alignments) else ALIGN_LEFT for index in selected_indexes)

    # Render Table Sections
    header_html = render_table_header_cells(selected_header_cells, selected_alignments, table_class_name)
    body_html = render_column_subset_table_body_rows(
        body_rows,
        selected_header_cells,
        selected_alignments,
        selected_indexes,
    )

    return (
        '<div class="table-wrap">'
        f'<table class="{table_class_name}">'
        "<thead><tr>"
        f"{header_html}"
        "</tr></thead>"
        "<tbody>"
        f"{body_html}"
        "</tbody></table></div>"
    )

def render_standard_table(
    header_cells: Sequence[str],
    alignments: Sequence[str],
    body_rows: Sequence[str],
    table_class_name: str = GENERIC_TABLE_CLASS_NAME,
) -> str:

    """ Render Standard Table """

    # Render Table Sections
    header_html = render_table_header_cells(header_cells, alignments, table_class_name)
    body_html = render_table_body_rows(body_rows, header_cells, alignments)

    return (
        '<div class="table-wrap">'
        f'<table class="{table_class_name}">'
        "<thead><tr>"
        f"{header_html}"
        "</tr></thead>"
        "<tbody>"
        f"{body_html}"
        "</tbody></table></div>"
    )

def render_split_configuration_table(
    table_title: str,
    header_cells: Sequence[str],
    alignments: Sequence[str],
    body_rows: Sequence[str],
    selected_indexes: Sequence[int],
    table_class_name: str,
) -> str:

    """ Render Split Configuration Table """

    # Render Selected Table Sections
    header_html = render_table_header_cells(header_cells, alignments, table_class_name)
    body_html = render_split_table_body_rows(body_rows, alignments, selected_indexes)

    return (
        '<div class="table-wrap table-wrap-split">'
        f'<div class="table-caption">{html.escape(table_title)}</div>'
        f'<table class="{table_class_name}">'
        "<thead><tr>"
        f"{header_html}"
        "</tr></thead>"
        "<tbody>"
        f"{body_html}"
        "</tbody></table></div>"
    )

def render_configuration_split_tables(body_rows: Sequence[str]) -> str:

    """ Render Configuration Split Tables """

    # Render Campaign Summary
    campaign_summary_html = render_split_configuration_table(
        "Campaign Summary",
        CONFIGURATION_TABLE_HEADER_CELLS[:3],
        CAMPAIGN_SUMMARY_ALIGNMENTS,
        body_rows,
        (0, 1, 2),
        "report-table report-table-summary",
    )

    # Render Data Pipeline Settings
    data_pipeline_html = render_split_configuration_table(
        "Data Pipeline Settings",
        (CONFIGURATION_TABLE_HEADER_CELLS[0], *CONFIGURATION_TABLE_HEADER_CELLS[3:8]),
        DATA_PIPELINE_ALIGNMENTS,
        body_rows,
        (0, 3, 4, 5, 6, 7),
        "report-table report-table-technical-data",
    )

    # Render Model And Schedule Settings
    model_and_schedule_html = render_split_configuration_table(
        "Model And Schedule Settings",
        (CONFIGURATION_TABLE_HEADER_CELLS[0], *CONFIGURATION_TABLE_HEADER_CELLS[8:11]),
        MODEL_AND_SCHEDULE_ALIGNMENTS,
        body_rows,
        (0, 8, 9, 10),
        "report-table report-table-technical-schedule",
    )

    return (
        '<div class="split-table-grid">'
        f"{campaign_summary_html}"
        f"{data_pipeline_html}"
        f"{model_and_schedule_html}"
        "</div>"
    )


def is_repository_status_wave_track_report(report_stem: str) -> bool:

    """ Return Whether A Report Should Use The Repository Status Table Profile """

    normalized_report_stem = report_stem.lower().replace("_", " ").replace("-", " ")
    required_terms = ("repository", "status", "wave", "track")
    return all(required_term in normalized_report_stem for required_term in required_terms)


def resolve_standard_table_class_name(
    header_cells: Sequence[str],
    report_stem: str,
    current_section_slug: str,
    current_subsection_slug: str,
) -> str:

    """ Resolve Standard Table Class Name """

    normalized_header_cells = tuple(header_cells)

    if normalized_header_cells == TRACK2_COMPONENT_HARMONIC_SUMMARY_TABLE_HEADER_CELLS:
        return TRACK2_COMPONENT_HARMONIC_SUMMARY_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_COMPONENT_TEMPERATURE_DIRECTION_TABLE_HEADER_CELLS:
        return TRACK2_COMPONENT_TEMPERATURE_DIRECTION_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_COMPONENT_H0_EXTREME_TABLE_HEADER_CELLS:
        return TRACK2_COMPONENT_H0_EXTREME_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_H0_SURFACE_SUMMARY_TABLE_HEADER_CELLS:
        return TRACK2D_H0_SURFACE_SUMMARY_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_H0_LARGEST_OFFSET_TABLE_HEADER_CELLS:
        return TRACK2D_H0_CANDIDATE_METRIC_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_H0_OVERLAP_TABLE_HEADER_CELLS:
        return TRACK2D_H0_CANDIDATE_OVERLAP_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_H0_ABSOLUTE_CORRELATION_TABLE_HEADER_CELLS:
        return TRACK2D_H0_CANDIDATE_METRIC_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_H0_QUADRANT_TABLE_HEADER_CELLS:
        return TRACK2D_H0_QUADRANT_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_PREDICTED_MEAN_CANDIDATE_TABLE_HEADER_CELLS:
        return TRACK2D_PREDICTED_MEAN_CANDIDATE_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2D_PREDICTED_MEAN_DIRECTION_TABLE_HEADER_CELLS:
        return TRACK2D_PREDICTED_MEAN_DIRECTION_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_ORIGINAL_ONNX_TARGET_TABLE_HEADER_CELLS:
        return TRACK2_ORIGINAL_ONNX_TARGET_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_ORIGINAL_ONNX_METRICS_TABLE_HEADER_CELLS:
        return TRACK2_ORIGINAL_ONNX_METRICS_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_ORIGINAL_ONNX_CURVES_TABLE_HEADER_CELLS:
        return TRACK2_ORIGINAL_ONNX_CURVES_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_FORWARD_REFERENCE_PAIRWISE_TABLE_HEADER_CELLS:
        return TRACK2_FORWARD_REFERENCE_PAIRWISE_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_FORWARD_REFERENCE_COLLAGE_METRICS_TABLE_HEADER_CELLS:
        return TRACK2_FORWARD_REFERENCE_COLLAGE_METRICS_TABLE_CLASS_NAME

    if normalized_header_cells == TRACK2_FORWARD_REFERENCE_COLLAGE_DELTAS_TABLE_HEADER_CELLS:
        return TRACK2_FORWARD_REFERENCE_COLLAGE_DELTAS_TABLE_CLASS_NAME

    # Resolve Historical Comparison Table
    if normalized_header_cells == HISTORICAL_REFERENCE_TABLE_HEADER_CELLS:
        return HISTORICAL_REFERENCE_TABLE_CLASS_NAME

    # Resolve Phase Result Table
    if normalized_header_cells == PHASE_RESULTS_TABLE_HEADER_CELLS:
        return PHASE_RESULTS_TABLE_CLASS_NAME

    # Resolve Ranking Table
    if normalized_header_cells in RANKING_TABLE_HEADER_CELL_GROUPS:
        return RANKING_RESULTS_TABLE_CLASS_NAME

    # Resolve Reusable Ranking/Metric Table Profiles
    if is_wide_identifier_ranking_table(normalized_header_cells):
        return WIDE_IDENTIFIER_RANKING_TABLE_CLASS_NAME

    if is_identifier_metric_summary_table(normalized_header_cells):
        return IDENTIFIER_METRIC_SUMMARY_TABLE_CLASS_NAME

    if is_family_metric_ranking_table(normalized_header_cells):
        return FAMILY_METRIC_RANKING_TABLE_CLASS_NAME

    if is_family_estimator_metric_ranking_table(normalized_header_cells):
        return FAMILY_ESTIMATOR_METRIC_RANKING_TABLE_CLASS_NAME

    # Resolve Reusable Cell-Repair / Before-After Table Profiles
    if is_campaign_cell_repair_ranking_table(normalized_header_cells):
        return CAMPAIGN_CELL_REPAIR_RANKING_TABLE_CLASS_NAME

    if is_surface_before_after_summary_table(normalized_header_cells):
        return SURFACE_BEFORE_AFTER_SUMMARY_TABLE_CLASS_NAME

    if is_family_best_retry_outcome_table(normalized_header_cells):
        return FAMILY_BEST_RETRY_OUTCOME_TABLE_CLASS_NAME

    if is_surface_delta_summary_table(normalized_header_cells):
        return SURFACE_DELTA_SUMMARY_TABLE_CLASS_NAME

    # Resolve SVR Reference-Grid Campaign Table Profiles
    if is_svr_reference_grid_ranking_table(normalized_header_cells):
        return SVR_REFERENCE_GRID_RANKING_TABLE_CLASS_NAME

    if is_svr_reference_grid_export_surface_table(normalized_header_cells):
        return SVR_REFERENCE_GRID_EXPORT_SURFACE_TABLE_CLASS_NAME

    if is_svr_reference_grid_gap_vs_paper_table(normalized_header_cells):
        return SVR_REFERENCE_GRID_GAP_VS_PAPER_TABLE_CLASS_NAME

    # Resolve Track 1 Forward Closeout Table Profiles
    if (
        current_section_slug == "family-results"
        and is_track1_forward_closeout_family_results_table(normalized_header_cells)
    ):
        return TRACK1_FORWARD_CLOSEOUT_FAMILY_RESULTS_TABLE_CLASS_NAME

    if (
        current_section_slug == "benchmark-status"
        and is_track1_forward_closeout_benchmark_status_table(normalized_header_cells)
    ):
        return TRACK1_FORWARD_CLOSEOUT_BENCHMARK_STATUS_TABLE_CLASS_NAME

    if (
        current_section_slug == "reference-archive-refresh"
        and is_track1_forward_closeout_reference_archive_table(normalized_header_cells)
    ):
        return TRACK1_FORWARD_CLOSEOUT_REFERENCE_ARCHIVE_TABLE_CLASS_NAME

    # Resolve Decision Matrix Table
    if normalized_header_cells == DECISION_MATRIX_TABLE_HEADER_CELLS:
        return DECISION_MATRIX_TABLE_CLASS_NAME

    # Resolve Comparative Example Table
    if normalized_header_cells == COMPARATIVE_EXAMPLE_TABLE_HEADER_CELLS:
        return COMPARATIVE_EXAMPLE_TABLE_CLASS_NAME

    # Resolve Wave 1 High-Order Harmonic Tracking Closeout Table Profiles
    if report_stem == "2026-05-20-12-25-49_wave1_high_order_harmonic_tracking_campaign_results_report":

        if (
            current_section_slug == "campaign-artifacts"
            and normalized_header_cells == ("Artifact", "Path")
        ):
            return WAVE1_HIGH_ORDER_ARTIFACT_TABLE_CLASS_NAME

        if (
            current_section_slug in {"execution-summary", "campaign-winner"}
            and normalized_header_cells == ("Field", "Value")
        ):
            return WAVE1_HIGH_ORDER_KEY_VALUE_TABLE_CLASS_NAME

        if (
            current_section_slug == "leaderboard"
            and normalized_header_cells == ("Rank", "Run", "Scope", "Harmonics", "Test MAE", "Test RMSE")
        ):
            return WAVE1_HIGH_ORDER_LEADERBOARD_TABLE_CLASS_NAME

        if (
            current_section_slug == "registry-effects"
            and normalized_header_cells == ("Registry Scope", "New Relevant Entry", "Test MAE", "Interpretation")
            ):
            return WAVE1_HIGH_ORDER_REGISTRY_TABLE_CLASS_NAME

    # Resolve Wave 1 Periodic MLP Explicit Harmonic Tracking Closeout Table Profiles
    if report_stem == "2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report":

        if (
            current_section_slug == "campaign-artifacts"
            and normalized_header_cells == ("Artifact", "Path")
        ):
            return WAVE1_HIGH_ORDER_ARTIFACT_TABLE_CLASS_NAME

        if (
            current_section_slug in {"execution-summary", "campaign-winner"}
            and normalized_header_cells == ("Field", "Value")
        ):
            return WAVE1_HIGH_ORDER_KEY_VALUE_TABLE_CLASS_NAME

        if (
            current_section_slug == "leaderboard"
            and normalized_header_cells == ("Rank", "Run", "Scope", "Harmonics", "Test MAE", "Test RMSE", "Params")
        ):
            return WAVE1_PERIODIC_MLP_LEADERBOARD_TABLE_CLASS_NAME

        if (
            current_section_slug == "registry-effects"
            and normalized_header_cells == ("Registry Scope", "Current Family Best", "Test MAE", "Interpretation")
        ):
            return WAVE1_PERIODIC_MLP_REGISTRY_TABLE_CLASS_NAME

    # Resolve Wave 2 Temporal Model Entry Closeout Table Profiles
    if report_stem in {
        "2026-05-24-12-36-49_wave2_temporal_model_entry_campaign_results_report",
        "2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report",
    }:

        if (
            current_section_slug == "campaign-artifacts"
            and normalized_header_cells == ("Artifact", "Path")
        ):
            return WAVE2_TEMPORAL_ARTIFACT_TABLE_CLASS_NAME

        if (
            current_section_slug == "leaderboard"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Test MAE", "Test RMSE", "Val MAE", "Params")
        ):
            return WAVE2_TEMPORAL_LEADERBOARD_TABLE_CLASS_NAME

        if (
            current_section_slug == "registry-effects"
            and normalized_header_cells == ("Registry Scope", "Current Family Best", "Test MAE", "Interpretation")
        ):
            return WAVE2_TEMPORAL_REGISTRY_TABLE_CLASS_NAME

    # Resolve Default Campaign Closeout Table Profiles
    if (
        current_section_slug == "campaign-artifacts"
        and normalized_header_cells == ("Artifact", "Path")
    ):
        return WAVE2_TEMPORAL_ARTIFACT_TABLE_CLASS_NAME

    if (
        current_section_slug == "leaderboard"
        and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Test MAE", "Test RMSE", "Val MAE", "Params")
    ):
        return WAVE2_TEMPORAL_LEADERBOARD_TABLE_CLASS_NAME

    if (
        current_section_slug == "registry-effects"
        and normalized_header_cells == ("Registry Scope", "Current Family Best", "Test MAE", "Interpretation")
    ):
        return WAVE2_TEMPORAL_REGISTRY_TABLE_CLASS_NAME

    # Resolve Track 2F Closeout Table Profiles
    if report_stem in {
        "2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report",
        "2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report",
    }:

        if (
            current_section_slug == "directional-branch-results"
            and normalized_header_cells
            == ("Surface", "Role", "Run", "Family", "Test MAE", "Test RMSE", "Val MAE", "Params")
        ):
            return TRACK2F_BRANCH_RESULTS_TABLE_CLASS_NAME

        if (
            current_section_slug == "scalar-leaderboard"
            and normalized_header_cells
            == ("Rank", "Surface", "Run", "Family", "Test MAE", "Test RMSE", "Val MAE", "Params")
        ):
            return TRACK2F_SCALAR_LEADERBOARD_TABLE_CLASS_NAME

    # Resolve Track 2G Curve-Aware Closeout Table Profiles
    if report_stem == "2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report":

        if (
            current_section_slug == "directional-branch-results"
            and normalized_header_cells
            == ("Surface", "Candidate", "Loss Profile", "Test MAE", "Test RMSE", "Val MAE")
        ):
            return TRACK2G_BRANCH_RESULTS_TABLE_CLASS_NAME

        if (
            current_section_slug == "loss-profile-leaderboard"
            and normalized_header_cells
            == ("Rank", "Surface", "Candidate", "Loss Profile", "Test MAE", "Test RMSE", "Val MAE")
        ):
            return TRACK2G_LOSS_LEADERBOARD_TABLE_CLASS_NAME

        if (
            current_section_slug == "baseline-comparison"
            and normalized_header_cells
            == ("Surface", "Track 2G Best", "Track 2G MAE", "Track 2F-Bis Ref.", "Ref. MAE", "Delta")
        ):
            return TRACK2G_BASELINE_COMPARISON_TABLE_CLASS_NAME

        if (
            current_section_slug == "registry-effects"
            and normalized_header_cells == ("Registry Scope", "Best Run", "Test MAE")
        ):
            return TRACK2G_REGISTRY_EFFECTS_TABLE_CLASS_NAME

    # Resolve Track 2 Best-Model Collage Summary Tables
    if (
        report_stem in {"track2_best_model_collage_report", "track2_multi_model_curve_comparison_report"}
        and normalized_header_cells
        == ("Candidate", "Source", "Surface", "Curve MAE [deg]", "Curve RMSE [deg]", "Mean Error")
    ):
        return TRACK2_BEST_MODEL_COLLAGE_TABLE_CLASS_NAME

    # Resolve Track 2 Official Verification Report Tables
    if report_stem == "track2_official_model_verification_report":

        if normalized_header_cells == ("Surface", "Training or Archive Scope", "Evaluation Scope"):
            return TRACK2_OFFICIAL_VERIFICATION_RULE_TABLE_CLASS_NAME

        if normalized_header_cells == ("Pipeline or Source", "Track 2 Role", "Current Status", "Verification Artifact"):
            return TRACK2_OFFICIAL_PIPELINE_COVERAGE_TABLE_CLASS_NAME

        if normalized_header_cells == ("Surface", "Branch", "Candidate", "Registry"):
            return TRACK2_OFFICIAL_CANDIDATE_REFRESH_TABLE_CLASS_NAME

        if (
            current_subsection_slug == "best-composite-references"
            and normalized_header_cells == ("Candidate", "Source", "Direction", "MAE [deg]", "RMSE [deg]", "Mean [%]", "P95 [%]")
        ):
            return TRACK2_OFFICIAL_BEST_COMPOSITE_TABLE_CLASS_NAME

        if (
            current_subsection_slug == "repository-owned-static-baselines"
            and normalized_header_cells == ("Direction", "Current Strongest Candidate", "MAE [deg]", "RMSE [deg]", "Mean [%]", "P95 [%]")
        ):
            return TRACK2_OFFICIAL_STATIC_BASELINE_TABLE_CLASS_NAME

        if normalized_header_cells == ("Date", "Campaign or Update", "Candidate Scope", "Matrix Status", "Visual Status", "Decision"):
            return TRACK2_OFFICIAL_CAMPAIGN_LEDGER_TABLE_CLASS_NAME

        if normalized_header_cells == ("Surface", "Candidate", "Branch", "MAE [deg]", "RMSE [deg]", "Mean [%]"):
            return TRACK2_OFFICIAL_TRACK2FBIS_RESULT_TABLE_CLASS_NAME

    # Resolve Wave 1 Recovery Table Profiles
    if report_stem == "2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report":

        if (
            current_section_slug == "recovery-campaign-ranking"
            and current_subsection_slug == "test-side-ranking"
            and normalized_header_cells == ("Rank", "Config", "Family", "Runtime", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return WAVE1_RECOVERY_TEST_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "recovery-campaign-ranking"
            and current_subsection_slug == "validation-side-snapshot"
            and normalized_header_cells == ("Config", "Parameters", "Val MAE [deg]", "Val RMSE [deg]")
        ):
            return WAVE1_RECOVERY_VALIDATION_SNAPSHOT_TABLE_CLASS_NAME

        if (
            current_section_slug == "family-level-interpretation"
            and current_subsection_slug == "residual-harmonic-mlp"
            and normalized_header_cells == ("Config", "Training Mode", "Val MAE [deg]", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return WAVE1_RECOVERY_RESIDUAL_TABLE_CLASS_NAME

        if (
            current_section_slug == "family-level-interpretation"
            and current_subsection_slug == "harmonic-regression"
            and normalized_header_cells == ("Config", "Harmonic Setup", "Val MAE [deg]", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return WAVE1_RECOVERY_HARMONIC_TABLE_CLASS_NAME

    # Resolve Wave 1 Residual Family Table Profiles
    if report_stem == "2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "test-side-ranking"
            and normalized_header_cells == ("Rank", "Config", "Parameters", "Runtime", "Test MAE [deg]", "Test RMSE [deg]", "Val MAE [deg]")
        ):
            return WAVE1_RESIDUAL_FAMILY_TEST_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "validation-side-snapshot"
            and normalized_header_cells == ("Config", "Val MAE [deg]", "Test MAE [deg]", "Generalization Gap [deg]")
        ):
            return WAVE1_RESIDUAL_FAMILY_VALIDATION_SNAPSHOT_TABLE_CLASS_NAME

        if (
            current_section_slug == "interpretation-by-search-axis"
            and current_subsection_slug == "1-deeper-residual-capacity-was-the-highest-value-change"
            and normalized_header_cells == ("Config", "Capacity Pattern", "Val MAE [deg]", "Test MAE [deg]")
        ):
            return WAVE1_RESIDUAL_FAMILY_CAPACITY_TABLE_CLASS_NAME

        if (
            current_section_slug == "interpretation-by-search-axis"
            and current_subsection_slug == "4-dense-training-regimes-did-not-produce-the-best-generalization"
            and normalized_header_cells == ("Config", "Data Regime", "Val MAE [deg]", "Test MAE [deg]")
        ):
            return WAVE1_RESIDUAL_FAMILY_DENSE_REGIME_TABLE_CLASS_NAME

        if (
            current_section_slug == "interpretation-by-search-axis"
            and current_subsection_slug == "5-joint-optimization-still-beats-the-frozen-structured-base"
            and normalized_header_cells == ("Config", "Training Mode", "Val MAE [deg]", "Test MAE [deg]")
        ):
            return WAVE1_RESIDUAL_FAMILY_TRAINING_MODE_TABLE_CLASS_NAME

    # Resolve Remote Training Validation Table Profiles
    if report_stem == "2026-04-03-22-35-07_remote_training_validation_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Config", "Family", "Runtime", "Test MAE [deg]", "Test RMSE [deg]", "Val MAE [deg]")
        ):
            return REMOTE_TRAINING_VALIDATION_COMPLETED_TABLE_CLASS_NAME

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "failed-run"
            and normalized_header_cells == ("Config", "Family", "Runtime", "Outcome")
        ):
            return REMOTE_TRAINING_VALIDATION_FAILED_TABLE_CLASS_NAME

    # Resolve Targeted Remote Follow-Up Table Profiles
    if report_stem == "2026-04-04-13-14-48_targeted_remote_followup_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Config", "Family", "Runtime", "Test MAE [deg]", "Test RMSE [deg]", "Val MAE [deg]")
        ):
            return TARGETED_REMOTE_FOLLOWUP_COMPLETED_TABLE_CLASS_NAME

        if (
            current_section_slug == "family-registry-impact"
            and current_subsection_slug == "updated-family-bests"
            and normalized_header_cells == ("Family", "Best Run After This Campaign", "Test MAE [deg]", "Status")
        ):
            return TARGETED_REMOTE_FOLLOWUP_FAMILY_BESTS_TABLE_CLASS_NAME

    # Resolve Track 1 Second Iteration Campaign Table Profiles
    if report_stem == "2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Config", "Harmonic Set", "Feature Set", "Test % Error", "Oracle Test %", "Test MAE [deg]")
        ):
            return TRACK1_SECOND_ITERATION_COMPLETED_TABLE_CLASS_NAME

    # Resolve Exact-Paper Faithful Reproduction Campaign Table Profiles
    if report_stem == "2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report":

        if (
            current_section_slug == "comparable-offline-ranking"
            and normalized_header_cells == ("Rank", "Config", "Target A", "Test MPE [%]", "Curve MAE [deg]", "Curve RMSE [deg]")
        ):
            return CAMPAIGN_SHARED_OFFLINE_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "comparable-offline-ranking"
            and normalized_header_cells == ("Config", "Oracle MPE [%]", "Robot TE RMS [deg]", "Cycloidal TE RMS [deg]")
        ):
            return CAMPAIGN_SHARED_OFFLINE_PLAYBACK_TABLE_CLASS_NAME

        if (
            current_section_slug == "exact-paper-support-runs"
            and normalized_header_cells == ("Rank", "Config", "ONNX Export", "Winner", "Mean Component MAPE [%]", "Mean Component MAE")
        ):
            return CAMPAIGN_EXACT_SUPPORT_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "exact-paper-support-runs"
            and normalized_header_cells == ("Config", "Mean Component RMSE", "ONNX Exported", "Failed Exports")
        ):
            return CAMPAIGN_EXACT_SUPPORT_EXPORT_TABLE_CLASS_NAME

    # Resolve Track 1 Overnight Gap-Closure Campaign Table Profiles
    if report_stem in {
        "2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report",
        "2026-04-13-16-16-23_track1_extended_overnight_campaign_results_report",
    }:

        if (
            current_section_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Config", "Block", "Test MPE [%]", "Curve MAE [deg]", "Curve RMSE [deg]")
        ):
            return TRACK1_OVERNIGHT_COMPLETED_TABLE_CLASS_NAME

        if (
            current_section_slug == "ranked-completed-runs"
            and normalized_header_cells in {
                ("Config", "Validation MPE [%]", "Oracle Test MPE [%]", "Delta Vs `8.877%` Baseline"),
                ("Config", "Validation MPE [%]", "Oracle Test MPE [%]", "Delta Vs `8.774%` Baseline"),
            }
        ):
            return TRACK1_OVERNIGHT_DELTA_TABLE_CLASS_NAME

        if (
            current_section_slug == "best-run-per-block"
            and normalized_header_cells == ("Block", "Best Config", "Test MPE [%]", "Interpretation")
        ):
            return TRACK1_OVERNIGHT_BLOCK_WINNER_TABLE_CLASS_NAME

    # Resolve Track 1 Exact Open-Cell Repair Campaign Table Profiles
    if report_stem == "2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Config", "Family Scope", "Harmonics Open", "Harmonics Partial", "Met Cells", "Regressions")
        ):
            return TRACK1_EXACT_OPEN_CELL_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Config", "Winner", "Mean Component MAPE [%]", "Export Mode", "Exported", "Failed")
        ):
            return TRACK1_EXACT_OPEN_CELL_EXPORT_TABLE_CLASS_NAME

    # Resolve Track 1 Full-Matrix Family Reproduction Campaign Table Profiles
    if report_stem == "2026-04-14-14-35-29_track1_full_matrix_family_reproduction_campaign_results_report":

        if (
            current_section_slug == "campaign-ranking"
            and current_subsection_slug == "ranked-completed-runs"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Targets", "Met", "Near", "Open", "Closure Score")
        ):
            return TRACK1_FULL_MATRIX_RANKING_TABLE_CLASS_NAME

        if (
            current_section_slug == "matrix-reproduction-impact"
            and current_subsection_slug == "campaign-wide-cell-totals"
            and normalized_header_cells == ("Surface", "Green", "Yellow", "Red")
        ):
            return TRACK1_FULL_MATRIX_CELL_TOTALS_TABLE_CLASS_NAME

    if report_stem == "2026-04-18-11-14-50_track1_remaining_family_partial_closeout_campaign_results_report":

        if (
            current_section_slug == "completed-family-closeout"
            and normalized_header_cells == ("Family", "Amplitude Run", "Phase Run", "Best Run", "Best Scope", "Best Closure Score", "Open Cells")
        ):
            return TRACK1_PARTIAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME

        if (
            current_section_slug == "aggregate-ranking"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Paper Cell", "Met", "Near", "Open", "Closure Score")
        ):
            return TRACK1_PARTIAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME

    if report_stem == "2026-04-18-16-34-18_track1_remaining_family_final_closeout_campaign_results_report":

        if (
            current_section_slug == "family-recovery-outcome"
            and normalized_header_cells == ("Family", "Amplitude Run", "Phase Run", "Best Run", "Best Scope", "Best Closure Score", "Open Cells")
        ):
            return TRACK1_FINAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME

        if (
            current_section_slug == "aggregate-ranking"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Paper Cell", "Met", "Near", "Open", "Closure Score")
        ):
            return TRACK1_FINAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME

    if report_stem == "2026-04-19-00-43-47_track1_remaining_family_cellwise_final_closeout_campaign_results_report":

        if (
            current_section_slug == "family-recovery-outcome"
            and normalized_header_cells == ("Family", "Amplitude Run", "Phase Run", "Best Run", "Best Scope", "Best Closure Score", "Open Cells")
        ):
            return TRACK1_FINAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME

        if (
            current_section_slug == "aggregate-ranking"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Paper Cell", "Met", "Near", "Open", "Closure Score")
        ):
            return TRACK1_FINAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME

    if report_stem == "2026-04-19-11-34-36_track1_remaining_family_residual_cellwise_closure_campaign_results_report":

        if (
            current_section_slug == "family-recovery-outcome"
            and normalized_header_cells == ("Family", "Amplitude Run", "Phase Run", "Best Run", "Best Scope", "Best Closure Score", "Open Cells")
        ):
            return TRACK1_FINAL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME

        if (
            current_section_slug == "aggregate-ranking"
            and normalized_header_cells == ("Rank", "Run", "Family", "Scope", "Paper Cell", "Met", "Near", "Open", "Closure Score")
        ):
            return TRACK1_FINAL_CLOSEOUT_AGGREGATE_TABLE_CLASS_NAME

    if report_stem == "2026-04-21-14-58-00_track1_open_cell_full_matrix_closure_campaign_results_report":

        if (
            current_section_slug == "family-representative-outcome"
            and normalized_header_cells == ("Family", "Best Run", "Scope", "Closure Score", "Met", "Near", "Open")
        ):
            return TRACK1_OPEN_CELL_CLOSEOUT_FAMILY_TABLE_CLASS_NAME

        if (
            current_section_slug == "canonical-benchmark-outcome"
            and normalized_header_cells == ("Surface", "Harmonics Met", "Total Harmonics", "Open Harmonics")
        ):
            return TRACK1_OPEN_CELL_CLOSEOUT_BENCHMARK_TABLE_CLASS_NAME

    if is_repository_status_wave_track_report(report_stem):

        if (
            current_section_slug == "executive-summary"
            and normalized_header_cells == ("Surface", "Run", "Family", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return REPOSITORY_STATUS_SCALAR_WINNER_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-1-static-baselines"
            and normalized_header_cells == ("Rank", "Family", "Scope", "Engine", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return REPOSITORY_STATUS_HPO_LEADER_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-1-static-baselines"
            and normalized_header_cells == ("Family Surface", "Best Run", "Harmonic Basis", "Test MAE [deg]")
        ):
            return REPOSITORY_STATUS_HARMONIC_RESULTS_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2-temporal-sequence-models"
            and normalized_header_cells == ("Run", "Family", "Scope", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return REPOSITORY_STATUS_TEMPORAL_WINNER_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2-temporal-sequence-models"
            and normalized_header_cells == ("Surface", "Run", "Family", "Test MAE [deg]")
        ):
            return REPOSITORY_STATUS_TEMPORAL_SURFACES_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2b-harmonic-temporal-hybrids"
            and normalized_header_cells == ("Run", "Family", "Scope", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return REPOSITORY_STATUS_WAVE2B_SCALAR_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2b-harmonic-temporal-hybrids"
            and normalized_header_cells == ("Candidate", "Surface", "Curve MAE [deg]", "Curve RMSE [deg]", "Mean Error [%]")
        ):
            return REPOSITORY_STATUS_WAVE2B_TRACK2_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2c-residual-harmonic-temporal-hybrids"
            and normalized_header_cells == ("Run", "Family", "Basis", "Scope", "Test MAE [deg]", "Test RMSE [deg]")
        ):
            return REPOSITORY_STATUS_WAVE2C_SCALAR_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2c-residual-harmonic-temporal-hybrids"
            and normalized_header_cells == ("Scope", "Candidate", "Basis", "Curve MAE [deg]", "Curve RMSE [deg]", "Mean Error [%]")
        ):
            return REPOSITORY_STATUS_WAVE2C_TRACK2_TABLE_CLASS_NAME

        if (
            current_section_slug == "wave-2c-residual-harmonic-temporal-hybrids"
            and normalized_header_cells == ("Scope", "Candidate", "Basis", "Curve MAE [deg]", "Mean Error [%]")
        ):
            return REPOSITORY_STATUS_WAVE2C_DENSE_TABLE_CLASS_NAME

        if (
            current_section_slug == "track-2-current-result"
            and normalized_header_cells == ("Scope", "Current Strongest Candidate", "MAE [deg]", "RMSE [deg]", "Mean [%]")
        ):
            return REPOSITORY_STATUS_TRACK2_CURRENT_TABLE_CLASS_NAME

        if (
            current_section_slug == "harmonic-bank-conclusions"
            and normalized_header_cells == ("Context", "Best Observed Choice", "Evidence")
        ):
            return REPOSITORY_STATUS_HARMONIC_BANK_TABLE_CLASS_NAME

    if (
        current_section_slug == "targeted-pair-outcome"
        and normalized_header_cells == ("Pair", "Baseline", "Campaign Best", "Accepted", "Source", "Result")
    ):
        return TRACK1_MLP_CLOSEOUT_TARGETED_PAIR_TABLE_CLASS_NAME

    if report_stem == "2026-04-24-12-39-24_track1_remaining_yellow_cell_interrupted_svm_partial_closeout_campaign_results_report":

        if (
            current_section_slug == "candidate-scientific-gains"
            and normalized_header_cells == ("Candidate", "Run Instance", "MAE", "RMSE", "Notes")
        ):
            return TRACK1_INTERRUPTED_SVM_CANDIDATE_GAINS_TABLE_CLASS_NAME

    if report_stem == "2026-05-08-19-53-19_track1_forward_dt_paper_faithful_search_campaign_results_report":

        if (
            current_section_slug == "historical-replay-outcome"
            and normalized_header_cells == ("Scope", "Mean MAE", "Mean RMSE", "Mean MAPE %")
        ):
            return TRACK1_FORWARD_DT_HISTORICAL_REPLAY_OUTCOME_TABLE_CLASS_NAME

    if (
        current_section_slug == "benchmark-restart-surface"
        and normalized_header_cells == ("Table", "Direction", "Green", "Yellow", "Red", "Total")
    ):
        return TRACK1_BIDIRECTIONAL_MEGA_BENCHMARK_SURFACE_TABLE_CLASS_NAME

    if (
        current_section_slug == "reference-archive-refresh"
        and normalized_header_cells == ("Direction", "Family", "Archived Targets", "Unique Source Runs", "Unique Source Configs", "Archive Root")
    ):
        return TRACK1_BIDIRECTIONAL_MEGA_REFERENCE_ARCHIVE_TABLE_CLASS_NAME

    if (
        current_section_slug == "archive-completeness"
        and normalized_header_cells == ("Direction", "Family", "Retune Bundle", "Eval Bundle", "Export Bundle", "ONNX", "PKL", "Exported Errors")
    ):
        return RCIM_RETUNED_ARCHIVE_COMPLETENESS_TABLE_CLASS_NAME

    if (
        current_section_slug == "mean-evaluation-metrics"
        and normalized_header_cells == ("Direction", "Family", "MSE", "RMSE", "MAE", "MAPE")
    ):
        return RCIM_RETUNED_MEAN_EVALUATION_METRICS_TABLE_CLASS_NAME

    if (
        current_section_slug in {"forward-retuned-tables", "backward-retuned-tables"}
        and current_subsection_slug in {
            "table-2-amplitude-mae",
            "table-3-amplitude-rmse",
            "table-4-phase-mae",
            "table-5-phase-rmse",
        }
        and normalized_header_cells
        and normalized_header_cells[0] == "Model"
    ):
        return RCIM_RETUNED_HARMONIC_METRIC_TABLE_CLASS_NAME

    return GENERIC_TABLE_CLASS_NAME

def render_table(
    markdown_lines: Sequence[str],
    start_index: int,
    report_stem: str,
    current_section_slug: str,
    current_subsection_slug: str,
) -> tuple[str, int]:

    """ Render Table """

    # Collect Table Lines
    table_lines, current_index = collect_table_lines(markdown_lines, start_index)

    # Validate Table Structure
    if len(table_lines) < 2: raise ValueError("Expected at least header and separator row in Markdown table.")

    # Parse Table Sections
    header_cells = split_table_row(table_lines[0])
    alignments = extract_table_alignments(table_lines[1])
    body_rows = table_lines[2:]

    # Render Configuration Comparison Matrix
    if tuple(header_cells) == CONFIGURATION_TABLE_HEADER_CELLS:
        return render_configuration_split_tables(body_rows), current_index

    # Render Track 2 Wide Tables With PDF-Safe Summary Columns
    if tuple(header_cells) == TRACK2_CURVE_FIRST_RANKING_TABLE_HEADER_CELLS:
        return (
            render_column_subset_table(
                header_cells,
                alignments,
                body_rows,
                TRACK2_CURVE_FIRST_RANKING_PDF_COLUMN_INDEXES,
                TRACK2_CURVE_FIRST_RANKING_TABLE_CLASS_NAME,
            ),
            current_index,
        )

    if tuple(header_cells) == TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_TABLE_HEADER_CELLS:
        return (
            render_column_subset_table(
                header_cells,
                alignments,
                body_rows,
                TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_PDF_COLUMN_INDEXES,
                TRACK2_CURVE_PAYLOAD_DIAGNOSTICS_TABLE_CLASS_NAME,
            ),
            current_index,
        )

    if tuple(header_cells) == TRACK2_SURFACE_LEADER_TABLE_HEADER_CELLS:
        return render_standard_table(header_cells, alignments, body_rows, TRACK2_SURFACE_LEADER_TABLE_CLASS_NAME), current_index

    if tuple(header_cells) == TRACK2_MEAN_CENTERED_TOP_TABLE_HEADER_CELLS:
        return render_standard_table(header_cells, alignments, body_rows, TRACK2_MEAN_CENTERED_TOP_TABLE_CLASS_NAME), current_index

    if tuple(header_cells) == TRACK2_MEAN_CENTERED_GROUP_TABLE_HEADER_CELLS:
        return render_standard_table(header_cells, alignments, body_rows, TRACK2_MEAN_CENTERED_GROUP_TABLE_CLASS_NAME), current_index

    if tuple(header_cells) == TRACK2D_MEAN_OFFSET_TABLE_HEADER_CELLS:
        return render_standard_table(header_cells, alignments, body_rows, TRACK2D_MEAN_OFFSET_TABLE_CLASS_NAME), current_index

    if tuple(header_cells) == TRACK2E_OFFSET_FEASIBILITY_TABLE_HEADER_CELLS:
        return render_standard_table(header_cells, alignments, body_rows, TRACK2E_OFFSET_FEASIBILITY_TABLE_CLASS_NAME), current_index

    # Resolve Table Class
    table_class_name = resolve_standard_table_class_name(
        header_cells,
        report_stem,
        current_section_slug,
        current_subsection_slug,
    )

    # Render Generic Markdown Table
    return render_standard_table(header_cells, alignments, body_rows, table_class_name), current_index

def render_list(markdown_lines: Sequence[str], start_index: int, base_indentation: int) -> tuple[str, int]:

    """ Render List """

    # Resolve List Type
    _, current_list_tag, _ = get_list_item_metadata(markdown_lines[start_index])
    current_index = start_index
    list_item_html_tokens: list[str] = []

    while current_index < len(markdown_lines):

        # Read Current Line
        current_line = markdown_lines[current_index]

        # Skip Empty Lines
        if not current_line.strip():
            current_index += 1
            continue

        # Validate List Item
        if not is_list_item(current_line): break

        # Parse List Item Metadata
        indentation_width, list_tag, item_content = get_list_item_metadata(current_line)

        # Validate Nesting Level
        if indentation_width < base_indentation or list_tag != current_list_tag: break

        # Render Nested List Branch
        if indentation_width > base_indentation:
            nested_list_html, current_index = render_list(
                markdown_lines,
                current_index,
                indentation_width,
            )

            if list_item_html_tokens:
                list_item_html_tokens[-1] = list_item_html_tokens[-1].replace(
                    "</li>",
                    f"{nested_list_html}</li>",
                    1,
                )

            continue

        current_index += 1
        continuation_lines: list[str] = []
        nested_html_tokens: list[str] = []

        # Collect Continuation Paragraphs And Nested Blocks
        while current_index < len(markdown_lines):

            # Read Lookahead Line
            lookahead_line = markdown_lines[current_index]

            # Skip Empty Spacing
            if not lookahead_line.strip():
                current_index += 1
                continue

            # Stop On Heading Or Table
            if is_heading(lookahead_line) or is_table_row(lookahead_line): break

            # Render Nested List Branch
            if is_list_item(lookahead_line):

                # Read Nested Indentation
                next_indentation_width, _, _ = get_list_item_metadata(lookahead_line)
                if next_indentation_width <= base_indentation: break

                # Render Nested List Branch
                nested_list_html, current_index = render_list(
                    markdown_lines,
                    current_index,
                    next_indentation_width,
                )
                nested_html_tokens.append(nested_list_html)
                continue

            continuation_lines.append(lookahead_line.strip())
            current_index += 1

        # Render One List Item
        item_body_html = convert_inline_markup(item_content)

        if continuation_lines:

            # Render Continuation Text
            continuation_text = " ".join(continuation_lines)
            item_body_html += (f'<p class="list-continuation">{convert_inline_markup(continuation_text)}</p>')

        # Append List Item HTML
        list_item_html_tokens.append(f'<li><div class="li-body">{item_body_html}</div>{"".join(nested_html_tokens)}</li>')

    # Return List HTML
    return (f'<{current_list_tag} class="report-list">{"".join(list_item_html_tokens)}</{current_list_tag}>', current_index)

def render_paragraph(paragraph_lines: Sequence[str], markdown_directory: Path) -> str:

    """ Render Paragraph """

    # Normalize Paragraph Text
    paragraph_text = " ".join(markdown_line.strip() for markdown_line in paragraph_lines).strip()
    parsed_image = parse_markdown_image(paragraph_text)
    if parsed_image is not None:
        return render_markdown_image(paragraph_text, markdown_directory)

    normalized_word_count = len(paragraph_text.rstrip(":").split())

    # Render Short Label Paragraph
    if paragraph_text.endswith(":") and normalized_word_count <= 6:
        label_text = convert_inline_markup(paragraph_text[:-1])
        return f'<p class="block-label">{label_text}</p>'

    # Render Standard Paragraph
    return f"<p>{convert_inline_markup(paragraph_text)}</p>"

def should_keep_section_together(section_body_tokens: Sequence[str]) -> bool:

    """ Report Whether A Section Is Compact Enough To Stay Together """

    section_body_html = "".join(section_body_tokens)

    # Skip Table-Heavy Or Explicitly Structured Sections
    if "<table" in section_body_html:
        return False

    if section_body_html.count('class="subsection-block"') > 1:
        return False

    # Estimate Visual Density From Visible Text
    visible_section_text = re.sub(r"<[^>]+>", " ", section_body_html)
    visible_word_count = len(visible_section_text.split())

    return visible_word_count <= 165

def render_markdown_body(markdown_text: str, markdown_path: Path) -> tuple[str, str]:

    """ Render Markdown Body """

    markdown_lines = markdown_text.splitlines()
    markdown_directory = markdown_path.parent.resolve()
    report_stem = markdown_path.stem

    # Validate Report Heading
    if not markdown_lines or not markdown_lines[0].startswith("# "):
        raise ValueError("Expected the report Markdown to start with one H1 heading.")

    # Initialize Markdown Parsing State
    report_title = markdown_lines[0][2:].strip()
    body_lines = markdown_lines[1:]
    current_index = 0
    paragraph_lines: list[str] = []
    document_html_tokens: list[str] = []
    current_section_title = ""
    current_section_slug = ""
    current_section_body_tokens: list[str] = []
    current_subsection_title = ""
    current_subsection_body_tokens: list[str] = []

    def flush_paragraph() -> None:

        """ Flush Paragraph """

        nonlocal paragraph_lines

        if paragraph_lines:

            # Append Paragraph HTML
            if current_subsection_title: current_subsection_body_tokens.append(render_paragraph(paragraph_lines, markdown_directory))
            else: current_section_body_tokens.append(render_paragraph(paragraph_lines, markdown_directory))

            paragraph_lines = []

    def flush_subsection() -> None:

        """ Flush Subsection """

        nonlocal current_subsection_title, current_subsection_body_tokens

        # Flush Paragraph Content
        flush_paragraph()

        if not current_subsection_title: return

        if current_subsection_body_tokens:

            # Append Subsection Block
            subsection_title_html = convert_inline_markup(current_subsection_title)
            subsection_slug = slugify(current_subsection_title)
            current_section_body_tokens.append(f'<div id="{subsection_slug}" class="subsection-block"><h3>{subsection_title_html}</h3>{"".join(current_subsection_body_tokens)}</div>')

        current_subsection_title = ""
        current_subsection_body_tokens = []

    def flush_section() -> None:

        """ Flush Section """

        nonlocal current_section_title, current_section_slug, current_section_body_tokens

        # Flush Nested Subsection
        flush_subsection()

        if current_section_title and current_section_body_tokens:

            # Append Section Block
            section_title_html = convert_inline_markup(current_section_title)
            section_class_names = ["section-card", f"section-{current_section_slug}"]
            report_specific_forced_page_break_section_slugs = REPORT_SPECIFIC_FORCED_PAGE_BREAK_SECTION_SLUGS.get(report_stem, set())
            force_page_break_before_section = False

            if (
                current_section_slug in FORCED_PAGE_BREAK_SECTION_SLUGS
                or current_section_slug in report_specific_forced_page_break_section_slugs
            ):
                section_class_names.append("section-force-page-break")
                force_page_break_before_section = True

            if should_keep_section_together(current_section_body_tokens):
                section_class_names.append("section-keep-together")

            if (
                force_page_break_before_section
                and report_stem not in {
                    "track2_curve_first_reranking_report",
                    "track2_curve_payload_diagnostics_report",
                    "track2_best_model_collage_report",
                    "track2_multi_model_curve_comparison_report",
                    "track2_forward_reference_curve_comparison_report",
                    "track2d_mean_offset_full_matrix_audit",
                    "track2e_offset_predictability_feasibility",
                    "2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report",
                    "2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report",
                    "2026-06-05-16-49-50_track2f_bis_harmonic_offset_probe_campaign_results_report",
                    "2026-06-09-01-56-25_track2g_curve_aware_training_campaign_results_report",
                }
                and not (
                    report_stem == "2026-04-22-01-08-33_track1_mlp_residual_cell_final_closure_campaign_results_report"
                    and current_section_slug == "targeted-pair-outcome"
                )
            ):
                document_html_tokens.append('<div class="explicit-page-break"></div>')

            document_html_tokens.append(
                f'<section id="{current_section_slug}" class="{" ".join(section_class_names)}"><h2>{section_title_html}</h2>{"".join(current_section_body_tokens)}</section>'
            )

        current_section_title = ""
        current_section_slug = ""
        current_section_body_tokens = []

    while current_index < len(body_lines):

        # Read Current Line
        current_line = body_lines[current_index].rstrip()
        stripped_line = current_line.strip()

        # Flush On Empty Line
        if not stripped_line:
            flush_paragraph()
            current_index += 1
            continue

        # Skip Standalone HTML Comments
        if is_html_comment_line(current_line):
            flush_paragraph()
            current_index += 1
            continue

        # Start New Section
        if current_line.startswith("## "):
            flush_section()
            current_section_title = current_line[3:].strip()
            current_section_slug = slugify(current_section_title)
            current_index += 1
            continue

        # Start New Subsection
        if current_line.startswith("### "):
            flush_subsection()
            current_subsection_title = current_line[4:].strip()
            current_index += 1
            continue

        # Render Table Block
        if is_table_row(current_line):

            # Flush Pending Paragraph
            flush_paragraph()
            table_html, current_index = render_table(
                body_lines,
                current_index,
                report_stem,
                current_section_slug,
                slugify(current_subsection_title) if current_subsection_title else "",
            )

            # Append Table HTML
            if current_subsection_title: current_subsection_body_tokens.append(table_html)
            else: current_section_body_tokens.append(table_html)

            continue

        # Render List Block
        if is_list_item(current_line):

            # Flush Pending Paragraph
            flush_paragraph()
            indentation_width, _, _ = get_list_item_metadata(current_line)
            list_html, current_index = render_list(body_lines, current_index, indentation_width)

            # Append List HTML
            if current_subsection_title: current_subsection_body_tokens.append(list_html)
            else: current_section_body_tokens.append(list_html)

            continue

        # Accumulate Paragraph Lines
        paragraph_lines.append(current_line)
        current_index += 1

    flush_section()

    return report_title, "\n".join(document_html_tokens)

def build_html_document(report_title: str, report_subtitle: str, report_category: str, body_html: str) -> str:

    """Assemble the standalone HTML document used for preview and PDF export.

    Args:
        report_title: Main report title shown in the hero block.
        report_subtitle: Subtitle shown below the report title.
        report_category: Category badge displayed in the hero block.
        body_html: Rendered report body HTML.

    Returns:
        str: Complete HTML document with the repository report stylesheet
        embedded inline.
    """

    # Escape Header Text
    escaped_title = html.escape(report_title)
    escaped_subtitle = html.escape(report_subtitle)
    escaped_category = html.escape(report_category)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escaped_title}</title>
  <style>
{REPORT_STYLESHEET}
  </style>
</head>
<body>
  <main class="page-shell">
    <header class="hero">
      <div class="hero-badge">{escaped_category}</div>
      <h1>{escaped_title}</h1>
      <p class="hero-subtitle">{escaped_subtitle}</p>
      <p class="hero-note">{html.escape(HERO_NOTE_TEXT)}</p>
    </header>
    {body_html}
  </main>
</body>
</html>
"""

def write_text_file(file_path: Path, file_content: str) -> None:

    """ Write Text File """

    # Create Parent Directory
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Save Text Content
    file_path.write_text(file_content, encoding="utf-8")

def convert_html_to_pdf(browser_executable_path: Path, html_path: Path, pdf_path: Path) -> None:

    """Export a rendered HTML report to PDF through a headless browser.

    Args:
        browser_executable_path: Resolved Chrome or Edge executable.
        html_path: Local HTML file generated by the report pipeline.
        pdf_path: Final PDF output path.

    Raises:
        subprocess.CalledProcessError: If the browser export command fails.
    """

    # Resolve Export Paths
    html_uri = html_path.resolve().as_uri()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_profile_path = create_workspace_temp_directory(BROWSER_PROFILE_TEMP_ROOT, "codex_report_chrome")

    try:

        # Export PDF Through Headless Browser
        subprocess.run(
            [
                str(browser_executable_path),
                *BROWSER_PDF_EXPORT_ARGUMENTS,
                f"--user-data-dir={temporary_profile_path}",
                f"--print-to-pdf={pdf_path.resolve()}",
                html_uri,
            ],
            check=True,
            capture_output=True,
            text=True,
        )

    finally:

        # Remove Temporary Browser Profile
        remove_temporary_directory(temporary_profile_path)

def main() -> None:

    """Run the styled Markdown-to-PDF export pipeline.

    The pipeline resolves paths, renders the Markdown source into the custom
    HTML layout, exports the PDF through a headless browser, and cleans
    temporary workspace artifacts unless an HTML preview is explicitly kept.
    """

    # Parse Command-Line Arguments
    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()
    platform_name = repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )

    # Resolve Report Paths
    input_markdown_path = resolve_report_path(parsed_arguments.input_markdown_path)
    output_pdf_path = resolve_report_path(parsed_arguments.output_pdf_path)
    output_html_path, use_temporary_html_path = resolve_output_html_path(
        parsed_arguments.output_html_path,
        output_pdf_path,
        parsed_arguments.keep_html,
    )

    # Render Styled HTML Document
    markdown_text = input_markdown_path.read_text(encoding="utf-8")
    report_title, body_html = render_markdown_body(markdown_text, input_markdown_path)
    report_subtitle = REPORT_SPECIFIC_SUBTITLE_DICTIONARY.get(
        input_markdown_path.stem,
        parsed_arguments.report_subtitle,
    )
    html_document = build_html_document(
        report_title,
        report_subtitle,
        parsed_arguments.report_category,
        body_html,
    )
    write_text_file(output_html_path, html_document)

    # Export Final PDF Report
    browser_executable_path = detect_browser_executable(
        parsed_arguments.chrome_executable_path,
        platform_name,
    )
    convert_html_to_pdf(
        browser_executable_path,
        output_html_path,
        output_pdf_path,
    )

    # Remove Temporary HTML Preview
    if use_temporary_html_path and output_html_path.exists():
        remove_temporary_file(output_html_path)

    print(f"Styled PDF generated at: {output_pdf_path}")

if __name__ == "__main__":

    main()
