param(
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
$script:LastWave4BPythonExitCode = 0

Set-Location $projectRoot

function Write-Wave4BStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave4BPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastWave4BPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastWave4BPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastWave4BPythonExitCode = $LASTEXITCODE
}

Write-Wave4BStatus -Label "INFO" -Message "Wave 4B MMT feature-generator checks only. Training launch is disabled."

$compileArgumentList = @(
    "-m",
    "py_compile",
    "scripts\features\wave4b_mmt_feature_generator.py",
    "scripts\campaigns\wave4\validate_wave4b_mmt_feature_generator_package.py"
)
Invoke-Wave4BPython -ArgumentList $compileArgumentList
if ($script:LastWave4BPythonExitCode -ne 0) {
    exit $script:LastWave4BPythonExitCode
}

$validatorArgumentList = @(
    "scripts\campaigns\wave4\validate_wave4b_mmt_feature_generator_package.py"
)
Invoke-Wave4BPython -ArgumentList $validatorArgumentList
if ($script:LastWave4BPythonExitCode -ne 0) {
    exit $script:LastWave4BPythonExitCode
}

Write-Wave4BStatus -Label "DONE" -Message "Wave 4B MMT feature-generator skeleton is implementation-ready and not campaign-ready."
exit 0
