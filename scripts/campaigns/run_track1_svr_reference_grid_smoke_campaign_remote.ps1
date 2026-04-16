param(
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path
$sourcePath = Join-Path $scriptDirectory "run_track1_svr_reference_grid_search_repair_campaign_remote.ps1"
$sourceText = Get-Content $sourcePath -Raw
$resolvedScriptDirectoryLiteral = $scriptDirectory.Replace("'", "''")
$resolvedProjectRootLiteral = $projectRoot.Replace("'", "''")

$sourceText = $sourceText.Replace(
    '$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path',
    ('$scriptDirectory = ''{0}''' -f $resolvedScriptDirectoryLiteral)
)
$sourceText = $sourceText.Replace(
    '$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path',
    ('$projectRoot = ''{0}''' -f $resolvedProjectRootLiteral)
)

$sourceText = $sourceText.Replace(
    '$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-14_track1_svr_reference_grid_search_repair_campaign"',
    '$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-16_track1_svr_reference_grid_smoke_campaign"'
)
$sourceText = $sourceText.Replace(
    '$planningReportPath = "doc\reports\campaign_plans\2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md"',
    '$planningReportPath = "doc\reports\campaign_plans\2026-04-16-12-45-00_track1_svr_reference_grid_smoke_campaign_plan_report.md"'
)
$sourceText = $sourceText.Replace(
    '$campaignName = "track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48"',
    '$campaignName = "track1_svr_reference_grid_smoke_campaign_2026_04_16_12_45_00"'
)
$sourceText = $sourceText.Replace(
    'run_track1_svr_reference_grid_search_repair_campaign.ps1',
    'run_track1_svr_reference_grid_smoke_campaign.ps1'
)
$oldCampaignListBlock = @'
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_track1_svr_reference_grid_amplitude_pair.yaml")
    (Join-Path $campaignConfigRoot "02_track1_svr_reference_grid_amplitude_40_only.yaml")
    (Join-Path $campaignConfigRoot "03_track1_svr_reference_grid_amplitude_240_only.yaml")
    (Join-Path $campaignConfigRoot "04_track1_svr_reference_grid_phase_162_only.yaml")
)
$runNameList = @(
    "track1_svr_reference_grid_amplitude_pair"
    "track1_svr_reference_grid_amplitude_40_only"
    "track1_svr_reference_grid_amplitude_240_only"
    "track1_svr_reference_grid_phase_162_only"
)
'@
$newCampaignListBlock = @'
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_track1_svr_reference_grid_amplitude_40_smoke_singlecore.yaml")
)
$runNameList = @(
    "track1_svr_reference_grid_amplitude_40_smoke_singlecore"
)
'@
$sourceText = $sourceText.Replace($oldCampaignListBlock, $newCampaignListBlock)

$temporaryWrapperPath = Join-Path $env:TEMP ("track1_svr_reference_grid_smoke_campaign_remote_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))

try {
    [System.IO.File]::WriteAllText($temporaryWrapperPath, $sourceText, [System.Text.UTF8Encoding]::new($false))
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $temporaryWrapperPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}
finally {
    if (Test-Path -LiteralPath $temporaryWrapperPath) {
        Remove-Item -LiteralPath $temporaryWrapperPath -Force -ErrorAction SilentlyContinue
    }
}
