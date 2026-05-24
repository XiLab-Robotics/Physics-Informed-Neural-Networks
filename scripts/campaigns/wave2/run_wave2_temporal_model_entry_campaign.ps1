param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave2_temporal_model_entry\campaigns\2026-05-24_wave2_temporal_model_entry_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave2\2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_temporal_convolution_global.yaml"
    "02_temporal_convolution_fw.yaml"
    "03_temporal_convolution_bw.yaml"
    "04_gru_sequence_global.yaml"
    "05_gru_sequence_fw.yaml"
    "06_gru_sequence_bw.yaml"
    "07_lstm_sequence_global.yaml"
    "08_lstm_sequence_fw.yaml"
    "09_lstm_sequence_bw.yaml"
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
    "wave2_temporal_model_entry_campaign_2026_05_24_11_01_15",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
