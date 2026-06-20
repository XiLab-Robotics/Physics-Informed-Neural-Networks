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

$campaignName = "wave3_harmonic_prior_residual_campaign_2026_06_14"
$campaignConfigRoot = "config\training\wave3_harmonic_prior_residual\campaigns\2026-06-14_wave3_harmonic_prior_residual_campaign\queue"
$validatorPath = "scripts\campaigns\wave_3\validate_wave3_harmonic_prior_residual_campaign.py"
$planningReportPath = "doc\reports\campaign_plans\wave_3\2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$script:LastWave3PythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_pointwise_control_global.yaml",
    "02_pointwise_control_fw.yaml",
    "03_pointwise_control_bw.yaml",
    "04_smooth_l1_structured_global.yaml",
    "05_smooth_l1_structured_fw.yaml",
    "06_smooth_l1_structured_bw.yaml"
)

function Write-Wave3Status {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave3Python {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastWave3PythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastWave3PythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastWave3PythonExitCode = $LASTEXITCODE
}

Write-Wave3Status -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-Wave3Status -Label "INFO" -Message ("Runnable queue root: {0}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

if ($RunOneBatchValidation) {
    $validatorArgumentList += "--run-one-batch"
}

Write-Wave3Status -Label "STEP" -Message "Validating Wave 5.1 harmonic-prior residual package."
Invoke-Wave3Python -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastWave3PythonExitCode
if ($pythonExitCode -ne 0) {
    exit $pythonExitCode
}

if ($PreflightOnly) {
    Write-Wave3Status -Label "DONE" -Message "Preflight validation completed without launching training."
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
    Write-Wave3Status -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}

Write-Wave3Status -Label "STEP" -Message "Launching local Wave 5.1 harmonic-prior residual campaign."
Invoke-Wave3Python -ArgumentList $argumentList
$trainingExitCode = $script:LastWave3PythonExitCode
exit $trainingExitCode
