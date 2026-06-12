param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$EnqueueOnly,
    [switch]$RunOneBatchValidation,
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

$campaignName = "track2h_quantile_probabilistic_campaign_2026_06_12"
$campaignConfigRoot = "config\training\track2h_quantile_probabilistic_modeling\campaigns\2026-06-12_track2h_quantile_probabilistic_campaign\queue"
$validatorPath = "scripts\campaigns\track2\validate_track2h_quantile_probabilistic_package.py"
$planningReportPath = "doc\reports\campaign_plans\track2\2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$script:LastTrack2HPythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_quantile_p10_p50_p90_global.yaml",
    "02_quantile_p10_p50_p90_fw.yaml",
    "03_quantile_p10_p50_p90_bw.yaml",
    "04_gaussian_nll_global.yaml",
    "05_gaussian_nll_fw.yaml",
    "06_gaussian_nll_bw.yaml"
)

function Write-Track2HStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Track2HPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastTrack2HPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastTrack2HPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2HPythonExitCode = $LASTEXITCODE
}

Write-Track2HStatus -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-Track2HStatus -Label "INFO" -Message ("Runnable queue root: {0}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

if ($RunOneBatchValidation) {
    $validatorArgumentList += "--run-one-batch"
}

Write-Track2HStatus -Label "STEP" -Message "Validating Track 2H quantile/probabilistic package."
Invoke-Track2HPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2HPythonExitCode
if ($pythonExitCode -ne 0) {
    exit $pythonExitCode
}

if ($PreflightOnly) {
    Write-Track2HStatus -Label "DONE" -Message "Preflight validation completed without launching training."
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
    Write-Track2HStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}

Write-Track2HStatus -Label "STEP" -Message "Launching local Track 2H quantile/probabilistic campaign."
Invoke-Track2HPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2HPythonExitCode
exit $trainingExitCode
