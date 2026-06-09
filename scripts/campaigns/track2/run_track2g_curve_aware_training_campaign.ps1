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
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignName = "track2g_curve_aware_training_campaign_2026_06_08"
$campaignConfigRoot = "config\training\track2g_curve_aware_training\campaigns\2026-06-08_track2g_curve_aware_training_campaign\queue"
$validatorPath = "scripts\campaigns\track2\validate_track2g_curve_aware_training_package.py"
$planningReportPath = "doc\reports\campaign_plans\track2\2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$script:LastTrack2GPythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_pointwise_control_global.yaml"
    "02_pointwise_control_fw.yaml"
    "03_pointwise_control_bw.yaml"
    "04_raw_centered_shape_global.yaml"
    "05_raw_centered_shape_fw.yaml"
    "06_raw_centered_shape_bw.yaml"
    "07_raw_offset_global.yaml"
    "08_raw_offset_fw.yaml"
    "09_raw_offset_bw.yaml"
    "10_full_curve_composite_global.yaml"
    "11_full_curve_composite_fw.yaml"
    "12_full_curve_composite_bw.yaml"
)

function Write-Track2GStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Track2GPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastTrack2GPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastTrack2GPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2GPythonExitCode = $LASTEXITCODE
}

Write-Track2GStatus -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-Track2GStatus -Label "INFO" -Message ("Runnable queue root: {0}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

Write-Track2GStatus -Label "STEP" -Message "Validating Track 2G package."
Invoke-Track2GPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2GPythonExitCode
if ($pythonExitCode -ne 0) {
    exit $pythonExitCode
}

if ($PreflightOnly) {
    Write-Track2GStatus -Label "DONE" -Message "Preflight validation completed without launching training."
    exit 0
}

$campaignConfigPathList = $campaignConfigFileNameList | ForEach-Object {
    Join-Path $campaignConfigRoot $_
}

foreach ($queueSubdirectoryName in @("pending", "running")) {
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path -LiteralPath $queueSubdirectoryPath)) {
        continue
    }

    foreach ($campaignConfigFileName in $campaignConfigFileNameList) {
        Get-ChildItem -LiteralPath $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -like "*$campaignConfigFileName" } |
            Remove-Item -Force
    }
}

if ($Remote) {
    if ($EnqueueOnly) {
        throw "-EnqueueOnly is supported only for local launcher verification."
    }

    $remoteLauncherPath = "scripts\campaigns\infrastructure\run_remote_training_campaign.ps1"
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
}

$argumentList = @(
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    $campaignName,
    "--planning-report-path",
    $planningReportPath
)

if ($EnqueueOnly) {
    $argumentList += "--enqueue-only"
    Write-Track2GStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}

Write-Track2GStatus -Label "STEP" -Message "Launching local Track 2G curve-aware training campaign."
Invoke-Track2GPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2GPythonExitCode
exit $trainingExitCode
