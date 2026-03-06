"""Smoke test for scripts/data_loader.py.

The test generates a synthetic RAW CSV with DataValid and Direction columns,
then validates:
- DataValid filtering behavior
- min-max normalization ranges for v/tau/T
- conversion to finite PyTorch tensors
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
import sys

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from data_loader import DataLoaderConfig, TransmissionErrorDataLoader  # noqa: E402


def build_synthetic_raw_csv(dataset_root: Path) -> Path:
    dataset_root.mkdir(parents=True, exist_ok=True)
    csv_path = dataset_root / "1000.0rpm1000.0Nm25.0deg.csv"

    fw_theta = np.linspace(0.0, 359.0, 40)
    fw_te = 0.02 * np.sin(np.deg2rad(fw_theta))
    bw_theta = np.linspace(359.0, 0.0, 40)
    bw_te = 0.02 * np.cos(np.deg2rad(bw_theta))

    # Invalid rows (DataValid=0) that must be filtered out.
    invalid_theta = np.array([111.0, 222.0, 333.0, 444.0])
    invalid_te = np.array([10.0, -10.0, 7.5, -7.5])

    df = pd.DataFrame(
        {
            "Position_Output_Reducer": np.concatenate([fw_theta, invalid_theta, bw_theta]),
            "Transmission_Error": np.concatenate([fw_te, invalid_te, bw_te]),
            "DataValid": np.concatenate(
                [np.ones_like(fw_theta), np.zeros_like(invalid_theta), np.ones_like(bw_theta)]
            ),
            "Direction": np.concatenate(
                [np.ones_like(fw_theta), np.ones_like(invalid_theta), -np.ones_like(bw_theta)]
            ),
        }
    )
    df.to_csv(csv_path, index=False)
    return csv_path


def main() -> None:
    smoke_root = ROOT / "data" / "_smoke_test_raw"
    csv_path = build_synthetic_raw_csv(smoke_root)

    cfg = DataLoaderConfig(
        dataset_root=smoke_root,
        min_samples_per_direction=10,
        standardize_target=False,
        harmonic_resample_points=0,
    )
    loader = TransmissionErrorDataLoader(cfg)
    result = loader.load(files=[csv_path])
    frame = result.frame

    # DataValid filter expectation: only 40 FW + 40 BW valid rows.
    expected_rows = 80
    if len(frame) != expected_rows:
        raise AssertionError(f"Expected {expected_rows} rows after DataValid filtering, got {len(frame)}")

    # Normalization checks from project formulas.
    v_expected = 2.0 * (1000.0 - 100.0) / 1700.0 - 1.0
    tau_expected = 2.0 * (1000.0 - 0.0) / 1800.0 - 1.0
    t_expected = 2.0 * (25.0 - 25.0) / 10.0 - 1.0

    if not np.allclose(frame["v_norm"].unique(), [v_expected], atol=1e-9):
        raise AssertionError("v_norm does not match expected min-max normalization value")
    if not np.allclose(frame["tau_norm"].unique(), [tau_expected], atol=1e-9):
        raise AssertionError("tau_norm does not match expected min-max normalization value")
    if not np.allclose(frame["T_norm"].unique(), [t_expected], atol=1e-9):
        raise AssertionError("T_norm does not match expected min-max normalization value")

    norm_cols = ["v_norm", "tau_norm", "T_norm"]
    norm_values = frame[norm_cols].to_numpy(dtype=float)
    if np.nanmin(norm_values) < -1.0 - 1e-9 or np.nanmax(norm_values) > 1.0 + 1e-9:
        raise AssertionError("Normalization outputs are outside [-1, 1]")

    # Convert to torch tensors and validate finite outputs.
    feature_cols = ["theta", "sin_theta", "cos_theta", "v_norm", "tau_norm", "T_norm", "dir_flag"]
    x = torch.tensor(frame[feature_cols].to_numpy(dtype=np.float32), dtype=torch.float32)
    y = torch.tensor(frame["te_target"].to_numpy(dtype=np.float32), dtype=torch.float32).unsqueeze(1)

    if not torch.isfinite(x).all().item() or not torch.isfinite(y).all().item():
        raise AssertionError("Non-finite values found in tensors")

    fw_count = int((frame["dir_flag"] == 1).sum())
    bw_count = int((frame["dir_flag"] == -1).sum())

    print("SMOKE TEST PASSED")
    print(f"rows={len(frame)}, fw={fw_count}, bw={bw_count}")
    print(f"x.shape={tuple(x.shape)}, y.shape={tuple(y.shape)}")
    print(
        "norm_values="
        f"v={v_expected:.9f}, tau={tau_expected:.9f}, T={t_expected:.9f}, "
        f"range=[{np.min(norm_values):.9f}, {np.max(norm_values):.9f}]"
    )
    print(f"example_file={csv_path}")


if __name__ == "__main__":
    main()

