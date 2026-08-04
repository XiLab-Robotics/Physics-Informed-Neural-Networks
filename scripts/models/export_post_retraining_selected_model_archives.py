"""Export the approved post-retraining Wave 5.2R model archive leaves."""

from __future__ import annotations

# Import Python Utilities
import argparse
import hashlib
from pathlib import Path
import shutil
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import onnx
import onnxruntime as ort
import torch
import yaml

# Import Repository Campaign And Export Utilities
from scripts.analysis.wave_5_2r.validate_wave52r_offline_leader_promotion import (
    H08OnnxWrapper,
    K01StatefulOnnxWrapper,
    run_k01_onnx_curve,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_offline_leader_cross_surface_promotion as promotion,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)


# Define The Approved Archive Contract
ARCHIVE_DATASET_ID = "polished_dataset"
ARCHIVE_DATASET_SCHEMA = "polished_setpoint_curve_v1"
ARCHIVE_INPUT_MODE = "setpoints"
ARCHIVE_ROOT = PROJECT_ROOT / "models" / ARCHIVE_DATASET_ID / ARCHIVE_INPUT_MODE
DEFAULT_STAGING_ROOT = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "post_retraining_model_archive_promotion"
    / "staged_models"
)
OFFICIAL_DECISION_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "offline_leader_cross_surface_track2"
    / "official_promotion_decision.yaml"
)
STAGE15_DECISION_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage15_official_forward_verification"
    / "closeout"
    / "stage15_official_forward_verification_decision.yaml"
)
STAGE15_PARITY_ROOT = (
    PROJECT_ROOT
    / "output"
    / "validation_checks"
    / "wave52r_stage15_deployment_parity"
)
H04_SOURCE_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
)
ONNX_OPSET_VERSION = 17
K01_EXPORT_CHUNK_LENGTH = 32
CURVE_PARITY_TOLERANCE_DEG = 2.0e-6
COEFFICIENT_PARITY_TOLERANCE_DEG = 1.0e-6
K01_REPLAY_TOLERANCE_DEG = 5.0e-5
K01_HIDDEN_STATE_TOLERANCE = 2.0e-5

SELECTED_K01_RUN_DIRECTORY_BY_SURFACE = {
    "forward": PROJECT_ROOT
    / "output/training_runs/temporal_analytical_residual_models"
    / "2026-07-31-10-45-41__stage9_k01__seed_271828",
    "backward": PROJECT_ROOT
    / "output/training_runs/temporal_analytical_residual_models"
    / "2026-07-31-10-55-28__stage9_k01__seed_271828",
    "global": PROJECT_ROOT
    / "output/training_runs/temporal_analytical_residual_models"
    / "2026-07-31-11-11-39__stage9_k01__seed_271828",
}
PAIRED_H04_RUN_DIRECTORY_BY_SURFACE = {
    "forward": PROJECT_ROOT
    / "output/training_runs/complex_harmonic_coefficient_residuals"
    / "2026-07-31-10-42-28__stage5_h04__seed_271828",
    "backward": PROJECT_ROOT
    / "output/training_runs/complex_harmonic_coefficient_residuals"
    / "2026-07-31-10-52-12__stage5_h04__seed_271828",
    "global": PROJECT_ROOT
    / "output/training_runs/complex_harmonic_coefficient_residuals"
    / "2026-07-31-11-05-16__stage5_h04__seed_271828",
}
H08_SOURCE_RUN_DIRECTORY = (
    PROJECT_ROOT
    / "output/training_runs/complex_harmonic_coefficient_residuals"
    / "2026-07-31-10-45-42__stage5_h08__seed_161803"
)
SURFACE_CAMPAIGN_LABEL = {
    "forward": "Fw",
    "backward": "Bw",
    "global": "global",
}


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse staging and promotion arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--staging-root",
        type=Path,
        default=DEFAULT_STAGING_ROOT,
        help="Temporary root used to build and validate the five approved leaves.",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="Copy validated staged leaves into models/ and rebuild the aggregate inventory.",
    )
    parser.add_argument(
        "--validate-existing",
        action="store_true",
        help="Validate the installed aggregate inventory and artifact paths without rebuilding staging.",
    )
    return parser.parse_args()


def project_relative_path(path: Path) -> str:
    """Return one repository-relative POSIX path."""

    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def compute_file_sha256(path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            digest.update(byte_chunk)
    return digest.hexdigest()


def read_yaml(path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {path}"
    return payload


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a single final newline."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def copy_file(source_path: Path, destination_path: Path) -> None:
    """Copy one required immutable artifact."""

    assert source_path.is_file(), f"Missing source artifact | {source_path}"
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)


def build_onnx_session(onnx_path: Path) -> ort.InferenceSession:
    """Build one deterministic single-threaded CPU inference session."""

    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    session_options = ort.SessionOptions()
    session_options.intra_op_num_threads = 1
    session_options.inter_op_num_threads = 1
    return ort.InferenceSession(
        str(onnx_path),
        sess_options=session_options,
        providers=["CPUExecutionProvider"],
    )


def load_all_curve_records() -> list[Any]:
    """Load the frozen Wave 5.2R split once for all selected surfaces."""

    phase1_configuration = stage5.load_yaml(stage5.PHASE1_CONFIGURATION_PATH)
    common_split_manifest = stage5.load_yaml(stage5.COMMON_SPLIT_MANIFEST_PATH)
    return stage5.load_curve_records(
        phase1_configuration,
        common_split_manifest,
    )


def build_leaf_root(staging_root: Path, family_name: str, surface: str) -> Path:
    """Return one staging leaf root."""

    return staging_root / family_name / surface


def copy_source_run_snapshots(
    source_run_directory: Path,
    leaf_root: Path,
) -> dict[str, str]:
    """Copy available source-run metadata into one immutable archive leaf."""

    source_run_root = leaf_root / "source_run"
    source_name_target_name_list = [
        ("metrics_summary.yaml", "metrics_summary.snapshot.yaml"),
        ("promotion_metadata.yaml", "promotion_metadata.snapshot.yaml"),
        ("training_config.yaml", "training_config.snapshot.yaml"),
        ("training_history.csv", "training_history.snapshot.csv"),
    ]
    copied_path_map = {}
    final_leaf_root = ARCHIVE_ROOT / leaf_root.relative_to(leaf_root.parents[1])
    for source_name, target_name in source_name_target_name_list:
        source_path = source_run_directory / source_name
        if not source_path.is_file():
            continue
        target_path = source_run_root / target_name
        copy_file(source_path, target_path)
        copied_path_map[target_name] = (
            final_leaf_root / "source_run" / target_name
        ).relative_to(PROJECT_ROOT).as_posix()
    return copied_path_map


def export_k01_leaf(
    all_record_list: list[Any],
    staging_root: Path,
    surface: str,
) -> dict[str, Any]:
    """Export and validate one selected K01 surface."""

    campaign_surface = SURFACE_CAMPAIGN_LABEL[surface]
    source_run_directory = SELECTED_K01_RUN_DIRECTORY_BY_SURFACE[surface]
    paired_h04_run_directory = PAIRED_H04_RUN_DIRECTORY_BY_SURFACE[surface]
    checkpoint_path = source_run_directory / "best_model.pt"
    paired_h04_checkpoint_path = paired_h04_run_directory / "best_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    assert checkpoint_payload["candidate"]["candidate_id"] == "K01"
    dataset, dataset_contract = promotion.build_surface_dataset(
        all_record_list,
        campaign_surface,
    )
    anchor_bundle = promotion.build_h04_anchor_bundle(
        dataset,
        paired_h04_checkpoint_path,
    )
    specification = next(
        candidate
        for candidate in stage9.build_candidate_list()
        if candidate.candidate_id == "K01"
    )
    model_object = stage9.build_model(specification, dataset)
    model_object.load_state_dict(checkpoint_payload["state_dict"], strict=True)
    model_object.eval()
    anchor_curve_matrix, anchor_coefficient_matrix = stage9.anchor_arrays_for_candidate(
        specification,
        anchor_bundle,
    )
    assert anchor_coefficient_matrix is not None
    test_batch = stage9.build_split_tensors(
        dataset,
        anchor_curve_matrix,
        anchor_coefficient_matrix,
        "test",
        torch.device("cpu"),
    )

    # Reproduce The Saved Checkpoint Payload And Stateful Contract
    replay_prediction_matrix, _, recurrent_metrics = stage9.predict_model(
        model_object,
        test_batch["condition"],
        test_batch["anchor"],
        test_batch["anchor_coefficient"],
        test_batch["angle"],
        stage9.DEFAULT_CHUNK_LENGTH,
    )
    with np.load(source_run_directory / "test_predictions.npz") as frozen_payload:
        replay_max_abs_difference_deg = float(
            np.max(np.abs(replay_prediction_matrix - frozen_payload["predicted_curve"]))
        )
    assert replay_max_abs_difference_deg <= K01_REPLAY_TOLERANCE_DEG
    assert recurrent_metrics["reset_reproducibility_max_abs_deg"] == 0.0
    assert (
        recurrent_metrics["chunk_equivalence_max_abs_deg"]
        <= K01_REPLAY_TOLERANCE_DEG
    )

    # Export One Fixed-Chunk Graph With Explicit Hidden-State Carry
    leaf_root = build_leaf_root(
        staging_root,
        "temporal_analytical_residual_k01",
        surface,
    )
    onnx_path = leaf_root / "onnx" / "model.onnx"
    python_path = leaf_root / "python" / "best_model.pt"
    copy_file(checkpoint_path, python_path)
    onnx_path.parent.mkdir(parents=True, exist_ok=True)
    first_angle = test_batch["angle"][:1]
    export_hidden_state = model_object.initial_hidden_state(1, first_angle)
    export_wrapper = K01StatefulOnnxWrapper(model_object)
    export_wrapper.eval()
    with torch.no_grad():
        torch.onnx.export(
            export_wrapper,
            (
                first_angle[:, :K01_EXPORT_CHUNK_LENGTH],
                test_batch["condition"][:1],
                test_batch["anchor"][:1, :K01_EXPORT_CHUNK_LENGTH],
                test_batch["anchor_coefficient"][:1],
                export_hidden_state,
            ),
            onnx_path,
            input_names=[
                "angular_position_deg",
                "condition",
                "analytical_anchor_curve",
                "analytical_anchor_coefficients",
                "hidden_state",
            ],
            output_names=[
                "prediction_curve",
                "residual_curve",
                "coefficient_correction",
                "predicted_coefficient",
                "final_hidden_state",
            ],
            opset_version=ONNX_OPSET_VERSION,
            do_constant_folding=True,
            dynamo=False,
        )

    # Validate The Full Held-Out Surface Through ONNX Runtime
    onnx_session = build_onnx_session(onnx_path)
    with torch.inference_mode():
        pytorch_output = model_object.forward_in_chunks(
            test_batch["angle"],
            test_batch["condition"],
            test_batch["anchor"],
            test_batch["anchor_coefficient"],
            chunk_length=K01_EXPORT_CHUNK_LENGTH,
        )
    onnx_prediction_list = []
    onnx_hidden_list = []
    for condition_index in range(test_batch["condition"].shape[0]):
        onnx_prediction, onnx_hidden = run_k01_onnx_curve(
            onnx_session,
            test_batch["angle"][condition_index].numpy(),
            test_batch["condition"][condition_index].numpy(),
            test_batch["anchor"][condition_index].numpy(),
            test_batch["anchor_coefficient"][condition_index].numpy(),
            model_object.hidden_size,
            model_object.num_layers,
        )
        onnx_prediction_list.append(onnx_prediction[0])
        onnx_hidden_list.append(onnx_hidden[:, 0, :])
    onnx_prediction_matrix = np.vstack(onnx_prediction_list)
    onnx_hidden_matrix = np.stack(onnx_hidden_list, axis=1)
    curve_parity_max_abs_difference_deg = float(
        np.max(
            np.abs(
                pytorch_output["prediction_curve"].numpy()
                - onnx_prediction_matrix
            )
        )
    )
    hidden_parity_max_abs_difference = float(
        np.max(
            np.abs(
                pytorch_output["final_hidden_state"].numpy()
                - onnx_hidden_matrix
            )
        )
    )
    assert curve_parity_max_abs_difference_deg <= CURVE_PARITY_TOLERANCE_DEG
    assert hidden_parity_max_abs_difference <= K01_HIDDEN_STATE_TOLERANCE

    metrics_payload = read_yaml(source_run_directory / "metrics_summary.yaml")
    source_snapshot_map = copy_source_run_snapshots(
        source_run_directory,
        leaf_root,
    )
    copy_file(
        OFFICIAL_DECISION_PATH,
        leaf_root / "source_run" / "official_promotion_decision.snapshot.yaml",
    )
    source_snapshot_map["official_promotion_decision.snapshot.yaml"] = (
        ARCHIVE_ROOT
        / "temporal_analytical_residual_k01"
        / surface
        / "source_run"
        / "official_promotion_decision.snapshot.yaml"
    ).relative_to(PROJECT_ROOT).as_posix()
    parity_payload = {
        "schema_version": 1,
        "status": "passed",
        "candidate_id": "K01",
        "surface": surface,
        "held_out_curve_count": int(test_batch["condition"].shape[0]),
        "fixed_chunk_length": K01_EXPORT_CHUNK_LENGTH,
        "checkpoint_replay_max_abs_difference_deg": replay_max_abs_difference_deg,
        "reset_reproducibility_max_abs_deg": recurrent_metrics[
            "reset_reproducibility_max_abs_deg"
        ],
        "chunk_equivalence_max_abs_deg": recurrent_metrics[
            "chunk_equivalence_max_abs_deg"
        ],
        "onnx_curve_max_abs_difference_deg": curve_parity_max_abs_difference_deg,
        "onnx_hidden_state_max_abs_difference": hidden_parity_max_abs_difference,
    }
    write_yaml(leaf_root / "validation" / "archive_parity_summary.yaml", parity_payload)
    return {
        "schema_version": 1,
        "dataset_id": ARCHIVE_DATASET_ID,
        "dataset_schema": ARCHIVE_DATASET_SCHEMA,
        "input_mode": ARCHIVE_INPUT_MODE,
        "model_family": "temporal_analytical_residual_k01",
        "model_type": "causal_temporal_analytical_residual",
        "candidate_id": "K01",
        "surface": surface,
        "random_seed": 271828,
        "run_instance_id": metrics_payload["run_instance_id"],
        "source_output_directory": project_relative_path(source_run_directory),
        "source_best_checkpoint_path": project_relative_path(checkpoint_path),
        "source_paired_h04_checkpoint_path": project_relative_path(
            paired_h04_checkpoint_path
        ),
        "python_model_path": (
            ARCHIVE_ROOT
            / "temporal_analytical_residual_k01"
            / surface
            / "python"
            / "best_model.pt"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_model_path": (
            ARCHIVE_ROOT
            / "temporal_analytical_residual_k01"
            / surface
            / "onnx"
            / "model.onnx"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_export_status": "exported",
        "onnx_export_error": "",
        "checkpoint_sha256": compute_file_sha256(checkpoint_path),
        "onnx_sha256": compute_file_sha256(onnx_path),
        "split_signature": dataset_contract["split_signature"],
        "acceptance_status": "promoted_cross_surface_offline_leader",
        "archive_role": "temporal_offline_leader",
        "deployment_status": "export_prepared_host_qualified_twincat_runtime_pending",
        "known_limitations": (
            ["backward_peak_to_peak_regression"]
            if surface == "backward"
            else []
        ),
        "source_run_snapshot_path_map": source_snapshot_map,
        "parity": parity_payload,
        "metrics": {
            "validation_mae_deg": metrics_payload["best_validation_mae_deg"],
            "test_mae_deg": metrics_payload["mae_deg"],
            "test_rmse_deg": metrics_payload["rmse_deg"],
            "centered_mae_deg": metrics_payload["centered_mae_deg"],
            "offset_abs_error_deg": metrics_payload["offset_abs_error_deg"],
        },
    }


def export_h08_forward_leaf(
    all_record_list: list[Any],
    staging_root: Path,
) -> dict[str, Any]:
    """Export and validate the selected H08 forward specialist."""

    surface = "forward"
    dataset, dataset_contract = promotion.build_surface_dataset(
        all_record_list,
        "Fw",
    )
    checkpoint_path = H08_SOURCE_RUN_DIRECTORY / "best_model.pt"
    checkpoint_payload = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    assert checkpoint_payload["candidate"]["candidate_id"] == "H08"
    specification = next(
        candidate
        for candidate in stage5.build_candidate_list()
        if candidate.candidate_id == "H08"
    )
    model_object = stage5.build_model(specification, dataset)
    model_object.load_state_dict(checkpoint_payload["state_dict"], strict=True)
    model_object.eval()
    test_batch = stage5.tensor_dataset_for_split(
        dataset,
        "data_selected",
        "test",
        torch.device("cpu"),
    )
    with torch.inference_mode():
        pytorch_output = model_object(
            test_batch["condition"],
            test_batch["anchor"],
        )
    with np.load(H08_SOURCE_RUN_DIRECTORY / "test_predictions.npz") as frozen_payload:
        replay_curve_max_abs_difference_deg = float(
            np.max(
                np.abs(
                    pytorch_output["prediction_curve"].numpy()
                    - frozen_payload["predicted_curve"]
                )
            )
        )
        replay_coefficient_max_abs_difference_deg = float(
            np.max(
                np.abs(
                    pytorch_output["prediction_coefficients"].numpy()
                    - frozen_payload["predicted_coefficient"]
                )
            )
        )
    assert replay_curve_max_abs_difference_deg <= CURVE_PARITY_TOLERANCE_DEG
    assert replay_coefficient_max_abs_difference_deg <= COEFFICIENT_PARITY_TOLERANCE_DEG

    leaf_root = build_leaf_root(
        staging_root,
        "complex_harmonic_coefficient_h08",
        surface,
    )
    python_path = leaf_root / "python" / "best_model.pt"
    onnx_path = leaf_root / "onnx" / "model.onnx"
    copy_file(checkpoint_path, python_path)
    onnx_path.parent.mkdir(parents=True, exist_ok=True)
    export_wrapper = H08OnnxWrapper(model_object)
    export_wrapper.eval()
    with torch.no_grad():
        torch.onnx.export(
            export_wrapper,
            (test_batch["condition"][:1], test_batch["anchor"][:1]),
            onnx_path,
            input_names=[
                "normalized_condition",
                "analytical_anchor_coefficients",
            ],
            output_names=[
                "prediction_curve",
                "prediction_coefficients",
                "coefficient_correction",
                "analytical_contribution_curve",
            ],
            dynamic_axes={
                "normalized_condition": {0: "batch"},
                "analytical_anchor_coefficients": {0: "batch"},
                "prediction_curve": {0: "batch"},
                "prediction_coefficients": {0: "batch"},
                "coefficient_correction": {0: "batch"},
                "analytical_contribution_curve": {0: "batch"},
            },
            opset_version=ONNX_OPSET_VERSION,
            do_constant_folding=True,
            dynamo=False,
        )
    onnx_session = build_onnx_session(onnx_path)
    onnx_output_list = onnx_session.run(
        None,
        {
            "normalized_condition": np.ascontiguousarray(test_batch["condition"].numpy()),
            "analytical_anchor_coefficients": np.ascontiguousarray(
                test_batch["anchor"].numpy()
            ),
        },
    )
    onnx_curve_max_abs_difference_deg = float(
        np.max(
            np.abs(
                pytorch_output["prediction_curve"].numpy()
                - onnx_output_list[0]
            )
        )
    )
    onnx_coefficient_max_abs_difference_deg = float(
        np.max(
            np.abs(
                pytorch_output["prediction_coefficients"].numpy()
                - onnx_output_list[1]
            )
        )
    )
    assert onnx_curve_max_abs_difference_deg <= CURVE_PARITY_TOLERANCE_DEG
    assert onnx_coefficient_max_abs_difference_deg <= COEFFICIENT_PARITY_TOLERANCE_DEG
    metrics_payload = read_yaml(H08_SOURCE_RUN_DIRECTORY / "metrics_summary.yaml")
    source_snapshot_map = copy_source_run_snapshots(H08_SOURCE_RUN_DIRECTORY, leaf_root)
    copy_file(
        OFFICIAL_DECISION_PATH,
        leaf_root / "source_run" / "official_promotion_decision.snapshot.yaml",
    )
    source_snapshot_map["official_promotion_decision.snapshot.yaml"] = (
        ARCHIVE_ROOT
        / "complex_harmonic_coefficient_h08"
        / surface
        / "source_run"
        / "official_promotion_decision.snapshot.yaml"
    ).relative_to(PROJECT_ROOT).as_posix()
    parity_payload = {
        "schema_version": 1,
        "status": "passed",
        "candidate_id": "H08",
        "surface": surface,
        "held_out_curve_count": int(test_batch["condition"].shape[0]),
        "checkpoint_curve_max_abs_difference_deg": replay_curve_max_abs_difference_deg,
        "checkpoint_coefficient_max_abs_difference_deg": (
            replay_coefficient_max_abs_difference_deg
        ),
        "onnx_curve_max_abs_difference_deg": onnx_curve_max_abs_difference_deg,
        "onnx_coefficient_max_abs_difference_deg": (
            onnx_coefficient_max_abs_difference_deg
        ),
    }
    write_yaml(leaf_root / "validation" / "archive_parity_summary.yaml", parity_payload)
    return {
        "schema_version": 1,
        "dataset_id": ARCHIVE_DATASET_ID,
        "dataset_schema": ARCHIVE_DATASET_SCHEMA,
        "input_mode": ARCHIVE_INPUT_MODE,
        "model_family": "complex_harmonic_coefficient_h08",
        "model_type": "complex_harmonic_coefficient_residual",
        "candidate_id": "H08",
        "surface": surface,
        "random_seed": 161803,
        "run_instance_id": metrics_payload["run_instance_id"],
        "source_output_directory": project_relative_path(H08_SOURCE_RUN_DIRECTORY),
        "source_best_checkpoint_path": project_relative_path(checkpoint_path),
        "python_model_path": (
            ARCHIVE_ROOT
            / "complex_harmonic_coefficient_h08"
            / surface
            / "python"
            / "best_model.pt"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_model_path": (
            ARCHIVE_ROOT
            / "complex_harmonic_coefficient_h08"
            / surface
            / "onnx"
            / "model.onnx"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_export_status": "exported",
        "onnx_export_error": "",
        "checkpoint_sha256": compute_file_sha256(checkpoint_path),
        "onnx_sha256": compute_file_sha256(onnx_path),
        "split_signature": dataset_contract["split_signature"],
        "acceptance_status": "retained_forward_offline_specialist",
        "archive_role": "non_temporal_forward_specialist",
        "deployment_status": "export_prepared_host_qualified_twincat_runtime_pending",
        "known_limitations": [
            "backward_not_archived_due_to_raw_offset_and_closure_regressions",
            "global_not_archived_due_to_raw_offset_shape_and_derivative_regressions",
        ],
        "source_run_snapshot_path_map": source_snapshot_map,
        "parity": parity_payload,
        "metrics": metrics_payload["test_metrics"],
    }


def export_h04_forward_leaf(staging_root: Path) -> dict[str, Any]:
    """Stage the already validated Stage 15 H04 deployment package."""

    surface = "forward"
    checkpoint_path = H04_SOURCE_RUN_DIRECTORY / "best_model.pt"
    onnx_source_path = STAGE15_PARITY_ROOT / "h04_bounded_coefficient_residual.onnx"
    onnx_summary_path = STAGE15_PARITY_ROOT / "stage15_onnx_parity_summary.yaml"
    plc_summary_path = STAGE15_PARITY_ROOT / "stage15_plc_static_parity_summary.yaml"
    onnx_summary = read_yaml(onnx_summary_path)
    plc_summary = read_yaml(plc_summary_path)
    assert onnx_summary["status"] == "passed"
    assert onnx_summary["python_onnx_parity_passed"] is True
    assert plc_summary["status"] == "passed"
    assert plc_summary["static_plc_reference_parity_passed"] is True
    assert compute_file_sha256(onnx_source_path) == onnx_summary["onnx_sha256"]
    build_onnx_session(onnx_source_path)

    leaf_root = build_leaf_root(
        staging_root,
        "complex_harmonic_coefficient_h04",
        surface,
    )
    python_path = leaf_root / "python" / "best_model.pt"
    onnx_path = leaf_root / "onnx" / "model.onnx"
    copy_file(checkpoint_path, python_path)
    copy_file(onnx_source_path, onnx_path)
    deployment_asset_name_list = [
        "FB_Stage15H04CoefficientResidual.st",
        "GVL_Stage15H04Parameters.st",
        "stage15_h04_plc_parameter_archive.npz",
    ]
    for asset_name in deployment_asset_name_list:
        copy_file(
            STAGE15_PARITY_ROOT / asset_name,
            leaf_root / "deployment_reference" / asset_name,
        )
    copy_file(
        onnx_summary_path,
        leaf_root / "validation" / "stage15_onnx_parity_summary.yaml",
    )
    copy_file(
        plc_summary_path,
        leaf_root / "validation" / "stage15_plc_static_parity_summary.yaml",
    )
    source_snapshot_map = copy_source_run_snapshots(H04_SOURCE_RUN_DIRECTORY, leaf_root)
    copy_file(
        STAGE15_DECISION_PATH,
        leaf_root / "source_run" / "stage15_decision.snapshot.yaml",
    )
    source_snapshot_map["stage15_decision.snapshot.yaml"] = (
        ARCHIVE_ROOT
        / "complex_harmonic_coefficient_h04"
        / surface
        / "source_run"
        / "stage15_decision.snapshot.yaml"
    ).relative_to(PROJECT_ROOT).as_posix()
    metrics_payload = read_yaml(H04_SOURCE_RUN_DIRECTORY / "metrics_summary.yaml")
    training_config_payload = read_yaml(
        H04_SOURCE_RUN_DIRECTORY / "training_config.yaml"
    )
    return {
        "schema_version": 1,
        "dataset_id": ARCHIVE_DATASET_ID,
        "dataset_schema": ARCHIVE_DATASET_SCHEMA,
        "input_mode": ARCHIVE_INPUT_MODE,
        "model_family": "complex_harmonic_coefficient_h04",
        "model_type": "complex_harmonic_coefficient_residual",
        "candidate_id": "H04",
        "surface": surface,
        "random_seed": training_config_payload["random_seed"],
        "run_instance_id": metrics_payload["run_instance_id"],
        "source_output_directory": project_relative_path(H04_SOURCE_RUN_DIRECTORY),
        "source_best_checkpoint_path": project_relative_path(checkpoint_path),
        "python_model_path": (
            ARCHIVE_ROOT
            / "complex_harmonic_coefficient_h04"
            / surface
            / "python"
            / "best_model.pt"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_model_path": (
            ARCHIVE_ROOT
            / "complex_harmonic_coefficient_h04"
            / surface
            / "onnx"
            / "model.onnx"
        ).relative_to(PROJECT_ROOT).as_posix(),
        "onnx_export_status": "exported",
        "onnx_export_error": "",
        "checkpoint_sha256": compute_file_sha256(checkpoint_path),
        "onnx_sha256": compute_file_sha256(onnx_path),
        "split_signature": stage5.SPLIT_SIGNATURE,
        "acceptance_status": "exploratory_grey_box_specialist",
        "archive_role": "compact_interpretable_forward_grey_box",
        "deployment_status": "static_plc_reference_parity_passed_twincat_runtime_pending",
        "known_limitations": [
            "does_not_beat_periodic_gru_on_raw_offset_p95_or_peak_to_peak",
            "twincat_compile_and_runtime_replay_pending",
            "backward_and_global_not_officially_verified_for_archive_promotion",
        ],
        "source_run_snapshot_path_map": source_snapshot_map,
        "parity": {
            "python_onnx": onnx_summary,
            "plc_static_reference": plc_summary,
        },
        "metrics": metrics_payload["test_metrics"],
    }


def validate_staged_inventory(
    staging_root: Path,
    inventory_list: list[dict[str, Any]],
) -> None:
    """Validate the exact five-leaf staged artifact contract."""

    expected_key_set = {
        ("temporal_analytical_residual_k01", "forward"),
        ("temporal_analytical_residual_k01", "backward"),
        ("temporal_analytical_residual_k01", "global"),
        ("complex_harmonic_coefficient_h08", "forward"),
        ("complex_harmonic_coefficient_h04", "forward"),
    }
    observed_key_set = {
        (str(entry["model_family"]), str(entry["surface"]))
        for entry in inventory_list
    }
    assert observed_key_set == expected_key_set
    inventory_path_list = sorted(staging_root.glob("*/*/reference_inventory.yaml"))
    assert len(inventory_path_list) == 5
    for inventory_path in inventory_path_list:
        inventory = read_yaml(inventory_path)
        assert inventory["onnx_export_status"] == "exported"
        leaf_root = inventory_path.parent
        assert (leaf_root / "python" / "best_model.pt").is_file()
        assert (leaf_root / "onnx" / "model.onnx").is_file()
        assert compute_file_sha256(leaf_root / "python" / "best_model.pt") == (
            inventory["checkpoint_sha256"]
        )
        assert compute_file_sha256(leaf_root / "onnx" / "model.onnx") == (
            inventory["onnx_sha256"]
        )


def rebuild_aggregate_inventory() -> dict[str, Any]:
    """Regenerate the polished-setpoint aggregate inventory from leaf provenance."""

    inventory_list = [
        read_yaml(path)
        for path in ARCHIVE_ROOT.glob("*/*/reference_inventory.yaml")
    ]
    inventory_list.sort(
        key=lambda entry: (str(entry["model_family"]), str(entry["surface"]))
    )
    surface_count_dictionary = {
        surface: sum(1 for entry in inventory_list if entry["surface"] == surface)
        for surface in ("global", "forward", "backward")
    }
    export_status_count_dictionary: dict[str, int] = {}
    for entry in inventory_list:
        status = str(entry["onnx_export_status"])
        export_status_count_dictionary[status] = (
            export_status_count_dictionary.get(status, 0) + 1
        )
    aggregate_payload = {
        "schema_version": 1,
        "dataset_id": ARCHIVE_DATASET_ID,
        "input_mode": ARCHIVE_INPUT_MODE,
        "entry_count": len(inventory_list),
        "surface_counts": surface_count_dictionary,
        "onnx_export_status_counts": export_status_count_dictionary,
        "entries": inventory_list,
    }
    write_yaml(
        ARCHIVE_ROOT / "model_development_export_inventory.yaml",
        aggregate_payload,
    )
    return aggregate_payload


def promote_staged_leaves(staging_root: Path) -> dict[str, Any]:
    """Copy the validated five-leaf staging bundle into the canonical archive."""

    for family_root in sorted(path for path in staging_root.iterdir() if path.is_dir()):
        target_family_root = ARCHIVE_ROOT / family_root.name
        assert not target_family_root.exists(), (
            f"Refusing to overwrite existing archive family | {target_family_root}"
        )
        shutil.copytree(family_root, target_family_root)
    aggregate_payload = rebuild_aggregate_inventory()
    assert aggregate_payload["entry_count"] == 113
    assert aggregate_payload["surface_counts"] == {
        "global": 37,
        "forward": 39,
        "backward": 37,
    }
    assert aggregate_payload["onnx_export_status_counts"] == {"exported": 113}
    return aggregate_payload


def validate_existing_archive() -> None:
    """Validate the installed aggregate inventory, paths, and available hashes."""

    aggregate_path = ARCHIVE_ROOT / "model_development_export_inventory.yaml"
    aggregate_payload = read_yaml(aggregate_path)
    inventory_path_list = sorted(ARCHIVE_ROOT.glob("*/*/reference_inventory.yaml"))
    assert aggregate_payload["entry_count"] == len(inventory_path_list) == 114
    assert aggregate_payload["surface_counts"] == {
        "global": 38,
        "forward": 39,
        "backward": 37,
    }
    assert aggregate_payload["onnx_export_status_counts"] == {"exported": 114}

    hashed_artifact_count = 0
    for inventory_path in inventory_path_list:
        inventory = read_yaml(inventory_path)
        python_model_path = PROJECT_ROOT / str(inventory["python_model_path"])
        onnx_model_path = PROJECT_ROOT / str(inventory["onnx_model_path"])
        assert python_model_path.is_file(), python_model_path
        assert onnx_model_path.is_file(), onnx_model_path
        if "checkpoint_sha256" in inventory:
            assert compute_file_sha256(python_model_path) == inventory["checkpoint_sha256"]
            hashed_artifact_count += 1
        if "onnx_sha256" in inventory:
            assert compute_file_sha256(onnx_model_path) == inventory["onnx_sha256"]
            hashed_artifact_count += 1

    assert hashed_artifact_count == 12
    print(
        "[PASS] Existing archive inventory | "
        f"entry_count={len(inventory_path_list)} | "
        f"hashed_artifacts={hashed_artifact_count}",
        flush=True,
    )


def main() -> None:
    """Stage, validate, and optionally promote the approved archive leaves."""

    arguments = parse_command_line_arguments()
    assert not (arguments.promote and arguments.validate_existing), (
        "--promote and --validate-existing are mutually exclusive"
    )
    if arguments.validate_existing:
        validate_existing_archive()
        return
    staging_root = arguments.staging_root.resolve()
    assert staging_root.is_relative_to(PROJECT_ROOT), (
        f"Staging root must remain inside the repository | {staging_root}"
    )
    if staging_root.exists():
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True, exist_ok=False)

    all_record_list = load_all_curve_records()
    inventory_list = [
        export_k01_leaf(all_record_list, staging_root, surface)
        for surface in ("forward", "backward", "global")
    ]
    inventory_list.append(export_h08_forward_leaf(all_record_list, staging_root))
    inventory_list.append(export_h04_forward_leaf(staging_root))
    for inventory in inventory_list:
        inventory_path = (
            staging_root
            / str(inventory["model_family"])
            / str(inventory["surface"])
            / "reference_inventory.yaml"
        )
        write_yaml(inventory_path, inventory)
    validate_staged_inventory(staging_root, inventory_list)
    write_yaml(
        staging_root.parent / "staged_archive_summary.yaml",
        {
            "schema_version": 1,
            "status": "passed",
            "staged_leaf_count": len(inventory_list),
            "staged_key_list": [
                {
                    "model_family": entry["model_family"],
                    "surface": entry["surface"],
                    "checkpoint_sha256": entry["checkpoint_sha256"],
                    "onnx_sha256": entry["onnx_sha256"],
                }
                for entry in inventory_list
            ],
        },
    )
    print(f"[PASS] Staged archive leaves: {len(inventory_list)}", flush=True)

    if arguments.promote:
        aggregate_payload = promote_staged_leaves(staging_root)
        print(
            "[PASS] Promoted archive leaves | "
            f"entry_count={aggregate_payload['entry_count']} | "
            f"surface_counts={aggregate_payload['surface_counts']}",
            flush=True,
        )


if __name__ == "__main__":
    main()
