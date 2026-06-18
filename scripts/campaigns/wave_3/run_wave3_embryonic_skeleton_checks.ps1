param(
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
$script:LastWave3PythonExitCode = 0

Set-Location $projectRoot

function Write-Wave3Status {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave3Python {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastWave3PythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastWave3PythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastWave3PythonExitCode = $LASTEXITCODE
}

Write-Wave3Status -Label "INFO" -Message "Wave 3 embryonic skeleton checks only. Training launch is disabled."

$compileArgumentList = @(
    "-m",
    "py_compile",
    "scripts\models\wave3_harmonic_prior_residual_network.py",
    "scripts\campaigns\wave_3\validate_wave3_embryonic_skeleton_package.py"
)
Invoke-Wave3Python -ArgumentList $compileArgumentList
if ($script:LastWave3PythonExitCode -ne 0) {
    exit $script:LastWave3PythonExitCode
}

$validatorArgumentList = @(
    "scripts\campaigns\wave_3\validate_wave3_embryonic_skeleton_package.py"
)
Invoke-Wave3Python -ArgumentList $validatorArgumentList
if ($script:LastWave3PythonExitCode -ne 0) {
    exit $script:LastWave3PythonExitCode
}

Write-Wave3Status -Label "DONE" -Message "Wave 3 skeleton is implementation-ready and not campaign-ready."
exit 0
