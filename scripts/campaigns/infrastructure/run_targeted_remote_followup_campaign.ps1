param(
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

# Define Campaign Identity
$campaignConfigRoot = "config\training\remote_followup\campaigns\2026-04-04_targeted_remote_followup_campaign"
$planningReportPath = "doc\reports\campaign_plans\infrastructure\2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md"
$campaignName = "targeted_remote_followup_campaign_2026_04_04_11_21_09"

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_residual_h12_deep_long_remote.yaml")
    (Join-Path $campaignConfigRoot "02_residual_h12_deep_dense_remote.yaml")
    (Join-Path $campaignConfigRoot "03_feedforward_high_compute_long_remote.yaml")
    (Join-Path $campaignConfigRoot "04_feedforward_stride1_high_compute_long_remote.yaml")
    (Join-Path $campaignConfigRoot "05_hist_gbr_remote_refined.yaml")
)
$sourceSyncPathList = @(
    "scripts"
    "config"
    "requirements.txt"
)

# Launch Operator-Triggered Remote Campaign Through The Canonical Sync Wrapper
& ".\scripts\campaigns\infrastructure\run_remote_training_campaign.ps1" `
    -CampaignConfigPathList $campaignConfigPathList `
    -CampaignName $campaignName `
    -PlanningReportPath $planningReportPath `
    -RemoteHostAlias $RemoteHostAlias `
    -RemoteRepositoryPath $RemoteRepositoryPath `
    -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
    -SourceSyncPathList $sourceSyncPathList

exit $LASTEXITCODE
