"""Data loading utilities for the RV reducer PINN workflow.

Technical notes:
- Raw traces are filtered with ``DataValid == 1`` when that field exists.
- Operating-condition features are normalized with min-max scaling in ``[-1, 1]``:
  ``v_norm = 2*(v_rpm-100)/1700 - 1``
  ``tau_norm = 2*(tau_Nm-0)/1800 - 1``
  ``T_norm = 2*(temp_degC-25)/10 - 1``
- Output rows expose the fields planned in ``doc/2026_03_06_pipeline_dati.md``.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

DEFAULT_HARMONIC_ORDERS: Tuple[int, ...] = (0, 1, 3, 39, 40, 78, 81, 156, 162, 240)


def _norm_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def _find_column(columns: Sequence[str], aliases: Sequence[str]) -> Optional[str]:
    normalized = {_norm_name(col): col for col in columns}
    for alias in aliases:
        resolved = normalized.get(_norm_name(alias))
        if resolved is not None:
            return resolved
    return None


def _to_numeric(series: pd.Series) -> np.ndarray:
    return pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)


def _normalize_minmax(value: float, lower: float, upper: float, clip: bool = True) -> float:
    if upper <= lower:
        raise ValueError(f"Invalid normalization range: [{lower}, {upper}]")
    norm = 2.0 * (value - lower) / (upper - lower) - 1.0
    if clip:
        return float(np.clip(norm, -1.0, 1.0))
    return float(norm)


def _largest_true_run(mask: np.ndarray) -> Optional[Tuple[int, int]]:
    best_start = -1
    best_len = 0
    current_start = -1
    current_len = 0
    for idx, value in enumerate(mask):
        if value:
            if current_len == 0:
                current_start = idx
            current_len += 1
            if current_len > best_len:
                best_len = current_len
                best_start = current_start
        else:
            current_len = 0
    if best_len == 0:
        return None
    return best_start, best_start + best_len


@dataclass(frozen=True)
class NormalizationRanges:
    v_rpm_min: float = 100.0
    v_rpm_max: float = 1800.0
    tau_nm_min: float = 0.0
    tau_nm_max: float = 1800.0
    temp_degc_min: float = 25.0
    temp_degc_max: float = 35.0
    clip: bool = True

    def normalize_v(self, v_rpm: float) -> float:
        return _normalize_minmax(v_rpm, self.v_rpm_min, self.v_rpm_max, clip=self.clip)

    def normalize_tau(self, tau_nm: float) -> float:
        return _normalize_minmax(tau_nm, self.tau_nm_min, self.tau_nm_max, clip=self.clip)

    def normalize_temp(self, temp_degc: float) -> float:
        return _normalize_minmax(temp_degc, self.temp_degc_min, self.temp_degc_max, clip=self.clip)


@dataclass(frozen=True)
class TargetScaler:
    mean: float
    std: float

    def transform(self, values: np.ndarray) -> np.ndarray:
        return (values - self.mean) / self.std

    def inverse_transform(self, values: np.ndarray) -> np.ndarray:
        return values * self.std + self.mean


@dataclass
class DataLoaderConfig:
    dataset_root: Path = Path("data/datasets")
    file_glob: str = "*.csv"
    max_files: Optional[int] = None
    min_samples_per_direction: int = 32
    default_split: str = "train"
    standardize_target: bool = True
    harmonic_orders: Tuple[int, ...] = DEFAULT_HARMONIC_ORDERS
    harmonic_resample_points: int = 2048
    ranges: NormalizationRanges = field(default_factory=NormalizationRanges)
    column_aliases: Dict[str, Tuple[str, ...]] = field(
        default_factory=lambda: {
            "theta_fw": (
                "Position_Output_Reducer_Fw",
                "Poisition_Output_Reducer_Fw",
            ),
            "te_fw": ("Transmission_Error_Fw",),
            "theta_bw": (
                "Position_Output_Reducer_Bw",
                "Poisition_Output_Reducer_Bw",
            ),
            "te_bw": ("Transmission_Error_Bw",),
            "theta_raw": (
                "Position_Output_Reducer",
                "Output_Angle_deg",
                "Theta_deg",
                "theta_deg",
            ),
            "te_raw": (
                "Transmission_Error",
                "TE",
                "te",
            ),
            "data_valid": ("DataValid", "Data_Valid", "data_valid"),
            "direction": ("Direction", "dir_flag", "Dir", "direction"),
        }
    )


@dataclass
class LoadResult:
    frame: pd.DataFrame
    target_scaler: TargetScaler
    skipped_files: Dict[str, str]


class TransmissionErrorDataLoader:
    def __init__(self, config: Optional[DataLoaderConfig] = None) -> None:
        self.config = config or DataLoaderConfig()

    def list_files(self) -> List[Path]:
        files = sorted(self.config.dataset_root.rglob(self.config.file_glob))
        if self.config.max_files is not None:
            files = files[: self.config.max_files]
        return files

    def load(
        self,
        files: Optional[Sequence[Path | str]] = None,
        split_by_condition: Optional[Dict[str, str]] = None,
    ) -> LoadResult:
        selected_files = [Path(p) for p in files] if files else self.list_files()
        split_by_condition = split_by_condition or {}
        rows: List[Dict[str, Any]] = []
        skipped: Dict[str, str] = {}

        for csv_path in selected_files:
            try:
                segments = self._extract_segments(csv_path)
                v_rpm, tau_nm, temp_degc = self._parse_condition(csv_path)
                condition_id = f"{v_rpm:.1f}rpm_{tau_nm:.1f}Nm_{temp_degc:.1f}deg"
                split = split_by_condition.get(condition_id, self.config.default_split)
                v_norm = self.config.ranges.normalize_v(v_rpm)
                tau_norm = self.config.ranges.normalize_tau(tau_nm)
                t_norm = self.config.ranges.normalize_temp(temp_degc)

                for direction_name, dir_flag, theta_deg, te_target in segments:
                    if theta_deg.size < self.config.min_samples_per_direction:
                        skipped[f"{csv_path}:{direction_name}"] = (
                            f"Insufficient samples ({theta_deg.size})"
                        )
                        continue
                    harmonics = self._estimate_harmonics(theta_deg, te_target)
                    theta = np.deg2rad(theta_deg)
                    sin_theta = np.sin(theta)
                    cos_theta = np.cos(theta)
                    file_id = str(csv_path.relative_to(self.config.dataset_root))
                    for idx in range(theta.size):
                        row: Dict[str, Any] = {
                            "theta": float(theta[idx]),
                            "sin_theta": float(sin_theta[idx]),
                            "cos_theta": float(cos_theta[idx]),
                            "v_norm": v_norm,
                            "tau_norm": tau_norm,
                            "T_norm": t_norm,
                            "dir_flag": int(dir_flag),
                            "te_target": float(te_target[idx]),
                            "theta_deg": float(theta_deg[idx]),
                            "file_id": file_id,
                            "split": split,
                            "condition_id": condition_id,
                            "v_rpm": float(v_rpm),
                            "tau_Nm": float(tau_nm),
                            "temp_degC": float(temp_degc),
                        }
                        for k in self.config.harmonic_orders:
                            row[f"A_target_{k}"] = harmonics["A"][k]
                            row[f"phi_target_{k}"] = harmonics["phi"][k]
                        rows.append(row)
            except Exception as exc:  # noqa: BLE001 - keep loader resilient at dataset level.
                skipped[str(csv_path)] = str(exc)

        if not rows:
            raise RuntimeError("No valid samples were loaded. Check dataset path and column mapping.")

        frame = pd.DataFrame(rows)
        scaler = self._fit_and_apply_target_scaler(frame)
        return LoadResult(frame=frame, target_scaler=scaler, skipped_files=skipped)

    @staticmethod
    def to_sample_dicts(
        frame: pd.DataFrame, harmonic_orders: Sequence[int] = DEFAULT_HARMONIC_ORDERS
    ) -> List[Dict[str, Any]]:
        samples: List[Dict[str, Any]] = []
        for _, row in frame.iterrows():
            sample: Dict[str, Any] = {
                "theta": float(row["theta"]),
                "sin_theta": float(row["sin_theta"]),
                "cos_theta": float(row["cos_theta"]),
                "v_norm": float(row["v_norm"]),
                "tau_norm": float(row["tau_norm"]),
                "T_norm": float(row["T_norm"]),
                "dir_flag": int(row["dir_flag"]),
                "te_target": float(row["te_target"]),
                "file_id": str(row["file_id"]),
                "split": str(row["split"]),
                "condition_id": str(row["condition_id"]),
            }
            sample["A_target"] = {
                int(k): float(row[f"A_target_{k}"])
                for k in harmonic_orders
                if f"A_target_{k}" in row.index
            }
            sample["phi_target"] = {
                int(k): float(row[f"phi_target_{k}"])
                for k in harmonic_orders
                if f"phi_target_{k}" in row.index
            }
            samples.append(sample)
        return samples

    def _extract_segments(
        self, csv_path: Path
    ) -> List[Tuple[str, int, np.ndarray, np.ndarray]]:
        df = pd.read_csv(csv_path)
        cols = df.columns.to_list()

        theta_fw_col = _find_column(cols, self.config.column_aliases["theta_fw"])
        te_fw_col = _find_column(cols, self.config.column_aliases["te_fw"])
        theta_bw_col = _find_column(cols, self.config.column_aliases["theta_bw"])
        te_bw_col = _find_column(cols, self.config.column_aliases["te_bw"])

        if theta_fw_col and te_fw_col and theta_bw_col and te_bw_col:
            return self._extract_preprocessed_segments(df, theta_fw_col, te_fw_col, theta_bw_col, te_bw_col)

        return self._extract_raw_segments(df)

    def _extract_preprocessed_segments(
        self,
        df: pd.DataFrame,
        theta_fw_col: str,
        te_fw_col: str,
        theta_bw_col: str,
        te_bw_col: str,
    ) -> List[Tuple[str, int, np.ndarray, np.ndarray]]:
        fw_theta = _to_numeric(df[theta_fw_col])
        fw_te = _to_numeric(df[te_fw_col])
        bw_theta = _to_numeric(df[theta_bw_col])
        bw_te = _to_numeric(df[te_bw_col])

        fw_theta, fw_te = self._clean_and_order(theta_deg=fw_theta, te=fw_te, increasing=True)
        bw_theta, bw_te = self._clean_and_order(theta_deg=bw_theta, te=bw_te, increasing=False)

        return [("fw", +1, fw_theta, fw_te), ("bw", -1, bw_theta, bw_te)]

    def _extract_raw_segments(self, df: pd.DataFrame) -> List[Tuple[str, int, np.ndarray, np.ndarray]]:
        cols = df.columns.to_list()
        theta_col = _find_column(cols, self.config.column_aliases["theta_raw"])
        te_col = _find_column(cols, self.config.column_aliases["te_raw"])
        if theta_col is None or te_col is None:
            raise ValueError(
                "Raw format detected but mandatory columns are missing "
                f"(theta: {theta_col}, te: {te_col})."
            )

        data_valid_col = _find_column(cols, self.config.column_aliases["data_valid"])
        if data_valid_col is not None:
            data_valid = _to_numeric(df[data_valid_col])
            keep = np.isfinite(data_valid) & (data_valid == 1.0)
            df = df.loc[keep].copy()

        theta = _to_numeric(df[theta_col])
        te = _to_numeric(df[te_col])
        finite = np.isfinite(theta) & np.isfinite(te)
        theta = theta[finite]
        te = te[finite]
        if theta.size < self.config.min_samples_per_direction:
            raise ValueError("Raw trace has too few finite samples after filtering.")

        direction_col = _find_column(cols, self.config.column_aliases["direction"])
        fw_mask, bw_mask = self._build_direction_masks(theta, df, direction_col, finite)

        segments: List[Tuple[str, int, np.ndarray, np.ndarray]] = []
        for direction_name, direction_flag, mask in (("fw", +1, fw_mask), ("bw", -1, bw_mask)):
            run = _largest_true_run(mask)
            if run is None:
                continue
            start, end = run
            seg_theta = theta[start:end]
            seg_te = te[start:end]
            theta_deg, te_seg = self._single_turn(seg_theta, seg_te, increasing=(direction_flag > 0))
            if theta_deg.size >= self.config.min_samples_per_direction:
                segments.append((direction_name, direction_flag, theta_deg, te_seg))

        if not segments:
            raise ValueError("Unable to extract forward/backward single-turn segments from raw trace.")
        return segments

    def _build_direction_masks(
        self,
        theta: np.ndarray,
        df: pd.DataFrame,
        direction_col: Optional[str],
        finite_mask_after_filter: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray]:
        if direction_col is not None:
            raw_direction = df[direction_col]
            raw_direction = raw_direction.loc[finite_mask_after_filter]
            numeric = pd.to_numeric(raw_direction, errors="coerce")
            if numeric.notna().any():
                values = numeric.to_numpy(dtype=float)
                fw = values > 0.0
                bw = values < 0.0
                if fw.any() and bw.any():
                    return fw, bw
            labels = raw_direction.astype(str).str.lower()
            fw = labels.str.contains("fw|forw|forward|\\+").to_numpy()
            bw = labels.str.contains("bw|back|backward|\\-").to_numpy()
            if fw.any() and bw.any():
                return fw, bw

        theta_unwrapped = np.rad2deg(np.unwrap(np.deg2rad(theta)))
        dtheta = np.diff(theta_unwrapped, prepend=theta_unwrapped[0])
        fw = dtheta >= 0.0
        bw = dtheta < 0.0
        return fw, bw

    def _single_turn(self, theta: np.ndarray, te: np.ndarray, increasing: bool) -> Tuple[np.ndarray, np.ndarray]:
        theta_unwrapped = np.rad2deg(np.unwrap(np.deg2rad(theta)))
        if increasing:
            start = float(np.nanmin(theta_unwrapped))
            window = (theta_unwrapped >= start) & (theta_unwrapped <= start + 360.0)
            theta_deg = theta_unwrapped[window] - start
        else:
            start = float(np.nanmax(theta_unwrapped))
            window = (theta_unwrapped <= start) & (theta_unwrapped >= start - 360.0)
            theta_deg = 360.0 - (start - theta_unwrapped[window])
        te_turn = te[window]
        return self._clean_and_order(theta_deg=theta_deg, te=te_turn, increasing=increasing)

    def _clean_and_order(
        self, theta_deg: np.ndarray, te: np.ndarray, increasing: bool
    ) -> Tuple[np.ndarray, np.ndarray]:
        finite = np.isfinite(theta_deg) & np.isfinite(te)
        theta_deg = np.clip(theta_deg[finite], 0.0, 360.0)
        te = te[finite]

        if theta_deg.size == 0:
            return theta_deg, te

        order = np.argsort(theta_deg)
        if not increasing:
            order = order[::-1]
        theta_deg = theta_deg[order]
        te = te[order]

        if theta_deg.size > 1:
            keep = np.ones(theta_deg.shape[0], dtype=bool)
            diff = np.diff(theta_deg)
            if increasing:
                keep[1:] = diff > 1e-10
            else:
                keep[1:] = diff < -1e-10
            theta_deg = theta_deg[keep]
            te = te[keep]
        return theta_deg, te

    def _estimate_harmonics(self, theta_deg: np.ndarray, te: np.ndarray) -> Dict[str, Dict[int, float]]:
        if len(self.config.harmonic_orders) == 0:
            return {"A": {}, "phi": {}}

        if self.config.harmonic_resample_points > 0 and theta_deg.size > 4:
            asc_theta = theta_deg[::-1] if theta_deg[0] > theta_deg[-1] else theta_deg.copy()
            asc_te = te[::-1] if theta_deg[0] > theta_deg[-1] else te.copy()
            order = np.argsort(asc_theta)
            asc_theta = asc_theta[order]
            asc_te = asc_te[order]
            rounded = np.round(asc_theta, 10)
            _, unique_idx = np.unique(rounded, return_index=True)
            asc_theta = asc_theta[unique_idx]
            asc_te = asc_te[unique_idx]
            grid_deg = np.linspace(0.0, 360.0, self.config.harmonic_resample_points, endpoint=False)
            te_used = np.interp(grid_deg, asc_theta, asc_te, period=360.0)
            theta_used = np.deg2rad(grid_deg)
        else:
            theta_used = np.deg2rad(theta_deg)
            te_used = te

        amps: Dict[int, float] = {}
        phases: Dict[int, float] = {}
        for k in self.config.harmonic_orders:
            if k == 0:
                amps[k] = float(np.mean(te_used))
                phases[k] = 0.0
                continue
            cos_term = np.cos(k * theta_used)
            sin_term = np.sin(k * theta_used)
            c_k = float(2.0 * np.mean(te_used * cos_term))
            s_k = float(-2.0 * np.mean(te_used * sin_term))
            amp = math.sqrt(c_k * c_k + s_k * s_k)
            phase = math.atan2(-s_k, c_k)
            amps[k] = amp
            phases[k] = phase
        return {"A": amps, "phi": phases}

    def _fit_and_apply_target_scaler(self, frame: pd.DataFrame) -> TargetScaler:
        raw = frame["te_target"].to_numpy(dtype=float)
        if not self.config.standardize_target:
            scaler = TargetScaler(mean=0.0, std=1.0)
            frame["te_target_raw"] = raw
            return scaler

        train_mask = frame["split"].eq("train").to_numpy()
        if not np.any(train_mask):
            train_mask = np.ones_like(raw, dtype=bool)

        mean = float(np.mean(raw[train_mask]))
        std = float(np.std(raw[train_mask]))
        if not np.isfinite(std) or std < 1e-12:
            std = 1.0
        scaler = TargetScaler(mean=mean, std=std)

        frame["te_target_raw"] = raw
        frame["te_target"] = scaler.transform(raw)
        return scaler

    def _parse_condition(self, csv_path: Path) -> Tuple[float, float, float]:
        name = csv_path.stem
        match = re.search(
            r"(?P<rpm>-?\d+(?:\.\d+)?)\s*rpm\s*(?P<nm>-?\d+(?:\.\d+)?)\s*nm\s*(?P<deg>-?\d+(?:\.\d+)?)\s*deg",
            name,
            re.IGNORECASE,
        )
        if match is not None:
            return (
                float(match.group("rpm")),
                float(match.group("nm")),
                float(match.group("deg")),
            )

        rpm_match = re.search(r"(?P<rpm>-?\d+(?:\.\d+)?)\s*rpm", str(csv_path.parent.name), re.IGNORECASE)
        temp_match = re.search(r"test[_\s-]*(?P<deg>-?\d+(?:\.\d+)?)\s*degree", str(csv_path.parent.parent.name), re.IGNORECASE)
        nm_match = re.search(r"(?P<nm>-?\d+(?:\.\d+)?)\s*nm", name, re.IGNORECASE)
        if rpm_match and nm_match and temp_match:
            return (
                float(rpm_match.group("rpm")),
                float(nm_match.group("nm")),
                float(temp_match.group("deg")),
            )

        raise ValueError(f"Cannot parse (rpm, Nm, degC) from filename: {csv_path.name}")


if __name__ == "__main__":
    loader = TransmissionErrorDataLoader(DataLoaderConfig(max_files=2))
    result = loader.load()
    print(f"Loaded rows: {len(result.frame)}")
    print(f"Target scaler: mean={result.target_scaler.mean:.6f}, std={result.target_scaler.std:.6f}")
    print(f"Skipped files/segments: {len(result.skipped_files)}")

