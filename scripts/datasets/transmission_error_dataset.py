from __future__ import annotations

# Import Python Utilities
import random
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

# Import Scientific Python Utilities
import numpy as np
import pandas as pd
import yaml

# Import PyTorch Utilities
import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset


PACKAGE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = PACKAGE_PATH.parents[1]
DEFAULT_CONFIG_PATH = PROJECT_PATH / "config" / "dataset_processing.yaml"
DEFAULT_DATASET_PATH = PROJECT_PATH / "data" / "datasets"
REDUCTION_RATIO = 81.0

FORWARD_DIRECTION = "forward"
BACKWARD_DIRECTION = "backward"

FORWARD_DIRECTION_FLAG = 1.0
BACKWARD_DIRECTION_FLAG = -1.0

FILENAME_PATTERN = re.compile(
    r"(?P<speed_rpm>[0-9.]+)rpm(?P<torque_nm>[0-9.]+)Nm(?P<temperature_deg>[0-9.]+)deg\.csv$"
)

FORWARD_POSITION_COLUMN_CANDIDATES = [
    "Poisition_Output_Reducer_Fw",
    "Position_Output_Reducer_Fw",
]

VALIDATED_COLUMN_MAP = {
    "Transmission_Error_Fw": "transmission_error_fw_deg",
    "Position_Output_Reducer_Bw": "position_output_reducer_bw_deg",
    "Transmission_Error_Bw": "transmission_error_bw_deg",
}


@dataclass(frozen=True)
class TransmissionErrorCurveSample:
    """ Transmission Error Curve Sample """

    source_file_path: Path
    direction_label: str
    direction_flag: float
    speed_rpm: float
    torque_nm: float
    oil_temperature_deg: float
    angular_position_deg: np.ndarray
    transmission_error_deg: np.ndarray


def resolve_project_relative_path(path_value: str | Path) -> Path:
    """ Resolve Project Relative Path """

    # Convert To Path
    resolved_path = Path(path_value)

    # Resolve Absolute Path
    if resolved_path.is_absolute():
        return resolved_path.resolve()

    # Resolve Project Relative Path
    return (PROJECT_PATH / resolved_path).resolve()


def load_dataset_processing_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """ Load Dataset Processing Config """

    # Resolve Config Path
    resolved_config_path = resolve_project_relative_path(config_path)

    # Validate Config Path
    assert resolved_config_path.exists(), f"Dataset Config Path does not exist | {resolved_config_path}"

    # Load YAML Configuration
    with resolved_config_path.open("r", encoding="utf-8") as config_file:
        dataset_processing_config = yaml.safe_load(config_file)

    # Validate Configuration
    assert isinstance(dataset_processing_config, dict), "Dataset Processing Config must be a dictionary"

    return dataset_processing_config


def resolve_dataset_root_from_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> Path:
    """ Resolve Dataset Root From Config """

    # Load Configuration
    dataset_processing_config = load_dataset_processing_config(config_path=config_path)

    # Resolve Dataset Root
    dataset_root = resolve_project_relative_path(dataset_processing_config["paths"]["dataset_root"])

    return dataset_root


def collect_dataset_csv_paths(dataset_root: str | Path = DEFAULT_DATASET_PATH) -> list[Path]:
    """ Collect Dataset CSV Paths """

    # Resolve Dataset Root
    dataset_root_path = Path(dataset_root).resolve()

    # Validate Dataset Root
    assert dataset_root_path.exists(), f"Dataset Root Path does not exist | {dataset_root_path}"

    # Collect CSV Paths
    csv_file_paths = sorted(dataset_root_path.rglob("*.csv"))

    # Validate CSV Collection
    assert len(csv_file_paths) > 0, f"No CSV files found inside Dataset Root | {dataset_root_path}"

    return csv_file_paths


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
    parent_folder_match = re.search(r"Test_(?P<temperature_deg>[0-9.]+)degree", csv_file_path.as_posix())
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


@lru_cache(maxsize=32)
def load_validated_te_dataframe(csv_file_path: str) -> pd.DataFrame:
    """ Load Validated TE Dataframe """

    # Load CSV File
    validated_dataframe = pd.read_csv(csv_file_path)

    # Resolve Forward Position Column
    forward_position_column = None
    for candidate_column in FORWARD_POSITION_COLUMN_CANDIDATES:
        if candidate_column in validated_dataframe.columns:
            forward_position_column = candidate_column
            break

    assert forward_position_column is not None, (
        f"Forward Position column not found | Expected one of: {FORWARD_POSITION_COLUMN_CANDIDATES} | "
        f"Given: {validated_dataframe.columns.tolist()}"
    )

    # Validate Remaining Columns
    csv_columns = set(validated_dataframe.columns.tolist())
    expected_columns = set(VALIDATED_COLUMN_MAP.keys()) | {forward_position_column}
    assert csv_columns == expected_columns, (
        f"Unexpected CSV columns detected | Expected: {sorted(expected_columns)} | Given: {sorted(csv_columns)}"
    )

    # Normalize Column Names
    validated_dataframe = validated_dataframe.rename(
        columns={
            forward_position_column: "position_output_reducer_fw_deg",
            **VALIDATED_COLUMN_MAP,
        }
    )

    return validated_dataframe


def compute_transmission_error(
    theta_input_deg: np.ndarray,
    theta_output_deg: np.ndarray,
    reduction_ratio: float = REDUCTION_RATIO,
) -> np.ndarray:
    """ Compute Transmission Error """

    # Convert Arrays To Numpy
    theta_input_deg = np.asarray(theta_input_deg, dtype=np.float64)
    theta_output_deg = np.asarray(theta_output_deg, dtype=np.float64)

    # Validate Input Shape
    assert theta_input_deg.shape == theta_output_deg.shape, (
        f"Theta Input and Theta Output shape mismatch | {theta_input_deg.shape} vs {theta_output_deg.shape}"
    )

    # Compute Transmission Error
    transmission_error_deg = theta_output_deg - reduction_ratio * theta_input_deg

    return transmission_error_deg


def extract_valid_rotation_window(
    output_position_deg: np.ndarray,
    data_valid_flag: np.ndarray,
    minimum_position_deg: float = 0.0,
    maximum_position_deg: float = 360.0,
) -> np.ndarray:
    """ Extract Valid Rotation Window """

    # Convert Arrays To Numpy
    output_position_deg = np.asarray(output_position_deg, dtype=np.float64)
    data_valid_flag = np.asarray(data_valid_flag).astype(bool)

    # Validate Input Shape
    assert output_position_deg.shape == data_valid_flag.shape, (
        f"Output Position and DataValid shape mismatch | {output_position_deg.shape} vs {data_valid_flag.shape}"
    )

    # Build DataValid Mask
    valid_data_mask = data_valid_flag

    # Build Position Mask
    valid_position_mask = (output_position_deg >= minimum_position_deg) & (output_position_deg <= maximum_position_deg)

    # Merge Masks
    valid_rotation_mask = valid_data_mask & valid_position_mask

    # Validate Final Window
    assert np.any(valid_rotation_mask), "Valid Rotation Mask is empty | Check DataValid flags and output position range"

    return valid_rotation_mask


def build_raw_directional_sample(
    source_file_path: str | Path,
    direction_label: str,
    theta_input_deg: np.ndarray,
    theta_output_deg: np.ndarray,
    output_position_deg: np.ndarray,
    data_valid_flag: np.ndarray,
    speed_rpm: float,
    torque_nm: float,
    oil_temperature_deg: float,
    reduction_ratio: float = REDUCTION_RATIO,
) -> TransmissionErrorCurveSample:
    """ Build Raw Directional Sample """

    # Validate Direction Label
    assert direction_label in [FORWARD_DIRECTION, BACKWARD_DIRECTION], f"Unsupported Direction Label | {direction_label}"

    # Extract Valid Rotation Window
    valid_rotation_mask = extract_valid_rotation_window(
        output_position_deg=output_position_deg,
        data_valid_flag=data_valid_flag,
    )

    # Compute Transmission Error
    transmission_error_deg = compute_transmission_error(
        theta_input_deg=np.asarray(theta_input_deg)[valid_rotation_mask],
        theta_output_deg=np.asarray(theta_output_deg)[valid_rotation_mask],
        reduction_ratio=reduction_ratio,
    )

    # Extract Valid Output Position
    angular_position_deg = np.asarray(output_position_deg, dtype=np.float64)[valid_rotation_mask]

    # Sort By Output Position
    sorting_indices = np.argsort(angular_position_deg)
    angular_position_deg = angular_position_deg[sorting_indices].astype(np.float32)
    transmission_error_deg = transmission_error_deg[sorting_indices].astype(np.float32)

    # Resolve Direction Flag
    direction_flag = FORWARD_DIRECTION_FLAG if direction_label == FORWARD_DIRECTION else BACKWARD_DIRECTION_FLAG

    return TransmissionErrorCurveSample(
        source_file_path=Path(source_file_path).resolve(),
        direction_label=direction_label,
        direction_flag=direction_flag,
        speed_rpm=float(speed_rpm),
        torque_nm=float(torque_nm),
        oil_temperature_deg=float(oil_temperature_deg),
        angular_position_deg=angular_position_deg,
        transmission_error_deg=transmission_error_deg,
    )


def build_validated_directional_sample(
    csv_file_path: str | Path,
    direction_label: str,
) -> TransmissionErrorCurveSample:
    """ Build Validated Directional Sample """

    # Resolve CSV Path
    csv_file_path = Path(csv_file_path).resolve()

    # Validate Direction Label
    assert direction_label in [FORWARD_DIRECTION, BACKWARD_DIRECTION], f"Unsupported Direction Label | {direction_label}"

    # Load Validated Dataframe
    validated_dataframe = load_validated_te_dataframe(str(csv_file_path))

    # Parse Metadata
    operating_condition_metadata = parse_operating_condition_metadata(csv_file_path)

    # Select Direction Columns
    if direction_label == FORWARD_DIRECTION:
        angular_position_key = "position_output_reducer_fw_deg"
        transmission_error_key = "transmission_error_fw_deg"
        direction_flag = FORWARD_DIRECTION_FLAG
    else:
        angular_position_key = "position_output_reducer_bw_deg"
        transmission_error_key = "transmission_error_bw_deg"
        direction_flag = BACKWARD_DIRECTION_FLAG

    # Extract Directional Arrays
    angular_position_deg = validated_dataframe[angular_position_key].to_numpy(dtype=np.float32)
    transmission_error_deg = validated_dataframe[transmission_error_key].to_numpy(dtype=np.float32)

    # Remove Invalid Samples
    finite_mask = np.isfinite(angular_position_deg) & np.isfinite(transmission_error_deg)
    angular_position_deg = angular_position_deg[finite_mask]
    transmission_error_deg = transmission_error_deg[finite_mask]

    # Keep Full Rotation Interval
    rotation_mask = (angular_position_deg >= 0.0) & (angular_position_deg <= 360.0)
    angular_position_deg = angular_position_deg[rotation_mask]
    transmission_error_deg = transmission_error_deg[rotation_mask]

    # Sort By Output Position
    sorting_indices = np.argsort(angular_position_deg)
    angular_position_deg = angular_position_deg[sorting_indices]
    transmission_error_deg = transmission_error_deg[sorting_indices]

    # Validate Final Arrays
    assert angular_position_deg.size > 0, f"Empty Angular Position array after processing | {csv_file_path} | {direction_label}"
    assert transmission_error_deg.size == angular_position_deg.size, (
        f"Transmission Error length mismatch | {transmission_error_deg.size} vs {angular_position_deg.size}"
    )

    return TransmissionErrorCurveSample(
        source_file_path=csv_file_path,
        direction_label=direction_label,
        direction_flag=direction_flag,
        speed_rpm=operating_condition_metadata["speed_rpm"],
        torque_nm=operating_condition_metadata["torque_nm"],
        oil_temperature_deg=operating_condition_metadata["oil_temperature_deg"],
        angular_position_deg=angular_position_deg,
        transmission_error_deg=transmission_error_deg,
    )


def build_validated_directional_samples(csv_file_path: str | Path) -> list[TransmissionErrorCurveSample]:
    """ Build Validated Directional Samples """

    # Build Forward And Backward Samples
    forward_sample = build_validated_directional_sample(csv_file_path=csv_file_path, direction_label=FORWARD_DIRECTION)
    backward_sample = build_validated_directional_sample(csv_file_path=csv_file_path, direction_label=BACKWARD_DIRECTION)

    return [forward_sample, backward_sample]


def build_directional_file_manifest(
    dataset_root: str | Path = DEFAULT_DATASET_PATH,
    use_forward_direction: bool = True,
    use_backward_direction: bool = True,
) -> list[tuple[Path, str]]:
    """ Build Directional File Manifest """

    # Validate Direction Configuration
    assert use_forward_direction or use_backward_direction, "At least one direction must be enabled"

    # Collect CSV Files
    csv_file_paths = collect_dataset_csv_paths(dataset_root=dataset_root)

    # Build Manifest
    directional_file_manifest: list[tuple[Path, str]] = []
    for csv_file_path in csv_file_paths:
        if use_forward_direction:
            directional_file_manifest.append((csv_file_path, FORWARD_DIRECTION))
        if use_backward_direction:
            directional_file_manifest.append((csv_file_path, BACKWARD_DIRECTION))

    return directional_file_manifest


class TransmissionErrorCurveDataset(Dataset):
    """ Transmission Error Curve Dataset """

    def __init__(
        self,
        dataset_root: str | Path = DEFAULT_DATASET_PATH,
        use_forward_direction: bool = True,
        use_backward_direction: bool = True,
        directional_file_manifest: list[tuple[str | Path, str]] | None = None,
    ) -> None:
        # Initialize Dataset Configuration
        self.dataset_root = Path(dataset_root).resolve()
        self.use_forward_direction = use_forward_direction
        self.use_backward_direction = use_backward_direction

        # Build Directional Manifest
        if directional_file_manifest is None:
            built_manifest = build_directional_file_manifest(
                dataset_root=self.dataset_root,
                use_forward_direction=self.use_forward_direction,
                use_backward_direction=self.use_backward_direction,
            )
        else:
            built_manifest = [(Path(csv_file_path).resolve(), direction_label) for csv_file_path, direction_label in directional_file_manifest]

        # Save Manifest
        self.directional_file_manifest = built_manifest

        # Validate Manifest
        assert len(self.directional_file_manifest) > 0, "Directional File Manifest is empty"

    def __len__(self) -> int:
        """ Return Dataset Length """

        return len(self.directional_file_manifest)

    def __getitem__(self, dataset_index: int) -> dict[str, Any]:
        """ Return Dataset Item """

        # Parse Manifest Entry
        csv_file_path, direction_label = self.directional_file_manifest[dataset_index]

        # Build Directional Sample
        transmission_error_curve_sample = build_validated_directional_sample(
            csv_file_path=csv_file_path,
            direction_label=direction_label,
        )

        # Build Input Feature Matrix
        sequence_length = transmission_error_curve_sample.angular_position_deg.shape[0]

        angular_position_column = transmission_error_curve_sample.angular_position_deg.astype(np.float32)
        speed_column = np.full(sequence_length, transmission_error_curve_sample.speed_rpm, dtype=np.float32)
        torque_column = np.full(sequence_length, transmission_error_curve_sample.torque_nm, dtype=np.float32)
        oil_temperature_column = np.full(sequence_length, transmission_error_curve_sample.oil_temperature_deg, dtype=np.float32)
        direction_column = np.full(sequence_length, transmission_error_curve_sample.direction_flag, dtype=np.float32)

        input_feature_matrix = np.column_stack(
            [
                angular_position_column,
                speed_column,
                torque_column,
                oil_temperature_column,
                direction_column,
            ]
        ).astype(np.float32)

        # Build Output Tensor
        transmission_error_column = transmission_error_curve_sample.transmission_error_deg[:, np.newaxis].astype(np.float32)
        angular_position_matrix = transmission_error_curve_sample.angular_position_deg[:, np.newaxis].astype(np.float32)

        return {
            "input_tensor": torch.from_numpy(input_feature_matrix),
            "target_tensor": torch.from_numpy(transmission_error_column),
            "angular_position_deg": torch.from_numpy(angular_position_matrix),
            "sequence_length": sequence_length,
            "speed_rpm": transmission_error_curve_sample.speed_rpm,
            "torque_nm": transmission_error_curve_sample.torque_nm,
            "oil_temperature_deg": transmission_error_curve_sample.oil_temperature_deg,
            "direction_label": transmission_error_curve_sample.direction_label,
            "direction_flag": transmission_error_curve_sample.direction_flag,
            "source_file_path": str(transmission_error_curve_sample.source_file_path),
        }


def collate_transmission_error_curves(batch_dictionary_list: list[dict[str, Any]]) -> dict[str, Any]:
    """ Collate Transmission Error Curves """

    # Validate Batch Input
    assert len(batch_dictionary_list) > 0, "Batch Dictionary List is empty"

    # Collect Batch Dimensions
    batch_size = len(batch_dictionary_list)
    sequence_length_tensor = torch.tensor(
        [sample_dictionary["sequence_length"] for sample_dictionary in batch_dictionary_list],
        dtype=torch.long,
    )
    maximum_sequence_length = int(sequence_length_tensor.max().item())
    input_feature_dim = batch_dictionary_list[0]["input_tensor"].shape[-1]
    target_feature_dim = batch_dictionary_list[0]["target_tensor"].shape[-1]

    # Initialize Padded Tensors
    input_tensor = torch.zeros(batch_size, maximum_sequence_length, input_feature_dim, dtype=torch.float32)
    target_tensor = torch.zeros(batch_size, maximum_sequence_length, target_feature_dim, dtype=torch.float32)
    angular_position_deg = torch.zeros(batch_size, maximum_sequence_length, 1, dtype=torch.float32)
    valid_mask = torch.zeros(batch_size, maximum_sequence_length, dtype=torch.bool)

    # Fill Padded Tensors
    for batch_index, sample_dictionary in enumerate(batch_dictionary_list):
        current_sequence_length = int(sample_dictionary["sequence_length"])

        input_tensor[batch_index, :current_sequence_length] = sample_dictionary["input_tensor"]
        target_tensor[batch_index, :current_sequence_length] = sample_dictionary["target_tensor"]
        angular_position_deg[batch_index, :current_sequence_length] = sample_dictionary["angular_position_deg"]
        valid_mask[batch_index, :current_sequence_length] = True

    return {
        "input_tensor": input_tensor,
        "target_tensor": target_tensor,
        "angular_position_deg": angular_position_deg,
        "valid_mask": valid_mask,
        "sequence_length": sequence_length_tensor,
        "speed_rpm": torch.tensor([sample_dictionary["speed_rpm"] for sample_dictionary in batch_dictionary_list], dtype=torch.float32),
        "torque_nm": torch.tensor([sample_dictionary["torque_nm"] for sample_dictionary in batch_dictionary_list], dtype=torch.float32),
        "oil_temperature_deg": torch.tensor(
            [sample_dictionary["oil_temperature_deg"] for sample_dictionary in batch_dictionary_list],
            dtype=torch.float32,
        ),
        "direction_flag": torch.tensor([sample_dictionary["direction_flag"] for sample_dictionary in batch_dictionary_list], dtype=torch.float32),
        "direction_label": [sample_dictionary["direction_label"] for sample_dictionary in batch_dictionary_list],
        "source_file_path": [sample_dictionary["source_file_path"] for sample_dictionary in batch_dictionary_list],
    }


def flatten_curve_batch(curve_batch_dictionary: dict[str, Any]) -> dict[str, torch.Tensor]:
    """ Flatten Curve Batch """

    # Extract Batch Tensors
    input_tensor = curve_batch_dictionary["input_tensor"]
    target_tensor = curve_batch_dictionary["target_tensor"]
    angular_position_deg = curve_batch_dictionary["angular_position_deg"]
    valid_mask = curve_batch_dictionary["valid_mask"]

    # Flatten Valid Samples
    flattened_input_tensor = input_tensor[valid_mask]
    flattened_target_tensor = target_tensor[valid_mask]
    flattened_angular_position_deg = angular_position_deg[valid_mask]

    return {
        "input_tensor": flattened_input_tensor,
        "target_tensor": flattened_target_tensor,
        "angular_position_deg": flattened_angular_position_deg,
    }


def split_directional_file_manifest(
    directional_file_manifest: list[tuple[Path, str]],
    validation_split: float = 0.2,
    random_seed: int = 42,
) -> tuple[list[tuple[Path, str]], list[tuple[Path, str]]]:
    """ Split Directional File Manifest """

    # Validate Split Configuration
    assert 0.0 < validation_split < 1.0, f"Validation Split must be between 0 and 1 | {validation_split}"

    # Collect Unique CSV Paths
    unique_csv_file_paths = sorted({csv_file_path for csv_file_path, _ in directional_file_manifest})
    assert len(unique_csv_file_paths) >= 2, "At least two CSV files are required to build train and validation splits"

    # Shuffle CSV Paths
    random_generator = random.Random(random_seed)
    random_generator.shuffle(unique_csv_file_paths)

    # Build Split Indices
    validation_file_count = max(1, int(round(len(unique_csv_file_paths) * validation_split)))
    if validation_file_count >= len(unique_csv_file_paths):
        validation_file_count = len(unique_csv_file_paths) - 1

    validation_csv_file_paths = set(unique_csv_file_paths[:validation_file_count])

    # Split Manifest
    train_directional_file_manifest = [
        (csv_file_path, direction_label)
        for csv_file_path, direction_label in directional_file_manifest
        if csv_file_path not in validation_csv_file_paths
    ]
    validation_directional_file_manifest = [
        (csv_file_path, direction_label)
        for csv_file_path, direction_label in directional_file_manifest
        if csv_file_path in validation_csv_file_paths
    ]

    # Validate Split Results
    assert len(train_directional_file_manifest) > 0, "Train Directional File Manifest is empty"
    assert len(validation_directional_file_manifest) > 0, "Validation Directional File Manifest is empty"

    return train_directional_file_manifest, validation_directional_file_manifest


def create_transmission_error_dataloaders(
    dataset_root: str | Path = DEFAULT_DATASET_PATH,
    batch_size: int = 8,
    validation_split: float = 0.2,
    random_seed: int = 42,
    num_workers: int = 0,
    use_forward_direction: bool = True,
    use_backward_direction: bool = True,
) -> dict[str, Any]:
    """ Create Transmission Error Dataloaders """

    # Build Directional Manifest
    directional_file_manifest = build_directional_file_manifest(
        dataset_root=dataset_root,
        use_forward_direction=use_forward_direction,
        use_backward_direction=use_backward_direction,
    )

    # Split Manifest
    train_directional_file_manifest, validation_directional_file_manifest = split_directional_file_manifest(
        directional_file_manifest=directional_file_manifest,
        validation_split=validation_split,
        random_seed=random_seed,
    )

    # Build Dataset Objects
    train_dataset = TransmissionErrorCurveDataset(
        dataset_root=dataset_root,
        directional_file_manifest=train_directional_file_manifest,
    )
    validation_dataset = TransmissionErrorCurveDataset(
        dataset_root=dataset_root,
        directional_file_manifest=validation_directional_file_manifest,
    )

    # Build DataLoaders
    train_dataloader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        collate_fn=collate_transmission_error_curves,
    )
    validation_dataloader = DataLoader(
        validation_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        collate_fn=collate_transmission_error_curves,
    )

    return {
        "train_dataset": train_dataset,
        "validation_dataset": validation_dataset,
        "train_dataloader": train_dataloader,
        "validation_dataloader": validation_dataloader,
    }


def create_transmission_error_dataloaders_from_config(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> dict[str, Any]:
    """ Create Transmission Error Dataloaders From Config """

    # Load Configuration
    dataset_processing_config = load_dataset_processing_config(config_path=config_path)

    # Extract Paths
    dataset_root = resolve_project_relative_path(dataset_processing_config["paths"]["dataset_root"])

    # Extract Dataloader Parameters
    dataloader_config = dataset_processing_config["dataloader"]
    split_config = dataset_processing_config["split"]
    direction_config = dataset_processing_config["directions"]

    return create_transmission_error_dataloaders(
        dataset_root=dataset_root,
        batch_size=int(dataloader_config["batch_size"]),
        validation_split=float(split_config["validation_split"]),
        random_seed=int(split_config["random_seed"]),
        num_workers=int(dataloader_config["num_workers"]),
        use_forward_direction=bool(direction_config["use_forward_direction"]),
        use_backward_direction=bool(direction_config["use_backward_direction"]),
    )
