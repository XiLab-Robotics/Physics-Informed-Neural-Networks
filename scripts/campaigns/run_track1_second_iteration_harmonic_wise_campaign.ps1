param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

function Invoke-CondaRun {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix
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

    $commandOutput | ForEach-Object {
        Write-Host $_
    }

    return $nativeExitCode
}

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\harmonic_wise\campaigns\2026-04-09_track1_second_iteration_harmonic_wise_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md"
$campaignName = "track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03"

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_full_rcim_baseline_reference.yaml")
    (Join-Path $campaignConfigRoot "02_h013_engineered_stage1.yaml")
    (Join-Path $campaignConfigRoot "03_h013_random_forest_diagnostic.yaml")
    (Join-Path $campaignConfigRoot "04_h01340_engineered_stage2.yaml")
    (Join-Path $campaignConfigRoot "05_h0134078_engineered_stage3.yaml")
    (Join-Path $campaignConfigRoot "06_full_rcim_no_engineering_reference.yaml")
    (Join-Path $campaignConfigRoot "07_full_rcim_engineered_balanced.yaml")
    (Join-Path $campaignConfigRoot "08_full_rcim_engineered_deeper.yaml")
)

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Harmonic-Wise Run Count | $($campaignConfigPathList.Count)" -ForegroundColor Cyan

for ($configIndex = 0; $configIndex -lt $campaignConfigPathList.Count; $configIndex++) {
    $configPath = $campaignConfigPathList[$configIndex]
    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Harmonic-Wise Campaign Progress {0}/{1} | {2}" -f ($configIndex + 1), $campaignConfigPathList.Count, $configPath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    $nativeExitCode = Invoke-CondaRun `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath "scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py" `
        -ConfigPath $configPath `
        -OutputSuffix "campaign_run"

    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Harmonic-wise campaign run failed | $configPath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Harmonic-wise campaign completed successfully" -ForegroundColor Green
exit 0
