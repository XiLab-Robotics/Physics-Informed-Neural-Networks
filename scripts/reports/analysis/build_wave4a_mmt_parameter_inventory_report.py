"""Build the Wave 5.2A MMT parameter-inventory report."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Serialization Libraries
import yaml


DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave4_mmt_parameter_inventory"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "wave4" / "mmt_parameter_inventory"
REPORT_FILENAME = "wave4a_mmt_parameter_inventory.md"
INVENTORY_FILENAME = "wave4a_mmt_parameter_inventory.csv"
SUMMARY_FILENAME = "wave4a_mmt_parameter_inventory_summary.yaml"


def build_inventory_rows() -> list[dict[str, str]]:

    """Build the MMT parameter availability inventory."""

    return [
        {
            "parameter_group": "tooth_counts",
            "paper_variables": "z1, z2, z4, z5",
            "implemented_location": "ReducerParameters.z1/z2/z4/z5",
            "availability_class": "known_geometry_constant",
            "repository_source": "MMT paper Table 3 and current RV-80E defaults",
            "current_value_or_policy": "z1=10, z2=38, z4=39, z5=40",
            "calibration_policy": "locked unless the reducer hardware changes",
            "leakage_risk": "none",
            "downstream_decision": "allowed_for_wave4b_features_and_wave4c_losses",
            "notes": "Defines the MMT transfer ratios and expected cycloid-pin mesh harmonic family.",
        },
        {
            "parameter_group": "involute_gear_geometry",
            "paper_variables": "m, alpha, lb1, lb2, ln",
            "implemented_location": "ReducerParameters.module_mm, pressure_angle_rad, derived base radii",
            "availability_class": "known_geometry_constant",
            "repository_source": "MMT paper Table 3 and implemented derived geometry",
            "current_value_or_policy": "module=1.75 mm, pressure_angle=20 deg; lb1/lb2/ln derived",
            "calibration_policy": "locked after geometry confirmation",
            "leakage_risk": "none",
            "downstream_decision": "allowed_for_diagnostic_and_feature_generation",
            "notes": "High-speed involute stage is useful but is not the dominant paper-reported RTE source.",
        },
        {
            "parameter_group": "pin_and_crank_geometry",
            "paper_variables": "lR, la, r, lHi, lai, lv",
            "implemented_location": "ReducerParameters.pin_pitch_radius_mm/crank_eccentricity_mm/pin_radius_mm",
            "availability_class": "known_geometry_constant",
            "repository_source": "MMT paper Table 3 and current RV-80E defaults",
            "current_value_or_policy": "lR=77.5 mm, la=1.5 mm, pin_radius=4.0 mm",
            "calibration_policy": "locked after reducer-specific geometry confirmation",
            "leakage_risk": "none",
            "downstream_decision": "allowed_for_wave4a_diagnostic_and_wave4b_features",
            "notes": "Core low-speed geometry; required before any physical interpretation of high harmonics.",
        },
        {
            "parameter_group": "operating_condition_metadata",
            "paper_variables": "theta1, thetaH, theta3 plus test condition labels",
            "implemented_location": "output_and_crank_angles(), measured TE curve metadata",
            "availability_class": "known_dataset_metadata",
            "repository_source": "dataset speed, torque, oil temperature, direction, TE angle grid",
            "current_value_or_policy": "available as causal condition labels; angle grid requires unit/wrap confirmation",
            "calibration_policy": "not calibrated; used for stratification and causal conditioning",
            "leakage_risk": "low if no target-derived curve mean or future TE is used at inference",
            "downstream_decision": "allowed_for_dataset_aligned_diagnostics",
            "notes": "The MMT model is kinematic; speed, torque, and temperature should stratify residuals, not force direct physics terms yet.",
        },
        {
            "parameter_group": "contact_geometry_state",
            "paper_variables": "theta_p, theta_k, theta_rho, theta_ci, x_c, y_c, x_k, y_k, xO4, yO4",
            "implemented_location": "run_rv80e_demo() placeholder contact sweep",
            "availability_class": "unavailable_or_ambiguous",
            "repository_source": "not directly present in the dataset; current code uses a transparent demo sweep",
            "current_value_or_policy": "must be reconstructed or parameterized before quantitative dataset claims",
            "calibration_policy": "blocked until reducer-specific contact reconstruction is defined",
            "leakage_risk": "high if fitted directly from held-out TE curves",
            "downstream_decision": "diagnostic_only_until_reconstruction_gate",
            "notes": "This is the main blocker for treating Wave 5.2A as a calibrated analytical baseline.",
        },
        {
            "parameter_group": "high_speed_original_errors",
            "paper_variables": "Eb1, Eb2, delta_l_b1, delta_l_b2, delta_theta_b1",
            "implemented_location": "EquivalentErrors.delta_l_b1_mm/delta_l_b2_mm/delta_theta_b1_rad",
            "availability_class": "calibratable_train_only",
            "repository_source": "paper Table 4 provides prototype values; dataset does not expose per-curve component measurements",
            "current_value_or_policy": "demo defaults use delta_l_b2=0.005 mm and zero input angle error",
            "calibration_policy": "fit only on training groups if used; keep validation/test untouched",
            "leakage_risk": "medium",
            "downstream_decision": "candidate_feature_or_weak_loss_after_calibration",
            "notes": "Paper reports smaller influence than low-speed errors for the prototype case.",
        },
        {
            "parameter_group": "crankshaft_and_cycloid_hole_errors",
            "paper_variables": "EH, Ec, Ea, delta_l_H, delta_l_c, delta_l_a",
            "implemented_location": "EquivalentErrors.delta_l_h_mm/delta_l_c_mm/delta_l_a_mm",
            "availability_class": "calibratable_train_only",
            "repository_source": "paper Table 4 and measured-component discussion; not present as dataset columns",
            "current_value_or_policy": "demo defaults: EH=0.004 mm, Ec=0.005 mm, Ea=0.003 mm",
            "calibration_policy": "fit as grouped equivalent-error channels on train only",
            "leakage_risk": "medium",
            "downstream_decision": "high_priority_wave4b_candidate_features",
            "notes": "Paper links these low-speed-stage errors to large RTE influence and high-frequency content.",
        },
        {
            "parameter_group": "cycloidal_profile_and_pin_radius_errors",
            "paper_variables": "delta, delta_r, delta_theta_c, delta_l_k, delta_l_rho",
            "implemented_location": "EquivalentErrors.cycloidal_profile_error_mm/pin_radius_error_mm",
            "availability_class": "calibratable_train_only",
            "repository_source": "paper Table 4; dataset lacks direct per-curve profile and pin-radius measurements",
            "current_value_or_policy": "demo defaults: profile=0.005 mm, pin_radius_error=0.002 mm",
            "calibration_policy": "fit as bounded low-speed equivalent-error channel on train only",
            "leakage_risk": "medium",
            "downstream_decision": "high_priority_wave4b_and_wave4c_candidate",
            "notes": "Directly affects cycloid-pin contribution f3 and is relevant to fragile high-order harmonics.",
        },
        {
            "parameter_group": "pin_pitch_circle_and_accumulated_pitch_errors",
            "paper_variables": "delta_l_R, AP, delta_theta_p",
            "implemented_location": "EquivalentErrors.delta_l_r_mm/accumulative_pitch_error_mm",
            "availability_class": "calibratable_train_only",
            "repository_source": "paper Table 4; dataset does not expose pin pitch measurement channels",
            "current_value_or_policy": "demo defaults: delta_l_R=0.005 mm, AP amplitude=0.005 mm",
            "calibration_policy": "fit on train by direction and load group only if stable",
            "leakage_risk": "medium",
            "downstream_decision": "candidate_for_offset_and_low_frequency_diagnostics",
            "notes": "Paper identifies AP variation as low-frequency and therefore relevant to mean/low-order residual checks.",
        },
        {
            "parameter_group": "output_disc_assembly_error",
            "paper_variables": "Ao, gamma_o, delta_l_H, delta_l_v",
            "implemented_location": "output_disc_assembly_errors() helper",
            "availability_class": "calibratable_train_only",
            "repository_source": "paper original-error mapping and frequency interpretation",
            "current_value_or_policy": "implemented helper exists, not used in the current demo defaults",
            "calibration_policy": "fit only as a causal latent or grouped train-only parameter",
            "leakage_risk": "high if tuned curve-by-curve from target mean",
            "downstream_decision": "candidate_latent_state_or_hysteresis_channel",
            "notes": "Paper attributes frequency component 1 to output-disc hole-position deviation.",
        },
        {
            "parameter_group": "measured_te_target",
            "paper_variables": "Delta theta_H, theta_H - theta1 / I",
            "implemented_location": "measured_rte() and repository TE target curves",
            "availability_class": "available_as_target_only",
            "repository_source": "measured TE curves",
            "current_value_or_policy": "allowed for evaluation and train-only calibration objectives",
            "calibration_policy": "never use held-out target means or full curves at inference",
            "leakage_risk": "high if used to normalize or calibrate held-out curves",
            "downstream_decision": "evaluation_target_not_inference_input",
            "notes": "Critical boundary for Wave 5.2B and Wave 5.2C leakage-safe design.",
        },
    ]


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def count_rows_by_field(row_list: list[dict[str, str]], field_name: str) -> dict[str, int]:

    """Count inventory rows by a categorical field."""

    output_dictionary: dict[str, int] = {}
    for row in row_list:
        key = row[field_name]
        output_dictionary[key] = output_dictionary.get(key, 0) + 1
    return dict(sorted(output_dictionary.items()))


def is_high_leakage_risk(row: dict[str, str]) -> bool:

    """Return whether an inventory row has high leakage risk."""

    return row["leakage_risk"].startswith("high")


def build_report_lines(run_id: str, row_list: list[dict[str, str]], output_directory: Path) -> list[str]:

    """Build the Wave 5.2A MMT parameter-inventory Markdown report."""

    availability_counts = count_rows_by_field(row_list, "availability_class")
    decision_counts = count_rows_by_field(row_list, "downstream_decision")
    high_risk_rows = [row for row in row_list if is_high_leakage_risk(row)]
    calibratable_rows = [row for row in row_list if row["availability_class"] == "calibratable_train_only"]

    report_lines = [
        "# Wave 5.2A MMT Parameter Inventory",
        "",
        "## Overview",
        "",
        (
            "This report classifies the inputs required by the repository-owned "
            "`MMT_TEModeling` equation chain before those equations are used as "
            "causal features, calibrated analytical baselines, or weak PINN losses."
        ),
        "",
        (
            "The inventory is intentionally not a training campaign. It does not "
            "create queue YAMLs, launchers, or active-campaign state."
        ),
        "",
        "## Summary",
        "",
        "| Field | Value |",
        "| --- | ---: |",
        f"| Run ID | `{run_id}` |",
        f"| Inventory Rows | {len(row_list)} |",
        f"| Train-Only Calibratable Groups | {len(calibratable_rows)} |",
        f"| High Leakage-Risk Groups | {len(high_risk_rows)} |",
        "| Campaign Readiness | `not_campaign_ready` |",
        "",
        "## Availability Summary",
        "",
        "| Availability Class | Count |",
        "| --- | ---: |",
    ]

    for availability_class, count in availability_counts.items():
        report_lines.append(f"| `{availability_class}` | {count} |")

    report_lines.extend(
        [
            "",
            "## Downstream Decision Summary",
            "",
            "| Downstream Decision | Count |",
            "| --- | ---: |",
        ]
    )

    for decision, count in decision_counts.items():
        report_lines.append(f"| `{decision}` | {count} |")

    report_lines.extend(
        [
            "",
            "## Parameter Inventory",
            "",
            "| Group | Availability | Leakage | Downstream Decision | Policy |",
            "| --- | --- | --- | --- | --- |",
        ]
    )

    for row in row_list:
        report_lines.append(
            f"| `{row['parameter_group']}` | `{row['availability_class']}` | "
            f"`{row['leakage_risk']}` | `{row['downstream_decision']}` | "
            f"{row['calibration_policy']} |"
        )

    report_lines.extend(
        [
            "",
            "## High-Risk Boundaries",
            "",
            "| Group | Reason | Required Gate |",
            "| --- | --- | --- |",
        ]
    )

    for row in high_risk_rows:
        report_lines.append(
            f"| `{row['parameter_group']}` | {row['notes']} | {row['calibration_policy']} |"
        )

    report_lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "The MMT path is usable today as an auditable diagnostic and as a "
                "source of geometry-locked harmonic hypotheses. It is not yet a "
                "dataset-calibrated predictor because contact geometry and original "
                "component-error channels are not directly observed in the current "
                "TE Curve Verification Pipeline dataset."
            ),
            "",
            (
                "`Wave 5.2B` should start with geometry-locked features plus train-only "
                "calibrated equivalent-error groups. `Wave 5.2C` should remain weak-loss "
                "only until the feature path proves that MMT terms explain held-out "
                "offset or fragile-harmonic structure without leakage."
            ),
            "",
            (
                "The paper supports low-speed-stage error groups as high-priority "
                "candidates. The output-disc assembly channel is especially relevant "
                "to the low-order frequency-1 family, but it must be handled as a "
                "latent or grouped calibration channel, not as a per-curve target "
                "mean correction."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / INVENTORY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py",
            "```",
        ]
    )
    return report_lines


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument("--report-date", type=str, default="")
    return parser.parse_args()


def main() -> None:

    """Build the Wave 5.2A MMT parameter-inventory report."""

    args = parse_arguments()
    run_id = args.run_id if args.run_id else f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__wave4a_mmt_parameter_inventory"
    report_date = args.report_date if args.report_date else datetime.now().strftime("%Y-%m-%d")
    output_directory = args.output_root / run_id
    report_directory = args.report_topic_root / f"[{report_date}]"
    report_path = report_directory / REPORT_FILENAME

    row_list = build_inventory_rows()
    summary_dictionary = {
        "run_id": run_id,
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "inventory_path": (output_directory / INVENTORY_FILENAME).relative_to(PROJECT_PATH).as_posix(),
        "row_count": len(row_list),
        "availability_counts": count_rows_by_field(row_list, "availability_class"),
        "downstream_decision_counts": count_rows_by_field(row_list, "downstream_decision"),
        "high_leakage_risk_count": len([row for row in row_list if is_high_leakage_risk(row)]),
        "campaign_readiness": "not_campaign_ready",
        "decision": "wave4a_inventory_complete_wave4b_wave4c_require_dataset_aligned_calibration",
    }

    write_csv(output_directory / INVENTORY_FILENAME, row_list)
    output_directory.mkdir(parents=True, exist_ok=True)
    with (output_directory / SUMMARY_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)

    report_directory.mkdir(parents=True, exist_ok=True)
    report_lines = build_report_lines(run_id=run_id, row_list=row_list, output_directory=output_directory)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Prepared Wave 5.2A MMT parameter-inventory artifacts | {output_directory}")
    print(f"Prepared Wave 5.2A MMT parameter-inventory report | {report_path}")


if __name__ == "__main__":
    main()
