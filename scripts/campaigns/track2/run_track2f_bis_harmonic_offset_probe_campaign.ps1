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

$campaignName = "track2f_bis_harmonic_offset_probe_campaign_2026_06_04"
$campaignConfigRoot = "config\training\track2f_bis_harmonic_offset_probe\campaigns\2026-06-04_track2f_bis_harmonic_offset_probe_campaign\queue"
$validatorPath = "scripts\campaigns\track2\validate_track2f_bis_harmonic_offset_probe_package.py"
$planningReportPath = "doc\reports\campaign_plans\track2\2026-06-04-22-57-04_track2f_bis_harmonic_offset_probe_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$script:LastTrack2FBisPythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_clean_sequential_residual_offset_control_global.yaml"
    "02_clean_sequential_residual_offset_control_fw.yaml"
    "03_clean_sequential_residual_offset_control_bw.yaml"
    "04_harmonic_residual_offset_probe_global.yaml"
    "05_harmonic_residual_offset_probe_fw.yaml"
    "06_harmonic_residual_offset_probe_bw.yaml"
)

function Write-Track2FBisStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Track2FBisPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastTrack2FBisPythonExitCode = $LASTEXITCODE
}

Write-Track2FBisStatus -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-Track2FBisStatus -Label "INFO" -Message ("Runnable queue root: {0}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--queue-root",
    $campaignConfigRoot,
    "--require-prepared-state"
)

Write-Track2FBisStatus -Label "STEP" -Message "Validating Track 2F-bis package."
Invoke-Track2FBisPython -ArgumentList $validatorArgumentList
$pythonExitCode = $script:LastTrack2FBisPythonExitCode
if ($pythonExitCode -ne 0) {
    exit $pythonExitCode
}

if ($PreflightOnly) {
    Write-Track2FBisStatus -Label "DONE" -Message "Preflight validation completed without launching training."
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
    Write-Track2FBisStatus -Label "STEP" -Message "Enqueue-only verification enabled; training will not start."
}

Write-Track2FBisStatus -Label "STEP" -Message "Launching local Track 2F-bis harmonic-offset campaign."
Invoke-Track2FBisPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2FBisPythonExitCode
exit $trainingExitCode
