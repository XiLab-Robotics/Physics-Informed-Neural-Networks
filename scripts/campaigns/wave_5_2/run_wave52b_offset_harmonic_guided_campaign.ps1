param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$RunOneBatchValidation,
    [switch]$EnqueueOnly,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "wave52b_offset_harmonic_guided_campaign_2026_07_01"
$CampaignManifestPath = "config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/campaign.yaml"
$PlanningReportPath = "doc/reports/campaign_plans/wave_5_2/2026-07-01-16-08-01_wave52b_offset_harmonic_guided_campaign_plan_report.md"
$ValidatorPath = "scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py"
$QueueRoot = "config\training\queue\wave52b_offset_harmonic_guided"
$script:LastPythonExitCode = 0

function Invoke-Wave52BPython {
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

function Get-Wave52BManifestConfigPathList {
    $PythonCode = @"
from pathlib import Path
import json
import sys
import yaml
manifest_path = Path(sys.argv[2])
payload = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
print(json.dumps(payload["queue_config_path_list"]))
"@
    $EncodedCommand = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($PythonCode))
    $PythonBootstrapCode = "import base64, sys; exec(base64.b64decode(sys.argv[1]).decode('utf-8'))"
    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        $JsonText = & $PythonExecutable -c $PythonBootstrapCode $EncodedCommand $CampaignManifestPath
    }
    elseif ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        $JsonText = & python -c $PythonBootstrapCode $EncodedCommand $CampaignManifestPath
    }
    else {
        $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
        $JsonText = & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python -c $PythonBootstrapCode $EncodedCommand $CampaignManifestPath
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to read campaign manifest | $CampaignManifestPath"
    }
    $ManifestConfigPathList = $JsonText | ConvertFrom-Json
    return @($ManifestConfigPathList)
}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"
Write-Host "[INFO] Scope: Wave 5.2B offset and harmonic guided matrix | runs=12 | surfaces=global,fw,bw"

$ValidatorArgumentList = @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath,
    "--require-prepared-state"
)
if ($RunOneBatchValidation) {
    $ValidatorArgumentList += "--run-one-batch"
}

Invoke-Wave52BPython -ArgumentList $ValidatorArgumentList
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly) {
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}

$CampaignConfigPathList = Get-Wave52BManifestConfigPathList

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

Write-Host "[STEP] Launching local Wave 5.2B offset and harmonic guided campaign."
Invoke-Wave52BPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
