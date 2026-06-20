param(
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
$script:LastWave3GroupedPythonExitCode = 0

Set-Location $projectRoot

function Write-Wave3GroupedStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-Wave3GroupedPython {
    param(
        [string[]]$ArgumentList
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastWave3GroupedPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastWave3GroupedPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastWave3GroupedPythonExitCode = $LASTEXITCODE
}

Write-Wave3GroupedStatus -Label "INFO" -Message "Wave 5.1 grouped harmonic-heads checks only. Training launch is disabled."

$compileArgumentList = @(
    "-m",
    "py_compile",
    "scripts\models\wave3_grouped_harmonic_heads_network.py",
    "scripts\models\model_factory.py",
    "scripts\campaigns\wave_3\validate_wave3_grouped_harmonic_heads_package.py"
)
Invoke-Wave3GroupedPython -ArgumentList $compileArgumentList
if ($script:LastWave3GroupedPythonExitCode -ne 0) {
    exit $script:LastWave3GroupedPythonExitCode
}

$validatorArgumentList = @(
    "scripts\campaigns\wave_3\validate_wave3_grouped_harmonic_heads_package.py"
)
Invoke-Wave3GroupedPython -ArgumentList $validatorArgumentList
if ($script:LastWave3GroupedPythonExitCode -ne 0) {
    exit $script:LastWave3GroupedPythonExitCode
}

Write-Wave3GroupedStatus -Label "DONE" -Message "Wave 5.1 grouped harmonic-heads skeleton is implementation-ready and not campaign-ready."
exit 0
