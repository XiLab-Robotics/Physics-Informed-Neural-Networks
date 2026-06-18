param(
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
$script:LastWave3PythonExitCode = 0

Set-Location $projectRoot

function Write-Wave3SmokeStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave3SmokePython {
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

Write-Wave3SmokeStatus -Label "INFO" -Message "Wave 3 training-smoke-ready checks only. No campaign is launched."

$compileArgumentList = @(
    "-m",
    "py_compile",
    "scripts\campaigns\wave_3\validate_wave3_training_smoke_ready.py"
)
Invoke-Wave3SmokePython -ArgumentList $compileArgumentList
if ($script:LastWave3PythonExitCode -ne 0) {
    exit $script:LastWave3PythonExitCode
}

$validatorArgumentList = @(
    "scripts\campaigns\wave_3\validate_wave3_training_smoke_ready.py"
)
Invoke-Wave3SmokePython -ArgumentList $validatorArgumentList
if ($script:LastWave3PythonExitCode -ne 0) {
    exit $script:LastWave3PythonExitCode
}

Write-Wave3SmokeStatus -Label "DONE" -Message "Wave 3 skeleton is training-smoke-ready and still not campaign-ready."
exit 0
