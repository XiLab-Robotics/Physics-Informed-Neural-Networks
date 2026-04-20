param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path

Set-Location $projectRoot
. (Join-Path $projectRoot "scripts\campaigns\infrastructure\shared_streaming_campaign_launcher.ps1")

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-14_track1_full_matrix_family_reproduction_campaign"
$planningReportPath = "doc\reports\campaign_plans\track1\exact_paper\2026-04-14-13-42-10_track1_full_matrix_family_reproduction_campaign_plan_report.md"
$campaignName = "track1_full_matrix_family_reproduction_campaign_2026_04_14_13_50_51"
$campaignOutputRoot = Join-Path "output\training_campaigns\track1\exact_paper" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"

New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_track1_svm_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "02_track1_svm_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "03_track1_mlp_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "04_track1_mlp_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "05_track1_rf_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "06_track1_rf_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "07_track1_dt_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "08_track1_dt_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "09_track1_et_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "10_track1_et_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "11_track1_ert_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "12_track1_ert_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "13_track1_gbm_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "14_track1_gbm_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "15_track1_hgbm_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "16_track1_hgbm_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "17_track1_xgbm_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "18_track1_xgbm_phase_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "19_track1_lgbm_amplitude_full_matrix.yaml")
    (Join-Path $campaignConfigRoot "20_track1_lgbm_phase_full_matrix.yaml")
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
Write-Host "[DONE] Exact-paper full-matrix family reproduction campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
exit 0
