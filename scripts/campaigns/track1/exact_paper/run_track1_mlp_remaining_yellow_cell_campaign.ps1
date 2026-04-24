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

$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-22_track1_mlp_remaining_yellow_cell_campaign"
$planningReportPath = "doc\reports\campaign_plans\track1\exact_paper\2026-04-22-01-40-43_track1_remaining_yellow_cell_multi_family_campaign_bundle_plan_report.md"
$campaignName = "track1_mlp_remaining_yellow_cell_campaign_2026_04_22_01_40_43"
$campaignConfigFileNameList = @(Get-ChildItem -LiteralPath $campaignConfigRoot -Filter "*.yaml" | Sort-Object Name | ForEach-Object { $_.Name })
$campaignConfigPathList = $campaignConfigFileNameList | ForEach-Object { Join-Path $campaignConfigRoot $_ }
$runNameList = $campaignConfigFileNameList | ForEach-Object { [System.IO.Path]::GetFileNameWithoutExtension($_) -replace '^[0-9]+_', '' }

if ($Remote) {
    & ".\scripts\campaigns\track1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $campaignName `
        -PlanningReportPath $planningReportPath `
        -LauncherRelativePath "scripts\campaigns\track1\exact_paper\run_track1_mlp_remaining_yellow_cell_campaign.ps1" `
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
