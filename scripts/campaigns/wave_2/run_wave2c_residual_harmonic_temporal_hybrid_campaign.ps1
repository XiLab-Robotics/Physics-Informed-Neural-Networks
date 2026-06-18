param(
    [switch]$Remote,
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave2c_residual_harmonic_temporal_hybrid\campaigns\2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave_2\2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_residual_harmonic_gru_sequence_sparse_rcim_global.yaml"
    "02_residual_harmonic_gru_sequence_sparse_rcim_fw.yaml"
    "03_residual_harmonic_gru_sequence_sparse_rcim_bw.yaml"
    "04_residual_harmonic_gru_sequence_dense_240_global.yaml"
    "05_residual_harmonic_gru_sequence_dense_240_fw.yaml"
    "06_residual_harmonic_gru_sequence_dense_240_bw.yaml"
    "07_residual_harmonic_gru_sequence_dense_360_global.yaml"
    "08_residual_harmonic_gru_sequence_dense_360_fw.yaml"
    "09_residual_harmonic_gru_sequence_dense_360_bw.yaml"
    "10_residual_harmonic_lstm_sequence_sparse_rcim_global.yaml"
    "11_residual_harmonic_lstm_sequence_sparse_rcim_fw.yaml"
    "12_residual_harmonic_lstm_sequence_sparse_rcim_bw.yaml"
    "13_residual_harmonic_lstm_sequence_dense_240_global.yaml"
    "14_residual_harmonic_lstm_sequence_dense_240_fw.yaml"
    "15_residual_harmonic_lstm_sequence_dense_240_bw.yaml"
    "16_residual_harmonic_lstm_sequence_dense_360_global.yaml"
    "17_residual_harmonic_lstm_sequence_dense_360_fw.yaml"
    "18_residual_harmonic_lstm_sequence_dense_360_bw.yaml"
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

if ($Remote) {
    $remoteLauncherPath = "scripts\campaigns\infrastructure\run_remote_training_campaign.ps1"
    $sourceSyncPathList = @("scripts", "config", "doc", "requirements.txt", "AGENTS.md")

    & $remoteLauncherPath `
        -CampaignConfigPathList $campaignConfigPathList `
        -CampaignName "wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27" `
        -PlanningReportPath $planningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList $sourceSyncPathList
    exit $LASTEXITCODE
}

$argumentList = @(
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    "wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
