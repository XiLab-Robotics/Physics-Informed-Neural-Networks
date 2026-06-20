"""Prepare the Wave 3.3 curve-aware training campaign package."""

from __future__ import annotations

# Import Python Utilities
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Paths
PROJECT_PATH = Path(__file__).resolve().parents[3]
CAMPAIGN_NAME = "track2g_curve_aware_training_campaign_2026_06_08"
CAMPAIGN_ROOT = Path(
    "config/training/track2g_curve_aware_training/campaigns/"
    "2026-06-08_track2g_curve_aware_training_campaign"
)
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
SOURCE_DATASET_VARIANT_ROOT = Path(
    "config/training/track2f_bis_harmonic_offset_probe/campaigns/"
    "2026-06-04_track2f_bis_harmonic_offset_probe_campaign/dataset_variants"
)
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/track_2/"
    "2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-08/"
    "2026-06-08-17-59-03_track2g_curve_aware_training_plan.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/track_2/run_track2g_curve_aware_training_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/track_2/validate_track2g_curve_aware_training_package.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/track_2/run_track2g_curve_aware_training_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME
RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]

DIRECTION_METADATA_DICTIONARY = {
    "global": {
        "surface": "global",
        "direction_token": "global",
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
        "dataset_file_name": "transmission_error_dataset_global.yaml",
    },
    "fw": {
        "surface": "Fw",
        "direction_token": "fw",
        "training_variant": "Fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
        "dataset_file_name": "transmission_error_dataset_fw.yaml",
    },
    "bw": {
        "surface": "Bw",
        "direction_token": "bw",
        "training_variant": "Bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
        "dataset_file_name": "transmission_error_dataset_bw.yaml",
    },
}

LOSS_PROFILE_DICTIONARY = {
    "pointwise_control": {
        "queue_label": "pointwise_control",
        "weights": {"point": 1.0, "centered": 0.0, "offset": 0.0, "amplitude": 0.0, "harmonic": 0.0},
        "notes": "Control profile. Same architecture with normalized pointwise loss only.",
    },
    "raw_centered_shape": {
        "queue_label": "raw_centered_shape",
        "weights": {"point": 1.0, "centered": 0.35, "offset": 0.0, "amplitude": 0.0, "harmonic": 0.15},
        "notes": "Curve-aware profile emphasizing mean-centered waveform shape and sparse non-DC harmonics.",
    },
    "raw_offset": {
        "queue_label": "raw_offset",
        "weights": {"point": 1.0, "centered": 0.0, "offset": 0.45, "amplitude": 0.0, "harmonic": 0.0},
        "notes": "Curve-aware profile emphasizing curve mean / DC offset correction.",
    },
    "full_curve_composite": {
        "queue_label": "full_curve_composite",
        "weights": {"point": 1.0, "centered": 0.25, "offset": 0.35, "amplitude": 0.10, "harmonic": 0.15},
        "notes": "Full composite profile balancing pointwise, centered-shape, offset, amplitude, and sparse harmonic terms.",
    },
}


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML file with stable formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")


def to_posix_path(path_value: Path) -> str:

    """Return a repository-relative path with POSIX separators."""

    return path_value.as_posix()


def validate_no_conflicting_active_campaign() -> None:

    """Stop if another prepared or active campaign is present."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    active_status = str(active_state.get("status", "")).strip().lower()
    active_campaign_name = str(active_state.get("campaign_name", "")).strip()
    same_campaign_is_prepared = active_status == "prepared" and active_campaign_name == CAMPAIGN_NAME
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        "Cannot prepare Wave 3.3 while another campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )


def copy_dataset_variants() -> list[Path]:

    """Copy the direction-specific dataset variants into the campaign root."""

    dataset_variant_path_list: list[Path] = []
    for direction_metadata in DIRECTION_METADATA_DICTIONARY.values():
        dataset_file_name = str(direction_metadata["dataset_file_name"])
        source_path = PROJECT_PATH / SOURCE_DATASET_VARIANT_ROOT / dataset_file_name
        target_path = PROJECT_PATH / DATASET_VARIANT_ROOT / dataset_file_name
        assert source_path.exists(), f"Missing source dataset variant | {source_path}"
        write_yaml_file(target_path, read_yaml_file(source_path))
        dataset_variant_path_list.append(DATASET_VARIANT_ROOT / dataset_file_name)
    return dataset_variant_path_list


def build_base_dataset_config() -> dict[str, Any]:

    """Build the shared sequence dataset config for curve-aware runs."""

    return {
        "curve_batch_size": 2,
        "point_stride": 1,
        "maximum_points_per_curve": None,
        "collate_mode": "sequence",
        "sequence_length": 33,
        "sequence_stride": 4,
        "sequence_target_position": "center",
        "maximum_sequences_per_curve": 192,
        "shuffle_training_batch_elements": False,
        "num_workers": 8,
        "pin_memory": True,
    }


def build_base_model_config() -> dict[str, Any]:

    """Build the shared harmonic residual-offset model config."""

    return {
        "input_size": 5,
        "output_size": 1,
        "harmonic_order": 240,
        "coefficient_mode": "linear_conditioned",
        "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
        "offset_hidden_size": 96,
        "offset_num_layers": 2,
        "offset_dropout_probability": 0.10,
        "offset_bidirectional": False,
        "offset_readout_position": "center",
        "offset_scale": 1.0,
        "freeze_structured_branch": False,
    }


def build_base_training_config(loss_profile_name: str) -> dict[str, Any]:

    """Build the shared training config for one loss profile."""

    loss_profile = LOSS_PROFILE_DICTIONARY[loss_profile_name]
    return {
        "learning_rate": 0.0005,
        "weight_decay": 0.0001,
        "min_epochs": 20,
        "max_epochs": 260,
        "patience": 40,
        "min_delta": 1.0e-05,
        "log_every_n_steps": 1,
        "fast_dev_run": False,
        "deterministic": False,
        "loss": {
            "profile": loss_profile_name,
            "weights": dict(loss_profile["weights"]),
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
        },
    }


def build_runtime_config() -> dict[str, Any]:

    """Build the shared runtime config."""

    return {
        "accelerator": "auto",
        "devices": "auto",
        "precision": "32",
        "benchmark": True,
        "use_non_blocking_transfer": True,
    }


def build_queue_config(queue_index: int, surface_key: str, loss_profile_name: str) -> dict[str, Any]:

    """Build one Wave 3.3 queue config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    direction_token = str(direction_metadata["direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    model_family = f"track2g_curve_aware_harmonic_residual_offset_{loss_profile_name}_{direction_token}"
    run_name = f"te_track2g_curve_aware_{loss_profile_name}_{direction_token}"
    loss_profile = LOSS_PROFILE_DICTIONARY[loss_profile_name]

    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": run_name,
            "model_family": model_family,
            "model_type": "curve_aware_harmonic_residual_offset_probe",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
            "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
            "phase_name": "track2g_curve_aware_training",
            "campaign_config_id": model_family,
            "queue_index": queue_index,
            "intervention": "curve_aware_loss",
            "loss_profile": loss_profile_name,
            "training_variant": direction_metadata["training_variant"],
            "direction_scope_label": direction_metadata["direction_scope_label"],
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
            "runtime_input_contract": "current point state plus supported short causal sequence history only",
            "promotion_rule": "Candidate must return through official TE curve-first verification.",
            "harmonic_basis": "sparse_rcim",
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
            "notes": loss_profile["notes"],
        },
        "dataset": build_base_dataset_config(),
        "model": build_base_model_config(),
        "training": build_base_training_config(loss_profile_name),
        "runtime": build_runtime_config(),
    }


def write_queue_configs() -> list[Path]:

    """Materialize all Wave 3.3 queue configs."""

    queue_path_list: list[Path] = []
    queue_index = 1
    for loss_profile_name in LOSS_PROFILE_DICTIONARY:
        for surface_key in ["global", "fw", "bw"]:
            queue_file_name = f"{queue_index:02d}_{LOSS_PROFILE_DICTIONARY[loss_profile_name]['queue_label']}_{surface_key}.yaml"
            queue_path = QUEUE_ROOT / queue_file_name
            write_yaml_file(PROJECT_PATH / queue_path, build_queue_config(queue_index, surface_key, loss_profile_name))
            queue_path_list.append(queue_path)
            queue_index += 1
    return queue_path_list


def write_campaign_readme(queue_path_list: list[Path]) -> Path:

    """Write the campaign-local README."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    readme_line_list = [
        "# Wave 3.3 Curve-Aware Training Campaign Package",
        "",
        "This package materializes the approved Wave 3.3 curve-aware training",
        "campaign. It contains 12 runnable queue entries: four loss profiles",
        "across `global`, `Fw`, and `Bw` surfaces.",
        "",
        "Runtime input remains point or short-history causal. Curve grouping is",
        "used only for training-loss aggregation and offline verification.",
        "",
        "## Queue Files",
        "",
    ]
    readme_line_list.extend(f"- `{to_posix_path(queue_path)}`" for queue_path in queue_path_list)
    readme_line_list.extend(
        [
            "",
            "## Launch Commands",
            "",
            "```powershell",
            ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly",
            ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1",
            ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -Remote",
            "```",
        ]
    )
    output_path = PROJECT_PATH / readme_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(readme_line_list) + "\n", encoding="utf-8")
    return readme_path


def write_launcher() -> None:

    """Write the operator-facing PowerShell launcher."""

    queue_file_name_list = [
        f"{queue_index:02d}_{LOSS_PROFILE_DICTIONARY[loss_profile_name]['queue_label']}_{surface_key}.yaml"
        for queue_index, (loss_profile_name, surface_key) in enumerate(
            [(loss_profile_name, surface_key) for loss_profile_name in LOSS_PROFILE_DICTIONARY for surface_key in ["global", "fw", "bw"]],
            start=1,
        )
    ]
    queue_file_block = "\n".join(f'    "{queue_file_name}"' for queue_file_name in queue_file_name_list)
    launcher_text = f"""param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$EnqueueOnly,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) {{ $env:PINNS_REMOTE_TRAINING_REPO_PATH }} else {{ "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks" }}),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) {{ $env:PINNS_REMOTE_TRAINING_CONDA_ENV }} else {{ "pinns_env" }})
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\\..\\..")).Path

Set-Location $projectRoot

$campaignName = "{CAMPAIGN_NAME}"
$campaignConfigRoot = "{str(QUEUE_ROOT).replace('/', chr(92))}"
$validatorPath = "{str(VALIDATOR_PATH).replace('/', chr(92))}"
$planningReportPath = "{str(PLANNING_REPORT_PATH).replace('/', chr(92))}"
$queueRoot = "config\\training\\queue"
$script:LastTrack2GPythonExitCode = 0
$campaignConfigFileNameList = @(
{queue_file_block}
)

function Write-Track2GStatus {{
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}}

function Invoke-Track2GPython {{
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {{
        & $PythonExecutable @ArgumentList
        $script:LastTrack2GPythonExitCode = $LASTEXITCODE
        return
    }}

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {{
        & python @ArgumentList
        $script:LastTrack2GPythonExitCode = $LASTEXITCODE
        return
    }}

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2GPythonExitCode = $LASTEXITCODE
}}

Write-Track2GStatus -Label "INFO" -Message ("Campaign: {{0}}" -f $campaignName)
Write-Track2GStatus -Label "INFO" -Message ("Runnable queue root: {{0}}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

Write-Track2GStatus -Label "STEP" -Message "Validating Wave 3.3 package."
Invoke-Track2GPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2GPythonExitCode
if ($pythonExitCode -ne 0) {{
    exit $pythonExitCode
}}

if ($PreflightOnly) {{
    Write-Track2GStatus -Label "DONE" -Message "Preflight validation completed without launching training."
    exit 0
}}

$campaignConfigPathList = $campaignConfigFileNameList | ForEach-Object {{
    Join-Path $campaignConfigRoot $_
}}

foreach ($queueSubdirectoryName in @("pending", "running")) {{
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path -LiteralPath $queueSubdirectoryPath)) {{
        continue
    }}

    foreach ($campaignConfigFileName in $campaignConfigFileNameList) {{
        Get-ChildItem -LiteralPath $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
            Where-Object {{ $_.Name -like "*$campaignConfigFileName" }} |
            Remove-Item -Force
    }}
}}

if ($Remote) {{
    if ($EnqueueOnly) {{
        throw "-EnqueueOnly is supported only for local launcher verification."
    }}

    $remoteLauncherPath = "scripts\\campaigns\\infrastructure\\run_remote_training_campaign.ps1"
    $sourceSyncPathList = @("scripts", "config", "doc", "requirements.txt", "AGENTS.md")

    & $remoteLauncherPath `
        -CampaignConfigPathList $campaignConfigPathList `
        -CampaignName $campaignName `
        -PlanningReportPath $planningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList $sourceSyncPathList
    exit $LASTEXITCODE
}}

$argumentList = @(
    "scripts\\training\\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    $campaignName,
    "--planning-report-path",
    $planningReportPath
)

if ($EnqueueOnly) {{
    $argumentList += "--enqueue-only"
    Write-Track2GStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}}

Write-Track2GStatus -Label "STEP" -Message "Launching local Wave 3.3 curve-aware training campaign."
Invoke-Track2GPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2GPythonExitCode
exit $trainingExitCode
"""
    output_path = PROJECT_PATH / LAUNCHER_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_text, encoding="utf-8")


def write_launcher_note() -> None:

    """Write the launcher documentation note."""

    launcher_note_text = """# Wave 3.3 Curve-Aware Training Campaign Launcher

## Overview

This launcher validates and runs the prepared Wave 3.3 curve-aware training
package.

The package contains 12 runnable queue YAML files: four loss profiles across
`global`, `Fw`, and `Bw` surfaces. Runtime inputs remain causal point or
short-history sequence inputs. Curve grouping is used only for training loss
aggregation and offline verification.

## Local Preflight

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly
```

## Local Training

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1
```

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -EnqueueOnly
```

## Remote Training

The operator-facing remote command is:

```powershell
.\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -Remote
```

The `-Remote` path uses the repository-owned remote training sync wrapper and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before
launch.
"""
    output_path = PROJECT_PATH / LAUNCHER_NOTE_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_note_text, encoding="utf-8")


def write_active_campaign_state(dataset_variant_path_list: list[Path], queue_path_list: list[Path], readme_path: Path) -> None:

    """Write the persistent active campaign state."""

    launch_command_list = [
        ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly",
        ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1",
        ".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -Remote",
    ]
    protected_file_list = [
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
        to_posix_path(PLANNING_REPORT_PATH),
        "scripts/training/transmission_error_regression_module.py",
        "scripts/training/transmission_error_datamodule.py",
        "scripts/training/shared_training_infrastructure.py",
        "scripts/training/train_feedforward_network.py",
        "scripts/training/run_training_campaign.py",
        "scripts/models/model_factory.py",
        to_posix_path(Path(__file__).relative_to(PROJECT_PATH)),
        to_posix_path(VALIDATOR_PATH),
        to_posix_path(LAUNCHER_PATH),
        to_posix_path(LAUNCHER_NOTE_PATH),
        to_posix_path(readme_path),
        *[to_posix_path(dataset_variant_path) for dataset_variant_path in dataset_variant_path_list],
        *[to_posix_path(queue_path) for queue_path in queue_path_list],
    ]
    active_campaign_state = {
        "status": "prepared",
        "campaign_name": CAMPAIGN_NAME,
        "prepared_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "campaign_config_root": to_posix_path(CAMPAIGN_ROOT),
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "execution_status": "prepared_for_track2g_curve_aware_training",
        "protected_file_list": protected_file_list,
        "queue_config_path_list": [to_posix_path(queue_path) for queue_path in queue_path_list],
        "launch_command_list": launch_command_list,
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def main() -> int:

    """Prepare the Wave 3.3 campaign package."""

    validate_no_conflicting_active_campaign()
    assert (PROJECT_PATH / PLANNING_REPORT_PATH).exists(), f"Missing plan | {PLANNING_REPORT_PATH}"
    assert (PROJECT_PATH / TECHNICAL_DOCUMENT_PATH).exists(), f"Missing technical document | {TECHNICAL_DOCUMENT_PATH}"

    dataset_variant_path_list = copy_dataset_variants()
    queue_path_list = write_queue_configs()
    readme_path = write_campaign_readme(queue_path_list)
    write_launcher()
    write_launcher_note()
    write_active_campaign_state(dataset_variant_path_list, queue_path_list, readme_path)

    print(f"Prepared {CAMPAIGN_NAME}")
    print(f"Runnable queue count: {len(queue_path_list)}")
    print(f"Campaign root: {to_posix_path(CAMPAIGN_ROOT)}")
    print("Local preflight command:")
    print(".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -PreflightOnly")
    print("Local training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1")
    print("Remote training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2g_curve_aware_training_campaign.ps1 -Remote")
    return 0


if __name__ == "__main__":
    sys.exit(main())
