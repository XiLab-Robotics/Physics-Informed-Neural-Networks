param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave1_directional_retraining\campaigns\2026-05-06_wave1_directional_retraining_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_tree_global.yaml"
    "02_tree_fw.yaml"
    "03_tree_bw.yaml"
    "04_residual_harmonic_mlp_global.yaml"
    "05_residual_harmonic_mlp_fw.yaml"
    "06_residual_harmonic_mlp_bw.yaml"
    "07_feedforward_global.yaml"
    "08_feedforward_fw.yaml"
    "09_feedforward_bw.yaml"
    "10_periodic_mlp_global.yaml"
    "11_periodic_mlp_fw.yaml"
    "12_periodic_mlp_bw.yaml"
    "13_harmonic_regression_global.yaml"
    "14_harmonic_regression_fw.yaml"
    "15_harmonic_regression_bw.yaml"
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
    "wave1_directional_retraining_campaign_2026_05_06_16_07_16",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
