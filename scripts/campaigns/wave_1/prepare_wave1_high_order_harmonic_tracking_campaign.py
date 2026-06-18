"""Prepare the Wave 1 high-order harmonic tracking campaign package."""

from __future__ import annotations

# Import Python Utilities
import copy, shutil, sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

CAMPAIGN_NAME = "wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01"
CAMPAIGN_ROOT = Path("config/training/wave1_high_order_harmonic_tracking/campaigns/2026-05-19_wave1_high_order_harmonic_tracking_campaign")
SOURCE_CAMPAIGN_ROOT = Path("config/training/wave1_directional_best_hyperparameter_search/campaigns/2026-05-11_wave1_directional_best_hyperparameter_search_campaign")
PLANNING_REPORT_PATH = Path("doc/reports/campaign_plans/wave_1/2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md")
TECHNICAL_DOCUMENT_PATH = Path("doc/technical/2026-05/2026-05-19/2026-05-19-17-32-08_wave1_high_order_harmonic_tracking.md")
LAUNCHER_PATH = Path("scripts/campaigns/wave_1/run_wave1_high_order_harmonic_tracking_campaign.ps1")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/run_wave1_high_order_harmonic_tracking_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns/wave1/high_order_harmonic_tracking") / CAMPAIGN_NAME

HARMONIC_BANK_DICTIONARY = {
    "rcim_sparse": {
        "harmonic_order": 240,
        "harmonic_index_list": [0, 1, 3, 39, 40, 78, 81, 156, 162, 240],
        "description": "RCIM selected sparse harmonic bank",
    },
    "dense240": {
        "harmonic_order": 240,
        "harmonic_index_list": list(range(0, 241)),
        "description": "dense paper-maximum harmonic bank 0..240",
    },
    "dense360": {
        "harmonic_order": 360,
        "harmonic_index_list": list(range(0, 361)),
        "description": "extended dense harmonic bank 0..360",
    },
}

MODEL_SCOPE_SOURCE_FILE_DICTIONARY = {
    "harmonic_regression": {
        "global": "harmonic_regression.yaml",
        "fw": "harmonic_regression_fw.yaml",
        "bw": "harmonic_regression_bw.yaml",
    },
    "residual_harmonic_mlp": {
        "global": "residual_harmonic_mlp.yaml",
        "fw": "residual_harmonic_mlp_fw.yaml",
        "bw": "residual_harmonic_mlp_bw.yaml",
    },
}

SCOPE_LABEL_DICTIONARY = {
    "global": "global",
    "fw": "Fw",
    "bw": "Bw",
}

def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML payload with stable repository formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")

def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload

def build_run_name(model_type: str, scope_key: str, bank_key: str) -> str:

    """Build a compact campaign run name."""

    if model_type == "harmonic_regression":
        model_token = "harmonic"
    else:
        model_token = "residual_harmonic"

    scope_label = SCOPE_LABEL_DICTIONARY[scope_key]
    return f"te_{model_token}_{bank_key}_tracking_{scope_label}"

def build_campaign_config(
    source_config: dict[str, Any],
    model_type: str,
    scope_key: str,
    bank_key: str,
    bank_config: dict[str, Any],
    config_index: int,
) -> dict[str, Any]:

    """Create one high-order harmonic tracking campaign configuration."""

    campaign_config = copy.deepcopy(source_config)
    run_name = build_run_name(model_type, scope_key, bank_key)
    campaign_config_id = f"{model_type}_{scope_key}_{bank_key}"
    bank_description = str(bank_config["description"])

    # Update Path And Experiment Identity
    dataset_variant_file_name = Path(str(campaign_config["paths"]["dataset_config_path"])).name
    campaign_config["paths"]["dataset_config_path"] = str(CAMPAIGN_ROOT / "dataset_variants" / dataset_variant_file_name).replace("\\", "/")
    campaign_config["paths"]["output_root"] = f"output/training_runs/{campaign_config['experiment']['model_family']}"
    campaign_config["experiment"]["run_name"] = run_name

    # Update Campaign Metadata
    metadata_config = campaign_config.setdefault("metadata", {})
    metadata_config["campaign_name"] = CAMPAIGN_NAME
    metadata_config["planning_report_path"] = str(PLANNING_REPORT_PATH).replace("\\", "/")
    metadata_config["technical_document_path"] = str(TECHNICAL_DOCUMENT_PATH).replace("\\", "/")
    metadata_config["phase_name"] = "wave1_high_order_harmonic_tracking"
    metadata_config["campaign_config_id"] = campaign_config_id
    metadata_config["harmonic_bank_name"] = bank_key
    metadata_config["harmonic_bank_description"] = bank_description
    metadata_config["notes"] = (
        f"Wave 1 high-order harmonic tracking follow-up | {bank_description} | "
        f"model={model_type} | scope={scope_key}. Baseline comparison uses existing Wave 1 "
        "directional best-hyperparameter results."
    )
    metadata_config.pop("output_run_name", None)
    metadata_config.pop("run_instance_id", None)

    # Update Harmonic Basis
    campaign_config["model"]["harmonic_order"] = int(bank_config["harmonic_order"])
    campaign_config["model"]["harmonic_index_list"] = list(bank_config["harmonic_index_list"])

    # Keep Dense Runs Conservative Enough For First-Pass Campaign Execution
    if bank_key.startswith("dense"):
        campaign_config["training"]["patience"] = min(int(campaign_config["training"]["patience"]), 25)

    campaign_config["metadata"]["queue_index"] = config_index
    return campaign_config

def build_queue_config_file_name(config_index: int, model_type: str, scope_key: str, bank_key: str) -> str:

    """Build one stable queue configuration filename."""

    model_token = model_type.replace("_mlp", "")
    return f"{config_index:02d}_{model_token}_{scope_key}_{bank_key}.yaml"

def write_launcher(queue_file_name_list: list[str]) -> None:

    """Write the PowerShell launcher for the prepared campaign."""

    queue_file_literal = "\n".join(f'    "{queue_file_name}"' for queue_file_name in queue_file_name_list)
    launcher_text = f"""param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\\..\\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "{str(CAMPAIGN_ROOT / "queue").replace("/", "\\")}"
$planningReportPath = "{str(PLANNING_REPORT_PATH).replace("/", "\\")}"
$queueRoot = "config\\training\\queue"

$campaignConfigFileNameList = @(
{queue_file_literal}
)

foreach ($queueSubdirectoryName in @("pending", "running")) {{
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path $queueSubdirectoryPath)) {{
        continue
    }}

    foreach ($campaignConfigFileName in $campaignConfigFileNameList) {{
        Get-ChildItem -Path $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
            Where-Object {{ $_.Name -like "*$campaignConfigFileName" }} |
            Remove-Item -Force
    }}
}}

$campaignConfigPathList = $campaignConfigFileNameList | ForEach-Object {{
    Join-Path $campaignConfigRoot $_
}}

$argumentList = @(
    "scripts\\training\\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    "{CAMPAIGN_NAME}",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
"""
    LAUNCHER_PATH.parent.mkdir(parents=True, exist_ok=True)
    LAUNCHER_PATH.write_text(launcher_text, encoding="utf-8")

def write_launcher_note() -> None:

    """Write the launcher usage note."""

    launcher_note_text = f"""# Wave 1 High-Order Harmonic Tracking Campaign Launcher

## Overview

This launcher runs the approved `Wave 1` high-order harmonic tracking package.
The package compares new harmonic bases for `harmonic_regression` and
`residual_harmonic_mlp` across `global`, `Fw`, and `Bw` direction scopes.

It does not launch `Track 1` paper-faithful workflows and does not change model
archives directly. Promotion remains a later closeout decision after scalar and
curve-level review.

## Campaign Package

Prepared campaign root:

- `{str(CAMPAIGN_ROOT).replace("\\", "/")}`

Prepared queue count:

- `18` YAML files

Harmonic banks:

- `rcim_sparse`: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- `dense240`: `0..240`
- `dense360`: `0..360`

## Planning Report

This launcher is tied to:

- `{str(PLANNING_REPORT_PATH).replace("\\", "/")}`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\\scripts\\campaigns\\wave1\\run_wave1_high_order_harmonic_tracking_campaign.ps1
```

Optional Python executable override:

```powershell
.\\scripts\\campaigns\\wave1\\run_wave1_high_order_harmonic_tracking_campaign.ps1 -PythonExecutable python
```

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `{str(CAMPAIGN_OUTPUT_DIRECTORY).replace("\\", "/")}`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.
"""
    LAUNCHER_NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    LAUNCHER_NOTE_PATH.write_text(launcher_note_text, encoding="utf-8")

def write_campaign_readme(queue_file_name_list: list[str]) -> None:

    """Write a short campaign-root README."""

    queue_listing = "\n".join(f"- `queue/{queue_file_name}`" for queue_file_name in queue_file_name_list)
    readme_text = f"""# Wave 1 High-Order Harmonic Tracking Campaign

Prepared campaign package for:

- `{CAMPAIGN_NAME}`

Planning report:

- `{str(PLANNING_REPORT_PATH).replace("\\", "/")}`

Queue files:

{queue_listing}
"""
    write_path = CAMPAIGN_ROOT / "README.md"
    write_path.write_text(readme_text, encoding="utf-8")

def write_active_campaign_state(queue_config_relative_path_list: list[str], protected_file_relative_path_list: list[str]) -> None:

    """Write the active campaign state for the prepared package."""

    active_campaign_state = {
        "status": "prepared",
        "campaign_name": CAMPAIGN_NAME,
        "prepared_at": "2026-05-19T17:40:01+02:00",
        "planning_report_path": str(PLANNING_REPORT_PATH).replace("\\", "/"),
        "technical_document_path": str(TECHNICAL_DOCUMENT_PATH).replace("\\", "/"),
        "campaign_config_root": str(CAMPAIGN_ROOT).replace("\\", "/"),
        "campaign_output_directory": str(CAMPAIGN_OUTPUT_DIRECTORY).replace("\\", "/"),
        "protected_file_list": protected_file_relative_path_list,
        "queue_config_path_list": queue_config_relative_path_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\wave1\\run_wave1_high_order_harmonic_tracking_campaign.ps1",
        ],
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)

def prepare_campaign_package() -> None:

    """Prepare the complete high-order harmonic tracking campaign package."""

    absolute_campaign_root = PROJECT_PATH / CAMPAIGN_ROOT
    absolute_queue_root = absolute_campaign_root / "queue"
    absolute_source_config_root = PROJECT_PATH / SOURCE_CAMPAIGN_ROOT / "source_training_configs"

    # Reset Generated Campaign Folder
    if absolute_campaign_root.exists():
        shutil.rmtree(absolute_campaign_root)
    absolute_queue_root.mkdir(parents=True, exist_ok=True)

    # Copy Dataset Variants For Campaign Self-Containment
    shutil.copytree(
        PROJECT_PATH / SOURCE_CAMPAIGN_ROOT / "dataset_variants",
        absolute_campaign_root / "dataset_variants",
    )

    queue_file_name_list: list[str] = []
    queue_config_relative_path_list: list[str] = []
    config_index = 1

    # Materialize Queue Configurations
    for model_type, scope_source_dictionary in MODEL_SCOPE_SOURCE_FILE_DICTIONARY.items():
        for scope_key, source_file_name in scope_source_dictionary.items():
            source_config = read_yaml_file(absolute_source_config_root / source_file_name)
            for bank_key, bank_config in HARMONIC_BANK_DICTIONARY.items():
                campaign_config = build_campaign_config(
                    source_config=source_config,
                    model_type=model_type,
                    scope_key=scope_key,
                    bank_key=bank_key,
                    bank_config=bank_config,
                    config_index=config_index,
                )
                config_file_name = build_queue_config_file_name(config_index, model_type, scope_key, bank_key)
                queue_config_path = absolute_queue_root / config_file_name
                write_yaml_file(queue_config_path, campaign_config)
                queue_file_name_list.append(config_file_name)
                queue_config_relative_path_list.append(str(CAMPAIGN_ROOT / "queue" / config_file_name).replace("\\", "/"))
                config_index += 1

    # Write Launcher And Documentation
    write_launcher(queue_file_name_list)
    write_launcher_note()
    write_campaign_readme(queue_file_name_list)

    protected_file_relative_path_list = [
        str(CAMPAIGN_ROOT / "README.md").replace("\\", "/"),
        str(CAMPAIGN_ROOT / "dataset_variants" / "transmission_error_dataset_global.yaml").replace("\\", "/"),
        str(CAMPAIGN_ROOT / "dataset_variants" / "transmission_error_dataset_fw.yaml").replace("\\", "/"),
        str(CAMPAIGN_ROOT / "dataset_variants" / "transmission_error_dataset_bw.yaml").replace("\\", "/"),
        *queue_config_relative_path_list,
        str(LAUNCHER_PATH).replace("\\", "/"),
        str(LAUNCHER_NOTE_PATH).replace("\\", "/"),
        str(PLANNING_REPORT_PATH).replace("\\", "/"),
        str(TECHNICAL_DOCUMENT_PATH).replace("\\", "/"),
    ]
    write_active_campaign_state(queue_config_relative_path_list, protected_file_relative_path_list)

    print(f"[DONE] Prepared campaign package | {CAMPAIGN_NAME}")
    print(f"[INFO] Queue configs | {len(queue_config_relative_path_list)}")
    print("[INFO] Launch command | .\\scripts\\campaigns\\wave1\\run_wave1_high_order_harmonic_tracking_campaign.ps1")

def main() -> int:

    """Run campaign preparation."""

    prepare_campaign_package()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
