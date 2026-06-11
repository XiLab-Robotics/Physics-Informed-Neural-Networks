"""Prepare the Track 2H dispersion-aware robust-loss campaign package."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = "track2h_dispersion_aware_modeling_campaign_2026_06_10"
CAMPAIGN_ROOT = Path(
    "config/training/track2h_dispersion_aware_modeling/campaigns/"
    "2026-06-10_track2h_dispersion_aware_modeling_campaign"
)
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
SOURCE_DATASET_VARIANT_ROOT = Path(
    "config/training/track2g_curve_aware_training/campaigns/"
    "2026-06-08_track2g_curve_aware_training_campaign/dataset_variants"
)
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/track2/"
    "2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-10/"
    "2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probes.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/track2/validate_track2h_dispersion_aware_modeling_package.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/track2/run_track2h_dispersion_aware_modeling_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME
RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]

DIRECTION_METADATA_DICTIONARY = {
    "global": {
        "surface": "global",
        "direction_token": "global",
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
        "dataset_file_name": "transmission_error_dataset_global.yaml",
    },
    "fw": {
        "surface": "Fw",
        "direction_token": "fw",
        "training_variant": "Fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
        "dataset_file_name": "transmission_error_dataset_fw.yaml",
    },
    "bw": {
        "surface": "Bw",
        "direction_token": "bw",
        "training_variant": "Bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
        "dataset_file_name": "transmission_error_dataset_bw.yaml",
    },
}

ROBUST_LOSS_PROFILE_DICTIONARY = {
    "mae_robust": {
        "queue_label": "mae_robust",
        "pointwise_loss": "mae",
        "notes": "Robust L1 pointwise objective; Track 2G pointwise-control remains the MSE control.",
    },
    "smooth_l1_robust": {
        "queue_label": "smooth_l1_robust",
        "pointwise_loss": "smooth_l1",
        "huber_delta": 1.0,
        "notes": "Smooth L1 / Huber-style pointwise objective with delta 1.0 in normalized target space.",
    },
    "log_cosh_robust": {
        "queue_label": "log_cosh_robust",
        "pointwise_loss": "log_cosh",
        "notes": "Log-cosh pointwise objective for smooth outlier-resistant deterministic regression.",
    },
}


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML file with stable formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")


def to_posix_path(path_value: Path) -> str:

    """Return a repository-relative path with POSIX separators."""

    return path_value.as_posix()


def validate_no_conflicting_active_campaign() -> None:

    """Stop if another prepared or active campaign is present."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    active_status = str(active_state.get("status", "")).strip().lower()
    active_campaign_name = str(active_state.get("campaign_name", "")).strip()
    same_campaign_is_prepared = active_status == "prepared" and active_campaign_name == CAMPAIGN_NAME
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        "Cannot prepare Track 2H while another campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )


def copy_dataset_variants() -> list[Path]:

    """Copy the direction-specific dataset variants into the campaign root."""

    dataset_variant_path_list: list[Path] = []
    for direction_metadata in DIRECTION_METADATA_DICTIONARY.values():
        dataset_file_name = str(direction_metadata["dataset_file_name"])
        source_path = PROJECT_PATH / SOURCE_DATASET_VARIANT_ROOT / dataset_file_name
        target_path = PROJECT_PATH / DATASET_VARIANT_ROOT / dataset_file_name
        assert source_path.exists(), f"Missing source dataset variant | {source_path}"
        write_yaml_file(target_path, read_yaml_file(source_path))
        dataset_variant_path_list.append(DATASET_VARIANT_ROOT / dataset_file_name)
    return dataset_variant_path_list


def build_base_dataset_config() -> dict[str, Any]:

    """Build the shared sequence dataset config for robust-loss runs."""

    return {
        "curve_batch_size": 2,
        "point_stride": 1,
        "maximum_points_per_curve": None,
        "collate_mode": "sequence",
        "sequence_length": 33,
        "sequence_stride": 4,
        "sequence_target_position": "center",
        "maximum_sequences_per_curve": 192,
        "shuffle_training_batch_elements": False,
        "num_workers": 8,
        "pin_memory": True,
    }


def build_base_model_config() -> dict[str, Any]:

    """Build the shared harmonic residual-offset model config."""

    return {
        "input_size": 5,
        "output_size": 1,
        "harmonic_order": 240,
        "coefficient_mode": "linear_conditioned",
        "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
        "offset_hidden_size": 96,
        "offset_num_layers": 2,
        "offset_dropout_probability": 0.10,
        "offset_bidirectional": False,
        "offset_readout_position": "center",
        "offset_scale": 1.0,
        "freeze_structured_branch": False,
    }


def build_base_training_config(loss_profile_name: str) -> dict[str, Any]:

    """Build the shared training config for one robust loss profile."""

    robust_loss_profile = ROBUST_LOSS_PROFILE_DICTIONARY[loss_profile_name]
    loss_dictionary: dict[str, Any] = {
        "profile": loss_profile_name,
        "pointwise_loss": robust_loss_profile["pointwise_loss"],
        "weights": {"point": 1.0, "centered": 0.0, "offset": 0.0, "amplitude": 0.0, "harmonic": 0.0},
        "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
    }
    if "huber_delta" in robust_loss_profile:
        loss_dictionary["huber_delta"] = float(robust_loss_profile["huber_delta"])

    return {
        "learning_rate": 0.0005,
        "weight_decay": 0.0001,
        "min_epochs": 20,
        "max_epochs": 260,
        "patience": 40,
        "min_delta": 1.0e-05,
        "log_every_n_steps": 1,
        "fast_dev_run": False,
        "deterministic": False,
        "loss": loss_dictionary,
    }


def build_runtime_config() -> dict[str, Any]:

    """Build the shared runtime config."""

    return {
        "accelerator": "auto",
        "devices": "auto",
        "precision": "32",
        "benchmark": True,
        "use_non_blocking_transfer": True,
    }


def build_queue_config(queue_index: int, surface_key: str, loss_profile_name: str) -> dict[str, Any]:

    """Build one Track 2H queue config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    direction_token = str(direction_metadata["direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    model_family = f"track2h_dispersion_aware_{loss_profile_name}_{direction_token}"
    run_name = f"te_track2h_{loss_profile_name}_{direction_token}"
    robust_loss_profile = ROBUST_LOSS_PROFILE_DICTIONARY[loss_profile_name]

    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": run_name,
            "model_family": model_family,
            "model_type": "curve_aware_harmonic_residual_offset_probe",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
            "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
            "phase_name": "track2h_dispersion_aware_modeling",
            "campaign_config_id": model_family,
            "queue_index": queue_index,
            "intervention": "robust_pointwise_loss",
            "probe_group": "robust_loss",
            "loss_profile": loss_profile_name,
            "pointwise_loss": robust_loss_profile["pointwise_loss"],
            "training_variant": direction_metadata["training_variant"],
            "direction_scope_label": direction_metadata["direction_scope_label"],
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
            "runtime_input_contract": "current point state plus supported short causal sequence history only",
            "promotion_rule": "Candidate must return through official Track 2 curve-first verification.",
            "harmonic_basis": "sparse_rcim",
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
            "baseline_control": "Track 2G pointwise-control MSE candidates",
            "notes": robust_loss_profile["notes"],
        },
        "dataset": build_base_dataset_config(),
        "model": build_base_model_config(),
        "training": build_base_training_config(loss_profile_name),
        "runtime": build_runtime_config(),
    }


def write_queue_configs() -> list[Path]:

    """Materialize all Track 2H queue configs."""

    queue_path_list: list[Path] = []
    queue_index = 1
    for loss_profile_name in ROBUST_LOSS_PROFILE_DICTIONARY:
        for surface_key in ["global", "fw", "bw"]:
            queue_file_name = f"{queue_index:02d}_{ROBUST_LOSS_PROFILE_DICTIONARY[loss_profile_name]['queue_label']}_{surface_key}.yaml"
            queue_path = QUEUE_ROOT / queue_file_name
            write_yaml_file(PROJECT_PATH / queue_path, build_queue_config(queue_index, surface_key, loss_profile_name))
            queue_path_list.append(queue_path)
            queue_index += 1
    return queue_path_list


def write_campaign_readme(queue_path_list: list[Path]) -> Path:

    """Write the campaign-local README."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    readme_line_list = [
        "# Track 2H Dispersion-Aware Modeling Campaign Package",
        "",
        "This package materializes the approved first Track 2H robust-loss",
        "probe. It contains 9 runnable queue entries: three robust pointwise",
        "losses across `global`, `Fw`, and `Bw` surfaces.",
        "",
        "The MSE pointwise-control baseline is the already verified Track 2G",
        "pointwise-control set. Runtime input remains causal point or",
        "short-history sequence input.",
        "",
        "## Queue Files",
        "",
    ]
    readme_line_list.extend(f"- `{to_posix_path(queue_path)}`" for queue_path in queue_path_list)
    readme_line_list.extend(
        [
            "",
            "## Launch Commands",
            "",
            "```powershell",
            ".\\scripts\\campaigns\\track2\\run_track2h_dispersion_aware_modeling_campaign.ps1 -PreflightOnly",
            ".\\scripts\\campaigns\\track2\\run_track2h_dispersion_aware_modeling_campaign.ps1",
            ".\\scripts\\campaigns\\track2\\run_track2h_dispersion_aware_modeling_campaign.ps1 -Remote",
            "```",
        ]
    )
    output_path = PROJECT_PATH / readme_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(readme_line_list) + "\n", encoding="utf-8")
    return readme_path


def write_active_campaign_state(queue_path_list: list[Path], dataset_variant_path_list: list[Path], readme_path: Path) -> None:

    """Write the persistent prepared campaign state."""

    protected_file_list = [
        to_posix_path(CAMPAIGN_ROOT),
        to_posix_path(PLANNING_REPORT_PATH),
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
        to_posix_path(LAUNCHER_PATH),
        to_posix_path(VALIDATOR_PATH),
        to_posix_path(LAUNCHER_NOTE_PATH),
        to_posix_path(readme_path),
    ]
    protected_file_list.extend(to_posix_path(path) for path in queue_path_list)
    protected_file_list.extend(to_posix_path(path) for path in dataset_variant_path_list)

    active_state = {
        "status": "prepared",
        "campaign_name": CAMPAIGN_NAME,
        "prepared_at": "2026-06-10T16:56:36+02:00",
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "queue_config_path_list": [to_posix_path(path) for path in queue_path_list],
        "protected_file_list": protected_file_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\track2\\run_track2h_dispersion_aware_modeling_campaign.ps1",
            ".\\scripts\\campaigns\\track2\\run_track2h_dispersion_aware_modeling_campaign.ps1 -Remote",
        ],
        "notes": "Prepared Track 2H robust-loss probe package. Training execution requires explicit operator launch approval.",
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_state)


def main() -> int:

    """Prepare the Track 2H robust-loss campaign package."""

    validate_no_conflicting_active_campaign()
    dataset_variant_path_list = copy_dataset_variants()
    queue_path_list = write_queue_configs()
    readme_path = write_campaign_readme(queue_path_list)
    write_active_campaign_state(queue_path_list, dataset_variant_path_list, readme_path)
    print(
        "Prepared Track 2H robust-loss campaign package | "
        f"campaign={CAMPAIGN_NAME} | queue_entries={len(queue_path_list)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
