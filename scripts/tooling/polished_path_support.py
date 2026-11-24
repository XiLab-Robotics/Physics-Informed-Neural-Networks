"""Resolve direction without assuming the canonical polished data root."""
import re
from pathlib import Path


def resolve_polished_direction(csv_file_path: str | Path,
                               dataset_root: str | Path | None = None) -> str:
    """Require a forward/backward child of a canonical or alternate polished root.

    When the caller knows the selected dataset root, use it explicitly. A
    standalone curve reader can instead resolve the unique named ancestor.
    Never silently fall back to the full canonical dataset.
    """
    path = Path(csv_file_path).resolve()
    if dataset_root is None:
        roots = [parent for parent in path.parents if parent.name == "polished_dataset"]
        if len(roots) != 1:
            raise ValueError(f"Expected one polished_dataset ancestor | {path}")
        root = roots[0]
    else:
        root = Path(dataset_root).resolve()
    if root.name != "polished_dataset" or not path.is_relative_to(root):
        raise ValueError(f"CSV outside selected polished_dataset root | {path} | {root}")
    parts = path.relative_to(root).parts
    if len(parts) < 2 or parts[0].lower() not in ("forward", "backward"):
        raise ValueError(f"Polished direction folder must be forward or backward | {path}")
    return parts[0].lower()


FILENAME_PATTERN = re.compile(r"(?P<speed_rpm>[0-9.]+)rpm(?P<torque_nm>[0-9.]+)Nm(?P<temperature_deg>[0-9.]+)deg\.csv$")


def parse_operating_condition_metadata(csv_file_path: str | Path) -> dict[str, float]:

    """ Parse Operating Condition Metadata """

    # Resolve CSV Path
    csv_file_path = Path(csv_file_path).resolve()

    # Parse File Name Metadata
    filename_match = FILENAME_PATTERN.search(csv_file_path.name)
    assert filename_match is not None, f"Unable to parse Operating Conditions from file name | {csv_file_path.name}"

    speed_rpm = float(filename_match.group("speed_rpm"))
    torque_nm = float(filename_match.group("torque_nm"))
    temperature_deg_from_filename = float(filename_match.group("temperature_deg"))

    # Parse Parent Folder Metadata
    normalized_path_text = csv_file_path.as_posix()
    parent_folder_match = re.search(r"Test_(?P<temperature_deg>[0-9.]+)degree", normalized_path_text)
    if parent_folder_match is None:
        parent_folder_match = re.search(r"/(?P<temperature_deg>[0-9.]+)degree/", normalized_path_text)
    assert parent_folder_match is not None, f"Unable to parse Test Temperature from folder path | {csv_file_path}"

    temperature_deg_from_folder = float(parent_folder_match.group("temperature_deg"))

    # Validate Temperature Consistency
    assert temperature_deg_from_filename == temperature_deg_from_folder, (
        f"Temperature mismatch between file name and folder | "
        f"{temperature_deg_from_filename} vs {temperature_deg_from_folder} | {csv_file_path}"
    )

    return {
        "speed_rpm": speed_rpm,
        "torque_nm": torque_nm,
        "oil_temperature_deg": temperature_deg_from_filename,
    }
