"""Plot Track 2 curves from the recovered original paper ONNX forward bank."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Scientific Python Utilities
import numpy as np
import onnxruntime as ort

# Import Project Utilities
from scripts.paper_reimplementation.rcim_ml_compensation.harmonic_wise_comparison import (
    harmonic_wise_support,
)
from scripts.paper_reimplementation.rcim_ml_compensation.reference_family_vs_feedforward import (
    reference_family_vs_feedforward_support,
)
from scripts.training import shared_training_infrastructure

DEFAULT_TRACK2_CONFIG_PATH = (
    PROJECT_PATH
    / "config"
    / "paper_reimplementation"
    / "rcim_ml_compensation"
    / "reference_family_vs_feedforward"
    / "full_track2_matrix_template.yaml"
)
DEFAULT_OUTPUT_ROOT = (
    PROJECT_PATH
    / "output"
    / "validation_checks"
    / "track2_original_onnx_fw_curve_plotter"
)

FULL_ORIGINAL_ONNX_VARIANT_ID = "paper_original_best_Fw_original_onnx_release"
SPARSE_SIMPLIFIED_ONNX_VARIANT_ID = "rcim_original_simplified_onnx_Fw"
SPARSE_PLC_HGBM_ONNX_VARIANT_ID = "rcim_original_plc_hgbm_onnx_Fw"

FULL_ORIGINAL_ONNX_TARGET_CONFIGURATION_LIST = [
    ("amplitude", 0, "SVR", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/SVR/ampl/SVR_ampl0.onnx"),
    ("amplitude", 1, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl1.onnx"),
    ("amplitude", 3, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl3.onnx"),
    ("amplitude", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx"),
    ("amplitude", 40, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl40.onnx"),
    ("amplitude", 78, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl78.onnx"),
    ("amplitude", 81, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl81.onnx"),
    ("amplitude", 156, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl156.onnx"),
    ("amplitude", 162, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl162.onnx"),
    ("amplitude", 240, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl240.onnx"),
    ("phase", 1, "LGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/LGBM/phase/LGBMRegressor_phase1.onnx"),
    ("phase", 3, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase3.onnx"),
    ("phase", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx"),
    ("phase", 40, "GBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/GBM/phase/GradientBoostingRegressor_phase40.onnx"),
    ("phase", 78, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase78.onnx"),
    ("phase", 81, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase81.onnx"),
    ("phase", 156, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/phase/RandomForestRegressor_phase156.onnx"),
    ("phase", 162, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/phase/ExtraTreesRegressor_phase162.onnx"),
    ("phase", 240, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/phase/ExtraTreesRegressor_phase240.onnx"),
]

SPARSE_SELECTED_HARMONIC_LIST = [0, 1, 39, 40]

SPARSE_SIMPLIFIED_ONNX_TARGET_CONFIGURATION_LIST = [
    ("amplitude", 0, "ET", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ET/ampl/ExtraTreeRegressor_ampl0.onnx"),
    ("amplitude", 1, "RF", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/RF/ampl/RandomForestRegressor_ampl1.onnx"),
    ("phase", 1, "LGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/LGBM/phase/LGBMRegressor_phase1.onnx"),
    ("amplitude", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx"),
    ("phase", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx"),
    ("amplitude", 40, "ERT", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/ERT/ampl/ExtraTreesRegressor_ampl40.onnx"),
    ("phase", 40, "GBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/GBM/phase/GradientBoostingRegressor_phase40.onnx"),
]

SPARSE_PLC_HGBM_ONNX_TARGET_CONFIGURATION_LIST = [
    ("amplitude", 0, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl0.onnx"),
    ("amplitude", 1, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl1.onnx"),
    ("phase", 1, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase1.onnx"),
    ("amplitude", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl39.onnx"),
    ("phase", 39, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase39.onnx"),
    ("amplitude", 40, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/ampl/HistGradientBoostingRegressor_ampl40.onnx"),
    ("phase", 40, "HGBM", "reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/HGBM/phase/HistGradientBoostingRegressor_phase40.onnx"),
]

ONNX_TARGET_CONFIGURATION_LIST = FULL_ORIGINAL_ONNX_TARGET_CONFIGURATION_LIST

ONNX_VARIANT_CONFIGURATION_DICTIONARY = {
    FULL_ORIGINAL_ONNX_VARIANT_ID: {
        "candidate_id": FULL_ORIGINAL_ONNX_VARIANT_ID,
        "display_name": "Original ONNX paper best Fw",
        "target_configuration_list": FULL_ORIGINAL_ONNX_TARGET_CONFIGURATION_LIST,
        "selected_harmonic_list": None,
    },
    SPARSE_SIMPLIFIED_ONNX_VARIANT_ID: {
        "candidate_id": SPARSE_SIMPLIFIED_ONNX_VARIANT_ID,
        "display_name": "RCIM original simplified ONNX Fw",
        "target_configuration_list": SPARSE_SIMPLIFIED_ONNX_TARGET_CONFIGURATION_LIST,
        "selected_harmonic_list": SPARSE_SELECTED_HARMONIC_LIST,
    },
    SPARSE_PLC_HGBM_ONNX_VARIANT_ID: {
        "candidate_id": SPARSE_PLC_HGBM_ONNX_VARIANT_ID,
        "display_name": "RCIM original PLC HGBM ONNX Fw",
        "target_configuration_list": SPARSE_PLC_HGBM_ONNX_TARGET_CONFIGURATION_LIST,
        "selected_harmonic_list": SPARSE_SELECTED_HARMONIC_LIST,
    },
}


@dataclass(frozen=True)
class HardcodedOnnxTarget:

    """One hardcoded paper-original ONNX target."""

    target_kind: str
    harmonic_order: int
    family_name: str
    model_path: Path
    session: ort.InferenceSession
    input_name: str


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config-path",
        type=Path,
        default=DEFAULT_TRACK2_CONFIG_PATH,
        help="Track 2 configuration that defines the canonical held-out curve split.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Directory where one PNG is written per plotted curve.",
    )
    parser.add_argument(
        "--variant-id",
        choices=sorted(ONNX_VARIANT_CONFIGURATION_DICTIONARY),
        default=FULL_ORIGINAL_ONNX_VARIANT_ID,
        help="Original ONNX variant to evaluate.",
    )
    parser.add_argument(
        "--max-curves",
        type=int,
        default=None,
        help="Optional maximum number of forward Track 2 curves to plot.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show each matplotlib figure interactively instead of only saving PNG files.",
    )
    return parser.parse_args()


def resolve_onnx_variant_configuration(variant_id: str) -> dict[str, Any]:

    """Resolve one named original-ONNX variant configuration."""

    assert variant_id in ONNX_VARIANT_CONFIGURATION_DICTIONARY, f"Unknown ONNX variant | {variant_id}"
    return ONNX_VARIANT_CONFIGURATION_DICTIONARY[variant_id]


def load_hardcoded_onnx_target_list(
    target_configuration_list: Sequence[tuple[str, int, str, str]] | None = None,
) -> list[HardcodedOnnxTarget]:

    """Load one hardcoded original paper forward ONNX target list."""

    if target_configuration_list is None:
        target_configuration_list = ONNX_TARGET_CONFIGURATION_LIST

    target_list: list[HardcodedOnnxTarget] = []
    for target_kind, harmonic_order, family_name, path_text in target_configuration_list:
        model_path = PROJECT_PATH / path_text
        assert model_path.exists(), f"Missing hardcoded ONNX target | {model_path}"
        session = ort.InferenceSession(str(model_path), providers=["CPUExecutionProvider"])
        target_list.append(
            HardcodedOnnxTarget(
                target_kind=target_kind,
                harmonic_order=int(harmonic_order),
                family_name=family_name,
                model_path=model_path,
                session=session,
                input_name=session.get_inputs()[0].name,
            )
        )

    return target_list


def build_forward_track2_curve_record_list(
    config_path: Path,
) -> tuple[list[harmonic_wise_support.HarmonicCurveRecord], list[int], str]:

    """Build the canonical forward Track 2 curve records."""

    training_config = reference_family_vs_feedforward_support.load_reference_family_comparison_config(config_path)
    selected_harmonic_list = [
        int(harmonic_order)
        for harmonic_order in training_config["evaluation"]["selected_harmonics"]
    ]
    curve_record_list, _, _, _ = reference_family_vs_feedforward_support.build_curve_record_list(
        training_config,
        selected_harmonic_list,
    )
    forward_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() == "forward"
    ]
    percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])
    return forward_curve_record_list, selected_harmonic_list, percentage_error_denominator


def predict_curve_target_dictionary(
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    target_list: list[HardcodedOnnxTarget],
) -> dict[tuple[str, int], float]:

    """Predict the 19 harmonic targets for one curve operating point."""

    feature_matrix = np.asarray(
        [[float(curve_record.speed_rpm), float(curve_record.oil_temperature_deg), float(curve_record.torque_nm)]],
        dtype=np.float32,
    )
    prediction_dictionary: dict[tuple[str, int], float] = {}
    for target in target_list:
        prediction_array = target.session.run(None, {target.input_name: feature_matrix})[0]
        prediction_dictionary[(target.target_kind, target.harmonic_order)] = float(
            np.asarray(prediction_array, dtype=np.float64).reshape(-1)[0]
        )
    return prediction_dictionary


def reconstruct_curve_from_prediction_dictionary(
    angular_position_deg: np.ndarray,
    selected_harmonic_list: list[int],
    prediction_dictionary: dict[tuple[str, int], float],
) -> np.ndarray:

    """Reconstruct one TE curve from amplitude and phase predictions."""

    coefficient_dictionary: dict[str, float] = {}
    for harmonic_order in selected_harmonic_list:
        predicted_amplitude = float(prediction_dictionary[("amplitude", int(harmonic_order))])
        if int(harmonic_order) == 0:
            coefficient_dictionary["coefficient_cos_h0"] = predicted_amplitude
            continue
        predicted_phase = float(prediction_dictionary[("phase", int(harmonic_order))])
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(
            predicted_amplitude * np.cos(predicted_phase)
        )
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(
            -predicted_amplitude * np.sin(predicted_phase)
        )

    return harmonic_wise_support.reconstruct_curve_from_coefficients(
        angular_position_deg,
        selected_harmonic_list,
        coefficient_dictionary,
    )


def save_or_show_curve_plot(
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
    predicted_curve_deg: np.ndarray,
    metric_dictionary: dict[str, float],
    plot_path: Path,
    show_plot: bool,
) -> None:

    """Save or show one measured-versus-predicted curve plot."""

    import matplotlib

    if not show_plot:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plot_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10.0, 5.0))
    axis.plot(curve_record.angular_position_deg, curve_record.transmission_error_deg, label="Measured TE", linewidth=1.2, color="#4a4a4a")
    axis.plot(curve_record.angular_position_deg, predicted_curve_deg, label="Original ONNX paper best Fw", linewidth=1.2, color="#1f77b4")
    axis.set_title(
        (
            f"Forward | {float(curve_record.speed_rpm):.0f} rpm | "
            f"{float(curve_record.torque_nm):.0f} Nm | "
            f"{float(curve_record.oil_temperature_deg):.0f} C | "
            f"MAE {float(metric_dictionary['mae']):.6f} deg"
        ),
        fontsize=10,
    )
    axis.set_xlabel("Angular Position [deg]")
    axis.set_ylabel("Transmission Error [deg]")
    axis.grid(True, alpha=0.28)
    axis.legend(loc="best", fontsize=8)
    figure.tight_layout()
    figure.savefig(plot_path, dpi=180)
    if show_plot:
        plt.show()
    plt.close(figure)


def run_plotter(arguments: argparse.Namespace) -> dict[str, Any]:

    """Run the hardcoded original-ONNX curve plotter."""

    variant_configuration = resolve_onnx_variant_configuration(str(arguments.variant_id))
    output_root = (
        shared_training_infrastructure.resolve_runtime_project_relative_path(arguments.output_root)
        / str(variant_configuration["candidate_id"])
    )
    target_list = load_hardcoded_onnx_target_list(
        variant_configuration["target_configuration_list"]
    )
    curve_record_list, selected_harmonic_list, percentage_error_denominator = build_forward_track2_curve_record_list(
        arguments.config_path
    )
    if variant_configuration["selected_harmonic_list"] is not None:
        selected_harmonic_list = [
            int(harmonic_order)
            for harmonic_order in variant_configuration["selected_harmonic_list"]
        ]
    if arguments.max_curves is not None:
        curve_record_list = curve_record_list[: int(arguments.max_curves)]

    plot_entry_list: list[dict[str, Any]] = []
    for curve_index, curve_record in enumerate(curve_record_list):
        prediction_dictionary = predict_curve_target_dictionary(curve_record, target_list)
        predicted_curve_deg = reconstruct_curve_from_prediction_dictionary(
            curve_record.angular_position_deg,
            selected_harmonic_list,
            prediction_dictionary,
        )
        metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
            curve_record.transmission_error_deg,
            predicted_curve_deg,
            percentage_error_denominator,
        )
        plot_path = output_root / "plots" / f"curve_{curve_index:03d}.png"
        save_or_show_curve_plot(
            curve_record,
            predicted_curve_deg,
            metric_dictionary,
            plot_path,
            bool(arguments.show),
        )
        plot_entry_list.append(
            {
                "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
                "plot_path": shared_training_infrastructure.format_project_relative_path(plot_path),
                "mae": float(metric_dictionary["mae"]),
                "rmse": float(metric_dictionary["rmse"]),
                "mean_percentage_error_pct": float(metric_dictionary["mean_percentage_error_pct"]),
            }
        )

    return {
        "candidate_id": str(variant_configuration["candidate_id"]),
        "curve_count": len(plot_entry_list),
        "target_count": len(target_list),
        "selected_harmonic_list": selected_harmonic_list,
        "plot_entry_list": plot_entry_list,
    }


def main() -> None:

    """Run the command-line entry point."""

    summary_dictionary = run_plotter(parse_command_line_arguments())
    print(
        "[DONE] Original ONNX paper-best forward plots | "
        f"candidate={summary_dictionary['candidate_id']} "
        f"curves={summary_dictionary['curve_count']} "
        f"targets={summary_dictionary['target_count']}"
    )


if __name__ == "__main__":
    main()
