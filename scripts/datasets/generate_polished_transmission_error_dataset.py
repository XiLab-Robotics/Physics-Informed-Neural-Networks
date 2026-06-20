from pathlib import Path
import csv
import math
import re
import warnings


# Repository Paths
SCRIPT_PATH = Path(__file__).resolve().parent
PROJECT_PATH = SCRIPT_PATH.parents[1]
INPUT_PATH = PROJECT_PATH / "data" / "original_dataset"
OUTPUT_PATH = PROJECT_PATH / "output" / "generated_polished_dataset"

GEAR_RATIO = 81.0
SAMPLE_TIME_S = 0.25e-3
USE_FORWARD_DIRECTION = True
USE_BACKWARD_DIRECTION = True
OVERWRITE_EXISTING_FILES = False

THETA_ENC_DEG = 1
Q_ENC_DEG = 2
TAU_LOAD_NM = 3
VALID_FW = 4
VALID_BW = 5
TEMP_DEG_C = 7
Q_ABS_DEG = 10

FILENAME_PATTERN = re.compile(
    r"^(?P<speed_rpm>[-+]?\d+(?:\.\d+)?)"
    r"rpm(?P<torque_nm>[-+]?\d+(?:\.\d+)?)"
    r"Nm(?P<temperature_deg>[-+]?\d+(?:\.\d+)?)"
    r"deg(?:_\d+)?\.csv$"
)

IGNORED_INPUT_FILENAMES = {
    "200.0rpm0.0Nm25.0deg1.csv",
    "200.0rpm100.0Nm25.0deg1.csv",
    "1100.0rpm100.0Nm30.0deg_collegamento.csv",
    "1600.0rpm100.0Nm30.0degCollegamiento.csv",
    "1600.0rpm100.0Nm30.0degcollegamento2.csv",
    "800.0rpm200.0Nm25.0deg.csv",
}


def number(text):
    text = text.strip()
    if "," in text and "." not in text:
        text = text.replace(",", ".")
    return float(text)


def average(values):
    return sum(values) / len(values)


def matlab_row_number(value):
    return f"{value:.17g}"


def filename_number(value):
    return f"{value:.1f}"


def folder_number(value):
    if float(value).is_integer():
        return str(int(value))
    return f"{value:g}"


def path_sort_key(path):
    return str(path.resolve()).lower()


def parse_operating_conditions(path):
    match = FILENAME_PATTERN.match(path.name)
    if match is None:
        raise ValueError(f"could not parse speed/torque/temperature from file name: {path.name}")

    return {
        "speed_rpm": float(match.group("speed_rpm")),
        "torque_nm": float(match.group("torque_nm")),
        "temperature_deg": float(match.group("temperature_deg")),
    }


def condition_key(conditions):
    return (
        conditions["speed_rpm"],
        conditions["torque_nm"],
        conditions["temperature_deg"],
    )


def output_folder(output_path, direction, conditions):
    return (
        output_path
        / direction
        / f"{folder_number(conditions['temperature_deg'])}degree"
        / f"{folder_number(conditions['speed_rpm'])}rpm"
    )


def output_filename(conditions):
    return (
        f"{filename_number(conditions['speed_rpm'])}rpm"
        f"{filename_number(conditions['torque_nm'])}Nm"
        f"{filename_number(conditions['temperature_deg'])}deg.csv"
    )


def delimiter_from_first_line(first_line):
    if ";" in first_line:
        return ";"
    if "," in first_line:
        return ","
    raise ValueError("could not detect CSV delimiter")


def read_measurement(path):
    data = {
        "theta_enc_deg": [],
        "q_enc_deg": [],
        "tau_load_nm": [],
        "valid_fw": [],
        "valid_bw": [],
        "temp_deg_c": [],
        "q_abs_deg": [],
    }

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        first_line = handle.readline()
        delimiter = delimiter_from_first_line(first_line)
        handle.seek(0)

        for row in csv.reader(handle, delimiter=delimiter):
            if len(row) < 11:
                continue
            try:
                parsed_row = {
                    "theta_enc_deg": number(row[THETA_ENC_DEG]),
                    "q_enc_deg": number(row[Q_ENC_DEG]),
                    "tau_load_nm": number(row[TAU_LOAD_NM]),
                    "valid_fw": number(row[VALID_FW]),
                    "valid_bw": number(row[VALID_BW]),
                    "temp_deg_c": number(row[TEMP_DEG_C]),
                    "q_abs_deg": number(row[Q_ABS_DEG]),
                }
            except ValueError:
                continue

            # Append only complete numeric rows to keep every signal aligned.
            for column_name, column_value in parsed_row.items():
                data[column_name].append(column_value)

    if len(data["theta_enc_deg"]) < 3:
        raise ValueError("not enough numeric rows")

    return data


def zeroing_offset_rad(data):
    raw_offset_rad = math.radians(average(data["q_abs_deg"][:3]) - average(data["q_enc_deg"][:3]))
    q_zeroing_offset = math.atan2(math.sin(raw_offset_rad), math.cos(raw_offset_rad))

    if q_zeroing_offset < -0.002:
        q_zeroing_offset += 0.0044
    elif q_zeroing_offset > 0.002:
        q_zeroing_offset -= 0.00415

    return q_zeroing_offset


def rewrap(angle_rad):
    return angle_rad % (2.0 * math.pi)


def valid_indices(flags):
    return [index for index, flag in enumerate(flags) if flag != 0.0]


def export_direction(data, indices, output_path, direction, conditions):
    if len(indices) < 2:
        return False

    q_offset_rad = zeroing_offset_rad(data)

    theta_rad = [math.radians(data["theta_enc_deg"][index]) / GEAR_RATIO for index in indices]
    q_rad = [math.radians(data["q_enc_deg"][index]) for index in indices]
    q_not_zeroed_rad = [q_value + q_offset_rad for q_value in q_rad]
    theta_te_rad = [
        q_not_zeroed_value - theta_value
        for q_not_zeroed_value, theta_value in zip(q_not_zeroed_rad, theta_rad)
    ]

    tau_load = [data["tau_load_nm"][index] for index in indices]
    temperature = [data["temp_deg_c"][index] for index in indices]

    dtheta_rad_s = [(theta_rad[1] - theta_rad[0]) / SAMPLE_TIME_S]
    dtheta_rad_s.extend(
        (theta_rad[index] - theta_rad[index - 1]) / SAMPLE_TIME_S
        for index in range(1, len(theta_rad))
    )
    theta_dot_rpm = [math.degrees(value) / 6.0 * GEAR_RATIO for value in dtheta_rad_s]

    theta_deg = [math.degrees(rewrap(value)) for value in theta_rad]
    theta_te_deg = [math.degrees(value) for value in theta_te_rad]

    direction_output_path = output_folder(output_path, direction, conditions)
    direction_output_path.mkdir(parents=True, exist_ok=True)
    output_file = direction_output_path / output_filename(conditions)

    if output_file.exists() and not OVERWRITE_EXISTING_FILES:
        raise FileExistsError(
            f"output file already exists: {output_file}. "
            "Set OVERWRITE_EXISTING_FILES = True to replace existing files."
        )

    with output_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["theta", "theta_dot", "tau_load", "T", "theta_TE"])
        writer.writerows(
            [
                matlab_row_number(theta_value),
                matlab_row_number(theta_dot_value),
                matlab_row_number(tau_load_value),
                matlab_row_number(temperature_value),
                matlab_row_number(theta_te_value),
            ]
            for theta_value, theta_dot_value, tau_load_value, temperature_value, theta_te_value
            in zip(theta_deg, theta_dot_rpm, tau_load, temperature, theta_te_deg)
        )

    return True


def is_inside(path, folder):
    try:
        path.resolve().relative_to(folder.resolve())
        return True
    except ValueError:
        return False


def is_generated_csv(path, input_path, output_path):
    if is_inside(path, output_path):
        return True

    if input_path.is_file():
        return False

    try:
        folder_names = path.relative_to(input_path).parts[:-1]
    except ValueError:
        folder_names = path.parts[:-1]

    return any(is_generated_folder(name) for name in folder_names)


def is_generated_folder(name):
    name = name.lower()
    return name in {"processed", "csv", "csv_python", "generated_polished_dataset"}


def input_files(search_path, output_path):
    if search_path.is_file():
        yield search_path
        return

    for path in search_path.rglob("*.csv"):
        if not is_generated_csv(path, search_path, output_path):
            yield path


def input_file_records(paths):
    records = []
    skipped = 0

    for path in sorted(set(paths), key=path_sort_key):
        if path.name in IGNORED_INPUT_FILENAMES:
            continue

        try:
            conditions = parse_operating_conditions(path)
        except ValueError as error:
            skipped += 1
            print(f"Skipped {path}: {error}")
            continue

        records.append((path, conditions))

    return records, skipped


def unique_condition_records(records):
    records_by_condition = {}
    for path, conditions in records:
        records_by_condition.setdefault(condition_key(conditions), []).append((path, conditions))

    selected_records = []
    for key in sorted(records_by_condition):
        condition_records = records_by_condition[key]
        selected_records.append(condition_records[0])

        if len(condition_records) > 1:
            paths = "\n".join(f"  - {path}" for path, _ in condition_records)
            speed_rpm, torque_nm, temperature_deg = key
            warnings.warn(
                "Duplicate source files with the same conditions "
                f"({filename_number(speed_rpm)}rpm, "
                f"{filename_number(torque_nm)}Nm, "
                f"{filename_number(temperature_deg)}deg). "
                "Keeping the first sorted source file and skipping the rest:\n"
                f"{paths}",
                RuntimeWarning,
                stacklevel=2,
            )

    return selected_records


def export_file(path, output_path, conditions):
    data = read_measurement(path)
    count = 0
    if USE_BACKWARD_DIRECTION and export_direction(
        data,
        valid_indices(data["valid_bw"]),
        output_path,
        "backward",
        conditions,
    ):
        count += 1
    if USE_FORWARD_DIRECTION and export_direction(
        data,
        valid_indices(data["valid_fw"]),
        output_path,
        "forward",
        conditions,
    ):
        count += 1
    return count


def main():
    input_path = Path(INPUT_PATH)
    output_path = Path(OUTPUT_PATH)

    if not input_path.exists():
        raise FileNotFoundError(f"input path does not exist: {input_path}")
    if not input_path.is_file() and not input_path.is_dir():
        raise ValueError(f"input path must be a CSV file or directory: {input_path}")
    if input_path.is_file() and input_path.suffix.lower() != ".csv":
        raise ValueError(f"input file must have a .csv extension: {input_path}")
    if output_path.exists() and not output_path.is_dir():
        raise ValueError(f"output path exists but is not a directory: {output_path}")
    if input_path.resolve() == output_path.resolve():
        raise ValueError("input and output paths must be different")

    output_path.mkdir(parents=True, exist_ok=True)

    exported = 0
    records, skipped = input_file_records(input_files(input_path, output_path))
    if not records:
        raise ValueError(f"no supported input CSV files found: {input_path}")

    selected_records = unique_condition_records(records)

    if not OVERWRITE_EXISTING_FILES:
        enabled_directions = []
        if USE_BACKWARD_DIRECTION:
            enabled_directions.append("backward")
        if USE_FORWARD_DIRECTION:
            enabled_directions.append("forward")

        existing_output_files = [
            output_folder(output_path, direction, conditions) / output_filename(conditions)
            for _, conditions in selected_records
            for direction in enabled_directions
            if (output_folder(output_path, direction, conditions) / output_filename(conditions)).exists()
        ]
        if existing_output_files:
            preview = "\n".join(f"  - {path}" for path in existing_output_files[:10])
            raise FileExistsError(
                "output files already exist; no files were written. "
                "Set OVERWRITE_EXISTING_FILES = True to replace them:\n"
                f"{preview}"
            )

    for path, conditions in selected_records:
        try:
            exported += export_file(path, output_path, conditions)
        except Exception as error:
            skipped += 1
            print(f"Skipped {path}: {error}")

    print(f"Exported {exported} files to {output_path}")
    if skipped:
        raise RuntimeError(f"skipped {skipped} input files; review the messages above")


if __name__ == "__main__":
    main()
