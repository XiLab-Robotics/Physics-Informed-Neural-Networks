"""Prepare the Wave 5.2B offset and harmonic guided campaign package."""

from __future__ import annotations

# Import Python Utilities
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = "wave52b_offset_harmonic_guided_campaign_2026_07_01"
CAMPAIGN_ROOT = Path(
    "config/training/wave52b_offset_harmonic_guided/campaigns/"
    "2026-07-01_wave52b_offset_harmonic_guided_campaign"
)
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/wave_5_2/"
    "2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-07/2026-07-01/"
    "2026-07-01-16-08-01_wave52b_offset_harmonic_guided_preparation.md"
)
MODEL_REPORT_PATH = Path("doc/reports/analysis/wave5_2/Wave 5.2B Offset And Harmonic Guided Model.md")
LAUNCHER_PATH = Path("scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME
QUEUE_EXECUTION_ROOT = Path("config/training/queue/wave52b_offset_harmonic_guided")
RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]


class NoAliasSafeDumper(yaml.SafeDumper):

    """YAML dumper that keeps generated configs free of anchors."""

    def ignore_aliases(self, data: Any) -> bool:

        """Disable YAML anchors for campaign-generated configuration files."""

        return True

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

ABLATION_PROFILE_DICTIONARY = {
    "pointwise_control": {
        "queue_label": "pointwise_control",
        "offset_scale": 0.0,
        "harmonic_scale": 0.0,
        "loss_weights": {"point": 1.0, "centered": 0.0, "offset": 0.0, "amplitude": 0.0, "harmonic": 0.0},
        "intervention": "wave52b_direct_pointwise_control",
    },
    "offset_head": {
        "queue_label": "offset_head",
        "offset_scale": 1.0,
        "harmonic_scale": 0.0,
        "loss_weights": {"point": 1.0, "centered": 0.0, "offset": 0.15, "amplitude": 0.0, "harmonic": 0.0},
        "intervention": "wave52b_explicit_offset_head",
    },
    "offset_centered_shape": {
        "queue_label": "offset_centered_shape",
        "offset_scale": 1.0,
        "harmonic_scale": 0.0,
        "loss_weights": {"point": 1.0, "centered": 0.20, "offset": 0.15, "amplitude": 0.05, "harmonic": 0.0},
        "intervention": "wave52b_offset_and_centered_shape_loss",
    },
    "offset_centered_shape_harmonic": {
        "queue_label": "offset_centered_shape_harmonic",
        "offset_scale": 1.0,
        "harmonic_scale": 1.0,
        "loss_weights": {"point": 1.0, "centered": 0.20, "offset": 0.15, "amplitude": 0.05, "harmonic": 0.10},
        "intervention": "wave52b_offset_centered_shape_and_sparse_harmonic_guidance",
    },
}


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write one YAML file with stable formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        yaml.dump(payload, Dumper=NoAliasSafeDumper, sort_keys=False, width=1000),
        encoding="utf-8",
    )


def to_posix_path(path_value: Path) -> str:

    """Return a repository-relative path with POSIX separators."""

    return path_value.as_posix()


def validate_no_conflicting_active_campaign() -> dict[str, Any]:

    """Stop if another local campaign is already prepared or active."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    active_status = str(active_state.get("status", "")).strip().lower()
    active_campaign_name = str(active_state.get("campaign_name", "")).strip()
    same_campaign_is_prepared = active_status == "prepared" and active_campaign_name == CAMPAIGN_NAME
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        "Cannot prepare Wave 5.2B while another local campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )
    return active_state


def build_dataset_variant(direction_metadata: dict[str, Any]) -> dict[str, Any]:

    """Build one polished-dataset direction variant."""

    return {
        "paths": {"dataset_root": "data/polished_dataset"},
        "dataset": {
            "name": "polished_dataset",
            "schema": "polished_point_v1",
            "reduction_ratio": 81.0,
            "angular_window_deg": {"minimum": 0.0, "maximum": 360.0},
        },
        "directions": {
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
        },
        "split": {"validation_split": 0.2, "test_split": 0.1, "random_seed": 42},
        "dataloader": {"batch_size": 8, "num_workers": 0},
    }


def write_dataset_variants() -> list[Path]:

    """Write direction-specific polished dataset variants."""

    dataset_variant_path_list: list[Path] = []
    for direction_metadata in DIRECTION_METADATA_DICTIONARY.values():
        dataset_file_name = str(direction_metadata["dataset_file_name"])
        dataset_variant_path = DATASET_VARIANT_ROOT / dataset_file_name
        write_yaml_file(PROJECT_PATH / dataset_variant_path, build_dataset_variant(direction_metadata))
        dataset_variant_path_list.append(dataset_variant_path)
    return dataset_variant_path_list


def build_base_dataset_config() -> dict[str, Any]:

    """Build the shared sequence dataset config."""

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
        "name": "polished_dataset",
    }


def build_model_config(ablation_profile_name: str) -> dict[str, Any]:

    """Build one Wave 5.2B model config."""

    ablation_profile = ABLATION_PROFILE_DICTIONARY[ablation_profile_name]
    return {
        "input_size": "auto",
        "output_size": 1,
        "base_hidden_size": [128, 96, 64],
        "offset_hidden_size": [64, 32],
        "activation_name": "GELU",
        "dropout_probability": 0.05,
        "use_layer_norm": True,
        "offset_scale": float(ablation_profile["offset_scale"]),
        "harmonic_scale": float(ablation_profile["harmonic_scale"]),
        "harmonic_order": 240,
        "coefficient_mode": "linear_conditioned",
        "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
        "readout_position": "center",
        "freeze_harmonic_branch": False,
    }


def build_training_config(ablation_profile_name: str) -> dict[str, Any]:

    """Build one Wave 5.2B training config."""

    ablation_profile = ABLATION_PROFILE_DICTIONARY[ablation_profile_name]
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
            "profile": ablation_profile_name,
            "pointwise_loss": "mse",
            "weights": dict(ablation_profile["loss_weights"]),
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
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


def build_queue_config(queue_index: int, surface_key: str, ablation_profile_name: str) -> dict[str, Any]:

    """Build one Wave 5.2B queue config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    ablation_profile = ABLATION_PROFILE_DICTIONARY[ablation_profile_name]
    direction_token = str(direction_metadata["direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    model_family = f"wave52b_offset_harmonic_guided_{ablation_profile_name}_{direction_token}"
    run_name = f"te_wave52b_offset_harmonic_guided_{ablation_profile_name}_{direction_token}"

    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": run_name,
            "model_family": model_family,
            "model_type": "wave52b_offset_harmonic_guided",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
            "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
            "model_report_path": to_posix_path(MODEL_REPORT_PATH),
            "phase_name": "wave52b_offset_harmonic_guided",
            "campaign_config_id": model_family,
            "queue_index": queue_index,
            "intervention": ablation_profile["intervention"],
            "probe_group": "wave52b_offset_harmonic_guided",
            "ablation_profile": ablation_profile_name,
            "training_variant": direction_metadata["training_variant"],
            "direction_scope_label": direction_metadata["direction_scope_label"],
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
            "dataset_id": "polished_dataset",
            "dataset_schema": "polished_point_v1",
            "comparison_baseline": "completed polished early-wave leaders and pending full-wave polished retraining package",
            "promotion_rule": "Candidate must return through official TE Curve Verification Pipeline after normal campaign closeout.",
            "wave52a_evidence": "Paired polished-vs-simplified matrix found offset and harmonic corrections dominate the dataset delta.",
            "harmonic_basis": "sparse_rcim",
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
        },
        "dataset": build_base_dataset_config(),
        "model": build_model_config(ablation_profile_name),
        "training": build_training_config(ablation_profile_name),
        "runtime": build_runtime_config(),
    }


def write_queue_configs() -> list[Path]:

    """Materialize all queue configs."""

    queue_path_list: list[Path] = []
    queue_index = 1
    for ablation_profile_name in ABLATION_PROFILE_DICTIONARY:
        for surface_key in ["global", "fw", "bw"]:
            queue_file_name = (
                f"{queue_index:03d}_{ABLATION_PROFILE_DICTIONARY[ablation_profile_name]['queue_label']}_{surface_key}.yaml"
            )
            queue_path = QUEUE_ROOT / queue_file_name
            write_yaml_file(PROJECT_PATH / queue_path, build_queue_config(queue_index, surface_key, ablation_profile_name))
            queue_path_list.append(queue_path)
            queue_index += 1
    return queue_path_list


def write_campaign_manifest(queue_path_list: list[Path], dataset_variant_path_list: list[Path]) -> Path:

    """Write the campaign manifest."""

    campaign_manifest_path = CAMPAIGN_ROOT / "campaign.yaml"
    manifest_dictionary = {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "campaign_type": "wave52b_offset_harmonic_guided_model_development",
        "dataset_name": "polished_dataset",
        "dataset_schema": "polished_point_v1",
        "expected_ablation_profile_list": list(ABLATION_PROFILE_DICTIONARY.keys()),
        "expected_surface_list": ["global", "fw", "bw"],
        "expected_run_count": len(queue_path_list),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "model_report_path": to_posix_path(MODEL_REPORT_PATH),
        "launcher_path": to_posix_path(LAUNCHER_PATH),
        "launcher_note_path": to_posix_path(LAUNCHER_NOTE_PATH),
        "validator_path": to_posix_path(VALIDATOR_PATH),
        "queue_execution_root": to_posix_path(QUEUE_EXECUTION_ROOT),
        "queue_config_path_list": [to_posix_path(path) for path in queue_path_list],
        "dataset_variant_path_list": [to_posix_path(path) for path in dataset_variant_path_list],
        "execution_policy": {
            "operator_run_required": True,
            "stop_on_error": True,
            "run_te_curve_verification_pipeline": False,
            "preserve_external_full_wave_polished_campaign": True,
        },
        "launch_command_list": [
            ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1",
            ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote",
        ],
    }
    write_yaml_file(PROJECT_PATH / campaign_manifest_path, manifest_dictionary)
    return campaign_manifest_path


def write_campaign_readme(queue_path_list: list[Path], campaign_manifest_path: Path) -> Path:

    """Write the campaign-local README."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    readme_line_list = [
        "# Wave 5.2B Offset And Harmonic Guided Campaign Package",
        "",
        "This package materializes the approved Wave 5.2B campaign on `polished_dataset`.",
        "It contains 12 runnable queue entries: four ablation profiles across",
        "`global`, `Fw`, and `Bw` surfaces.",
        "",
        "## Manifest",
        "",
        f"- `{to_posix_path(campaign_manifest_path)}`",
        "",
        "## Queue Files",
        "",
    ]
    readme_line_list.extend(f"- `{to_posix_path(queue_path)}`" for queue_path in queue_path_list)
    readme_line_list.extend([
        "",
        "## Launch Commands",
        "",
        "```powershell",
        ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly",
        ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1",
        ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote",
        "```",
    ])
    output_path = PROJECT_PATH / readme_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(readme_line_list) + "\n", encoding="utf-8")
    return readme_path


def write_active_campaign_state(
    previous_active_state: dict[str, Any],
    queue_path_list: list[Path],
    dataset_variant_path_list: list[Path],
    campaign_manifest_path: Path,
    readme_path: Path,
) -> None:

    """Write the persistent prepared campaign state."""

    protected_file_list = [
        to_posix_path(CAMPAIGN_ROOT),
        to_posix_path(campaign_manifest_path),
        to_posix_path(PLANNING_REPORT_PATH),
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
        to_posix_path(MODEL_REPORT_PATH),
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
        "prepared_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "campaign_manifest_path": to_posix_path(campaign_manifest_path),
        "queue_config_path_list": [to_posix_path(path) for path in queue_path_list],
        "protected_file_list": protected_file_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1",
            ".\\scripts\\campaigns\\wave_5_2\\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote",
        ],
        "notes": (
            "Prepared Wave 5.2B offset and harmonic guided package on polished_dataset. "
            "Training execution requires explicit operator launch approval. The external full-wave polished retraining "
            "campaign recorded under next_prepared_campaign remains untouched."
        ),
    }
    for preserved_key in ["last_completed_campaign", "next_prepared_campaign"]:
        if preserved_key in previous_active_state:
            active_state[preserved_key] = previous_active_state[preserved_key]
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_state)


def main() -> int:

    """Prepare the Wave 5.2B campaign package."""

    previous_active_state = validate_no_conflicting_active_campaign()
    dataset_variant_path_list = write_dataset_variants()
    queue_path_list = write_queue_configs()
    campaign_manifest_path = write_campaign_manifest(queue_path_list, dataset_variant_path_list)
    readme_path = write_campaign_readme(queue_path_list, campaign_manifest_path)
    write_active_campaign_state(
        previous_active_state,
        queue_path_list,
        dataset_variant_path_list,
        campaign_manifest_path,
        readme_path,
    )
    print(
        "Prepared Wave 5.2B offset and harmonic guided campaign package | "
        f"campaign={CAMPAIGN_NAME} | queue_entries={len(queue_path_list)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
