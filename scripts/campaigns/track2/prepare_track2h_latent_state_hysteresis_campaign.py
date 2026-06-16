"""Prepare the Track 2H-L latent-state hysteresis campaign package."""

from __future__ import annotations

# Import Python Utilities
import sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = "track2h_latent_state_hysteresis_campaign_2026_06_16"
CAMPAIGN_ROOT = Path(
    "config/training/track2h_latent_state_hysteresis/campaigns/"
    "2026-06-16_track2h_latent_state_hysteresis_campaign"
)
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
SOURCE_DATASET_VARIANT_ROOT = Path(
    "config/training/track2g_curve_aware_training/campaigns/"
    "2026-06-08_track2g_curve_aware_training_campaign/dataset_variants"
)
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/track2/"
    "2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-16/"
    "2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/track2/run_track2h_latent_state_hysteresis_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/track2/validate_track2h_latent_state_hysteresis_package.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/track2/run_track2h_latent_state_hysteresis_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME

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

LATENT_PROFILE_DICTIONARY = {
    "gru_offset_residual": {
        "queue_label": "gru_offset_residual",
        "latent_encoder_type": "gru",
        "latent_hidden_size": 96,
        "latent_num_layers": 2,
        "latent_channel_size": None,
        "latent_kernel_size": 5,
        "notes": "Compact causal GRU hidden state over previous operating-state samples.",
    },
    "causal_tcn_offset_residual": {
        "queue_label": "causal_tcn_offset_residual",
        "latent_encoder_type": "causal_tcn",
        "latent_hidden_size": 96,
        "latent_num_layers": 1,
        "latent_channel_size": [96, 96],
        "latent_kernel_size": 5,
        "notes": "Left-padded temporal convolution state over previous operating-state samples.",
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
        "Cannot prepare Track 2H-L latent-state package while another campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )


def copy_dataset_variants() -> list[Path]:

    """Copy direction-specific dataset variants into the campaign root."""

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

    """Build the shared causal sequence dataset config."""

    return {
        "curve_batch_size": 2,
        "point_stride": 1,
        "maximum_points_per_curve": None,
        "collate_mode": "sequence",
        "sequence_length": 33,
        "sequence_stride": 4,
        "sequence_target_position": "last",
        "maximum_sequences_per_curve": 192,
        "shuffle_training_batch_elements": False,
        "num_workers": 8,
        "pin_memory": True,
    }


def build_model_config(profile_name: str) -> dict[str, Any]:

    """Build the latent-state model config for one profile."""

    profile_dictionary = LATENT_PROFILE_DICTIONARY[profile_name]
    return {
        "input_size": 5,
        "output_size": 1,
        "latent_encoder_type": profile_dictionary["latent_encoder_type"],
        "latent_hidden_size": int(profile_dictionary["latent_hidden_size"]),
        "latent_num_layers": int(profile_dictionary["latent_num_layers"]),
        "latent_dropout_probability": 0.10,
        "latent_channel_size": profile_dictionary["latent_channel_size"],
        "latent_kernel_size": int(profile_dictionary["latent_kernel_size"]),
        "latent_activation_name": "GELU",
        "readout_position": "last",
        "base_hidden_size": [96, 64],
        "head_hidden_size": [96, 64],
        "head_activation_name": "GELU",
        "head_dropout_probability": 0.05,
        "use_layer_norm": True,
        "offset_scale": 1.0,
        "residual_scale": 1.0,
    }


def build_training_config(profile_name: str) -> dict[str, Any]:

    """Build the training config for one latent-state profile."""

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
        "loss": {
            "profile": profile_name,
            "pointwise_loss": "smooth_l1",
            "huber_delta": 0.75,
            "weights": {"point": 1.0, "centered": 0.20, "offset": 0.20, "amplitude": 0.05, "harmonic": 0.0},
            "harmonic_index_list": [],
        },
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


def build_queue_config(queue_index: int, surface_key: str, profile_name: str) -> dict[str, Any]:

    """Build one Track 2H-L queue config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    direction_token = str(direction_metadata["direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    profile_dictionary = LATENT_PROFILE_DICTIONARY[profile_name]
    model_family = f"track2h_latent_state_hysteresis_{profile_name}_{direction_token}"
    run_name = f"te_track2h_l_{profile_name}_{direction_token}"

    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": run_name,
            "model_family": model_family,
            "model_type": "latent_state_hysteresis_probe",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
            "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
            "phase_name": "track2h_latent_state_hysteresis",
            "campaign_config_id": model_family,
            "queue_index": queue_index,
            "intervention": "latent_state_hysteresis_probe",
            "probe_group": "latent_state_hysteresis",
            "loss_profile": profile_name,
            "latent_encoder_type": profile_dictionary["latent_encoder_type"],
            "training_variant": direction_metadata["training_variant"],
            "direction_scope_label": direction_metadata["direction_scope_label"],
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
            "runtime_input_contract": "current point state plus previous operating-state samples only",
            "causal_window_contract": "sequence_target_position=last and readout_position=last; no future samples are used",
            "forbidden_inputs": "measured TE, curve mean, held-out full-curve statistics, future samples, post-prediction centering",
            "promotion_rule": "Candidate must return through normal closeout and separate official Track 2 curve-first verification.",
            "baseline_control": "Completed Track 2H robust/probabilistic/MDN probes plus Wave 3 harmonic-prior residual",
            "notes": profile_dictionary["notes"],
        },
        "dataset": build_base_dataset_config(),
        "model": build_model_config(profile_name),
        "training": build_training_config(profile_name),
        "runtime": build_runtime_config(),
    }


def write_queue_configs() -> list[Path]:

    """Materialize all queue configs."""

    queue_path_list: list[Path] = []
    queue_index = 1
    for profile_name in LATENT_PROFILE_DICTIONARY:
        for surface_key in ["global", "fw", "bw"]:
            queue_file_name = f"{queue_index:02d}_{LATENT_PROFILE_DICTIONARY[profile_name]['queue_label']}_{surface_key}.yaml"
            queue_path = QUEUE_ROOT / queue_file_name
            write_yaml_file(PROJECT_PATH / queue_path, build_queue_config(queue_index, surface_key, profile_name))
            queue_path_list.append(queue_path)
            queue_index += 1
    return queue_path_list


def write_campaign_readme(queue_path_list: list[Path]) -> Path:

    """Write the campaign-local README."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    readme_line_list = [
        "# Track 2H-L Latent-State Hysteresis Campaign Package",
        "",
        "This package materializes the approved Track 2H-L latent-state /",
        "hysteresis-aware probe. It contains 6 runnable queue entries:",
        "`gru_offset_residual` and `causal_tcn_offset_residual` across",
        "`global`, `Fw`, and `Bw` surfaces.",
        "",
        "All entries use `sequence_target_position: last` and",
        "`readout_position: last`, so the latent state is estimated only from",
        "the current and previous operating-state samples in the window.",
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
            ".\\scripts\\campaigns\\track2\\run_track2h_latent_state_hysteresis_campaign.ps1 -PreflightOnly",
            ".\\scripts\\campaigns\\track2\\run_track2h_latent_state_hysteresis_campaign.ps1",
            ".\\scripts\\campaigns\\track2\\run_track2h_latent_state_hysteresis_campaign.ps1 -Remote",
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
        "prepared_at": "2026-06-16T16:58:30+02:00",
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "queue_config_path_list": [to_posix_path(path) for path in queue_path_list],
        "protected_file_list": protected_file_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\track2\\run_track2h_latent_state_hysteresis_campaign.ps1",
            ".\\scripts\\campaigns\\track2\\run_track2h_latent_state_hysteresis_campaign.ps1 -Remote",
        ],
        "notes": "Prepared Track 2H-L latent-state hysteresis package. Training execution requires explicit operator launch approval.",
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_state)


def main() -> int:

    """Prepare the Track 2H-L latent-state hysteresis campaign package."""

    validate_no_conflicting_active_campaign()
    dataset_variant_path_list = copy_dataset_variants()
    queue_path_list = write_queue_configs()
    readme_path = write_campaign_readme(queue_path_list)
    write_active_campaign_state(queue_path_list, dataset_variant_path_list, readme_path)
    print(
        "Prepared Track 2H-L latent-state hysteresis campaign package | "
        f"campaign={CAMPAIGN_NAME} | queue_entries={len(queue_path_list)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
