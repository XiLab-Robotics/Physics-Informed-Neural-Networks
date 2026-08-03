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

$CampaignName = "wave52r_integrated_specialist_model_2026_08_02"
$CampaignScriptPath = "scripts/campaigns/wave_5_2/run_wave52r_integrated_specialist_model.py"
$CampaignConfigurationPath = "config/training/wave52r_integrated_specialist_model/campaigns/2026-08-02_wave52r_integrated_specialist_model/campaign.yaml"
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/integrated_specialist_model/2026-08-02-19-55-10_wave52r_integrated_specialist_model_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-08/2026-08-02/2026-08-02-19-27-36_wave52r_integrated_specialist_model_roadmap.md"
$script:LastPythonExitCode = 0

function Write-IntegratedSpecialistStatus {
    param([string]$Label, [string]$Message)

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-IntegratedSpecialistPython {
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

$RequiredPathList = @(
    $CampaignScriptPath,
    $CampaignConfigurationPath,
    $PlanningReportPath,
    $TechnicalDocumentPath,
    "scripts/models/integrated_specialist_residual_network.py",
    "scripts/models/causal_temporal_analytical_residual_network.py",
    "scripts/models/complex_harmonic_coefficient_residual_network.py",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations/phase0_curve_audit.csv",
    "data/polished_dataset"
)
foreach ($RequiredPath in $RequiredPathList) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required integrated-specialist path is missing | $RequiredPath"
    }
}

Write-IntegratedSpecialistStatus -Label "INFO" -Message "Campaign: $CampaignName"
Write-IntegratedSpecialistStatus -Label "INFO" -Message "Scope: empirical Wave 5.2R; no PINN or deployment claim."
Write-IntegratedSpecialistStatus -Label "STEP" -Message "Running local package and frozen-expert preflight."
Invoke-IntegratedSpecialistPython -ArgumentList @("-B", $CampaignScriptPath, "--preflight-only")
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if (-not $Remote) {
    if ($PreflightOnly -or -not $Run) {
        Write-IntegratedSpecialistStatus -Label "DONE" -Message "Local preflight completed without training."
        exit 0
    }
    Write-IntegratedSpecialistStatus -Label "STEP" -Message "Launching approved local campaign."
    Invoke-IntegratedSpecialistPython -ArgumentList @("-B", $CampaignScriptPath, "--run")
    exit $script:LastPythonExitCode
}

# Build A Recoverable Remote Package With Every Frozen Dependency
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar -ErrorAction Stop
$RemoteWorkRoot = Join-Path $ProjectRoot ".temp\wave52r_integrated_specialist_model"
New-Item -ItemType Directory -Force -Path $RemoteWorkRoot | Out-Null
$LocalSourceArchivePath = Join-Path $RemoteWorkRoot "integrated_specialist_source.tar"
$LocalResultArchivePath = Join-Path $RemoteWorkRoot "integrated_specialist_results.tar"
$LocalRemoteScriptPath = Join-Path $RemoteWorkRoot "integrated_specialist_remote_run.ps1"
$SourcePathList = @(
    "scripts",
    "config",
    "doc/running/active_training_campaign.yaml",
    "doc/running/te_model_live_backlog.md",
    "doc/reports/analysis/project_status/current/Training Results Master Summary.md",
    "doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md",
    "doc/reports/analysis/model_development_waves/wave_5_2/integrated_specialist_model/[2026-08-02]/wave52r_integrated_specialist_model_report.md",
    "doc/reports/campaign_plans/model_development_waves/wave_5_2/integrated_specialist_model/2026-08-02-19-55-10_wave52r_integrated_specialist_model_campaign_plan_report.md",
    "doc/scripts/campaigns/wave_5_2/run_wave52r_integrated_specialist_model.md",
    "doc/technical/2026-08/2026-08-02/2026-08-02-19-27-36_wave52r_integrated_specialist_model_roadmap.md",
    "requirements.txt",
    "AGENTS.md",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations",
    "output/validation_checks/wave52r_integrated_specialist_model",
    "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-31-10-42-28__stage5_h04__seed_271828",
    "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-31-10-45-42__stage5_h08__seed_161803",
    "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-31-10-52-12__stage5_h04__seed_271828",
    "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-31-11-05-16__stage5_h04__seed_271828",
    "output/training_runs/temporal_analytical_residual_models/2026-07-31-10-45-41__stage9_k01__seed_271828",
    "output/training_runs/temporal_analytical_residual_models/2026-07-31-10-55-28__stage9_k01__seed_271828",
    "output/training_runs/temporal_analytical_residual_models/2026-07-31-11-11-39__stage9_k01__seed_271828"
)
& tar -cf $LocalSourceArchivePath @SourcePathList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$RemoteRunnerArgument = if ($Run -and -not $PreflightOnly) { "--run" } else { "--preflight-only" }
$RemoteScriptText = @"
`$ErrorActionPreference = "Stop"
`$RemoteRepositoryPath = '$($RemoteRepositoryPath.Replace("'", "''"))'
`$RemoteSourceArchivePath = Join-Path `$env:USERPROFILE "integrated_specialist_source.tar"
`$RemoteResultArchivePath = Join-Path `$env:USERPROFILE "integrated_specialist_results.tar"
New-Item -ItemType Directory -Force -Path `$RemoteRepositoryPath | Out-Null
& tar -xf `$RemoteSourceArchivePath -C `$RemoteRepositoryPath
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
Set-Location -LiteralPath `$RemoteRepositoryPath
if (-not (Test-Path -LiteralPath "data\polished_dataset")) {
    throw "Remote polished_dataset is missing."
}
& conda run --no-capture-output -n '$RemoteCondaEnvironmentName' python -B '$CampaignScriptPath' '$RemoteRunnerArgument'
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
`$ResultPathList = @(
    "output\validation_checks\wave52r_integrated_specialist_model"
)
if ('$RemoteRunnerArgument' -eq '--run') {
    `$CampaignOutputDirectory = Get-ChildItem -LiteralPath "output\training_campaigns" -Directory |
        Where-Object { `$_.Name -like "*$CampaignName*" } |
        Sort-Object LastWriteTime |
        Select-Object -Last 1
    if (`$null -eq `$CampaignOutputDirectory) {
        throw "Remote integrated-specialist campaign output was not found."
    }
    `$ResultPathList += (Resolve-Path -Relative `$CampaignOutputDirectory.FullName).TrimStart(".", "\", "/")
    `$ResultPathList += Get-Content -LiteralPath (Join-Path `$CampaignOutputDirectory.FullName "campaign_artifact_path_list.txt")
    `$ResultPathList += "doc\running\active_training_campaign.yaml"
}
& tar -cf `$RemoteResultArchivePath @ResultPathList
exit `$LASTEXITCODE
"@
[System.IO.File]::WriteAllText(
    $LocalRemoteScriptPath,
    $RemoteScriptText,
    [System.Text.UTF8Encoding]::new($false)
)
& scp -q $LocalSourceArchivePath "${RemoteHostAlias}:integrated_specialist_source.tar"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q $LocalRemoteScriptPath "${RemoteHostAlias}:integrated_specialist_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File integrated_specialist_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q "${RemoteHostAlias}:integrated_specialist_results.tar" $LocalResultArchivePath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& tar -xf $LocalResultArchivePath -C $ProjectRoot
exit $LASTEXITCODE
