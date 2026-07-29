"""Build the Wave 5.2R Stage 14 forward tournament audit."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime
import hashlib
from pathlib import Path
from typing import Any

# Import Numerical And Serialization Utilities
import numpy as np
import yaml


# Define Tournament Paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage14_cross_formulation_forward_tournament"
)
STAGE0_METRICS_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage0_forward_evidence_freeze"
    / "frozen_contract"
    / "baseline_metrics.csv"
)
STAGE5_RUN_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
)
STAGE5_METRICS_PATH = STAGE5_RUN_PATH / "metrics_summary.yaml"
STAGE5_STABILITY_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_campaigns"
    / (
        "2026-07-28-16-17-06_"
        "wave52r_stage5_complex_harmonic_coefficient_residuals_2026_07_28"
    )
    / "campaign_stability_summary.yaml"
)
SPLIT_SIGNATURE = (
    "c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16"
)


@dataclass(frozen=True)
class EligibilityRecord:
    """Record all Stage 14 entry requirements for one formulation."""

    formulation_id: str
    stage: str
    formulation_name: str
    isolated_gate_passed: bool
    three_seed_evaluation_completed: bool
    matched_control_beaten: bool
    leakage_and_causality_passed: bool
    complete_full_curve_payload_available: bool
    inference_path_inspectable: bool
    eligible: bool
    exclusion_reason: str
    primary_evidence_path: str


def now_iso() -> str:
    """Return one timezone-aware local timestamp."""

    return datetime.now().astimezone().isoformat(timespec="seconds")


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def load_yaml(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict)
    return payload


def read_csv(path: Path) -> list[dict[str, str]]:
    """Read one CSV table as dictionaries."""

    with path.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def write_csv(path: Path, row_list: list[dict[str, Any]]) -> None:
    """Write one stable CSV table."""

    assert row_list
    path.parent.mkdir(parents=True, exist_ok=True)
    field_name_list: list[str] = []
    for row in row_list:
        for field_name in row:
            if field_name not in field_name_list:
                field_name_list.append(field_name)
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def calculate_sha256(path: Path) -> str:
    """Calculate one file SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        while True:
            block = input_file.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def build_eligibility_record_list() -> list[EligibilityRecord]:
    """Build the complete declarative Stage 14 eligibility matrix."""

    report_root = (
        "doc/reports/campaign_results/model_development_waves/wave_5_2/"
    )
    record_list = [
        EligibilityRecord(
            "S4_PRIMARY",
            "Stage 4",
            "PF-A residual capacity hybrids",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No primary hybrid passed the matched-control and cancellation gates.",
            report_root
            + "2026-07-28-11-26-08_wave52r_stage4_data_only_residual_"
            "capacity_ladder_results_report.md",
        ),
        EligibilityRecord(
            "H04",
            "Stage 5",
            "bounded PF-A core-coefficient correction",
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            "",
            report_root
            + "2026-07-28-16-20-55_wave52r_stage5_complex_harmonic_"
            "coefficient_residuals_results_report.md",
        ),
        EligibilityRecord(
            "H08",
            "Stage 5",
            "broader data-selected harmonic correction",
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            "Raw gain regressed closure and retained amplitude and phase gates.",
            report_root
            + "2026-07-28-16-20-55_wave52r_stage5_complex_harmonic_"
            "coefficient_residuals_results_report.md",
        ),
        EligibilityRecord(
            "S6_PRIMARY",
            "Stage 6",
            "spectral, Sobolev, coordinate, and weak residuals",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No candidate passed derivative, harmonic, tail, and matched-control gates.",
            report_root
            + "2026-07-29-15-35-41_wave52r_stage6_spectral_sobolev_"
            "guidance_results_report.md",
        ),
        EligibilityRecord(
            "S7_PRIMARY",
            "Stage 7",
            "mean and centered-shape multi-head models",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No predictive candidate passed the isolated multi-head gates.",
            report_root
            + "2026-07-29-17-47-24_wave52r_stage7_mean_centered_shape_"
            "multi_head_results_report.md",
        ),
        EligibilityRecord(
            "S8_PRIMARY",
            "Stage 8",
            "weak forward compliance priors",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No weak prior beat data-only while preserving model-local derivatives.",
            report_root
            + "2026-07-29-18-22-31_wave52r_stage8_weak_forward_"
            "compliance_priors_results_report.md",
        ),
        EligibilityRecord(
            "K01",
            "Stage 9",
            "causal coefficient-residual GRU",
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            "Complete closure, P95, and chunk-equivalence gate failed; stability skipped.",
            report_root
            + "2026-07-29-19-52-39_wave52r_stage9_temporal_analytical_"
            "residual_models_results_report.md",
        ),
        EligibilityRecord(
            "S10_PRIMARY",
            "Stage 10",
            "sparse and symbolic condition laws",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No compact law passed shape, complexity, and sign-stability gates.",
            report_root
            + "2026-07-29-20-23-30_wave52r_stage10_sparse_and_symbolic_"
            "formulation_discovery_results_report.md",
        ),
        EligibilityRecord(
            "S11_PRIMARY",
            "Stage 11",
            "uncertainty and physics-trust calibration",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No trust component passed localization, selective-risk, and cost gates.",
            report_root
            + "2026-07-29-21-21-32_wave52r_stage11_uncertainty_and_"
            "physics_trust_calibration_results_report.md",
        ),
        EligibilityRecord(
            "S12_PRIMARY",
            "Stage 12",
            "advanced constraint optimization",
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            "No optimizer beat frozen K01 while preserving the complete gate.",
            report_root
            + "2026-07-29-23-10-48_wave52r_stage12_advanced_constraint_"
            "optimization_results_report.md",
        ),
        EligibilityRecord(
            "W01_ORACLE",
            "Stage 13",
            "weak-form harmonic residual",
            False,
            False,
            False,
            True,
            False,
            True,
            False,
            "Synthetic certification cannot substitute for a real-data isolated gate.",
            report_root
            + "2026-07-29-23-34-07_wave52r_stage13_synthetic_weak_form_"
            "oracle_lane_results_report.md",
        ),
    ]
    assert sum(record.eligible for record in record_list) == 1
    assert next(record for record in record_list if record.eligible).formulation_id == "H04"
    return record_list


def validate_evidence_record_list(
    record_list: list[EligibilityRecord],
) -> list[dict[str, Any]]:
    """Validate every declared evidence file and return its inventory."""

    inventory_row_list: list[dict[str, Any]] = []
    for record in record_list:
        evidence_path = PROJECT_ROOT / record.primary_evidence_path
        assert evidence_path.exists(), evidence_path
        inventory_row_list.append(
            {
                "formulation_id": record.formulation_id,
                "evidence_path": record.primary_evidence_path,
                "byte_size": evidence_path.stat().st_size,
                "sha256": calculate_sha256(evidence_path),
            }
        )
    return inventory_row_list


def build_tournament_payload() -> dict[str, Any]:
    """Build the compatible-unit tournament and bounded nomination."""

    baseline_row_map = {
        row["candidate_id"]: row for row in read_csv(STAGE0_METRICS_PATH)
    }
    h04_payload = load_yaml(STAGE5_METRICS_PATH)
    h04_metric_map = h04_payload["test_metrics"]
    stability_payload = load_yaml(STAGE5_STABILITY_PATH)
    h04_stability_row_list = [
        row
        for row in stability_payload["row_list"]
        if row["candidate_id"] == "H04"
    ]
    h04_seed_mae_list = [
        float(h04_metric_map["mae_deg"])
    ] + [float(row["mae_deg"]) for row in h04_stability_row_list]
    assert len(h04_seed_mae_list) == 3
    assert all(
        value < float(
            baseline_row_map["PF_A_LOCAL_QUADRATIC"]["curve_mae_deg"]
        )
        for value in h04_seed_mae_list
    )
    assert (STAGE5_RUN_PATH / "best_model.pt").exists()
    assert (STAGE5_RUN_PATH / "test_predictions.npz").exists()

    comparison_row_list = [
        {
            "candidate_id": "H04",
            "role": "eligible_entrant",
            "raw_mae_deg": float(h04_metric_map["mae_deg"]),
            "centered_mae_deg": float(h04_metric_map["centered_mae_deg"]),
            "offset_abs_error_deg": float(
                h04_metric_map["offset_abs_error_deg"]
            ),
            "metric_contract": "stage5_full_resolution_degree",
        }
    ]
    for candidate_id in [
        "PF_A_LOCAL_QUADRATIC",
        "accepted_periodic_mlp_harmonic_Fw",
        "accepted_periodic_gru_sequence_Fw",
    ]:
        row = baseline_row_map[candidate_id]
        comparison_row_list.append(
            {
                "candidate_id": candidate_id,
                "role": "frozen_non_entrant_reference",
                "raw_mae_deg": float(row["curve_mae_deg"]),
                "centered_mae_deg": float(row["centered_curve_mae_deg"]),
                "offset_abs_error_deg": float(
                    row["absolute_curve_mean_error_deg"]
                ),
                "metric_contract": row["metric_contract"],
            }
        )

    category_row_list = [
        {
            "category": "best_raw_error",
            "entrant_leader": "H04",
            "reference_leader": "accepted_periodic_gru_sequence_Fw",
            "entrant_beats_reference": False,
            "decision": "incumbent_reference_retained",
        },
        {
            "category": "best_centered_shape",
            "entrant_leader": "H04",
            "reference_leader": "accepted_periodic_gru_sequence_Fw",
            "entrant_beats_reference": True,
            "decision": "H04_has_compatible_shape_advantage",
        },
        {
            "category": "best_offset",
            "entrant_leader": "H04",
            "reference_leader": "accepted_periodic_gru_sequence_Fw",
            "entrant_beats_reference": False,
            "decision": "incumbent_reference_retained",
        },
        {
            "category": "best_harmonic_fidelity",
            "entrant_leader": "H04",
            "reference_leader": "not_ranked",
            "entrant_beats_reference": False,
            "decision": "defer_to_common_stage15_metric_contract",
        },
        {
            "category": "best_robustness",
            "entrant_leader": "H04",
            "reference_leader": "not_seed_matched",
            "entrant_beats_reference": False,
            "decision": "H04_three_seed_gate_passed_cross_model_rank_deferred",
        },
        {
            "category": "best_interpretability",
            "entrant_leader": "H04",
            "reference_leader": "PF_A_LOCAL_QUADRATIC",
            "entrant_beats_reference": False,
            "decision": "H04_inspectable_but_PF_A_remains_white_box_reference",
        },
        {
            "category": "best_twincat_readiness",
            "entrant_leader": "H04",
            "reference_leader": "PF_A_LOCAL_QUADRATIC",
            "entrant_beats_reference": False,
            "decision": "H04_requires_export_and_parity_before_acceptance",
        },
        {
            "category": "recommended_balanced_candidate",
            "entrant_leader": "H04",
            "reference_leader": "accepted_periodic_gru_sequence_Fw",
            "entrant_beats_reference": False,
            "decision": "nominate_H04_for_official_verification_not_acceptance",
        },
    ]
    return {
        "comparison_row_list": comparison_row_list,
        "category_row_list": category_row_list,
        "h04_seed_mae_deg_list": h04_seed_mae_list,
        "h04_seed_mae_mean_deg": float(np.mean(h04_seed_mae_list)),
        "h04_seed_mae_std_deg": float(np.std(h04_seed_mae_list)),
        "h04_checkpoint_path": str(
            (STAGE5_RUN_PATH / "best_model.pt").relative_to(PROJECT_ROOT)
        ).replace("\\", "/"),
        "h04_curve_payload_path": str(
            (STAGE5_RUN_PATH / "test_predictions.npz").relative_to(PROJECT_ROOT)
        ).replace("\\", "/"),
    }


def build_stage14_artifacts() -> None:
    """Build and validate all Stage 14 machine-readable artifacts."""

    eligibility_record_list = build_eligibility_record_list()
    evidence_inventory = validate_evidence_record_list(
        eligibility_record_list
    )
    tournament_payload = build_tournament_payload()
    eligibility_row_list = [
        asdict(record) for record in eligibility_record_list
    ]
    decision_payload = {
        "schema_version": 1,
        "stage": "wave52r_stage14_cross_formulation_forward_tournament",
        "generated_at": now_iso(),
        "status": "completed",
        "dataset_id": "polished_dataset",
        "input_mode": "setpoints",
        "surface": "fw",
        "split_signature": SPLIT_SIGNATURE,
        "audited_formulation_count": len(eligibility_row_list),
        "eligible_entrant_count": 1,
        "eligible_entrant_id_list": ["H04"],
        "tournament_structure": "single_entrant_with_frozen_references",
        "balanced_nominee_id": "H04",
        "nomination_scope": "stage15_official_verification_only",
        "official_acceptance": False,
        "registry_update_authorized": False,
        "incumbent_forward_reference": "accepted_periodic_gru_sequence_Fw",
        "incumbent_status": "retained",
        "harmonic_cross_contract_ranking_permitted": False,
        "stage15_authorized": True,
        "stage15_required_work": [
            "official common-surface forward curve-first verification",
            "harmonic metric normalization",
            "Python and ONNX numerical parity",
            "TwinCAT inference graph and PLC numerical parity",
        ],
        "eligibility_record_list": eligibility_row_list,
        **tournament_payload,
    }
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    write_csv(
        OUTPUT_DIRECTORY / "stage14_entry_eligibility_matrix.csv",
        eligibility_row_list,
    )
    write_csv(
        OUTPUT_DIRECTORY / "stage14_evidence_inventory.csv",
        evidence_inventory,
    )
    write_csv(
        OUTPUT_DIRECTORY / "stage14_compatible_metric_comparison.csv",
        tournament_payload["comparison_row_list"],
    )
    write_csv(
        OUTPUT_DIRECTORY / "stage14_tournament_category_matrix.csv",
        tournament_payload["category_row_list"],
    )
    write_yaml(
        OUTPUT_DIRECTORY / "stage14_tournament_decision.yaml",
        decision_payload,
    )
    validate_stage14_artifacts()
    print(
        "Stage 14 tournament audit completed | "
        f"{OUTPUT_DIRECTORY.relative_to(PROJECT_ROOT)}"
    )


def validate_stage14_artifacts() -> None:
    """Validate the completed Stage 14 artifact contract."""

    decision_path = OUTPUT_DIRECTORY / "stage14_tournament_decision.yaml"
    assert decision_path.exists()
    decision_payload = load_yaml(decision_path)
    assert decision_payload["status"] == "completed"
    assert decision_payload["eligible_entrant_count"] == 1
    assert decision_payload["eligible_entrant_id_list"] == ["H04"]
    assert decision_payload["balanced_nominee_id"] == "H04"
    assert decision_payload["official_acceptance"] is False
    assert decision_payload["registry_update_authorized"] is False
    assert decision_payload["stage15_authorized"] is True
    assert decision_payload["harmonic_cross_contract_ranking_permitted"] is False
    eligibility_row_list = read_csv(
        OUTPUT_DIRECTORY / "stage14_entry_eligibility_matrix.csv"
    )
    assert len(eligibility_row_list) == 11
    assert sum(row["eligible"] == "True" for row in eligibility_row_list) == 1
    assert next(
        row for row in eligibility_row_list if row["eligible"] == "True"
    )["formulation_id"] == "H04"
    category_row_list = read_csv(
        OUTPUT_DIRECTORY / "stage14_tournament_category_matrix.csv"
    )
    assert len(category_row_list) == 8


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Build or validate the Stage 14 tournament artifacts."""

    argument_namespace = parse_arguments()
    if argument_namespace.validate_only:
        validate_stage14_artifacts()
        print("Stage 14 tournament artifacts validated.")
        return
    build_stage14_artifacts()


if __name__ == "__main__":
    main()
