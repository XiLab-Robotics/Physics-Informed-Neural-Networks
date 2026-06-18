param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave1_high_order_harmonic_tracking\campaigns\2026-05-19_wave1_high_order_harmonic_tracking_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave_1\2026-05-19-17-40-01_wave1_high_order_harmonic_tracking_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_harmonic_regression_global_rcim_sparse.yaml"
    "02_harmonic_regression_global_dense240.yaml"
    "03_harmonic_regression_global_dense360.yaml"
    "04_harmonic_regression_fw_rcim_sparse.yaml"
    "05_harmonic_regression_fw_dense240.yaml"
    "06_harmonic_regression_fw_dense360.yaml"
    "07_harmonic_regression_bw_rcim_sparse.yaml"
    "08_harmonic_regression_bw_dense240.yaml"
    "09_harmonic_regression_bw_dense360.yaml"
    "10_residual_harmonic_global_rcim_sparse.yaml"
    "11_residual_harmonic_global_dense240.yaml"
    "12_residual_harmonic_global_dense360.yaml"
    "13_residual_harmonic_fw_rcim_sparse.yaml"
    "14_residual_harmonic_fw_dense240.yaml"
    "15_residual_harmonic_fw_dense360.yaml"
    "16_residual_harmonic_bw_rcim_sparse.yaml"
    "17_residual_harmonic_bw_dense240.yaml"
    "18_residual_harmonic_bw_dense360.yaml"
)

foreach ($queueSubdirectoryName in @("pending", "running")) {
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path $queueSubdirectoryPath)) {
        continue
    }

    foreach ($campaignConfigFileName in $campaignConfigFileNameList) {
        Get-ChildItem -Path $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -like "*$campaignConfigFileName" } |
            Remove-Item -Force
    }
}

$campaignConfigPathList = $campaignConfigFileNameList | ForEach-Object {
    Join-Path $campaignConfigRoot $_
}

$argumentList = @(
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    "wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
