param(
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
$script:LastWave4PythonExitCode = 0

Set-Location $projectRoot

function Write-Wave4Status {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave4Python {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastWave4PythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastWave4PythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastWave4PythonExitCode = $LASTEXITCODE
}

Write-Wave4Status -Label "INFO" -Message "Wave 4 embryonic skeleton checks only. Training launch is disabled."

$compileArgumentList = @(
    "-m",
    "py_compile",
    "scripts\models\wave4_mmt_diagnostic_adapter.py",
    "scripts\campaigns\wave_4\validate_wave4_embryonic_skeleton_package.py"
)
Invoke-Wave4Python -ArgumentList $compileArgumentList
if ($script:LastWave4PythonExitCode -ne 0) {
    exit $script:LastWave4PythonExitCode
}

$validatorArgumentList = @(
    "scripts\campaigns\wave_4\validate_wave4_embryonic_skeleton_package.py"
)
Invoke-Wave4Python -ArgumentList $validatorArgumentList
if ($script:LastWave4PythonExitCode -ne 0) {
    exit $script:LastWave4PythonExitCode
}

Write-Wave4Status -Label "DONE" -Message "Wave 4A skeleton is implementation-ready and not campaign-ready."
exit 0
