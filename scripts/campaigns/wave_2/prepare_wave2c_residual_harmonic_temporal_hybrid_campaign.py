"""Prepare the Wave 2C residual harmonic temporal hybrid campaign package."""

from __future__ import annotations

# Import Python Utilities
import importlib.util
import shutil, sys
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[3]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

CAMPAIGN_NAME = "wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27"
CAMPAIGN_ROOT = Path(
    "config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/"
    "2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign"
)
HYDRA_CONFIG_ROOT = Path("config/training/hydra/wave2")
PLANNING_REPORT_PATH = Path(
    "doc/reports/campaign_plans/wave_2/"
    "2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = Path(
    "doc/technical/2026-05/2026-05-27/"
    "2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrids.md"
)
LAUNCHER_PATH = Path("scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1")
LAUNCHER_NOTE_PATH = Path(
    "doc/scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.md"
)
ACTIVE_CAMPAIGN_STATE_PATH = Path("doc/running/active_training_campaign.yaml")
CAMPAIGN_OUTPUT_DIRECTORY = (
    Path("output/training_campaigns/wave2/residual_harmonic_temporal_hybrid") / CAMPAIGN_NAME
)
PREPARED_AT = "2026-05-27T18:20:41+02:00"

SPARSE_RCIM_HARMONIC_INDEX_LIST = [0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
HARMONIC_BASIS_DICTIONARY = {
    "sparse_rcim": {
        "harmonic_order": 240,
        "harmonic_index_list": SPARSE_RCIM_HARMONIC_INDEX_LIST,
        "output_suffix": "sparse_rcim",
        "note": "sparse RCIM harmonic list",
    },
    "dense_240": {
        "harmonic_order": 240,
        "harmonic_index_list": list(range(0, 241)),
        "output_suffix": "dense240",
        "note": "explicit inclusive dense 0..240 harmonic list",
    },
    "dense_360": {
        "harmonic_order": 360,
        "harmonic_index_list": list(range(0, 361)),
        "output_suffix": "dense360",
        "note": "explicit inclusive dense 0..360 harmonic list",
    },
}
MODEL_FAMILY_LIST = [
    "residual_harmonic_gru_sequence",
    "residual_harmonic_lstm_sequence",
]
DIRECTION_LIST = [
    "global",
    "fw",
    "bw",
]
DIRECTION_MODEL_FAMILY_SUFFIX_DICTIONARY = {
    "global": "",
    "fw": "_fw",
    "bw": "_bw",
}
DIRECTION_DATASET_FILE_NAME_DICTIONARY = {
    "global": "transmission_error_dataset_global.yaml",
    "fw": "transmission_error_dataset_fw.yaml",
    "bw": "transmission_error_dataset_bw.yaml",
}


def load_hydra_composer():

    """Load the Hydra composer without importing the full training package."""

    module_path = PROJECT_PATH / "scripts" / "training" / "compose_hydra_training_config.py"
    module_specification = importlib.util.spec_from_file_location(
        "wave2c_compose_hydra_training_config",
        module_path,
    )
    assert module_specification is not None
    assert module_specification.loader is not None
    module = importlib.util.module_from_spec(module_specification)
    sys.modules[module_specification.name] = module
    module_specification.loader.exec_module(module)
    return module.compose_hydra_training_config


def to_posix_path(path_value: Path) -> str:

    """Convert a repository path to a stable POSIX-style string."""

    return path_value.as_posix()


def to_windows_path(path_value: Path) -> str:

    """Convert a repository path to a PowerShell-friendly string."""

    return str(path_value).replace("/", "\\")


def read_yaml_file(input_path: Path) -> dict[str, Any]:

    """Read one YAML file into a dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_file(output_path: Path, payload: dict[str, Any]) -> None:

    """Write a YAML payload with stable repository formatting."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(payload, sort_keys=False, width=1000), encoding="utf-8")


def validate_no_active_campaign() -> None:

    """Stop if another campaign is already prepared or active."""

    active_campaign_path = PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH
    active_campaign_state = read_yaml_file(active_campaign_path)
    active_status = str(active_campaign_state.get("status", "")).strip().lower()
    active_campaign_name = str(active_campaign_state.get("campaign_name", "")).strip()
    same_campaign_is_prepared = (
        active_status == "prepared"
        and active_campaign_name == CAMPAIGN_NAME
    )
    assert active_status in ["", "none"] or same_campaign_is_prepared, (
        f"Cannot prepare Wave 2C package while another campaign is active | status={active_status}"
    )


def build_surface_model_family(model_family: str, direction_name: str, harmonic_basis_name: str) -> str:

    """Build the direction-qualified and basis-qualified model family name."""

    basis_suffix = HARMONIC_BASIS_DICTIONARY[harmonic_basis_name]["output_suffix"]
    direction_suffix = DIRECTION_MODEL_FAMILY_SUFFIX_DICTIONARY[direction_name]
    return f"{model_family}{direction_suffix}_{basis_suffix}"


def build_queue_config_file_name(
    queue_index: int,
    model_family: str,
    harmonic_basis_name: str,
    direction_name: str,
) -> str:

    """Build one stable queue configuration filename."""

    return f"{queue_index:02d}_{model_family}_{harmonic_basis_name}_{direction_name}.yaml"


def build_campaign_training_config(
    model_family: str,
    harmonic_basis_name: str,
    direction_name: str,
    queue_index: int,
) -> tuple[dict[str, Any], dict[str, Any]]:

    """Compose and adapt one Wave 2C campaign training configuration."""

    compose_hydra_training_config = load_hydra_composer()
    materialized_bundle = compose_hydra_training_config(
        config_dir=(PROJECT_PATH / HYDRA_CONFIG_ROOT).resolve(),
        config_name="config",
        override_list=[
            f"model_family={model_family}",
            f"direction={direction_name}",
            "campaign_profile=wave2c_residual_harmonic_temporal_hybrid",
        ],
    )

    training_config = materialized_bundle.training_config
    dataset_config = materialized_bundle.dataset_config
    basis_configuration = HARMONIC_BASIS_DICTIONARY[harmonic_basis_name]
    surface_model_family = build_surface_model_family(model_family, direction_name, harmonic_basis_name)
    dataset_file_name = DIRECTION_DATASET_FILE_NAME_DICTIONARY[direction_name]
    dataset_config_path = CAMPAIGN_ROOT / "dataset_variants" / dataset_file_name

    # Route artifacts through direction-aware and basis-aware family roots.
    training_config["paths"]["dataset_config_path"] = to_posix_path(dataset_config_path)
    training_config["paths"]["output_root"] = f"output/training_runs/{surface_model_family}"
    training_config["experiment"]["run_name"] = (
        f"{training_config['experiment']['run_name']}_{basis_configuration['output_suffix']}"
    )
    training_config["experiment"]["model_family"] = surface_model_family

    # Apply The Explicit Harmonic Basis Tier.
    training_config["model"]["harmonic_order"] = int(basis_configuration["harmonic_order"])
    training_config["model"]["harmonic_index_list"] = list(basis_configuration["harmonic_index_list"])

    # Attach campaign metadata.
    metadata_dictionary = training_config.setdefault("metadata", {})
    metadata_dictionary["campaign_name"] = CAMPAIGN_NAME
    metadata_dictionary["planning_report_path"] = to_posix_path(PLANNING_REPORT_PATH)
    metadata_dictionary["technical_document_path"] = to_posix_path(TECHNICAL_DOCUMENT_PATH)
    metadata_dictionary["phase_name"] = "wave2c_residual_harmonic_temporal_hybrid_preparation"
    metadata_dictionary["campaign_config_id"] = surface_model_family
    metadata_dictionary["queue_index"] = queue_index
    metadata_dictionary["base_model_family"] = model_family
    metadata_dictionary["harmonic_basis"] = harmonic_basis_name
    metadata_dictionary["harmonic_basis_note"] = str(basis_configuration["note"])
    metadata_dictionary["notes"] = (
        f"Wave 2C residual harmonic temporal hybrid campaign | family={model_family} | "
        f"basis={harmonic_basis_name} | direction={direction_name}. "
        "Candidate must return through official Track 2 verification."
    )
    metadata_dictionary.pop("output_run_name", None)
    metadata_dictionary.pop("run_instance_id", None)

    return training_config, dataset_config


def write_launcher(queue_file_name_list: list[str]) -> None:

    """Write the PowerShell launcher for the prepared campaign."""

    queue_file_literal = "\n".join(f'    "{queue_file_name}"' for queue_file_name in queue_file_name_list)
    launcher_text = f"""param(
    [switch]$Remote,
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) {{ $env:PINNS_REMOTE_TRAINING_REPO_PATH }} else {{ "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks" }}),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) {{ $env:PINNS_REMOTE_TRAINING_CONDA_ENV }} else {{ "pinns_env" }})
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\\..\\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "{to_windows_path(CAMPAIGN_ROOT / "queue")}"
$planningReportPath = "{to_windows_path(PLANNING_REPORT_PATH)}"
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

if ($Remote) {{
    $remoteLauncherPath = "scripts\\campaigns\\infrastructure\\run_remote_training_campaign.ps1"
    $sourceSyncPathList = @("scripts", "config", "doc", "requirements.txt", "AGENTS.md")

    & $remoteLauncherPath `
        -CampaignConfigPathList $campaignConfigPathList `
        -CampaignName "{CAMPAIGN_NAME}" `
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

    launcher_note_text = f"""# Wave 2C Residual Harmonic Temporal Hybrid Campaign Launcher

## Overview

This launcher runs the prepared `Wave 2C` residual harmonic temporal hybrid
campaign after explicit operator approval. The package compares residual
harmonic `GRU` and residual harmonic `LSTM` sequence models across the required
`global`, `Fw`, and `Bw` direction surfaces and across sparse plus dense
harmonic-basis tiers.

The launcher does not run `Track 2` verification by itself. Promotion remains a
post-campaign closeout step that must refresh the official `Track 2` matrix and
visual reports.

## Campaign Package

Prepared campaign root:

- `{to_posix_path(CAMPAIGN_ROOT)}`

Prepared queue count:

- `18` YAML files

Families:

- `residual_harmonic_gru_sequence`
- `residual_harmonic_lstm_sequence`

Harmonic basis tiers:

- `sparse_rcim`: `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]`
- `dense_240`: explicit inclusive list `0..240`
- `dense_360`: explicit inclusive list `0..360`

## Planning Report

This launcher is tied to:

- `{to_posix_path(PLANNING_REPORT_PATH)}`

## Practical Use

Run the full prepared campaign from the repository root:

```powershell
.\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1
```

Run the same prepared campaign on the configured LAN remote workstation:

```powershell
.\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -Remote
```

Optional Python executable override:

```powershell
.\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -PythonExecutable python
```

Optional remote overrides:

```powershell
.\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 `
  -Remote `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName pinns_env
```

The `-Remote` path delegates to
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`. It syncs
`scripts`, `config`, `doc`, `requirements.txt`, and `AGENTS.md` before launch,
then syncs the manifest-declared campaign outputs, per-run training artifacts,
queue end state, and affected registries back into the local repository.

When `PINNS_REMOTE_TRAINING_REPO_PATH` is not set, the launcher defaults to the
validated LAN clone path:

- `C:\\Users\\Martina Salami\\Documents\\Davide\\Physics-Informed-Neural-Networks`

## Expected Outputs

The shared campaign runner writes campaign artifacts under:

- `{to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY)}`

Per-run training artifacts are written under each configured
`output/training_runs/<model_family>/` root with immutable run-instance
directories.

## Operator Notes

The launcher clears stale `pending` and `running` queue copies for the prepared
file names before starting. It does not remove completed or failed historical
queue records.

Training must not be launched until the prepared campaign package is explicitly
approved.
"""
    LAUNCHER_NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    LAUNCHER_NOTE_PATH.write_text(launcher_note_text, encoding="utf-8")


def write_campaign_readme(queue_file_name_list: list[str]) -> None:

    """Write a short campaign-root README."""

    queue_listing = "\n".join(f"- `queue/{queue_file_name}`" for queue_file_name in queue_file_name_list)
    readme_text = f"""# Wave 2C Residual Harmonic Temporal Hybrid Campaign

Prepared campaign package for:

- `{CAMPAIGN_NAME}`

Planning report:

- `{to_posix_path(PLANNING_REPORT_PATH)}`

Queue files:

{queue_listing}
"""
    (PROJECT_PATH / CAMPAIGN_ROOT / "README.md").write_text(readme_text, encoding="utf-8")


def write_active_campaign_state(
    queue_config_relative_path_list: list[str],
    protected_file_relative_path_list: list[str],
) -> None:

    """Write the active campaign state for the prepared package."""

    active_campaign_state = {
        "status": "prepared",
        "campaign_name": CAMPAIGN_NAME,
        "prepared_at": PREPARED_AT,
        "planning_report_path": to_posix_path(PLANNING_REPORT_PATH),
        "technical_document_path": to_posix_path(TECHNICAL_DOCUMENT_PATH),
        "campaign_config_root": to_posix_path(CAMPAIGN_ROOT),
        "campaign_output_directory": to_posix_path(CAMPAIGN_OUTPUT_DIRECTORY),
        "protected_file_list": protected_file_relative_path_list,
        "queue_config_path_list": queue_config_relative_path_list,
        "launch_command_list": [
            ".\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1",
            ".\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -Remote",
        ],
    }
    write_yaml_file(PROJECT_PATH / ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def prepare_campaign_package() -> None:

    """Prepare the complete Wave 2C residual harmonic temporal hybrid campaign package."""

    validate_no_active_campaign()

    absolute_campaign_root = PROJECT_PATH / CAMPAIGN_ROOT
    absolute_queue_root = absolute_campaign_root / "queue"
    absolute_dataset_variant_root = absolute_campaign_root / "dataset_variants"

    # Reset Generated Campaign Folder
    if absolute_campaign_root.exists():
        shutil.rmtree(absolute_campaign_root)
    absolute_queue_root.mkdir(parents=True, exist_ok=True)
    absolute_dataset_variant_root.mkdir(parents=True, exist_ok=True)

    queue_file_name_list: list[str] = []
    queue_config_relative_path_list: list[str] = []
    dataset_variant_relative_path_list: list[str] = []
    queue_index = 1

    # Compose And Persist Queue Configurations
    for model_family in MODEL_FAMILY_LIST:
        for harmonic_basis_name in HARMONIC_BASIS_DICTIONARY:
            for direction_name in DIRECTION_LIST:
                training_config, dataset_config = build_campaign_training_config(
                    model_family=model_family,
                    harmonic_basis_name=harmonic_basis_name,
                    direction_name=direction_name,
                    queue_index=queue_index,
                )

                dataset_file_name = DIRECTION_DATASET_FILE_NAME_DICTIONARY[direction_name]
                dataset_variant_path = absolute_dataset_variant_root / dataset_file_name
                if not dataset_variant_path.exists():
                    write_yaml_file(dataset_variant_path, dataset_config)
                    dataset_variant_relative_path_list.append(
                        to_posix_path(CAMPAIGN_ROOT / "dataset_variants" / dataset_file_name)
                    )

                config_file_name = build_queue_config_file_name(
                    queue_index,
                    model_family,
                    harmonic_basis_name,
                    direction_name,
                )
                queue_config_path = absolute_queue_root / config_file_name
                write_yaml_file(queue_config_path, training_config)
                queue_file_name_list.append(config_file_name)
                queue_config_relative_path_list.append(to_posix_path(CAMPAIGN_ROOT / "queue" / config_file_name))
                queue_index += 1

    # Write Launcher And Documentation
    write_launcher(queue_file_name_list)
    write_launcher_note()
    write_campaign_readme(queue_file_name_list)

    protected_file_relative_path_list = [
        to_posix_path(CAMPAIGN_ROOT / "README.md"),
        *dataset_variant_relative_path_list,
        *queue_config_relative_path_list,
        to_posix_path(LAUNCHER_PATH),
        to_posix_path(LAUNCHER_NOTE_PATH),
        to_posix_path(PLANNING_REPORT_PATH),
        to_posix_path(TECHNICAL_DOCUMENT_PATH),
    ]
    write_active_campaign_state(queue_config_relative_path_list, protected_file_relative_path_list)

    print(f"[DONE] Prepared campaign package | {CAMPAIGN_NAME}")
    print(f"[INFO] Queue configs | {len(queue_config_relative_path_list)}")
    print("[INFO] Launch command | .\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1")
    print("[INFO] Remote launch command | .\\scripts\\campaigns\\wave2\\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1 -Remote")


def main() -> int:

    """Run campaign preparation."""

    prepare_campaign_package()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
