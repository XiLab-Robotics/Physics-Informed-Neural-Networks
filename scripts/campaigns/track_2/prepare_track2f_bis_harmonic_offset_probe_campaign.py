"""Prepare the Track 2F-bis harmonic-offset probe campaign package."""

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
CAMPAIGN_NAME = "track2f_bis_harmonic_offset_probe_campaign_2026_06_04"
CAMPAIGN_ROOT = Path(
    "config/training/track2f_bis_harmonic_offset_probe/campaigns/"
    "2026-06-04_track2f_bis_harmonic_offset_probe_campaign"
)
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/track_2/"
    "2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-04/"
    "2026-06-04-21-14-52_track2f_bis_harmonic_offset_probe.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/track_2/run_track2f_bis_harmonic_offset_probe_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/track_2/validate_track2f_bis_harmonic_offset_probe_package.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/track_2/run_track2f_bis_harmonic_offset_probe_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
MODEL_IMPLEMENTATION_PATH = Path("scripts/models/harmonic_residual_offset_network.py")
MODEL_FACTORY_PATH = Path("scripts/models/model_factory.py")
MODEL_INIT_PATH = Path("scripts/models/__init__.py")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME
SOURCE_DATASET_VARIANT_ROOT = Path(
    "config/training/track2f_offset_aware_probe/campaigns/"
    "2026-06-03_track2f_offset_aware_probe_campaign/dataset_variants"
)
RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]

DIRECTION_METADATA_DICTIONARY = {
    "global": {
        "surface": "global",
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
        "run_direction_token": "global",
        "dataset_file_name": "transmission_error_dataset_global.yaml",
    },
    "fw": {
        "surface": "Fw",
        "training_variant": "Fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
        "run_direction_token": "fw",
        "dataset_file_name": "transmission_error_dataset_fw.yaml",
    },
    "bw": {
        "surface": "Bw",
        "training_variant": "Bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
        "run_direction_token": "bw",
        "dataset_file_name": "transmission_error_dataset_bw.yaml",
    },
}


def to_posix_path(path_value: Path) -> str:

    """Convert a repository path to a POSIX-style string."""

    return path_value.as_posix()


def to_windows_path(path_value: Path) -> str:

    """Convert a repository path to a PowerShell-style string."""

    return str(path_value).replace("/", "\\")


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read a YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML payload with stable repository formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")


def validate_no_conflicting_active_campaign() -> None:

    """Stop if another campaign is currently prepared or active."""

    active_state = read_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH)
    active_status = str(active_state.get("status", "")).strip().lower()
    active_campaign_name = str(active_state.get("campaign_name", "")).strip()
    same_campaign_is_prepared = active_status == "prepared" and active_campaign_name == CAMPAIGN_NAME
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        "Cannot prepare Track 2F-bis while another campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )


def copy_dataset_variants() -> list[Path]:

    """Copy the direction-specific dataset variants into the campaign package."""

    dataset_variant_path_list: list[Path] = []
    for direction_metadata in DIRECTION_METADATA_DICTIONARY.values():
        dataset_file_name = str(direction_metadata["dataset_file_name"])
        source_path = PROJECT_PATH / SOURCE_DATASET_VARIANT_ROOT / dataset_file_name
        target_path = PROJECT_PATH / DATASET_VARIANT_ROOT / dataset_file_name
        assert source_path.exists(), f"Missing source dataset variant | {source_path}"
        dataset_payload = read_yaml_file(source_path)
        write_yaml_file(target_path, dataset_payload)
        dataset_variant_path_list.append(DATASET_VARIANT_ROOT / dataset_file_name)
    return dataset_variant_path_list


def build_common_metadata(
    queue_index: int,
    surface_key: str,
    intervention_name: str,
    model_family: str,
) -> dict[str, Any]:

    """Build shared campaign metadata for one queue entry."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    return {
        "campaign_name": CAMPAIGN_NAME,
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "phase_name": "track2f_bis_harmonic_offset_probe_training",
        "campaign_config_id": model_family,
        "queue_index": queue_index,
        "intervention": intervention_name,
        "training_variant": direction_metadata["training_variant"],
        "direction_scope_label": direction_metadata["direction_scope_label"],
        "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
        "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
        "runtime_input_contract": "current point state plus supported short causal sequence history only",
        "promotion_rule": "Candidate must return through official Track 2 curve-first verification.",
    }


def build_base_dataset_config() -> dict[str, Any]:

    """Build the shared sequence dataset config for Track 2F-bis entries."""

    return {
        "curve_batch_size": 2,
        "point_stride": 1,
        "maximum_points_per_curve": None,
        "collate_mode": "sequence",
        "sequence_length": 33,
        "sequence_stride": 4,
        "sequence_target_position": "center",
        "maximum_sequences_per_curve": 192,
        "num_workers": 8,
        "pin_memory": True,
    }


def build_base_training_config() -> dict[str, Any]:

    """Build the shared training config for Track 2F-bis entries."""

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
    }


def build_runtime_config() -> dict[str, Any]:

    """Build the shared runtime config for Track 2F-bis entries."""

    return {
        "accelerator": "auto",
        "devices": "auto",
        "precision": "32",
        "benchmark": True,
        "use_non_blocking_transfer": True,
    }


def build_clean_control_training_config(queue_index: int, surface_key: str) -> dict[str, Any]:

    """Build one clean non-harmonic Track 2F-like control config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    run_direction_token = str(direction_metadata["run_direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    model_family = f"track2f_bis_clean_sequential_residual_offset_{run_direction_token}"
    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": f"te_track2f_bis_clean_residual_offset_{run_direction_token}",
            "model_family": model_family,
            "model_type": "sequential_residual_offset_probe",
        },
        "metadata": {
            **build_common_metadata(
                queue_index=queue_index,
                surface_key=surface_key,
                intervention_name="clean_sequential_residual_offset_control",
                model_family=model_family,
            ),
            "notes": (
                "Track 2F-bis clean non-harmonic control. Final TE prediction is "
                "base_te_prediction + residual_offset_prediction."
            ),
        },
        "dataset": build_base_dataset_config(),
        "model": {
            "input_size": 5,
            "output_size": 1,
            "base_hidden_size": [96, 64],
            "base_activation_name": "GELU",
            "base_dropout_probability": 0.05,
            "base_use_layer_norm": True,
            "offset_hidden_size": 96,
            "offset_num_layers": 2,
            "offset_dropout_probability": 0.10,
            "offset_bidirectional": False,
            "offset_readout_position": "center",
            "offset_scale": 1.0,
        },
        "training": build_base_training_config(),
        "runtime": build_runtime_config(),
    }


def build_harmonic_offset_training_config(queue_index: int, surface_key: str) -> dict[str, Any]:

    """Build one harmonic residual-offset training config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    run_direction_token = str(direction_metadata["run_direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    model_family = f"track2f_bis_harmonic_residual_offset_{run_direction_token}"
    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": f"te_track2f_bis_harmonic_residual_offset_{run_direction_token}",
            "model_family": model_family,
            "model_type": "harmonic_residual_offset_probe",
        },
        "metadata": {
            **build_common_metadata(
                queue_index=queue_index,
                surface_key=surface_key,
                intervention_name="harmonic_residual_offset_probe",
                model_family=model_family,
            ),
            "harmonic_basis": "sparse_rcim",
            "harmonic_index_list": RCIM_HARMONIC_INDEX_LIST,
            "notes": (
                "Track 2F-bis harmonic-offset probe. Final TE prediction is "
                "structured_harmonic_shape_prediction + causal_residual_offset_prediction."
            ),
        },
        "dataset": build_base_dataset_config(),
        "model": {
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
        },
        "training": build_base_training_config(),
        "runtime": build_runtime_config(),
    }


def write_queue_configs() -> list[Path]:

    """Write all six Track 2F-bis queue YAML files."""

    queue_path_list: list[Path] = []
    queue_index = 1
    for surface_key in DIRECTION_METADATA_DICTIONARY:
        queue_file_name = f"{queue_index:02d}_clean_sequential_residual_offset_control_{surface_key}.yaml"
        queue_path = QUEUE_ROOT / queue_file_name
        write_yaml_file(PROJECT_PATH / queue_path, build_clean_control_training_config(queue_index, surface_key))
        queue_path_list.append(queue_path)
        queue_index += 1

    for surface_key in DIRECTION_METADATA_DICTIONARY:
        queue_file_name = f"{queue_index:02d}_harmonic_residual_offset_probe_{surface_key}.yaml"
        queue_path = QUEUE_ROOT / queue_file_name
        write_yaml_file(PROJECT_PATH / queue_path, build_harmonic_offset_training_config(queue_index, surface_key))
        queue_path_list.append(queue_path)
        queue_index += 1

    return queue_path_list


def write_campaign_readme(queue_path_list: list[Path]) -> Path:

    """Write a campaign-local README for the prepared package."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    queue_line_list = [f"- `{to_posix_path(queue_path)}`" for queue_path in queue_path_list]
    readme_text = f"""# Track 2F-Bis Harmonic-Offset Probe Campaign Package

This package materializes the approved Track 2F-bis harmonic-offset probe.

It contains six runnable queue YAML files:

{chr(10).join(queue_line_list)}

## Launch Commands

Preflight validation:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly
```

Local training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1
```

Remote training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote
```
"""
    output_path = PROJECT_PATH / readme_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(readme_text, encoding="utf-8")
    return readme_path


def write_launcher() -> None:

    """Write the Track 2F-bis PowerShell launcher."""

    campaign_config_file_name_list = [
        "01_clean_sequential_residual_offset_control_global.yaml",
        "02_clean_sequential_residual_offset_control_fw.yaml",
        "03_clean_sequential_residual_offset_control_bw.yaml",
        "04_harmonic_residual_offset_probe_global.yaml",
        "05_harmonic_residual_offset_probe_fw.yaml",
        "06_harmonic_residual_offset_probe_bw.yaml",
    ]
    campaign_config_block = "\n".join(f'    "{file_name}"' for file_name in campaign_config_file_name_list)
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
$campaignConfigRoot = "{to_windows_path(QUEUE_ROOT)}"
$validatorPath = "{to_windows_path(VALIDATOR_PATH)}"
$planningReportPath = "{to_windows_path(PLANNING_REPORT_PATH)}"
$queueRoot = "config\\training\\queue"
$script:LastTrack2FBisPythonExitCode = 0
$campaignConfigFileNameList = @(
{campaign_config_block}
)

function Write-Track2FBisStatus {{
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}}

function Invoke-Track2FBisPython {{
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {{
        & $PythonExecutable @ArgumentList
        $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
        return
    }}

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {{
        & python @ArgumentList
        $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
        return
    }}

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
}}

Write-Track2FBisStatus -Label "INFO" -Message ("Campaign: {{0}}" -f $campaignName)
Write-Track2FBisStatus -Label "INFO" -Message ("Runnable queue root: {{0}}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

Write-Track2FBisStatus -Label "STEP" -Message "Validating Track 2F-bis package."
Invoke-Track2FBisPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2FBisPythonExitCode
if ($pythonExitCode -ne 0) {{
    exit $pythonExitCode
}}

if ($PreflightOnly) {{
    Write-Track2FBisStatus -Label "DONE" -Message "Preflight validation completed without launching training."
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
    Write-Track2FBisStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}}

Write-Track2FBisStatus -Label "STEP" -Message "Launching local Track 2F-bis harmonic-offset campaign."
Invoke-Track2FBisPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2FBisPythonExitCode
exit $trainingExitCode
"""
    output_path = PROJECT_PATH / LAUNCHER_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_text, encoding="utf-8")


def write_launcher_note() -> None:

    """Write the operator-facing launcher note."""

    launcher_note_text = """# Track 2F-Bis Harmonic-Offset Probe Campaign Launcher

## Overview

This launcher validates and runs the prepared Track 2F-bis harmonic-offset
probe package.

The package contains six runnable queue YAML files:

- three clean `sequential_residual_offset_probe` control entries;
- three `harmonic_residual_offset_probe` entries with sparse `RCIM` harmonic
  shape and causal residual-offset correction.

Each branch is prepared separately for `global`, `Fw`, and `Bw`.

## Local Preflight

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly
```

## Local Training

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1
```

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -EnqueueOnly
```

## Remote Training

The operator-facing remote command is:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote
```

The `-Remote` path uses the repository-owned remote training sync wrapper and
syncs `scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before
launch.
"""
    output_path = PROJECT_PATH / LAUNCHER_NOTE_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_note_text, encoding="utf-8")


def write_active_campaign_state(
    dataset_variant_path_list: list[Path],
    queue_path_list: list[Path],
    readme_path: Path,
) -> None:

    """Write the persistent active campaign state for Track 2F-bis."""

    launch_command_list = [
        ".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly",
        ".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1",
        ".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote",
    ]
    protected_file_list = [
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
        to_posix_path(PLANNING_REPORT_PATH),
        to_posix_path(MODEL_IMPLEMENTATION_PATH),
        to_posix_path(MODEL_FACTORY_PATH),
        to_posix_path(MODEL_INIT_PATH),
        to_posix_path(LAUNCHER_PATH),
        to_posix_path(VALIDATOR_PATH),
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
        "execution_status": "prepared_for_track2f_bis_harmonic_offset_probe_training",
        "protected_file_list": protected_file_list,
        "queue_config_path_list": [to_posix_path(queue_path) for queue_path in queue_path_list],
        "launch_command_list": launch_command_list,
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def main() -> int:

    """Prepare the Track 2F-bis campaign package."""

    validate_no_conflicting_active_campaign()
    assert (PROJECT_PATH / PLANNING_REPORT_PATH).exists(), f"Missing plan | {PLANNING_REPORT_PATH}"
    assert (PROJECT_PATH / TECHNICAL_DOCUMENT_PATH).exists(), f"Missing doc | {TECHNICAL_DOCUMENT_PATH}"
    assert (PROJECT_PATH / MODEL_IMPLEMENTATION_PATH).exists(), f"Missing model implementation | {MODEL_IMPLEMENTATION_PATH}"

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
    print(".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly")
    print("Local training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1")
    print("Remote training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote")
    return 0


if __name__ == "__main__":
    sys.exit(main())
