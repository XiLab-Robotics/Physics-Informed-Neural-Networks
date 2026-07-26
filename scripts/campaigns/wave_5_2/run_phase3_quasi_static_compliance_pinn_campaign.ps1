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

$CampaignName = "phase3_quasi_static_compliance_pinn_2026_07_26"
$CampaignManifestPath = "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/campaign.yaml"
$CampaignConfigPathList = @(
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/001_c0_learned_mean_control_fw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/002_c0_learned_mean_control_bw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/003_c0_learned_mean_control_global.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/004_c1_linear_compliance_soft_fw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/005_c1_linear_compliance_soft_bw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/006_c2_temperature_compliance_soft_fw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/007_c2_temperature_compliance_soft_bw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/008_c3_nonlinear_compliance_soft_fw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/009_c3_nonlinear_compliance_soft_bw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/010_c4_hard_elastic_offset_fw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/011_c4_hard_elastic_offset_bw.yaml",
    "config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/012_c5_shared_stiffness_global.yaml"
)
$PlanningReportPath = "doc/reports/campaign_plans/model_development_waves/wave_5_2/quasi_static_compliance_pinn/2026-07-26-17-16-41_phase3_quasi_static_compliance_pinn_campaign_plan_report.md"
$TechnicalDocumentPath = "doc/technical/2026-07/2026-07-26/2026-07-26-17-14-40_phase_3_quasi_static_compliance_pinn.md"
$ModelReportPath = "doc/reports/analysis/model_development_waves/wave_5_2/quasi_static_compliance_pinn/[2026-07-26]/phase3_quasi_static_compliance_pinn_model_report.md"
$AuditArtifactPath = "output/analysis/pinn_program_compliance/phase3_compliance_audit.yaml"
$CommonSplitManifestPath = "output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml"
$QueueRoot = "config\training\queue\quasi_static_compliance_pinn\$CampaignName"
$script:LastPythonExitCode = 0

function Write-Phase3PinnStatus {
    param(
        [string]$Label,
        [string]$Message
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] [$Label] $Message"
}

function Invoke-Phase3PinnPython {
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

Write-Phase3PinnStatus -Label "INFO" -Message "Campaign: $CampaignName"
Write-Phase3PinnStatus -Label "INFO" -Message "Scope: C0-C5 on Fw, Bw, and bounded global surfaces"
Write-Phase3PinnStatus -Label "INFO" -Message "Manifest: $CampaignManifestPath"

foreach ($RequiredPath in @(
    $CampaignManifestPath,
    $PlanningReportPath,
    $TechnicalDocumentPath,
    $ModelReportPath,
    $AuditArtifactPath,
    $CommonSplitManifestPath
) + $CampaignConfigPathList) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Required campaign path is missing | $RequiredPath"
    }
}

Write-Phase3PinnStatus -Label "STEP" -Message "Validating the Phase 3 identifiability audit."
Invoke-Phase3PinnPython -ArgumentList @(
    "-B",
    "scripts\analysis\pinn_program_compliance\validate_phase3_compliance_audit.py"
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

Write-Phase3PinnStatus -Label "STEP" -Message "Running deterministic compliance-PINN validation."
Invoke-Phase3PinnPython -ArgumentList @(
    "-B",
    "scripts\testing\validate_quasi_static_compliance_pinn.py"
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($RunOneBatchValidation) {
    Write-Phase3PinnStatus -Label "STEP" -Message "Running one-batch validation for all twelve queue entries."
    foreach ($CampaignConfigPath in $CampaignConfigPathList) {
        Write-Phase3PinnStatus -Label "STEP" -Message "Validating $CampaignConfigPath"
        Invoke-Phase3PinnPython -ArgumentList @(
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
    Write-Phase3PinnStatus -Label "DONE" -Message "Preflight completed without training."
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
            $AuditArtifactPath,
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
    Write-Phase3PinnStatus -Label "STEP" -Message "Enqueue-only verification enabled."
}

Write-Phase3PinnStatus -Label "STEP" -Message "Launching local Phase 3 PINN campaign."
Invoke-Phase3PinnPython -ArgumentList $TrainingArgumentList
exit $script:LastPythonExitCode
