param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [ValidateSet("all", "fw", "bw")]
    [string]$Surface = "all",
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_lan_env" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "polished_dataset_rcim_model_bank_reproduction_2026_06_22"
$CampaignManifestPath = "config/paper_reimplementation/rcim_ml_compensation/polished_dataset_rcim_model_bank_reproduction/campaigns/2026-06-22_polished_rcim_model_bank_reproduction/campaign.yaml"
$PlanningReportPath = "doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-22-22-55-55_polished_rcim_model_bank_reproduction_campaign_plan_report.md"
$ValidatorPath = "scripts/campaigns/cross_wave/validate_polished_dataset_retraining_campaign_package.py"
$RunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\run_original_dataset_exact_model_bank_validation.py"
$CampaignOutputDirectory = "output\training_campaigns\cross_wave\polished_dataset\rcim_model_bank_reproduction\polished_dataset_rcim_model_bank_reproduction_2026_06_22"
$ConfigPathList = @(
    "config/paper_reimplementation/rcim_ml_compensation/polished_dataset_rcim_model_bank_reproduction/campaigns/2026-06-22_polished_rcim_model_bank_reproduction/queue/rcim_model_bank_reproduction_polished_dataset_fw.yaml",
    "config/paper_reimplementation/rcim_ml_compensation/polished_dataset_rcim_model_bank_reproduction/campaigns/2026-06-22_polished_rcim_model_bank_reproduction/queue/rcim_model_bank_reproduction_polished_dataset_bw.yaml"
)
$RunNameList = @(
    "rcim_model_bank_reproduction_polished_dataset_fw",
    "rcim_model_bank_reproduction_polished_dataset_bw"
)
$SurfaceList = @(
    "fw",
    "bw"
)
$script:LastPythonExitCode = 0

function Invoke-PolishedPython {
    param(
        [string[]]$ArgumentList,
        [string]$LogPath = ""
    )

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        if ([string]::IsNullOrWhiteSpace($LogPath)) {
            & $PythonExecutable @ArgumentList
        } else {
            $PreviousErrorActionPreference = $ErrorActionPreference
            $ErrorActionPreference = "Continue"
            try {
                & $PythonExecutable @ArgumentList 2>&1 | ForEach-Object { $_.ToString() } | Tee-Object -FilePath $LogPath
            } finally {
                $ErrorActionPreference = $PreviousErrorActionPreference
            }
        }
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        if ([string]::IsNullOrWhiteSpace($LogPath)) {
            & python @ArgumentList
        } else {
            $PreviousErrorActionPreference = $ErrorActionPreference
            $ErrorActionPreference = "Continue"
            try {
                & python @ArgumentList 2>&1 | ForEach-Object { $_.ToString() } | Tee-Object -FilePath $LogPath
            } finally {
                $ErrorActionPreference = $PreviousErrorActionPreference
            }
        }
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    if ([string]::IsNullOrWhiteSpace($LogPath)) {
        & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList
    } else {
        $PreviousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        try {
            & $condaExecutablePath run --no-capture-output -n $CondaEnvironmentName python @ArgumentList 2>&1 | ForEach-Object { $_.ToString() } | Tee-Object -FilePath $LogPath
        } finally {
            $ErrorActionPreference = $PreviousErrorActionPreference
        }
    }
    $script:LastPythonExitCode = $LASTEXITCODE
}

function Resolve-SelectedSurfaceIndexes {
    if ($Surface -eq "all") {
        return @(0..($SurfaceList.Count - 1))
    }

    $SelectedIndex = [Array]::IndexOf($SurfaceList, $Surface)
    if ($SelectedIndex -lt 0) {
        throw "Unsupported surface selector | $Surface"
    }
    return @($SelectedIndex)
}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"
Write-Host "[INFO] Surface: $Surface"

Invoke-PolishedPython -ArgumentList @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly) {
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}

$SelectedSurfaceIndexList = Resolve-SelectedSurfaceIndexes
$SelectedConfigPathList = foreach ($ConfigIndex in $SelectedSurfaceIndexList) {
    $ConfigPathList[$ConfigIndex]
}
$SelectedRunNameList = foreach ($ConfigIndex in $SelectedSurfaceIndexList) {
    $RunNameList[$ConfigIndex]
}

if ($Remote) {
    & ".\scripts\campaigns\track_1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $CampaignName `
        -PlanningReportPath $PlanningReportPath `
        -LauncherRelativePath "scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1" `
        -CampaignOutputRootOverride $CampaignOutputDirectory `
        -CampaignConfigPathList @($SelectedConfigPathList) `
        -RunNameList @($SelectedRunNameList) `
        -ValidationOutputRoot "output\validation_checks\rcim_model_bank_reproduction_polished_dataset" `
        -ValidationReportRoot "doc\reports\analysis\validation_checks\rcim_model_bank_reproduction_polished_dataset" `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}

$LogRoot = Join-Path $ProjectRoot (Join-Path $CampaignOutputDirectory "logs")
New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null

foreach ($ConfigIndex in $SelectedSurfaceIndexList) {
    $ConfigPath = $ConfigPathList[$ConfigIndex]
    $ConfigStem = [System.IO.Path]::GetFileNameWithoutExtension($ConfigPath)
    $LogPath = Join-Path $LogRoot ($ConfigStem + ".log")
    Write-Host ("[INFO] RCIM polished run {0}/{1} | surface={2} | {3}" -f ($ConfigIndex + 1), $ConfigPathList.Count, $SurfaceList[$ConfigIndex], $ConfigPath)
    Write-Host ("[INFO] Run log | {0}" -f $LogPath)
    Invoke-PolishedPython -ArgumentList @(
        "-B",
        $RunnerPath,
        "--config-path",
        $ConfigPath,
        "--output-suffix",
        "polished_dataset_campaign_validation"
    ) -LogPath $LogPath
    if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }
}

Write-Host "[DONE] Polished RCIM Model-Bank Reproduction campaign completed"
