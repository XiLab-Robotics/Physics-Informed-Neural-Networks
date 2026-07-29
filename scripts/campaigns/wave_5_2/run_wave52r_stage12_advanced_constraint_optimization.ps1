param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$Run,
    [switch]$ResumeFailed,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "wave52r_stage12_advanced_constraint_optimization_2026_07_29"
$CampaignScriptPath = "scripts/campaigns/wave_5_2/run_wave52r_stage12_advanced_constraint_optimization.py"
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/advanced_constraint_optimization/2026-07-29-21-38-21_wave52r_stage12_advanced_constraint_optimization_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-29/2026-07-29-21-38-21_wave52r_stage12_advanced_constraint_optimization.md"
$ModelReportPath = "doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage12_advanced_constraint_optimization/stage12_advanced_constraint_optimization_model_report.md"
$Stage9RunPath = "output/training_runs/temporal_analytical_residual_models/2026-07-29-19-21-15__stage9_k01"
$script:LastPythonExitCode = 0

function Write-Stage12Status {
    param([string]$Label, [string]$Message)

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Stage12Python {
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
    $Stage9RunPath,
    "scripts/training/advanced_constraint_optimization.py",
    "scripts/training/physics_guided_optimization_instrumentation.py",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals"
)) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required Stage 12 path is missing | $RequiredPath"
    }
}

Write-Stage12Status -Label "INFO" -Message "Campaign: $CampaignName"
Write-Stage12Status -Label "INFO" -Message "Scope: polished_dataset / setpoints / Fw"
Write-Stage12Status -Label "STEP" -Message "Running split, K01 replay, gradient, constraint, and deterministic-sampling preflight."
Invoke-Stage12Python -ArgumentList @("-B", $CampaignScriptPath, "--preflight-only")
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly -or -not $Run) {
    if ($ResumeFailed) {
        Write-Stage12Status -Label "STEP" -Message "Recovering failed local Stage 12 entries."
        Invoke-Stage12Python -ArgumentList @("-B", $CampaignScriptPath, "--resume-failed")
        exit $script:LastPythonExitCode
    }
    Write-Stage12Status -Label "DONE" -Message "Preflight completed without training."
    exit 0
}

if (-not $Remote) {
    Write-Stage12Status -Label "STEP" -Message "Launching local Stage 12 campaign."
    Invoke-Stage12Python -ArgumentList @("-B", $CampaignScriptPath, "--run")
    exit $script:LastPythonExitCode
}

# Build A Recoverable Remote Package
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar -ErrorAction Stop
$RemoteWorkRoot = Join-Path $ProjectRoot ".temp\stage12_remote_campaign"
New-Item -ItemType Directory -Force -Path $RemoteWorkRoot | Out-Null
$LocalSourceArchivePath = Join-Path $RemoteWorkRoot "stage12_source.tar"
$LocalResultArchivePath = Join-Path $RemoteWorkRoot "stage12_results.tar"
$LocalRemoteScriptPath = Join-Path $RemoteWorkRoot "stage12_remote_run.ps1"
$SourcePathList = @(
    "scripts",
    "config",
    "doc",
    "site",
    "requirements.txt",
    "AGENTS.md",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations",
    "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml",
    "output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals",
    "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-28-16-17-13__stage5_h04",
    $Stage9RunPath
)
& tar -cf $LocalSourceArchivePath @SourcePathList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$RemoteScriptText = @"
`$ErrorActionPreference = "Stop"
`$RemoteRepositoryPath = '$($RemoteRepositoryPath.Replace("'", "''"))'
`$RemoteSourceArchivePath = Join-Path `$env:USERPROFILE "stage12_source.tar"
`$RemoteResultArchivePath = Join-Path `$env:USERPROFILE "stage12_results.tar"
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
if (`$null -eq `$CampaignOutputDirectory) { throw "Stage 12 remote output was not found." }
`$CampaignRelativePath = (Resolve-Path -Relative `$CampaignOutputDirectory.FullName).TrimStart(".", "\", "/")
& tar -cf `$RemoteResultArchivePath `
    `$CampaignRelativePath `
    "output/training_runs/advanced_constraint_optimization" `
    "output/analysis/wave_5_2r/stage12_advanced_constraint_optimization" `
    "config/training/advanced_constraint_optimization" `
    "doc/running/active_training_campaign.yaml"
exit `$LASTEXITCODE
"@
[System.IO.File]::WriteAllText(
    $LocalRemoteScriptPath,
    $RemoteScriptText,
    [System.Text.UTF8Encoding]::new($false)
)
& scp -q $LocalSourceArchivePath "${RemoteHostAlias}:stage12_source.tar"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q $LocalRemoteScriptPath "${RemoteHostAlias}:stage12_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File stage12_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q "${RemoteHostAlias}:stage12_results.tar" $LocalResultArchivePath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& tar -xf $LocalResultArchivePath -C $ProjectRoot
exit $LASTEXITCODE
