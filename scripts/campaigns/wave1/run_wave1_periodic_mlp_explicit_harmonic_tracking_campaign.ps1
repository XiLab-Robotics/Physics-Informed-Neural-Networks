param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave1_periodic_mlp_explicit_harmonic_tracking\campaigns\2026-05-20_wave1_periodic_mlp_explicit_harmonic_tracking_campaign\queue"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignConfigFileNameList = @(
    "01_periodic_mlp_global_rcim_sparse.yaml"
    "02_periodic_mlp_global_dense240.yaml"
    "03_periodic_mlp_global_dense360.yaml"
    "04_periodic_mlp_fw_rcim_sparse.yaml"
    "05_periodic_mlp_fw_dense240.yaml"
    "06_periodic_mlp_fw_dense360.yaml"
    "07_periodic_mlp_bw_rcim_sparse.yaml"
    "08_periodic_mlp_bw_dense240.yaml"
    "09_periodic_mlp_bw_dense360.yaml"
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
    "wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
