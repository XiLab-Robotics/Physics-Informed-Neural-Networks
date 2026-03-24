"""Lightning data module and batch utilities for TE regression training."""

from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any

# Import PyTorch Lightning Utilities
from lightning.pytorch import LightningDataModule

# Import PyTorch Utilities
import torch
from torch.utils.data import DataLoader

# Import Dataset Utilities
from scripts.datasets.transmission_error_dataset import TransmissionErrorCurveDataset
from scripts.datasets.transmission_error_dataset import build_directional_file_manifest
from scripts.datasets.transmission_error_dataset import load_dataset_processing_config
from scripts.datasets.transmission_error_dataset import resolve_project_relative_path
from scripts.datasets.transmission_error_dataset import split_directional_file_manifest

@dataclass
class NormalizationStatistics:

    """Feature and target normalization tensors for TE regression."""

    input_feature_mean: torch.Tensor
    input_feature_std: torch.Tensor
    target_mean: torch.Tensor
    target_std: torch.Tensor

@dataclass
class DatasetSplitSummary:

    """Curve counts for the train, validation, and test splits."""

    train_curve_count: int
    validation_curve_count: int
    test_curve_count: int

def move_batch_tensor_collection_to_device(batch_value: Any, device: torch.device, use_non_blocking_transfer: bool = False) -> Any:

    """Recursively move a nested batch structure to the requested device.

    Args:
        batch_value: Tensor, list, tuple, dictionary, or scalar batch value.
        device: Target device for tensor transfer.
        use_non_blocking_transfer: Whether CUDA transfers should request
            non-blocking behavior when possible.

    Returns:
        Any: Batch structure mirrored on the target device.
    """

    # Move Tensor To Requested Device
    if isinstance(batch_value, torch.Tensor):

        non_blocking_transfer_is_enabled = use_non_blocking_transfer and device.type == "cuda"
        return batch_value.to(device, non_blocking=non_blocking_transfer_is_enabled)

    # Recursively Move Dictionary Values
    if isinstance(batch_value, dict):
        return {key: move_batch_tensor_collection_to_device(value, device, use_non_blocking_transfer) for key, value in batch_value.items()}

    # Recursively Move Tuple Values
    if isinstance(batch_value, tuple):
        return tuple(move_batch_tensor_collection_to_device(value, device, use_non_blocking_transfer) for value in batch_value)

    # Recursively Move List Values
    if isinstance(batch_value, list):
        return [move_batch_tensor_collection_to_device(value, device, use_non_blocking_transfer) for value in batch_value]

    return batch_value

def extract_point_tensor_from_curve_sample(curve_sample_dictionary: dict[str, Any], point_stride: int = 1, maximum_points_per_curve: int | None = None) -> dict[str, torch.Tensor]:

    """Convert one curve sample into a point-sampled tensor dictionary.

    Args:
        curve_sample_dictionary: Dataset sample containing full-curve tensors.
        point_stride: Step used to subsample curve points.
        maximum_points_per_curve: Optional hard cap on sampled points per curve.

    Returns:
        dict[str, torch.Tensor]: Point-level tensors for model input, target,
        and angular position.
    """

    # Validate Sampling Parameters
    assert point_stride > 0, f"Point Stride must be positive | {point_stride}"
    if maximum_points_per_curve is not None: assert maximum_points_per_curve > 0, (f"Maximum Points Per Curve must be positive | {maximum_points_per_curve}")

    # Extract Curve Tensors
    input_tensor = curve_sample_dictionary["input_tensor"].float()
    target_tensor = curve_sample_dictionary["target_tensor"].float()
    angular_position_deg = curve_sample_dictionary["angular_position_deg"].float()

    # Validate Curve Shapes
    assert input_tensor.ndim == 2, f"Input Tensor must be rank-2 | {tuple(input_tensor.shape)}"
    assert target_tensor.ndim == 2, f"Target Tensor must be rank-2 | {tuple(target_tensor.shape)}"
    assert angular_position_deg.ndim == 2, f"Angular Position Tensor must be rank-2 | {tuple(angular_position_deg.shape)}"
    assert input_tensor.shape[0] == target_tensor.shape[0] == angular_position_deg.shape[0], ("Input, Target, and Angular Position tensors must share the same sequence length")

    # Build Point Indices
    point_index_tensor = torch.arange(0, input_tensor.shape[0], point_stride, dtype=torch.long)
    assert len(point_index_tensor) > 0, "Point Index Tensor is empty after applying Point Stride"

    # Reduce Number Of Points Per Curve
    if maximum_points_per_curve is not None and len(point_index_tensor) > maximum_points_per_curve:

        # Distribute Reduced Indices Across The Full Curve Span
        reduced_index_positions = torch.linspace(0, len(point_index_tensor) - 1, steps=maximum_points_per_curve, dtype=torch.float32,).round().long()
        point_index_tensor = point_index_tensor.index_select(0, reduced_index_positions)

    # Extract Point Tensors
    point_input_tensor = input_tensor.index_select(0, point_index_tensor)
    point_target_tensor = target_tensor.index_select(0, point_index_tensor)
    point_angular_position_deg = angular_position_deg.index_select(0, point_index_tensor)

    return {
        "input_tensor": point_input_tensor,
        "target_tensor": point_target_tensor,
        "angular_position_deg": point_angular_position_deg,
    }

def collate_transmission_error_points(batch_dictionary_list: list[dict[str, Any]], point_stride: int = 1, maximum_points_per_curve: int | None = None, shuffle_points: bool = True) -> dict[str, Any]:

    """Collate curve samples into one point-level training batch.

    Args:
        batch_dictionary_list: Curve-level samples produced by the dataset.
        point_stride: Step used to subsample points from each curve.
        maximum_points_per_curve: Optional cap on sampled points per curve.
        shuffle_points: Whether to shuffle the concatenated point batch.

    Returns:
        dict[str, Any]: Batch dictionary containing concatenated tensors and
        lightweight curve-level metadata.
    """

    # Validate Batch Input
    assert len(batch_dictionary_list) > 0, "Batch Dictionary List is empty"

    # Initialize Point Lists
    input_tensor_list: list[torch.Tensor] = []
    target_tensor_list: list[torch.Tensor] = []
    angular_position_tensor_list: list[torch.Tensor] = []
    point_count_per_curve: list[int] = []

    # Extract Point Samples From Each Curve
    for curve_sample_dictionary in batch_dictionary_list:

        # Extract Point Sample Dictionary From Curve Sample Dictionary
        point_sample_dictionary = extract_point_tensor_from_curve_sample(
            curve_sample_dictionary,
            point_stride,
            maximum_points_per_curve,
        )

        # Append Point Tensors To Batch Lists
        input_tensor_list.append(point_sample_dictionary["input_tensor"])
        target_tensor_list.append(point_sample_dictionary["target_tensor"])
        angular_position_tensor_list.append(point_sample_dictionary["angular_position_deg"])
        point_count_per_curve.append(point_sample_dictionary["input_tensor"].shape[0])

    # Concatenate Point Tensors
    input_tensor = torch.cat(input_tensor_list, dim=0)
    target_tensor = torch.cat(target_tensor_list, dim=0)
    angular_position_deg = torch.cat(angular_position_tensor_list, dim=0)

    # Shuffle Points Inside Batch
    if shuffle_points and input_tensor.shape[0] > 1:

        permutation_indices = torch.randperm(input_tensor.shape[0])
        input_tensor = input_tensor.index_select(0, permutation_indices)
        target_tensor = target_tensor.index_select(0, permutation_indices)
        angular_position_deg = angular_position_deg.index_select(0, permutation_indices)

    return {
        "input_tensor": input_tensor,
        "target_tensor": target_tensor,
        "angular_position_deg": angular_position_deg,
        "point_count_per_curve": torch.tensor(point_count_per_curve, dtype=torch.long),
        "curve_count": len(batch_dictionary_list),
        "direction_label": [curve_sample_dictionary["direction_label"] for curve_sample_dictionary in batch_dictionary_list],
        "source_file_path": [curve_sample_dictionary["source_file_path"] for curve_sample_dictionary in batch_dictionary_list],
    }

class TransmissionErrorDataModule(LightningDataModule):

    """LightningDataModule for TE curve splits, sampling, and normalization."""

    def __init__(
        self,
        dataset_config_path: str | Path,
        curve_batch_size: int = 2,
        point_stride: int = 20,
        maximum_points_per_curve: int | None = None,
        num_workers: int = 0,
        pin_memory: bool = False,
        use_non_blocking_transfer: bool = False,
    ) -> None:
        """Initialize the reusable TE training datamodule.

        Args:
            dataset_config_path: Dataset YAML configuration path.
            curve_batch_size: Number of curves loaded per dataloader batch.
            point_stride: Subsampling stride applied inside each curve.
            maximum_points_per_curve: Optional cap on sampled points per curve.
            num_workers: PyTorch dataloader worker count.
            pin_memory: Whether dataloaders should pin host memory.
            use_non_blocking_transfer: Whether device transfer should request
                non-blocking CUDA copies when possible.
        """

        super().__init__()

        # Validate Dataloader Parameters
        assert curve_batch_size > 0, f"Curve Batch Size must be positive | {curve_batch_size}"
        assert point_stride > 0, f"Point Stride must be positive | {point_stride}"
        assert num_workers >= 0, f"Num Workers must be non-negative | {num_workers}"

        # Save Dataset Parameters
        self.dataset_config_path = resolve_project_relative_path(dataset_config_path)
        self.curve_batch_size = curve_batch_size
        self.point_stride = point_stride
        self.maximum_points_per_curve = maximum_points_per_curve
        self.num_workers = num_workers
        self.pin_memory = pin_memory
        self.use_non_blocking_transfer = use_non_blocking_transfer

        # Initialize Runtime Attributes
        self.train_dataset: TransmissionErrorCurveDataset | None = None
        self.validation_dataset: TransmissionErrorCurveDataset | None = None
        self.test_dataset: TransmissionErrorCurveDataset | None = None
        self.input_feature_dim: int | None = None
        self.target_feature_dim: int | None = None
        self.normalization_statistics: NormalizationStatistics | None = None

    def setup(self, stage: str | None = None) -> None:

        """Create dataset splits and compute normalization statistics.

        Args:
            stage: Lightning stage hint. The current implementation uses the
                same prepared splits for fit, validation, and test access.
        """

        # Skip Repeated Setup If Datasets Are Already Available
        if self.train_dataset is not None and self.validation_dataset is not None and self.test_dataset is not None: return

        # Load Dataset Processing Configuration
        dataset_processing_config = load_dataset_processing_config(self.dataset_config_path)

        # Resolve Dataset Root
        dataset_root = resolve_project_relative_path(dataset_processing_config["paths"]["dataset_root"])

        # Build Directional File Manifest
        directional_file_manifest = build_directional_file_manifest(
            dataset_root,
            bool(dataset_processing_config["directions"]["use_forward_direction"]),
            bool(dataset_processing_config["directions"]["use_backward_direction"]),
        )

        # Split Directional File Manifest
        train_directional_file_manifest, validation_directional_file_manifest, test_directional_file_manifest = split_directional_file_manifest(
            directional_file_manifest,
            float(dataset_processing_config["split"]["validation_split"]),
            float(dataset_processing_config["split"].get("test_split", 0.0)),
            int(dataset_processing_config["split"]["random_seed"]),
        )

        # Build Train Dataset Object
        self.train_dataset = TransmissionErrorCurveDataset(
            dataset_root=dataset_root,
            directional_file_manifest=train_directional_file_manifest,
        )

        # Build Validation Dataset Object
        self.validation_dataset = TransmissionErrorCurveDataset(
            dataset_root=dataset_root,
            directional_file_manifest=validation_directional_file_manifest,
        )

        # Build Test Dataset Object
        self.test_dataset = TransmissionErrorCurveDataset(
            dataset_root=dataset_root,
            directional_file_manifest=test_directional_file_manifest,
        )

        # Read Feature Dimensions
        first_train_sample = self.train_dataset[0]
        self.input_feature_dim = int(first_train_sample["input_tensor"].shape[-1])
        self.target_feature_dim = int(first_train_sample["target_tensor"].shape[-1])

        # Compute Normalization Statistics
        self.normalization_statistics = self.compute_normalization_statistics(self.train_dataset)

    def compute_normalization_statistics(self, curve_dataset: TransmissionErrorCurveDataset) -> NormalizationStatistics:

        """Compute point-level normalization statistics from the train split.

        Args:
            curve_dataset: Dataset used to accumulate sampled point statistics.

        Returns:
            NormalizationStatistics: Mean and standard deviation tensors for
            model inputs and targets.
        """

        # Initialize Accumulators
        input_feature_sum = torch.zeros(self.input_feature_dim, dtype=torch.float64)
        input_feature_squared_sum = torch.zeros(self.input_feature_dim, dtype=torch.float64)
        target_sum = torch.zeros(self.target_feature_dim, dtype=torch.float64)
        target_squared_sum = torch.zeros(self.target_feature_dim, dtype=torch.float64)
        total_point_count = 0

        # Scan Training Curves
        for curve_index in range(len(curve_dataset)):

            curve_sample_dictionary = curve_dataset[curve_index]
            point_sample_dictionary = extract_point_tensor_from_curve_sample(
                curve_sample_dictionary,
                self.point_stride,
                self.maximum_points_per_curve,
            )

            input_tensor = point_sample_dictionary["input_tensor"].double()
            target_tensor = point_sample_dictionary["target_tensor"].double()

            input_feature_sum += input_tensor.sum(dim=0)
            input_feature_squared_sum += torch.square(input_tensor).sum(dim=0)
            target_sum += target_tensor.sum(dim=0)
            target_squared_sum += torch.square(target_tensor).sum(dim=0)
            total_point_count += int(input_tensor.shape[0])

        # Validate Point Count
        assert total_point_count > 0, "Normalization Statistics cannot be computed from an empty training set"

        # Compute Means
        input_feature_mean = input_feature_sum / total_point_count
        target_mean = target_sum / total_point_count

        # Compute Variances
        input_feature_variance = (input_feature_squared_sum / total_point_count) - torch.square(input_feature_mean)
        target_variance = (target_squared_sum / total_point_count) - torch.square(target_mean)

        # Clamp Variances
        input_feature_variance = torch.clamp(input_feature_variance, min=1.0e-12)
        target_variance = torch.clamp(target_variance, min=1.0e-12)

        # Compute Standard Deviations
        input_feature_std = torch.sqrt(input_feature_variance)
        target_std = torch.sqrt(target_variance)

        return NormalizationStatistics(
            input_feature_mean=input_feature_mean.float(),
            input_feature_std=input_feature_std.float(),
            target_mean=target_mean.float(),
            target_std=target_std.float(),
        )

    def get_input_feature_dim(self) -> int:

        """Return the resolved input feature dimension after setup."""

        assert self.input_feature_dim is not None, "Input Feature Dim is not available before setup"
        return self.input_feature_dim

    def get_target_feature_dim(self) -> int:

        """Return the resolved target feature dimension after setup."""

        assert self.target_feature_dim is not None, "Target Feature Dim is not available before setup"
        return self.target_feature_dim

    def get_normalization_statistics(self) -> NormalizationStatistics:

        """Return the cached normalization statistics after setup."""

        assert self.normalization_statistics is not None, "Normalization Statistics are not available before setup"
        return self.normalization_statistics

    def get_dataset_split_summary(self) -> DatasetSplitSummary:

        """Return the current split sizes in number of curves."""

        assert self.train_dataset is not None, "Train Dataset is not initialized"
        assert self.validation_dataset is not None, "Validation Dataset is not initialized"
        assert self.test_dataset is not None, "Test Dataset is not initialized"

        return DatasetSplitSummary(
            train_curve_count=len(self.train_dataset),
            validation_curve_count=len(self.validation_dataset),
            test_curve_count=len(self.test_dataset),
        )

    def train_dataloader(self) -> DataLoader:

        """Build the training dataloader with point-level collation."""

        assert self.train_dataset is not None, "Train Dataset is not initialized"

        return DataLoader(
            self.train_dataset,
            batch_size=self.curve_batch_size,
            shuffle=True,
            num_workers=self.num_workers,
            persistent_workers=(self.num_workers > 0),
            pin_memory=self.pin_memory,
            collate_fn=partial(
                collate_transmission_error_points,
                point_stride=self.point_stride,
                maximum_points_per_curve=self.maximum_points_per_curve,
                shuffle_points=True,
            ),
        )

    def val_dataloader(self) -> DataLoader:

        """Build the validation dataloader with deterministic point ordering."""

        assert self.validation_dataset is not None, "Validation Dataset is not initialized"

        return DataLoader(
            self.validation_dataset,
            batch_size=self.curve_batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            persistent_workers=(self.num_workers > 0),
            pin_memory=self.pin_memory,
            collate_fn=partial(
                collate_transmission_error_points,
                point_stride=self.point_stride,
                maximum_points_per_curve=self.maximum_points_per_curve,
                shuffle_points=False,
            ),
        )

    def test_dataloader(self) -> DataLoader:

        """Build the test dataloader with deterministic point ordering."""

        assert self.test_dataset is not None, "Test Dataset is not initialized"

        return DataLoader(
            self.test_dataset,
            batch_size=self.curve_batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            persistent_workers=(self.num_workers > 0),
            pin_memory=self.pin_memory,
            collate_fn=partial(
                collate_transmission_error_points,
                point_stride=self.point_stride,
                maximum_points_per_curve=self.maximum_points_per_curve,
                shuffle_points=False,
            ),
        )

    def transfer_batch_to_device(self, batch: Any, device: torch.device, dataloader_idx: int) -> Any:

        """Move a collated batch to the target accelerator device.

        Args:
            batch: Batch emitted by one of the TE dataloaders.
            device: Target Lightning device.
            dataloader_idx: Dataloader index supplied by Lightning.

        Returns:
            Any: Batch moved to the requested device.
        """

        return move_batch_tensor_collection_to_device(
            batch,
            device,
            self.use_non_blocking_transfer,
        )
