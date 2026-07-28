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

$CampaignName = "wave52r_stage4_data_only_residual_capacity_2026_07_28"
$CampaignDirectory = "config/training/data_only_residual_capacity/campaigns/2026-07-28_wave52r_stage4_data_only_residual_capacity"
$CampaignManifestPath = "$CampaignDirectory/campaign.yaml"
$CampaignConfigPathList = @(
    "$CampaignDirectory/queue/001_c01_r1_compact.yaml",
    "$CampaignDirectory/queue/002_c02_r1_deep.yaml",
    "$CampaignDirectory/queue/003_c03_r1_compact.yaml",
    "$CampaignDirectory/queue/004_c04_r1_deep.yaml",
    "$CampaignDirectory/queue/005_c05_r1_compact.yaml",
    "$CampaignDirectory/queue/006_c06_r1_deep.yaml",
    "$CampaignDirectory/queue/007_h01_r2_compact.yaml",
    "$CampaignDirectory/queue/008_h02_r2_deep.yaml",
    "$CampaignDirectory/queue/009_h03_r3_compact.yaml",
    "$CampaignDirectory/queue/010_h04_r3_deep.yaml",
    "$CampaignDirectory/queue/011_h05_r4_compact.yaml",
    "$CampaignDirectory/queue/012_h06_r4_deep.yaml",
    "$CampaignDirectory/queue/013_h07_r5_compact.yaml",
    "$CampaignDirectory/queue/014_h08_r5_deep.yaml",
    "$CampaignDirectory/queue/015_a01_r2_compact.yaml",
    "$CampaignDirectory/queue/016_a02_r2_compact.yaml",
    "$CampaignDirectory/queue/017_a03_r5_compact.yaml",
    "$CampaignDirectory/queue/018_a04_r5_compact.yaml"
)
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/data_only_residual_capacity_ladder/2026-07-27-22-39-42_wave52r_stage4_data_only_residual_capacity_ladder_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-27/2026-07-27-22-37-41_wave52r_stage4_data_only_residual_capacity_ladder.md"
$ModelReportPath = "doc/reports/analysis/model_development_waves/wave_5_2/physics_guided_pinn_reassessment/[2026-07-28]/stage4_data_only_residual_capacity_ladder/stage4_data_only_residual_capacity_model_report.md"
$CausalAnchorPath = "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_causal_setpoint_pf_a_surface.yaml"
$CalibrationPath = "output/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/stage4_training_only_calibration.yaml"
$ValidationScriptPath = "scripts/analysis/wave_5_2r/stage4_data_only_residual_capacity_ladder/validate_stage4_model_and_campaign.py"
$CommonSplitManifestPath = "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml"
$QueueRoot = "config\training\queue\data_only_residual_capacity\$CampaignName"
$script:LastPythonExitCode = 0

function Write-Stage4Status {
    param(
        [string]$Label,
        [string]$Message
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Stage4Python {
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

Write-Stage4Status -Label "INFO" -Message "Campaign: $CampaignName"
Write-Stage4Status -Label "INFO" -Message "Scope: polished_dataset / setpoints / Fw"
Write-Stage4Status -Label "INFO" -Message "Queue entries: $($CampaignConfigPathList.Count)"

foreach ($RequiredPath in @(
    $CampaignManifestPath,
    $PlanningReportPath,
    $TechnicalDocumentPath,
    $ModelReportPath,
    $CausalAnchorPath,
    $CalibrationPath,
    $ValidationScriptPath,
    $CommonSplitManifestPath
) + $CampaignConfigPathList) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required Stage 4 path is missing | $RequiredPath"
    }
}

Write-Stage4Status -Label "STEP" -Message "Running deterministic model and package validation."
Invoke-Stage4Python -ArgumentList @(
    "-B",
    $ValidationScriptPath
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($RunOneBatchValidation) {
    Write-Stage4Status -Label "STEP" -Message "Running all eighteen real-dataset one-batch validations."
    foreach ($CampaignConfigPath in $CampaignConfigPathList) {
        Write-Stage4Status -Label "STEP" -Message "Validating $CampaignConfigPath"
        Invoke-Stage4Python -ArgumentList @(
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
    $ExecutionPath = if ($Remote) { "remote-compatible" } else { "local" }
    Write-Stage4Status -Label "DONE" -Message "$ExecutionPath preflight completed without training."
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
            $CausalAnchorPath,
            $CalibrationPath,
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
    Write-Stage4Status -Label "STEP" -Message "Enqueue-only verification enabled."
}

Write-Stage4Status -Label "STEP" -Message "Launching local Stage 4 campaign."
Invoke-Stage4Python -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
