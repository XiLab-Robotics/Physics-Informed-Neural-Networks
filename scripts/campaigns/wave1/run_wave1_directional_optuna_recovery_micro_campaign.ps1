param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$GpuId = "0"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

function Get-EnvironmentPythonPath {
    param(
        [string]$RequestedCondaEnvironmentName
    )

    if ([string]::IsNullOrWhiteSpace($RequestedCondaEnvironmentName)) {
        return $null
    }

    $condaExecutablePath = (where.exe conda.exe 2>$null | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
        return $null
    }

    try {
        $environmentListJson = (& $condaExecutablePath env list --json 2>$null | Out-String)
        if (-not [string]::IsNullOrWhiteSpace($environmentListJson)) {
            $environmentList = $environmentListJson | ConvertFrom-Json
            foreach ($environmentPath in $environmentList.envs) {
                if ((Split-Path -Leaf $environmentPath) -eq $RequestedCondaEnvironmentName) {
                    $candidatePythonPath = Join-Path $environmentPath "python.exe"
                    if (Test-Path $candidatePythonPath) {
                        return (Resolve-Path $candidatePythonPath).Path
                    }
                }
            }
        }
    }
    catch {
    }

    $condaBasePath = (& $condaExecutablePath info --base 2>$null | Select-Object -Last 1)
    if (-not [string]::IsNullOrWhiteSpace($condaBasePath)) {
        $environmentPythonPath = Join-Path $condaBasePath.Trim() ("envs\" + $RequestedCondaEnvironmentName + "\python.exe")
        if (Test-Path $environmentPythonPath) {
            return (Resolve-Path $environmentPythonPath).Path
        }
    }

    return $null
}

function Resolve-PythonExecutablePath {
    param(
        [string]$RequestedPythonExecutable,
        [string]$RequestedCondaEnvironmentName
    )

    if (-not [string]::IsNullOrWhiteSpace($env:CONDA_PREFIX)) {
        $activeEnvironmentPythonPath = Join-Path $env:CONDA_PREFIX "python.exe"
        if (
            (Test-Path $activeEnvironmentPythonPath) -and
            ((Split-Path -Leaf $env:CONDA_PREFIX) -eq $RequestedCondaEnvironmentName) -and
            [string]::Equals($RequestedPythonExecutable, "python", [System.StringComparison]::OrdinalIgnoreCase)
        ) {
            return (Resolve-Path $activeEnvironmentPythonPath).Path
        }
    }

    $environmentPythonPath = Get-EnvironmentPythonPath -RequestedCondaEnvironmentName $RequestedCondaEnvironmentName
    if (
        -not [string]::IsNullOrWhiteSpace($environmentPythonPath) -and
        [string]::Equals($RequestedPythonExecutable, "python", [System.StringComparison]::OrdinalIgnoreCase)
    ) {
        return $environmentPythonPath
    }

    if (Test-Path $RequestedPythonExecutable) {
        return (Resolve-Path $RequestedPythonExecutable).Path
    }

    $resolvedCommand = Get-Command $RequestedPythonExecutable -ErrorAction SilentlyContinue
    if ($null -ne $resolvedCommand) {
        return $resolvedCommand.Source
    }

    throw "Unable to resolve Python executable | requested=$RequestedPythonExecutable"
}

Set-Location $projectRoot

$resolvedPythonExecutablePath = Resolve-PythonExecutablePath `
    -RequestedPythonExecutable $PythonExecutable `
    -RequestedCondaEnvironmentName $CondaEnvironmentName

$campaignRoot = "config\training\wave1_directional_optuna_recovery_micro\campaigns\2026-05-12_wave1_directional_optuna_recovery_micro_campaign"
$studyConfigPath = Join-Path $campaignRoot "optuna_studies\feedforward_recovery_micro.yaml"

Write-Host "[INFO] Resolved Python executable | $resolvedPythonExecutablePath" -ForegroundColor Cyan
& $resolvedPythonExecutablePath -c "import optuna, sys; print(sys.executable)"
if ($LASTEXITCODE -ne 0) {
    throw "Optuna import preflight failed for Python executable | $resolvedPythonExecutablePath"
}

& $resolvedPythonExecutablePath `
    "scripts\training\run_optuna_neural_hpo_study.py" `
    "--study-config-path" $studyConfigPath `
    "--gpu-id" $GpuId

if ($LASTEXITCODE -ne 0) {
    throw "Recovery micro-campaign failed | exit_code=$LASTEXITCODE"
}

Write-Host "[DONE] Wave 1 directional Optuna recovery micro-campaign completed" -ForegroundColor Green
