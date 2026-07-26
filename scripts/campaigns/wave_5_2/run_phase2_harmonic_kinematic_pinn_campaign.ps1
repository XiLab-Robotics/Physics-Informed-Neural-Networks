param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$RunOneBatchValidation,
    [switch]$EnqueueOnly,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26"
$CampaignManifestPath = "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/campaign.yaml"
$CampaignConfigPathList = @(
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/001_h0_fourier_control_fw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/002_h0_fourier_control_bw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/003_h1_oscillator_residual_fw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/004_h1_oscillator_residual_bw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/005_h2_oscillator_periodic_closure_fw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/006_h2_oscillator_periodic_closure_bw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/007_h3_oscillator_periodic_bauer_anchor_fw.yaml",
    "config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/008_h3_oscillator_periodic_bauer_anchor_bw.yaml"
)
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/harmonic_kinematic_pinn/2026-07-25-20-44-23_phase2_harmonic_kinematic_pinn_campaign_plan_report.md"
$AnalyticalAnchorPath = "output/analysis/polynomial_fourier_benchmark/phase1_coefficient_models.yaml"
$CommonSplitManifestPath = "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml"
$QueueRoot = "config\training\queue\harmonic_kinematic_pinn\$CampaignName"
$script:LastPythonExitCode = 0

function Write-Phase2PinnStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Phase2PinnPython {
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

Write-Phase2PinnStatus -Label "INFO" -Message "Campaign: $CampaignName"
Write-Phase2PinnStatus -Label "INFO" -Message "Scope: polished_dataset setpoints, separate Fw and Bw surfaces"
Write-Phase2PinnStatus -Label "INFO" -Message "Manifest: $CampaignManifestPath"

foreach ($RequiredPath in @(
    $CampaignManifestPath,
    $PlanningReportPath,
    $AnalyticalAnchorPath,
    $CommonSplitManifestPath
) + $CampaignConfigPathList) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required campaign path is missing | $RequiredPath"
    }
}

Write-Phase2PinnStatus -Label "STEP" -Message "Running deterministic PINN primitive validation."
Invoke-Phase2PinnPython -ArgumentList @(
    "-B",
    "scripts\testing\validate_harmonic_kinematic_pinn.py"
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($RunOneBatchValidation) {
    Write-Phase2PinnStatus -Label "STEP" -Message "Running one-batch validation for all eight queue entries."
    foreach ($CampaignConfigPath in $CampaignConfigPathList) {
        Write-Phase2PinnStatus -Label "STEP" -Message "Validating $CampaignConfigPath"
        Invoke-Phase2PinnPython -ArgumentList @(
            "-B",
            "scripts\training\validate_training_setup.py",
            "--config-path",
            $CampaignConfigPath,
            "--dataset",
            "polished_dataset"
        )
        if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }
    }
}

if ($PreflightOnly) {
    Write-Phase2PinnStatus -Label "DONE" -Message "Preflight completed without training."
    exit 0
}

if ($Remote) {
    if ($EnqueueOnly) {
        throw "-EnqueueOnly is supported only for local launcher verification."
    }

    & ".\scripts\campaigns\infrastructure\run_remote_training_campaign.ps1" `
        -CampaignConfigPathList $CampaignConfigPathList `
        -CampaignName $CampaignName `
        -PlanningReportPath $PlanningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList @(
            "scripts",
            "config",
            "doc",
            "site",
            "requirements.txt",
            "AGENTS.md",
            $AnalyticalAnchorPath,
            $CommonSplitManifestPath
        ) `
        -AdditionalTrainingArgumentList @(
            "--dataset",
            "polished_dataset",
            "--input-mode",
            "setpoints",
            "--queue-root",
            $QueueRoot,
            "--stop-on-error"
        )
    exit $LASTEXITCODE
}

$TrainingArgumentList = @(
    "-B",
    "scripts\training\run_training_campaign.py"
) + $CampaignConfigPathList + @(
    "--dataset",
    "polished_dataset",
    "--input-mode",
    "setpoints",
    "--queue-root",
    $QueueRoot,
    "--campaign-name",
    $CampaignName,
    "--planning-report-path",
    $PlanningReportPath,
    "--stop-on-error"
)
if ($EnqueueOnly) {
    $TrainingArgumentList += "--enqueue-only"
    Write-Phase2PinnStatus -Label "STEP" -Message "Enqueue-only verification enabled."
}

Write-Phase2PinnStatus -Label "STEP" -Message "Launching local Phase 2 PINN campaign."
Invoke-Phase2PinnPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
