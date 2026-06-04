param(
    [switch]$Remote,
    [switch]$PreflightOnly,
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

$campaignName = "track2f_offset_aware_probe_campaign_2026_06_03"
$descriptorRoot = "config\training\track2f_offset_aware_probe\campaigns\2026-06-03_track2f_offset_aware_probe_campaign\probe_descriptors"
$campaignConfigRoot = "config\training\track2f_offset_aware_probe\campaigns\2026-06-03_track2f_offset_aware_probe_campaign\queue"
$validatorPath = "scripts\campaigns\track2\validate_track2f_offset_aware_probe_package.py"
$baselineOutputRoot = "output\validation_checks\track2f_offset_aware_probe\2026-06-03_track2f_offset_aware_probe_prelaunch"
$planningReportPath = "doc\reports\campaign_plans\track2\2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md"
$queueRoot = "config\training\queue"
$campaignConfigFileNameList = @(
    "01_sequential_residual_offset_probe_global.yaml"
    "02_sequential_residual_offset_probe_fw.yaml"
    "03_sequential_residual_offset_probe_bw.yaml"
)

function Write-Track2FStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Track2FPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        return $LASTEXITCODE
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    return $LASTEXITCODE
}

Write-Track2FStatus -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-Track2FStatus -Label "INFO" -Message ("Descriptor root: {0}" -f $descriptorRoot)
Write-Track2FStatus -Label "INFO" -Message ("Runnable queue root: {0}" -f $campaignConfigRoot)

$validatorArgumentList = @(
    $validatorPath,
    "--descriptor-root",
    $descriptorRoot,
    "--require-prepared-state"
)

if (-not $PreflightOnly) {
    $validatorArgumentList += @(
        "--write-baseline-status",
        "--output-root",
        $baselineOutputRoot
    )
}

Write-Track2FStatus -Label "STEP" -Message "Validating Track 2F package."
$pythonExitCode = Invoke-Track2FPython -ArgumentList $validatorArgumentList
if ($pythonExitCode -ne 0) {
    exit $pythonExitCode
}

if ($PreflightOnly) {
    Write-Track2FStatus -Label "DONE" -Message "Preflight validation completed without launching training."
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

Write-Track2FStatus -Label "STEP" -Message "Launching local sequential residual-offset probe campaign."
$trainingExitCode = Invoke-Track2FPython -ArgumentList $argumentList
exit $trainingExitCode
