"""Wave 5.2B MMT feature-generator skeleton.

This module exposes a leakage-aware feature schema and a dry-run sample payload
derived from the existing Wave 5.2A MMT diagnostic curve. It is not a training
entry point and must remain campaign-disabled until a later approved campaign
package selects consumers, losses, and surfaces.
"""

from __future__ import annotations

# Import Standard Libraries
import csv
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Import Numerical Libraries
import numpy as np

# Import Project Utilities
from scripts.models.wave4_mmt_diagnostic_adapter import Wave4MMTDiagnosticAdapter
from scripts.paper_reimplementation.mmt_te_modeling.mmt_te_modeling_reproduction import ARCSECOND_PER_RADIAN


DEFAULT_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
INFERENCE_SAFE = "inference_safe"
TRAIN_ONLY_CALIBRATION = "train_only_calibration"
DIAGNOSTIC_ONLY = "diagnostic_only"


@dataclass(frozen=True)
class Wave4BFeatureSpecification:

    """Metadata for one candidate Wave 5.2B feature or label field."""

    feature_name: str
    feature_group: str
    feature_kind: str
    usage_policy: str
    leakage_risk: str
    source_boundary: str
    notes: str


@dataclass(frozen=True)
class Wave4BFeaturePayload:

    """Dry-run feature output bundle."""

    schema_row_list: list[dict[str, str]]
    sample_row_list: list[dict[str, Any]]
    harmonic_row_list: list[dict[str, Any]]
    status_dictionary: dict[str, Any]


def format_float(value: float) -> str:

    """Format one float for stable CSV output."""

    return f"{float(value):.9f}"


def build_feature_schema() -> list[Wave4BFeatureSpecification]:

    """Build the conservative Wave 5.2B feature schema."""

    return [
        Wave4BFeatureSpecification(
            feature_name="mmt_rte_arcsec",
            feature_group="global_analytical_curve",
            feature_kind="point_curve_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_geometry_and_train_only_calibration_are_locked",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Raw analytical RTE curve sample from the MMT equation chain.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_centered_rte_arcsec",
            feature_group="global_analytical_curve",
            feature_kind="point_curve_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_centering_uses_mmt_curve_only",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Centered analytical curve; no measured TE mean is used.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_rte_mean_arcsec",
            feature_group="global_analytical_curve",
            feature_kind="curve_summary_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_computed_from_mmt_curve_only",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Analytical curve mean, not a measured target mean.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_rte_peak_to_peak_arcsec",
            feature_group="global_analytical_curve",
            feature_kind="curve_summary_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_computed_from_mmt_curve_only",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Analytical curve peak-to-peak amplitude.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_harmonic_amplitude_arcsec",
            feature_group="harmonic_terms",
            feature_kind="harmonic_summary_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_computed_from_mmt_curve_only",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Amplitude for selected harmonic bins from the MMT curve.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_harmonic_phase_rad",
            feature_group="harmonic_terms",
            feature_kind="harmonic_summary_feature",
            usage_policy=INFERENCE_SAFE,
            leakage_risk="none_if_computed_from_mmt_curve_only",
            source_boundary="Wave 5.2A MMT diagnostic curve",
            notes="Phase for selected harmonic bins from the MMT curve.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_subsystem_f1_high_speed_involute",
            feature_group="subsystem_terms",
            feature_kind="future_subsystem_feature",
            usage_policy=DIAGNOSTIC_ONLY,
            leakage_risk="medium_until_dataset_aligned_parameter_gate",
            source_boundary="MMT equation-chain subsystem term",
            notes="Reserved schema slot; not emitted as inference feature in this skeleton.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_subsystem_f2i_crankshaft_input_average",
            feature_group="subsystem_terms",
            feature_kind="future_subsystem_feature",
            usage_policy=TRAIN_ONLY_CALIBRATION,
            leakage_risk="medium_if_equivalent_errors_are_fit_on_held_out_curves",
            source_boundary="MMT equation-chain subsystem term",
            notes="Reserved for grouped train-only equivalent-error calibration.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_subsystem_f3_cycloid_pin",
            feature_group="subsystem_terms",
            feature_kind="future_subsystem_feature",
            usage_policy=TRAIN_ONLY_CALIBRATION,
            leakage_risk="medium_if_profile_or_pin_errors_are_fit_on_held_out_curves",
            source_boundary="MMT equation-chain subsystem term",
            notes="High-priority future feature, blocked until calibration policy is explicit.",
        ),
        Wave4BFeatureSpecification(
            feature_name="mmt_subsystem_f4i_crankshaft_output_average",
            feature_group="subsystem_terms",
            feature_kind="future_subsystem_feature",
            usage_policy=TRAIN_ONLY_CALIBRATION,
            leakage_risk="high_if_tuned_curve_by_curve_from_target_mean",
            source_boundary="MMT equation-chain subsystem term",
            notes="Reserved for grouped latent-state or hysteresis-like calibration.",
        ),
        Wave4BFeatureSpecification(
            feature_name="measured_minus_mmt_mean_offset_arcsec",
            feature_group="residual_terms",
            feature_kind="residual_label",
            usage_policy=DIAGNOSTIC_ONLY,
            leakage_risk="high_if_used_at_inference",
            source_boundary="measured TE target minus MMT analytical curve",
            notes="Allowed only as training/evaluation label material, never as inference feature.",
        ),
        Wave4BFeatureSpecification(
            feature_name="measured_minus_mmt_centered_residual_arcsec",
            feature_group="residual_terms",
            feature_kind="residual_label",
            usage_policy=DIAGNOSTIC_ONLY,
            leakage_risk="high_if_used_at_inference",
            source_boundary="measured TE target minus MMT analytical curve",
            notes="Target-derived residual placeholder; excluded from dry-run inference fields.",
        ),
    ]


def compute_harmonic_summary(rte_arcsec: np.ndarray, harmonic_index_list: list[int]) -> list[dict[str, Any]]:

    """Compute selected harmonic amplitudes and phases for one MMT curve."""

    centered_rte_arcsec = rte_arcsec - float(np.mean(rte_arcsec))
    spectrum = np.fft.rfft(centered_rte_arcsec)
    amplitude = 2.0 * np.abs(spectrum) / centered_rte_arcsec.size
    phase = np.angle(spectrum)
    maximum_harmonic_index = len(amplitude) - 1

    row_list: list[dict[str, Any]] = []
    for harmonic_index in harmonic_index_list:
        safe_index = int(harmonic_index)
        if safe_index > maximum_harmonic_index:
            row_list.append(
                {
                    "harmonic_index": safe_index,
                    "is_available": False,
                    "mmt_harmonic_amplitude_arcsec": "",
                    "mmt_harmonic_phase_rad": "",
                    "usage_policy": INFERENCE_SAFE,
                }
            )
            continue
        if safe_index == 0:
            amplitude_value = abs(float(np.mean(rte_arcsec)))
            phase_value = 0.0
        else:
            amplitude_value = float(amplitude[safe_index])
            phase_value = float(phase[safe_index])
        row_list.append(
            {
                "harmonic_index": safe_index,
                "is_available": True,
                "mmt_harmonic_amplitude_arcsec": format_float(amplitude_value),
                "mmt_harmonic_phase_rad": format_float(phase_value),
                "usage_policy": INFERENCE_SAFE,
            }
        )
    return row_list


def build_sample_rows(angle_rad: np.ndarray, rte_rad: np.ndarray) -> list[dict[str, Any]]:

    """Build point-wise dry-run feature rows from the MMT demonstration curve."""

    angle_rad = np.asarray(angle_rad, dtype=float)
    rte_arcsec = np.asarray(rte_rad, dtype=float) * ARCSECOND_PER_RADIAN
    centered_rte_arcsec = rte_arcsec - float(np.mean(rte_arcsec))
    rte_mean_arcsec = float(np.mean(rte_arcsec))
    rte_peak_to_peak_arcsec = float(np.ptp(rte_arcsec))

    return [
        {
            "sample_index": int(sample_index),
            "angle_rad": format_float(float(angle_value)),
            "mmt_rte_arcsec": format_float(float(rte_arcsec[sample_index])),
            "mmt_centered_rte_arcsec": format_float(float(centered_rte_arcsec[sample_index])),
            "mmt_rte_mean_arcsec": format_float(rte_mean_arcsec),
            "mmt_rte_peak_to_peak_arcsec": format_float(rte_peak_to_peak_arcsec),
            "usage_policy": INFERENCE_SAFE,
        }
        for sample_index, angle_value in enumerate(angle_rad)
    ]


def generate_wave4b_feature_payload(
    sample_count: int = 720,
    harmonic_index_list: list[int] | None = None,
) -> Wave4BFeaturePayload:

    """Generate the Wave 5.2B dry-run schema and sample feature payload."""

    assert sample_count > 8, f"Sample Count must be greater than 8 | {sample_count}"
    selected_harmonic_index_list = harmonic_index_list or list(DEFAULT_HARMONIC_INDEX_LIST)

    adapter = Wave4MMTDiagnosticAdapter()
    angle_rad, rte_rad = adapter.run_demo_curve(sample_count=sample_count)
    rte_arcsec = np.asarray(rte_rad, dtype=float) * ARCSECOND_PER_RADIAN

    schema_row_list = [asdict(specification) for specification in build_feature_schema()]
    sample_row_list = build_sample_rows(angle_rad=angle_rad, rte_rad=rte_rad)
    harmonic_row_list = compute_harmonic_summary(
        rte_arcsec=rte_arcsec,
        harmonic_index_list=selected_harmonic_index_list,
    )
    status_dictionary = {
        "implementation_status": "implementation_ready",
        "campaign_readiness": "not_campaign_ready",
        "sample_count": int(sample_count),
        "schema_feature_count": int(len(schema_row_list)),
        "sample_feature_row_count": int(len(sample_row_list)),
        "harmonic_summary_row_count": int(len(harmonic_row_list)),
        "inference_safe_feature_count": int(
            sum(row["usage_policy"] == INFERENCE_SAFE for row in schema_row_list)
        ),
        "blocked_feature_count": int(
            sum(row["usage_policy"] != INFERENCE_SAFE for row in schema_row_list)
        ),
        "blocker_list": [
            "requires_track2h_quantile_probabilistic_closeout",
            "requires_real_wave4b_campaign_plan",
            "requires_feature_consumer_selection",
        ],
    }

    return Wave4BFeaturePayload(
        schema_row_list=schema_row_list,
        sample_row_list=sample_row_list,
        harmonic_row_list=harmonic_row_list,
        status_dictionary=status_dictionary,
    )


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)
