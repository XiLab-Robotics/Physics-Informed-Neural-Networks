param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\.." )).Path
Set-Location $projectRoot
. (Join-Path $scriptDirectory "invoke_exact_paper_campaign_local.ps1")

$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-18_track1_lgbm_cellwise_reference_campaign"
$planningReportPath = "doc\reports\campaign_plans\track1\exact_paper\2026-04-18-22-28-04_track1_remaining_family_cellwise_reference_campaigns_plan_report.md"
$campaignName = "track1_lgbm_cellwise_reference_campaign_2026_04_18_22_28_04"
$campaignConfigFileNameList = @(
        "01_track1_lgbm_amplitude_0_cellwise_reference.yaml"
    "02_track1_lgbm_amplitude_1_cellwise_reference.yaml"
    "03_track1_lgbm_amplitude_3_cellwise_reference.yaml"
    "04_track1_lgbm_amplitude_39_cellwise_reference.yaml"
    "05_track1_lgbm_amplitude_40_cellwise_reference.yaml"
    "06_track1_lgbm_amplitude_78_cellwise_reference.yaml"
    "07_track1_lgbm_amplitude_81_cellwise_reference.yaml"
    "08_track1_lgbm_amplitude_156_cellwise_reference.yaml"
    "09_track1_lgbm_amplitude_162_cellwise_reference.yaml"
    "10_track1_lgbm_amplitude_240_cellwise_reference.yaml"
    "11_track1_lgbm_phase_1_cellwise_reference.yaml"
    "12_track1_lgbm_phase_3_cellwise_reference.yaml"
    "13_track1_lgbm_phase_39_cellwise_reference.yaml"
    "14_track1_lgbm_phase_40_cellwise_reference.yaml"
    "15_track1_lgbm_phase_78_cellwise_reference.yaml"
    "16_track1_lgbm_phase_81_cellwise_reference.yaml"
    "17_track1_lgbm_phase_156_cellwise_reference.yaml"
    "18_track1_lgbm_phase_162_cellwise_reference.yaml"
    "19_track1_lgbm_phase_240_cellwise_reference.yaml"
)
$campaignConfigPathList = @(
        (Join-Path $campaignConfigRoot "01_track1_lgbm_amplitude_0_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "02_track1_lgbm_amplitude_1_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "03_track1_lgbm_amplitude_3_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "04_track1_lgbm_amplitude_39_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "05_track1_lgbm_amplitude_40_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "06_track1_lgbm_amplitude_78_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "07_track1_lgbm_amplitude_81_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "08_track1_lgbm_amplitude_156_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "09_track1_lgbm_amplitude_162_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "10_track1_lgbm_amplitude_240_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "11_track1_lgbm_phase_1_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "12_track1_lgbm_phase_3_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "13_track1_lgbm_phase_39_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "14_track1_lgbm_phase_40_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "15_track1_lgbm_phase_78_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "16_track1_lgbm_phase_81_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "17_track1_lgbm_phase_156_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "18_track1_lgbm_phase_162_cellwise_reference.yaml")
    (Join-Path $campaignConfigRoot "19_track1_lgbm_phase_240_cellwise_reference.yaml")
)
$runNameList = @(
        "track1_lgbm_amplitude_0_cellwise_reference"
    "track1_lgbm_amplitude_1_cellwise_reference"
    "track1_lgbm_amplitude_3_cellwise_reference"
    "track1_lgbm_amplitude_39_cellwise_reference"
    "track1_lgbm_amplitude_40_cellwise_reference"
    "track1_lgbm_amplitude_78_cellwise_reference"
    "track1_lgbm_amplitude_81_cellwise_reference"
    "track1_lgbm_amplitude_156_cellwise_reference"
    "track1_lgbm_amplitude_162_cellwise_reference"
    "track1_lgbm_amplitude_240_cellwise_reference"
    "track1_lgbm_phase_1_cellwise_reference"
    "track1_lgbm_phase_3_cellwise_reference"
    "track1_lgbm_phase_39_cellwise_reference"
    "track1_lgbm_phase_40_cellwise_reference"
    "track1_lgbm_phase_78_cellwise_reference"
    "track1_lgbm_phase_81_cellwise_reference"
    "track1_lgbm_phase_156_cellwise_reference"
    "track1_lgbm_phase_162_cellwise_reference"
    "track1_lgbm_phase_240_cellwise_reference"
)

if ($Remote) {
    & ".\scripts\campaigns\track1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $campaignName `
        -PlanningReportPath $planningReportPath `
        -LauncherRelativePath "scripts\campaigns\track1\exact_paper\run_track1_lgbm_cellwise_reference_campaign.ps1" `
        -CampaignConfigPathList $campaignConfigPathList `
        -RunNameList $runNameList `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}

$nativeExitCode = Invoke-ExactPaperCampaignLocal `
    -CampaignName $campaignName `
    -PlanningReportPath $planningReportPath `
    -CampaignConfigRoot $campaignConfigRoot `
    -CampaignConfigFileNameList $campaignConfigFileNameList `
    -CondaEnvironmentName $CondaEnvironmentName `
    -PythonExecutable $PythonExecutable
exit $nativeExitCode
