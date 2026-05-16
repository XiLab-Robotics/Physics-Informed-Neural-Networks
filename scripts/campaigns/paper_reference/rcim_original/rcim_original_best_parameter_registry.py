"""RCIM original best-parameter registry helper."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support
from typing import Any

import pandas as pd
import yaml

PAPER_REFERENCE_FAMILY_CODE_LIST = [
    "SVR",
    "MLP",
    "RF",
    "DT",
    "ET",
    "ERT",
    "GBM",
    "HGBM",
    "LGBM",
    "XGBM",
    "ELM",
]
DEFAULT_REGISTRY_PATH = Path("output/registries/program/rcim_original_best_hyperparameters.yaml")
SUMMARY_BEST_FILENAME = "summaryBestParameter+_3.8_allFreq.csv"
SUMMARY_CROSS_VALIDATION_FILENAME = "summaryCrossValidation+_3.8_allFreq.csv"
CANONICAL_METRIC_NAME = "aggregate_mae_mean"


def _utc_now_string() -> str:

    """Return one stable timestamp string for registry updates."""

    # Keep Registry Timestamps UTC And Explicit.
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _normalize_family_code(family_code: str) -> str:

    """Normalize one historical family code to the runtime family code."""

    # Preserve Historical SVM Labels While Unifying Runtime Lookup To SVR.
    normalized_family_code = family_code.strip().upper()
    if normalized_family_code == "SVM":
        return "SVR"
    return normalized_family_code


def _parse_family_list(families_argument: str) -> list[str]:

    """Parse one comma-separated family list."""

    # Default To The Canonical Paper-Reference Family Surface.
    if not families_argument.strip():
        return list(PAPER_REFERENCE_FAMILY_CODE_LIST)
    return [
        family_code.strip().upper()
        for family_code in families_argument.split(",")
        if family_code.strip()
    ]


def _load_registry(registry_path: Path) -> dict[str, Any]:

    """Load the YAML registry or return one empty scaffold."""

    # Start From One Explicit Empty Scaffold When The Registry Is New.
    if not registry_path.exists():
        return {"version": 1, "updated_at": None, "branches": {}}

    with registry_path.open("r", encoding="utf-8") as registry_file:
        loaded_payload = yaml.safe_load(registry_file) or {}

    loaded_payload.setdefault("version", 1)
    loaded_payload.setdefault("updated_at", None)
    loaded_payload.setdefault("branches", {})
    return loaded_payload


def _write_registry(registry_path: Path, registry_payload: dict[str, Any]) -> None:

    """Persist the YAML registry."""

    # Keep The Registry Parent Tree Stable Under output/registries/program.
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("w", encoding="utf-8", newline="\n") as registry_file:
        yaml.safe_dump(
            registry_payload,
            registry_file,
            sort_keys=False,
            allow_unicode=False,
            default_flow_style=False,
        )


def _build_cross_validation_path(best_parameter_summary_path: Path) -> Path:

    """Resolve the sibling cross-validation summary path."""

    # The Retune Stage Always Emits The Metric Summary Beside The Best-Parameter Summary.
    return best_parameter_summary_path.parent / SUMMARY_CROSS_VALIDATION_FILENAME


def _compute_aggregate_mae_mean(summary_row: pd.Series) -> float:

    """Compute the canonical aggregate comparison metric for one family row."""

    # Use The Mean Of The Per-Target MAE Columns So Cross-Family Comparisons Stay Reproducible.
    mae_column_name_list = [
        column_name
        for column_name in summary_row.index
        if column_name.endswith("_MAE")
    ]
    if not mae_column_name_list:
        raise ValueError("No *_MAE columns were found in the cross-validation summary row.")
    return float(summary_row[mae_column_name_list].astype(float).mean())


def _read_best_parameter_dataframe(best_parameter_summary_path: Path) -> pd.DataFrame:

    """Read the semicolon best-parameter summary."""

    # The Historical RCIM Summaries Always Use Semicolon Separation.
    return pd.read_csv(best_parameter_summary_path, sep=";", decimal=",")


def _read_cross_validation_dataframe(cross_validation_summary_path: Path) -> pd.DataFrame:

    """Read the semicolon cross-validation summary."""

    # Preserve The Historical Decimal And Separator Conventions.
    return pd.read_csv(cross_validation_summary_path, sep=";", decimal=",")


def _build_metric_entry_map(cross_validation_dataframe: pd.DataFrame) -> dict[str, dict[str, Any]]:

    """Build one family-wise metric map from the cross-validation summary."""

    # Keep The Stored Registry Entries Tied To One Explicit Metric Payload.
    metric_entry_map: dict[str, dict[str, Any]] = {}
    for _, summary_row in cross_validation_dataframe.iterrows():
        family_code = _normalize_family_code(str(summary_row["0_method"]))
        metric_entry_map[family_code] = {
            "summary_family_code": str(summary_row["0_method"]).strip(),
            CANONICAL_METRIC_NAME: _compute_aggregate_mae_mean(summary_row),
        }
    return metric_entry_map


def update_from_retune(
    branch_name: str,
    registry_path: Path,
    best_parameter_summary_path: Path,
    cross_validation_summary_path: Path | None,
) -> int:

    """Update the YAML registry from one retune artifact pair."""

    # Resolve The Paired Retune Summaries Before Touching The Registry.
    resolved_cross_validation_summary_path = (
        cross_validation_summary_path
        if cross_validation_summary_path is not None
        else _build_cross_validation_path(best_parameter_summary_path)
    )
    if not best_parameter_summary_path.exists():
        raise FileNotFoundError(f"Missing best-parameter summary: {best_parameter_summary_path}")
    if not resolved_cross_validation_summary_path.exists():
        raise FileNotFoundError(
            f"Missing cross-validation summary: {resolved_cross_validation_summary_path}"
        )

    best_parameter_dataframe = _read_best_parameter_dataframe(best_parameter_summary_path)
    cross_validation_dataframe = _read_cross_validation_dataframe(resolved_cross_validation_summary_path)
    metric_entry_map = _build_metric_entry_map(cross_validation_dataframe)
    registry_payload = _load_registry(registry_path)
    branch_payload = registry_payload["branches"].setdefault(branch_name.lower(), {})

    # Compare Each Family Entry Against The Stored Canonical Metric Before Updating.
    updated_family_code_list: list[str] = []
    skipped_family_code_list: list[str] = []
    updated_at_string = _utc_now_string()
    for _, summary_row in best_parameter_dataframe.iterrows():
        summary_family_code = str(summary_row["0_method"]).strip()
        family_code = _normalize_family_code(summary_family_code)
        if family_code not in metric_entry_map:
            raise ValueError(f"Missing cross-validation metrics for family {family_code}")

        new_metric_value = metric_entry_map[family_code][CANONICAL_METRIC_NAME]
        current_entry = branch_payload.get(family_code)
        should_update_entry = (
            current_entry is None
            or float(current_entry[CANONICAL_METRIC_NAME]) > float(new_metric_value)
        )

        if should_update_entry:
            branch_payload[family_code] = {
                "family_code": family_code,
                "summary_family_code": summary_family_code,
                "best_parameters": str(summary_row["best_parameters"]),
                CANONICAL_METRIC_NAME: new_metric_value,
                "metric_name": CANONICAL_METRIC_NAME,
                "source_best_parameter_summary_path": str(best_parameter_summary_path.resolve()),
                "source_cross_validation_summary_path": str(
                    resolved_cross_validation_summary_path.resolve()
                ),
                "updated_at": updated_at_string,
            }
            updated_family_code_list.append(family_code)
        else:
            skipped_family_code_list.append(family_code)

    registry_payload["updated_at"] = updated_at_string
    _write_registry(registry_path, registry_payload)

    # Emit One Compact Operator Summary For The PowerShell Wrapper.
    print(f"[INFO] Registry Path | {registry_path.resolve()}")
    print(f"[INFO] Branch | {branch_name.lower()}")
    print(f"[INFO] Updated Families | {','.join(updated_family_code_list) if updated_family_code_list else 'none'}")
    print(f"[INFO] Skipped Families | {','.join(skipped_family_code_list) if skipped_family_code_list else 'none'}")
    return 0


def materialize_summary(
    branch_name: str,
    registry_path: Path,
    families_argument: str,
    output_summary_path: Path,
) -> int:

    """Write one retune-style summary CSV from the YAML registry."""

    # Resolve The Requested Family Surface Before Writing Any Output.
    requested_family_code_list = _parse_family_list(families_argument)
    registry_payload = _load_registry(registry_path)
    branch_payload = registry_payload["branches"].get(branch_name.lower(), {})

    missing_family_code_list = [
        family_code
        for family_code in requested_family_code_list
        if family_code not in branch_payload
    ]
    if missing_family_code_list:
        print(f"[WARNING] Registry Path | {registry_path.resolve()}")
        print(f"[WARNING] Branch | {branch_name.lower()}")
        print(f"[WARNING] Missing Families | {','.join(missing_family_code_list)}")
        return 2

    # Re-Emit The Historical CSV Shape So training_models.py Can Consume It Unchanged.
    materialized_row_list = []
    for family_code in requested_family_code_list:
        family_entry = branch_payload[family_code]
        materialized_row_list.append(
            {
                "0_method": family_entry["summary_family_code"],
                "best_parameters": family_entry["best_parameters"],
            }
        )

    output_summary_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(materialized_row_list).to_csv(
        output_summary_path,
        sep=";",
        decimal=",",
        index=False,
    )

    print(f"[INFO] Registry Path | {registry_path.resolve()}")
    print(f"[INFO] Branch | {branch_name.lower()}")
    print(f"[INFO] Output Summary | {output_summary_path.resolve()}")
    print(f"[INFO] Families | {','.join(requested_family_code_list)}")
    return 0


def _build_argument_parser() -> argparse.ArgumentParser:

    """Build the CLI parser."""

    # Keep The CLI Explicit So The PowerShell Launcher Can Delegate Narrow Tasks.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--registry-path",
        type=Path,
        default=DEFAULT_REGISTRY_PATH,
        help="YAML registry path. Defaults under output/registries/program/.",
    )
    subparser = parser.add_subparsers(dest="command_name", required=True)

    update_parser = subparser.add_parser("update-from-retune")
    update_parser.add_argument("--branch", required=True, help="Branch name: forward or backward.")
    update_parser.add_argument(
        "--best-parameter-summary-path",
        type=Path,
        required=True,
        help="Path to summaryBestParameter+_3.8_allFreq.csv",
    )
    update_parser.add_argument(
        "--cross-validation-summary-path",
        type=Path,
        default=None,
        help="Optional explicit path to summaryCrossValidation+_3.8_allFreq.csv",
    )

    materialize_parser = subparser.add_parser("materialize-summary")
    materialize_parser.add_argument("--branch", required=True, help="Branch name: forward or backward.")
    materialize_parser.add_argument(
        "--families",
        default="",
        help="Optional comma-separated family subset. Defaults to the full paper-reference family set.",
    )
    materialize_parser.add_argument(
        "--output-summary-path",
        type=Path,
        required=True,
        help="Target CSV path to generate.",
    )
    repository_path_support.add_platform_arguments(parser)
    return parser


def main() -> int:

    """Run the CLI."""

    # Dispatch The Narrow Registry Commands.
    parser = _build_argument_parser()
    args = parser.parse_args()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(args)
    )

    if args.command_name == "update-from-retune":
        return update_from_retune(
            branch_name=args.branch,
            registry_path=args.registry_path,
            best_parameter_summary_path=args.best_parameter_summary_path.resolve(),
            cross_validation_summary_path=(
                args.cross_validation_summary_path.resolve()
                if args.cross_validation_summary_path is not None
                else None
            ),
        )

    return materialize_summary(
        branch_name=args.branch,
        registry_path=args.registry_path,
        families_argument=args.families,
        output_summary_path=args.output_summary_path.resolve(),
    )


if __name__ == "__main__":

    raise SystemExit(main())
