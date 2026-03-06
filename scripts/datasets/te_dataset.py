import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional, Dict, Any

import torch
from torch.utils.data import Dataset, DataLoader, random_split

# Ensure A Single Sample Schema Is Used
# X = [theta_out, omega_in_rpm, tl_c, mout_nm, direction]
# y = [te]

@dataclass
class Normalizers:
    x_mean: torch.Tensor
    x_std: torch.Tensor
    y_mean: torch.Tensor
    y_std: torch.Tensor


class TEDataset(Dataset):

    # Ensure Dataset Is Materialized As Pointwise Samples
    def __init__(
        self,
        csv_dir: str,
        index_csv: str,
        theta_unit: str = "deg",
        normalize_x: bool = True,
        normalize_y: bool = True,
    ) -> None:
        super().__init__()

        # Ensure Index CSV Is Loaded
        idx = pd.read_csv(index_csv)
        required = {"file", "omega_in_rpm", "mout_nm", "tl_c"}
        if not required.issubset(set(idx.columns)):
            raise ValueError(f"index_csv must contain columns: {sorted(required)}")

        xs: list[np.ndarray] = []
        ys: list[np.ndarray] = []

        # Ensure Every Experiment File Is Expanded Into Samples
        for row in idx.itertuples(index=False):
            fpath = os.path.join(csv_dir, getattr(row, "file"))
            df = pd.read_csv(fpath, header=None)

            if df.shape[1] < 4:
                raise ValueError(f"{fpath} must have 4 columns: theta_f, TE_f, theta_b, TE_b")

            theta_f = df.iloc[:, 0].to_numpy(dtype=np.float32)
            te_f    = df.iloc[:, 1].to_numpy(dtype=np.float32)
            theta_b = df.iloc[:, 2].to_numpy(dtype=np.float32)
            te_b    = df.iloc[:, 3].to_numpy(dtype=np.float32)

            # Ensure Theta Is Converted If Needed
            if theta_unit == "deg":
                theta_f = np.deg2rad(theta_f)
                theta_b = np.deg2rad(theta_b)
            elif theta_unit != "rad":
                raise ValueError("theta_unit must be 'deg' or 'rad'")

            omega = np.float32(getattr(row, "omega_in_rpm"))
            mout  = np.float32(getattr(row, "mout_nm"))
            tl    = np.float32(getattr(row, "tl_c"))

            # Ensure Forward Samples Are Added
            x_f = np.stack([
                theta_f,
                np.full_like(theta_f, omega),
                np.full_like(theta_f, tl),
                np.full_like(theta_f, mout),
                np.zeros_like(theta_f),          # direction = 0
            ], axis=1)
            y_f = te_f.reshape(-1, 1)

            # Ensure Backward Samples Are Added
            x_b = np.stack([
                theta_b,
                np.full_like(theta_b, omega),
                np.full_like(theta_b, tl),
                np.full_like(theta_b, mout),
                np.ones_like(theta_b),           # direction = 1
            ], axis=1)
            y_b = te_b.reshape(-1, 1)

            xs.append(x_f); ys.append(y_f)
            xs.append(x_b); ys.append(y_b)

        X = np.concatenate(xs, axis=0)
        Y = np.concatenate(ys, axis=0)

        self.X = torch.from_numpy(X)
        self.Y = torch.from_numpy(Y)

        self.normalize_x = normalize_x
        self.normalize_y = normalize_y
        self.norm: Optional[Normalizers] = None

        # Ensure Normalizers Are Computed On Demand
        if self.normalize_x or self.normalize_y:
            self._fit_normalizers()

    # Ensure Normalization Stats Are Computed
    def _fit_normalizers(self) -> None:
        eps = 1e-8

        x_mean = self.X.mean(dim=0)
        x_std  = self.X.std(dim=0).clamp_min(eps)

        y_mean = self.Y.mean(dim=0)
        y_std  = self.Y.std(dim=0).clamp_min(eps)

        self.norm = Normalizers(x_mean=x_mean, x_std=x_std, y_mean=y_mean, y_std=y_std)

        if self.normalize_x:
            self.X = (self.X - x_mean) / x_std
        if self.normalize_y:
            self.Y = (self.Y - y_mean) / y_std

    def __len__(self) -> int:
        return int(self.X.shape[0])

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.X[idx], self.Y[idx]


# Ensure DataLoaders Are Built With A Reproducible Split
def build_loaders(
    dataset: TEDataset,
    train_ratio: float,
    val_ratio: float,
    test_ratio: float,
    seed: int,
    batch_size: int,
    num_workers: int,
) -> Dict[str, DataLoader]:

    n = len(dataset)
    n_train = int(n * train_ratio)
    n_val   = int(n * val_ratio)
    n_test  = n - n_train - n_val

    gen = torch.Generator().manual_seed(seed)
    ds_train, ds_val, ds_test = random_split(dataset, [n_train, n_val, n_test], generator=gen)

    # Ensure Loaders Are Shuffled Only For Training
    return {
        "train": DataLoader(ds_train, batch_size=batch_size, shuffle=True,  num_workers=num_workers, pin_memory=True),
        "val":   DataLoader(ds_val,   batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=True),
        "test":  DataLoader(ds_test,  batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=True),
    }