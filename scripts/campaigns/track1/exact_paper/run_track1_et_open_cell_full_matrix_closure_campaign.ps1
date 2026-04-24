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
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\.." )).Path
Set-Location $projectRoot
. (Join-Path $scriptDirectory "invoke_exact_paper_campaign_local.ps1")

$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign"
$planningReportPath = "doc\reports\campaign_plans\track1\exact_paper\2026-04-20-23-50-13_track1_open_cell_full_matrix_closure_campaigns_plan_report.md"
$campaignName = "track1_et_open_cell_full_matrix_closure_campaign_2026_04_20_23_50_13"
$campaignConfigFileNameList = @(
    "001_track1_et_phase_240_closure_attempt_01.yaml"
    "002_track1_et_phase_240_closure_attempt_02.yaml"
    "003_track1_et_phase_240_closure_attempt_03.yaml"
    "004_track1_et_phase_240_closure_attempt_04.yaml"
    "005_track1_et_phase_240_closure_attempt_05.yaml"
    "006_track1_et_phase_240_closure_attempt_06.yaml"
    "007_track1_et_phase_240_closure_attempt_07.yaml"
    "008_track1_et_phase_240_closure_attempt_08.yaml"
    "009_track1_et_phase_240_closure_attempt_09.yaml"
    "010_track1_et_phase_240_closure_attempt_10.yaml"
    "011_track1_et_phase_240_closure_attempt_11.yaml"
    "012_track1_et_phase_240_closure_attempt_12.yaml"
    "013_track1_et_phase_240_closure_attempt_13.yaml"
    "014_track1_et_phase_240_closure_attempt_14.yaml"
    "015_track1_et_phase_240_closure_attempt_15.yaml"
    "016_track1_et_phase_240_closure_attempt_16.yaml"
    "017_track1_et_phase_240_closure_attempt_17.yaml"
    "018_track1_et_phase_240_closure_attempt_18.yaml"
    "019_track1_et_phase_240_closure_attempt_19.yaml"
    "020_track1_et_phase_240_closure_attempt_20.yaml"
    "021_track1_et_phase_240_closure_attempt_21.yaml"
    "022_track1_et_phase_240_closure_attempt_22.yaml"
    "023_track1_et_phase_240_closure_attempt_23.yaml"
    "024_track1_et_phase_240_closure_attempt_24.yaml"
    "025_track1_et_phase_240_closure_attempt_25.yaml"
    "026_track1_et_phase_240_closure_attempt_26.yaml"
    "027_track1_et_phase_240_closure_attempt_27.yaml"
)
$campaignConfigPathList = @(
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\001_track1_et_phase_240_closure_attempt_01.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\002_track1_et_phase_240_closure_attempt_02.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\003_track1_et_phase_240_closure_attempt_03.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\004_track1_et_phase_240_closure_attempt_04.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\005_track1_et_phase_240_closure_attempt_05.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\006_track1_et_phase_240_closure_attempt_06.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\007_track1_et_phase_240_closure_attempt_07.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\008_track1_et_phase_240_closure_attempt_08.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\009_track1_et_phase_240_closure_attempt_09.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\010_track1_et_phase_240_closure_attempt_10.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\011_track1_et_phase_240_closure_attempt_11.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\012_track1_et_phase_240_closure_attempt_12.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\013_track1_et_phase_240_closure_attempt_13.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\014_track1_et_phase_240_closure_attempt_14.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\015_track1_et_phase_240_closure_attempt_15.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\016_track1_et_phase_240_closure_attempt_16.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\017_track1_et_phase_240_closure_attempt_17.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\018_track1_et_phase_240_closure_attempt_18.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\019_track1_et_phase_240_closure_attempt_19.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\020_track1_et_phase_240_closure_attempt_20.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\021_track1_et_phase_240_closure_attempt_21.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\022_track1_et_phase_240_closure_attempt_22.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\023_track1_et_phase_240_closure_attempt_23.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\024_track1_et_phase_240_closure_attempt_24.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\025_track1_et_phase_240_closure_attempt_25.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\026_track1_et_phase_240_closure_attempt_26.yaml"
    "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\track1\exact_paper\forward\open_cell_full_matrix_closure\et\2026-04-20_track1_et_open_cell_full_matrix_closure_campaign\027_track1_et_phase_240_closure_attempt_27.yaml"
)
$runNameList = @(
    "track1_et_phase_240_closure_attempt_01"
    "track1_et_phase_240_closure_attempt_02"
    "track1_et_phase_240_closure_attempt_03"
    "track1_et_phase_240_closure_attempt_04"
    "track1_et_phase_240_closure_attempt_05"
    "track1_et_phase_240_closure_attempt_06"
    "track1_et_phase_240_closure_attempt_07"
    "track1_et_phase_240_closure_attempt_08"
    "track1_et_phase_240_closure_attempt_09"
    "track1_et_phase_240_closure_attempt_10"
    "track1_et_phase_240_closure_attempt_11"
    "track1_et_phase_240_closure_attempt_12"
    "track1_et_phase_240_closure_attempt_13"
    "track1_et_phase_240_closure_attempt_14"
    "track1_et_phase_240_closure_attempt_15"
    "track1_et_phase_240_closure_attempt_16"
    "track1_et_phase_240_closure_attempt_17"
    "track1_et_phase_240_closure_attempt_18"
    "track1_et_phase_240_closure_attempt_19"
    "track1_et_phase_240_closure_attempt_20"
    "track1_et_phase_240_closure_attempt_21"
    "track1_et_phase_240_closure_attempt_22"
    "track1_et_phase_240_closure_attempt_23"
    "track1_et_phase_240_closure_attempt_24"
    "track1_et_phase_240_closure_attempt_25"
    "track1_et_phase_240_closure_attempt_26"
    "track1_et_phase_240_closure_attempt_27"
)

if ($Remote) {
    & ".\scripts\campaigns\track1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $campaignName `
        -PlanningReportPath $planningReportPath `
        -LauncherRelativePath "scripts\campaigns\track1\exact_paper\run_track1_et_open_cell_full_matrix_closure_campaign.ps1" `
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
