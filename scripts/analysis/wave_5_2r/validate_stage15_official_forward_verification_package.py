"""Validate the Wave 5.2R Stage 15 verification package without running it."""

from __future__ import annotations

# Import Python Utilities
import argparse
from datetime import datetime
from pathlib import Path
import re
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Scientific Python Utilities
import numpy as np
import yaml

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import (
    harmonic_wise_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)


# Define The Frozen Stage 15 Package
DEFAULT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "wave52r_stage15_official_forward_verification_matrix.yaml"
)
FROZEN_PREDICTION_PATH = (
    PROJECT_ROOT
    / "output"
    / "training_runs"
    / "complex_harmonic_coefficient_residuals"
    / "2026-07-28-16-17-13__stage5_h04"
    / "test_predictions.npz"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "analysis"
    / "wave_5_2r"
    / "stage15_official_forward_verification"
    / "stage15_package_preflight.yaml"
)
CONDITION_ID_PATTERN = re.compile(
    r"^speed_(?P<speed>[0-9]+)rpm__"
    r"torque_(?P<torque>[0-9]+)Nm__"
    r"temperature_(?P<temperature>[0-9]+)degC$"
)


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping with a normal final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def build_frozen_curve_record(
    condition_id: str,
    angular_sample_count: int,
) -> harmonic_wise_support.HarmonicCurveRecord:
    """Build one metadata-only curve record from a frozen condition ID."""

    condition_match = CONDITION_ID_PATTERN.fullmatch(condition_id)
    assert condition_match is not None, (
        f"Unsupported frozen Stage 5 condition ID | {condition_id}"
    )
    angular_position_deg = np.linspace(
        0.0,
        360.0,
        num=angular_sample_count,
        endpoint=False,
        dtype=np.float32,
    )
    return harmonic_wise_support.HarmonicCurveRecord(
        source_file_path=Path(f"{condition_id}.csv"),
        direction_label="forward",
        direction_flag=1.0,
        speed_rpm=float(condition_match.group("speed")),
        torque_nm=float(condition_match.group("torque")),
        oil_temperature_deg=float(
            condition_match.group("temperature")
        ),
        angular_position_deg=angular_position_deg,
        transmission_error_deg=np.zeros_like(angular_position_deg),
        coefficient_dictionary={},
        amplitude_phase_dictionary={},
        input_feature_matrix=None,
    )


def validate_package(config_path: Path) -> dict[str, Any]:
    """Validate candidate loading and exact H04 frozen-payload replay."""

    training_config = (
        reference_family_vs_feedforward_support
        .load_reference_family_comparison_config(config_path)
    )
    candidate_configuration_list = (
        reference_family_vs_feedforward_support
        .resolve_track2_candidate_configuration_list(training_config)
    )
    candidate_id_list = [
        str(candidate_configuration["candidate_id"])
        for candidate_configuration in candidate_configuration_list
    ]
    assert len(candidate_id_list) == 4
    assert len(set(candidate_id_list)) == len(candidate_id_list)

    h04_configuration = candidate_configuration_list[0]
    pf_a_configuration = candidate_configuration_list[1]
    h04_candidate = (
        reference_family_vs_feedforward_support.load_track2_candidate(
            h04_configuration
        )
    )
    pf_a_candidate = (
        reference_family_vs_feedforward_support.load_track2_candidate(
            pf_a_configuration
        )
    )
    assert h04_candidate.training_config is not None
    assert pf_a_candidate.training_config is not None
    assert not h04_candidate.training_config["anchor_only"]
    assert pf_a_candidate.training_config["anchor_only"]

    frozen_payload = np.load(FROZEN_PREDICTION_PATH)
    frozen_condition_id_array = frozen_payload["condition_id"]
    frozen_prediction_matrix = frozen_payload["predicted_curve"]
    assert frozen_prediction_matrix.shape == (97, 2048)
    replay_curve_list = []
    anchor_curve_list = []
    for condition_id in frozen_condition_id_array.tolist():
        curve_record = build_frozen_curve_record(
            str(condition_id),
            angular_sample_count=2048,
        )
        replay_curve_list.append(
            reference_family_vs_feedforward_support
            .predict_stage5_coefficient_residual_curve(
                h04_candidate.model_object,
                h04_candidate.training_config,
                curve_record,
            )
        )
        anchor_curve_list.append(
            reference_family_vs_feedforward_support
            .predict_stage5_coefficient_residual_curve(
                pf_a_candidate.model_object,
                pf_a_candidate.training_config,
                curve_record,
            )
        )

    replay_curve_matrix = np.vstack(replay_curve_list)
    anchor_curve_matrix = np.vstack(anchor_curve_list)
    replay_max_abs_difference_deg = float(
        np.max(
            np.abs(
                replay_curve_matrix
                - frozen_prediction_matrix.astype(np.float32)
            )
        )
    )
    assert replay_max_abs_difference_deg <= 1.0e-6, (
        "Stage 15 H04 adapter does not reproduce the frozen Stage 5 payload | "
        f"max_abs_difference_deg={replay_max_abs_difference_deg:.12g}"
    )
    analytical_correction_rms_deg = float(
        np.sqrt(
            np.mean(
                np.square(replay_curve_matrix - anchor_curve_matrix)
            )
        )
    )
    assert analytical_correction_rms_deg > 0.0

    for candidate_configuration in candidate_configuration_list[2:]:
        inventory_path = (
            reference_family_vs_feedforward_support
            .shared_training_infrastructure
            .resolve_runtime_project_relative_path(
                candidate_configuration["reference_inventory_path"]
            )
        )
        assert inventory_path.is_file()

    result = {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "status": "passed",
        "config_path": config_path.relative_to(PROJECT_ROOT).as_posix(),
        "candidate_id_list": candidate_id_list,
        "forward_test_curve_count": 97,
        "angular_sample_count": 2048,
        "h04_frozen_replay_max_abs_difference_deg": (
            replay_max_abs_difference_deg
        ),
        "h04_vs_pf_a_correction_rms_deg": (
            analytical_correction_rms_deg
        ),
        "heavy_matrix_executed": False,
    }
    write_yaml(OUTPUT_PATH, result)
    return result


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(
        description="Validate the Stage 15 verification package."
    )
    argument_parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
    )
    return argument_parser.parse_args()


def main() -> None:
    """Run the package preflight."""

    arguments = parse_arguments()
    result = validate_package(arguments.config_path.resolve())
    print(
        "[PASS] Stage 15 package preflight | "
        f"candidates={len(result['candidate_id_list'])} | "
        "H04 replay max abs difference="
        f"{result['h04_frozen_replay_max_abs_difference_deg']:.3e} deg",
        flush=True,
    )


if __name__ == "__main__":
    main()
