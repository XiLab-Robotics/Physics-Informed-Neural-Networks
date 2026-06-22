"""Refresh TE collage reports with canonical wave-based model names."""

from __future__ import annotations

# Import Python Utilities
import argparse
import re
import shutil
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "analysis"
    / "track2"
    / "best_model_collage_report"
    / "[2026-06-18]"
    / "track2_best_model_collage_report.md"
)

MODEL_FAMILY_RENAME_DICTIONARY = {
    "track1_best": "rcim_model_bank_reproduction_best",
    "sequential_residual_offset_probe": "wave3_1_sequential_residual_offset_probe",
    "track2f_bis_clean_sequential_residual_offset": "wave3_2_clean_sequential_residual_offset",
    "track2f_bis_harmonic_residual_offset": "wave3_2_harmonic_residual_offset",
    "track2g_curve_aware_pointwise_control": "wave3_3_curve_aware_pointwise_control",
    "track2g_curve_aware_raw_centered_shape": "wave3_3_raw_centered_shape_curve_aware",
    "track2g_curve_aware_raw_offset": "wave3_3_raw_offset_curve_aware",
    "track2g_curve_aware_full_curve_composite": "wave3_3_full_curve_composite",
    "track2h_mae_robust": "wave4_1_mae_robust_loss",
    "track2h_smooth_l1_robust": "wave4_1_smooth_l1_robust_loss",
    "track2h_log_cosh_robust": "wave4_1_log_cosh_robust_loss",
    "track2h_quantile_p10_p50_p90": "wave4_2_quantile_p10_p50_p90",
    "track2h_gaussian_nll": "wave4_2_gaussian_nll",
    "track2h_mdn_k2": "wave4_3_mixture_density_k2",
    "track2h_mdn_k3": "wave4_3_mixture_density_k3",
    "track2h_l_gru_offset_residual": "wave4_4_gru_latent_offset_residual",
    "track2h_l_causal_tcn_offset_residual": "wave4_4_causal_tcn_latent_offset_residual",
    "wave3_harmonic_prior_residual_pointwise_control": "wave5_1_harmonic_prior_pointwise_control",
    "wave3_harmonic_prior_residual_smooth_l1_structured": "wave5_1_harmonic_prior_smooth_l1_structured",
}

SOURCE_LABEL_RENAME_DICTIONARY = {
    "rcim_track1": "rcim_model_bank_reproduction",
    "track2f_offset_aware_probe_registry": "wave3_1_offset_aware_probe_registry",
    "track2f_bis_harmonic_offset_probe_registry": "wave3_2_harmonic_offset_probe_registry",
    "track2g_curve_aware_training_registry": "wave3_3_curve_aware_training_registry",
    "track2h_dispersion_aware_modeling_registry": "wave4_1_robust_loss_registry",
    "track2h_quantile_probabilistic_registry": "wave4_2_probabilistic_registry",
    "track2h_mixture_density_heads_registry": "wave4_3_mixture_density_registry",
    "track2h_latent_state_hysteresis_registry": "wave4_4_latent_state_hysteresis_registry",
    "wave3_harmonic_prior_residual_registry": "wave5_1_harmonic_prior_residual_registry",
}

GROUP_TITLE_RENAME_DICTIONARY = {
    "Forward Track2h Mixture Density Heads Registry Models": "Forward Wave 4.3 Mixture Density Models",
    "Backward Track2h Mixture Density Heads Registry Models": "Backward Wave 4.3 Mixture Density Models",
    "Global Track2h Mixture Density Heads Registry Models": "Global Wave 4.3 Mixture Density Models",
    "Forward Track2h Latent State Hysteresis Registry Models": "Forward Wave 4.4 Latent State Hysteresis Models",
    "Backward Track2h Latent State Hysteresis Registry Models": "Backward Wave 4.4 Latent State Hysteresis Models",
    "Global Track2h Latent State Hysteresis Registry Models": "Global Wave 4.4 Latent State Hysteresis Models",
}

ASSET_GROUP_RENAME_DICTIONARY = {
    "forward_track2f": "forward_wave3_1",
    "backward_track2f": "backward_wave3_1",
    "global_track2f": "global_wave3_1",
    "forward_track2f_bis": "forward_wave3_2",
    "backward_track2f_bis": "backward_wave3_2",
    "global_track2f_bis": "global_wave3_2",
    "forward_track2g": "forward_wave3_3",
    "backward_track2g": "backward_wave3_3",
    "global_track2g": "global_wave3_3",
    "forward_track2h": "forward_wave4_1",
    "backward_track2h": "backward_wave4_1",
    "global_track2h": "global_wave4_1",
    "forward_track2h_quantile_probabilistic": "forward_wave4_2",
    "backward_track2h_quantile_probabilistic": "backward_wave4_2",
    "global_track2h_quantile_probabilistic": "global_wave4_2",
    "a_fw_trac_mixt_dens_head_reg_f6ec842d96": "auto_forward_wave4_3_mixture_density_registry",
    "a_bw_trac_mixt_dens_head_reg_18b372da4f": "auto_backward_wave4_3_mixture_density_registry",
    "a_mix_trac_mixt_dens_head_reg_434037e96c": "auto_mixed_wave4_3_mixture_density_registry",
    "a_fw_trac_late_stat_hyst_reg_b9a1d6d37a": "auto_forward_wave4_4_latent_state_hysteresis_registry",
    "a_bw_trac_late_stat_hyst_reg_7a4d528fe8": "auto_backward_wave4_4_latent_state_hysteresis_registry",
    "a_mix_trac_late_stat_hyst_reg_4bc86c3c52": "auto_mixed_wave4_4_latent_state_hysteresis_registry",
    "a_fw_w3_harm_pri_res_reg_ae5ebf52ea": "auto_forward_wave5_1_harmonic_prior_residual_registry",
    "a_bw_w3_harm_pri_res_reg_06ebe1c05e": "auto_backward_wave5_1_harmonic_prior_residual_registry",
    "a_mix_w3_harm_pri_res_reg_66ff2b30f7": "auto_mixed_wave5_1_harmonic_prior_residual_registry",
}

ORDERED_GROUP_TITLE_LIST = [
    "Forward Reference Best Models",
    "Backward Reference Best Models",
    "Forward Wave 1 Family Best Models",
    "Backward Wave 1 Family Best Models",
    "Global Wave 1 Family Best Models",
    "Forward Wave 2.1 Temporal Family Best Models",
    "Backward Wave 2.1 Temporal Family Best Models",
    "Global Wave 2.1 Temporal Family Best Models",
    "Forward Wave 2.3 Residual Harmonic Temporal Models",
    "Backward Wave 2.3 Residual Harmonic Temporal Models",
    "Global Wave 2.3 Residual Harmonic Temporal Models",
    "Forward Wave 3.1 Offset-Aware Probe Models",
    "Backward Wave 3.1 Offset-Aware Probe Models",
    "Global Wave 3.1 Offset-Aware Probe Models",
    "Forward Wave 3.2 Harmonic-Offset Probe Models",
    "Backward Wave 3.2 Harmonic-Offset Probe Models",
    "Global Wave 3.2 Harmonic-Offset Probe Models",
    "Forward Wave 3.3 Curve-Aware Training Models",
    "Backward Wave 3.3 Curve-Aware Training Models",
    "Global Wave 3.3 Curve-Aware Training Models",
    "Forward Wave 4.1 Robust-Loss Models",
    "Backward Wave 4.1 Robust-Loss Models",
    "Global Wave 4.1 Robust-Loss Models",
    "Forward Wave 4.2 Quantile Probabilistic Models",
    "Backward Wave 4.2 Quantile Probabilistic Models",
    "Global Wave 4.2 Quantile Probabilistic Models",
    "Forward Wave 4.3 Mixture Density Models",
    "Backward Wave 4.3 Mixture Density Models",
    "Global Wave 4.3 Mixture Density Models",
    "Forward Wave 4.4 Latent State Hysteresis Models",
    "Backward Wave 4.4 Latent State Hysteresis Models",
    "Global Wave 4.4 Latent State Hysteresis Models",
    "Forward Wave 5.1 Harmonic Prior Residual Registry Models",
    "Backward Wave 5.1 Harmonic Prior Residual Registry Models",
    "Global Wave 5.1 Harmonic Prior Residual Registry Models",
]


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Refresh the current TE collage report with canonical wave-based names.",
    )
    argument_parser.add_argument(
        "--report-path",
        type=Path,
        default=REPORT_PATH,
        help="Markdown report path to refresh in place.",
    )
    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    return build_argument_parser().parse_args()


def format_canonical_candidate_id(candidate_id: str) -> str:

    """Format one candidate id with the canonical model-family prefix."""

    for legacy_suffix, canonical_suffix in [("_Fw", "_fw"), ("_Bw", "_bw"), ("_global", "_global")]:
        if candidate_id.endswith(legacy_suffix):
            candidate_base = candidate_id[: -len(legacy_suffix)]
            canonical_base = MODEL_FAMILY_RENAME_DICTIONARY.get(candidate_base, candidate_base)
            return f"{canonical_base}{canonical_suffix}"

    return MODEL_FAMILY_RENAME_DICTIONARY.get(candidate_id, candidate_id)


def sanitize_name(raw_value: str) -> str:

    """Sanitize one identifier for report asset filenames."""

    sanitized_text = re.sub(r"[^a-zA-Z0-9_\\-]+", "_", raw_value.strip())
    sanitized_text = re.sub(r"_+", "_", sanitized_text)
    return sanitized_text.strip("_").lower()


def apply_text_replacements(markdown_text: str) -> str:

    """Apply canonical naming replacements to report text."""

    replacement_dictionary = {}
    for legacy_base, canonical_base in MODEL_FAMILY_RENAME_DICTIONARY.items():
        for legacy_suffix, canonical_suffix in [("_Fw", "_fw"), ("_Bw", "_bw"), ("_global", "_global")]:
            replacement_dictionary[f"{legacy_base}{legacy_suffix}"] = f"{canonical_base}{canonical_suffix}"
        replacement_dictionary[legacy_base] = canonical_base

    replacement_dictionary.update(SOURCE_LABEL_RENAME_DICTIONARY)
    replacement_dictionary.update(GROUP_TITLE_RENAME_DICTIONARY)

    refreshed_text = markdown_text
    for legacy_text, canonical_text in sorted(
        replacement_dictionary.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        token_pattern = re.compile(
            rf"(?<![A-Za-z0-9_]){re.escape(legacy_text)}(?![A-Za-z0-9_])"
        )
        refreshed_text = token_pattern.sub(canonical_text, refreshed_text)

    refreshed_text = refreshed_text.replace(
        "the current best reference, RCIM Model-Bank Reproduction, Wave 1 directional, and Wave 1\n"
        "global models.",
        "the current best reference, RCIM Model-Bank Reproduction, and wave-based\n"
        "model-development families.",
    )
    refreshed_text = refreshed_text.replace(
        "- global Wave 1 models are shown on two forward and two backward curves;",
        "- global models are shown on two forward and two backward curves;",
    )
    return refreshed_text


def strip_continued_suffix(group_title: str) -> str:

    """Strip generated gallery continuation suffixes."""

    if group_title.endswith(" Continued"):
        return group_title[: -len(" Continued")]
    return re.sub(r" Continued \d+$", "", group_title)


def extract_section_dictionary(
    text_block: str,
    heading_pattern: str,
) -> dict[str, list[str]]:

    """Extract Markdown sections keyed by normalized group title."""

    heading_regex = re.compile(heading_pattern, re.MULTILINE)
    match_list = list(heading_regex.finditer(text_block))
    section_dictionary: dict[str, list[str]] = {}
    for match_index, match in enumerate(match_list):
        section_start = match.start()
        section_end = match_list[match_index + 1].start() if match_index + 1 < len(match_list) else len(text_block)
        section_text = text_block[section_start:section_end].strip()
        group_title = strip_continued_suffix(match.group("title").strip())
        section_dictionary.setdefault(group_title, []).append(section_text)
    return section_dictionary


def rebuild_ordered_report(markdown_text: str) -> str:

    """Rebuild metric and gallery sections in canonical wave order."""

    metrics_heading = "## Metrics Summary"
    gallery_heading = "## Collage Gallery - "
    output_heading = "## Output Artifacts"

    metrics_start = markdown_text.index(metrics_heading)
    gallery_start = markdown_text.index(gallery_heading, metrics_start)
    output_start = markdown_text.index(output_heading, gallery_start)

    pre_metrics_text = markdown_text[: metrics_start + len(metrics_heading)].rstrip()
    metrics_block = markdown_text[metrics_start + len(metrics_heading) : gallery_start]
    gallery_block = markdown_text[gallery_start:output_start]
    output_block = markdown_text[output_start:].strip()

    metrics_section_dictionary = extract_section_dictionary(metrics_block, r"^### (?P<title>.+)$")
    gallery_section_dictionary = extract_section_dictionary(gallery_block, r"^## Collage Gallery - (?P<title>.+)$")

    ordered_metrics_section_list: list[str] = []
    ordered_gallery_section_list: list[str] = []
    for group_title in ORDERED_GROUP_TITLE_LIST:
        ordered_metrics_section_list.extend(metrics_section_dictionary.pop(group_title, []))
        ordered_gallery_section_list.extend(gallery_section_dictionary.pop(group_title, []))

    for remaining_group_title in sorted(metrics_section_dictionary):
        ordered_metrics_section_list.extend(metrics_section_dictionary[remaining_group_title])
    for remaining_group_title in sorted(gallery_section_dictionary):
        ordered_gallery_section_list.extend(gallery_section_dictionary[remaining_group_title])

    return (
        pre_metrics_text
        + "\n\n"
        + "\n\n".join(ordered_metrics_section_list)
        + "\n\n"
        + "\n\n".join(ordered_gallery_section_list)
        + "\n\n"
        + output_block
        + "\n"
    )


def refresh_asset_tree(report_path: Path, refreshed_markdown_text: str) -> None:

    """Copy existing report assets into canonical folders and filenames."""

    report_directory = report_path.parent
    asset_root = report_directory / "assets"
    temporary_asset_root = report_directory / "assets_canonical"
    if temporary_asset_root.exists():
        shutil.rmtree(temporary_asset_root)
    temporary_asset_root.mkdir(parents=True, exist_ok=True)

    original_markdown_text = report_path.read_text(encoding="utf-8")
    asset_path_replacement_dictionary: dict[str, str] = {}
    image_regex = re.compile(
        r"!\[(?P<candidate_id>[^\]]+?) (?:curve-verification|TE Curve Verification Pipeline) collage\]"
        r"\((?P<relative_path>assets/[^)]+\.png)\)"
    )
    for image_match in image_regex.finditer(original_markdown_text):
        legacy_candidate_id = image_match.group("candidate_id")
        source_relative_path = image_match.group("relative_path")
        source_path = report_directory / source_relative_path
        if not source_path.exists():
            continue

        source_group_name = Path(source_relative_path).parts[1]
        canonical_group_name = ASSET_GROUP_RENAME_DICTIONARY.get(source_group_name, source_group_name)
        canonical_candidate_id = format_canonical_candidate_id(legacy_candidate_id)
        canonical_filename = f"{sanitize_name(canonical_candidate_id)}.png"
        target_path = temporary_asset_root / canonical_group_name / canonical_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)
        refreshed_source_relative_path = apply_text_replacements(source_relative_path)
        final_relative_path = target_path.relative_to(report_directory).as_posix().replace(
            "assets_canonical/",
            "assets/",
        )
        asset_path_replacement_dictionary[refreshed_source_relative_path] = final_relative_path

    rewritten_text = refreshed_markdown_text
    for refreshed_source_relative_path, final_relative_path in sorted(
        asset_path_replacement_dictionary.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        rewritten_text = rewritten_text.replace(refreshed_source_relative_path, final_relative_path)

    if asset_root.exists():
        shutil.rmtree(asset_root)
    temporary_asset_root.rename(asset_root)
    report_path.write_text(rewritten_text, encoding="utf-8", newline="\n")


def run_refresh(report_path: Path) -> None:

    """Run the canonical wave-name refresh."""

    resolved_report_path = report_path.resolve()
    assert resolved_report_path.exists(), f"Report path does not exist | {resolved_report_path}"
    markdown_text = resolved_report_path.read_text(encoding="utf-8")
    refreshed_markdown_text = apply_text_replacements(markdown_text)
    refreshed_markdown_text = rebuild_ordered_report(refreshed_markdown_text)
    refresh_asset_tree(resolved_report_path, refreshed_markdown_text)
    print(f"[DONE] Refreshed canonical wave names | {resolved_report_path}")


def main() -> None:

    """Run the command-line entry point."""

    arguments = parse_command_line_arguments()
    run_refresh(arguments.report_path)


if __name__ == "__main__":
    main()
