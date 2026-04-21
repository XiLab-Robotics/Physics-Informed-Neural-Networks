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
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\.." )).Path
Set-Location $projectRoot

$launcherRelativePathList = @(
    "scripts\campaigns\track1\exact_paper\run_track1_rf_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_dt_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_et_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_ert_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_gbm_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_hgbm_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_xgbm_open_cell_full_matrix_closure_campaign.ps1"
    "scripts\campaigns\track1\exact_paper\run_track1_lgbm_open_cell_full_matrix_closure_campaign.ps1"
)

Write-Host "[INFO] Track 1 relaunch mode | resume after completed MLP family" -ForegroundColor Cyan
Write-Host "[INFO] Relaunch family launcher count | $($launcherRelativePathList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Execution Mode | $(if ($Remote) { 'remote' } else { 'local' })" -ForegroundColor Cyan

for ($launcherIndex = 0; $launcherIndex -lt $launcherRelativePathList.Count; $launcherIndex++) {
    $launcherRelativePath = $launcherRelativePathList[$launcherIndex]
    $launcherPath = Join-Path $projectRoot $launcherRelativePath

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Relaunch Campaign Progress {0}/{1} | {2}" -f ($launcherIndex + 1), $launcherRelativePathList.Count, $launcherRelativePath) -ForegroundColor Cyan
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
        Write-Host "[ERROR] Track 1 relaunch launcher failed | $launcherRelativePath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Track 1 open-cell full-matrix relaunch after MLP completed successfully" -ForegroundColor Green
exit 0
