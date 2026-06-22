"""Refresh TE overlay reports with canonical wave-based model names."""

from __future__ import annotations

# Import Python Utilities
import argparse
import shutil
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Report Refresh Utilities
from scripts.reports.analysis.refresh_track2_collage_canonical_wave_names import (
    apply_text_replacements,
)

REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "multi_model_curve_comparison_report"
    / "[2026-06-18]"
    / "track2_multi_model_curve_comparison_report.md"
)

COMPARISON_ASSET_RENAME_DICTIONARY = {
    "forward_track2f.png": "forward_wave3_1.png",
    "backward_track2f.png": "backward_wave3_1.png",
    "forward_track2f_bis.png": "forward_wave3_2.png",
    "backward_track2f_bis.png": "backward_wave3_2.png",
    "forward_track2g.png": "forward_wave3_3.png",
    "backward_track2g.png": "backward_wave3_3.png",
    "forward_track2h.png": "forward_wave4_1.png",
    "backward_track2h.png": "backward_wave4_1.png",
    "forward_track2h_qp.png": "forward_wave4_2.png",
    "backward_track2h_qp.png": "backward_wave4_2.png",
    "a_fw_trac_mixt_dens_head_reg_f6ec842d96.png": "forward_wave4_3_mixture_density.png",
    "a_bw_trac_mixt_dens_head_reg_18b372da4f.png": "backward_wave4_3_mixture_density.png",
    "a_fw_trac_late_stat_hyst_reg_b9a1d6d37a.png": "forward_wave4_4_latent_state_hysteresis.png",
    "a_bw_trac_late_stat_hyst_reg_7a4d528fe8.png": "backward_wave4_4_latent_state_hysteresis.png",
    "a_fw_w3_harm_pri_res_reg_ae5ebf52ea.png": "forward_wave5_1_harmonic_prior_residual.png",
    "a_bw_w3_harm_pri_res_reg_06ebe1c05e.png": "backward_wave5_1_harmonic_prior_residual.png",
    "forward_reference_tree_track2f.png": "forward_reference_tree_wave3_1.png",
    "backward_reference_tree_track2f.png": "backward_reference_tree_wave3_1.png",
    "forward_reference_tree_track2g.png": "forward_reference_tree_wave3_3.png",
    "backward_reference_tree_track2g.png": "backward_reference_tree_wave3_3.png",
    "forward_reference_tree_track2h.png": "forward_reference_tree_wave4_1.png",
    "backward_reference_tree_track2h.png": "backward_reference_tree_wave4_1.png",
}

TITLE_RENAME_DICTIONARY = {
    "Forward Track2h Mixture Density Heads Registry Overlay": "Forward Wave 4.3 Mixture Density Overlay",
    "Backward Track2h Mixture Density Heads Registry Overlay": "Backward Wave 4.3 Mixture Density Overlay",
    "Forward Track2h Latent State Hysteresis Registry Overlay": "Forward Wave 4.4 Latent State Hysteresis Overlay",
    "Backward Track2h Latent State Hysteresis Registry Overlay": "Backward Wave 4.4 Latent State Hysteresis Overlay",
}


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Refresh the current TE overlay report with canonical wave-based names.",
    )
    argument_parser.add_argument(
        "--report-path",
        type=Path,
        default=REPORT_PATH,
        help="Markdown overlay report path to refresh in place.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def refresh_comparison_assets(report_path: Path, report_text: str) -> str:

    """Rename linked comparison assets and update Markdown references."""

    report_directory = report_path.parent
    comparison_asset_directory = report_directory / "assets" / "comparisons"
    temporary_asset_directory = report_directory / "assets" / "comparisons_canonical"
    if temporary_asset_directory.exists():
        shutil.rmtree(temporary_asset_directory)
    temporary_asset_directory.mkdir(parents=True, exist_ok=True)

    rewritten_text = report_text
    for source_filename, target_filename in COMPARISON_ASSET_RENAME_DICTIONARY.items():
        source_path = comparison_asset_directory / source_filename
        if not source_path.exists():
            continue
        target_path = temporary_asset_directory / target_filename
        shutil.copyfile(source_path, target_path)
        rewritten_text = rewritten_text.replace(
            f"assets/comparisons/{source_filename}",
            f"assets/comparisons/{target_filename}",
        )

    for source_path in comparison_asset_directory.glob("*.png"):
        if source_path.name in COMPARISON_ASSET_RENAME_DICTIONARY:
            continue
        shutil.copyfile(source_path, temporary_asset_directory / source_path.name)

    shutil.rmtree(comparison_asset_directory)
    temporary_asset_directory.rename(comparison_asset_directory)
    return rewritten_text


def run_refresh(report_path: Path) -> None:

    """Run the canonical wave-name refresh."""

    resolved_report_path = report_path.resolve()
    assert resolved_report_path.exists(), f"Report path does not exist | {resolved_report_path}"
    report_text = resolved_report_path.read_text(encoding="utf-8")
    report_text = apply_text_replacements(report_text)
    for legacy_title, canonical_title in TITLE_RENAME_DICTIONARY.items():
        report_text = report_text.replace(legacy_title, canonical_title)
    report_text = refresh_comparison_assets(resolved_report_path, report_text)
    resolved_report_path.write_text(report_text, encoding="utf-8", newline="\n")
    print(f"[DONE] Refreshed canonical overlay names | {resolved_report_path}")


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_command_line_arguments()
    run_refresh(arguments.report_path)


if __name__ == "__main__":
    main()
