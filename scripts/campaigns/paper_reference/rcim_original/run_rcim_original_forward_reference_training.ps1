param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$Families = "",
    [double]$TestSize = 0.20,
    [string]$OutputSuffix = "",
    [string]$DataframePath = "",
    [switch]$PrintOnly
)

$ErrorActionPreference = "Stop"

# Resolve The Repository Root From The Script Location.
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path
Set-Location $projectRoot

# Build The Direction-Specific Archive Root And Run Instance Identifier.
$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$runInstanceId = $runTimestamp + "__fw_v18_paper_reference"
if (-not [string]::IsNullOrWhiteSpace($OutputSuffix)) {
    $runInstanceId = $runInstanceId + "_" + $OutputSuffix
}

$outputRoot = Join-Path $projectRoot ("models\paper_reference\rcim_original\forward\source_runs\" + $runInstanceId)
New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null

# Build The Recovered-Workflow Training Command.
$argumentList = @(
    "run", "-n", $CondaEnvironmentName,
    $PythonExecutable,
    "-B",
    "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py",
    "--mode", "paper_eval",
    "--direction", "forward",
    "--test-size", $TestSize.ToString([System.Globalization.CultureInfo]::InvariantCulture),
    "--output-root", $outputRoot
)

if (-not [string]::IsNullOrWhiteSpace($Families)) {
    $argumentList += @("--families", $Families)
}

if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
    $argumentList += @("--dataframe-path", $DataframePath)
}

Write-Host "[INFO] RCIM Original Forward Reference Training" -ForegroundColor Cyan
Write-Host "[INFO] Mode | paper_eval" -ForegroundColor Cyan
Write-Host "[INFO] Direction | forward" -ForegroundColor Cyan
Write-Host "[INFO] Output Root | $outputRoot" -ForegroundColor Cyan
if (-not [string]::IsNullOrWhiteSpace($Families)) {
    Write-Host "[INFO] Families | $Families" -ForegroundColor Cyan
}
if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
    Write-Host "[INFO] Dataframe Override | $DataframePath" -ForegroundColor Cyan
}

$commandPreview = "conda " + (($argumentList | ForEach-Object {
    if ($_ -match '\s') { '"' + $_ + '"' } else { $_ }
}) -join " ")
Write-Host "[INFO] Command | $commandPreview" -ForegroundColor DarkCyan

if ($PrintOnly) {
    Write-Host "[DONE] Print-Only Mode Enabled. No Training Was Launched." -ForegroundColor Green
    exit 0
}

# Launch The Recovered Original Forward Replay.
& conda @argumentList
$nativeExitCode = $LASTEXITCODE

if ($nativeExitCode -ne 0) {
    Write-Host "[ERROR] RCIM Original Forward Reference Training Failed." -ForegroundColor Red
    exit $nativeExitCode
}

Write-Host "[DONE] RCIM Original Forward Reference Training Completed." -ForegroundColor Green
Write-Host "[DONE] Output Root | $outputRoot" -ForegroundColor Green
exit 0
