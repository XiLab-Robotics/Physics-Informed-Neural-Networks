param(
    [ValidateSet("Retune", "PaperEval")]
    [string]$Stage = "Retune",
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$Families = "",
    [double]$TestSize = 0.20,
    [string]$OutputSuffix = "",
    [string]$DataframePath = "",
    [string]$BestParameterSummaryPath = "",
    [switch]$SkipPaperEval,
    [switch]$SkipPaperExport,
    [switch]$PrintOnly
)

$ErrorActionPreference = "Stop"

# Resolve The Repository Root From The Script Location.
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path
Set-Location $projectRoot
. (Join-Path $scriptDirectory "shared_rcim_original_launcher_helpers.ps1")

# Build The Campaign Root Under output/training_campaigns Instead Of models/paper_reference.
$runLabel = if ($Stage -eq "Retune") { "bw_v17_retune_bundle" } else { "bw_paper_reference_bundle" }
$runContext = New-RcimOriginalRunRoot `
    -ProjectRoot $projectRoot `
    -DirectionLabel "backward" `
    -RunLabel $runLabel `
    -OutputSuffix $OutputSuffix `
    -CreateDirectories:(-not $PrintOnly)

Write-Host "[INFO] RCIM Original Backward Reference Training" -ForegroundColor Cyan
Write-Host "[INFO] Stage | $Stage" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Cyan
Write-Host "[INFO] Logs Root | $($runContext.LogsRoot)" -ForegroundColor Cyan

$stageResultList = @()

if ($Stage -eq "Retune") {
    $retuneRoot = Join-Path $runContext.CampaignRoot "retune"
    if (-not $PrintOnly) {
        New-Item -ItemType Directory -Force -Path $retuneRoot | Out-Null
    }

    $retuneResult = Invoke-RcimOriginalPythonStage `
        -ProjectRoot $projectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -StageName "retune" `
        -StageRoot $retuneRoot `
        -LogsRoot $runContext.LogsRoot `
        -ModeName "retune" `
        -DirectionName "backward" `
        -Families $Families `
        -TestSize $TestSize `
        -DataframePath $DataframePath `
        -BestParameterSummaryPath "" `
        -PrintOnly:$PrintOnly

    $stageResultList += [pscustomobject]@{
        Stage = "retune"
        ExitCode = $retuneResult.ExitCode
        StdoutLogPath = $retuneResult.StdoutLogPath
        StderrLogPath = $retuneResult.StderrLogPath
        CombinedLogPath = $retuneResult.CombinedLogPath
        StageRoot = $retuneRoot
    }

    if ($retuneResult.ExitCode -ne 0) {
        Write-Host "[ERROR] Backward Retune Stage Failed." -ForegroundColor Red
        exit $retuneResult.ExitCode
    }

    Write-Host "[DONE] Backward Retune Completed." -ForegroundColor Green
    Write-Host "[DONE] Inspect summaryBestParameter+*.csv Under | $retuneRoot\output_prediction" -ForegroundColor Green
}
else {
    if ([string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) {
        Write-Host "[WARNING] No Best-Parameter Summary Path Was Provided. The Built-In Tuned Family Map Will Be Used." -ForegroundColor Yellow
    }
    else {
        Write-Host "[INFO] Best-Parameter Summary Path | $BestParameterSummaryPath" -ForegroundColor Cyan
    }

    if (-not $SkipPaperEval) {
        $paperEvalRoot = Join-Path $runContext.CampaignRoot "paper_eval"
        if (-not $PrintOnly) {
            New-Item -ItemType Directory -Force -Path $paperEvalRoot | Out-Null
        }

        $paperEvalResult = Invoke-RcimOriginalPythonStage `
            -ProjectRoot $projectRoot `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable `
            -StageName "paper_eval" `
            -StageRoot $paperEvalRoot `
            -LogsRoot $runContext.LogsRoot `
            -ModeName "paper_eval" `
            -DirectionName "backward" `
            -Families $Families `
            -TestSize $TestSize `
            -DataframePath $DataframePath `
            -BestParameterSummaryPath $BestParameterSummaryPath `
            -PrintOnly:$PrintOnly

        $stageResultList += [pscustomobject]@{
            Stage = "paper_eval"
            ExitCode = $paperEvalResult.ExitCode
            StdoutLogPath = $paperEvalResult.StdoutLogPath
            StderrLogPath = $paperEvalResult.StderrLogPath
            CombinedLogPath = $paperEvalResult.CombinedLogPath
            StageRoot = $paperEvalRoot
        }

        if ($paperEvalResult.ExitCode -ne 0) {
            Write-Host "[ERROR] Backward Paper-Eval Stage Failed." -ForegroundColor Red
            exit $paperEvalResult.ExitCode
        }
    }

    if (-not $SkipPaperExport) {
        $paperExportRoot = Join-Path $runContext.CampaignRoot "paper_export"
        if (-not $PrintOnly) {
            New-Item -ItemType Directory -Force -Path $paperExportRoot | Out-Null
        }

        $paperExportResult = Invoke-RcimOriginalPythonStage `
            -ProjectRoot $projectRoot `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable `
            -StageName "paper_export" `
            -StageRoot $paperExportRoot `
            -LogsRoot $runContext.LogsRoot `
            -ModeName "paper_export" `
            -DirectionName "backward" `
            -Families $Families `
            -TestSize $TestSize `
            -DataframePath $DataframePath `
            -BestParameterSummaryPath $BestParameterSummaryPath `
            -PrintOnly:$PrintOnly

        $stageResultList += [pscustomobject]@{
            Stage = "paper_export"
            ExitCode = $paperExportResult.ExitCode
            StdoutLogPath = $paperExportResult.StdoutLogPath
            StderrLogPath = $paperExportResult.StderrLogPath
            CombinedLogPath = $paperExportResult.CombinedLogPath
            StageRoot = $paperExportRoot
        }

        if ($paperExportResult.ExitCode -ne 0) {
            Write-Host "[ERROR] Backward Paper-Export Stage Failed." -ForegroundColor Red
            exit $paperExportResult.ExitCode
        }
    }
}

if (-not $PrintOnly) {
    $launcherSummaryPath = Join-Path $runContext.CampaignRoot "launcher_summary.json"
    [pscustomobject]@{
        direction = "backward"
        stage = $Stage
        run_instance_id = $runContext.RunInstanceId
        campaign_root = $runContext.CampaignRoot
        logs_root = $runContext.LogsRoot
        best_parameter_summary_path = $(if ([string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) { $null } else { $BestParameterSummaryPath })
        skipped_paper_eval = [bool]$SkipPaperEval
        skipped_paper_export = [bool]$SkipPaperExport
        stage_results = $stageResultList
    } | ConvertTo-Json -Depth 6 | Set-Content -Path $launcherSummaryPath -Encoding UTF8

    Write-Host "[DONE] RCIM Original Backward Reference Training Completed." -ForegroundColor Green
    Write-Host "[DONE] Launcher Summary | $launcherSummaryPath" -ForegroundColor Green
}
else {
    Write-Host "[DONE] RCIM Original Backward Reference Training Preview Completed." -ForegroundColor Green
    Write-Host "[DONE] No Files Were Written Because -PrintOnly Was Used." -ForegroundColor Green
}

Write-Host "[DONE] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Green
exit 0
