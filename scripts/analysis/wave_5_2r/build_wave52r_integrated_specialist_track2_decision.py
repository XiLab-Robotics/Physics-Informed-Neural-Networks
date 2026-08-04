"""Build the Wave 5.2R integrated-specialist Track 2 decision artifacts."""

from __future__ import annotations

# Import Python Utilities
import csv
from datetime import datetime
from pathlib import Path
import statistics
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml


# Define Frozen Evidence Paths
PAYLOAD_DIAGNOSTICS_PATH = (
    PROJECT_ROOT
    / "output/validation_checks/wave52r_integrated_specialist_track2_curve_payload_diagnostics"
    / "2026-08-04-00-31-50__track2c_curve_payload_diagnostics/curve_payload_diagnostics.csv"
)
MATRIX_SUMMARY_PATH_BY_SURFACE = {
    "Fw": PROJECT_ROOT
    / "output/validation_checks/track2_reference_comparison"
    / "2026-08-03-21-58-09__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_forward"
    / "validation_summary.yaml",
    "Bw": PROJECT_ROOT
    / "output/validation_checks/track2_reference_comparison"
    / "2026-08-03-21-59-38__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_backward"
    / "validation_summary.yaml",
    "global": PROJECT_ROOT
    / "output/validation_checks/track2_reference_comparison"
    / "2026-08-03-22-01-08__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_global"
    / "validation_summary.yaml",
}
OUTPUT_ROOT = PROJECT_ROOT / "output/analysis/wave_5_2r/integrated_specialist_track2_decision"
SCORE_CSV_PATH = OUTPUT_ROOT / "multi_index_candidate_scores.csv"
DECISION_YAML_PATH = OUTPUT_ROOT / "multi_index_surface_decision.yaml"
SURFACE_DIRECTION_MAP = {"Fw": "forward", "Bw": "backward", "global": None}
BLOCK_WEIGHT_MAP = {
    "shape_harmonic_fidelity": 0.35,
    "raw_operating_error": 0.20,
    "offset_continuity": 0.20,
    "robustness": 0.15,
    "deployment_readiness": 0.10,
}
DEPLOYMENT_PENALTY_MAP = {
    "wave52r_promotion_k01_global_seed_271828": 0.00,
    "wave52r_integrated_a02_seed_314159": 0.20,
    "wave52r_promotion_h08_fw_seed_161803": 0.15,
}


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
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=False, width=120)


def load_payload_rows() -> list[dict[str, str]]:
    """Load the bounded CVP 1.2 shortlist evidence."""

    with PAYLOAD_DIAGNOSTICS_PATH.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def rank_loss_map(value_by_candidate: dict[str, float]) -> dict[str, float]:
    """Convert lower-is-better values to bounded average-rank losses."""

    ordered_value_list = sorted(set(value_by_candidate.values()))
    denominator = max(len(ordered_value_list) - 1, 1)
    return {
        candidate_id: ordered_value_list.index(value) / denominator
        for candidate_id, value in value_by_candidate.items()
    }


def mean_rank_block(
    metric_map_by_candidate: dict[str, dict[str, float]],
    metric_name_list: list[str],
) -> dict[str, float]:
    """Return the mean bounded rank loss across one metric block."""

    rank_map_by_metric = {
        metric_name: rank_loss_map(
            {
                candidate_id: metric_map[metric_name]
                for candidate_id, metric_map in metric_map_by_candidate.items()
            }
        )
        for metric_name in metric_name_list
    }
    return {
        candidate_id: statistics.fmean(
            rank_map_by_metric[metric_name][candidate_id]
            for metric_name in metric_name_list
        )
        for candidate_id in metric_map_by_candidate
    }


def candidate_veto_reason(candidate_id: str) -> str:
    """Return the frozen promotion veto for one shortlist candidate."""

    if candidate_id.startswith("wave52r_integrated_a") and "_a02_" not in candidate_id:
        return "campaign_branch_gate_failed"
    if candidate_id == "wave52r_promotion_h08_fw_seed_161803":
        return "frozen_h08_raw_and_offset_regression_vs_k01"
    return ""


def aggregate_surface_metrics(
    surface: str,
    payload_rows: list[dict[str, str]],
) -> dict[str, dict[str, float]]:
    """Aggregate raw and CVP 1.2 metrics for one official surface."""

    direction_label = SURFACE_DIRECTION_MAP[surface]
    matrix_summary = read_yaml(MATRIX_SUMMARY_PATH_BY_SURFACE[surface])
    raw_metric_map = matrix_summary["candidate_metric_summary"]
    surface_rows = [
        row
        for row in payload_rows
        if (direction_label is None or row["direction_label"] == direction_label)
        and row["candidate_id"] in raw_metric_map
    ]
    candidate_id_list = sorted({row["candidate_id"] for row in surface_rows})
    metric_map_by_candidate: dict[str, dict[str, float]] = {}
    for candidate_id in candidate_id_list:
        candidate_rows = [row for row in surface_rows if row["candidate_id"] == candidate_id]
        assert candidate_rows
        assert candidate_id in raw_metric_map
        metric_map_by_candidate[candidate_id] = {
            "raw_mae_deg": float(raw_metric_map[candidate_id]["mae"]),
            "raw_rmse_deg": float(raw_metric_map[candidate_id]["rmse"]),
            "mean_percentage_error_pct": float(raw_metric_map[candidate_id]["mean_percentage_error_pct"]),
            "p95_mean_percentage_error_pct": float(raw_metric_map[candidate_id]["p95_mean_percentage_error_pct"]),
            "absolute_offset_error_deg": statistics.fmean(
                float(row["absolute_curve_mean_error_deg"]) for row in candidate_rows
            ),
            "centered_shape_mae_deg": statistics.fmean(
                float(row["centered_curve_mae_deg"]) for row in candidate_rows
            ),
            "peak_to_peak_error_pct": statistics.fmean(
                float(row["peak_to_peak_error_pct"]) for row in candidate_rows
            ),
            "closure_mismatch_deg": statistics.fmean(
                float(row["closure_mismatch_deg"]) for row in candidate_rows
            ),
            "harmonic_amplitude_error_pct": statistics.fmean(
                float(row["mean_harmonic_amplitude_error_pct"]) for row in candidate_rows
            ),
            "harmonic_phase_error_deg": statistics.fmean(
                float(row["mean_harmonic_phase_error_deg"]) for row in candidate_rows
            ),
            "deployment_penalty": DEPLOYMENT_PENALTY_MAP.get(candidate_id, 1.0),
        }
    return metric_map_by_candidate


def build_surface_score_entries(
    surface: str,
    metric_map_by_candidate: dict[str, dict[str, float]],
) -> list[dict[str, Any]]:
    """Build transparent multi-index scores for one surface."""

    block_map = {
        "shape_harmonic_fidelity": mean_rank_block(
            metric_map_by_candidate,
            [
                "centered_shape_mae_deg",
                "peak_to_peak_error_pct",
                "harmonic_amplitude_error_pct",
                "harmonic_phase_error_deg",
            ],
        ),
        "raw_operating_error": mean_rank_block(
            metric_map_by_candidate,
            ["raw_mae_deg", "raw_rmse_deg", "mean_percentage_error_pct"],
        ),
        "offset_continuity": mean_rank_block(
            metric_map_by_candidate,
            ["absolute_offset_error_deg", "closure_mismatch_deg"],
        ),
        "robustness": mean_rank_block(
            metric_map_by_candidate,
            ["p95_mean_percentage_error_pct"],
        ),
        "deployment_readiness": {
            candidate_id: metric_map["deployment_penalty"]
            for candidate_id, metric_map in metric_map_by_candidate.items()
        },
    }
    entry_list = []
    for candidate_id, metric_map in metric_map_by_candidate.items():
        block_score_map = {
            block_name: block_map[block_name][candidate_id]
            for block_name in BLOCK_WEIGHT_MAP
        }
        composite_score = sum(
            BLOCK_WEIGHT_MAP[block_name] * block_score
            for block_name, block_score in block_score_map.items()
        )
        entry_list.append(
            {
                "surface": surface,
                "candidate_id": candidate_id,
                **metric_map,
                **{f"{block_name}_score": score for block_name, score in block_score_map.items()},
                "composite_score": composite_score,
                "veto_reason": candidate_veto_reason(candidate_id),
            }
        )
    entry_list.sort(key=lambda entry: (entry["composite_score"], entry["candidate_id"]))
    for rank, entry in enumerate(entry_list, start=1):
        entry["rank"] = rank
    return entry_list


def build_surface_decision(surface: str, entry_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Build axis winners and the veto-aware recommendation."""

    def winner(metric_name: str) -> str:
        return min(entry_list, key=lambda entry: (entry[metric_name], entry["candidate_id"]))["candidate_id"]

    eligible_entry_list = [entry for entry in entry_list if not entry["veto_reason"]]
    assert eligible_entry_list
    recommended_candidate_id = min(
        eligible_entry_list,
        key=lambda entry: (entry["composite_score"], entry["candidate_id"]),
    )["candidate_id"]
    return {
        "surface": surface,
        "best_raw_error": winner("raw_mae_deg"),
        "best_shape_fidelity": winner("shape_harmonic_fidelity_score"),
        "best_offset_behavior": winner("offset_continuity_score"),
        "best_robustness": winner("p95_mean_percentage_error_pct"),
        "best_unvetoed_composite": recommended_candidate_id,
        "recommended_candidate": recommended_candidate_id,
        "accepted_registry_changed": False,
    }


def write_score_csv(entry_list: list[dict[str, Any]]) -> None:
    """Write the machine-readable candidate score table."""

    SCORE_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    field_name_list = list(entry_list[0].keys())
    with SCORE_CSV_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_name_list)
        writer.writeheader()
        writer.writerows(entry_list)


def main() -> None:
    """Build the three-surface official decision artifacts."""

    payload_rows = load_payload_rows()
    all_entry_list = []
    surface_decision_list = []
    for surface in ("Fw", "Bw", "global"):
        surface_entry_list = build_surface_score_entries(
            surface,
            aggregate_surface_metrics(surface, payload_rows),
        )
        all_entry_list.extend(surface_entry_list)
        surface_decision_list.append(build_surface_decision(surface, surface_entry_list))
    write_score_csv(all_entry_list)
    write_yaml(
        DECISION_YAML_PATH,
        {
            "schema_version": 1,
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "policy": {
                "policy_path": "doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md",
                "lower_score_is_better": True,
                "block_weight_map": BLOCK_WEIGHT_MAP,
                "normalization": "bounded_average_rank_loss_within_surface_shortlist",
                "veto_policy": "campaign gate failures and frozen H08 regression remain non-promotable",
            },
            "evidence_scope": {
                "matrix_candidate_count": 29,
                "cvp_1_2_shortlist_candidate_count": 9,
                "visual_shortlist_candidate_count": 15,
                "duplicate_a08_note": "A08 is prediction-equivalent to A02 and is not rescored as an independent candidate.",
            },
            "surface_decision_list": surface_decision_list,
            "accepted_registry_changed": False,
            "deployment_claim_authorized": False,
            "score_csv_path": SCORE_CSV_PATH.relative_to(PROJECT_ROOT).as_posix(),
        },
    )
    for decision in surface_decision_list:
        print(
            "[DECISION] "
            f"surface={decision['surface']} | recommended={decision['recommended_candidate']} | "
            f"raw={decision['best_raw_error']} | shape={decision['best_shape_fidelity']} | "
            f"offset={decision['best_offset_behavior']} | robustness={decision['best_robustness']}"
        )


if __name__ == "__main__":
    main()
