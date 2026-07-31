param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$Run,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location -LiteralPath $ProjectRoot

$CampaignName = "wave52r_offline_leader_cross_surface_promotion_2026_07_30"
$CampaignScriptPath = "scripts/campaigns/wave_5_2/run_wave52r_offline_leader_cross_surface_promotion.py"
$CampaignConfigurationPath = "config/training/wave52r_offline_leader_cross_surface_promotion/campaigns/2026-07-30_wave52r_offline_leader_cross_surface_promotion/campaign.yaml"
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/offline_leader_global_promotion/2026-07-30-17-35-29_wave52r_offline_leader_global_promotion_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-30/2026-07-30-17-35-29_wave52r_offline_leader_global_promotion_and_four_leader_portfolio.md"
$LocalGateSummaryPath = "output/validation_checks/wave52r_offline_leader_promotion/2026-07-30-19-24-35__wave52r_offline_leader_promotion/promotion_gate_summary.yaml"
$script:LastPythonExitCode = 0

function Write-PromotionStatus {
    param([string]$Label, [string]$Message)

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-PromotionPython {
    param([string[]]$ArgumentList)

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }
    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }
    $CondaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $CondaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}

foreach ($RequiredPath in @(
    $CampaignScriptPath,
    $CampaignConfigurationPath,
    $PlanningReportPath,
    $TechnicalDocumentPath,
    $LocalGateSummaryPath,
    "scripts/models/causal_temporal_analytical_residual_network.py",
    "scripts/models/complex_harmonic_coefficient_residual_network.py",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations/phase0_curve_audit.csv",
    "data/polished_dataset"
)) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required promotion-campaign path is missing | $RequiredPath"
    }
}

Write-PromotionStatus -Label "INFO" -Message "Campaign: $CampaignName"
Write-PromotionStatus -Label "INFO" -Message "Scope: polished_dataset / setpoints / Fw + Bw + global / K01 + H08"
Write-PromotionStatus -Label "INFO" -Message "Incumbents: periodic GRU and periodic harmonic MLP remain frozen controls."
Write-PromotionStatus -Label "STEP" -Message "Running cross-surface dataset, model, provenance, and package preflight."
Invoke-PromotionPython -ArgumentList @("-B", $CampaignScriptPath, "--preflight-only")
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly -or -not $Run) {
    Write-PromotionStatus -Label "DONE" -Message "Preflight completed without campaign execution."
    exit 0
}

if (-not $Remote) {
    Write-PromotionStatus -Label "STEP" -Message "Launching local 27-run promotion campaign."
    Invoke-PromotionPython -ArgumentList @("-B", $CampaignScriptPath, "--run")
    exit $script:LastPythonExitCode
}

# Build A Recoverable Remote Package
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar -ErrorAction Stop
$RemoteWorkRoot = Join-Path $ProjectRoot ".temp\wave52r_offline_leader_cross_surface_promotion"
New-Item -ItemType Directory -Force -Path $RemoteWorkRoot | Out-Null
$LocalSourceArchivePath = Join-Path $RemoteWorkRoot "promotion_source.tar"
$LocalResultArchivePath = Join-Path $RemoteWorkRoot "promotion_results.tar"
$LocalRemoteScriptPath = Join-Path $RemoteWorkRoot "promotion_remote_run.ps1"
$SourcePathList = @(
    "scripts",
    "config",
    "doc",
    "site",
    "requirements.txt",
    "AGENTS.md",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations",
    "output/validation_checks/wave52r_offline_leader_promotion/2026-07-30-19-24-35__wave52r_offline_leader_promotion"
)
& tar -cf $LocalSourceArchivePath @SourcePathList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$RemoteScriptText = @"
`$ErrorActionPreference = "Stop"
`$RemoteRepositoryPath = '$($RemoteRepositoryPath.Replace("'", "''"))'
`$RemoteSourceArchivePath = Join-Path `$env:USERPROFILE "promotion_source.tar"
`$RemoteResultArchivePath = Join-Path `$env:USERPROFILE "promotion_results.tar"
New-Item -ItemType Directory -Force -Path `$RemoteRepositoryPath | Out-Null
& tar -xf `$RemoteSourceArchivePath -C `$RemoteRepositoryPath
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
Set-Location -LiteralPath `$RemoteRepositoryPath
if (-not (Test-Path -LiteralPath "data\polished_dataset")) {
    throw "Remote polished_dataset is missing."
}
& conda run --no-capture-output -n '$RemoteCondaEnvironmentName' python -B '$CampaignScriptPath' --run
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
`$CampaignOutputDirectory = Get-ChildItem -LiteralPath "output\training_campaigns" -Directory |
    Where-Object { `$_.Name -like "*$CampaignName*" } |
    Sort-Object LastWriteTime |
    Select-Object -Last 1
if (`$null -eq `$CampaignOutputDirectory) {
    throw "Remote promotion campaign output was not found."
}
`$ArtifactPathListPath = Join-Path `$CampaignOutputDirectory.FullName "campaign_artifact_path_list.txt"
`$ResultPathList = @(
    (Resolve-Path -Relative `$CampaignOutputDirectory.FullName).TrimStart(".", "\", "/"),
    "output\validation_checks\wave52r_offline_leader_cross_surface_promotion",
    "doc\running\active_training_campaign.yaml"
)
`$ResultPathList += Get-Content -LiteralPath `$ArtifactPathListPath
& tar -cf `$RemoteResultArchivePath @ResultPathList
exit `$LASTEXITCODE
"@
[System.IO.File]::WriteAllText(
    $LocalRemoteScriptPath,
    $RemoteScriptText,
    [System.Text.UTF8Encoding]::new($false)
)
& scp -q $LocalSourceArchivePath "${RemoteHostAlias}:promotion_source.tar"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q $LocalRemoteScriptPath "${RemoteHostAlias}:promotion_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File promotion_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q "${RemoteHostAlias}:promotion_results.tar" $LocalResultArchivePath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& tar -xf $LocalResultArchivePath -C $ProjectRoot
exit $LASTEXITCODE
