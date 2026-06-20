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

$campaignName = "track2h_mixture_density_heads_campaign_2026_06_13"
$campaignConfigRoot = "config\training\track2h_mixture_density_heads\campaigns\2026-06-13_track2h_mixture_density_heads_campaign\queue"
$validatorPath = "scripts\campaigns\track_2\validate_track2h_mixture_density_heads_package.py"
$planningReportPath = "doc\reports\campaign_plans\track_2\2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$script:LastTrack2HPythonExitCode = 0
$campaignConfigFileNameList = @(
    "01_mdn_k2_global.yaml",
    "02_mdn_k2_fw.yaml",
    "03_mdn_k2_bw.yaml",
    "04_mdn_k3_global.yaml",
    "05_mdn_k3_fw.yaml",
    "06_mdn_k3_bw.yaml"
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

Write-Track2HStatus -Label "STEP" -Message "Validating Wave 4.3 mixture-density heads package."
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

Write-Track2HStatus -Label "STEP" -Message "Launching local Wave 4.3 mixture-density heads campaign."
Invoke-Track2HPython -ArgumentList $argumentList
$trainingExitCode = $script:LastTrack2HPythonExitCode
exit $trainingExitCode
