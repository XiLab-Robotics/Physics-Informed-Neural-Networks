param(
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

# Define Campaign Identity
$campaignConfigRoot = "config\training\remote_validation\campaigns\2026-04-03_remote_training_validation_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-03-17-54-21_remote_training_validation_campaign_plan_report.md"
$campaignName = "remote_training_validation_campaign_2026_04_03_17_54_21"

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_random_forest_remote_medium.yaml")
    (Join-Path $campaignConfigRoot "02_random_forest_remote_aggressive.yaml")
    (Join-Path $campaignConfigRoot "03_hist_gbr_remote_deep.yaml")
    (Join-Path $campaignConfigRoot "04_feedforward_high_compute_remote.yaml")
    (Join-Path $campaignConfigRoot "05_feedforward_stride1_big_remote.yaml")
)
$sourceSyncPathList = @(
    "scripts"
    "config"
    "requirements.txt"
)

# Launch Operator-Triggered Remote Campaign Through The Canonical Sync Wrapper
& ".\scripts\campaigns\run_remote_training_campaign.ps1" `
    -CampaignConfigPathList $campaignConfigPathList `
    -CampaignName $campaignName `
    -PlanningReportPath $planningReportPath `
    -RemoteHostAlias $RemoteHostAlias `
    -RemoteRepositoryPath $RemoteRepositoryPath `
    -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
    -SourceSyncPathList $sourceSyncPathList

exit $LASTEXITCODE
