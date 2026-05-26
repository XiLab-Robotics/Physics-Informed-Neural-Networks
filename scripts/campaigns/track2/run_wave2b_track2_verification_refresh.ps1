param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "wave2b_harmonic_temporal_hybrid_track2_refresh_2026_05_26",
    [string]$ReportDate = "2026-05-26",
    [switch]$SkipVisualReports,
    [switch]$SkipPdfExport
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$track2ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\full_track2_matrix_template.yaml"
$matrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$collageRunnerPath = "scripts\reports\analysis\build_track2_best_model_collage_report.py"
$overlayRunnerPath = "scripts\reports\analysis\build_track2_multi_model_curve_comparison_report.py"
$pdfPipelinePath = "scripts\reports\pdf\run_report_pipeline.py"
$collageReportPath = "doc\reports\analysis\track2\best_model_collage_report\[$ReportDate]\track2_best_model_collage_report.md"
$overlayReportPath = "doc\reports\analysis\track2\multi_model_curve_comparison_report\[$ReportDate]\track2_multi_model_curve_comparison_report.md"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_{1}" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"), $OutputSuffix)

function Write-StatusLine {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Invoke-LoggedCondaPython {
    param(
        [string]$StepName,
        [string[]]$ArgumentList
    )

    New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
    $logPath = Join-Path $logRoot ("{0}.log" -f $StepName)

    Write-StatusLine "STEP" ("Running {0} | log={1}" -f $StepName, $logPath)
    & conda run --no-capture-output -n $CondaEnvironmentName python @ArgumentList 2>&1 |
        Tee-Object -FilePath $logPath

    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw ("Track 2 step failed | step={0} | exit_code={1} | log={2}" -f $StepName, $exitCode, $logPath)
    }
}

if ($Remote) {
    if ([string]::IsNullOrWhiteSpace($RemoteRepositoryPath)) {
        throw "RemoteRepositoryPath is required for -Remote. Set PINNS_REMOTE_TRAINING_REPO_PATH or pass -RemoteRepositoryPath."
    }

    Write-StatusLine "INFO" ("Launching Track 2 refresh remotely | host={0} | repo={1}" -f $RemoteHostAlias, $RemoteRepositoryPath)
    $remoteScriptPath = "scripts\campaigns\track2\run_wave2b_track2_verification_refresh.ps1"
    $remoteCommand = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& '.\$remoteScriptPath' -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix' -ReportDate '$ReportDate'$(if ($SkipVisualReports) { " -SkipVisualReports" } else { "" })$(if ($SkipPdfExport) { " -SkipPdfExport" } else { "" })
exit `$LASTEXITCODE
"@

    $remoteCommand | ssh $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command -"
    exit $LASTEXITCODE
}

Write-StatusLine "INFO" "Preparing local Wave 2B Track 2 verification refresh"
Write-StatusLine "INFO" ("Config: {0}" -f $track2ConfigPath)
Write-StatusLine "INFO" ("Output suffix: {0}" -f $OutputSuffix)
Write-StatusLine "INFO" ("Report date: {0}" -f $ReportDate)

Invoke-LoggedCondaPython `
    -StepName "01_track2_matrix" `
    -ArgumentList @(
        "-B",
        $matrixRunnerPath,
        "--config-path",
        $track2ConfigPath,
        "--output-suffix",
        $OutputSuffix,
        "--windows"
    )

if (-not $SkipVisualReports) {
    Invoke-LoggedCondaPython `
        -StepName "02_track2_best_model_collage_report" `
        -ArgumentList @(
            "-B",
            $collageRunnerPath,
            "--config-path",
            $track2ConfigPath,
            "--report-date",
            $ReportDate,
            "--windows"
        )

    Invoke-LoggedCondaPython `
        -StepName "03_track2_multi_model_curve_comparison_report" `
        -ArgumentList @(
            "-B",
            $overlayRunnerPath,
            "--config-path",
            $track2ConfigPath,
            "--report-date",
            $ReportDate,
            "--windows"
        )

    if (-not $SkipPdfExport) {
        Invoke-LoggedCondaPython `
            -StepName "04_track2_visual_report_pdf_export" `
            -ArgumentList @(
                "-B",
                $pdfPipelinePath,
                "--input-markdown-path",
                $collageReportPath,
                "--input-markdown-path",
                $overlayReportPath,
                "--clean-temp",
                "--windows"
            )
    }
}

Write-StatusLine "DONE" ("Track 2 operator-launched refresh completed | log_root={0}" -f $logRoot)
Write-StatusLine "DONE" "Tell Codex the run completed so the official decision report and closeout synchronization can be inspected."
