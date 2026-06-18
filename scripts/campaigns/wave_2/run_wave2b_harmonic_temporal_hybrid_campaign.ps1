param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave2b_harmonic_temporal_hybrid\campaigns\2026-05-25_wave2b_harmonic_temporal_hybrid_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave_2\2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_periodic_temporal_convolution_global.yaml"
    "02_periodic_temporal_convolution_fw.yaml"
    "03_periodic_temporal_convolution_bw.yaml"
    "04_periodic_gru_sequence_global.yaml"
    "05_periodic_gru_sequence_fw.yaml"
    "06_periodic_gru_sequence_bw.yaml"
    "07_periodic_lstm_sequence_global.yaml"
    "08_periodic_lstm_sequence_fw.yaml"
    "09_periodic_lstm_sequence_bw.yaml"
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
    "wave2b_harmonic_temporal_hybrid_campaign_2026_05_25",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
