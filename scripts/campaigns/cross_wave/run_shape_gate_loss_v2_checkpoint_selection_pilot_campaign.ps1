param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$RunOneBatchValidation,
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

$CampaignName = "shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21"
$CampaignManifestPath = "config/training/shape_gate_loss_v2_pilot/campaigns/2026-07-21_shape_gate_loss_v2_checkpoint_selection_pilot/campaign.yaml"
$CampaignConfigPathList = @(
    "config/training/shape_gate_loss_v2_pilot/campaigns/2026-07-21_shape_gate_loss_v2_checkpoint_selection_pilot/queue/001_shape_gate_loss_v2_periodic_gru_sequence_fw.yaml"
)
$PlanningReportPath = "doc/reports/campaign_plans/cross_wave/shape_gate_loss_v2/2026-07-21-12-21-36_shape_gate_loss_v2_checkpoint_selection_pilot_campaign_plan_report.md"
$QueueRoot = "config\training\queue\shape_gate_loss_v2_pilot"
$script:LastPythonExitCode = 0

function Write-ShapeGateV2PilotStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-ShapeGateV2PilotPython {
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

    $CondaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $CondaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}

Write-ShapeGateV2PilotStatus -Label "INFO" -Message "Campaign: $CampaignName"
Write-ShapeGateV2PilotStatus -Label "INFO" -Message "Primary scope: polished_dataset setpoints Fw"
Write-ShapeGateV2PilotStatus -Label "INFO" -Message "Manifest: $CampaignManifestPath"

foreach ($RequiredPath in @($CampaignManifestPath, $PlanningReportPath) + $CampaignConfigPathList) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required campaign path is missing | $RequiredPath"
    }
}

if ($RunOneBatchValidation) {
    Write-ShapeGateV2PilotStatus -Label "STEP" -Message "Running one-batch validation without launching training."
    Invoke-ShapeGateV2PilotPython -ArgumentList @(
        "-B",
        "scripts\training\validate_training_setup.py",
        "--config-path",
        $CampaignConfigPathList[0],
        "--dataset",
        "polished_dataset"
    )
    if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }
}

if ($PreflightOnly) {
    Write-ShapeGateV2PilotStatus -Label "DONE" -Message "Preflight completed without training."
    exit 0
}

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
            "--input-mode",
            "setpoints",
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
    "--input-mode",
    "setpoints",
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
    Write-ShapeGateV2PilotStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}

Write-ShapeGateV2PilotStatus -Label "STEP" -Message "Launching local shape-gate loss v2 checkpoint-selection pilot."
Invoke-ShapeGateV2PilotPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
