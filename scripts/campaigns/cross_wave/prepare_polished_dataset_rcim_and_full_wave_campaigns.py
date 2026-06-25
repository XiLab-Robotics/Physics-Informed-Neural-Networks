"""Prepare polished RCIM and full-wave retraining campaign packages."""

from __future__ import annotations

# Import Python Utilities
import os, sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(os.path.abspath(__file__)).parents[3]
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank import exact_paper_model_bank_support
from scripts.training import shared_training_infrastructure

TECHNICAL_DOCUMENT_PATH = (
    "doc/technical/2026-06/2026-06-22/"
    "2026-06-22-22-55-55_polished_rcim_and_full_wave_retraining_campaigns.md"
)
RCIM_CAMPAIGN_NAME = "polished_dataset_rcim_model_bank_reproduction_2026_06_22"
FULL_WAVE_CAMPAIGN_NAME = "polished_dataset_full_wave_retraining_2026_06_22"
RCIM_CAMPAIGN_ROOT = (
    "config/paper_reimplementation/rcim_ml_compensation/"
    "polished_dataset_rcim_model_bank_reproduction/campaigns/2026-06-22_polished_rcim_model_bank_reproduction"
)
FULL_WAVE_CAMPAIGN_ROOT = (
    "config/training/polished_dataset_retraining/campaigns/"
    "2026-06-22_polished_full_wave_retraining"
)
RCIM_PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/cross_wave/polished_dataset/"
    "2026-06-22-22-55-55_polished_rcim_model_bank_reproduction_campaign_plan_report.md"
)
FULL_WAVE_PLANNING_REPORT_PATH = (
    "doc/reports/campaign_plans/cross_wave/polished_dataset/"
    "2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md"
)
RCIM_LAUNCHER_PATH = "scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1"
FULL_WAVE_LAUNCHER_PATH = "scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.ps1"
RCIM_LAUNCHER_NOTE_PATH = "doc/scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.md"
FULL_WAVE_LAUNCHER_NOTE_PATH = "doc/scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.md"
ACTIVE_CAMPAIGN_STATE_PATH = "doc/running/active_training_campaign.yaml"
VALIDATOR_PATH = "scripts/campaigns/cross_wave/validate_polished_dataset_retraining_campaign_package.py"
POLISHED_DATASET_NAME = "polished_dataset"

SURFACE_CONFIGURATION = {
    "global": {
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
    },
    "fw": {
        "training_variant": "fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
    },
    "bw": {
        "training_variant": "bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
    },
}

FULL_WAVE_SOURCE_ENTRY_LIST = [
    ("tree", "global", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/01_tree_global.yaml"),
    ("tree", "fw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/02_tree_fw.yaml"),
    ("tree", "bw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/03_tree_bw.yaml"),
    ("residual_harmonic_mlp", "global", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/04_residual_harmonic_mlp_global.yaml"),
    ("residual_harmonic_mlp", "fw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/05_residual_harmonic_mlp_fw.yaml"),
    ("residual_harmonic_mlp", "bw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/06_residual_harmonic_mlp_bw.yaml"),
    ("feedforward", "global", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/07_feedforward_global.yaml"),
    ("feedforward", "fw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/08_feedforward_fw.yaml"),
    ("feedforward", "bw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/09_feedforward_bw.yaml"),
    ("periodic_mlp", "global", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/10_periodic_mlp_global.yaml"),
    ("periodic_mlp", "fw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/11_periodic_mlp_fw.yaml"),
    ("periodic_mlp", "bw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/12_periodic_mlp_bw.yaml"),
    ("harmonic_regression", "global", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/13_harmonic_regression_global.yaml"),
    ("harmonic_regression", "fw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/14_harmonic_regression_fw.yaml"),
    ("harmonic_regression", "bw", "config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue/15_harmonic_regression_bw.yaml"),
    ("periodic_mlp_harmonic", "global", "config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/01_periodic_mlp_global_rcim_sparse.yaml"),
    ("periodic_mlp_harmonic", "fw", "config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/04_periodic_mlp_fw_rcim_sparse.yaml"),
    ("periodic_mlp_harmonic", "bw", "config/training/wave1_periodic_mlp_explicit_harmonic_tracking/campaigns/2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign/queue/07_periodic_mlp_bw_rcim_sparse.yaml"),
    ("temporal_convolution", "global", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/01_temporal_convolution_global.yaml"),
    ("temporal_convolution", "fw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/02_temporal_convolution_fw.yaml"),
    ("temporal_convolution", "bw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/03_temporal_convolution_bw.yaml"),
    ("gru_sequence", "global", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/04_gru_sequence_global.yaml"),
    ("gru_sequence", "fw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/05_gru_sequence_fw.yaml"),
    ("gru_sequence", "bw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/06_gru_sequence_bw.yaml"),
    ("lstm_sequence", "global", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/07_lstm_sequence_global.yaml"),
    ("lstm_sequence", "fw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/08_lstm_sequence_fw.yaml"),
    ("lstm_sequence", "bw", "config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/09_lstm_sequence_bw.yaml"),
    ("periodic_temporal_convolution", "global", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/01_periodic_temporal_convolution_global.yaml"),
    ("periodic_temporal_convolution", "fw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/02_periodic_temporal_convolution_fw.yaml"),
    ("periodic_temporal_convolution", "bw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/03_periodic_temporal_convolution_bw.yaml"),
    ("periodic_gru_sequence", "global", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/04_periodic_gru_sequence_global.yaml"),
    ("periodic_gru_sequence", "fw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/05_periodic_gru_sequence_fw.yaml"),
    ("periodic_gru_sequence", "bw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/06_periodic_gru_sequence_bw.yaml"),
    ("periodic_lstm_sequence", "global", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/07_periodic_lstm_sequence_global.yaml"),
    ("periodic_lstm_sequence", "fw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/08_periodic_lstm_sequence_fw.yaml"),
    ("periodic_lstm_sequence", "bw", "config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/09_periodic_lstm_sequence_bw.yaml"),
]

for family_name in ["residual_harmonic_gru_sequence", "residual_harmonic_lstm_sequence"]:
    architecture_prefix = "gru" if "gru" in family_name else "lstm"
    for harmonic_profile, index_offset in [("sparse_rcim", 1), ("dense240", 4), ("dense360", 7)]:
        for surface_index, surface_name in enumerate(["global", "fw", "bw"]):
            file_index = index_offset + surface_index + (0 if architecture_prefix == "gru" else 9)
            source_stem = harmonic_profile.replace("dense", "dense_")
            canonical_family = f"{family_name}_{harmonic_profile}"
            FULL_WAVE_SOURCE_ENTRY_LIST.append(
                (
                    canonical_family,
                    surface_name,
                    "config/training/wave2c_residual_harmonic_temporal_hybrid/"
                    "campaigns/2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign/"
                    f"queue/{file_index:02d}_{family_name}_{source_stem}_{surface_name}.yaml",
                )
            )

FULL_WAVE_SOURCE_ENTRY_LIST.extend(
    [
        ("wave3_1_sequential_residual_offset_probe", "global", "config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/01_sequential_residual_offset_probe_global.yaml"),
        ("wave3_1_sequential_residual_offset_probe", "fw", "config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/02_sequential_residual_offset_probe_fw.yaml"),
        ("wave3_1_sequential_residual_offset_probe", "bw", "config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/03_sequential_residual_offset_probe_bw.yaml"),
        ("wave3_2_clean_sequential_residual_offset", "global", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/01_clean_sequential_residual_offset_control_global.yaml"),
        ("wave3_2_clean_sequential_residual_offset", "fw", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/02_clean_sequential_residual_offset_control_fw.yaml"),
        ("wave3_2_clean_sequential_residual_offset", "bw", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/03_clean_sequential_residual_offset_control_bw.yaml"),
        ("wave3_2_harmonic_residual_offset", "global", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/04_harmonic_residual_offset_probe_global.yaml"),
        ("wave3_2_harmonic_residual_offset", "fw", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/05_harmonic_residual_offset_probe_fw.yaml"),
        ("wave3_2_harmonic_residual_offset", "bw", "config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/06_harmonic_residual_offset_probe_bw.yaml"),
    ]
)

for family_name, file_prefix in [
    ("wave3_3_curve_aware_pointwise_control", "pointwise_control"),
    ("wave3_3_raw_centered_shape_curve_aware", "raw_centered_shape"),
    ("wave3_3_raw_offset_curve_aware", "raw_offset"),
    ("wave3_3_full_curve_composite", "full_curve_composite"),
    ("wave4_1_mae_robust_loss", "mae_robust"),
    ("wave4_1_smooth_l1_robust_loss", "smooth_l1_robust"),
    ("wave4_1_log_cosh_robust_loss", "log_cosh_robust"),
]:
    campaign_root = (
        "track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign"
        if family_name.startswith("wave3_3")
        else "track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign"
    )
    base_index = {
        "pointwise_control": 1,
        "raw_centered_shape": 4,
        "raw_offset": 7,
        "full_curve_composite": 10,
        "mae_robust": 1,
        "smooth_l1_robust": 4,
        "log_cosh_robust": 7,
    }[file_prefix]
    for surface_index, surface_name in enumerate(["global", "fw", "bw"]):
        FULL_WAVE_SOURCE_ENTRY_LIST.append(
            (
                family_name,
                surface_name,
                f"config/training/{campaign_root}/queue/{base_index + surface_index:02d}_{file_prefix}_{surface_name}.yaml",
            )
        )

for family_name, file_prefix, campaign_root, base_index in [
    ("wave4_2_quantile_p10_p50_p90", "quantile_p10_p50_p90", "track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign", 1),
    ("wave4_2_gaussian_nll", "gaussian_nll", "track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign", 4),
    ("wave4_3_mixture_density_k2", "mdn_k2", "track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign", 1),
    ("wave4_3_mixture_density_k3", "mdn_k3", "track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign", 4),
    ("wave4_4_gru_latent_offset_residual", "gru_offset_residual", "track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign", 1),
    ("wave4_4_causal_tcn_latent_offset_residual", "causal_tcn_offset_residual", "track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign", 4),
    ("wave5_1_harmonic_prior_pointwise_control", "pointwise_control", "wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign", 1),
    ("wave5_1_harmonic_prior_smooth_l1_structured", "smooth_l1_structured", "wave3_harmonic_prior_residual/campaigns/2026-06-14_wave3_harmonic_prior_residual_campaign", 4),
]:
    for surface_index, surface_name in enumerate(["global", "fw", "bw"]):
        FULL_WAVE_SOURCE_ENTRY_LIST.append(
            (
                family_name,
                surface_name,
                f"config/training/{campaign_root}/queue/{base_index + surface_index:02d}_{file_prefix}_{surface_name}.yaml",
            )
        )


def read_yaml_file(input_path: str | Path) -> dict[str, Any]:

    """Read one YAML file."""

    resolved_path = PROJECT_PATH / Path(input_path)
    with resolved_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"YAML payload must be a dictionary | {resolved_path}"
    return payload


def write_yaml_file(payload: dict[str, Any], output_path: str | Path) -> None:

    """Write one YAML file."""

    resolved_path = PROJECT_PATH / Path(output_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    with resolved_path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def write_text_file(output_path: str | Path, text: str) -> None:

    """Write one UTF-8 text file."""

    resolved_path = PROJECT_PATH / Path(output_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_path.write_text(text, encoding="utf-8")


def normalize_path(path_value: str) -> str:

    """Normalize a repository path for YAML and Markdown."""

    return path_value.replace("\\", "/")


def build_windows_launcher_command(launcher_path: str) -> str:

    """Build a readable repository-relative PowerShell launcher command."""

    return ".\\" + launcher_path.replace("/", "\\")


def build_rcim_config(direction_name: str) -> dict[str, Any]:

    """Build one polished RCIM direction config from the exact-paper baseline."""

    baseline_path = (
        "config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/"
        f"baseline_{direction_name}.yaml"
    )
    config = deepcopy(read_yaml_file(baseline_path))
    surface_name = "fw" if direction_name == "forward" else "bw"
    config.setdefault("paths", {})["output_root"] = "output/validation_checks/rcim_model_bank_reproduction_polished_dataset"
    config.setdefault("experiment", {})["run_name"] = (
        f"rcim_model_bank_reproduction_polished_dataset_{surface_name}"
    )
    config["experiment"]["model_family"] = "rcim_model_bank_reproduction"
    config["experiment"]["model_type"] = f"exact_model_bank_{direction_name}"
    config.setdefault("dataset", {})["name"] = POLISHED_DATASET_NAME
    config.setdefault("metadata", {})["campaign_name"] = RCIM_CAMPAIGN_NAME
    config["metadata"]["planning_report_path"] = RCIM_PLANNING_REPORT_PATH
    config["metadata"]["technical_document_path"] = TECHNICAL_DOCUMENT_PATH
    config["metadata"]["dataset_schema"] = "polished_point_v1"
    config["metadata"]["campaign_config_id"] = f"rcim_model_bank_reproduction_{surface_name}"
    config["metadata"]["training_variant"] = surface_name
    config["metadata"]["direction_scope_label"] = "forward_only" if direction_name == "forward" else "backward_only"
    config["metadata"]["use_forward_direction"] = direction_name == "forward"
    config["metadata"]["use_backward_direction"] = direction_name == "backward"
    config.setdefault("training", {})["random_seed"] = 42
    config.setdefault("training", {}).setdefault("hyperparameter_search", {})["grid_search_verbose"] = 1
    return config


def build_full_wave_config(
    canonical_family_name: str,
    surface_name: str,
    source_config_path: str,
    queue_index: int,
) -> dict[str, Any]:

    """Build one polished full-wave config from an existing source config."""

    source_config = read_yaml_file(source_config_path)
    config = shared_training_infrastructure.apply_dataset_override(source_config, POLISHED_DATASET_NAME)
    canonical_id = f"{canonical_family_name}_{surface_name}"
    surface_configuration = SURFACE_CONFIGURATION[surface_name]

    config.setdefault("paths", {})["dataset_config_path"] = "config/datasets/transmission_error_dataset.yaml"
    config["paths"]["output_root"] = f"output/training_runs/{canonical_family_name}"
    config.setdefault("experiment", {})["run_name"] = f"te_{canonical_id}"
    config["experiment"]["model_family"] = canonical_id

    metadata = config.setdefault("metadata", {})
    metadata["campaign_name"] = FULL_WAVE_CAMPAIGN_NAME
    metadata["planning_report_path"] = FULL_WAVE_PLANNING_REPORT_PATH
    metadata["technical_document_path"] = TECHNICAL_DOCUMENT_PATH
    metadata["phase_name"] = "polished_dataset_full_wave_retraining"
    metadata["campaign_config_id"] = canonical_id
    metadata["base_model_family"] = canonical_family_name
    metadata["source_config_path"] = normalize_path(source_config_path)
    metadata["dataset_schema"] = "polished_point_v1"
    metadata["queue_index"] = queue_index
    metadata.update(surface_configuration)

    if "output_run_name" in metadata:
        metadata["output_run_name"] = f"te_{canonical_id}"

    return config


def build_rcim_planning_report() -> str:

    """Build the polished RCIM campaign plan Markdown."""

    return "\n".join(
        [
            "# Polished Dataset RCIM Model-Bank Reproduction Campaign Plan",
            "",
            "## Campaign Status",
            "",
            "Prepared package. Operator execution is required; this plan does not start training.",
            "",
            "## Objective",
            "",
            "Rerun the old `Track 1` paper-reimplementation branch, now named",
            "`RCIM Model-Bank Reproduction`, on `polished_dataset` measured curves.",
            "",
            "The campaign uses the polished rows to reconstruct curve-level harmonic",
            "targets and curve-level operating features from measured columns. It is a",
            "polished reproduction of the RCIM model-bank workflow, not a frozen paper",
            "original or paper-retuned reference run.",
            "",
            "## Dataset Contract",
            "",
            "- dataset: `polished_dataset`",
            "- schema: `polished_point_v1`",
            "- measured inputs: `theta`, `theta_dot`, `tau_load`, `T`",
            "- measured target: `theta_TE`",
            "- RCIM curve-level operating features are derived from measured curve",
            "  medians of `theta_dot`, `tau_load`, and `T`.",
            "",
            "## Run Matrix",
            "",
            "| Surface | Config | Families |",
            "| --- | --- | --- |",
            "| `fw` | `rcim_model_bank_reproduction_polished_dataset_fw.yaml` | SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM |",
            "| `bw` | `rcim_model_bank_reproduction_polished_dataset_bw.yaml` | SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM |",
            "",
            "## Execution Policy",
            "",
            "- Local and `-Remote` launch paths are supported.",
            "- Heavy training is operator-run only.",
            "- Normal closeout must produce campaign results and registry/status",
            "  synchronization before any separate `TE Curve Verification Pipeline` refresh.",
            "",
        ]
    )


def build_full_wave_planning_report() -> str:

    """Build the polished full-wave campaign plan Markdown."""

    return "\n".join(
        [
            "# Polished Dataset Full Wave Retraining Campaign Plan",
            "",
            "## Campaign Status",
            "",
            "Prepared package. Operator execution is required; this plan does not start training.",
            "",
            "## Objective",
            "",
            "Retrain all non-paper model-development families visible in the current",
            "`TE Curve Verification Pipeline` best-model collage reference using",
            "`polished_dataset`.",
            "",
            "The campaign uses canonical future model-family names from commit",
            "`4dff9a28b56824da5f90e38e626e75c9348b842d`.",
            "",
            "## Scope",
            "",
            "- model families: `36`",
            "- surfaces: `global`, `fw`, `bw`",
            "- training configs: `108`",
            "- excluded: paper-original and paper-retuned reference surfaces",
            "- separate first campaign: `RCIM Model-Bank Reproduction` polished rerun",
            "",
            "## Dataset Contract",
            "",
            "- dataset: `polished_dataset`",
            "- schema: `polished_point_v1`",
            "- inputs: `theta`, `theta_dot`, `tau_load`, `T`",
            "- target: `theta_TE`",
            "- no filename-derived setpoints are used as model inputs",
            "",
            "## Execution Policy",
            "",
            "- Local and `-Remote` launch paths are supported.",
            "- Campaign runner uses `--dataset polished_dataset` and the generated",
            "  canonical config queue.",
            "- `--stop-on-error` remains enabled by default.",
            "- Normal closeout must happen before any separate",
            "  `TE Curve Verification Pipeline` refresh.",
            "",
        ]
    )


def build_launcher_note(title: str, launcher_path: str, manifest_path: str) -> str:

    """Build one launcher-note Markdown file."""

    surface_section_lines: list[str] = []
    if launcher_path == RCIM_LAUNCHER_PATH:
        surface_section_lines = [
            "## Local Surface Launch",
            "",
            "Use `-Surface fw` or `-Surface bw` to run only one measured direction.",
            "",
            "```powershell",
            f"{build_windows_launcher_command(launcher_path)} -Surface fw",
            "```",
            "",
            "```powershell",
            f"{build_windows_launcher_command(launcher_path)} -Surface bw",
            "```",
            "",
            "## Remote Surface Launch",
            "",
            "```powershell",
            f"{build_windows_launcher_command(launcher_path)} -Remote -Surface bw",
            "```",
            "",
        ]

    return "\n".join(
        [
            f"# {title}",
            "",
            "## Purpose",
            "",
            "Operator-facing launcher for a prepared `polished_dataset` retraining campaign.",
            "",
            "## Preflight",
            "",
            "```powershell",
            f"{build_windows_launcher_command(launcher_path)} -PreflightOnly",
            "```",
            "",
            "## Local Launch",
            "",
            "```powershell",
            build_windows_launcher_command(launcher_path),
            "```",
            "",
            *surface_section_lines,
            "## Remote Launch",
            "",
            "```powershell",
            f"{build_windows_launcher_command(launcher_path)} -Remote",
            "```",
            "",
            "## Campaign Manifest",
            "",
            f"`{manifest_path}`",
            "",
        ]
    )


def build_rcim_launcher() -> str:

    """Build the polished RCIM PowerShell launcher."""

    return f"""param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [ValidateSet("all", "fw", "bw")]
    [string]$Surface = "all",
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) {{ $env:PINNS_REMOTE_TRAINING_REPO_PATH }} else {{ "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks" }}),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) {{ $env:PINNS_REMOTE_TRAINING_CONDA_ENV }} else {{ "pinns_lan_env" }})
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\\..\\..")).Path
Set-Location $ProjectRoot

$CampaignName = "{RCIM_CAMPAIGN_NAME}"
$CampaignManifestPath = "{RCIM_CAMPAIGN_ROOT}/campaign.yaml"
$PlanningReportPath = "{RCIM_PLANNING_REPORT_PATH}"
$ValidatorPath = "{VALIDATOR_PATH}"
$RunnerPath = "scripts\\paper_reimplementation\\rcim_ml_compensation\\original_dataset_exact_model_bank\\run_original_dataset_exact_model_bank_validation.py"
$CampaignOutputDirectory = "output\\training_campaigns\\cross_wave\\polished_dataset\\rcim_model_bank_reproduction\\{RCIM_CAMPAIGN_NAME}"
$ConfigPathList = @(
    "{RCIM_CAMPAIGN_ROOT}/queue/rcim_model_bank_reproduction_polished_dataset_fw.yaml",
    "{RCIM_CAMPAIGN_ROOT}/queue/rcim_model_bank_reproduction_polished_dataset_bw.yaml"
)
$RunNameList = @(
    "rcim_model_bank_reproduction_polished_dataset_fw",
    "rcim_model_bank_reproduction_polished_dataset_bw"
)
$SurfaceList = @(
    "fw",
    "bw"
)
$script:LastPythonExitCode = 0

function Invoke-PolishedPython {{
    param(
        [string[]]$ArgumentList,
        [string]$LogPath = ""
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {{
        if ([string]::IsNullOrWhiteSpace($LogPath)) {{
            & $PythonExecutable @ArgumentList
        }} else {{
            & $PythonExecutable @ArgumentList 2>&1 | Tee-Object -FilePath $LogPath
        }}
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }}

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {{
        if ([string]::IsNullOrWhiteSpace($LogPath)) {{
            & python @ArgumentList
        }} else {{
            & python @ArgumentList 2>&1 | Tee-Object -FilePath $LogPath
        }}
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }}

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    if ([string]::IsNullOrWhiteSpace($LogPath)) {{
        & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    }} else {{
        & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList 2>&1 | Tee-Object -FilePath $LogPath
    }}
    $script:LastPythonExitCode = $LASTEXITCODE
}}

function Resolve-SelectedSurfaceIndexes {{
    if ($Surface -eq "all") {{
        return @(0..($SurfaceList.Count - 1))
    }}

    $SelectedIndex = [Array]::IndexOf($SurfaceList, $Surface)
    if ($SelectedIndex -lt 0) {{
        throw "Unsupported surface selector | $Surface"
    }}
    return @($SelectedIndex)
}}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"
Write-Host "[INFO] Surface: $Surface"

Invoke-PolishedPython -ArgumentList @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath
)
if ($script:LastPythonExitCode -ne 0) {{ exit $script:LastPythonExitCode }}

if ($PreflightOnly) {{
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}}

$SelectedSurfaceIndexList = Resolve-SelectedSurfaceIndexes
$SelectedConfigPathList = foreach ($ConfigIndex in $SelectedSurfaceIndexList) {{
    $ConfigPathList[$ConfigIndex]
}}
$SelectedRunNameList = foreach ($ConfigIndex in $SelectedSurfaceIndexList) {{
    $RunNameList[$ConfigIndex]
}}

if ($Remote) {{
    & ".\\scripts\\campaigns\\track_1\\exact_paper\\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $CampaignName `
        -PlanningReportPath $PlanningReportPath `
        -LauncherRelativePath "{RCIM_LAUNCHER_PATH}" `
        -CampaignOutputRootOverride $CampaignOutputDirectory `
        -CampaignConfigPathList @($SelectedConfigPathList) `
        -RunNameList @($SelectedRunNameList) `
        -ValidationOutputRoot "output\\validation_checks\\rcim_model_bank_reproduction_polished_dataset" `
        -ValidationReportRoot "doc\\reports\\analysis\\validation_checks\\rcim_model_bank_reproduction_polished_dataset" `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}}

$LogRoot = Join-Path $ProjectRoot (Join-Path $CampaignOutputDirectory "logs")
New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null

foreach ($ConfigIndex in $SelectedSurfaceIndexList) {{
    $ConfigPath = $ConfigPathList[$ConfigIndex]
    $ConfigStem = [System.IO.Path]::GetFileNameWithoutExtension($ConfigPath)
    $LogPath = Join-Path $LogRoot ($ConfigStem + ".log")
    Write-Host ("[INFO] RCIM polished run {{0}}/{{1}} | surface={{2}} | {{3}}" -f ($ConfigIndex + 1), $ConfigPathList.Count, $SurfaceList[$ConfigIndex], $ConfigPath)
    Write-Host ("[INFO] Run log | {{0}}" -f $LogPath)
    Invoke-PolishedPython -ArgumentList @(
        "-B",
        $RunnerPath,
        "--config-path",
        $ConfigPath,
        "--output-suffix",
        "polished_dataset_campaign_validation"
    ) -LogPath $LogPath
    if ($script:LastPythonExitCode -ne 0) {{ exit $script:LastPythonExitCode }}
}}

Write-Host "[DONE] Polished RCIM Model-Bank Reproduction campaign completed"
"""


def build_full_wave_launcher() -> str:

    """Build the polished full-wave PowerShell launcher."""

    return f"""param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$EnqueueOnly,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) {{ $env:PINNS_REMOTE_TRAINING_REPO_PATH }} else {{ "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks" }}),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) {{ $env:PINNS_REMOTE_TRAINING_CONDA_ENV }} else {{ "pinns_env" }})
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\\..\\..")).Path
Set-Location $ProjectRoot

$CampaignName = "{FULL_WAVE_CAMPAIGN_NAME}"
$CampaignManifestPath = "{FULL_WAVE_CAMPAIGN_ROOT}/campaign.yaml"
$PlanningReportPath = "{FULL_WAVE_PLANNING_REPORT_PATH}"
$ValidatorPath = "{VALIDATOR_PATH}"
$QueueRoot = "config\\training\\queue\\polished_dataset_full_wave_retraining"
$script:LastPythonExitCode = 0

function Invoke-PolishedPython {{
    param([string[]]$ArgumentList)

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {{
        & $PythonExecutable @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }}

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {{
        & python @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }}

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}}

function Get-ManifestConfigPathList {{
    $PythonCode = @"
from pathlib import Path
import json
import yaml
manifest_path = Path(r"$CampaignManifestPath")
payload = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
print(json.dumps(payload["queue_config_path_list"]))
"@
    $EncodedCommand = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($PythonCode))
    $JsonText = & conda run --no-capture-output -n $CondaEnvironmentName python -c "import base64; exec(base64.b64decode('$EncodedCommand').decode('utf-8'))"
    if ($LASTEXITCODE -ne 0) {{
        throw "Failed to read campaign manifest | $CampaignManifestPath"
    }}
    return @($JsonText | ConvertFrom-Json)
}}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"

Invoke-PolishedPython -ArgumentList @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath
)
if ($script:LastPythonExitCode -ne 0) {{ exit $script:LastPythonExitCode }}

if ($PreflightOnly) {{
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}}

$CampaignConfigPathList = Get-ManifestConfigPathList

if ($Remote) {{
    if ($EnqueueOnly) {{
        throw "-EnqueueOnly is supported only for local launcher verification."
    }}

    & ".\\scripts\\campaigns\\infrastructure\\run_remote_training_campaign.ps1" `
        -CampaignConfigPathList $CampaignConfigPathList `
        -CampaignName $CampaignName `
        -PlanningReportPath $PlanningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList @("scripts", "config", "doc", "site", "requirements.txt", "AGENTS.md") `
        -AdditionalTrainingArgumentList @(
            "--dataset",
            "polished_dataset",
            "--queue-root",
            $QueueRoot,
            "--stop-on-error"
        )
    exit $LASTEXITCODE
}}

$TrainingArgumentList = @(
    "-B",
    "scripts\\training\\run_training_campaign.py"
) + $CampaignConfigPathList + @(
    "--dataset",
    "polished_dataset",
    "--queue-root",
    $QueueRoot,
    "--campaign-name",
    $CampaignName,
    "--planning-report-path",
    $PlanningReportPath,
    "--stop-on-error"
)
if ($EnqueueOnly) {{
    $TrainingArgumentList += "--enqueue-only"
}}

Write-Host "[STEP] Launching local polished full-wave retraining campaign."
$RunExitCode = Invoke-PolishedPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
"""


def prepare_rcim_campaign() -> list[str]:

    """Prepare polished RCIM configs and manifest."""

    queue_path_list: list[str] = []
    for direction_name, surface_name in [("forward", "fw"), ("backward", "bw")]:
        config_path = (
            f"{RCIM_CAMPAIGN_ROOT}/queue/"
            f"rcim_model_bank_reproduction_polished_dataset_{surface_name}.yaml"
        )
        write_yaml_file(build_rcim_config(direction_name), config_path)
        queue_path_list.append(config_path)

    manifest = {
        "schema_version": 1,
        "campaign_name": RCIM_CAMPAIGN_NAME,
        "campaign_type": "rcim_model_bank_reproduction",
        "dataset_name": POLISHED_DATASET_NAME,
        "dataset_schema": "polished_point_v1",
        "planning_report_path": RCIM_PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": True,
            "run_te_curve_verification_pipeline": False,
            "excluded_training_surface_list": ["paper_original", "paper_retuned"],
        },
    }
    write_yaml_file(manifest, f"{RCIM_CAMPAIGN_ROOT}/campaign.yaml")
    return queue_path_list


def prepare_full_wave_campaign() -> list[str]:

    """Prepare polished full-wave configs and manifest."""

    assert len(FULL_WAVE_SOURCE_ENTRY_LIST) == 108, len(FULL_WAVE_SOURCE_ENTRY_LIST)
    queue_path_list: list[str] = []
    for queue_index, (canonical_family_name, surface_name, source_config_path) in enumerate(
        FULL_WAVE_SOURCE_ENTRY_LIST,
        start=1,
    ):
        assert (PROJECT_PATH / source_config_path).exists(), source_config_path
        canonical_id = f"{canonical_family_name}_{surface_name}"
        output_path = f"{FULL_WAVE_CAMPAIGN_ROOT}/queue/{queue_index:03d}_{canonical_id}.yaml"
        write_yaml_file(
            build_full_wave_config(canonical_family_name, surface_name, source_config_path, queue_index),
            output_path,
        )
        queue_path_list.append(output_path)

    manifest = {
        "schema_version": 1,
        "campaign_name": FULL_WAVE_CAMPAIGN_NAME,
        "campaign_type": "full_wave_model_development_retraining",
        "dataset_name": POLISHED_DATASET_NAME,
        "dataset_schema": "polished_point_v1",
        "expected_family_count": 36,
        "expected_surface_list": ["global", "fw", "bw"],
        "expected_run_count": 108,
        "planning_report_path": FULL_WAVE_PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "queue_config_path_list": queue_path_list,
        "execution_policy": {
            "operator_run_required": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
            "excluded_training_surface_list": ["paper_original", "paper_retuned"],
        },
    }
    write_yaml_file(manifest, f"{FULL_WAVE_CAMPAIGN_ROOT}/campaign.yaml")
    return queue_path_list


def prepare_active_campaign_state(rcim_queue_path_list: list[str]) -> None:

    """Set the active campaign state to the first campaign to execute."""

    prepared_timestamp = datetime.now().astimezone().isoformat()
    active_state = {
        "status": "prepared",
        "campaign_name": RCIM_CAMPAIGN_NAME,
        "prepared_at": prepared_timestamp,
        "campaign_output_directory": (
            "output/training_campaigns/cross_wave/polished_dataset/"
            f"rcim_model_bank_reproduction/{RCIM_CAMPAIGN_NAME}"
        ),
        "planning_report_path": RCIM_PLANNING_REPORT_PATH,
        "technical_document_path": TECHNICAL_DOCUMENT_PATH,
        "queue_config_path_list": rcim_queue_path_list,
        "protected_file_list": [
            RCIM_PLANNING_REPORT_PATH,
            f"{RCIM_CAMPAIGN_ROOT}/campaign.yaml",
            *rcim_queue_path_list,
            RCIM_LAUNCHER_PATH,
            RCIM_LAUNCHER_NOTE_PATH,
            ACTIVE_CAMPAIGN_STATE_PATH,
        ],
        "launch_command_list": [
            build_windows_launcher_command(RCIM_LAUNCHER_PATH),
            f"{build_windows_launcher_command(RCIM_LAUNCHER_PATH)} -Remote",
        ],
        "notes": (
            "Prepared first polished retraining campaign. Run and close this RCIM "
            "Model-Bank Reproduction campaign before launching the prepared full-wave campaign."
        ),
        "next_prepared_campaign": {
            "campaign_name": FULL_WAVE_CAMPAIGN_NAME,
            "planning_report_path": FULL_WAVE_PLANNING_REPORT_PATH,
            "campaign_manifest_path": f"{FULL_WAVE_CAMPAIGN_ROOT}/campaign.yaml",
            "launch_command_list": [
                build_windows_launcher_command(FULL_WAVE_LAUNCHER_PATH),
                f"{build_windows_launcher_command(FULL_WAVE_LAUNCHER_PATH)} -Remote",
            ],
            "expected_run_count": 108,
        },
    }
    write_yaml_file(active_state, ACTIVE_CAMPAIGN_STATE_PATH)


def main() -> None:

    """Prepare all approved campaign artifacts."""

    rcim_queue_path_list = prepare_rcim_campaign()
    full_wave_queue_path_list = prepare_full_wave_campaign()
    write_text_file(RCIM_PLANNING_REPORT_PATH, build_rcim_planning_report())
    write_text_file(FULL_WAVE_PLANNING_REPORT_PATH, build_full_wave_planning_report())
    write_text_file(RCIM_LAUNCHER_PATH, build_rcim_launcher())
    write_text_file(FULL_WAVE_LAUNCHER_PATH, build_full_wave_launcher())
    write_text_file(
        RCIM_LAUNCHER_NOTE_PATH,
        build_launcher_note(
            "Run Polished Dataset RCIM Model-Bank Reproduction Campaign",
            RCIM_LAUNCHER_PATH,
            f"{RCIM_CAMPAIGN_ROOT}/campaign.yaml",
        ),
    )
    write_text_file(
        FULL_WAVE_LAUNCHER_NOTE_PATH,
        build_launcher_note(
            "Run Polished Dataset Full Wave Retraining Campaign",
            FULL_WAVE_LAUNCHER_PATH,
            f"{FULL_WAVE_CAMPAIGN_ROOT}/campaign.yaml",
        ),
    )
    prepare_active_campaign_state(rcim_queue_path_list)

    print(f"[DONE] RCIM polished configs prepared | count={len(rcim_queue_path_list)}")
    print(f"[DONE] Full-wave polished configs prepared | count={len(full_wave_queue_path_list)}")
    print(f"[DONE] Active campaign state set to | {RCIM_CAMPAIGN_NAME}")


if __name__ == "__main__":
    main()
