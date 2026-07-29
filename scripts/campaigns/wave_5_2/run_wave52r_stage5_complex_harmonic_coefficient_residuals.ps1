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
Set-Location $ProjectRoot

$CampaignName = "wave52r_stage5_complex_harmonic_coefficient_residuals_2026_07_28"
$CampaignScriptPath = "scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.py"
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/complex_harmonic_coefficient_residuals/2026-07-28-15-56-46_wave52r_stage5_complex_harmonic_coefficient_residuals_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-28/2026-07-28-15-56-46_wave52r_stage5_complex_harmonic_coefficient_residuals.md"
$ModelReportPath = "doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-28]/stage5_complex_harmonic_coefficient_residuals/stage5_complex_harmonic_coefficient_residual_model_report.md"
$CausalAnchorPath = "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml"
$CommonSplitManifestPath = "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml"
$Phase1ConfigurationPath = "config/analysis/polynomial_fourier_benchmark/phase1_benchmark.yaml"
$script:LastPythonExitCode = 0

function Write-Stage5Status {
    param(
        [string]$Label,
        [string]$Message
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Stage5Python {
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
    $PlanningReportPath,
    $TechnicalDocumentPath,
    $ModelReportPath,
    $CausalAnchorPath,
    $CommonSplitManifestPath,
    $Phase1ConfigurationPath
)) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required Stage 5 path is missing | $RequiredPath"
    }
}

Write-Stage5Status -Label "INFO" -Message "Campaign: $CampaignName"
Write-Stage5Status -Label "INFO" -Message "Scope: polished_dataset / setpoints / Fw"
Write-Stage5Status -Label "STEP" -Message "Running representation and model preflight."
Invoke-Stage5Python -ArgumentList @(
    "-B",
    $CampaignScriptPath,
    "--preflight-only"
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly -or -not $Run) {
    $ExecutionPath = if ($Remote) { "remote-compatible" } else { "local" }
    Write-Stage5Status -Label "DONE" -Message "$ExecutionPath preflight completed without training."
    exit 0
}

if (-not $Remote) {
    Write-Stage5Status -Label "STEP" -Message "Launching local eighteen-run Stage 5 campaign."
    Invoke-Stage5Python -ArgumentList @(
        "-B",
        $CampaignScriptPath,
        "--run"
    )
    exit $script:LastPythonExitCode
}

# Build A Recoverable Remote Source Package
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar -ErrorAction Stop
$RemoteWorkRoot = Join-Path $ProjectRoot ".temp\stage5_remote_campaign"
New-Item -ItemType Directory -Force -Path $RemoteWorkRoot | Out-Null
$LocalSourceArchivePath = Join-Path $RemoteWorkRoot "stage5_source.tar"
$LocalResultArchivePath = Join-Path $RemoteWorkRoot "stage5_results.tar"
$LocalRemoteScriptPath = Join-Path $RemoteWorkRoot "stage5_remote_run.ps1"

$SourcePathList = @(
    "scripts",
    "config",
    "doc",
    "site",
    "requirements.txt",
    "AGENTS.md",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations/phase0_curve_audit.csv",
    "output/analysis/pinn_program_foundations/phase0_condition_support.csv",
    "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml"
)
Write-Stage5Status -Label "STEP" -Message "Packing required source, configuration, documentation, and anchor evidence."
& tar -cf $LocalSourceArchivePath @SourcePathList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$RemoteScriptText = @"
`$ErrorActionPreference = "Stop"
`$RemoteRepositoryPath = '$($RemoteRepositoryPath.Replace("'", "''"))'
`$RemoteSourceArchivePath = Join-Path `$env:USERPROFILE "stage5_source.tar"
`$RemoteResultArchivePath = Join-Path `$env:USERPROFILE "stage5_results.tar"
New-Item -ItemType Directory -Force -Path `$RemoteRepositoryPath | Out-Null
& tar -xf `$RemoteSourceArchivePath -C `$RemoteRepositoryPath
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
Set-Location -LiteralPath `$RemoteRepositoryPath
& conda run --no-capture-output -n '$RemoteCondaEnvironmentName' python -B '$CampaignScriptPath' --run
if (`$LASTEXITCODE -ne 0) { exit `$LASTEXITCODE }
`$CampaignOutputDirectory = Get-ChildItem -LiteralPath "output\training_campaigns" -Directory |
    Where-Object { `$_.Name -like "*$CampaignName*" } |
    Sort-Object LastWriteTime |
    Select-Object -Last 1
if (`$null -eq `$CampaignOutputDirectory) {
    throw "Stage 5 remote campaign output was not found."
}
`$CampaignRelativePath = Resolve-Path -Relative `$CampaignOutputDirectory.FullName
`$CampaignRelativePath = `$CampaignRelativePath.TrimStart(".", "\", "/")
& tar -cf `$RemoteResultArchivePath `
    `$CampaignRelativePath `
    "output/training_runs/complex_harmonic_coefficient_residuals" `
    "output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals" `
    "config/training/complex_harmonic_coefficient_residuals" `
    "doc/running/active_training_campaign.yaml"
exit `$LASTEXITCODE
"@
[System.IO.File]::WriteAllText(
    $LocalRemoteScriptPath,
    $RemoteScriptText,
    [System.Text.UTF8Encoding]::new($false)
)

Write-Stage5Status -Label "STEP" -Message "Syncing Stage 5 source package to $RemoteHostAlias."
& scp -q $LocalSourceArchivePath "${RemoteHostAlias}:stage5_source.tar"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q $LocalRemoteScriptPath "${RemoteHostAlias}:stage5_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Stage5Status -Label "STEP" -Message "Executing Stage 5 on the remote workstation."
& ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File stage5_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Stage5Status -Label "STEP" -Message "Synchronizing campaign, per-run, analysis, configuration, and state artifacts."
& scp -q "${RemoteHostAlias}:stage5_results.tar" $LocalResultArchivePath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& tar -xf $LocalResultArchivePath -C $ProjectRoot
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Stage5Status -Label "DONE" -Message "Remote Stage 5 campaign and artifact synchronization completed."
exit 0
