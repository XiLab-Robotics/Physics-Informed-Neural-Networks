"""Build the Wave 4A MMT equation diagnostic report."""

from __future__ import annotations

# Import Standard Libraries
import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Numerical Libraries
import numpy as np
import yaml

# Import Project Utilities
from scripts.models.wave4_mmt_diagnostic_adapter import Wave4MMTDiagnosticAdapter


DEFAULT_OUTPUT_ROOT = PROJECT_PATH / "output" / "validation_checks" / "wave4_mmt_equation_diagnostic"
DEFAULT_REPORT_TOPIC_ROOT = PROJECT_PATH / "doc" / "reports" / "analysis" / "wave4" / "mmt_equation_diagnostic"
REPORT_FILENAME = "wave4a_mmt_equation_diagnostic.md"
CURVE_TABLE_FILENAME = "wave4a_mmt_demo_curve.csv"
HARMONIC_TABLE_FILENAME = "wave4a_mmt_harmonic_summary.csv"
SUMMARY_FILENAME = "wave4a_mmt_equation_diagnostic_summary.yaml"
SUSPICIOUS_HARMONIC_INDEX_LIST = [0, 1, 156, 162, 240]


def format_float(value: float) -> str:

    """Format one float for stable CSV or Markdown output."""

    return f"{float(value):.9f}"


def write_csv(output_path: Path, row_list: list[dict[str, Any]]) -> None:

    """Write dictionaries to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    assert row_list, f"No rows available for CSV output | {output_path}"
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(row_list[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(row_list)


def build_curve_rows(angle_rad: np.ndarray, rte_rad: np.ndarray) -> list[dict[str, Any]]:

    """Build point-wise MMT demonstration curve rows."""

    rte_arcsec = np.asarray(rte_rad, dtype=float) * 206264.80624709636
    return [
        {
            "sample_index": int(index),
            "angle_rad": format_float(float(angle_value)),
            "rte_rad": format_float(float(rte_value)),
            "rte_arcsec": format_float(float(rte_arcsec[index])),
        }
        for index, (angle_value, rte_value) in enumerate(zip(angle_rad, rte_rad, strict=True))
    ]


def compute_harmonic_rows(rte_rad: np.ndarray, maximum_harmonic: int | None = None) -> list[dict[str, Any]]:

    """Compute harmonic amplitude rows for the MMT demonstration curve."""

    rte_arcsec = np.asarray(rte_rad, dtype=float) * 206264.80624709636
    centered_rte_arcsec = rte_arcsec - float(np.mean(rte_arcsec))
    spectrum = np.fft.rfft(centered_rte_arcsec)
    amplitude = 2.0 * np.abs(spectrum) / centered_rte_arcsec.size
    maximum_index = len(amplitude) - 1 if maximum_harmonic is None else min(int(maximum_harmonic), len(amplitude) - 1)

    row_list: list[dict[str, Any]] = [
        {
            "harmonic_index": 0,
            "amplitude_arcsec": format_float(abs(float(np.mean(rte_arcsec)))),
            "is_suspicious_track2_harmonic": True,
            "is_top_demo_harmonic": False,
        }
    ]
    top_index_set = set((np.argsort(amplitude[1:])[-12:][::-1] + 1).tolist())
    for harmonic_index in range(1, maximum_index + 1):
        row_list.append(
            {
                "harmonic_index": int(harmonic_index),
                "amplitude_arcsec": format_float(float(amplitude[harmonic_index])),
                "is_suspicious_track2_harmonic": harmonic_index in SUSPICIOUS_HARMONIC_INDEX_LIST,
                "is_top_demo_harmonic": harmonic_index in top_index_set,
            }
        )
    return row_list


def build_report_lines(
    run_id: str,
    summary_dictionary: dict[str, Any],
    harmonic_row_list: list[dict[str, Any]],
    output_directory: Path,
) -> list[str]:

    """Build the Wave 4A diagnostic Markdown report."""

    top_rows = sorted(
        [row for row in harmonic_row_list if bool(row["is_top_demo_harmonic"])],
        key=lambda row: float(row["amplitude_arcsec"]),
        reverse=True,
    )[:12]
    suspicious_rows = [
        row
        for row in harmonic_row_list
        if int(row["harmonic_index"]) in SUSPICIOUS_HARMONIC_INDEX_LIST
    ]

    report_lines = [
        "# Wave 4A MMT Equation Diagnostic",
        "",
        "## Overview",
        "",
        (
            "This diagnostic runs the repository-owned `MMT_TEModeling` equation-chain "
            "demonstration through the `Wave4MMTDiagnosticAdapter` and summarizes its "
            "mean, peak-to-peak value, and harmonic content."
        ),
        "",
        "This is a diagnostic-only artifact. It is not a PINN loss, not a calibrated",
        "analytical baseline, and not a training campaign result.",
        "",
        "## Summary",
        "",
        "| Field | Value |",
        "| --- | ---: |",
        f"| Run ID | `{run_id}` |",
        f"| Sample Count | {summary_dictionary['sample_count']} |",
        f"| RTE Mean [arcsec] | {float(summary_dictionary['rte_arcsec_mean']):.6f} |",
        f"| RTE Peak To Peak [arcsec] | {float(summary_dictionary['rte_arcsec_peak_to_peak']):.6f} |",
        f"| Campaign Readiness | `{summary_dictionary['campaign_readiness']}` |",
        "",
        "## Dominant Demonstration Harmonics",
        "",
        "| Harmonic | Amplitude [arcsec] | Track 2 Suspicious Group |",
        "| ---: | ---: | --- |",
    ]

    for row in top_rows:
        report_lines.append(
            f"| {row['harmonic_index']} | {float(row['amplitude_arcsec']):.6f} | "
            f"{'yes' if bool(row['is_suspicious_track2_harmonic']) else 'no'} |"
        )

    report_lines.extend(
        [
            "",
            "## Track 2 Suspicious Harmonic Probe",
            "",
            "| Harmonic | Amplitude [arcsec] | Top Demonstration Harmonic |",
            "| ---: | ---: | --- |",
        ]
    )

    for row in suspicious_rows:
        report_lines.append(
            f"| {row['harmonic_index']} | {float(row['amplitude_arcsec']):.6f} | "
            f"{'yes' if bool(row['is_top_demo_harmonic']) else 'no'} |"
        )

    report_lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "The MMT equation chain is now callable as a diagnostic and can produce "
                "auditable harmonic signatures. This is useful for deciding whether MMT "
                "terms should become diagnostic-only, feature-generator, calibrated "
                "baseline, or weak-loss material."
            ),
            (
                "The current demonstration is not dataset-calibrated. Any relationship "
                "between the displayed harmonic amplitudes and Track 2 failure modes is "
                "therefore a hypothesis, not evidence of causality."
            ),
            (
                "The next Wave 4A requirement remains the parameter inventory: which "
                "MMT inputs are known from the rig, fixed by reducer geometry, calibrated "
                "on training conditions only, or unavailable."
            ),
            "",
            "## Machine-Readable Artifacts",
            "",
            f"- `{(output_directory / CURVE_TABLE_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / HARMONIC_TABLE_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            f"- `{(output_directory / SUMMARY_FILENAME).relative_to(PROJECT_PATH).as_posix()}`",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py",
            "```",
        ]
    )
    return report_lines


def parse_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-topic-root", type=Path, default=DEFAULT_REPORT_TOPIC_ROOT)
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument("--report-date", type=str, default="")
    parser.add_argument("--sample-count", type=int, default=720)
    parser.add_argument("--top-harmonic-count", type=int, default=12)
    return parser.parse_args()


def main() -> None:

    """Build the Wave 4A MMT diagnostic report."""

    args = parse_arguments()
    run_id = args.run_id if args.run_id else f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}__wave4a_mmt_equation_diagnostic"
    report_date = args.report_date if args.report_date else datetime.now().strftime("%Y-%m-%d")
    output_directory = args.output_root / run_id
    report_directory = args.report_topic_root / f"[{report_date}]"
    report_path = report_directory / REPORT_FILENAME

    adapter = Wave4MMTDiagnosticAdapter()
    angle_rad, rte_rad = adapter.run_demo_curve(sample_count=args.sample_count)
    summary = adapter.run_demo_summary(sample_count=args.sample_count, top_k=args.top_harmonic_count)
    harmonic_row_list = compute_harmonic_rows(rte_rad)
    curve_row_list = build_curve_rows(angle_rad, rte_rad)
    summary_dictionary = {
        "run_id": run_id,
        "report_path": report_path.relative_to(PROJECT_PATH).as_posix(),
        "sample_count": int(summary.sample_count),
        "rte_arcsec_mean": float(summary.rte_arcsec_mean),
        "rte_arcsec_peak_to_peak": float(summary.rte_arcsec_peak_to_peak),
        "dominant_harmonic_index_list": list(summary.dominant_harmonic_index_list),
        "dominant_harmonic_amplitude_arcsec_list": list(summary.dominant_harmonic_amplitude_arcsec_list),
        "suspicious_track2_harmonic_index_list": list(SUSPICIOUS_HARMONIC_INDEX_LIST),
        "campaign_readiness": summary.campaign_readiness,
        "decision": "diagnostic_only_until_parameter_inventory_and_dataset_calibration",
    }

    write_csv(output_directory / CURVE_TABLE_FILENAME, curve_row_list)
    write_csv(output_directory / HARMONIC_TABLE_FILENAME, harmonic_row_list)
    output_directory.mkdir(parents=True, exist_ok=True)
    with (output_directory / SUMMARY_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(summary_dictionary, output_file, sort_keys=False)

    report_lines = build_report_lines(
        run_id=run_id,
        summary_dictionary=summary_dictionary,
        harmonic_row_list=harmonic_row_list,
        output_directory=output_directory,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="\n") as report_file:
        report_file.write("\n".join(report_lines).rstrip() + "\n")

    print(f"Prepared Wave 4A MMT diagnostic artifacts | {output_directory}")
    print(f"Prepared Markdown report | {report_path}")


if __name__ == "__main__":
    main()
