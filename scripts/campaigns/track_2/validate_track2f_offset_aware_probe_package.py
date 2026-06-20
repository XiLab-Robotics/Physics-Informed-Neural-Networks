"""Validate the prepared Wave 3.1 offset-aware probe package."""

from __future__ import annotations

# Import Python Utilities
import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_NAME = "track2f_offset_aware_probe_campaign_2026_06_03"
EXPECTED_SURFACE_LIST = ["global", "fw", "bw"]
EXPECTED_INTERVENTION_LIST = [
    "posthoc_direction_torque_offset_baseline",
    "sequential_residual_offset_probe",
    "multi_head_shape_offset_probe",
]
TRACK2E_RECOMMENDATION_PATH = Path(
    "output/validation_checks/track2e_offset_predictability_feasibility/"
    "2026-06-03-13-28-54__track2e_offset_predictability_feasibility/"
    "track2e_surface_intervention_recommendation.csv"
)


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file as a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML payload with stable formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")


def load_descriptor_list(descriptor_root: Path) -> list[dict[str, Any]]:

    """Load all probe descriptor YAML files."""

    descriptor_path_list = sorted(descriptor_root.glob("*.yaml"))
    assert descriptor_path_list, f"No descriptor YAML files found | {descriptor_root}"

    descriptor_list: list[dict[str, Any]] = []
    for descriptor_path in descriptor_path_list:
        descriptor = read_yaml_file(descriptor_path)
        descriptor["descriptor_path"] = descriptor_path.as_posix()
        descriptor_list.append(descriptor)
    return descriptor_list


def validate_descriptor_matrix(descriptor_list: list[dict[str, Any]]) -> None:

    """Validate that the descriptor matrix has the expected Wave 3.1 shape."""

    assert len(descriptor_list) == 9, f"Expected 9 descriptors | found={len(descriptor_list)}"

    observed_pair_set = {
        (str(descriptor["surface_key"]), str(descriptor["intervention"]))
        for descriptor in descriptor_list
    }
    expected_pair_set = {
        (surface_name, intervention_name)
        for surface_name in EXPECTED_SURFACE_LIST
        for intervention_name in EXPECTED_INTERVENTION_LIST
    }
    missing_pair_set = expected_pair_set.difference(observed_pair_set)
    unexpected_pair_set = observed_pair_set.difference(expected_pair_set)
    assert not missing_pair_set, f"Missing Wave 3.1 descriptor pairs | {sorted(missing_pair_set)}"
    assert not unexpected_pair_set, f"Unexpected Wave 3.1 descriptor pairs | {sorted(unexpected_pair_set)}"

    for descriptor in descriptor_list:
        assert descriptor.get("campaign_name") == CAMPAIGN_NAME
        assert "runtime_input_contract" in descriptor
        assert descriptor.get("implementation_status") in [
            "runnable_posthoc_baseline",
            "runnable_training_entry",
            "blocked_until_model_type_implementation",
        ]


def validate_active_campaign_state() -> None:

    """Validate that the persistent active-campaign state points at Wave 3.1."""

    active_state_path = PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH
    active_state = read_yaml_file(active_state_path)
    assert active_state.get("status") == "prepared", "Wave 3.1 campaign state is not prepared."
    assert active_state.get("campaign_name") == CAMPAIGN_NAME, (
        "Active campaign state does not point at Wave 3.1."
    )


def load_track2e_recommendation_rows() -> list[dict[str, str]]:

    """Load the CVP 1.5 surface recommendation table."""

    recommendation_path = PROJECT_PATH / TRACK2E_RECOMMENDATION_PATH
    assert recommendation_path.exists(), f"Missing CVP 1.5 recommendation CSV | {recommendation_path}"
    with recommendation_path.open("r", encoding="utf-8", newline="") as input_file:
        return list(csv.DictReader(input_file))


def write_baseline_status_artifacts(
    descriptor_list: list[dict[str, Any]],
    output_root: Path,
) -> None:

    """Write a light validation artifact for the runnable baseline descriptors."""

    recommendation_row_list = load_track2e_recommendation_rows()
    recommendation_by_surface = {
        str(row["candidate_surface"]).lower(): row
        for row in recommendation_row_list
    }

    output_root.mkdir(parents=True, exist_ok=True)
    status_csv_path = output_root / "track2f_probe_entry_status.csv"
    summary_yaml_path = output_root / "track2f_probe_package_summary.yaml"

    field_name_list = [
        "probe_id",
        "surface",
        "intervention",
        "implementation_status",
        "track2e_reference_candidate",
        "track2e_corrected_mae_upper_bound_deg",
        "track2e_correction_gain_pct",
        "launch_decision",
    ]
    with status_csv_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_name_list)
        writer.writeheader()
        for descriptor in descriptor_list:
            surface_name = str(descriptor["surface"]).lower()
            recommendation_row = recommendation_by_surface.get(surface_name, {})
            implementation_status = str(descriptor["implementation_status"])
            if implementation_status == "runnable_posthoc_baseline":
                launch_decision = "runnable_baseline_validation"
            elif implementation_status == "runnable_training_entry":
                launch_decision = "runnable_training_campaign_entry"
            else:
                launch_decision = "blocked_pending_model_type"
            writer.writerow(
                {
                    "probe_id": descriptor["probe_id"],
                    "surface": descriptor["surface"],
                    "intervention": descriptor["intervention"],
                    "implementation_status": implementation_status,
                    "track2e_reference_candidate": recommendation_row.get("candidate_id", ""),
                    "track2e_corrected_mae_upper_bound_deg": recommendation_row.get(
                        "corrected_mae_upper_bound_deg",
                        "",
                    ),
                    "track2e_correction_gain_pct": recommendation_row.get("correction_gain_pct", ""),
                    "launch_decision": launch_decision,
                }
            )

    blocked_descriptor_count = sum(
        1
        for descriptor in descriptor_list
        if descriptor["implementation_status"] == "blocked_until_model_type_implementation"
    )
    runnable_baseline_count = sum(
        1
        for descriptor in descriptor_list
        if descriptor["implementation_status"] == "runnable_posthoc_baseline"
    )
    runnable_training_count = sum(
        1
        for descriptor in descriptor_list
        if descriptor["implementation_status"] == "runnable_training_entry"
    )
    write_yaml_file(
        summary_yaml_path,
        {
            "campaign_name": CAMPAIGN_NAME,
            "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "descriptor_count": len(descriptor_list),
            "runnable_posthoc_baseline_count": runnable_baseline_count,
            "runnable_training_entry_count": runnable_training_count,
            "blocked_learned_probe_count": blocked_descriptor_count,
            "status_csv_path": status_csv_path.relative_to(PROJECT_PATH).as_posix(),
            "track2e_recommendation_path": TRACK2E_RECOMMENDATION_PATH.as_posix(),
            "training_launch_status": "sequential_residual_offset_probe_enabled_multi_head_blocked",
        },
    )

    print(f"TRACK2F_STATUS_CSV={status_csv_path.relative_to(PROJECT_PATH).as_posix()}")
    print(f"TRACK2F_SUMMARY_YAML={summary_yaml_path.relative_to(PROJECT_PATH).as_posix()}")


def parse_arguments() -> argparse.Namespace:

    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--descriptor-root",
        required=True,
        type=Path,
        help="Repository-relative directory containing Wave 3.1 probe descriptors.",
    )
    parser.add_argument(
        "--require-prepared-state",
        action="store_true",
        help="Require doc/running/active_training_campaign.yaml to point at Wave 3.1.",
    )
    parser.add_argument(
        "--write-baseline-status",
        action="store_true",
        help="Write non-training baseline status artifacts for the prepared descriptors.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(
            "output/validation_checks/track2f_offset_aware_probe/"
            "2026-06-03_track2f_offset_aware_probe_prelaunch"
        ),
        help="Repository-relative output root for optional validation artifacts.",
    )
    return parser.parse_args()


def main() -> int:

    """Validate the Wave 3.1 package."""

    argument_namespace = parse_arguments()
    descriptor_root = PROJECT_PATH / argument_namespace.descriptor_root
    output_root = PROJECT_PATH / argument_namespace.output_root

    descriptor_list = load_descriptor_list(descriptor_root)
    validate_descriptor_matrix(descriptor_list)
    if argument_namespace.require_prepared_state:
        validate_active_campaign_state()
    if argument_namespace.write_baseline_status:
        write_baseline_status_artifacts(descriptor_list, output_root)

    runnable_count = sum(
        1
        for descriptor in descriptor_list
        if descriptor["implementation_status"] in [
            "runnable_posthoc_baseline",
            "runnable_training_entry",
        ]
    )
    blocked_count = len(descriptor_list) - runnable_count
    print(
        "Wave 3.1 package validated | "
        f"descriptors={len(descriptor_list)} | runnable_entries={runnable_count} | "
        f"blocked_learned_probes={blocked_count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
