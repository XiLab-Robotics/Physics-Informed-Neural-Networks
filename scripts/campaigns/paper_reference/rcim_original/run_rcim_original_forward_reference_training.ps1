param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$Families = "",
    [double]$TestSize = 0.20,
    [string]$OutputSuffix = "",
    [string]$DataframePath = "",
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
$runContext = New-RcimOriginalRunRoot `
    -ProjectRoot $projectRoot `
    -DirectionLabel "forward" `
    -RunLabel "fw_paper_reference_bundle" `
    -OutputSuffix $OutputSuffix `
    -CreateDirectories:(-not $PrintOnly)

$paperEvalRoot = Join-Path $runContext.CampaignRoot "paper_eval"
$paperExportRoot = Join-Path $runContext.CampaignRoot "paper_export"
if (-not $PrintOnly) {
    New-Item -ItemType Directory -Force -Path $paperEvalRoot | Out-Null
    New-Item -ItemType Directory -Force -Path $paperExportRoot | Out-Null
}

Write-Host "[INFO] RCIM Original Forward Reference Training" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Cyan
Write-Host "[INFO] Logs Root | $($runContext.LogsRoot)" -ForegroundColor Cyan

$stageResultList = @()

if (-not $SkipPaperEval) {
    $paperEvalResult = Invoke-RcimOriginalPythonStage `
        -ProjectRoot $projectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -StageName "paper_eval" `
        -StageRoot $paperEvalRoot `
        -LogsRoot $runContext.LogsRoot `
        -ModeName "paper_eval" `
        -DirectionName "forward" `
        -Families $Families `
        -TestSize $TestSize `
        -DataframePath $DataframePath `
        -BestParameterSummaryPath "" `
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
        Write-Host "[ERROR] Forward Paper-Eval Stage Failed." -ForegroundColor Red
        exit $paperEvalResult.ExitCode
    }
}

if (-not $SkipPaperExport) {
    $paperExportResult = Invoke-RcimOriginalPythonStage `
        -ProjectRoot $projectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -StageName "paper_export" `
        -StageRoot $paperExportRoot `
        -LogsRoot $runContext.LogsRoot `
        -ModeName "paper_export" `
        -DirectionName "forward" `
        -Families $Families `
        -TestSize $TestSize `
        -DataframePath $DataframePath `
        -BestParameterSummaryPath "" `
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
        Write-Host "[ERROR] Forward Paper-Export Stage Failed." -ForegroundColor Red
        exit $paperExportResult.ExitCode
    }
}

if (-not $PrintOnly) {
    $launcherSummaryPath = Join-Path $runContext.CampaignRoot "launcher_summary.json"
    [pscustomobject]@{
        direction = "forward"
        run_instance_id = $runContext.RunInstanceId
        campaign_root = $runContext.CampaignRoot
        logs_root = $runContext.LogsRoot
        skipped_paper_eval = [bool]$SkipPaperEval
        skipped_paper_export = [bool]$SkipPaperExport
        stage_results = $stageResultList
    } | ConvertTo-Json -Depth 6 | Set-Content -Path $launcherSummaryPath -Encoding UTF8

    Write-Host "[DONE] RCIM Original Forward Reference Training Completed." -ForegroundColor Green
    Write-Host "[DONE] Launcher Summary | $launcherSummaryPath" -ForegroundColor Green
}
else {
    Write-Host "[DONE] RCIM Original Forward Reference Training Preview Completed." -ForegroundColor Green
    Write-Host "[DONE] No Files Were Written Because -PrintOnly Was Used." -ForegroundColor Green
}

Write-Host "[DONE] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Green
exit 0
