param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [switch]$EnqueueOnly,
    [switch]$RunOneBatchValidation,
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
Set-Location $projectRoot

$campaignName = "polished_dataset_stage1_smoke_2026_06_21"
$campaignManifestPath = "config\training\polished_dataset_retraining\campaigns\2026-06-21_polished_dataset_stage1_smoke\campaign.yaml"
$planningReportPath = "doc\reports\campaign_plans\cross_wave\polished_dataset\2026-06-21-03-26-07_polished_dataset_full_program_retraining_campaign_plan_report.md"
$validatorPath = "scripts\campaigns\cross_wave\validate_polished_dataset_stage1_smoke_package.py"
$queueRoot = "config\training\queue\polished_dataset_stage1_smoke"
$script:LastPythonExitCode = 0
$campaignConfigPathList = @(
    "config\training\feedforward\presets\trial.yaml",
    "config\training\wave1_directional_retraining\campaigns\2026-05-06_wave1_directional_retraining_campaign\queue\01_tree_global.yaml",
    "config\training\wave1_directional_retraining\campaigns\2026-05-06_wave1_directional_retraining_campaign\queue\13_harmonic_regression_global.yaml",
    "config\training\wave2b_harmonic_temporal_hybrid\campaigns\2026-05-25_wave2b_harmonic_temporal_hybrid_campaign\queue\04_periodic_gru_sequence_global.yaml",
    "config\training\wave2c_residual_harmonic_temporal_hybrid\campaigns\2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign\queue\01_residual_harmonic_gru_sequence_sparse_rcim_global.yaml",
    "config\training\track2g_curve_aware_training\campaigns\2026-06-08_track2g_curve_aware_training_campaign\queue\10_full_curve_composite_global.yaml",
    "config\training\wave3_harmonic_prior_residual\campaigns\2026-06-14_wave3_harmonic_prior_residual_campaign\queue\04_smooth_l1_structured_global.yaml",
    "config\training\track2h_latent_state_hysteresis\campaigns\2026-06-16_track2h_latent_state_hysteresis_campaign\queue\01_gru_offset_residual_global.yaml"
)

function Write-PolishedStageStatus {
    param([string]$Label, [string]$Message)

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-PolishedStagePython {
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

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}

Write-PolishedStageStatus -Label "INFO" -Message ("Campaign: {0}" -f $campaignName)
Write-PolishedStageStatus -Label "INFO" -Message ("Dataset: polished_dataset")

$validatorArgumentList = @(
    "-B",
    $validatorPath,
    "--campaign-manifest-path",
    $campaignManifestPath
)
if ($RunOneBatchValidation) {
    $validatorArgumentList += "--run-one-batch"
}

Write-PolishedStageStatus -Label "STEP" -Message "Validating the Stage 1 package."
Invoke-PolishedStagePython -ArgumentList $validatorArgumentList
if ($script:LastPythonExitCode -ne 0) {
    exit $script:LastPythonExitCode
}

if ($PreflightOnly) {
    Write-PolishedStageStatus -Label "DONE" -Message "Preflight completed without training."
    exit 0
}

if ($Remote) {
    if ($EnqueueOnly) {
        throw "-EnqueueOnly is supported only for local launcher verification."
    }

    $remoteLauncherPath = "scripts\campaigns\infrastructure\run_remote_training_campaign.ps1"
    $sourceSyncPathList = @("scripts", "config", "doc", "site", "requirements.txt", "AGENTS.md")
    & $remoteLauncherPath `
        -CampaignConfigPathList $campaignConfigPathList `
        -CampaignName $campaignName `
        -PlanningReportPath $planningReportPath `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName `
        -SourceSyncPathList $sourceSyncPathList `
        -AdditionalTrainingArgumentList @(
            "--dataset",
            "polished_dataset",
            "--queue-root",
            $queueRoot,
            "--stop-on-error"
        )
    exit $LASTEXITCODE
}

$trainingArgumentList = @(
    "-B",
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--dataset",
    "polished_dataset",
    "--queue-root",
    $queueRoot,
    "--campaign-name",
    $campaignName,
    "--planning-report-path",
    $planningReportPath,
    "--stop-on-error"
)
if ($EnqueueOnly) {
    $trainingArgumentList += "--enqueue-only"
}

Write-PolishedStageStatus -Label "STEP" -Message "Launching the local Stage 1 campaign."
Invoke-PolishedStagePython -ArgumentList $trainingArgumentList
exit $script:LastPythonExitCode
