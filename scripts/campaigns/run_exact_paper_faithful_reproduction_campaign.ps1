param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot
. (Join-Path $scriptDirectory "shared_streaming_campaign_launcher.ps1")

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\paper_faithful_reproduction\campaigns\2026-04-10_exact_paper_faithful_reproduction_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_plan_report.md"
$campaignName = "exact_paper_faithful_reproduction_campaign_2026_04_10_21_47_55"
$campaignOutputRoot = Join-Path "output\training_campaigns" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"

New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

# Define Coordinated Run Matrix
$campaignRunList = @(
    @{
        ConfigPath = (Join-Path $campaignConfigRoot "01_exact_paper_recovered_reference.yaml")
        RunnerScriptPath = "scripts\paper_reimplementation\rcim_ml_compensation\run_exact_paper_model_bank_validation.py"
        OutputSuffix = "campaign_run"
        RunnerLabel = "Exact-Paper"
    }
    @{
        ConfigPath = (Join-Path $campaignConfigRoot "02_exact_paper_amplitude_phase_reference.yaml")
        RunnerScriptPath = "scripts\paper_reimplementation\rcim_ml_compensation\run_exact_paper_model_bank_validation.py"
        OutputSuffix = "campaign_run"
        RunnerLabel = "Exact-Paper"
    }
    @{
        ConfigPath = (Join-Path $campaignConfigRoot "03_exact_paper_dominant_harmonic_specialized.yaml")
        RunnerScriptPath = "scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py"
        OutputSuffix = "campaign_run"
        RunnerLabel = "Harmonic-Wise"
    }
    @{
        ConfigPath = (Join-Path $campaignConfigRoot "04_track1_current_best_shared_evaluator_reference.yaml")
        RunnerScriptPath = "scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py"
        OutputSuffix = "campaign_run"
        RunnerLabel = "Harmonic-Wise"
    }
)

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Coordinated Run Count | $($campaignRunList.Count)" -ForegroundColor Cyan

for ($runIndex = 0; $runIndex -lt $campaignRunList.Count; $runIndex++) {
    $campaignRun = $campaignRunList[$runIndex]
    $configPath = $campaignRun.ConfigPath
    $runnerScriptPath = $campaignRun.RunnerScriptPath
    $outputSuffix = $campaignRun.OutputSuffix
    $runnerLabel = $campaignRun.RunnerLabel
    $configFileName = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
    $runLogPath = Join-Path $campaignLogRoot ($configFileName + ".log")

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Campaign Progress {0}/{1} | {2} | {3}" -f ($runIndex + 1), $campaignRunList.Count, $runnerLabel, $configPath) -ForegroundColor Cyan
    Write-Host ("[INFO] Runner Script | {0}" -f $runnerScriptPath) -ForegroundColor Cyan
    Write-Host ("[INFO] Log Path | {0}" -f $runLogPath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    $nativeExitCode = Invoke-CondaRunWithLoggedOutput `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath $runnerScriptPath `
        -ConfigPath $configPath `
        -OutputSuffix $outputSuffix `
        -LogPath $runLogPath

    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Coordinated paper-faithful campaign run failed | $configPath" -ForegroundColor Red
        Write-Host "[ERROR] Failing log file | $runLogPath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Exact-paper faithful reproduction campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
exit 0
