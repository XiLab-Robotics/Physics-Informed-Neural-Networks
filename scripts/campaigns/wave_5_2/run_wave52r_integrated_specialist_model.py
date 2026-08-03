"""Preflight and run the Wave 5.2R integrated-specialist campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from datetime import datetime
import hashlib
from pathlib import Path
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import torch
import yaml

# Import Repository Models And Campaign Utilities
from scripts.campaigns.wave_5_2 import (
    run_wave52r_offline_leader_cross_surface_promotion as promotion,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage5_complex_harmonic_coefficient_residuals as stage5,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage7_mean_centered_shape_multi_head as stage7,
)
from scripts.campaigns.wave_5_2 import (
    run_wave52r_stage9_temporal_analytical_residual_models as stage9,
)
from scripts.models.integrated_specialist_residual_network import (
    IntegratedSpecialistResidualNetwork,
)


# Define The Approval-Gated Campaign Contract
CAMPAIGN_NAME = "wave52r_integrated_specialist_model_2026_08_02"
CAMPAIGN_CONFIGURATION_PATH = (
    PROJECT_ROOT
    / "config"
    / "training"
    / "wave52r_integrated_specialist_model"
    / "campaigns"
    / "2026-08-02_wave52r_integrated_specialist_model"
    / "campaign.yaml"
)
ACTIVE_CAMPAIGN_PATH = PROJECT_ROOT / "doc/running/active_training_campaign.yaml"
PREFLIGHT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output/validation_checks/wave52r_integrated_specialist_model"
    / "campaign_preflight_summary.yaml"
)
CAMPAIGN_OUTPUT_ROOT = PROJECT_ROOT / "output/training_campaigns"
RUN_OUTPUT_ROOT = PROJECT_ROOT / "output/training_runs/integrated_specialist_models"
SURFACE_LIST = ["Fw", "Bw", "global"]
TRAINABLE_ABLATION_LIST = ["A02", "A03", "A04", "A05", "A06", "A07"]
REPLAY_ABLATION_LIST = ["A00", "A00D", "A01"]


def now_timestamp() -> str:
    """Return one sortable local timestamp."""

    return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


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


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write one stable CSV table."""

    assert row_list
    field_name_list: list[str] = []
    for row in row_list:
        for field_name in row:
            if field_name not in field_name_list:
                field_name_list.append(field_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def file_sha256(input_path: Path) -> str:
    """Return one lowercase SHA-256 file digest."""

    digest = hashlib.sha256()
    with input_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            digest.update(byte_chunk)
    return digest.hexdigest()


def relative_path(input_path: Path) -> str:
    """Return one repository-relative POSIX path."""

    return input_path.relative_to(PROJECT_ROOT).as_posix()


def require_campaign_approval(configuration: dict[str, Any]) -> None:
    """Refuse training until the campaign plan has explicit approval."""

    approval = configuration.get("approval", {})
    assert approval.get("technical_document_status") == "approved"
    if approval.get("campaign_plan_status") != "approved":
        raise RuntimeError(
            "Training is blocked: campaign_plan_status is not approved. "
            "Run preflight only, record explicit approval, then launch again."
        )


def load_all_dataset_dictionary() -> dict[str, stage5.Stage5Dataset]:
    """Load the immutable grouped split for all three surfaces."""

    phase1_configuration = stage5.load_yaml(stage5.PHASE1_CONFIGURATION_PATH)
    split_manifest = stage5.load_yaml(stage5.COMMON_SPLIT_MANIFEST_PATH)
    record_list = stage5.load_curve_records(
        phase1_configuration,
        split_manifest,
    )
    return {
        surface: promotion.build_surface_dataset(record_list, surface)[0]
        for surface in SURFACE_LIST
    }


def build_angle_matrix(curve_count: int) -> np.ndarray:
    """Return the fixed full-revolution angle matrix."""

    angle_array = np.linspace(
        0.0,
        360.0,
        stage5.ANGULAR_SAMPLE_COUNT,
        endpoint=False,
        dtype=np.float32,
    )
    return np.repeat(angle_array[None, :], curve_count, axis=0)


def predict_k01(
    dataset: stage5.Stage5Dataset,
    h04_checkpoint_path: Path,
    k01_checkpoint_path: Path,
    selected_index_array: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Replay one frozen K01 and return its H04 analytical anchor."""

    anchor_bundle = promotion.build_h04_anchor_bundle(
        dataset,
        h04_checkpoint_path,
    )
    specification = next(
        item for item in stage9.build_candidate_list() if item.candidate_id == "K01"
    )
    model = stage9.build_model(specification, dataset)
    checkpoint = torch.load(
        k01_checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    model.load_state_dict(checkpoint["state_dict"], strict=True)
    model.eval()
    if selected_index_array is None:
        selected_index_array = np.arange(dataset.curve_matrix.shape[0])
    prediction_list: list[np.ndarray] = []
    angle_matrix = build_angle_matrix(dataset.curve_matrix.shape[0])
    with torch.inference_mode():
        for start_index in range(0, len(selected_index_array), 16):
            batch_index = selected_index_array[start_index : start_index + 16]
            output = model.forward_in_chunks(
                torch.as_tensor(angle_matrix[batch_index]),
                torch.as_tensor(
                    dataset.condition_matrix[batch_index],
                    dtype=torch.float32,
                ),
                torch.as_tensor(
                    anchor_bundle.h04_curve_matrix[batch_index],
                    dtype=torch.float32,
                ),
                torch.as_tensor(
                    anchor_bundle.h04_coefficient_matrix[batch_index],
                    dtype=torch.float32,
                ),
                chunk_length=stage9.DEFAULT_CHUNK_LENGTH,
            )
            prediction_list.append(output["prediction_curve"].cpu().numpy())
    return (
        np.vstack(prediction_list),
        anchor_bundle.h04_curve_matrix[selected_index_array],
    )


def predict_h08(
    dataset: stage5.Stage5Dataset,
    checkpoint_path: Path,
    selected_index_array: np.ndarray | None = None,
) -> np.ndarray:
    """Replay the frozen forward H08 checkpoint without its mean transfer."""

    specification = next(
        item for item in stage5.build_candidate_list() if item.candidate_id == "H08"
    )
    model = stage5.build_model(specification, dataset)
    checkpoint = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=False,
    )
    model.load_state_dict(checkpoint["state_dict"], strict=True)
    model.eval()
    normalized_condition = (
        dataset.condition_matrix - dataset.feature_mean
    ) / dataset.feature_scale
    if selected_index_array is None:
        selected_index_array = np.arange(dataset.curve_matrix.shape[0])
    with torch.inference_mode():
        output = model(
            torch.as_tensor(
                normalized_condition[selected_index_array],
                dtype=torch.float32,
            ),
            torch.as_tensor(
                dataset.anchor_coefficient_map[
                    specification.order_set_name
                ][selected_index_array],
                dtype=torch.float32,
            ),
        )
    return output["prediction_curve"].cpu().numpy()


def route_directional_matrix(
    global_dataset: stage5.Stage5Dataset,
    fw_dataset: stage5.Stage5Dataset,
    bw_dataset: stage5.Stage5Dataset,
    fw_matrix: np.ndarray,
    bw_matrix: np.ndarray,
) -> np.ndarray:
    """Align independently replayed directional matrices to global records."""

    value_by_id = {
        **{
            f"{condition_id}__Fw": fw_matrix[index]
            for index, condition_id in enumerate(fw_dataset.condition_id_list)
        },
        **{
            f"{condition_id}__Bw": bw_matrix[index]
            for index, condition_id in enumerate(bw_dataset.condition_id_list)
        },
    }
    return np.vstack(
        [value_by_id[condition_id] for condition_id in global_dataset.condition_id_list]
    )


def prepare_frozen_input_bundle(
    configuration: dict[str, Any],
) -> dict[str, np.ndarray | stage5.Stage5Dataset]:
    """Replay and align all frozen experts used by the ablation matrix."""

    dataset_dictionary = load_all_dataset_dictionary()
    checkpoint = configuration["frozen_checkpoint_contract"]
    global_k01, global_h04 = predict_k01(
        dataset_dictionary["global"],
        PROJECT_ROOT / checkpoint["global_h04"],
        PROJECT_ROOT / checkpoint["global_k01"],
    )
    fw_k01, fw_h04 = predict_k01(
        dataset_dictionary["Fw"],
        PROJECT_ROOT / checkpoint["fw_h04"],
        PROJECT_ROOT / checkpoint["fw_k01"],
    )
    bw_k01, bw_h04 = predict_k01(
        dataset_dictionary["Bw"],
        PROJECT_ROOT / checkpoint["bw_h04"],
        PROJECT_ROOT / checkpoint["bw_k01"],
    )
    fw_h08 = predict_h08(
        dataset_dictionary["Fw"],
        PROJECT_ROOT / checkpoint["fw_h08"],
    )
    zero_bw_h08 = np.zeros_like(dataset_dictionary["Bw"].curve_matrix)
    return {
        "dataset": dataset_dictionary["global"],
        "global_k01": global_k01,
        "directional_k01": route_directional_matrix(
            dataset_dictionary["global"],
            dataset_dictionary["Fw"],
            dataset_dictionary["Bw"],
            fw_k01,
            bw_k01,
        ),
        "global_h04": global_h04,
        "directional_h04": route_directional_matrix(
            dataset_dictionary["global"],
            dataset_dictionary["Fw"],
            dataset_dictionary["Bw"],
            fw_h04,
            bw_h04,
        ),
        "fw_h08": route_directional_matrix(
            dataset_dictionary["global"],
            dataset_dictionary["Fw"],
            dataset_dictionary["Bw"],
            fw_h08,
            zero_bw_h08,
        ),
    }


def ablation_flags(ablation_id: str) -> dict[str, bool]:
    """Resolve one single-component architecture profile."""

    return {
        "enable_h08_branch": ablation_id == "A02",
        "enable_h04_branch": ablation_id == "A03",
        "enable_shape_branch": ablation_id in {"A04", "A05"},
        "enable_condition_branch": ablation_id in {"A06", "A07"},
        "use_thresholded_condition_library": ablation_id == "A07",
    }


def build_model(
    dataset: stage5.Stage5Dataset,
    ablation_id: str,
    passed_branch_list: list[str] | None = None,
) -> IntegratedSpecialistResidualNetwork:
    """Build one ablation or the conditional integrated model."""

    flags = ablation_flags(ablation_id)
    if ablation_id == "A08":
        passed_branch_set = set(passed_branch_list or [])
        flags = {
            "enable_h08_branch": "A02" in passed_branch_set,
            "enable_h04_branch": "A03" in passed_branch_set,
            "enable_shape_branch": bool({"A04", "A05"} & passed_branch_set),
            "enable_condition_branch": bool({"A06", "A07"} & passed_branch_set),
            "use_thresholded_condition_library": (
                "A07" in passed_branch_set and "A06" not in passed_branch_set
            ),
        }
    return IntegratedSpecialistResidualNetwork(
        condition_feature_mean=torch.as_tensor(dataset.feature_mean),
        condition_feature_scale=torch.as_tensor(dataset.feature_scale),
        harmonic_order_list=list(stage5.CORE_ORDER_LIST),
        branch_bound_deg=0.02,
        **flags,
    )


def select_array(
    value: np.ndarray,
    mask: np.ndarray,
    device: torch.device,
) -> torch.Tensor:
    """Move one masked floating array to the training device."""

    return torch.as_tensor(value[mask], dtype=torch.float32, device=device)


def forward_model(
    model: IntegratedSpecialistResidualNetwork,
    bundle: dict[str, Any],
    mask: np.ndarray,
    baseline_key: str,
    device: torch.device,
) -> dict[str, torch.Tensor]:
    """Evaluate one complete split through inspectable branch outputs."""

    dataset = bundle["dataset"]
    condition = select_array(dataset.condition_matrix, mask, device)
    direction = condition[:, 3:4]
    return model.forward_components(
        condition,
        select_array(build_angle_matrix(len(dataset.condition_id_list)), mask, device),
        select_array(bundle[baseline_key], mask, device),
        select_array(bundle["fw_h08"], mask, device),
        select_array(bundle["directional_h04"], mask, device),
        direction,
    )


def optimization_loss(
    ablation_id: str,
    output: dict[str, torch.Tensor],
    target: torch.Tensor,
) -> torch.Tensor:
    """Apply the predeclared branch-specific training objective."""

    prediction = output["prediction_curve"]
    raw_loss = torch.mean(torch.abs(prediction - target))
    prediction_centered = prediction - torch.mean(prediction, dim=1, keepdim=True)
    target_centered = target - torch.mean(target, dim=1, keepdim=True)
    shape_loss = torch.mean(torch.abs(prediction_centered - target_centered))
    closure_loss = torch.mean(torch.abs(prediction[:, 0] - prediction[:, -1]))
    spectrum_difference = torch.fft.rfft(prediction_centered, dim=1) - torch.fft.rfft(
        target_centered,
        dim=1,
    )
    harmonic_loss = torch.mean(torch.abs(spectrum_difference[:, 1:241])) / (
        prediction.shape[1]
    )
    residual_rms = torch.sqrt(
        torch.mean((prediction - output["k01_baseline_curve"]).square()) + 1.0e-12
    )
    if ablation_id == "A04":
        return raw_loss + 0.75 * shape_loss + 1.0e-4 * residual_rms
    if ablation_id == "A05":
        return (
            raw_loss
            + 0.35 * shape_loss
            + 0.20 * harmonic_loss
            + 0.10 * closure_loss
            + 1.0e-4 * residual_rms
        )
    return raw_loss + 0.25 * shape_loss + 1.0e-4 * residual_rms


def train_ablation(
    ablation_id: str,
    random_seed: int,
    bundle: dict[str, Any],
    configuration: dict[str, Any],
    campaign_output_directory: Path,
    passed_branch_list: list[str] | None = None,
) -> tuple[dict[str, Any], IntegratedSpecialistResidualNetwork]:
    """Train one seed with validation-only checkpoint selection."""

    stage9.seed_everything(random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataset = bundle["dataset"]
    model = build_model(dataset, ablation_id, passed_branch_list).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(configuration["training_contract"]["learning_rate"]),
        weight_decay=float(configuration["training_contract"]["weight_decay"]),
    )
    train_mask = dataset.split_array == "train"
    validation_mask = dataset.split_array == "validation"
    target_validation = select_array(dataset.curve_matrix, validation_mask, device)
    maximum_epoch_count = int(configuration["training_contract"]["maximum_epochs"])
    curve_batch_size = int(configuration["training_contract"]["curve_batch_size"])
    training_index_array = np.flatnonzero(train_mask)
    random_generator = np.random.default_rng(random_seed)
    best_validation_loss = float("inf")
    best_epoch = 0
    best_state: dict[str, torch.Tensor] | None = None
    history_row_list: list[dict[str, Any]] = []

    for epoch_index in range(maximum_epoch_count):
        model.train()
        shuffled_training_index = random_generator.permutation(training_index_array)
        training_loss_list = []
        for batch_start in range(0, len(shuffled_training_index), curve_batch_size):
            batch_index = shuffled_training_index[
                batch_start : batch_start + curve_batch_size
            ]
            batch_mask = np.zeros(len(dataset.condition_id_list), dtype=bool)
            batch_mask[batch_index] = True
            optimizer.zero_grad(set_to_none=True)
            train_output = forward_model(
                model,
                bundle,
                batch_mask,
                "global_k01",
                device,
            )
            target_train = select_array(dataset.curve_matrix, batch_mask, device)
            train_loss = optimization_loss(ablation_id, train_output, target_train)
            train_loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            training_loss_list.append(float(train_loss.detach().cpu()))
        model.eval()
        with torch.inference_mode():
            validation_output = forward_model(
                model,
                bundle,
                validation_mask,
                "global_k01",
                device,
            )
            validation_loss = optimization_loss(
                ablation_id,
                validation_output,
                target_validation,
            )
        history_row_list.append(
            {
                "epoch": epoch_index + 1,
                "training_loss": float(np.mean(training_loss_list)),
                "validation_loss": float(validation_loss.detach().cpu()),
            }
        )
        if float(validation_loss) < best_validation_loss:
            best_validation_loss = float(validation_loss)
            best_epoch = epoch_index + 1
            best_state = {
                name: value.detach().cpu().clone()
                for name, value in model.state_dict().items()
            }
    assert best_state is not None
    model.load_state_dict(best_state)
    run_instance_id = (
        f"{now_timestamp()}__{ablation_id.lower()}__seed_{random_seed}"
    )
    run_directory = RUN_OUTPUT_ROOT / run_instance_id
    run_directory.mkdir(parents=True, exist_ok=False)
    checkpoint_path = run_directory / "best_model.pt"
    torch.save(
        {
            "state_dict": best_state,
            "ablation_id": ablation_id,
            "random_seed": random_seed,
            "split_signature": stage5.SPLIT_SIGNATURE,
            "passed_branch_list": passed_branch_list or [],
        },
        checkpoint_path,
    )
    write_csv(run_directory / "training_history.csv", history_row_list)
    result = {
        "ablation_id": ablation_id,
        "random_seed": random_seed,
        "run_instance_id": run_instance_id,
        "status": "completed",
        "best_epoch": best_epoch,
        "best_validation_loss": best_validation_loss,
        "checkpoint_path": relative_path(checkpoint_path),
        "parameter_count": sum(parameter.numel() for parameter in model.parameters()),
        "runtime_target_derived_input_count": 0,
        "passed_branch_list": ",".join(passed_branch_list or []),
        "campaign_output_directory": relative_path(campaign_output_directory),
    }
    return result, model


def split_metrics(
    measured: np.ndarray,
    predicted: np.ndarray,
) -> dict[str, float]:
    """Return the repository multi-index curve metric payload."""

    return stage7.evaluate_metrics(measured, predicted)


def evaluate_model_split(
    model: IntegratedSpecialistResidualNetwork,
    bundle: dict[str, Any],
    split_name: str,
    surface_name: str = "global",
) -> tuple[dict[str, float], np.ndarray, dict[str, np.ndarray]]:
    """Evaluate one frozen integrated model on one declared split."""

    dataset = bundle["dataset"]
    mask = dataset.split_array == split_name
    if surface_name != "global":
        surface_mask = np.asarray(
            [
                condition_id.endswith(f"__{surface_name}")
                for condition_id in dataset.condition_id_list
            ]
        )
        mask = mask & surface_mask
    device = next(model.parameters()).device
    model.eval()
    with torch.inference_mode():
        output = forward_model(model, bundle, mask, "global_k01", device)
    prediction = output["prediction_curve"].cpu().numpy()
    component_dictionary = {
        name: value.cpu().numpy() for name, value in output.items()
    }
    return (
        split_metrics(dataset.curve_matrix[mask], prediction),
        prediction,
        component_dictionary,
    )


def branch_gate(
    ablation_id: str,
    candidate_metrics_by_surface: dict[str, dict[str, float]],
    baseline_metrics_by_surface: dict[str, dict[str, float]],
    tolerance: dict[str, float],
) -> dict[str, Any]:
    """Apply the frozen validation-only incremental branch gate."""

    specialty_metric_map = {
        "A02": "retained_phase_mae_rad",
        "A03": "centered_shape_mae_deg",
        "A04": "centered_shape_mae_deg",
        "A05": "periodic_closure_error_deg",
        "A06": "mae_deg",
        "A07": "mae_deg",
    }
    specialty_metric = specialty_metric_map[ablation_id]
    specialty_surface = "Fw" if ablation_id == "A02" else "global"
    specialty_passed = candidate_metrics_by_surface[specialty_surface][
        specialty_metric
    ] <= (
        (1.0 - float(tolerance["specialty_improvement_fraction"]))
        * baseline_metrics_by_surface[specialty_surface][specialty_metric]
    )
    preserved_metric_list = [
        "mae_deg",
        "offset_abs_error_deg",
        "centered_shape_mae_deg",
        "peak_to_peak_abs_error_deg",
        "per_curve_mae_p95",
    ]
    non_regression_limit = 1.0 + float(tolerance["non_regression_fraction"])
    preserved = all(
        candidate_metrics_by_surface[surface_name][metric_name]
        <= non_regression_limit
        * baseline_metrics_by_surface[surface_name][metric_name]
        for surface_name in SURFACE_LIST
        for metric_name in preserved_metric_list
    )
    return {
        "ablation_id": ablation_id,
        "specialty_surface": specialty_surface,
        "specialty_metric": specialty_metric,
        "specialty_improved": bool(specialty_passed),
        "multi_index_non_regression_passed": bool(preserved),
        "passed": bool(specialty_passed and preserved),
    }


def replay_metrics(
    bundle: dict[str, Any],
    prediction_key: str,
    split_name: str,
    surface_name: str = "global",
) -> tuple[dict[str, float], np.ndarray]:
    """Evaluate one frozen replay matrix without training."""

    dataset = bundle["dataset"]
    mask = dataset.split_array == split_name
    if surface_name != "global":
        mask = mask & np.asarray(
            [
                condition_id.endswith(f"__{surface_name}")
                for condition_id in dataset.condition_id_list
            ]
        )
    prediction = bundle[prediction_key][mask]
    return split_metrics(dataset.curve_matrix[mask], prediction), prediction


def run_preflight() -> dict[str, Any]:
    """Validate configuration, checkpoints, routing, and model identities."""

    assert CAMPAIGN_CONFIGURATION_PATH.exists()
    configuration = read_yaml(CAMPAIGN_CONFIGURATION_PATH)
    assert configuration["campaign_name"] == CAMPAIGN_NAME
    assert configuration["dataset_id"] == "polished_dataset"
    assert configuration["input_mode"] == "setpoints"
    assert configuration["surface_list"] == SURFACE_LIST
    assert configuration["ablation_order"] == [
        *REPLAY_ABLATION_LIST,
        *TRAINABLE_ABLATION_LIST,
        "A08",
    ]
    assert configuration["baseline_topology_contract"][
        "selected_specialist_attachment_topology"
    ] == "global_k01"
    active_state = read_yaml(ACTIVE_CAMPAIGN_PATH)
    assert active_state["campaign_name"] == CAMPAIGN_NAME
    assert active_state["status"] in {
        "prepared_pending_campaign_plan_approval",
        "prepared_approved",
    }
    persistent_approval = configuration["persistent_state_contract"]["approval"]
    for approval_key in (
        "technical_document_status",
        "campaign_plan_status",
        "approval_source",
    ):
        assert active_state["approval"][approval_key] == persistent_approval[
            approval_key
        ]
    protected_path_list = active_state["protected_file_list"]
    assert protected_path_list
    for protected_path_text in protected_path_list:
        protected_path = PROJECT_ROOT / protected_path_text
        if protected_path.resolve() == PREFLIGHT_OUTPUT_PATH.resolve():
            continue
        assert protected_path.exists(), protected_path_text
    for required_path_key in (
        "campaign_manifest_path",
        "launcher_path",
        "launcher_note_path",
        "planning_report_path",
        "technical_document_path",
    ):
        required_path = PROJECT_ROOT / active_state[required_path_key]
        assert required_path.exists(), required_path
    queue_directory = CAMPAIGN_CONFIGURATION_PATH.parent / "queue"
    queue_path_list = sorted(queue_directory.glob("*.yaml"))
    assert len(queue_path_list) == 10
    queue_payload_list = [read_yaml(queue_path) for queue_path in queue_path_list]
    assert [payload["queue_index"] for payload in queue_payload_list] == list(
        range(1, 11)
    )
    assert [payload["ablation_id"] for payload in queue_payload_list] == (
        configuration["ablation_order"]
    )
    checkpoint_digest_dictionary = {}
    for checkpoint_name, checkpoint_path_text in configuration[
        "frozen_checkpoint_contract"
    ].items():
        checkpoint_path = PROJECT_ROOT / checkpoint_path_text
        assert checkpoint_path.exists(), checkpoint_path
        checkpoint_digest_dictionary[checkpoint_name] = file_sha256(checkpoint_path)
    dataset_dictionary = load_all_dataset_dictionary()
    dataset = dataset_dictionary["global"]
    checkpoint = configuration["frozen_checkpoint_contract"]
    fw_global_index = next(
        index
        for index, condition_id in enumerate(dataset.condition_id_list)
        if condition_id.endswith("__Fw")
    )
    bw_global_index = next(
        index
        for index, condition_id in enumerate(dataset.condition_id_list)
        if condition_id.endswith("__Bw")
    )
    selected_global_index = np.asarray([fw_global_index, bw_global_index])
    global_k01, global_h04 = predict_k01(
        dataset,
        PROJECT_ROOT / checkpoint["global_h04"],
        PROJECT_ROOT / checkpoint["global_k01"],
        selected_global_index,
    )
    fw_h08 = predict_h08(
        dataset_dictionary["Fw"],
        PROJECT_ROOT / checkpoint["fw_h08"],
        np.asarray([0]),
    )
    h08_input = np.vstack([fw_h08[0], np.zeros_like(fw_h08[0])])
    model = build_model(dataset, "A01")
    with torch.inference_mode():
        output = model.forward_components(
            torch.as_tensor(
                dataset.condition_matrix[selected_global_index],
                dtype=torch.float32,
            ),
            torch.as_tensor(build_angle_matrix(2), dtype=torch.float32),
            torch.as_tensor(global_k01, dtype=torch.float32),
            torch.as_tensor(h08_input, dtype=torch.float32),
            torch.as_tensor(global_h04, dtype=torch.float32),
            torch.as_tensor(
                dataset.condition_matrix[selected_global_index, 3:4],
                dtype=torch.float32,
            ),
        )
    replay_difference = float(
        torch.max(
            torch.abs(
                output["prediction_curve"] - output["k01_baseline_curve"]
            )
        )
    )
    h08_model = build_model(dataset, "A02")
    with torch.no_grad():
        h08_model.h08_gate_head[-1].bias.fill_(1.0)
    with torch.inference_mode():
        backward_output = h08_model.forward_components(
            torch.as_tensor(
                dataset.condition_matrix[selected_global_index],
                dtype=torch.float32,
            ),
            torch.as_tensor(build_angle_matrix(2), dtype=torch.float32),
            torch.as_tensor(global_k01, dtype=torch.float32),
            torch.as_tensor(h08_input, dtype=torch.float32),
            torch.as_tensor(global_h04, dtype=torch.float32),
            torch.as_tensor(
                dataset.condition_matrix[selected_global_index, 3:4],
                dtype=torch.float32,
            ),
        )
    backward_h08_abs_max = float(
        torch.max(torch.abs(backward_output["h08_centered_residual"][1]))
    )
    forward_h08_abs_max = float(
        torch.max(torch.abs(backward_output["h08_centered_residual"][0]))
    )
    assert replay_difference == 0.0
    assert backward_h08_abs_max == 0.0
    assert forward_h08_abs_max > 0.0
    payload = {
        "schema_version": 1,
        "generated_at": now_iso(),
        "status": "passed",
        "campaign_name": CAMPAIGN_NAME,
        "campaign_plan_status": configuration["approval"]["campaign_plan_status"],
        "training_execution_started": False,
        "split_signature": stage5.SPLIT_SIGNATURE,
        "surface_list": SURFACE_LIST,
        "random_seed_list": configuration["random_seed_list"],
        "maximum_run_count": configuration["maximum_run_count"],
        "queue_entry_count": len(queue_path_list),
        "protected_file_count": len(protected_path_list),
        "k01_decomposition_replay_max_abs_deg": replay_difference,
        "backward_h08_residual_abs_max_deg": backward_h08_abs_max,
        "forward_h08_residual_abs_max_deg": forward_h08_abs_max,
        "checkpoint_sha256": checkpoint_digest_dictionary,
        "runtime_target_derived_input_count": 0,
        "training_authorized": (
            configuration["approval"]["campaign_plan_status"] == "approved"
        ),
    }
    write_yaml(PREFLIGHT_OUTPUT_PATH, payload)
    print(
        "[PASS] Integrated-specialist package preflight | "
        f"approval={payload['campaign_plan_status']} | training_started=false",
        flush=True,
    )
    return payload


def campaign_state(
    configuration: dict[str, Any],
    status: str,
    output_directory: Path | None = None,
) -> dict[str, Any]:
    """Build the persistent campaign state payload."""

    payload = dict(configuration["persistent_state_contract"])
    payload["status"] = status
    if ACTIVE_CAMPAIGN_PATH.exists():
        current_state = read_yaml(ACTIVE_CAMPAIGN_PATH)
        payload["protected_file_list"] = current_state.get(
            "protected_file_list",
            [],
        )
    if output_directory is not None:
        payload["campaign_output_directory"] = relative_path(output_directory)
    return payload


def run_campaign() -> Path:
    """Execute replay controls, single branches, and conditional A08."""

    preflight = run_preflight()
    configuration = read_yaml(CAMPAIGN_CONFIGURATION_PATH)
    require_campaign_approval(configuration)
    assert preflight["status"] == "passed"
    bundle = prepare_frozen_input_bundle(configuration)
    dataset = bundle["dataset"]
    output_directory = CAMPAIGN_OUTPUT_ROOT / f"{now_timestamp()}_{CAMPAIGN_NAME}"
    output_directory.mkdir(parents=True, exist_ok=False)
    running_state = {
        **campaign_state(configuration, "running", output_directory),
        "started_at": now_iso(),
    }
    write_yaml(ACTIVE_CAMPAIGN_PATH, running_state)

    # Evaluate Baseline Topologies On Validation Before Specialist Training
    baseline_validation_metrics_by_surface = {
        surface_name: replay_metrics(
            bundle,
            "global_k01",
            "validation",
            surface_name,
        )[0]
        for surface_name in SURFACE_LIST
    }
    global_validation_metrics = baseline_validation_metrics_by_surface["global"]
    directional_validation_metrics, _ = replay_metrics(
        bundle,
        "directional_k01",
        "validation",
    )
    topology_contract = configuration["baseline_topology_contract"]
    selected_topology = topology_contract[
        "selected_specialist_attachment_topology"
    ]
    assert selected_topology == "global_k01"
    write_yaml(
        output_directory / "baseline_topology_comparison.yaml",
        {
            "validation_only": True,
            "predeclared_specialist_attachment_topology": selected_topology,
            "comparison_control_topology": topology_contract[
                "comparison_control_topology"
            ],
            "selection_basis": topology_contract["selection_basis"],
            "global_k01_metrics": global_validation_metrics,
            "directional_k01_metrics": directional_validation_metrics,
            "deployment_topology_decision_authorized": False,
        },
    )

    result_row_list: list[dict[str, Any]] = []
    model_by_run: dict[str, IntegratedSpecialistResidualNetwork] = {}
    gate_row_list: list[dict[str, Any]] = []
    for ablation_id in TRAINABLE_ABLATION_LIST:
        for random_seed in configuration["random_seed_list"]:
            result, model = train_ablation(
                ablation_id,
                int(random_seed),
                bundle,
                configuration,
                output_directory,
            )
            validation_metrics_by_surface = {
                surface_name: evaluate_model_split(
                    model,
                    bundle,
                    "validation",
                    surface_name,
                )[0]
                for surface_name in SURFACE_LIST
            }
            for surface_name, metric_payload in validation_metrics_by_surface.items():
                result.update(
                    {
                        f"validation_{surface_name}_{key}": value
                        for key, value in metric_payload.items()
                    }
                )
            gate = branch_gate(
                ablation_id,
                validation_metrics_by_surface,
                baseline_validation_metrics_by_surface,
                configuration["acceptance_gate"],
            )
            result.update({f"gate_{key}": value for key, value in gate.items()})
            result_row_list.append(result)
            model_by_run[result["run_instance_id"]] = model
            gate_row_list.append({**gate, "random_seed": random_seed})

    # Require Two Of Three Seeds Before A Branch May Enter A08
    passed_branch_list = []
    for ablation_id in TRAINABLE_ABLATION_LIST:
        passed_seed_count = sum(
            int(row["passed"])
            for row in gate_row_list
            if row["ablation_id"] == ablation_id
        )
        if passed_seed_count >= 2:
            passed_branch_list.append(ablation_id)
    if passed_branch_list:
        for random_seed in configuration["random_seed_list"]:
            result, model = train_ablation(
                "A08",
                int(random_seed),
                bundle,
                configuration,
                output_directory,
                passed_branch_list,
            )
            for surface_name in SURFACE_LIST:
                validation_metrics, _, _ = evaluate_model_split(
                    model,
                    bundle,
                    "validation",
                    surface_name,
                )
                result.update(
                    {
                        f"validation_{surface_name}_{key}": value
                        for key, value in validation_metrics.items()
                    }
                )
            result_row_list.append(result)
            model_by_run[result["run_instance_id"]] = model

    # Freeze Selection, Then Perform Exactly One Final Test Evaluation
    for result in result_row_list:
        model = model_by_run[result["run_instance_id"]]
        test_metrics, prediction, component = evaluate_model_split(
            model,
            bundle,
            "test",
            "global",
        )
        result.update(
            {f"test_global_{key}": value for key, value in test_metrics.items()}
        )
        for surface_name in ("Fw", "Bw"):
            surface_metrics, _, _ = evaluate_model_split(
                model,
                bundle,
                "test",
                surface_name,
            )
            result.update(
                {
                    f"test_{surface_name}_{key}": value
                    for key, value in surface_metrics.items()
                }
            )
        run_directory = PROJECT_ROOT / result["checkpoint_path"]
        run_directory = run_directory.parent
        test_mask = dataset.split_array == "test"
        np.savez_compressed(
            run_directory / "test_predictions.npz",
            measured_curve=dataset.curve_matrix[test_mask],
            predicted_curve=prediction,
            **component,
        )
        write_yaml(run_directory / "metrics_summary.yaml", result)

    replay_result_list = []
    for ablation_id, prediction_key in (
        ("A00", "global_k01"),
        ("A00D", "directional_k01"),
        ("A01", "global_k01"),
    ):
        test_metrics_by_surface = {
            surface_name: replay_metrics(
                bundle,
                prediction_key,
                "test",
                surface_name,
            )[0]
            for surface_name in SURFACE_LIST
        }
        flattened_test_metrics = {
            f"test_{surface_name}_{key}": value
            for surface_name, metric_payload in test_metrics_by_surface.items()
            for key, value in metric_payload.items()
        }
        replay_result_list.append(
            {
                "ablation_id": ablation_id,
                "random_seed": 271828,
                "run_instance_id": f"frozen_{prediction_key}",
                "status": "completed_replay",
                **flattened_test_metrics,
            }
        )
    result_row_list = replay_result_list + result_row_list
    for queue_index, result in enumerate(result_row_list, start=1):
        write_yaml(
            output_directory
            / "queue_state"
            / f"{queue_index:03d}_{result['ablation_id'].lower()}_"
            f"seed_{result['random_seed']}.yaml",
            {
                "status": result["status"],
                "ablation_id": result["ablation_id"],
                "random_seed": result["random_seed"],
                "run_instance_id": result["run_instance_id"],
            },
        )
    if not passed_branch_list:
        write_yaml(
            output_directory / "queue_state" / "a08_conditional_skip.yaml",
            {
                "status": "skipped_no_branch_passed_two_of_three_seeds",
                "ablation_id": "A08",
            },
        )
    write_csv(output_directory / "campaign_results.csv", result_row_list)
    write_yaml(
        output_directory / "branch_gate_summary.yaml",
        {
            "validation_only": True,
            "gate_row_list": gate_row_list,
            "passed_branch_list": passed_branch_list,
            "a08_executed": bool(passed_branch_list),
        },
    )
    ordered_result_list = sorted(
        result_row_list,
        key=lambda row: (
            float(row.get("validation_global_mae_deg", float("inf"))),
            row["ablation_id"],
            int(row["random_seed"]),
        ),
    )
    provisional_best = ordered_result_list[0]
    write_yaml(
        output_directory / "campaign_leaderboard.yaml",
        {
            "selection_scope": "validation-only scalar ordering",
            "promotion_authorized": False,
            "result_list": ordered_result_list,
        },
    )
    write_yaml(
        output_directory / "campaign_best_run.yaml",
        {
            "status": "provisional_validation_winner",
            "best_run": provisional_best,
            "promotion_authorized": False,
            "official_curve_verification_status": "pending_separate_operator_step",
        },
    )
    with (output_directory / "campaign_best_run.md").open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        output_file.write(
            "# Campaign Best Run\n\n"
            f"- Provisional ablation: `{provisional_best['ablation_id']}`\n"
            f"- Run instance: `{provisional_best['run_instance_id']}`\n\n"
            "This validation-only result does not authorize model promotion.\n"
        )
    artifact_path_list = sorted(
        {relative_path(PROJECT_ROOT / row["checkpoint_path"] .rsplit("/", 1)[0])
         for row in result_row_list if "checkpoint_path" in row}
    )
    with (output_directory / "campaign_artifact_path_list.txt").open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:
        output_file.write("\n".join(artifact_path_list) + "\n")
    completed_state = {
        **running_state,
        "status": "completed",
        "completed_at": now_iso(),
        "completed_run_count": len(result_row_list),
        "campaign_best_run_path": relative_path(
            output_directory / "campaign_best_run.yaml"
        ),
        "official_curve_verification_status": "pending_separate_operator_step",
    }
    write_yaml(output_directory / "campaign_state.yaml", completed_state)
    write_yaml(ACTIVE_CAMPAIGN_PATH, completed_state)
    print(
        "[DONE] Integrated-specialist campaign completed | "
        f"runs={len(result_row_list)} | a08={bool(passed_branch_list)}",
        flush=True,
    )
    return output_directory


def parse_arguments() -> argparse.Namespace:
    """Parse campaign runner arguments."""

    parser = argparse.ArgumentParser(
        description="Preflight or run the Wave 5.2R integrated-specialist campaign."
    )
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Run package preflight by default or execute after approval."""

    arguments = parse_arguments()
    if arguments.run:
        run_campaign()
        return
    run_preflight()


if __name__ == "__main__":
    main()
