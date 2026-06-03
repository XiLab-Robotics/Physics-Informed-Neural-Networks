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
$validatorPath = "scripts\campaigns\track2\validate_track2f_offset_aware_probe_package.py"
$baselineOutputRoot = "output\validation_checks\track2f_offset_aware_probe\2026-06-03_track2f_offset_aware_probe_prelaunch"

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

if ($Remote) {
    Write-Track2FStatus -Label "BLOCKED" -Message "Remote Track 2F learned training is not enabled yet."
    Write-Track2FStatus -Label "BLOCKED" -Message "The prepared descriptors include learned probe placeholders, but the model types are not implemented in scripts/training/run_training_campaign.py."
    Write-Track2FStatus -Label "NEXT" -Message "Implement the sequential and multi-head Track 2F model types, then replace this guard with the canonical remote training sync wrapper."
    exit 2
}

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
}
else {
    Write-Track2FStatus -Label "DONE" -Message "Baseline-status artifacts written without launching learned training."
    Write-Track2FStatus -Label "NEXT" -Message "Learned Track 2F training remains blocked until its model types are implemented."
}
