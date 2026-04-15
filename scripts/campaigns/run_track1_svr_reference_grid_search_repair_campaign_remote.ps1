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
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-14_track1_svr_reference_grid_search_repair_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md"
$campaignName = "track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48"

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_track1_svr_reference_grid_amplitude_pair.yaml")
    (Join-Path $campaignConfigRoot "02_track1_svr_reference_grid_amplitude_40_only.yaml")
    (Join-Path $campaignConfigRoot "03_track1_svr_reference_grid_amplitude_240_only.yaml")
    (Join-Path $campaignConfigRoot "04_track1_svr_reference_grid_phase_162_only.yaml")
)
$sourceSyncPathList = @(
    "scripts"
    "config"
    "doc"
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
