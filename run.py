"""Paper-facing Human-Like launcher for Legacy RCIM and selected DirectML."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "polished_dataset"
COLUMNS = ("theta", "theta_dot", "tau_load", "T", "theta_TE")
DIRECTIONS = ("forward", "backward")
BASELINES = ("feedforward", "harmonic_regression", "tree", "gru_sequence",
             "lstm_sequence", "temporal_convolution", "periodic_mlp",
             "periodic_mlp_harmonic", "residual_harmonic_mlp",
             "periodic_gru_sequence")
SPECIALISTS = ("temporal_analytical_residual_k01", "complex_harmonic_coefficient_h08")
MODELS = BASELINES + SPECIALISTS


def onnx_path(model: str, direction: str) -> Path:
    if model not in MODELS:
        raise ValueError(f"Unknown model: {model}")
    if direction not in DIRECTIONS:
        raise ValueError("Only forward and backward are supported")
    if model == "complex_harmonic_coefficient_h08" and direction != "forward":
        raise ValueError("H08 is a forward-only specialist")
    return ROOT / "models" / "direct_ml" / model / direction / "onnx" / "model.onnx"


def catalog() -> None:
    print("DirectML: published ONNX models (not PLC-qualified)")
    for model in MODELS:
        present = [direction for direction in DIRECTIONS if
                   (model != "complex_harmonic_coefficient_h08" or direction == "forward")
                   and onnx_path(model, direction).is_file()]
        print(f"  {model:43} {','.join(present) or 'MISSING'}")
    print("Legacy RCIM: accepted 10 families x 19 targets per mode/direction")
    for mode in ("setpoints", "actual_values"):
        for direction in DIRECTIONS:
            path = ROOT / "models" / "legacy" / mode / direction
            names = [p for p in path.iterdir() if p.is_dir()] if path.is_dir() else []
            print(f"  {mode}/{direction}: {len(names)} family archives")


def validate_data(root: Path, allow_incomplete: bool = False) -> None:
    """Validate CSV names, pairing and headers; not a full numerical or SHA audit."""
    observed: dict[str, set[str]] = {}
    for direction in DIRECTIONS:
        d = root / direction
        if not d.is_dir():
            raise FileNotFoundError(d)
        paths: set[str] = set()
        for file in sorted(d.rglob("*.csv")):
            name = file.relative_to(d).as_posix()
            if name in paths:
                raise ValueError(f"Duplicate CSV path {name}")
            paths.add(name)
            with file.open("r", newline="", encoding="utf-8-sig") as f:
                header = next(csv.reader(f), [])
            if tuple(header) != COLUMNS:
                raise ValueError(f"Invalid polished CSV header in {file}: {header}")
        if not paths:
            raise ValueError(f"No CSV data in {d}")
        observed[direction] = paths
    if observed["forward"] != observed["backward"]:
        raise ValueError("Fw/Bw paths are not paired on the same nominal conditions")
    count = len(observed["forward"])
    if not allow_incomplete and count != 969:
        raise ValueError(f"Canonical polished dataset must contain 969 pairs, got {count}")
    print(json.dumps({"status": "STRUCTURAL_PASS", "forward": count, "backward": count,
                      "columns": COLUMNS, "scope": "path/header only"}, indent=2))


def new_run_directory(pipeline: str, family: str, direction: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    folder = ROOT / "results" / pipeline / f"{stamp}_{family}_{direction}"
    folder.mkdir(parents=True, exist_ok=False)
    return folder


def train(args: argparse.Namespace) -> None:
    import yaml
    if args.pipeline == "legacy":
        if args.profile != "historical":
            raise ValueError("RCIM exact reimplementation supports the historical split protocol only")
        config = ROOT / "configs" / "legacy" / args.input_mode / (args.direction + ".yaml")
        module = ("scripts.paper_reimplementation.rcim_ml_compensation."
                  "original_dataset_exact_model_bank.run_original_dataset_exact_model_bank_validation")
        family = "rcim_model_bank"
    else:
        if not args.model:
            raise ValueError("--model is required for DirectML")
        onnx_path(args.model, args.direction)
        if args.input_mode != "setpoints":
            raise ValueError("DirectML pretrained-source training supports setpoints only")
        if args.model in SPECIALISTS:
            raise ValueError(f"{args.model}: pretrained offline specialist retained; dedicated retraining is not yet ported")
        family = args.model
        config = ROOT / "configs" / "direct_ml" / family / (args.direction + ".yaml")
        module = ("scripts.training.train_tree_regressor" if family == "tree"
                  else "scripts.training.train_feedforward_network")
    if not config.is_file():
        raise FileNotFoundError(config)
    with config.open("r", encoding="utf-8") as f:
        payload = yaml.safe_load(f)
    if not isinstance(payload, dict):
        raise ValueError("Expected YAML mapping")
    target = new_run_directory(args.pipeline, family, args.direction)
    payload.setdefault("paths", {})["output_root"] = (target / "artifacts").relative_to(ROOT).as_posix()
    meta = payload.setdefault("metadata", {})
    for obsolete in ("run_instance_id", "source_config_path", "planning_report_path",
                     "technical_document_path"):
        meta.pop(obsolete, None)
    meta["output_run_name"] = f"humanlike_{family}_{args.direction}"
    if args.pipeline == "direct_ml" and args.profile == "paired":
        manifest = ROOT / "configs" / "splits" / "paired_conditions.yaml"
        if not manifest.is_file():
            raise FileNotFoundError(manifest)
        payload.setdefault("dataset", {})["split_manifest_path"] = manifest.relative_to(ROOT).as_posix()
    else:
        payload.setdefault("dataset", {}).pop("split_manifest_path", None)
    cfg = target / "config.yaml"
    cfg.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    receipt = {"pipeline": args.pipeline, "family": family, "direction": args.direction,
               "input_mode": args.input_mode, "split_profile": args.profile,
               "source_config": config.relative_to(ROOT).as_posix(), "status": "PREPARED"}
    target.joinpath("manifest.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    cmd = [sys.executable, "-m", module, "--config-path", str(cfg)]
    print("Run directory:", target)
    print("Command:", " ".join(cmd))
    if args.dry_run:
        print("DRY_RUN: training was not executed")
        return
    rc = subprocess.run(cmd, cwd=ROOT, check=False).returncode
    receipt["exit_code"] = rc
    receipt["status"] = "COMPLETED" if rc == 0 else "FAILED"
    target.joinpath("manifest.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    if rc:
        raise SystemExit(rc)


def evaluate(args: argparse.Namespace) -> None:
    """CPU ONNX evaluation limited to pointwise [N,5] models and one TE CSV."""
    path = onnx_path(args.model, args.direction)
    if args.model in SPECIALISTS:
        raise ValueError("Specialist state/coefficients need a dedicated evaluator; not qualified here")
    if not path.is_file():
        raise FileNotFoundError(path)
    csvpath = args.csv.resolve()
    if args.direction not in csvpath.parts:
        raise ValueError("CSV direction does not match model direction")
    import numpy as np
    import pandas as pd
    import onnxruntime as ort
    from scripts.datasets.transmission_error_dataset import parse_operating_condition_metadata
    df = pd.read_csv(csvpath, nrows=args.max_points)
    if tuple(df.columns) != COLUMNS or df.empty:
        raise ValueError("Invalid or empty polished CSV")
    info = parse_operating_condition_metadata(csvpath)
    n = len(df)
    x = np.column_stack((
        df["theta"].to_numpy(dtype=np.float32),
        np.full(n, info["speed_rpm"], dtype=np.float32),
        np.full(n, info["torque_nm"], dtype=np.float32),
        np.full(n, info["oil_temperature_deg"], dtype=np.float32),
        np.full(n, 1.0 if args.direction == "forward" else -1.0, dtype=np.float32),
    ))
    session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
    ins = session.get_inputs()
    if len(ins) != 1 or len(ins[0].shape) != 2 or (isinstance(ins[0].shape[1], int) and ins[0].shape[1] != 5):
        raise ValueError(f"ONNX input is not pointwise [N,5]: {[v.shape for v in ins]}")
    fixed_batch = ins[0].shape[0] if isinstance(ins[0].shape[0], int) else None
    stride = fixed_batch or args.batch_size
    if fixed_batch and n % fixed_batch:
        raise ValueError("Fixed-batch ONNX requires a CSV sample count divisible by batch size")
    pred = np.concatenate([
        np.asarray(session.run(None, {ins[0].name: x[i:i+stride]})[0], dtype=np.float64).reshape(-1)
        for i in range(0, n, stride)
    ])
    truth = df["theta_TE"].to_numpy(dtype=np.float64)
    if pred.shape != truth.shape or not np.isfinite(pred).all():
        raise ValueError("Non-finite or unexpected model prediction")
    err = pred - truth
    metrics = {"model": args.model, "direction": args.direction, "samples": n,
               "mae_deg": float(np.abs(err).mean()), "rmse_deg": float(np.sqrt(np.mean(err**2))),
               "offset_deg": float(err.mean()), "centered_mae_deg": float(np.abs(err-err.mean()).mean())}
    out = new_run_directory("evaluation", args.model, args.direction)
    out.joinpath("metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    pd.DataFrame({"theta_deg": df["theta"], "measured_te_deg": truth, "predicted_te_deg": pred,
                  "error_deg": err}).to_csv(out / "predictions.csv", index=False)
    from matplotlib import pyplot as plt
    plotdir = out / "plots"
    plotdir.mkdir()
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["theta"], truth, label="Measured TE")
    ax.plot(df["theta"], pred, label="Predicted TE")
    ax.set(xlabel="Angle (deg)", ylabel="Transmission error (deg)", title=f"{args.model} - {args.direction}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(plotdir / "prediction_vs_measurement.png", dpi=160)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(df["theta"], err)
    ax.set(xlabel="Angle (deg)", ylabel="Prediction error (deg)", title="Pointwise error")
    fig.tight_layout()
    fig.savefig(plotdir / "error.png", dpi=160)
    plt.close(fig)
    print(json.dumps(metrics, indent=2))
    print("Results:", out)


def main() -> None:
    p = argparse.ArgumentParser(description="Human-Like TE: Legacy RCIM and DirectML")
    sp = p.add_subparsers(dest="command", required=True)
    sp.add_parser("catalog")
    d = sp.add_parser("validate-data")
    d.add_argument("--dataset", type=Path, default=DATA)
    d.add_argument("--allow-incomplete", action="store_true")
    t = sp.add_parser("train")
    t.add_argument("--pipeline", choices=("legacy", "direct_ml"), required=True)
    t.add_argument("--direction", choices=DIRECTIONS, required=True)
    t.add_argument("--model", choices=MODELS)
    t.add_argument("--input-mode", choices=("setpoints", "actual_values"), default="setpoints")
    t.add_argument("--profile", choices=("historical", "paired"), default="historical")
    t.add_argument("--dry-run", action="store_true")
    e = sp.add_parser("evaluate")
    e.add_argument("--model", choices=MODELS, required=True)
    e.add_argument("--direction", choices=DIRECTIONS, required=True)
    e.add_argument("--csv", type=Path, required=True)
    e.add_argument("--max-points", type=int, default=8192)
    e.add_argument("--batch-size", type=int, default=512)
    args = p.parse_args()
    try:
        if args.command == "catalog":
            catalog()
        elif args.command == "validate-data":
            validate_data(args.dataset, args.allow_incomplete)
        elif args.command == "train":
            train(args)
        else:
            if args.max_points < 1 or args.batch_size < 1:
                raise ValueError("Positive --max-points and --batch-size required")
            evaluate(args)
    except (FileNotFoundError, ValueError) as error:
        p.exit(2, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()
