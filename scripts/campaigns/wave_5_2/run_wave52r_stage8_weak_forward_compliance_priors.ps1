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

$CampaignName = "wave52r_stage8_weak_forward_compliance_priors_2026_07_29"
$CampaignScriptPath = "scripts/campaigns/wave_5_2/run_wave52r_stage8_weak_forward_compliance_priors.py"
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/weak_forward_compliance_priors/2026-07-29-18-00-37_wave52r_stage8_weak_forward_compliance_priors_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-29/2026-07-29-18-00-37_wave52r_stage8_weak_forward_compliance_priors.md"
$ModelReportPath = "doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-29]/stage8_weak_forward_compliance_priors/stage8_weak_forward_compliance_priors_model_report.md"
$H04RunPath = "output/training_runs/complex_harmonic_coefficient_residuals/2026-07-28-16-17-13__stage5_h04"
$script:LastPythonExitCode = 0

function Write-Stage8Status {
    param([string]$Label, [string]$Message)

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Stage8Python {
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
    $H04RunPath,
    "scripts/models/weak_forward_compliance_residual_network.py",
    "output/analysis/pinn_program_compliance"
)) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required Stage 8 path is missing | $RequiredPath"
    }
}

Write-Stage8Status -Label "INFO" -Message "Campaign: $CampaignName"
Write-Stage8Status -Label "INFO" -Message "Scope: polished_dataset / setpoints / Fw"
Write-Stage8Status -Label "STEP" -Message "Running bootstrap, derivative, model, split, and leakage preflight."
Invoke-Stage8Python -ArgumentList @("-B", $CampaignScriptPath, "--preflight-only")
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly -or -not $Run) {
    Write-Stage8Status -Label "DONE" -Message "Preflight completed without training."
    exit 0
}

if (-not $Remote) {
    Write-Stage8Status -Label "STEP" -Message "Launching local Stage 8 campaign."
    Invoke-Stage8Python -ArgumentList @("-B", $CampaignScriptPath, "--run")
    exit $script:LastPythonExitCode
}

# Build A Recoverable Remote Package
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar -ErrorAction Stop
$RemoteWorkRoot = Join-Path $ProjectRoot ".temp\stage8_remote_campaign"
New-Item -ItemType Directory -Force -Path $RemoteWorkRoot | Out-Null
$LocalSourceArchivePath = Join-Path $RemoteWorkRoot "stage8_source.tar"
$LocalResultArchivePath = Join-Path $RemoteWorkRoot "stage8_results.tar"
$LocalRemoteScriptPath = Join-Path $RemoteWorkRoot "stage8_remote_run.ps1"
$SourcePathList = @(
    "scripts",
    "config",
    "doc",
    "site",
    "requirements.txt",
    "AGENTS.md",
    "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml",
    "output/analysis/pinn_program_foundations",
    "output/analysis/pinn_program_compliance",
    "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml",
    "output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals",
    $H04RunPath
)
& tar -cf $LocalSourceArchivePath @SourcePathList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$RemoteScriptText = @"
`$ErrorActionPreference = "Stop"
`$RemoteRepositoryPath = '$($RemoteRepositoryPath.Replace("'", "''"))'
`$RemoteSourceArchivePath = Join-Path `$env:USERPROFILE "stage8_source.tar"
`$RemoteResultArchivePath = Join-Path `$env:USERPROFILE "stage8_results.tar"
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
if (`$null -eq `$CampaignOutputDirectory) { throw "Stage 8 remote output was not found." }
`$CampaignRelativePath = (Resolve-Path -Relative `$CampaignOutputDirectory.FullName).TrimStart(".", "\", "/")
& tar -cf `$RemoteResultArchivePath `
    `$CampaignRelativePath `
    "output/training_runs/weak_forward_compliance_priors" `
    "output/analysis/wave_5_2r/stage8_weak_forward_compliance_priors" `
    "config/training/weak_forward_compliance_priors" `
    "doc/running/active_training_campaign.yaml"
exit `$LASTEXITCODE
"@
[System.IO.File]::WriteAllText(
    $LocalRemoteScriptPath,
    $RemoteScriptText,
    [System.Text.UTF8Encoding]::new($false)
)
& scp -q $LocalSourceArchivePath "${RemoteHostAlias}:stage8_source.tar"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q $LocalRemoteScriptPath "${RemoteHostAlias}:stage8_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File stage8_remote_run.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& scp -q "${RemoteHostAlias}:stage8_results.tar" $LocalResultArchivePath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& tar -xf $LocalResultArchivePath -C $ProjectRoot
exit $LASTEXITCODE
