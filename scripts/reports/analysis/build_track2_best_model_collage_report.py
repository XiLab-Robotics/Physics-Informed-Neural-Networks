"""Build the TE Curve Verification Pipeline best-model collage report and plot artifacts."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import hashlib
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np
import yaml
from tqdm import tqdm

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.reports.analysis import track2_circular_plotting
from scripts.tooling import repository_path_support
from scripts.training import shared_training_infrastructure

DEFAULT_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "track2_best_model_collage_report"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "track2" / "best_model_collage_report"
DEFAULT_FAMILY_REGISTRY_ROOT = PROJECT_PATH / "output" / "registries" / "families"
DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42"
    / "campaign_leaderboard.yaml"
)
SUMMARY_FILENAME = "track2_best_model_collage_summary.yaml"
METRICS_FILENAME = "track2_best_model_collage_metrics.csv"
REPORT_FILENAME = "track2_best_model_collage_report.md"
MAX_REPORT_ASSET_FRAGMENT_LENGTH = 48

CANONICAL_MODEL_FAMILY_NAME_DICTIONARY = {
    "sequential_residual_offset_probe": "wave3_1_sequential_residual_offset_probe",
    "track2f_bis_clean_sequential_residual_offset": "wave3_2_clean_sequential_residual_offset",
    "track2f_bis_harmonic_residual_offset": "wave3_2_harmonic_residual_offset",
    "track2g_curve_aware_pointwise_control": "wave3_3_curve_aware_pointwise_control",
    "track2g_curve_aware_raw_centered_shape": "wave3_3_raw_centered_shape_curve_aware",
    "track2g_curve_aware_raw_offset": "wave3_3_raw_offset_curve_aware",
    "track2g_curve_aware_full_curve_composite": "wave3_3_full_curve_composite",
    "track2h_mae_robust": "wave4_1_mae_robust_loss",
    "track2h_smooth_l1_robust": "wave4_1_smooth_l1_robust_loss",
    "track2h_log_cosh_robust": "wave4_1_log_cosh_robust_loss",
    "track2h_quantile_p10_p50_p90": "wave4_2_quantile_p10_p50_p90",
    "track2h_gaussian_nll": "wave4_2_gaussian_nll",
    "track2h_mdn_k2": "wave4_3_mixture_density_k2",
    "track2h_mdn_k3": "wave4_3_mixture_density_k3",
    "track2h_l_gru_offset_residual": "wave4_4_gru_latent_offset_residual",
    "track2h_l_causal_tcn_offset_residual": "wave4_4_causal_tcn_latent_offset_residual",
    "wave3_harmonic_prior_residual_pointwise_control": "wave5_1_harmonic_prior_pointwise_control",
    "wave3_harmonic_prior_residual_smooth_l1_structured": "wave5_1_harmonic_prior_smooth_l1_structured",
}
CANONICAL_SOURCE_LABEL_DICTIONARY = {
    "track2f_offset_aware_probe_registry": "wave3_1_offset_aware_probe_registry",
    "track2f_bis_harmonic_offset_probe_registry": "wave3_2_harmonic_offset_probe_registry",
    "track2g_curve_aware_training_registry": "wave3_3_curve_aware_training_registry",
    "track2h_dispersion_aware_modeling_registry": "wave4_1_robust_loss_registry",
    "track2h_quantile_probabilistic_registry": "wave4_2_probabilistic_registry",
    "track2h_mixture_density_heads_registry": "wave4_3_mixture_density_registry",
    "track2h_latent_state_hysteresis_registry": "wave4_4_latent_state_hysteresis_registry",
    "wave3_harmonic_prior_residual_registry": "wave5_1_harmonic_prior_residual_registry",
}
CANONICAL_SOURCE_TITLE_DICTIONARY = {
    "track2h_mixture_density_heads_registry": "Wave 4.3 Mixture Density Models",
    "track2h_latent_state_hysteresis_registry": "Wave 4.4 Latent State Hysteresis Models",
    "wave3_harmonic_prior_residual_registry": "Wave 5.1 Harmonic Prior Residual Models",
}
CANONICAL_SOURCE_WAVE_ORDER_DICTIONARY = {
    "track2h_mixture_density_heads_registry": 43,
    "track2h_latent_state_hysteresis_registry": 44,
    "wave3_harmonic_prior_residual_registry": 51,
}
CANONICAL_SURFACE_SUFFIX_DICTIONARY = {
    "Fw": "fw",
    "Bw": "bw",
    "global": "global",
}

WAVE1_BASE_FAMILY_LIST = [
    "feedforward",
    "harmonic_regression",
    "periodic_mlp",
    "residual_harmonic_mlp",
    "tree",
]
WAVE2_BASE_FAMILY_LIST = [
    "temporal_convolution",
    "gru_sequence",
    "lstm_sequence",
    "periodic_temporal_convolution",
    "periodic_gru_sequence",
    "periodic_lstm_sequence",
]
WAVE2C_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "residual_harmonic_gru_sequence_sparse_rcim",
        "candidate_family": "residual_harmonic_gru_sequence_sparse_rcim",
        "global_family": "residual_harmonic_gru_sequence_sparse_rcim",
        "fw_family": "residual_harmonic_gru_sequence_fw_sparse_rcim",
        "bw_family": "residual_harmonic_gru_sequence_bw_sparse_rcim",
    },
    {
        "candidate_id_prefix": "residual_harmonic_gru_sequence_dense240",
        "candidate_family": "residual_harmonic_gru_sequence_dense240",
        "global_family": "residual_harmonic_gru_sequence_dense240",
        "fw_family": "residual_harmonic_gru_sequence_fw_dense240",
        "bw_family": "residual_harmonic_gru_sequence_bw_dense240",
    },
    {
        "candidate_id_prefix": "residual_harmonic_gru_sequence_dense360",
        "candidate_family": "residual_harmonic_gru_sequence_dense360",
        "global_family": "residual_harmonic_gru_sequence_dense360",
        "fw_family": "residual_harmonic_gru_sequence_fw_dense360",
        "bw_family": "residual_harmonic_gru_sequence_bw_dense360",
    },
    {
        "candidate_id_prefix": "residual_harmonic_lstm_sequence_sparse_rcim",
        "candidate_family": "residual_harmonic_lstm_sequence_sparse_rcim",
        "global_family": "residual_harmonic_lstm_sequence_sparse_rcim",
        "fw_family": "residual_harmonic_lstm_sequence_fw_sparse_rcim",
        "bw_family": "residual_harmonic_lstm_sequence_bw_sparse_rcim",
    },
    {
        "candidate_id_prefix": "residual_harmonic_lstm_sequence_dense240",
        "candidate_family": "residual_harmonic_lstm_sequence_dense240",
        "global_family": "residual_harmonic_lstm_sequence_dense240",
        "fw_family": "residual_harmonic_lstm_sequence_fw_dense240",
        "bw_family": "residual_harmonic_lstm_sequence_bw_dense240",
    },
    {
        "candidate_id_prefix": "residual_harmonic_lstm_sequence_dense360",
        "candidate_family": "residual_harmonic_lstm_sequence_dense360",
        "global_family": "residual_harmonic_lstm_sequence_dense360",
        "fw_family": "residual_harmonic_lstm_sequence_fw_dense360",
        "bw_family": "residual_harmonic_lstm_sequence_bw_dense360",
    },
]
TRACK2F_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "sequential_residual_offset_probe",
        "candidate_family": "sequential_residual_offset_probe",
        "global_family": "sequential_residual_offset_probe",
        "fw_family": "sequential_residual_offset_probe_fw",
        "bw_family": "sequential_residual_offset_probe_bw",
    },
]
TRACK2F_BIS_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "track2f_bis_clean_sequential_residual_offset",
        "candidate_family": "track2f_bis_clean_sequential_residual_offset",
        "global_family": "track2f_bis_clean_sequential_residual_offset_global",
        "fw_family": "track2f_bis_clean_sequential_residual_offset_fw",
        "bw_family": "track2f_bis_clean_sequential_residual_offset_bw",
    },
    {
        "candidate_id_prefix": "track2f_bis_harmonic_residual_offset",
        "candidate_family": "track2f_bis_harmonic_residual_offset",
        "global_family": "track2f_bis_harmonic_residual_offset_global",
        "fw_family": "track2f_bis_harmonic_residual_offset_fw",
        "bw_family": "track2f_bis_harmonic_residual_offset_bw",
    },
]
TRACK2G_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "track2g_curve_aware_pointwise_control",
        "candidate_family": "track2g_curve_aware_pointwise_control",
        "global_family": "track2g_curve_aware_harmonic_residual_offset_pointwise_control_global",
        "fw_family": "track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw",
        "bw_family": "track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw",
    },
    {
        "candidate_id_prefix": "track2g_curve_aware_raw_centered_shape",
        "candidate_family": "track2g_curve_aware_raw_centered_shape",
        "global_family": "track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global",
        "fw_family": "track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw",
        "bw_family": "track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw",
    },
    {
        "candidate_id_prefix": "track2g_curve_aware_raw_offset",
        "candidate_family": "track2g_curve_aware_raw_offset",
        "global_family": "track2g_curve_aware_harmonic_residual_offset_raw_offset_global",
        "fw_family": "track2g_curve_aware_harmonic_residual_offset_raw_offset_fw",
        "bw_family": "track2g_curve_aware_harmonic_residual_offset_raw_offset_bw",
    },
    {
        "candidate_id_prefix": "track2g_curve_aware_full_curve_composite",
        "candidate_family": "track2g_curve_aware_full_curve_composite",
        "global_family": "track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global",
        "fw_family": "track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw",
        "bw_family": "track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw",
    },
]
TRACK2H_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "track2h_mae_robust",
        "candidate_family": "track2h_mae_robust",
        "global_family": "track2h_dispersion_aware_mae_robust_global",
        "fw_family": "track2h_dispersion_aware_mae_robust_fw",
        "bw_family": "track2h_dispersion_aware_mae_robust_bw",
    },
    {
        "candidate_id_prefix": "track2h_smooth_l1_robust",
        "candidate_family": "track2h_smooth_l1_robust",
        "global_family": "track2h_dispersion_aware_smooth_l1_robust_global",
        "fw_family": "track2h_dispersion_aware_smooth_l1_robust_fw",
        "bw_family": "track2h_dispersion_aware_smooth_l1_robust_bw",
    },
    {
        "candidate_id_prefix": "track2h_log_cosh_robust",
        "candidate_family": "track2h_log_cosh_robust",
        "global_family": "track2h_dispersion_aware_log_cosh_robust_global",
        "fw_family": "track2h_dispersion_aware_log_cosh_robust_fw",
        "bw_family": "track2h_dispersion_aware_log_cosh_robust_bw",
    },
]
TRACK2H_QUANTILE_PROBABILISTIC_FAMILY_CONFIGURATION_LIST = [
    {
        "candidate_id_prefix": "track2h_quantile_p10_p50_p90",
        "candidate_family": "track2h_quantile_p10_p50_p90",
        "global_family": "track2h_quantile_probabilistic_quantile_p10_p50_p90_global",
        "fw_family": "track2h_quantile_probabilistic_quantile_p10_p50_p90_fw",
        "bw_family": "track2h_quantile_probabilistic_quantile_p10_p50_p90_bw",
    },
    {
        "candidate_id_prefix": "track2h_gaussian_nll",
        "candidate_family": "track2h_gaussian_nll",
        "global_family": "track2h_quantile_probabilistic_gaussian_nll_global",
        "fw_family": "track2h_quantile_probabilistic_gaussian_nll_fw",
        "bw_family": "track2h_quantile_probabilistic_gaussian_nll_bw",
    },
]
FORWARD_REFERENCE_CANDIDATE_ID_LIST = [
    "paper_original_best_Fw",
    "paper_retuned_best_Fw",
    "track1_best_Fw",
]
BACKWARD_REFERENCE_CANDIDATE_ID_LIST = [
    "paper_retuned_best_Bw",
    "track1_best_Bw",
]


@dataclass(frozen=True)
class ReportCandidateGroup:

    """One logical report group for a set of candidates."""

    group_id: str
    group_title: str
    candidate_id_list: list[str]
    selection_mode: str


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description=(
            "Generate the TE Curve Verification Pipeline best-model visual report with one four-curve "
            "collage per selected reference, Wave 1 directional, and Wave 1 "
            "global candidate."
        )
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="TE Curve Verification Pipeline comparison config used for reference candidate metadata and dataset loading.",
    )
    argument_parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root for generated collage artifacts and machine-readable summaries.",
    )
    argument_parser.add_argument(
        "--report-topic-root",
        type=Path,
        default=DEFAULT_REPORT_TOPIC_ROOT,
        help="Root for the dated Markdown/PDF report bundle.",
    )
    argument_parser.add_argument(
        "--report-date",
        type=str,
        default=None,
        help=(
            "Optional YYYY-MM-DD report bundle date to refresh instead of "
            "creating a report folder from the current date."
        ),
    )
    argument_parser.add_argument(
        "--dataset",
        choices=["polished_dataset", "simplified_dataset"],
        default=None,
        help="Dataset selector overriding the comparison YAML for this visual report.",
    )
    argument_parser.add_argument(
        "--surface-scope",
        choices=["all", "forward", "backward", "global"],
        default="all",
        help="Limit the visual report to one dataset-surface report scope.",
    )
    argument_parser.add_argument(
        "--candidate-id",
        dest="candidate_id_list",
        action="append",
        default=[],
        help=(
            "Optional candidate id to include. May be repeated to build a "
            "bounded visual shortlist from a compact matrix."
        ),
    )
    argument_parser.add_argument(
        "--family-registry-root",
        type=Path,
        default=DEFAULT_FAMILY_REGISTRY_ROOT,
        help="Root containing current Wave 1 family latest_family_best.yaml registries.",
    )
    argument_parser.add_argument(
        "--periodic-mlp-harmonic-campaign-leaderboard-path",
        type=Path,
        default=DEFAULT_PERIODIC_MLP_HARMONIC_CAMPAIGN_LEADERBOARD_PATH,
        help="Completed campaign leaderboard used to add explicit-harmonic periodic MLP candidates.",
    )
    argument_parser.add_argument(
        "--curves-per-collage",
        type=int,
        default=4,
        help="Number of deterministic representative curves to draw per candidate collage.",
    )
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def normalize_surface_scope(surface_scope: str) -> str:

    """Normalize one human-facing report surface scope."""

    normalized_scope = str(surface_scope).strip().lower()
    assert normalized_scope in {"all", "forward", "backward", "global"}, (
        f"Unsupported report surface scope | {surface_scope}"
    )
    return normalized_scope


def candidate_configuration_matches_surface_scope(
    candidate_configuration: dict[str, Any],
    surface_scope: str,
) -> bool:

    """Return whether one candidate configuration belongs in one visual scope."""

    normalized_scope = normalize_surface_scope(surface_scope)
    if normalized_scope == "all":
        return True
    if normalized_scope == "global":
        return str(candidate_configuration.get("candidate_surface", "")).strip() == "global"
    return normalized_scope in reference_family_vs_feedforward_support.normalize_allowed_direction_list(
        candidate_configuration
    )


def filter_curve_record_list_by_surface_scope(
    curve_record_list: list[Any],
    surface_scope: str,
) -> list[Any]:

    """Filter curve records for one visual report surface scope."""

    normalized_scope = normalize_surface_scope(surface_scope)
    if normalized_scope in {"all", "global"}:
        return curve_record_list
    filtered_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == normalized_scope
    ]
    assert filtered_curve_record_list, f"No curve records available for surface scope | {surface_scope}"
    return filtered_curve_record_list


def filter_group_list_by_surface_scope(
    group_list: list[ReportCandidateGroup],
    candidate_lookup: dict[str, Any],
    surface_scope: str,
) -> list[ReportCandidateGroup]:

    """Keep only report groups that can be built for one surface scope."""

    normalized_scope = normalize_surface_scope(surface_scope)
    filtered_group_list: list[ReportCandidateGroup] = []
    for group in group_list:
        if normalized_scope in {"forward", "backward"} and group.selection_mode != normalized_scope:
            continue
        if normalized_scope == "global" and group.selection_mode not in {"global", "mixed"}:
            continue
        if all(candidate_id in candidate_lookup for candidate_id in group.candidate_id_list):
            filtered_group_list.append(group)
    assert filtered_group_list, f"No visual report groups available for surface scope | {surface_scope}"
    return filtered_group_list


def resolve_timestamped_output_paths(
    output_root: Path,
    report_topic_root: Path,
    report_date: str | None,
) -> tuple[str, Path, Path]:

    """Resolve timestamped output and report directories."""

    current_timestamp = datetime.now().astimezone()
    run_instance_id = (
        f"{current_timestamp.strftime('%Y-%m-%d-%H-%M-%S')}"
        "__track2_best_model_collage_report"
    )
    if report_date is None:
        report_date = current_timestamp.strftime("%Y-%m-%d")
    else:
        datetime.strptime(report_date, "%Y-%m-%d")

    output_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(output_root)
        / run_instance_id
    )
    report_directory = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(report_topic_root)
        / f"[{report_date}]"
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    report_directory.mkdir(parents=True, exist_ok=True)
    return run_instance_id, output_directory, report_directory


def build_wave1_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 1 candidate configurations."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for base_family_name in WAVE1_BASE_FAMILY_LIST:
        candidate_configuration_list.extend(
            [
                {
                    "candidate_id": f"{base_family_name}_global",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "global",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": ["forward", "backward"],
                },
                {
                    "candidate_id": f"{base_family_name}_fw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "Fw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_fw/latest_family_best.yaml",
                    "allowed_direction_list": ["forward"],
                },
                {
                    "candidate_id": f"{base_family_name}_bw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave1_current_registry",
                    "candidate_surface": "Bw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_bw/latest_family_best.yaml",
                    "allowed_direction_list": ["backward"],
                },
            ]
        )

    return candidate_configuration_list


def build_wave2_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 2.1 temporal candidate configurations."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for base_family_name in WAVE2_BASE_FAMILY_LIST:
        candidate_configuration_list.extend(
            [
                {
                    "candidate_id": f"{base_family_name}_global",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "global",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": ["forward", "backward"],
                },
                {
                    "candidate_id": f"{base_family_name}_fw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "Fw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_fw/latest_family_best.yaml",
                    "allowed_direction_list": ["forward"],
                },
                {
                    "candidate_id": f"{base_family_name}_bw",
                    "candidate_family": base_family_name,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2_temporal_entry_registry",
                    "candidate_surface": "Bw",
                    "family_registry_path": f"{registry_root_text}/{base_family_name}_bw/latest_family_best.yaml",
                    "allowed_direction_list": ["backward"],
                },
            ]
        )

    return candidate_configuration_list


def build_wave2c_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 2.3 residual harmonic temporal candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in WAVE2C_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, allowed_direction_list in [
            ("global", ["forward", "backward"]),
            ("Fw", ["forward"]),
            ("Bw", ["backward"]),
        ]:
            registry_family_name = surface_family_dictionary[candidate_surface]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "wave2c_residual_harmonic_temporal_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )

    return candidate_configuration_list


def build_track2f_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 3.1 offset-aware probe candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in TRACK2F_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, allowed_direction_list in [
            ("global", ["forward", "backward"]),
            ("Fw", ["forward"]),
            ("Bw", ["backward"]),
        ]:
            registry_family_name = surface_family_dictionary[candidate_surface]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "track2f_offset_aware_probe_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )

    return candidate_configuration_list


def build_track2f_bis_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 3.2 harmonic-offset probe candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in TRACK2F_BIS_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, registry_family_name in surface_family_dictionary.items():
            allowed_direction_list = ["forward", "backward"]
            if candidate_surface == "Fw":
                allowed_direction_list = ["forward"]
            if candidate_surface == "Bw":
                allowed_direction_list = ["backward"]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "track2f_bis_harmonic_offset_probe_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )
    return candidate_configuration_list


def build_track2g_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 3.3 curve-aware training candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in TRACK2G_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, registry_family_name in surface_family_dictionary.items():
            allowed_direction_list = ["forward", "backward"]
            if candidate_surface == "Fw":
                allowed_direction_list = ["forward"]
            if candidate_surface == "Bw":
                allowed_direction_list = ["backward"]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "track2g_curve_aware_training_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )
    return candidate_configuration_list


def build_track2h_registry_candidate_configuration_list(family_registry_root: Path) -> list[dict[str, Any]]:

    """Build current-registry Wave 4.1 robust-loss candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in TRACK2H_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, registry_family_name in surface_family_dictionary.items():
            allowed_direction_list = ["forward", "backward"]
            if candidate_surface == "Fw":
                allowed_direction_list = ["forward"]
            if candidate_surface == "Bw":
                allowed_direction_list = ["backward"]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "track2h_dispersion_aware_modeling_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )
    return candidate_configuration_list


def build_track2h_quantile_probabilistic_registry_candidate_configuration_list(
    family_registry_root: Path,
) -> list[dict[str, Any]]:

    """Build current-registry Wave 4.2 quantile/probabilistic candidates."""

    registry_root_text = shared_training_infrastructure.format_project_relative_path(
        shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_root)
    ).replace("\\", "/")
    candidate_configuration_list: list[dict[str, Any]] = []

    for family_configuration in TRACK2H_QUANTILE_PROBABILISTIC_FAMILY_CONFIGURATION_LIST:
        candidate_id_prefix = str(family_configuration["candidate_id_prefix"])
        candidate_family = str(family_configuration["candidate_family"])
        surface_family_dictionary = {
            "global": str(family_configuration["global_family"]),
            "Fw": str(family_configuration["fw_family"]),
            "Bw": str(family_configuration["bw_family"]),
        }
        for candidate_surface, registry_family_name in surface_family_dictionary.items():
            allowed_direction_list = ["forward", "backward"]
            if candidate_surface == "Fw":
                allowed_direction_list = ["forward"]
            if candidate_surface == "Bw":
                allowed_direction_list = ["backward"]
            candidate_configuration_list.append(
                {
                    "candidate_id": f"{candidate_id_prefix}_{candidate_surface}",
                    "candidate_family": candidate_family,
                    "candidate_kind": "wave1_registry_model",
                    "candidate_source_label": "track2h_quantile_probabilistic_registry",
                    "candidate_surface": candidate_surface,
                    "family_registry_path": f"{registry_root_text}/{registry_family_name}/latest_family_best.yaml",
                    "allowed_direction_list": allowed_direction_list,
                }
            )
    return candidate_configuration_list


def build_periodic_mlp_harmonic_campaign_candidate_configuration_list(
    campaign_leaderboard_path: Path,
    output_directory: Path,
) -> list[dict[str, Any]]:

    """Build explicit-harmonic periodic MLP candidate configs from one campaign."""

    resolved_leaderboard_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        campaign_leaderboard_path
    )
    if not resolved_leaderboard_path.exists():
        return []

    with resolved_leaderboard_path.open("r", encoding="utf-8") as input_stream:
        leaderboard = yaml.safe_load(input_stream)
    entry_list = list(leaderboard["entry_list"])
    model_family_to_candidate_metadata = {
        "periodic_mlp": {
            "candidate_id": "periodic_mlp_harmonic_global",
            "candidate_surface": "global",
            "allowed_direction_list": ["forward", "backward"],
        },
        "periodic_mlp_fw": {
            "candidate_id": "periodic_mlp_harmonic_fw",
            "candidate_surface": "Fw",
            "allowed_direction_list": ["forward"],
        },
        "periodic_mlp_bw": {
            "candidate_id": "periodic_mlp_harmonic_bw",
            "candidate_surface": "Bw",
            "allowed_direction_list": ["backward"],
        },
    }
    snapshot_directory = output_directory / "registry_snapshots" / "periodic_mlp_harmonic_campaign"
    snapshot_directory.mkdir(parents=True, exist_ok=True)
    candidate_configuration_list: list[dict[str, Any]] = []

    for model_family, candidate_metadata in model_family_to_candidate_metadata.items():
        matching_entry_list = [
            entry
            for entry in entry_list
            if str(entry["model_family"]).strip() == model_family
        ]
        if not matching_entry_list:
            continue

        best_entry = min(
            matching_entry_list,
            key=lambda entry: (
                float(entry["test_mae"]),
                float(entry["test_rmse"]),
                float(entry["val_mae"]),
                int(entry["trainable_parameter_count"]),
            ),
        )
        snapshot_path = snapshot_directory / f"{candidate_metadata['candidate_id']}.yaml"
        shared_training_infrastructure.save_yaml_snapshot(
            {
                "schema_version": 1,
                "source_campaign_leaderboard_path": shared_training_infrastructure.format_project_relative_path(
                    resolved_leaderboard_path
                ),
                "best_entry": best_entry,
            },
            snapshot_path,
        )
        candidate_configuration_list.append(
            {
                "candidate_id": candidate_metadata["candidate_id"],
                "candidate_family": "periodic_mlp_harmonic",
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": "wave1_periodic_mlp_harmonic_campaign",
                "candidate_surface": candidate_metadata["candidate_surface"],
                "family_registry_path": shared_training_infrastructure.format_project_relative_path(
                    snapshot_path
                ).replace("\\", "/"),
                "allowed_direction_list": candidate_metadata["allowed_direction_list"],
            }
        )

    return candidate_configuration_list


def resolve_report_candidate_configuration_list(
    training_config: dict[str, Any],
    family_registry_root: Path,
    periodic_mlp_harmonic_campaign_leaderboard_path: Path,
    output_directory: Path,
) -> list[dict[str, Any]]:

    """Resolve the selected TE curve-verification report candidates."""

    all_candidate_configuration_list = (
        reference_family_vs_feedforward_support.resolve_track2_candidate_configuration_list(training_config)
    )
    comparison_mode = str(
        training_config.get("comparison", {}).get(
            "comparison_mode",
            "",
        )
    ).strip()
    if comparison_mode.startswith("wave52r_"):
        return all_candidate_configuration_list

    wanted_reference_candidate_id_set = set(FORWARD_REFERENCE_CANDIDATE_ID_LIST + BACKWARD_REFERENCE_CANDIDATE_ID_LIST)
    reference_candidate_configuration_list = [
        candidate_configuration
        for candidate_configuration in all_candidate_configuration_list
        if str(candidate_configuration["candidate_id"]) in wanted_reference_candidate_id_set
    ]
    assert len(reference_candidate_configuration_list) == len(wanted_reference_candidate_id_set), (
        "Could not resolve every requested TE Curve Verification Pipeline reference best candidate."
    )

    explicit_candidate_configuration_list = (
        reference_candidate_configuration_list
        + build_wave1_registry_candidate_configuration_list(family_registry_root)
        + build_wave2_registry_candidate_configuration_list(family_registry_root)
        + build_wave2c_registry_candidate_configuration_list(family_registry_root)
        + build_track2f_registry_candidate_configuration_list(family_registry_root)
        + build_track2f_bis_registry_candidate_configuration_list(family_registry_root)
        + build_track2g_registry_candidate_configuration_list(family_registry_root)
        + build_track2h_registry_candidate_configuration_list(family_registry_root)
        + build_track2h_quantile_probabilistic_registry_candidate_configuration_list(family_registry_root)
        + build_periodic_mlp_harmonic_campaign_candidate_configuration_list(
            periodic_mlp_harmonic_campaign_leaderboard_path,
            output_directory,
        )
    )
    explicit_candidate_id_set = {
        str(candidate_configuration["candidate_id"])
        for candidate_configuration in explicit_candidate_configuration_list
    }
    auto_registry_candidate_configuration_list = [
        candidate_configuration
        for candidate_configuration in all_candidate_configuration_list
        if str(candidate_configuration.get("candidate_kind", "")).strip() == "wave1_registry_model"
        and str(candidate_configuration["candidate_id"]) not in explicit_candidate_id_set
    ]

    return explicit_candidate_configuration_list + auto_registry_candidate_configuration_list


def format_auto_registry_group_title(source_label: str) -> str:

    """Format a registry source label into a readable report group title."""

    if source_label in CANONICAL_SOURCE_TITLE_DICTIONARY:
        return CANONICAL_SOURCE_TITLE_DICTIONARY[source_label]

    acronym_dictionary = {
        "rcim": "RCIM",
        "mlp": "MLP",
        "gru": "GRU",
        "lstm": "LSTM",
        "pinn": "PINN",
        "pinns": "PINNs",
        "te": "TE",
    }
    title_part_list: list[str] = []
    for raw_part in str(source_label).replace("-", "_").split("_"):
        if not raw_part:
            continue
        lowered_part = raw_part.lower()
        if lowered_part in acronym_dictionary:
            title_part_list.append(acronym_dictionary[lowered_part])
        elif lowered_part.startswith("track") and lowered_part[5:].isdigit():
            title_part_list.append(f"Track {lowered_part[5:]}")
        elif lowered_part.startswith("wave") and lowered_part[4:].isdigit():
            title_part_list.append(f"Wave {lowered_part[4:]}")
        else:
            title_part_list.append(lowered_part.capitalize())
    return " ".join(title_part_list)


def format_canonical_source_label(source_label: str) -> str:

    """Return the canonical reader-facing source label for a candidate."""

    return CANONICAL_SOURCE_LABEL_DICTIONARY.get(source_label, source_label)


def format_canonical_candidate_family(candidate_family: str) -> str:

    """Return the canonical reader-facing candidate family."""

    return CANONICAL_MODEL_FAMILY_NAME_DICTIONARY.get(candidate_family, candidate_family)


def format_canonical_candidate_id(candidate_id: str) -> str:

    """Return the canonical reader-facing candidate id."""

    for legacy_suffix, canonical_suffix in CANONICAL_SURFACE_SUFFIX_DICTIONARY.items():
        suffix_text = f"_{legacy_suffix}"
        if candidate_id.endswith(suffix_text):
            candidate_base = candidate_id[: -len(suffix_text)]
            canonical_base = format_canonical_candidate_family(candidate_base)
            return f"{canonical_base}_{canonical_suffix}"

    return format_canonical_candidate_family(candidate_id)


def build_candidate_id_list_by_surface(
    source_candidate_configuration_list: list[dict[str, Any]],
    surface_label: str,
) -> list[str]:

    """Build a stable candidate-id list for one source and candidate surface."""

    return [
        str(candidate_configuration["candidate_id"])
        for candidate_configuration in source_candidate_configuration_list
        if str(candidate_configuration.get("candidate_surface", "")).strip() == surface_label
    ]


def append_auto_registry_group_list(
    group_list: list[ReportCandidateGroup],
    candidate_configuration_list: list[dict[str, Any]],
) -> list[ReportCandidateGroup]:

    """Append matrix-discovered registry groups that are not explicitly curated."""

    covered_source_label_set: set[str] = set()
    candidate_source_lookup = {
        str(candidate_configuration["candidate_id"]): str(candidate_configuration.get("candidate_source_label", "")).strip()
        for candidate_configuration in candidate_configuration_list
    }
    for group in group_list:
        for candidate_id in group.candidate_id_list:
            source_label = candidate_source_lookup.get(candidate_id)
            if source_label:
                covered_source_label_set.add(source_label)

    source_candidate_dictionary: dict[str, list[dict[str, Any]]] = {}
    for candidate_configuration in candidate_configuration_list:
        source_label = str(candidate_configuration.get("candidate_source_label", "")).strip()
        if not source_label or source_label in covered_source_label_set:
            continue
        source_candidate_dictionary.setdefault(source_label, []).append(candidate_configuration)

    sorted_source_item_list = sorted(
        source_candidate_dictionary.items(),
        key=lambda item: (
            CANONICAL_SOURCE_WAVE_ORDER_DICTIONARY.get(item[0], 999),
            format_canonical_source_label(item[0]),
        ),
    )
    for source_label, source_candidate_configuration_list in sorted_source_item_list:
        title_label = format_auto_registry_group_title(source_label)
        source_fragment = sanitize_filename_fragment(format_canonical_source_label(source_label))
        for surface_label, selection_mode, direction_title in [
            ("Fw", "forward", "Forward"),
            ("Bw", "backward", "Backward"),
            ("global", "mixed", "Global"),
        ]:
            candidate_id_list = build_candidate_id_list_by_surface(
                source_candidate_configuration_list,
                surface_label,
            )
            if not candidate_id_list:
                continue
            group_list.append(
                ReportCandidateGroup(
                    group_id=f"auto_{selection_mode}_{source_fragment}",
                    group_title=f"{direction_title} {title_label} Models",
                    candidate_id_list=candidate_id_list,
                    selection_mode=selection_mode,
                )
            )

    return group_list


def build_report_group_list(
    candidate_configuration_list: list[dict[str, Any]],
) -> list[ReportCandidateGroup]:

    """Build the ordered report groups."""

    wave1_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_forward_candidate_id_list.append("periodic_mlp_harmonic_fw")
    wave1_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_backward_candidate_id_list.append("periodic_mlp_harmonic_bw")
    wave1_global_candidate_id_list = [f"{family_name}_global" for family_name in WAVE1_BASE_FAMILY_LIST]
    wave1_global_candidate_id_list.append("periodic_mlp_harmonic_global")
    wave2_forward_candidate_id_list = [f"{family_name}_fw" for family_name in WAVE2_BASE_FAMILY_LIST]
    wave2_backward_candidate_id_list = [f"{family_name}_bw" for family_name in WAVE2_BASE_FAMILY_LIST]
    wave2_global_candidate_id_list = [f"{family_name}_global" for family_name in WAVE2_BASE_FAMILY_LIST]
    wave2c_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in WAVE2C_FAMILY_CONFIGURATION_LIST
    ]
    wave2c_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in WAVE2C_FAMILY_CONFIGURATION_LIST
    ]
    wave2c_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in WAVE2C_FAMILY_CONFIGURATION_LIST
    ]
    track2f_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in TRACK2F_FAMILY_CONFIGURATION_LIST
    ]
    track2f_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in TRACK2F_FAMILY_CONFIGURATION_LIST
    ]
    track2f_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in TRACK2F_FAMILY_CONFIGURATION_LIST
    ]
    track2f_bis_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in TRACK2F_BIS_FAMILY_CONFIGURATION_LIST
    ]
    track2f_bis_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in TRACK2F_BIS_FAMILY_CONFIGURATION_LIST
    ]
    track2f_bis_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in TRACK2F_BIS_FAMILY_CONFIGURATION_LIST
    ]
    track2g_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in TRACK2G_FAMILY_CONFIGURATION_LIST
    ]
    track2g_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in TRACK2G_FAMILY_CONFIGURATION_LIST
    ]
    track2g_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in TRACK2G_FAMILY_CONFIGURATION_LIST
    ]
    track2h_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in TRACK2H_FAMILY_CONFIGURATION_LIST
    ]
    track2h_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in TRACK2H_FAMILY_CONFIGURATION_LIST
    ]
    track2h_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in TRACK2H_FAMILY_CONFIGURATION_LIST
    ]
    track2h_quantile_probabilistic_forward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Fw"
        for family_configuration in TRACK2H_QUANTILE_PROBABILISTIC_FAMILY_CONFIGURATION_LIST
    ]
    track2h_quantile_probabilistic_backward_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_Bw"
        for family_configuration in TRACK2H_QUANTILE_PROBABILISTIC_FAMILY_CONFIGURATION_LIST
    ]
    track2h_quantile_probabilistic_global_candidate_id_list = [
        f"{family_configuration['candidate_id_prefix']}_global"
        for family_configuration in TRACK2H_QUANTILE_PROBABILISTIC_FAMILY_CONFIGURATION_LIST
    ]

    group_list = [
        ReportCandidateGroup(
            group_id="forward_reference",
            group_title="Forward Reference Best Models",
            candidate_id_list=FORWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_reference",
            group_title="Backward Reference Best Models",
            candidate_id_list=BACKWARD_REFERENCE_CANDIDATE_ID_LIST,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="forward_wave1",
            group_title="Forward Wave 1 Family Best Models",
            candidate_id_list=wave1_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave1",
            group_title="Backward Wave 1 Family Best Models",
            candidate_id_list=wave1_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave1",
            group_title="Global Wave 1 Family Best Models",
            candidate_id_list=wave1_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave2",
            group_title="Forward Wave 2.1 Temporal Family Best Models",
            candidate_id_list=wave2_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave2",
            group_title="Backward Wave 2.1 Temporal Family Best Models",
            candidate_id_list=wave2_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave2",
            group_title="Global Wave 2.1 Temporal Family Best Models",
            candidate_id_list=wave2_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave2c",
            group_title="Forward Wave 2.3 Residual Harmonic Temporal Models",
            candidate_id_list=wave2c_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave2c",
            group_title="Backward Wave 2.3 Residual Harmonic Temporal Models",
            candidate_id_list=wave2c_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave2c",
            group_title="Global Wave 2.3 Residual Harmonic Temporal Models",
            candidate_id_list=wave2c_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave3_1",
            group_title="Forward Wave 3.1 Offset-Aware Probe Models",
            candidate_id_list=track2f_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave3_1",
            group_title="Backward Wave 3.1 Offset-Aware Probe Models",
            candidate_id_list=track2f_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave3_1",
            group_title="Global Wave 3.1 Offset-Aware Probe Models",
            candidate_id_list=track2f_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave3_2",
            group_title="Forward Wave 3.2 Harmonic-Offset Probe Models",
            candidate_id_list=track2f_bis_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave3_2",
            group_title="Backward Wave 3.2 Harmonic-Offset Probe Models",
            candidate_id_list=track2f_bis_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave3_2",
            group_title="Global Wave 3.2 Harmonic-Offset Probe Models",
            candidate_id_list=track2f_bis_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave3_3",
            group_title="Forward Wave 3.3 Curve-Aware Training Models",
            candidate_id_list=track2g_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave3_3",
            group_title="Backward Wave 3.3 Curve-Aware Training Models",
            candidate_id_list=track2g_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave3_3",
            group_title="Global Wave 3.3 Curve-Aware Training Models",
            candidate_id_list=track2g_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave4_1",
            group_title="Forward Wave 4.1 Robust-Loss Models",
            candidate_id_list=track2h_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave4_1",
            group_title="Backward Wave 4.1 Robust-Loss Models",
            candidate_id_list=track2h_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave4_1",
            group_title="Global Wave 4.1 Robust-Loss Models",
            candidate_id_list=track2h_global_candidate_id_list,
            selection_mode="mixed",
        ),
        ReportCandidateGroup(
            group_id="forward_wave4_2",
            group_title="Forward Wave 4.2 Quantile Probabilistic Models",
            candidate_id_list=track2h_quantile_probabilistic_forward_candidate_id_list,
            selection_mode="forward",
        ),
        ReportCandidateGroup(
            group_id="backward_wave4_2",
            group_title="Backward Wave 4.2 Quantile Probabilistic Models",
            candidate_id_list=track2h_quantile_probabilistic_backward_candidate_id_list,
            selection_mode="backward",
        ),
        ReportCandidateGroup(
            group_id="global_wave4_2",
            group_title="Global Wave 4.2 Quantile Probabilistic Models",
            candidate_id_list=track2h_quantile_probabilistic_global_candidate_id_list,
            selection_mode="mixed",
        ),
    ]
    return append_auto_registry_group_list(group_list, candidate_configuration_list)


def sort_curve_entry_list(entry_list: list[dict[str, Any]]) -> list[dict[str, Any]]:

    """Sort curve entries into a stable visual-inspection order."""

    return sorted(
        entry_list,
        key=lambda entry: (
            str(entry["direction_label"]),
            float(entry["oil_temperature_deg"]),
            float(entry["torque_nm"]),
            float(entry["speed_rpm"]),
            str(entry["source_file_path"]),
        ),
    )


def select_spread_entries(entry_list: list[dict[str, Any]], requested_count: int) -> list[dict[str, Any]]:

    """Select entries spread across the available sorted curve list."""

    sorted_entry_list = sort_curve_entry_list(entry_list)
    if len(sorted_entry_list) <= requested_count:
        return sorted_entry_list
    selected_position_array = np.linspace(0, len(sorted_entry_list) - 1, requested_count)
    selected_index_list = sorted({int(round(position)) for position in selected_position_array})
    while len(selected_index_list) < requested_count:
        selected_index_list.append(len(selected_index_list))
        selected_index_list = sorted(set(selected_index_list))
    return [sorted_entry_list[index_value] for index_value in selected_index_list[:requested_count]]


def select_candidate_collage_entries(
    candidate_entry_list: list[dict[str, Any]],
    selection_mode: str,
    curves_per_collage: int,
) -> list[dict[str, Any]]:

    """Select the representative entries for one candidate collage."""

    assert curves_per_collage == 4, "The current report layout expects four curves per collage."
    if selection_mode != "mixed":
        direction_entry_list = [
            entry
            for entry in candidate_entry_list
            if str(entry["direction_label"]).strip().lower() == selection_mode
        ]
        return select_spread_entries(direction_entry_list, curves_per_collage)

    forward_entry_list = [
        entry
        for entry in candidate_entry_list
        if str(entry["direction_label"]).strip().lower() == "forward"
    ]
    backward_entry_list = [
        entry
        for entry in candidate_entry_list
        if str(entry["direction_label"]).strip().lower() == "backward"
    ]
    return select_spread_entries(forward_entry_list, 2) + select_spread_entries(backward_entry_list, 2)


def sanitize_filename_fragment(raw_value: str) -> str:

    """Sanitize one filename fragment."""

    return shared_training_infrastructure.sanitize_name(str(raw_value).strip().lower())


def save_candidate_collage(
    collage_path: Path,
    candidate_id: str,
    selected_entry_list: list[dict[str, Any]],
) -> None:

    """Save one four-curve collage for a candidate."""

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    collage_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis_array = plt.subplots(2, 2, figsize=(12.0, 7.0), sharex=False, sharey=False)
    flattened_axis_list = list(axis_array.reshape(-1))

    for axis, per_candidate_entry in zip(flattened_axis_list, selected_entry_list):
        angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float32)
        truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float32)
        predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float32)
        track2_circular_plotting.plot_circular_angle_curve(
            axis,
            angular_position_deg,
            truth_curve_deg,
            label="Measured TE",
            linewidth=1.2,
            color="#4a4a4a",
        )
        track2_circular_plotting.plot_circular_angle_curve(
            axis,
            angular_position_deg,
            predicted_curve_deg,
            label=candidate_id,
            linewidth=1.2,
            color="#1f77b4",
        )
        axis.set_title(
            (
                f"{per_candidate_entry['direction_label']} | "
                f"{float(per_candidate_entry['speed_rpm']):.0f} rpm | "
                f"{float(per_candidate_entry['torque_nm']):.0f} Nm | "
                f"{float(per_candidate_entry['oil_temperature_deg']):.0f} C"
            ),
            fontsize=9,
        )
        axis.set_xlabel("Angular Position [deg]", fontsize=8)
        axis.set_ylabel("TE [deg]", fontsize=8)
        axis.grid(True, alpha=0.28)
        axis.tick_params(labelsize=8)

    for empty_axis in flattened_axis_list[len(selected_entry_list):]:
        empty_axis.axis("off")

    flattened_axis_list[0].legend(loc="best", fontsize=8)
    figure.suptitle(candidate_id, fontsize=13)
    figure.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    figure.savefig(collage_path, dpi=180)
    plt.close(figure)


def build_relative_markdown_path(target_path: Path, markdown_directory: Path) -> str:

    """Build a Markdown-safe relative path from a report to an artifact."""

    relative_path = os.path.relpath(target_path.resolve(), markdown_directory.resolve())
    return relative_path.replace("\\", "/")


def build_compact_report_asset_fragment(identifier_text: str) -> str:

    """Build a deterministic short filesystem fragment for report assets."""

    sanitized_identifier = sanitize_filename_fragment(identifier_text)
    if len(sanitized_identifier) <= MAX_REPORT_ASSET_FRAGMENT_LENGTH:
        return sanitized_identifier

    digest_text = hashlib.sha1(sanitized_identifier.encode("utf-8")).hexdigest()[:10]
    token_alias_dictionary = {
        "auto": "a",
        "forward": "fw",
        "backward": "bw",
        "mixed": "mix",
        "global": "glb",
        "harmonic": "harm",
        "prior": "pri",
        "residual": "res",
        "registry": "reg",
    }
    compact_token_list: list[str] = []
    for token in sanitized_identifier.split("_"):
        if not token:
            continue
        lowered_token = token.lower()
        if lowered_token in token_alias_dictionary:
            compact_token_list.append(token_alias_dictionary[lowered_token])
        elif lowered_token.startswith("wave") and lowered_token[4:].isdigit():
            compact_token_list.append(f"w{lowered_token[4:]}")
        elif lowered_token.startswith("track") and lowered_token[5:].isdigit():
            compact_token_list.append(f"t{lowered_token[5:]}")
        else:
            compact_token_list.append(lowered_token[:4])

    suffix_text = f"_{digest_text}"
    compact_identifier = "_".join(compact_token_list)
    maximum_prefix_length = MAX_REPORT_ASSET_FRAGMENT_LENGTH - len(suffix_text)
    compact_identifier = compact_identifier[:maximum_prefix_length].rstrip("_")
    return f"{compact_identifier}{suffix_text}"


def save_candidate_metrics_csv(
    csv_path: Path,
    candidate_summary_list: list[dict[str, Any]],
) -> None:

    """Save compact metrics for every collaged candidate."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "group_id",
                "canonical_candidate_id",
                "legacy_candidate_id",
                "canonical_candidate_family",
                "legacy_candidate_family",
                "canonical_candidate_source_label",
                "legacy_candidate_source_label",
                "candidate_surface",
                "direction_scope",
                "curve_mae_deg",
                "curve_rmse_deg",
                "mean_percentage_error_pct",
                "p95_mean_percentage_error_pct",
                "collage_path",
            ]
        )
        for candidate_summary in candidate_summary_list:
            metric_dictionary = candidate_summary["metrics"]
            writer.writerow(
                [
                    candidate_summary["group_id"],
                    candidate_summary["canonical_candidate_id"],
                    candidate_summary["legacy_candidate_id"],
                    candidate_summary["canonical_candidate_family"],
                    candidate_summary["legacy_candidate_family"],
                    candidate_summary["canonical_candidate_source_label"],
                    candidate_summary["legacy_candidate_source_label"],
                    candidate_summary["candidate_surface"],
                    candidate_summary["direction_scope"],
                    f"{metric_dictionary['mae']:.9f}",
                    f"{metric_dictionary['rmse']:.9f}",
                    f"{metric_dictionary['mean_percentage_error_pct']:.9f}",
                    f"{metric_dictionary['p95_mean_percentage_error_pct']:.9f}",
                    candidate_summary["collage_path"],
                ]
            )


def append_candidate_table(
    report_line_list: list[str],
    group_summary_list: list[dict[str, Any]],
) -> None:

    """Append one compact candidate table."""

    report_line_list.extend(
        [
            "| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |",
            "| --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for candidate_summary in group_summary_list:
        metric_dictionary = candidate_summary["metrics"]
        report_line_list.append(
            f"| `{candidate_summary['canonical_candidate_id']}` | "
            f"`{candidate_summary['canonical_candidate_source_label']}` | "
            f"{candidate_summary['candidate_surface']} | "
            f"{metric_dictionary['mae']:.6f} | "
            f"{metric_dictionary['rmse']:.6f} | "
            f"{metric_dictionary['mean_percentage_error_pct']:.3f} |"
        )


def get_gallery_section_title(group_title: str, chunk_index: int) -> str:

    """Return a stable gallery section title for two-model PDF pages."""

    base_title = f"Collage Gallery - {group_title}"
    if chunk_index == 0:
        return base_title
    if chunk_index == 1:
        return f"{base_title} Continued"
    return f"{base_title} Continued {chunk_index}"


def build_report_markdown(
    report_path: Path,
    output_directory: Path,
    candidate_summary_list: list[dict[str, Any]],
    group_list: list[ReportCandidateGroup],
    metrics_csv_path: Path,
    validation_summary_path: Path,
) -> str:

    """Build the Markdown report body."""

    report_line_list = [
        "# TE Curve Verification Pipeline Best Model Collage Report",
        "",
        "## Overview",
        "",
        "This report compares representative `TE Curve Verification Pipeline` TE-curve predictions for",
        "the current best reference, RCIM Model-Bank Reproduction, Wave 1 directional, and Wave 1",
        "global models. Each model is shown as one four-image collage so local",
        "oscillation tracking can be inspected directly.",
        "",
        "## Scope",
        "",
        "- each collage contains four deterministic held-out test curves;",
        "- forward models are shown on forward curves only;",
        "- backward models are shown on backward curves only;",
        "- global Wave 1 models are shown on two forward and two backward curves;",
        "- `Measured TE` uses the same line width as predictions and a dark-gray",
        "  color for balanced visual comparison.",
        "",
        "## Metrics Summary",
        "",
    ]

    candidate_summary_by_group = {
        group.group_id: [
            candidate_summary
            for candidate_summary in candidate_summary_list
            if candidate_summary["group_id"] == group.group_id
        ]
        for group in group_list
    }

    for group in group_list:
        report_line_list.extend(
            [
                f"### {group.group_title}",
                "",
            ]
        )
        append_candidate_table(report_line_list, candidate_summary_by_group[group.group_id])
        report_line_list.append("")

    for group in group_list:
        group_summary_list = candidate_summary_by_group[group.group_id]
        for chunk_start_index in range(0, len(group_summary_list), 2):
            chunk_index = chunk_start_index // 2
            section_title = get_gallery_section_title(group.group_title, chunk_index)
            report_line_list.extend([f"## {section_title}", ""])
            for candidate_summary in group_summary_list[chunk_start_index : chunk_start_index + 2]:
                report_line_list.extend(
                    [
                        f"{candidate_summary['canonical_candidate_id']}:",
                        "",
                        (
                            f"![{candidate_summary['canonical_candidate_id']} TE Curve Verification Pipeline collage]"
                            f"({candidate_summary['collage_markdown_path']})"
                        ),
                        "",
                    ]
                )

    report_line_list.extend(["## Output Artifacts", ""])

    report_line_list.extend(
        [
            f"- output directory: `{shared_training_infrastructure.format_project_relative_path(output_directory)}`;",
            f"- summary YAML: `{shared_training_infrastructure.format_project_relative_path(validation_summary_path)}`;",
            f"- metrics CSV: `{shared_training_infrastructure.format_project_relative_path(metrics_csv_path)}`;",
            f"- report Markdown: `{shared_training_infrastructure.format_project_relative_path(report_path)}`.",
        ]
    )

    return "\n".join(report_line_list) + "\n"


def run_track2_best_model_collage_report(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the full TE Curve Verification Pipeline best-model collage report generation."""

    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(arguments)
    )
    assert int(arguments.curves_per_collage) == 4, "This report requires exactly four curves per collage."

    run_instance_id, output_directory, report_directory = resolve_timestamped_output_paths(
        arguments.output_root,
        arguments.report_topic_root,
        arguments.report_date,
    )
    report_path = report_directory / REPORT_FILENAME
    metrics_csv_path = output_directory / METRICS_FILENAME
    validation_summary_path = output_directory / SUMMARY_FILENAME
    report_asset_root = report_path.parent / "assets"
    if report_asset_root.exists():
        shutil.rmtree(report_asset_root)

    training_config = shared_training_infrastructure.apply_dataset_override(
        shared_training_infrastructure.load_training_config(arguments.config_path),
        arguments.dataset,
    )
    selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
    curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    curve_record_list = filter_curve_record_list_by_surface_scope(
        curve_record_list,
        arguments.surface_scope,
    )
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

    candidate_configuration_list = resolve_report_candidate_configuration_list(
        training_config,
        arguments.family_registry_root,
        arguments.periodic_mlp_harmonic_campaign_leaderboard_path,
        output_directory,
    )
    candidate_configuration_list = [
        candidate_configuration
        for candidate_configuration in candidate_configuration_list
        if candidate_configuration_matches_surface_scope(candidate_configuration, arguments.surface_scope)
    ]
    requested_candidate_id_set = {
        str(candidate_id).strip()
        for candidate_id in arguments.candidate_id_list
        if str(candidate_id).strip()
    }
    if requested_candidate_id_set:
        candidate_configuration_list = [
            candidate_configuration
            for candidate_configuration in candidate_configuration_list
            if str(candidate_configuration["candidate_id"])
            in requested_candidate_id_set
        ]
        resolved_candidate_id_set = {
            str(candidate_configuration["candidate_id"])
            for candidate_configuration in candidate_configuration_list
        }
        assert resolved_candidate_id_set == requested_candidate_id_set, (
            "Could not resolve every requested collage candidate | "
            f"missing={sorted(requested_candidate_id_set - resolved_candidate_id_set)}"
        )
    assert candidate_configuration_list, (
        "No collage candidates available for requested surface scope | "
        f"surface_scope={arguments.surface_scope}"
    )
    candidate_list = [
        reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
        for candidate_configuration in tqdm(
            candidate_configuration_list,
            desc="Load collage candidates",
            unit="candidate",
            ascii=True,
            ncols=80,
            dynamic_ncols=False,
        )
    ]
    candidate_lookup = {
        candidate.candidate_id: candidate
        for candidate in candidate_list
    }

    per_candidate_entry_list: list[dict[str, Any]] = []
    for candidate in tqdm(
        candidate_list,
        desc="Evaluate collage candidates",
        unit="candidate",
        ascii=True,
        ncols=80,
        dynamic_ncols=False,
    ):
        candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
            candidate,
            curve_record_list,
            percentage_error_denominator,
            include_curve_payload=False,
        )
        per_candidate_entry_list.extend(candidate_entry_list)

    grouped_entry_dictionary: dict[str, list[dict[str, Any]]] = {}
    for per_candidate_entry in per_candidate_entry_list:
        grouped_entry_dictionary.setdefault(str(per_candidate_entry["candidate_id"]), []).append(per_candidate_entry)

    candidate_metric_summary = reference_family_vs_feedforward_support.build_candidate_metric_summary(
        per_candidate_entry_list
    )
    direction_metric_summary = reference_family_vs_feedforward_support.build_generic_group_metric_summary(
        per_candidate_entry_list,
        "direction_label",
    )
    group_list = filter_group_list_by_surface_scope(
        build_report_group_list(candidate_configuration_list),
        candidate_lookup,
        arguments.surface_scope,
    )
    candidate_summary_list: list[dict[str, Any]] = []

    def build_curve_key(entry_dictionary: dict[str, Any]) -> tuple[str, str]:
        return (
            str(entry_dictionary["source_file_path"]),
            str(entry_dictionary["direction_label"]),
        )

    curve_record_lookup = {
        (
            shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
            str(curve_record.direction_label),
        ): curve_record
        for curve_record in curve_record_list
    }

    for group in tqdm(
        group_list,
        desc="Build collage groups",
        unit="group",
        ascii=True,
        ncols=80,
        dynamic_ncols=False,
    ):
        for candidate_id in tqdm(
            group.candidate_id_list,
            desc="Collage group",
            unit="candidate",
            leave=False,
            ascii=True,
            ncols=80,
            dynamic_ncols=False,
        ):
            candidate = candidate_lookup[candidate_id]
            canonical_candidate_id = format_canonical_candidate_id(candidate_id)
            canonical_candidate_family = format_canonical_candidate_family(candidate.candidate_family)
            canonical_source_label = format_canonical_source_label(candidate.candidate_source_label)
            selected_entry_list = select_candidate_collage_entries(
                grouped_entry_dictionary[candidate_id],
                group.selection_mode,
                int(arguments.curves_per_collage),
            )
            selected_curve_record_list = [
                curve_record_lookup[build_curve_key(selected_entry)]
                for selected_entry in selected_entry_list
            ]
            selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
                candidate,
                selected_curve_record_list,
                percentage_error_denominator,
                include_curve_payload=True,
            )
            selected_payload_lookup = {
                build_curve_key(selected_payload_entry): selected_payload_entry
                for selected_payload_entry in selected_payload_entry_list
            }
            selected_entry_list = [
                selected_payload_lookup[build_curve_key(selected_entry)]
                for selected_entry in selected_entry_list
            ]
            collage_path = (
                output_directory
                / "collages"
                / group.group_id
                / f"{sanitize_filename_fragment(canonical_candidate_id)}.png"
            )
            report_asset_path = (
                report_asset_root
                / build_compact_report_asset_fragment(group.group_id)
                / f"{sanitize_filename_fragment(canonical_candidate_id)}.png"
            )
            save_candidate_collage(collage_path, canonical_candidate_id, selected_entry_list)
            report_asset_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(collage_path, report_asset_path)

            if group.selection_mode in {"forward", "backward"}:
                metric_dictionary = direction_metric_summary[group.selection_mode][candidate_id]
            else:
                metric_dictionary = candidate_metric_summary[candidate_id]

            candidate_summary_list.append(
                {
                    "group_id": group.group_id,
                    "candidate_id": canonical_candidate_id,
                    "canonical_candidate_id": canonical_candidate_id,
                    "legacy_candidate_id": candidate_id,
                    "candidate_family": canonical_candidate_family,
                    "canonical_candidate_family": canonical_candidate_family,
                    "legacy_candidate_family": candidate.candidate_family,
                    "candidate_kind": candidate.candidate_kind,
                    "candidate_source_label": canonical_source_label,
                    "canonical_candidate_source_label": canonical_source_label,
                    "legacy_candidate_source_label": candidate.candidate_source_label,
                    "candidate_surface": candidate.candidate_surface,
                    "direction_scope": group.selection_mode,
                    "allowed_direction_list": candidate.allowed_direction_list,
                    "source_path": shared_training_infrastructure.format_project_relative_path(
                        candidate.source_path
                    ),
                    "metrics": metric_dictionary,
                    "collage_path": shared_training_infrastructure.format_project_relative_path(collage_path),
                    "collage_markdown_path": build_relative_markdown_path(report_asset_path, report_path.parent),
                    "selected_curve_list": [
                        {
                            "source_file_path": entry["source_file_path"],
                            "direction_label": entry["direction_label"],
                            "speed_rpm": float(entry["speed_rpm"]),
                            "torque_nm": float(entry["torque_nm"]),
                            "oil_temperature_deg": float(entry["oil_temperature_deg"]),
                            "metrics": entry["metrics"],
                        }
                        for entry in selected_entry_list
                    ],
                }
            )

    save_candidate_metrics_csv(metrics_csv_path, candidate_summary_list)
    validation_summary = {
        "schema_version": 1,
        "run_instance_id": run_instance_id,
        "output_directory": shared_training_infrastructure.format_project_relative_path(output_directory),
        "report_path": shared_training_infrastructure.format_project_relative_path(report_path),
        "dataset": {
            "config_path": str(training_config["paths"]["dataset_config_path"]),
            "dataset_name": str(training_config.get("dataset", {}).get("name", "configured_default")),
            "dataset_root": shared_training_infrastructure.format_project_relative_path(dataset_root),
            "surface_scope": str(arguments.surface_scope),
            "curve_count": int(len(curve_record_list)),
            "selected_harmonic_list": selected_harmonic_list,
        },
        "candidate_count": int(len(candidate_summary_list)),
        "candidate_summary_list": candidate_summary_list,
        "metrics_csv_path": shared_training_infrastructure.format_project_relative_path(metrics_csv_path),
    }
    shared_training_infrastructure.save_yaml_snapshot(validation_summary, validation_summary_path)

    report_markdown = build_report_markdown(
        report_path,
        output_directory,
        candidate_summary_list,
        group_list,
        metrics_csv_path,
        validation_summary_path,
    )
    report_path.write_text(report_markdown, encoding="utf-8")
    return validation_summary


def main() -> None:

    """Run the command-line entry point."""

    validation_summary = run_track2_best_model_collage_report(parse_command_line_arguments())
    print(f"[DONE] TE Curve Verification Pipeline collage report: {validation_summary['report_path']}")
    print(f"[DONE] Artifacts: {validation_summary['output_directory']}")


if __name__ == "__main__":
    main()
