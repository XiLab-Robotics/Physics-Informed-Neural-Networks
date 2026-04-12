param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

function Invoke-CondaRunWithLoggedOutput {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix,
        [string]$LogPath
    )

    $previousErrorActionPreference = $ErrorActionPreference
    $global:ErrorActionPreference = "Continue"

    try {
        $commandOutput = & conda run -n $EnvironmentName $PythonExecutablePath `
            $RunnerScriptPath `
            --config-path $ConfigPath `
            --output-suffix $OutputSuffix 2>&1
        $nativeExitCode = $LASTEXITCODE
    }
    finally {
        $global:ErrorActionPreference = $previousErrorActionPreference
    }

    $commandOutput | Tee-Object -FilePath $LogPath | ForEach-Object {
        Write-Host $_
    }
    return $nativeExitCode
}

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-10_exact_paper_model_bank_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md"
$campaignName = "exact_paper_model_bank_campaign_2026_04_10_17_04_41"
$campaignOutputRoot = Join-Path "output\training_campaigns" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"

New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_exact_full_bank_diagnostic_continue.yaml")
    (Join-Path $campaignConfigRoot "02_exact_full_bank_strict_reference.yaml")
    (Join-Path $campaignConfigRoot "03_exact_svr_export_diagnostic.yaml")
    (Join-Path $campaignConfigRoot "04_exact_non_svr_export_reference.yaml")
)

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Exact-Paper Run Count | $($campaignConfigPathList.Count)" -ForegroundColor Cyan

for ($configIndex = 0; $configIndex -lt $campaignConfigPathList.Count; $configIndex++) {
    $configPath = $campaignConfigPathList[$configIndex]
    $configFileName = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
    $runLogPath = Join-Path $campaignLogRoot ($configFileName + ".log")

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Exact-Paper Campaign Progress {0}/{1} | {2}" -f ($configIndex + 1), $campaignConfigPathList.Count, $configPath) -ForegroundColor Cyan
    Write-Host ("[INFO] Log Path | {0}" -f $runLogPath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    $nativeExitCode = Invoke-CondaRunWithLoggedOutput `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath "scripts\paper_reimplementation\rcim_ml_compensation\run_exact_paper_model_bank_validation.py" `
        -ConfigPath $configPath `
        -OutputSuffix "campaign_run" `
        -LogPath $runLogPath

    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Exact-paper campaign run failed | $configPath" -ForegroundColor Red
        Write-Host "[ERROR] Failing log file | $runLogPath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Exact-paper campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
exit 0
