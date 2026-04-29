"""Direct entrypoint for the recovered original RCIM evaluation stage."""

import argparse
import json
import os
import shutil
import sys
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm


SCRIPT_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = SCRIPT_ROOT.parents[3]
UTILITIES_ROOT = SCRIPT_ROOT / "utilities"
REFERENCE_ROOT = REPOSITORY_ROOT / "reference" / "rcim_ml_compensation_recovered_assets" / "code" / "original_pipeline"
DEFAULT_VALIDATION_ROOT = REPOSITORY_ROOT / "output" / "validation_checks" / "paper_reimplementation_rcim_recovered_original_workflow"


def _ensure_utilities_on_path():
    """Expose the copied original utility modules to Python imports."""
    if str(UTILITIES_ROOT) not in sys.path:
        sys.path.insert(0, str(UTILITIES_ROOT))


def _normalize_direction(direction):
    """Map CLI direction aliases to the original RCIM suffixes."""
    normalized_direction = direction.strip().lower()
    if normalized_direction in {"fw", "forward"}:
        return "Fw", "forward"
    if normalized_direction in {"bw", "backward"}:
        return "Bw", "backward"
    raise ValueError(f"Unsupported direction: {direction}")


def _build_default_output_root(direction_label, output_suffix):
    """Create the default repository-owned runtime root for this stage."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    suffix = f"_{output_suffix}" if output_suffix else ""
    return DEFAULT_VALIDATION_ROOT / f"{timestamp}__evaluate_{direction_label}{suffix}"


def _write_summary(summary_path, payload):
    """Persist a minimal JSON summary for reproducibility."""
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


@contextmanager
def _pushd(target_directory_path):
    """Temporarily change the working directory."""
    original_directory = Path.cwd()
    os.chdir(target_directory_path)
    try:
        yield
    finally:
        os.chdir(original_directory)


def _copy_directory_contents(source_directory_path, destination_directory_path):
    """Copy the source directory contents into the destination directory."""
    destination_directory_path.mkdir(parents=True, exist_ok=True)
    for child_path in source_directory_path.iterdir():
        target_path = destination_directory_path / child_path.name
        if child_path.is_dir():
            shutil.copytree(child_path, target_path, dirs_exist_ok=True)
        else:
            shutil.copy2(child_path, target_path)


def _prepare_runtime_instances_input(source_directory_path, runtime_cache_directory_path):
    """Prepare the instance directory expected by the original Statistics helper."""
    source_file_list = list(source_directory_path.iterdir())
    if any(file_path.suffix.lower() == ".pickle" for file_path in source_file_list):
        _copy_directory_contents(source_directory_path, runtime_cache_directory_path)
        return runtime_cache_directory_path
    return source_directory_path


def _build_argument_parser():
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--direction",
        default="forward",
        help="Direction to evaluate: forward/Fw or backward/Bw.",
    )
    parser.add_argument(
        "--instances-path",
        type=Path,
        default=REFERENCE_ROOT / "instances_V3",
        help="Directory containing original RCIM instance CSVs or pickles.",
    )
    parser.add_argument(
        "--prediction-directory",
        type=Path,
        default=REFERENCE_ROOT / "output_prediction" / "instV3.8_Fw_allFreq_def",
        help="Directory containing prediction CSVs to evaluate.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help="Repository-owned runtime root. Defaults under output/validation_checks/.",
    )
    parser.add_argument(
        "--output-suffix",
        default="",
        help="Optional suffix appended to the default runtime root name.",
    )
    return parser


ACRONYMS = {
    "DecisionTreeRegressor": "DT",
    "ExtraTreeRegressor": "ET",
    "ExtraTreesRegressor": "ETs",
    "RandomForestRegressor": "RF",
    "GradientBoostingRegressor": "GBM",
    "HistGradientBoostingRegressor": "HGBM",
    "XGBRegressor": "XGBM",
    "LGBMRegressor": "LGBM",
    "SVR": "SVM",
    "MLPRegressor": "MLP",
    "MinimumDistance": "MinDist",
}


def extract_values(inst):
    """Original helper kept verbatim in behavior."""
    rpm = inst.rpm
    torque = inst.tor
    deg = inst.deg
    return rpm, torque, deg


def get_acronym_method(file_name):
    """Original helper kept verbatim in behavior."""
    method = ""
    for element in ACRONYMS.keys():
        if element in file_name:
            method = ACRONYMS[element]
    return method


def custom_sort(main_list, order_list):
    """Original helper kept verbatim in behavior."""
    order_dict = {val: idx for idx, val in enumerate(order_list)}

    def custom_compare(item):
        return [order_dict.get(part, float("inf")) for part in item.split("_")]

    main_list.sort(key=custom_compare)


def convert_to_scientific_notation(number):
    """Original helper kept verbatim in behavior."""
    return "{:.1e}".format(number)


def export_table_for_paper(dataframe, error, ampl_phase, output_file):
    """Original helper kept verbatim in behavior."""
    dataframe_columns = [column_name for column_name in dataframe.columns if (error in column_name) and (ampl_phase in column_name)]
    dataframe_data = dataframe[dataframe_columns]
    dataframe_data = dataframe_data.applymap(convert_to_scientific_notation)
    dataframe_data["method"] = dataframe["method"]
    new_order_columns = dataframe_data.columns[-1:].to_list() + dataframe_data.columns[:-2].to_list()
    dataframe_data = dataframe_data[new_order_columns]
    dataframe_data.to_csv(output_file + "_" + error + "_" + ampl_phase + ".csv", sep="\t", index=False)


def main():
    """Run the recovered original evaluation stage with repository-owned path handling."""
    parser = _build_argument_parser()
    args = parser.parse_args()

    _ensure_utilities_on_path()
    from statistics import Statistics  # pylint: disable=import-outside-toplevel

    direction_code, direction_label = _normalize_direction(args.direction)
    if direction_code != "Fw":
        raise ValueError("The shipped recovered evaluation script is forward-shaped only at the moment.")

    output_root = args.output_root or _build_default_output_root(direction_label, args.output_suffix)
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    runtime_instances_directory_path = output_root / "instances_V3"
    runtime_instances_directory_path.mkdir(exist_ok=True)
    runtime_instances_input_path = _prepare_runtime_instances_input(args.instances_path.resolve(), runtime_instances_directory_path)

    runtime_prediction_directory_path = output_root / "output_prediction" / "instV3.8_Fw_allFreq_def"
    _copy_directory_contents(args.prediction_directory.resolve(), runtime_prediction_directory_path)

    evaluation_details_directory_path = output_root / "evaluation" / "V3.9" / "details"
    evaluation_details_directory_path.mkdir(parents=True, exist_ok=True)

    with _pushd(output_root):
        statistics = Statistics()
        input_path = "output_prediction/instV3.8_Fw_allFreq_def/"
        file_list = os.listdir(input_path)
        file_list = [input_path + file_name for file_name in file_list if os.path.isfile(input_path + file_name) and file_name[0] != "."]
        custom_sort(file_list, list(ACRONYMS.keys()))

        statistics.read_all_fft(str(runtime_instances_input_path))
        errors_summary = {"method": [], "mode": [], "MSE": [], "RMSE": [], "MAE": [], "MAPE": []}
        output_summary_file_path = None

        for prediction_file_path in file_list:
            error_total = {
                "instance": [],
                "rpm": [],
                "tor": [],
                "deg": [],
                "method": [],
                "mode": [],
                "MSE": [],
                "RMSE": [],
                "MAE": [],
                "MAPE": [],
            }
            errors_component = {
                "method": [],
                "mode": [],
                "ampl_phase": [],
                "freq": [],
                "MSE": [],
                "RMSE": [],
                "MAE": [],
                "MAPE": [],
            }
            data = pd.DataFrame()
            method = get_acronym_method(prediction_file_path)

            for inst in tqdm(statistics.instances):
                rpm, torque, deg = extract_values(inst)
                mode = "fft"
                mse, rmse, mae, mape, data, skip = inst.predicted_TE_Fw_noShow(prediction_file_path, mode, data)
                if skip is True:
                    continue
                error_total["rpm"].append(rpm)
                error_total["tor"].append(torque)
                error_total["deg"].append(deg)
                error_total["instance"].append(inst.name)
                error_total["method"].append(method)
                error_total["mode"].append(mode)
                error_total["MSE"].append(round(mse, 5))
                error_total["RMSE"].append(round(rmse, 5))
                error_total["MAE"].append(round(mae, 5))
                error_total["MAPE"].append(round(mape, 2))

                column_to_predict = [column_name for column_name in data.columns if "ampl" in column_name or "phase" in column_name]
                for element in column_to_predict:
                    mse, rmse, mae, mape, data, skip = inst.predicted_TE_Fw_noShow_component(prediction_file_path, mode, data, element)
                    errors_component["method"].append(method)
                    errors_component["mode"].append(mode)
                    errors_component["MSE"].append(mse)
                    errors_component["RMSE"].append(rmse)
                    errors_component["MAE"].append(mae)
                    errors_component["MAPE"].append(mape)
                    errors_component["ampl_phase"].append(element.split("_")[-2])
                    errors_component["freq"].append(element.split("_")[-1])

            if not error_total["method"]:
                print(f"Skipping {prediction_file_path} because no matching instances were evaluated.")
                continue

            column_to_predict = [column_name for column_name in data.columns if "ampl" in column_name or "phase" in column_name]
            dataframe_component = pd.DataFrame(errors_component)
            for element in column_to_predict:
                dataframe_mean = dataframe_component[
                    (dataframe_component["ampl_phase"] == element.split("_")[-2])
                    & (dataframe_component["freq"] == element.split("_")[-1])
                ]
                for error_name in ["MSE", "RMSE", "MAE", "MAPE"]:
                    component_key = element.split("_")[-2] + "_" + element.split("_")[-1] + "_" + error_name
                    if component_key not in errors_summary:
                        errors_summary[component_key] = []
                    errors_summary[component_key].append(float(np.mean(dataframe_mean[error_name])))

            pd.DataFrame(error_total).to_csv(
                "evaluation/V3.9/details/dfOutTot_evaluation_details_V12_" + str(Path(prediction_file_path).name) + ".csv",
                sep=";",
                decimal=",",
            )
            errors_summary["method"].append(error_total["method"][0])
            errors_summary["mode"].append("fft")
            errors_summary["MSE"].append(float(np.mean(error_total["MSE"])))
            errors_summary["RMSE"].append(float(np.mean(error_total["RMSE"])))
            errors_summary["MAE"].append(float(np.mean(error_total["MAE"])))
            errors_summary["MAPE"].append(float(np.mean(error_total["MAPE"])))

            final_output = pd.DataFrame(errors_summary)
            output_summary_file_path = "evaluation/V3.9/dfOutTot_evaluation_V12" + str(Path(prediction_file_path).name) + ".csv"
            if os.path.isfile(output_summary_file_path):
                existing_dataframe = pd.read_csv(output_summary_file_path, sep=";", decimal=",")
                final_output = pd.concat([existing_dataframe, final_output])
            final_output.to_csv(output_summary_file_path, sep=";", decimal=",", index=False)

            if prediction_file_path == file_list[-1]:
                for error in ["_MSE", "_RMSE", "_MAE", "_MAPE"]:
                    for ampl_phase in ["ampl", "phase"]:
                        export_table_for_paper(final_output, error, ampl_phase, "evaluation/V3.9/")

        if output_summary_file_path is None:
            raise ValueError("No evaluation rows were produced. Check that the prediction CSVs match the supplied instances.")

    _write_summary(
        output_root / "run_summary.json",
        {
            "stage": "evaluate_models",
            "direction": direction_label,
            "instances_path": str(args.instances_path.resolve()),
            "runtime_instances_input_path": str(runtime_instances_input_path),
            "prediction_directory": str(args.prediction_directory.resolve()),
            "runtime_prediction_directory_path": str(runtime_prediction_directory_path),
            "evaluation_root": str(output_root / "evaluation"),
            "output_summary_file_path": output_summary_file_path,
        },
    )
    print(output_root)


if __name__ == "__main__":
    main()
