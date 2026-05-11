param(
    [string]$PythonExecutable = "python",
    [string[]]$GpuIdList = @("0")
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignRoot = "config\training\wave1_directional_best_hyperparameter_search\campaigns\2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
$gridQueueRoot = Join-Path $campaignRoot "grid_queue"
$optunaStudyRoot = Join-Path $campaignRoot "optuna_studies"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md"
$campaignName = "wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11"
$campaignOutputRoot = "output\training_campaigns\wave1\directional_best_hyperparameter_search\$campaignName"
$launcherLogRoot = Join-Path $campaignOutputRoot "launcher_logs"
New-Item -ItemType Directory -Path $launcherLogRoot -Force | Out-Null

$gridQueueConfigPathList = Get-ChildItem -Path $gridQueueRoot -Filter *.yaml -File | Sort-Object Name | ForEach-Object { $_.FullName }
$optunaStudyConfigPathList = Get-ChildItem -Path $optunaStudyRoot -Filter *.yaml -File | Sort-Object Name | ForEach-Object { $_.FullName }

if ($gridQueueConfigPathList.Count -gt 0) {
    Write-Host "[INFO] Running bounded CPU grid phase | $($gridQueueConfigPathList.Count) configs" -ForegroundColor Cyan
    $gridArgumentList = @("scripts\training\run_training_campaign.py") + $gridQueueConfigPathList + @(
        "--campaign-name", $campaignName,
        "--planning-report-path", $planningReportPath
    )
    & $PythonExecutable @gridArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "Bounded grid phase failed | exit_code=$LASTEXITCODE"
    }
}

if ($optunaStudyConfigPathList.Count -eq 0) {
    Write-Host "[INFO] No Optuna study configs found | neural HPO phase skipped" -ForegroundColor Yellow
    exit 0
}

if ($GpuIdList.Count -le 0) {
    throw "GpuIdList must contain at least one GPU id."
}

for ($batchStartIndex = 0; $batchStartIndex -lt $optunaStudyConfigPathList.Count; $batchStartIndex += $GpuIdList.Count) {
    $processRecordList = @()

    for ($slotIndex = 0; $slotIndex -lt $GpuIdList.Count; $slotIndex++) {
        $studyIndex = $batchStartIndex + $slotIndex
        if ($studyIndex -ge $optunaStudyConfigPathList.Count) {
            break
        }

        $gpuId = $GpuIdList[$slotIndex]
        $studyConfigPath = $optunaStudyConfigPathList[$studyIndex]
        $studyStem = [System.IO.Path]::GetFileNameWithoutExtension($studyConfigPath)
        $stdoutPath = Join-Path $launcherLogRoot "$studyStem.stdout.log"
        $stderrPath = Join-Path $launcherLogRoot "$studyStem.stderr.log"
        $argumentList = @(
            "scripts\training\run_optuna_neural_hpo_study.py",
            "--study-config-path", $studyConfigPath,
            "--gpu-id", $gpuId
        )

        $process = Start-Process `
            -FilePath $PythonExecutable `
            -ArgumentList $argumentList `
            -WorkingDirectory $projectRoot `
            -RedirectStandardOutput $stdoutPath `
            -RedirectStandardError $stderrPath `
            -WindowStyle Hidden `
            -PassThru

        $processRecordList += [PSCustomObject]@{
            Process = $process
            StudyConfigPath = $studyConfigPath
            GpuId = $gpuId
            StdoutPath = $stdoutPath
            StderrPath = $stderrPath
        }
    }

    foreach ($processRecord in $processRecordList) {
        $processRecord.Process.WaitForExit()
        if ($processRecord.Process.ExitCode -ne 0) {
            throw ("Optuna study failed | gpu={0} | config={1} | stdout={2} | stderr={3} | exit_code={4}" -f `
                $processRecord.GpuId, `
                $processRecord.StudyConfigPath, `
                $processRecord.StdoutPath, `
                $processRecord.StderrPath, `
                $processRecord.Process.ExitCode)
        }
    }
}

Write-Host "[DONE] Wave 1 directional best-hyperparameter search launcher completed" -ForegroundColor Green
