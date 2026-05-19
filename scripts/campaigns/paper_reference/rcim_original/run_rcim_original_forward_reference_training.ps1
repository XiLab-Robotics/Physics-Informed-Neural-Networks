param(
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$PythonExecutable = "python",
    [string]$Families = "",
    [double]$TestSize = 0.20,
    [string]$OutputSuffix = "",
    [string]$DataframePath = "",
    [int]$RetuneGridSearchVerbose = 10,
    [int]$RetuneCrossValidateVerbose = 10,
    [switch]$SkipPaperEval,
    [switch]$SkipPaperExport,
    [switch]$PrintOnly
)

$ErrorActionPreference = "Stop"

# Resolve The Repository Root From The Script Location.
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path
Set-Location $projectRoot

# Delegate To The Unified Launcher While Preserving The Historical Wrapper Surface.
& (Join-Path $scriptDirectory "run_rcim_original_reference_training.ps1") `
    -Branch Forward `
    -Stage Original `
    -CondaEnvironmentName $CondaEnvironmentName `
    -PythonExecutable $PythonExecutable `
    -Families $Families `
    -TestSize $TestSize `
    -OutputSuffix $OutputSuffix `
    -DataframePath $DataframePath `
    -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
    -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
    -NoEval:$SkipPaperEval `
    -NoExport:$SkipPaperExport `
    -PrintOnly:$PrintOnly

exit $LASTEXITCODE
