param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$EnqueueOnly,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "polished_dataset_full_wave_retraining_2026_06_22"
$CampaignManifestPath = "config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/campaign.yaml"
$PlanningReportPath = "doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_full_wave_retraining_campaign_plan_report.md"
$ValidatorPath = "scripts/campaigns/cross_wave/validate_polished_dataset_retraining_campaign_package.py"
$QueueRoot = "config\training\queue\polished_dataset_full_wave_retraining"
$script:LastPythonExitCode = 0

function Invoke-PolishedPython {
    param([string[]]$ArgumentList)

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}

function Get-ManifestConfigPathList {
    $PythonCode = @"
from pathlib import Path
import json
import yaml
manifest_path = Path(r"$CampaignManifestPath")
payload = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
print(json.dumps(payload["queue_config_path_list"]))
"@
    $EncodedCommand = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($PythonCode))
    $JsonText = & conda run --no-capture-output -n $CondaEnvironmentName python -c "import base64; exec(base64.b64decode('$EncodedCommand').decode('utf-8'))"
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to read campaign manifest | $CampaignManifestPath"
    }
    return @($JsonText | ConvertFrom-Json)
}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"

Invoke-PolishedPython -ArgumentList @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly) {
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}

$CampaignConfigPathList = Get-ManifestConfigPathList

if ($Remote) {
    if ($EnqueueOnly) {
        throw "-EnqueueOnly is supported only for local launcher verification."
    }

    & ".\scripts\campaigns\infrastructure\run_remote_training_campaign.ps1" `
        -CampaignConfigPathList $CampaignConfigPathList `
        -CampaignName $CampaignName `
        -PlanningReportPath $PlanningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList @("scripts", "config", "doc", "site", "requirements.txt", "AGENTS.md") `
        -AdditionalTrainingArgumentList @(
            "--dataset",
            "polished_dataset",
            "--queue-root",
            $QueueRoot,
            "--stop-on-error"
        )
    exit $LASTEXITCODE
}

$TrainingArgumentList = @(
    "-B",
    "scripts\training\run_training_campaign.py"
) + $CampaignConfigPathList + @(
    "--dataset",
    "polished_dataset",
    "--queue-root",
    $QueueRoot,
    "--campaign-name",
    $CampaignName,
    "--planning-report-path",
    $PlanningReportPath,
    "--stop-on-error"
)
if ($EnqueueOnly) {
    $TrainingArgumentList += "--enqueue-only"
}

Write-Host "[STEP] Launching local polished full-wave retraining campaign."
$RunExitCode = Invoke-PolishedPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
