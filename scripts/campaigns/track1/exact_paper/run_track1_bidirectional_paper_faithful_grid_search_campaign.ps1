param(
    [switch]$Remote,
    [ValidateSet("Forward", "Backward", "Both")]
    [string]$Direction = "Both",
    [string]$Family = "All",
    [string]$Families = "",
    [ValidateSet("Search", "Eval", "Export", "LoadBest")]
    [string]$Stage = "Search",
    [string]$BestParameterSummaryPath = "",
    [int]$GridSearchVerboseOverride = -1,
    [int]$HistoricalCrossValidateVerboseOverride = -1,
    [switch]$NoEval,
    [switch]$NoExport,
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$ActiveCampaignPath = Join-Path $ProjectRoot "doc\running\active_training_campaign.yaml"
$RunnerPath = Join-Path $ProjectRoot "scripts\paper_reimplementation\rcim_ml_compensation\original_dataset_exact_model_bank\run_original_dataset_exact_model_bank_validation.py"
$ExactPaperFamilyOrder = @("SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM")
. (Join-Path $ProjectRoot "scripts\campaigns\infrastructure\shared_streaming_campaign_launcher.ps1")
Set-Location $ProjectRoot

function Get-CampaignQueueBundle {

    param(
        [string]$CampaignYamlPath,
        [string]$ProjectRootPath,
        [string]$EnvironmentName,
        [string]$PythonCommand
    )

    $TemporaryPythonScriptPath = Join-Path $env:TEMP ("track1_bidirectional_paper_faithful_grid_search_queue_bundle_{0}.py" -f ([guid]::NewGuid().ToString("N")))
    $ProjectRootPythonLiteral = $ProjectRootPath | ConvertTo-Json -Compress
    $CampaignYamlPythonLiteral = $CampaignYamlPath | ConvertTo-Json -Compress
    $PythonScriptText = @"
from pathlib import Path
import json
import yaml

project_root = Path($ProjectRootPythonLiteral)
campaign_path = Path($CampaignYamlPythonLiteral)
campaign_payload = yaml.safe_load(campaign_path.read_text(encoding="utf-8"))
queue_path_list = campaign_payload.get("queue_config_path_list", [])
run_name_list = [
    yaml.safe_load((project_root / queue_path).read_text(encoding="utf-8"))["experiment"]["run_name"]
    for queue_path in queue_path_list
]
payload = {
    "campaign_name": campaign_payload.get("campaign_name"),
    "planning_report_path": campaign_payload.get("planning_report_path"),
    "campaign_output_directory": campaign_payload.get("campaign_output_directory"),
    "queue_config_path_list": queue_path_list,
    "run_name_list": run_name_list,
}
print(json.dumps(payload))
"@

    try {
        Set-Content -LiteralPath $TemporaryPythonScriptPath -Value $PythonScriptText -Encoding UTF8
        $CampaignBundleJson = & conda run -n $EnvironmentName $PythonCommand $TemporaryPythonScriptPath
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to read active campaign YAML | $CampaignYamlPath"
        }

        return ($CampaignBundleJson | ConvertFrom-Json)
    }
    finally {
        if (Test-Path -LiteralPath $TemporaryPythonScriptPath) {
            Remove-Item -LiteralPath $TemporaryPythonScriptPath -Force -ErrorAction SilentlyContinue
        }
    }
}

function Get-CampaignConfigDirectionLabel {

    param(
        [string]$ConfigRelativePath
    )

    $normalizedPath = $ConfigRelativePath.Replace("/", "\").ToLowerInvariant()
    if ($normalizedPath.Contains("\forward\")) {
        return "Forward"
    }
    if ($normalizedPath.Contains("\backward\")) {
        return "Backward"
    }
    throw "Unable to resolve direction from config path | $ConfigRelativePath"
}

function Get-CampaignConfigFamilyName {

    param(
        [string]$ConfigRelativePath
    )

    $normalizedPath = $ConfigRelativePath.Replace("/", "\").ToLowerInvariant()
    foreach ($familyName in $ExactPaperFamilyOrder) {
        $familySlug = $familyName.ToLowerInvariant()
        if ($normalizedPath.Contains("\$familySlug\")) {
            return $familyName
        }
    }
    throw "Unable to resolve family from config path | $ConfigRelativePath"
}

function Select-CampaignQueueEntries {

    param(
        [object]$CampaignBundle,
        [string]$DirectionName,
        [string[]]$RequestedFamilyList
    )

    $selectedConfigPathList = New-Object System.Collections.ArrayList
    $selectedRunNameList = New-Object System.Collections.ArrayList

    for ($queueIndex = 0; $queueIndex -lt @($CampaignBundle.queue_config_path_list).Count; $queueIndex++) {
        $configRelativePath = @($CampaignBundle.queue_config_path_list)[$queueIndex]
        $runName = @($CampaignBundle.run_name_list)[$queueIndex]
        $configDirectionName = Get-CampaignConfigDirectionLabel -ConfigRelativePath $configRelativePath
        $configFamilyName = Get-CampaignConfigFamilyName -ConfigRelativePath $configRelativePath
        $directionMatches = ($DirectionName -eq "Both") -or ($configDirectionName -eq $DirectionName)
        $familyMatches = ($RequestedFamilyList -contains "All") -or ($RequestedFamilyList -contains $configFamilyName)

        if ($directionMatches -and $familyMatches) {
            [void]$selectedConfigPathList.Add($configRelativePath)
            [void]$selectedRunNameList.Add($runName)
        }
    }

    return @{
        queue_config_path_list = @($selectedConfigPathList)
        run_name_list = @($selectedRunNameList)
    }
}

function Build-SubsetCampaignIdentity {

    param(
        [string]$BaseCampaignName,
        [string]$BaseCampaignOutputDirectory,
        [string]$DirectionName,
        [string[]]$RequestedFamilyList,
        [string]$StageName
    )

    $directionSlug = $DirectionName.ToLowerInvariant()
    $familySlug = if ($RequestedFamilyList -contains "All") {
        "all"
    }
    else {
        (($RequestedFamilyList | ForEach-Object { $_.ToLowerInvariant() }) -join "_")
    }
    $stageSlug = $StageName.ToLowerInvariant()
    $scopeSlug = "{0}_{1}_{2}" -f $directionSlug, $familySlug, $stageSlug
    return @{
        campaign_name = "{0}__{1}" -f $BaseCampaignName, $scopeSlug
        campaign_output_directory = "{0}__{1}" -f $BaseCampaignOutputDirectory, $scopeSlug
    }
}

function Resolve-RequestedFamilyList {

    param(
        [string]$FamilyName,
        [string]$FamiliesText
    )

    $requestedTokenList = New-Object System.Collections.ArrayList

    if (-not [string]::IsNullOrWhiteSpace($FamiliesText)) {
        foreach ($familyToken in ($FamiliesText -split ",")) {
            $normalizedToken = $familyToken.Trim().ToUpperInvariant()
            if (-not [string]::IsNullOrWhiteSpace($normalizedToken)) {
                [void]$requestedTokenList.Add($normalizedToken)
            }
        }
    }
    elseif (-not [string]::IsNullOrWhiteSpace($FamilyName)) {
        [void]$requestedTokenList.Add($FamilyName.Trim().ToUpperInvariant())
    }

    if ($requestedTokenList.Count -eq 0) {
        [void]$requestedTokenList.Add("ALL")
    }

    $resolvedFamilyList = New-Object System.Collections.ArrayList
    foreach ($requestedToken in @($requestedTokenList | Select-Object -Unique)) {
        if ($requestedToken -eq "ALL") {
            return @("All")
        }

        if ($ExactPaperFamilyOrder -notcontains $requestedToken) {
            throw "Unsupported exact-paper family selector | $requestedToken"
        }

        [void]$resolvedFamilyList.Add($requestedToken)
    }

    return @($resolvedFamilyList | Select-Object -Unique)
}

$CampaignQueueBundle = Get-CampaignQueueBundle `
    -CampaignYamlPath $ActiveCampaignPath `
    -ProjectRootPath $ProjectRoot `
    -EnvironmentName $CondaEnvironmentName `
    -PythonCommand $PythonExecutable

$RequestedFamilyList = Resolve-RequestedFamilyList `
    -FamilyName $Family `
    -FamiliesText $Families

$SelectedQueueBundle = Select-CampaignQueueEntries `
    -CampaignBundle $CampaignQueueBundle `
    -DirectionName $Direction `
    -RequestedFamilyList $RequestedFamilyList

if (@($SelectedQueueBundle.queue_config_path_list).Count -le 0) {
    throw "No prepared exact-paper configs matched the requested launcher scope | direction=$Direction | families=$($RequestedFamilyList -join ',')"
}

$InvocationCampaignIdentity = Build-SubsetCampaignIdentity `
    -BaseCampaignName $CampaignQueueBundle.campaign_name `
    -BaseCampaignOutputDirectory $CampaignQueueBundle.campaign_output_directory `
    -DirectionName $Direction `
    -RequestedFamilyList $RequestedFamilyList `
    -StageName $Stage

$RunnerArgumentList = @("--stage", $Stage.ToLowerInvariant())
if (-not [string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) {
    $RunnerArgumentList += @("--best-parameter-summary-path", $BestParameterSummaryPath)
}
if ($GridSearchVerboseOverride -ge 0) {
    $RunnerArgumentList += @("--grid-search-verbose-override", $GridSearchVerboseOverride.ToString())
}
if ($HistoricalCrossValidateVerboseOverride -ge 0) {
    $RunnerArgumentList += @("--historical-cross-validate-verbose-override", $HistoricalCrossValidateVerboseOverride.ToString())
}
if ($NoEval) {
    $RunnerArgumentList += "--no-eval"
}
if ($NoExport) {
    $RunnerArgumentList += "--no-export"
}

if ($Remote) {
    & ".\scripts\campaigns\track1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $InvocationCampaignIdentity.campaign_name `
        -PlanningReportPath $CampaignQueueBundle.planning_report_path `
        -LauncherRelativePath "scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1" `
        -LauncherArgumentList (@("-Direction", $Direction, "-Families", ($RequestedFamilyList -join ",")) + $RunnerArgumentList) `
        -CampaignOutputRootOverride $InvocationCampaignIdentity.campaign_output_directory `
        -CampaignConfigPathList @($SelectedQueueBundle.queue_config_path_list) `
        -RunNameList @($SelectedQueueBundle.run_name_list) `
        -ValidationOutputRoot "output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank" `
        -ValidationReportRoot "doc\reports\analysis\validation_checks" `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}

$CampaignOutputDirectory = $InvocationCampaignIdentity.campaign_output_directory
$CampaignLogRoot = Join-Path $ProjectRoot (Join-Path $CampaignOutputDirectory "logs")
New-Item -ItemType Directory -Force -Path $CampaignLogRoot | Out-Null

$QueueConfigPathList = @($SelectedQueueBundle.queue_config_path_list)
$QueueConfigCount = $QueueConfigPathList.Count

Write-Host "[INFO] Campaign Name | $($InvocationCampaignIdentity.campaign_name)" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $($CampaignQueueBundle.planning_report_path)" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $CampaignOutputDirectory" -ForegroundColor Cyan
Write-Host "[INFO] Requested Direction | $Direction" -ForegroundColor Cyan
Write-Host "[INFO] Requested Families | $($RequestedFamilyList -join ',')" -ForegroundColor Cyan
Write-Host "[INFO] Requested Stage | $Stage" -ForegroundColor Cyan
Write-Host "[INFO] Exact-Paper Run Count | $QueueConfigCount" -ForegroundColor Cyan

for ($ConfigIndex = 0; $ConfigIndex -lt $QueueConfigCount; $ConfigIndex++) {
    $ConfigRelativePath = $QueueConfigPathList[$ConfigIndex]
    $ConfigPath = Join-Path $ProjectRoot $ConfigRelativePath
    $ConfigFileStem = [System.IO.Path]::GetFileNameWithoutExtension($ConfigRelativePath)
    $RunLogPath = Join-Path $CampaignLogRoot ($ConfigFileStem + ".log")
    $CompletedCount = $ConfigIndex
    $RemainingCount = $QueueConfigCount - $CompletedCount
    $PercentComplete = if ($QueueConfigCount -gt 0) {
        [Math]::Round((100.0 * $CompletedCount) / $QueueConfigCount, 1)
    }
    else {
        0.0
    }

    Write-Host ("REMOTE_ACTIVE_CONFIG::{0}::{1}::{2}" -f ($ConfigIndex + 1), $QueueConfigCount, $ConfigRelativePath)
    Write-Host ("REMOTE_ACTIVE_LOG::{0}" -f (Join-Path $CampaignOutputDirectory ("logs\" + ($ConfigFileStem + ".log"))))
    Write-Host ("REMOTE_ACTIVE_STAGE::{0}" -f "Preparing exact-paper validation subprocess")
    Write-Host ("[INFO] Campaign progress | completed={0}/{1} | remaining={2} | percent={3:N1}% | active_run={4}" -f $CompletedCount, $QueueConfigCount, $RemainingCount, $PercentComplete, $ConfigFileStem) -ForegroundColor Cyan
    Write-Host ("[INFO] Running paper-faithful grid-search validation | {0}" -f $ConfigPath) -ForegroundColor Cyan
    Write-Progress -Id 2000 -Activity "Exact-paper family-stage launcher" -Status ("Completed {0}/{1} | Remaining {2}" -f $CompletedCount, $QueueConfigCount, $RemainingCount) -CurrentOperation $ConfigFileStem -PercentComplete ([Math]::Min(99, [int]$PercentComplete))

    $NativeExitCode = Invoke-CondaRunWithLoggedOutput `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath $RunnerPath `
        -ConfigPath $ConfigPath `
        -OutputSuffix "campaign_validation" `
        -LogPath $RunLogPath `
        -AdditionalArgumentList $RunnerArgumentList `
        -SuppressGridSearchConsoleNoise `
        -GridSearchHeartbeatSeconds 10 `
        -EmitRemoteStageMarkers

    if ($NativeExitCode -ne 0) {
        throw "Paper-faithful grid-search campaign run failed | $ConfigPath"
    }

    Write-Host ("REMOTE_COMPLETED_CONFIG::{0}::{1}::{2}" -f ($ConfigIndex + 1), $QueueConfigCount, $ConfigRelativePath)
    Write-Host ("REMOTE_ACTIVE_STAGE::{0}" -f "Completed exact-paper validation subprocess")
    Write-Host ("[DONE] Exact-paper config complete | {0}" -f $ConfigRelativePath) -ForegroundColor Green
}

Write-Progress -Id 2000 -Activity "Exact-paper family-stage launcher" -Completed
Write-Host "[DONE] Track 1 bidirectional paper-faithful grid-search campaign completed" -ForegroundColor Green
