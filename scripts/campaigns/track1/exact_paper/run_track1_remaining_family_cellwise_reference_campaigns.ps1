param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\.." )).Path
Set-Location $projectRoot

$launcherRelativePathList = @(
    "scripts\campaigns\track1\exact_paper\run_track1_mlp_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_rf_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_dt_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_et_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_ert_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_gbm_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_hgbm_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_xgbm_cellwise_reference_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_lgbm_cellwise_reference_campaign.ps1")

Write-Host "[INFO] Aggregate Track 1 Remaining Family Cellwise Launcher Count | $($launcherRelativePathList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Execution Mode | $(if ($Remote) { 'remote' } else { 'local' })" -ForegroundColor Cyan

for ($launcherIndex = 0; $launcherIndex -lt $launcherRelativePathList.Count; $launcherIndex++) {
    $launcherRelativePath = $launcherRelativePathList[$launcherIndex]
    $launcherPath = Join-Path $projectRoot $launcherRelativePath

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Aggregate Campaign Progress {0}/{1} | {2}" -f ($launcherIndex + 1), $launcherRelativePathList.Count, $launcherRelativePath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    if ($Remote) {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $launcherPath `
            -Remote `
            -RemoteHostAlias $RemoteHostAlias `
            -RemoteRepositoryPath $RemoteRepositoryPath `
            -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    }
    else {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $launcherPath `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable
    }

    $nativeExitCode = if ($LASTEXITCODE -eq $null) { 0 } else { [int]$LASTEXITCODE }
    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Aggregate remaining-family cellwise launcher failed | $launcherRelativePath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Track 1 remaining family cellwise reference campaign sequence completed successfully" -ForegroundColor Green
exit 0
