"""Prepare the Wave 1 directional retraining campaign package."""

from __future__ import annotations

# Import Python Utilities
import argparse
import sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

# Import Project Utilities
from scripts.tooling import repository_path_support
from scripts.campaigns.infrastructure.directional_training_variant_support import (
    BACKWARD_ONLY_TRAINING_VARIANT,
    FORWARD_ONLY_TRAINING_VARIANT,
    GLOBAL_TRAINING_VARIANT,
    TRAINING_VARIANT_SEQUENCE,
    apply_directional_variant_to_training_config,
    build_dataset_config_for_variant,
    load_yaml_file,
    resolve_variant_specification,
    save_yaml_file,
)

PLANNING_REPORT_RELATIVE_PATH = (
    "doc/reports/campaign_plans/wave1/"
    "2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md"
)
CAMPAIGN_NAME = "wave1_directional_retraining_campaign_2026_05_06_16_07_16"
CAMPAIGN_ROOT = (
    PROJECT_PATH
    / "config"
    / "training"
    / "wave1_directional_retraining"
    / "campaigns"
    / "2026-05-06_wave1_directional_retraining_campaign"
)
QUEUE_CONFIG_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
CANONICAL_DATASET_CONFIG_PATH = (
    PROJECT_PATH / "config" / "datasets" / "transmission_error_dataset.yaml"
)
FAMILY_BEST_REGISTRY_RELATIVE_PATH_MAP = {
    "tree": "output/registries/families/tree/latest_family_best.yaml",
    "residual_harmonic_mlp": (
        "output/registries/families/residual_harmonic_mlp/latest_family_best.yaml"
    ),
    "feedforward": "output/registries/families/feedforward/latest_family_best.yaml",
    "periodic_mlp": "output/registries/families/periodic_mlp/latest_family_best.yaml",
    "harmonic_regression": (
        "output/registries/families/harmonic_regression/latest_family_best.yaml"
    ),
}
CAMPAIGN_FAMILY_ORDER = [
    "tree",
    "residual_harmonic_mlp",
    "feedforward",
    "periodic_mlp",
    "harmonic_regression",
]
VARIANT_FILENAME_TOKEN_MAP = {
    GLOBAL_TRAINING_VARIANT: "global",
    FORWARD_ONLY_TRAINING_VARIANT: "fw",
    BACKWARD_ONLY_TRAINING_VARIANT: "bw",
}


def build_dataset_variant_relative_path(training_variant: str) -> str:

    """Build one repository-relative dataset-config path for a variant."""

    variant_specification = resolve_variant_specification(training_variant)
    dataset_filename = (
        "transmission_error_dataset_"
        f"{variant_specification['dataset_suffix']}.yaml"
    )
    return str(
        (
            Path("config")
            / "training"
            / "wave1_directional_retraining"
            / "campaigns"
            / "2026-05-06_wave1_directional_retraining_campaign"
            / "dataset_variants"
            / dataset_filename
        ).as_posix()
    )


def build_family_source_training_config(base_model_family: str) -> dict:

    """Load the current best training config for one base model family."""

    family_registry_path = PROJECT_PATH / FAMILY_BEST_REGISTRY_RELATIVE_PATH_MAP[base_model_family]
    family_registry_dictionary = load_yaml_file(family_registry_path)
    best_entry_dictionary = family_registry_dictionary.get("best_entry", {})
    assert isinstance(best_entry_dictionary, dict), (
        f"best_entry must be a dictionary | {family_registry_path}"
    )

    output_directory_text = str(best_entry_dictionary.get("output_directory", "")).strip()
    assert output_directory_text, f"Missing output_directory in best_entry | {family_registry_path}"

    source_training_config_path = (
        PROJECT_PATH / output_directory_text / "training_config.yaml"
    )
    return load_yaml_file(source_training_config_path)


def build_campaign_readme_markdown(generated_config_relative_path_list: list[str]) -> str:

    """Build the campaign README text."""

    markdown_line_list = [
        f"# {CAMPAIGN_NAME}",
        "",
        "## Overview",
        "",
        "This campaign package retrains the current Wave 1 family-best baselines",
        "under three explicit data scopes: `global`, `Fw`, and `Bw`.",
        "",
        "## Candidate Count",
        "",
        "- base families: `5`",
        "- variants per family: `3`",
        "- total configs: `15`",
        "",
        "## Generated Queue Configs",
        "",
    ]

    for config_relative_path in generated_config_relative_path_list:
        markdown_line_list.append(f"- `{config_relative_path}`")

    markdown_line_list.extend(
        [
            "",
            "## Notes",
            "",
            "- the active Track 1 campaign state was intentionally left untouched;",
            "- launcher execution still requires explicit user approval of the campaign plan;",
            "- directional identity is written into both config metadata and registry-facing family keys.",
            "",
        ]
    )
    return "\n".join(markdown_line_list)



def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments."""

    argument_parser = argparse.ArgumentParser(description=__doc__)
    repository_path_support.add_platform_arguments(argument_parser)
    return argument_parser.parse_args()

def main() -> None:

    """Prepare the directional Wave 1 retraining package on disk."""

    parsed_arguments = parse_command_line_arguments()
    repository_path_support.set_runtime_platform(
        repository_path_support.resolve_argument_platform(parsed_arguments)
    )

    base_dataset_config = load_yaml_file(CANONICAL_DATASET_CONFIG_PATH)
    generated_config_relative_path_list: list[str] = []

    # Materialize the Shared Dataset Variants Used by all Family Retraining Runs
    for training_variant in TRAINING_VARIANT_SEQUENCE:
        dataset_variant_payload = build_dataset_config_for_variant(
            base_dataset_config,
            training_variant,
        )
        dataset_variant_relative_path = build_dataset_variant_relative_path(training_variant)
        save_yaml_file(
            dataset_variant_payload,
            PROJECT_PATH / dataset_variant_relative_path,
        )

    # Build the 5 x 3 Family-Variant Queue Surface
    queue_index = 1
    for base_model_family in CAMPAIGN_FAMILY_ORDER:
        base_training_config = build_family_source_training_config(base_model_family)
        for training_variant in TRAINING_VARIANT_SEQUENCE:
            variant_filename_token = VARIANT_FILENAME_TOKEN_MAP[training_variant]
            campaign_config_id = f"{base_model_family}_{variant_filename_token}"
            note_suffix = (
                "Directional Wave 1 retraining variant prepared from the current "
                f"`{base_model_family}` family-best source config with `{training_variant}` data scope."
            )
            prepared_training_config = apply_directional_variant_to_training_config(
                base_training_config=base_training_config,
                training_variant=training_variant,
                dataset_config_relative_path=build_dataset_variant_relative_path(training_variant),
                planning_report_relative_path=PLANNING_REPORT_RELATIVE_PATH,
                campaign_name=CAMPAIGN_NAME,
                phase_name="wave1_directional_retraining",
                campaign_config_id=campaign_config_id,
                note_suffix=note_suffix,
            )
            output_filename = (
                f"{queue_index:02d}_{base_model_family}_{variant_filename_token}.yaml"
            )
            output_path = QUEUE_CONFIG_ROOT / output_filename
            save_yaml_file(prepared_training_config, output_path)
            generated_config_relative_path_list.append(
                str(output_path.relative_to(PROJECT_PATH)).replace("\\", "/")
            )
            queue_index += 1

    save_yaml_file(
        {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": PLANNING_REPORT_RELATIVE_PATH,
            "base_family_order": CAMPAIGN_FAMILY_ORDER,
            "variant_order": TRAINING_VARIANT_SEQUENCE,
            "queue_config_relative_path_list": generated_config_relative_path_list,
        },
        CAMPAIGN_ROOT / "campaign_manifest.yaml",
    )
    (CAMPAIGN_ROOT / "README.md").write_text(
        build_campaign_readme_markdown(generated_config_relative_path_list),
        encoding="utf-8",
    )

    print(
        "[DONE] Prepared Wave 1 directional retraining campaign configs | "
        f"{len(generated_config_relative_path_list)}",
        flush=True,
    )
    print(
        f"[DONE] Campaign root | {CAMPAIGN_ROOT.relative_to(PROJECT_PATH)}",
        flush=True,
    )


if __name__ == "__main__":

    main()
