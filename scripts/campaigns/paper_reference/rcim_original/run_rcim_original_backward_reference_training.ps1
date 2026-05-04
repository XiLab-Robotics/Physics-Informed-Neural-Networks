param(
    [ValidateSet("Retune", "PaperEval")]
    [string]$Stage = "Retune",
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

# Map The Requested Backward Stage To The Recovered Training Mode.
$normalizedStage = $Stage.Trim()
switch ($normalizedStage) {
    "Retune" {
        $modeName = "retune"
        $runLabel = "bw_v17_retune"
    }
    "PaperEval" {
        $modeName = "paper_eval"
        $runLabel = "bw_v18_paper_reference"
    }
    default {
        throw "Unsupported backward stage: $Stage"
    }
}

# Build The Direction-Specific Archive Root And Run Instance Identifier.
$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$runInstanceId = $runTimestamp + "__" + $runLabel
if (-not [string]::IsNullOrWhiteSpace($OutputSuffix)) {
    $runInstanceId = $runInstanceId + "_" + $OutputSuffix
}

$outputRoot = Join-Path $projectRoot ("models\paper_reference\rcim_original\backward\source_runs\" + $runInstanceId)
New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null

# Build The Recovered-Workflow Training Command.
$argumentList = @(
    "run", "-n", $CondaEnvironmentName,
    $PythonExecutable,
    "-B",
    "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py",
    "--mode", $modeName,
    "--direction", "backward",
    "--test-size", $TestSize.ToString([System.Globalization.CultureInfo]::InvariantCulture),
    "--output-root", $outputRoot
)

if (-not [string]::IsNullOrWhiteSpace($Families)) {
    $argumentList += @("--families", $Families)
}

if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
    $argumentList += @("--dataframe-path", $DataframePath)
}

Write-Host "[INFO] RCIM Original Backward Reference Training" -ForegroundColor Cyan
Write-Host "[INFO] Stage | $normalizedStage" -ForegroundColor Cyan
Write-Host "[INFO] Mode | $modeName" -ForegroundColor Cyan
Write-Host "[INFO] Direction | backward" -ForegroundColor Cyan
Write-Host "[INFO] Output Root | $outputRoot" -ForegroundColor Cyan
if (-not [string]::IsNullOrWhiteSpace($Families)) {
    Write-Host "[INFO] Families | $Families" -ForegroundColor Cyan
}
if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
    Write-Host "[INFO] Dataframe Override | $DataframePath" -ForegroundColor Cyan
}
if ($normalizedStage -eq "PaperEval") {
    Write-Host "[WARNING] This Stage Assumes The Backward Tuned Parameters Have Already Been Transferred Into The Paper-Eval Family Map." -ForegroundColor Yellow
}

$commandPreview = "conda " + (($argumentList | ForEach-Object {
    if ($_ -match '\s') { '"' + $_ + '"' } else { $_ }
}) -join " ")
Write-Host "[INFO] Command | $commandPreview" -ForegroundColor DarkCyan

if ($PrintOnly) {
    Write-Host "[DONE] Print-Only Mode Enabled. No Training Was Launched." -ForegroundColor Green
    exit 0
}

# Launch The Requested Backward Stage.
& conda @argumentList
$nativeExitCode = $LASTEXITCODE

if ($nativeExitCode -ne 0) {
    Write-Host "[ERROR] RCIM Original Backward Reference Training Failed." -ForegroundColor Red
    exit $nativeExitCode
}

if ($normalizedStage -eq "Retune") {
    Write-Host "[DONE] Backward Retune Completed." -ForegroundColor Green
    Write-Host "[DONE] Inspect output_prediction\\summaryBestParameter+*.csv Under | $outputRoot" -ForegroundColor Green
}
else {
    Write-Host "[DONE] Backward Paper-Eval Replay Completed." -ForegroundColor Green
}

Write-Host "[DONE] Output Root | $outputRoot" -ForegroundColor Green
exit 0
