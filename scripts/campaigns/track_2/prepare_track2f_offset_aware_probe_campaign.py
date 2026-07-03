"""Prepare the Wave 3.1 offset-aware probe campaign package."""

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
CAMPAIGN_NAME = "track2f_offset_aware_probe_campaign_2026_06_03"
CAMPAIGN_ROOT = Path(
    "config/training/track2f_offset_aware_probe/campaigns/"
    "2026-06-03_track2f_offset_aware_probe_campaign"
)
PROBE_DESCRIPTOR_ROOT = CAMPAIGN_ROOT / "probe_descriptors"
QUEUE_ROOT = CAMPAIGN_ROOT / "queue"
DATASET_VARIANT_ROOT = CAMPAIGN_ROOT / "dataset_variants"
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/track_2/"
    "2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-03/"
    "2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md"
)
SEQUENTIAL_PROBE_TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-03/"
    "2026-06-03-18-18-20_track2f_sequential_residual_offset_probe.md"
)
LAUNCHER_FIX_TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-06/2026-06-04/"
    "2026-06-04-11-15-13_track2f_launcher_exit_flow_fix.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.ps1")
VALIDATOR_PATH = Path("scripts/campaigns/track_2/validate_track2f_offset_aware_probe_package.py")
LAUNCHER_NOTE_PATH = Path("doc/scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.md")
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
MODEL_REPORT_PATH = Path("doc/reports/analysis/model_development_waves/wave_2/Track 2F Sequential Residual-Offset Probe Model.md")
CAMPAIGN_OUTPUT_DIRECTORY = Path("output/training_campaigns") / CAMPAIGN_NAME
BASELINE_STATUS_OUTPUT_DIRECTORY = (
    Path("output/validation_checks/track2f_offset_aware_probe")
    / "2026-06-03_track2f_offset_aware_probe_prelaunch"
)
SOURCE_DATASET_VARIANT_ROOT = Path(
    "config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/"
    "2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign/dataset_variants"
)
TRACK2E_RECOMMENDATION_PATH = Path(
    "output/validation_checks/track2e_offset_predictability_feasibility/"
    "2026-06-03-13-28-54__track2e_offset_predictability_feasibility/"
    "track2e_surface_intervention_recommendation.csv"
)

SURFACE_REFERENCE_DICTIONARY = {
    "global": {
        "surface": "global",
        "track2e_reference_candidate": "harmonic_regression_global",
        "direction_scope": "forward_and_backward",
    },
    "fw": {
        "surface": "Fw",
        "track2e_reference_candidate": "LGBM19_Fw",
        "direction_scope": "forward_only",
    },
    "bw": {
        "surface": "Bw",
        "track2e_reference_candidate": "rcim_retuned_XGBM19_Bw",
        "direction_scope": "backward_only",
    },
}
INTERVENTION_DICTIONARY = {
    "posthoc_direction_torque_offset_baseline": {
        "implementation_status": "runnable_posthoc_baseline",
        "role": "non_learned_causal_baseline",
        "launch_guard": "validation_only_no_training_entrypoint_required",
    },
    "sequential_residual_offset_probe": {
        "implementation_status": "runnable_training_entry",
        "role": "second_stage_causal_residual_offset_predictor",
        "launch_guard": "runnable after Wave 3.1 sequential residual-offset model registration",
    },
    "multi_head_shape_offset_probe": {
        "implementation_status": "blocked_until_model_type_implementation",
        "role": "shared_trunk_centered_shape_and_offset_heads",
        "launch_guard": (
            "blocked because scripts/training/run_training_campaign.py has no "
            "multi_head_shape_offset_probe model_type"
        ),
    },
}
DIRECTION_METADATA_DICTIONARY = {
    "global": {
        "training_variant": "global",
        "direction_scope_label": "bidirectional",
        "use_forward_direction": True,
        "use_backward_direction": True,
        "model_family": "sequential_residual_offset_probe",
        "run_direction_token": "global",
        "dataset_file_name": "transmission_error_dataset_global.yaml",
    },
    "fw": {
        "training_variant": "Fw",
        "direction_scope_label": "forward_only",
        "use_forward_direction": True,
        "use_backward_direction": False,
        "model_family": "sequential_residual_offset_probe_fw",
        "run_direction_token": "fw",
        "dataset_file_name": "transmission_error_dataset_fw.yaml",
    },
    "bw": {
        "training_variant": "Bw",
        "direction_scope_label": "backward_only",
        "use_forward_direction": False,
        "use_backward_direction": True,
        "model_family": "sequential_residual_offset_probe_bw",
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
    same_campaign_is_prepared = (
        active_status == "prepared"
        and active_campaign_name == CAMPAIGN_NAME
    )
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        "Cannot prepare Wave 3.1 while another campaign is prepared or active | "
        f"status={active_status} | campaign_name={active_campaign_name}"
    )


def build_probe_descriptor(
    probe_index: int,
    surface_key: str,
    intervention_name: str,
) -> dict[str, Any]:

    """Build one Wave 3.1 probe descriptor."""

    surface_reference = SURFACE_REFERENCE_DICTIONARY[surface_key]
    intervention_reference = INTERVENTION_DICTIONARY[intervention_name]
    probe_id = f"track2f_{surface_key}_{intervention_name}"
    return {
        "schema_version": 1,
        "campaign_name": CAMPAIGN_NAME,
        "probe_index": probe_index,
        "probe_id": probe_id,
        "surface": surface_reference["surface"],
        "surface_key": surface_key,
        "direction_scope": surface_reference["direction_scope"],
        "intervention": intervention_name,
        "intervention_role": intervention_reference["role"],
        "implementation_status": intervention_reference["implementation_status"],
        "launch_guard": intervention_reference["launch_guard"],
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "track2e_reference_candidate": surface_reference["track2e_reference_candidate"],
        "track2e_recommendation_path": to_posix_path(TRACK2E_RECOMMENDATION_PATH),
        "runtime_input_contract": {
            "allowed_inputs": [
                "current point-level operating state",
                "supported short causal history",
                "causal derived features from already observed samples",
                "direction, speed, torque, and oil temperature when runtime-available",
            ],
            "forbidden_inputs": [
                "future TE samples",
                "complete-curve means during inference",
                "full-curve normalization during inference",
                "future-looking smoothing",
            ],
            "validation_only_units": [
                "full TE Curve Verification Pipeline curve raw error",
                "centered-shape error",
                "mean-offset error",
                "amplitude error",
                "harmonic phase error",
            ],
        },
        "promotion_rule": (
            "Candidate cannot be promoted from pointwise MAE/RMSE alone; it must return "
            "through official TE curve-first verification on the matching surface."
        ),
    }


def build_probe_descriptor_file_name(probe_index: int, surface_key: str, intervention_name: str) -> str:

    """Build one stable descriptor filename."""

    return f"{probe_index:02d}_{surface_key}_{intervention_name}.yaml"


def write_probe_descriptors() -> list[Path]:

    """Write all nine Wave 3.1 probe descriptors."""

    descriptor_path_list: list[Path] = []
    probe_index = 1
    for intervention_name in INTERVENTION_DICTIONARY:
        for surface_key in SURFACE_REFERENCE_DICTIONARY:
            descriptor = build_probe_descriptor(probe_index, surface_key, intervention_name)
            descriptor_path = (
                PROBE_DESCRIPTOR_ROOT
                / build_probe_descriptor_file_name(probe_index, surface_key, intervention_name)
            )
            write_yaml_file(PROJECT_PATH / descriptor_path, descriptor)
            descriptor_path_list.append(descriptor_path)
            probe_index += 1
    return descriptor_path_list


def copy_dataset_variants() -> list[Path]:

    """Copy the direction-specific dataset variants into the Wave 3.1 package."""

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


def build_sequential_probe_training_config(queue_index: int, surface_key: str) -> dict[str, Any]:

    """Build one runnable sequential residual-offset training config."""

    direction_metadata = DIRECTION_METADATA_DICTIONARY[surface_key]
    model_family = str(direction_metadata["model_family"])
    run_direction_token = str(direction_metadata["run_direction_token"])
    dataset_file_name = str(direction_metadata["dataset_file_name"])
    return {
        "paths": {
            "dataset_config_path": to_posix_path(DATASET_VARIANT_ROOT / dataset_file_name),
            "output_root": f"output/training_runs/{model_family}",
        },
        "experiment": {
            "run_name": f"te_sequential_residual_offset_probe_remote_{run_direction_token}",
            "model_family": model_family,
            "model_type": "sequential_residual_offset_probe",
        },
        "metadata": {
            "campaign_name": CAMPAIGN_NAME,
            "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
            "technical_document_path": to_posix_path(SEQUENTIAL_PROBE_TECHNICAL_DOCUMENT_PATH),
            "parent_technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
            "phase_name": "track2f_sequential_residual_offset_probe_training",
            "campaign_config_id": model_family,
            "queue_index": queue_index,
            "base_model_family": "sequential_residual_offset_probe",
            "training_variant": direction_metadata["training_variant"],
            "direction_scope_label": direction_metadata["direction_scope_label"],
            "use_forward_direction": bool(direction_metadata["use_forward_direction"]),
            "use_backward_direction": bool(direction_metadata["use_backward_direction"]),
            "track2e_reference_candidate": SURFACE_REFERENCE_DICTIONARY[surface_key]["track2e_reference_candidate"],
            "track2e_recommendation_path": to_posix_path(TRACK2E_RECOMMENDATION_PATH),
            "runtime_input_contract": "current point state plus supported short causal sequence history only",
            "notes": (
                "Wave 3.1 sequential residual-offset probe. Final TE prediction is "
                "base_te_prediction + residual_offset_prediction. Candidate must "
                "return through official TE curve-first verification."
            ),
        },
        "dataset": {
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
        },
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
        "training": {
            "learning_rate": 0.0005,
            "weight_decay": 0.0001,
            "min_epochs": 20,
            "max_epochs": 260,
            "patience": 40,
            "min_delta": 1.0e-05,
            "log_every_n_steps": 1,
            "fast_dev_run": False,
            "deterministic": False,
        },
        "runtime": {
            "accelerator": "auto",
            "devices": "auto",
            "precision": "32",
            "benchmark": True,
            "use_non_blocking_transfer": True,
        },
    }


def write_sequential_probe_queue_configs() -> list[Path]:

    """Write the three runnable sequential probe queue YAML files."""

    queue_path_list: list[Path] = []
    for queue_index, surface_key in enumerate(SURFACE_REFERENCE_DICTIONARY, start=1):
        queue_file_name = f"{queue_index:02d}_sequential_residual_offset_probe_{surface_key}.yaml"
        queue_path = QUEUE_ROOT / queue_file_name
        training_config = build_sequential_probe_training_config(queue_index, surface_key)
        write_yaml_file(PROJECT_PATH / queue_path, training_config)
        queue_path_list.append(queue_path)
    return queue_path_list


def write_campaign_readme(descriptor_path_list: list[Path]) -> Path:

    """Write a campaign-local README for the prepared descriptor package."""

    readme_path = CAMPAIGN_ROOT / "README.md"
    descriptor_line_list = [
        f"- `{to_posix_path(descriptor_path)}`"
        for descriptor_path in descriptor_path_list
    ]
    readme_text = f"""# Wave 3.1 Offset-Aware Probe Campaign Package

This package materializes the approved Wave 3.1 offset-aware probe plan.

It contains descriptor entries for the full Wave 3.1 matrix plus three
runnable `sequential_residual_offset_probe` queue YAML files. The post-hoc
`direction_torque` offset baseline remains a validation-only benchmark, while
`multi_head_shape_offset_probe` remains guarded until its own model type is
introduced through a later technical gate.

## Descriptor Matrix

{chr(10).join(descriptor_line_list)}

## Launch Commands

Preflight validation:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly
```

Sequential probe training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1
```

Remote sequential probe training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```
"""
    output_path = PROJECT_PATH / readme_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(readme_text, encoding="utf-8")
    return readme_path


def write_launcher() -> None:

    """Write the Wave 3.1 PowerShell launcher."""

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
$descriptorRoot = "{to_windows_path(PROBE_DESCRIPTOR_ROOT)}"
$campaignConfigRoot = "{to_windows_path(QUEUE_ROOT)}"
$validatorPath = "{to_windows_path(VALIDATOR_PATH)}"
$baselineOutputRoot = "{to_windows_path(BASELINE_STATUS_OUTPUT_DIRECTORY)}"
$planningReportPath = "{to_windows_path(PLANNING_REPORT_PATH)}"
$queueRoot = "config\\training\\queue"
$script:LastTrack2FPythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_sequential_residual_offset_probe_global.yaml"
    "02_sequential_residual_offset_probe_fw.yaml"
    "03_sequential_residual_offset_probe_bw.yaml"
)

function Write-Track2FStatus {{
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}}

function Invoke-Track2FPython {{
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {{
        & $PythonExecutable @ArgumentList
        $script:LastTrack2FPythonExitCode = $LASTEXITCODE
        return
    }}

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {{
        & python @ArgumentList
        $script:LastTrack2FPythonExitCode = $LASTEXITCODE
        return
    }}

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2FPythonExitCode = $LASTEXITCODE
}}

Write-Track2FStatus -Label "INFO" -Message ("Campaign: {{0}}" -f $campaignName)
Write-Track2FStatus -Label "INFO" -Message ("Descriptor root: {{0}}" -f $descriptorRoot)
Write-Track2FStatus -Label "INFO" -Message ("Runnable queue root: {{0}}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--descriptor-root",
    $descriptorRoot,
    "--require-prepared-state"
)

if (-not $PreflightOnly) {{
    $validatorArgumentList += @(
        "--write-baseline-status",
        "--output-root",
        $baselineOutputRoot
    )
}}

Write-Track2FStatus -Label "STEP" -Message "Validating Wave 3.1 package."
Invoke-Track2FPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2FPythonExitCode
if ($pythonExitCode -ne 0) {{
    exit $pythonExitCode
}}

if ($PreflightOnly) {{
    Write-Track2FStatus -Label "DONE" -Message "Preflight validation completed without launching training."
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
    Write-Track2FStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}}

Write-Track2FStatus -Label "STEP" -Message "Launching local sequential residual-offset probe campaign."
Invoke-Track2FPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2FPythonExitCode
exit $trainingExitCode
"""
    output_path = PROJECT_PATH / LAUNCHER_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_text, encoding="utf-8")


def write_launcher_note() -> None:

    """Write the operator-facing launcher note."""

    launcher_note_text = f"""# Wave 3.1 Offset-Aware Probe Campaign Launcher

## Overview

This launcher validates the prepared Wave 3.1 offset-aware probe package.

The package contains nine descriptor entries across `global`, `Fw`, and `Bw`
surfaces and three runnable sequential residual-offset queue YAML files:

- three `posthoc_direction_torque_offset_baseline` validation entries;
- three `sequential_residual_offset_probe` training entries;
- three `multi_head_shape_offset_probe` learned-probe placeholders.

The multi-head entries remain guarded because that model type is intentionally
deferred to a later technical gate.

## Local Preflight

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly
```

This validates descriptor count, surface/intervention coverage, CVP 1.5
reference availability, and prepared campaign state.

By default, the launcher runs validation through `conda run -n pinns_env
python` so the repository YAML dependencies are available. Use
`-PythonExecutable` only when pointing at another Python environment that has
the same dependencies installed.

## Local Sequential Probe Training

Run this from the repository root:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1
```

This validates the package, enqueues the three sequential residual-offset
training YAML files, and starts the local campaign runner.

Use this local verification command to confirm launcher flow without starting
training:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -EnqueueOnly
```

## Remote Sequential Probe Training

The operator-facing remote command is recorded for continuity:

```powershell
.\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```

This uses the canonical remote training sync wrapper for the three runnable
sequential residual-offset queue YAML files. It does not launch the multi-head
placeholder entries.
"""
    output_path = PROJECT_PATH / LAUNCHER_NOTE_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(launcher_note_text, encoding="utf-8")


def write_active_campaign_state(
    descriptor_path_list: list[Path],
    dataset_variant_path_list: list[Path],
    queue_path_list: list[Path],
    readme_path: Path,
) -> None:

    """Write the persistent active campaign state for Wave 3.1."""

    launch_command_list = [
        ".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly",
        ".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1",
        ".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -Remote",
    ]
    protected_file_list = [
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
        to_posix_path(SEQUENTIAL_PROBE_TECHNICAL_DOCUMENT_PATH),
        to_posix_path(LAUNCHER_FIX_TECHNICAL_DOCUMENT_PATH),
        to_posix_path(MODEL_REPORT_PATH),
        to_posix_path(PLANNING_REPORT_PATH),
        to_posix_path(LAUNCHER_PATH),
        to_posix_path(LAUNCHER_NOTE_PATH),
        to_posix_path(readme_path),
        *[to_posix_path(dataset_variant_path) for dataset_variant_path in dataset_variant_path_list],
        *[to_posix_path(queue_path) for queue_path in queue_path_list],
        *[to_posix_path(descriptor_path) for descriptor_path in descriptor_path_list],
    ]
    active_campaign_state = {
        "status": "prepared",
        "campaign_name": CAMPAIGN_NAME,
        "prepared_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "campaign_config_root": to_posix_path(CAMPAIGN_ROOT),
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "baseline_status_output_directory": to_posix_path(BASELINE_STATUS_OUTPUT_DIRECTORY),
        "execution_status": "prepared_for_sequential_residual_offset_probe_training",
        "training_launch_guard": (
            "multi-head Wave 3.1 probes remain blocked until the multi-head "
            "shape/offset model type is implemented"
        ),
        "protected_file_list": protected_file_list,
        "queue_config_path_list": [to_posix_path(queue_path) for queue_path in queue_path_list],
        "launch_command_list": launch_command_list,
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def main() -> int:

    """Prepare the Wave 3.1 campaign package."""

    validate_no_conflicting_active_campaign()
    assert (PROJECT_PATH / PLANNING_REPORT_PATH).exists(), f"Missing plan | {PLANNING_REPORT_PATH}"
    assert (PROJECT_PATH / TECHNICAL_DOCUMENT_PATH).exists(), f"Missing doc | {TECHNICAL_DOCUMENT_PATH}"
    assert (PROJECT_PATH / SEQUENTIAL_PROBE_TECHNICAL_DOCUMENT_PATH).exists(), (
        f"Missing sequential probe doc | {SEQUENTIAL_PROBE_TECHNICAL_DOCUMENT_PATH}"
    )
    assert (PROJECT_PATH / TRACK2E_RECOMMENDATION_PATH).exists(), (
        f"Missing CVP 1.5 recommendation CSV | {TRACK2E_RECOMMENDATION_PATH}"
    )

    descriptor_path_list = write_probe_descriptors()
    dataset_variant_path_list = copy_dataset_variants()
    queue_path_list = write_sequential_probe_queue_configs()
    readme_path = write_campaign_readme(descriptor_path_list)
    write_launcher()
    write_launcher_note()
    write_active_campaign_state(
        descriptor_path_list,
        dataset_variant_path_list,
        queue_path_list,
        readme_path,
    )

    print(f"Prepared {CAMPAIGN_NAME}")
    print(f"Descriptor count: {len(descriptor_path_list)}")
    print(f"Runnable queue count: {len(queue_path_list)}")
    print(f"Campaign root: {to_posix_path(CAMPAIGN_ROOT)}")
    print("Local preflight command:")
    print(".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly")
    print("Local sequential training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1")
    print("Remote sequential training command:")
    print(".\\scripts\\campaigns\\track2\\run_track2f_offset_aware_probe_campaign.ps1 -Remote")
    return 0


if __name__ == "__main__":
    sys.exit(main())
