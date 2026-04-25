$script:invoke_exact_paper_campaign_local_root = $PSScriptRoot
$script:invoke_exact_paper_campaign_local_project_root = (Resolve-Path (Join-Path $script:invoke_exact_paper_campaign_local_root "..\..\..\..")).Path

function Invoke-ExactPaperCampaignLocal {

    param(
        [Parameter(Mandatory = $true)]
        [string]$CampaignName,

        [Parameter(Mandatory = $true)]
        [string]$PlanningReportPath,

        [Parameter(Mandatory = $true)]
        [string]$CampaignConfigRoot,

        [Parameter(Mandatory = $true)]
        [string[]]$CampaignConfigFileNameList,

        [string]$CampaignOutputRootOverride = "",
        [string]$RunnerScriptPath = "scripts\paper_reimplementation\rcim_ml_compensation\run_exact_paper_model_bank_validation.py",
        [string]$OutputSuffix = "campaign_run",
        [string]$CondaEnvironmentName = "standard_ml_codex_env",
        [string]$PythonExecutable = "python"
    )

    . (Join-Path $script:invoke_exact_paper_campaign_local_project_root "scripts\campaigns\infrastructure\shared_streaming_campaign_launcher.ps1")

    $campaignOutputRoot = if ([string]::IsNullOrWhiteSpace($CampaignOutputRootOverride)) {
        Join-Path "output\training_campaigns\track1\exact_paper" $CampaignName
    }
    else {
        $CampaignOutputRootOverride
    }
    $campaignLogRoot = Join-Path $campaignOutputRoot "logs"

    New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

    $campaignConfigPathList = @()
    foreach ($configFileName in $CampaignConfigFileNameList) {
        $campaignConfigPathList += (Join-Path $CampaignConfigRoot $configFileName)
    }

    Write-Host "[INFO] Campaign Name | $CampaignName" -ForegroundColor Cyan
    Write-Host "[INFO] Planning Report | $PlanningReportPath" -ForegroundColor Cyan
    Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
    Write-Host "[INFO] Exact-Paper Run Count | $($campaignConfigPathList.Count)" -ForegroundColor Cyan

    for ($configIndex = 0; $configIndex -lt $campaignConfigPathList.Count; $configIndex++) {
        $configPath = $campaignConfigPathList[$configIndex]
        $configFileName = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
        $runLogPath = Join-Path $campaignLogRoot ($configFileName + ".log")

        Write-Host ""
        Write-Host ("=" * 96) -ForegroundColor DarkCyan
        Write-Host ("REMOTE_ACTIVE_CONFIG::{0}::{1}::{2}" -f ($configIndex + 1), $campaignConfigPathList.Count, $configPath)
        Write-Host ("REMOTE_ACTIVE_LOG::{0}" -f $runLogPath)
        Write-Host ("REMOTE_ACTIVE_STAGE::{0}" -f "Preparing exact-paper validation subprocess")
        Write-Host ("[INFO] Exact-Paper Campaign Progress {0}/{1} | {2}" -f ($configIndex + 1), $campaignConfigPathList.Count, $configPath) -ForegroundColor Cyan
        Write-Host ("[INFO] Log Path | {0}" -f $runLogPath) -ForegroundColor Cyan
        Write-Host ("=" * 96) -ForegroundColor DarkCyan

        $nativeExitCode = Invoke-CondaRunWithLoggedOutput `
            -EnvironmentName $CondaEnvironmentName `
            -PythonExecutablePath $PythonExecutable `
            -RunnerScriptPath $RunnerScriptPath `
            -ConfigPath $configPath `
            -OutputSuffix $OutputSuffix `
            -LogPath $runLogPath `
            -SuppressGridSearchConsoleNoise `
            -GridSearchHeartbeatSeconds 20 `
            -EmitRemoteStageMarkers

        if ($nativeExitCode -ne 0) {
            Write-Host "[ERROR] Exact-paper campaign run failed | $configPath" -ForegroundColor Red
            Write-Host "[ERROR] Failing log file | $runLogPath" -ForegroundColor Red
            return $nativeExitCode
        }

        Write-Host ("REMOTE_COMPLETED_CONFIG::{0}::{1}::{2}" -f ($configIndex + 1), $campaignConfigPathList.Count, $configPath)
        Write-Host ("REMOTE_ACTIVE_STAGE::{0}" -f "Completed exact-paper validation subprocess")
        Write-Host ("[DONE] Exact-paper config complete | {0}" -f $configPath) -ForegroundColor Green
    }

    Write-Host ""
    Write-Host "[DONE] Exact-paper campaign completed successfully" -ForegroundColor Green
    Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
    return 0
}
