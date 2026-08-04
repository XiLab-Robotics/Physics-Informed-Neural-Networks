"""Promote the host-qualified Wave 5.2R A02 composition archive."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import hashlib
from pathlib import Path
import shutil
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml

# Import Project Inventory Utility
from scripts.models.export_post_retraining_selected_model_archives import (
    rebuild_aggregate_inventory,
)


# Define The Approved A02 Archive Contract
DEFAULT_SOURCE_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "deployment"
    / "wave52r_integrated_specialist_a02"
    / "2026-08-04-13-39-00__a02_export_parity"
)
SOURCE_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "integrated_specialist_models"
    / "2026-08-03-17-49-51__a02__seed_314159"
)
DECISION_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "integrated_specialist_track2_decision"
)
ARCHIVE_ROOT = (
    PROJECT_ROOT
    / "models"
    / "polished_dataset"
    / "setpoints"
    / "integrated_specialist_a02"
    / "global"
)
STAGING_ROOT = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_a02_model_archive_promotion"
    / "staged_models"
    / "integrated_specialist_a02"
    / "global"
)


def parse_arguments() -> argparse.Namespace:
    """Parse source and promotion arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-directory",
        type=Path,
        default=DEFAULT_SOURCE_DIRECTORY,
        help="Host-qualified A02 export-parity output directory.",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="Install the validated staged leaf and rebuild the aggregate inventory.",
    )
    return parser.parse_args()


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def compute_file_sha256(file_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def copy_file(source_path: Path, destination_path: Path) -> None:
    """Copy one required immutable artifact."""

    assert source_path.is_file(), source_path
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)


def project_relative_path(input_path: Path) -> str:
    """Return one repository-relative POSIX path."""

    return input_path.relative_to(PROJECT_ROOT).as_posix()


def tree_digest_map(root_directory: Path) -> dict[str, str]:
    """Return stable relative-path SHA-256 evidence for one directory tree."""

    return {
        artifact_path.relative_to(root_directory).as_posix(): compute_file_sha256(
            artifact_path
        )
        for artifact_path in sorted(root_directory.rglob("*"))
        if artifact_path.is_file()
    }


def load_a02_official_metrics() -> dict[str, dict[str, float]]:
    """Read the official per-surface A02 Track 2 metric rows."""

    score_path = DECISION_DIRECTORY / "multi_index_candidate_scores.csv"
    metric_dictionary = {}
    with score_path.open("r", encoding="utf-8", newline="") as input_file:
        for row in csv.DictReader(input_file):
            if row["candidate_id"] != "wave52r_integrated_a02_seed_314159":
                continue
            surface = row["surface"]
            metric_dictionary[surface] = {
                "raw_mae_deg": float(row["raw_mae_deg"]),
                "raw_rmse_deg": float(row["raw_rmse_deg"]),
                "mean_percentage_error_pct": float(
                    row["mean_percentage_error_pct"]
                ),
                "p95_mean_percentage_error_pct": float(
                    row["p95_mean_percentage_error_pct"]
                ),
                "centered_shape_mae_deg": float(
                    row["centered_shape_mae_deg"]
                ),
                "absolute_offset_error_deg": float(
                    row["absolute_offset_error_deg"]
                ),
                "harmonic_amplitude_error_pct": float(
                    row["harmonic_amplitude_error_pct"]
                ),
                "harmonic_phase_error_deg": float(
                    row["harmonic_phase_error_deg"]
                ),
            }
    assert set(metric_dictionary) == {"Fw", "Bw", "global"}
    return metric_dictionary


def stage_archive(source_directory: Path) -> dict[str, Any]:
    """Build and validate one immutable A02 archive leaf."""

    source_directory = (
        source_directory
        if source_directory.is_absolute()
        else PROJECT_ROOT / source_directory
    )
    summary_path = source_directory / "a02_export_parity_summary.yaml"
    summary = read_yaml(summary_path)
    assert summary["status"] == "passed"
    assert summary["candidate_id"] == "wave52r_integrated_a02_seed_314159"
    assert all(
        summary["qualification"][gate_name] == "passed"
        for gate_name in (
            "campaign_reconstruction_parity",
            "onnx_runtime_parity",
            "plc_float32_reference_parity",
            "backward_zero_residual",
        )
    )
    for artifact_name, relative_path in summary["artifact_path"].items():
        artifact_path = PROJECT_ROOT / relative_path
        assert artifact_path.is_file(), artifact_path
        assert compute_file_sha256(artifact_path) == summary[
            "artifact_sha256"
        ][artifact_name]

    if STAGING_ROOT.exists():
        shutil.rmtree(STAGING_ROOT)
    checkpoint_source = SOURCE_RUN_DIRECTORY / "best_model.pt"
    onnx_source = PROJECT_ROOT / summary["artifact_path"]["onnx"]
    copy_map = {
        checkpoint_source: STAGING_ROOT / "python" / "best_model.pt",
        onnx_source: STAGING_ROOT / "onnx" / "model.onnx",
        PROJECT_ROOT
        / summary["artifact_path"]["gate_parameters"]: STAGING_ROOT
        / "deployment"
        / "a02_gate_parameters.npz",
        PROJECT_ROOT
        / summary["artifact_path"]["parameter_st"]: STAGING_ROOT
        / "plc_reference"
        / "GVL_Wave52rA02Parameters.st",
        PROJECT_ROOT
        / summary["artifact_path"]["composer_st"]: STAGING_ROOT
        / "plc_reference"
        / "FB_Wave52rA02CurveComposer.st",
        SOURCE_RUN_DIRECTORY
        / "metrics_summary.yaml": STAGING_ROOT
        / "source_run"
        / "metrics_summary.snapshot.yaml",
        SOURCE_RUN_DIRECTORY
        / "training_history.csv": STAGING_ROOT
        / "source_run"
        / "training_history.snapshot.csv",
        summary_path: STAGING_ROOT
        / "source_run"
        / "export_parity_summary.snapshot.yaml",
        PROJECT_ROOT
        / summary["artifact_path"]["per_condition_parity"]: STAGING_ROOT
        / "source_run"
        / "a02_parity_per_condition.snapshot.csv",
        DECISION_DIRECTORY
        / "multi_index_surface_decision.yaml": STAGING_ROOT
        / "source_run"
        / "official_curve_verification_decision.snapshot.yaml",
    }
    for source_path, target_path in copy_map.items():
        copy_file(source_path, target_path)

    final_root = ARCHIVE_ROOT
    inventory = {
        "schema_version": 1,
        "dataset_id": "polished_dataset",
        "dataset_schema": "polished_setpoint_curve_v1",
        "input_mode": "setpoints",
        "model_family": "integrated_specialist_a02",
        "model_type": "routed_k01_h08_curve_composition",
        "candidate_id": "A02",
        "surface": "global",
        "random_seed": 314159,
        "run_instance_id": "2026-08-03-17-49-51__a02__seed_314159",
        "source_output_directory": project_relative_path(SOURCE_RUN_DIRECTORY),
        "source_best_checkpoint_path": project_relative_path(
            SOURCE_RUN_DIRECTORY / "best_model.pt"
        ),
        "python_model_path": project_relative_path(
            final_root / "python" / "best_model.pt"
        ),
        "onnx_model_path": project_relative_path(
            final_root / "onnx" / "model.onnx"
        ),
        "onnx_export_status": "exported",
        "onnx_export_error": "",
        "onnx_role": "fixed_shape_curve_composer_requiring_k01_and_h08_curves",
        "checkpoint_sha256": compute_file_sha256(checkpoint_source),
        "onnx_sha256": compute_file_sha256(onnx_source),
        "split_signature": (
            "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
        ),
        "acceptance_status": "verified_offline_candidate_not_registry_replacement",
        "archive_role": "forward_specialist_routed_global_composition",
        "deployment_status": (
            "export_prepared_host_and_plc_reference_qualified_twincat_runtime_pending"
        ),
        "dependency_archive_path_map": {
            "global_k01": (
                "models/polished_dataset/setpoints/"
                "temporal_analytical_residual_k01/global"
            ),
            "forward_h08": (
                "models/polished_dataset/setpoints/"
                "complex_harmonic_coefficient_h08/forward"
            ),
        },
        "surface_contract": summary["surface_contract"],
        "input_shape": summary["input_shape"],
        "known_limitations": [
            "composer_requires_complete_2048_sample_k01_and_h08_curves",
            "k01_requires_stateful_32_sample_chunk_execution_and_h04_anchor_inputs",
            "fixed_grid_replay_is_not_continuously_varying_online_compensation",
            "twincat_build_target_activation_ads_license_and_latency_pending",
            "accepted_deployment_registries_unchanged",
        ],
        "source_run_snapshot_path_map": {
            path.name: project_relative_path(final_root / "source_run" / path.name)
            for path in sorted((STAGING_ROOT / "source_run").iterdir())
        },
        "deployment_artifact_path_map": {
            "gate_parameters": project_relative_path(
                final_root / "deployment" / "a02_gate_parameters.npz"
            ),
            "plc_parameter_source": project_relative_path(
                final_root
                / "plc_reference"
                / "GVL_Wave52rA02Parameters.st"
            ),
            "plc_composer_source": project_relative_path(
                final_root
                / "plc_reference"
                / "FB_Wave52rA02CurveComposer.st"
            ),
        },
        "parity": summary["parity"],
        "metrics": load_a02_official_metrics(),
    }
    write_yaml(STAGING_ROOT / "reference_inventory.yaml", inventory)
    staged_inventory = read_yaml(STAGING_ROOT / "reference_inventory.yaml")
    assert compute_file_sha256(
        STAGING_ROOT / "python" / "best_model.pt"
    ) == staged_inventory["checkpoint_sha256"]
    assert compute_file_sha256(
        STAGING_ROOT / "onnx" / "model.onnx"
    ) == staged_inventory["onnx_sha256"]
    return inventory


def promote_archive() -> dict[str, Any]:
    """Install the staged leaf and rebuild the canonical aggregate inventory."""

    if ARCHIVE_ROOT.exists():
        if tree_digest_map(ARCHIVE_ROOT) != tree_digest_map(STAGING_ROOT):
            raise FileExistsError(
                "Installed A02 archive differs from the validated staged leaf: "
                f"{ARCHIVE_ROOT}"
            )
    else:
        ARCHIVE_ROOT.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(STAGING_ROOT, ARCHIVE_ROOT)
    aggregate = rebuild_aggregate_inventory()
    assert aggregate["entry_count"] == 114
    assert aggregate["surface_counts"] == {
        "global": 38,
        "forward": 39,
        "backward": 37,
    }
    assert aggregate["onnx_export_status_counts"] == {"exported": 114}
    return aggregate


def main() -> None:
    """Stage and optionally install the approved A02 archive."""

    arguments = parse_arguments()
    inventory = stage_archive(arguments.source_directory)
    if arguments.promote:
        aggregate = promote_archive()
        print(
            "[PASS] Promoted Wave 5.2R A02 archive | "
            f"entries={aggregate['entry_count']} | "
            f"checkpoint={inventory['checkpoint_sha256'][:12]} | "
            f"onnx={inventory['onnx_sha256'][:12]}",
            flush=True,
        )
    else:
        print(
            "[PASS] Staged Wave 5.2R A02 archive | "
            f"path={project_relative_path(STAGING_ROOT)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
