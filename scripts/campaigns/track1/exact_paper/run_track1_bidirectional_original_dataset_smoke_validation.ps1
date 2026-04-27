param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$ConfigRoot = Join-Path $ProjectRoot "config\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\smoke"
$RunnerPath = Join-Path $ProjectRoot "scripts\paper_reimplementation\rcim_ml_compensation\run_original_dataset_exact_model_bank_validation.py"

$ConfigPathList = Get-ChildItem -Path $ConfigRoot -Filter *.yaml -Recurse | Sort-Object FullName
if ($ConfigPathList.Count -eq 0) {
    throw "No smoke configs found under $ConfigRoot"
}

foreach ($ConfigPath in $ConfigPathList) {
    Write-Host "[INFO] Running smoke validation | $($ConfigPath.FullName)" -ForegroundColor Cyan
    conda run -n $CondaEnvironmentName $PythonExecutable $RunnerPath --config-path $ConfigPath.FullName --output-suffix smoke_validation
    if ($LASTEXITCODE -ne 0) {
        throw "Smoke validation failed | $($ConfigPath.FullName)"
    }
}

Write-Host "[DONE] Track 1 bidirectional original-dataset smoke validation completed" -ForegroundColor Green
