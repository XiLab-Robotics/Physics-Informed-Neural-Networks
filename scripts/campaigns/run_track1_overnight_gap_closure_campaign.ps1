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
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\harmonic_wise\campaigns\2026-04-13_track1_overnight_gap_closure_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md"
$campaignName = "track1_overnight_gap_closure_campaign_2026_04_13_01_02_23"
$campaignOutputRoot = Join-Path "output\training_campaigns" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"

New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

# Define Coordinated Run Matrix
$campaignRunList = @(
    @{ ConfigPath = (Join-Path $campaignConfigRoot "01_track1_hgbm_h01_deeper_low_order.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "02_track1_hgbm_h013_deeper_low_order.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "03_track1_hgbm_h01_ultradeep_guarded.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "04_track1_hgbm_h01_shallow_regularized.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "05_track1_hgbm_h0139_low_order_anchor.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "06_track1_hgbm_h014078_low_order_anchor.yaml"); GroupLabel = "Campaign A"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "07_track1_hgbm_h162_h240_repair.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "08_track1_hgbm_h081_h162_h240_repair.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "09_track1_hgbm_h156_h162_h240_repair.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "10_track1_hgbm_h039_h162_h240_bridge.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "11_track1_hgbm_h013_h162_h240_joint.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "12_track1_hgbm_h240_extreme_focus.yaml"); GroupLabel = "Campaign B"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "13_track1_rf_full_rcim_reference.yaml"); GroupLabel = "Campaign C"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "14_track1_rf_h01_focus.yaml"); GroupLabel = "Campaign C"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "15_track1_rf_h081_focus.yaml"); GroupLabel = "Campaign C"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "16_track1_rf_h156_h162_h240_focus.yaml"); GroupLabel = "Campaign C"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "17_track1_hgbm_h01_engineered_recheck.yaml"); GroupLabel = "Campaign D"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "18_track1_hgbm_h013_engineered_recheck.yaml"); GroupLabel = "Campaign D"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "19_track1_hgbm_h162_h240_engineered_recheck.yaml"); GroupLabel = "Campaign D"; RunnerLabel = "Harmonic-Wise" }
    @{ ConfigPath = (Join-Path $campaignConfigRoot "20_track1_rf_h01_h081_engineered_recheck.yaml"); GroupLabel = "Campaign D"; RunnerLabel = "Harmonic-Wise" }
)

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Coordinated Run Count | $($campaignRunList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Logical Campaign Blocks | Campaign A, Campaign B, Campaign C, Campaign D" -ForegroundColor Cyan

for ($runIndex = 0; $runIndex -lt $campaignRunList.Count; $runIndex++) {
    $campaignRun = $campaignRunList[$runIndex]
    $configPath = $campaignRun.ConfigPath
    $groupLabel = $campaignRun.GroupLabel
    $runnerLabel = $campaignRun.RunnerLabel
    $configFileName = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
    $runLogPath = Join-Path $campaignLogRoot ($configFileName + ".log")

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Campaign Progress {0}/{1} | {2} | {3}" -f ($runIndex + 1), $campaignRunList.Count, $groupLabel, $configPath) -ForegroundColor Cyan
    Write-Host ("[INFO] Runner Script | scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py") -ForegroundColor Cyan
    Write-Host ("[INFO] Log Path | {0}" -f $runLogPath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    $nativeExitCode = Invoke-CondaRunWithLoggedOutput `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath "scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py" `
        -ConfigPath $configPath `
        -OutputSuffix "campaign_run" `
        -LogPath $runLogPath

    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Track 1 overnight campaign run failed | $configPath" -ForegroundColor Red
        Write-Host "[ERROR] Failing log file | $runLogPath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Track 1 overnight gap-closure campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
exit 0
