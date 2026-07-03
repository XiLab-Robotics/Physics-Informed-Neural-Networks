param(
    [switch]$Run,
    [switch]$Remote,
    [switch]$AcknowledgeFullWaveClosureMerged,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$ReportDate = (Get-Date -Format "yyyy-MM-dd"),
    [string[]]$DatasetList = @("polished_dataset", "simplified_dataset"),
    [string[]]$SurfaceScopeList = @("forward", "backward", "global"),
    [string[]]$ForwardCandidatePair = @(),
    [string[]]$BackwardCandidatePair = @(),
    [string[]]$GlobalCandidatePair = @(),
    [switch]$SkipVisualReports,
    [switch]$SkipDifferenceReports,
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
$differenceRunnerPath = "scripts\reports\analysis\build_track2_dataset_difference_report.py"
$pdfPipelinePath = "scripts\reports\pdf\run_report_pipeline.py"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_dataset_surface_report_split" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))

function Write-StatusLine {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Format-CmdArgument {
    param(
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return '""'
    }

    $escapedValue = $Value.Replace('"', '\"')
    if ($escapedValue.Contains(" ") -or $escapedValue.Contains("&") -or $escapedValue.Contains("[") -or $escapedValue.Contains("]")) {
        return ('"{0}"' -f $escapedValue)
    }

    return $escapedValue
}

function Invoke-LoggedCondaPython {
    param(
        [string]$StepName,
        [string[]]$ArgumentList
    )

    New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
    $logPath = Join-Path $logRoot ("{0}.log" -f $StepName)
    Write-StatusLine "STEP" ("Running {0} | log={1}" -f $StepName, $logPath)

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    $fullArgumentList = @("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + $ArgumentList
    $commandText = (@($condaExecutablePath) + $fullArgumentList | ForEach-Object { Format-CmdArgument -Value $_ }) -join " "
    $redirectedCommandText = "{0} > {1} 2>&1" -f $commandText, (Format-CmdArgument -Value $logPath)

    $processStartInfo = [System.Diagnostics.ProcessStartInfo]::new()
    $processStartInfo.FileName = "cmd.exe"
    $processStartInfo.Arguments = ('/d /c {0}' -f $redirectedCommandText)
    $processStartInfo.UseShellExecute = $false
    $processStartInfo.CreateNoWindow = $true
    $processStartInfo.WorkingDirectory = $projectRoot

    $process = [System.Diagnostics.Process]::new()
    $process.StartInfo = $processStartInfo
    try {
        $null = $process.Start()
        $process.WaitForExit()
    }
    finally {
        if (($null -ne $process) -and (-not $process.HasExited)) {
            $process.Kill()
        }
    }

    if (Test-Path -LiteralPath $logPath) {
        Get-Content -Tail 120 -LiteralPath $logPath | ForEach-Object { Write-Host $_ }
    }

    if ([int]$process.ExitCode -ne 0) {
        throw ("TE Curve Verification Pipeline step failed | step={0} | exit_code={1} | log={2}" -f $StepName, [int]$process.ExitCode, $logPath)
    }
}

function Get-CandidatePairListForSurface {
    param(
        [string]$SurfaceScope
    )

    if ($SurfaceScope -eq "forward") {
        return $ForwardCandidatePair
    }
    if ($SurfaceScope -eq "backward") {
        return $BackwardCandidatePair
    }
    if ($SurfaceScope -eq "global") {
        return $GlobalCandidatePair
    }
    return @()
}

function Format-RemoteSingleQuotedArgument {
    param(
        [string]$Value
    )

    return "'{0}'" -f $Value.Replace("'", "''")
}

function Format-RemoteCandidatePairArguments {
    $argumentText = ""
    foreach ($candidatePair in $ForwardCandidatePair) {
        $argumentText += " -ForwardCandidatePair " + (Format-RemoteSingleQuotedArgument -Value $candidatePair)
    }
    foreach ($candidatePair in $BackwardCandidatePair) {
        $argumentText += " -BackwardCandidatePair " + (Format-RemoteSingleQuotedArgument -Value $candidatePair)
    }
    foreach ($candidatePair in $GlobalCandidatePair) {
        $argumentText += " -GlobalCandidatePair " + (Format-RemoteSingleQuotedArgument -Value $candidatePair)
    }
    return $argumentText
}

function Assert-LaunchGate {
    $activeCampaignText = Get-Content -Raw -LiteralPath "doc\running\active_training_campaign.yaml"
    if ($activeCampaignText -notmatch "status:\s+none") {
        throw "Active local campaign state is not clear. Inspect doc/running/active_training_campaign.yaml before launching."
    }
    if (-not $AcknowledgeFullWaveClosureMerged) {
        throw "Full-wave polished retraining closure merge gate is not acknowledged. Merge the closure commits/artifacts, then rerun with -AcknowledgeFullWaveClosureMerged."
    }
}

function Write-ExecutionPlan {
    Write-StatusLine "PLAN" ("Report date: {0}" -f $ReportDate)
    Write-StatusLine "PLAN" ("Datasets: {0}" -f ($DatasetList -join ", "))
    Write-StatusLine "PLAN" ("Surface scopes: {0}" -f ($SurfaceScopeList -join ", "))
    Write-StatusLine "PLAN" "Run gate: full-wave polished retraining closure commits/artifacts must be merged before -Run."
    foreach ($datasetName in $DatasetList) {
        foreach ($surfaceScope in $SurfaceScopeList) {
            $outputSuffix = "track2_dataset_surface_{0}_{1}_{2}" -f $datasetName, $surfaceScope, $ReportDate.Replace("-", "_")
            Write-Host ("  matrix: {0} / {1} / {2}" -f $datasetName, $surfaceScope, $outputSuffix)
            if (-not $SkipVisualReports) {
                Write-Host ("  collage: {0} / {1}" -f $datasetName, $surfaceScope)
                if ($surfaceScope -ne "global") {
                    Write-Host ("  overlay: {0} / {1}" -f $datasetName, $surfaceScope)
                }
            }
        }
    }
    if (-not $SkipDifferenceReports) {
        Write-StatusLine "PLAN" ("Forward pairs: {0}" -f ($(if ($ForwardCandidatePair.Count) { $ForwardCandidatePair -join ", " } else { "<none>" })))
        Write-StatusLine "PLAN" ("Backward pairs: {0}" -f ($(if ($BackwardCandidatePair.Count) { $BackwardCandidatePair -join ", " } else { "<none>" })))
        Write-StatusLine "PLAN" ("Global pairs: {0}" -f ($(if ($GlobalCandidatePair.Count) { $GlobalCandidatePair -join ", " } else { "<none>" })))
    }
}

if ($Remote) {
    $remoteScriptPath = "scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1"
    $remoteCandidatePairArgumentText = Format-RemoteCandidatePairArguments
    $remoteCommand = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& '.\$remoteScriptPath' -Run -AcknowledgeFullWaveClosureMerged -CondaEnvironmentName '$RemoteCondaEnvironmentName' -ReportDate '$ReportDate'$remoteCandidatePairArgumentText$(if ($SkipVisualReports) { " -SkipVisualReports" } else { "" })$(if ($SkipDifferenceReports) { " -SkipDifferenceReports" } else { "" })$(if ($SkipPdfExport) { " -SkipPdfExport" } else { "" })
exit `$LASTEXITCODE
"@
    Write-StatusLine "REMOTE" ("Launching remote dataset-surface report split on {0}" -f $RemoteHostAlias)
    ssh $RemoteHostAlias $remoteCommand
    exit $LASTEXITCODE
}

Write-ExecutionPlan
if (-not $Run) {
    Write-StatusLine "DONE" "Dry run only. Re-run with -Run -AcknowledgeFullWaveClosureMerged after the full-wave closure merge is present."
    exit 0
}

Assert-LaunchGate

foreach ($datasetName in $DatasetList) {
    foreach ($surfaceScope in $SurfaceScopeList) {
        $outputSuffix = "track2_dataset_surface_{0}_{1}_{2}" -f $datasetName, $surfaceScope, $ReportDate.Replace("-", "_")
        $safeStepPrefix = "{0}_{1}" -f $datasetName, $surfaceScope

        Invoke-LoggedCondaPython `
            -StepName ("01_matrix_{0}" -f $safeStepPrefix) `
            -ArgumentList @(
                "-B",
                $matrixRunnerPath,
                "--config-path",
                $track2ConfigPath,
                "--output-suffix",
                $outputSuffix,
                "--dataset",
                $datasetName,
                "--surface-scope",
                $surfaceScope,
                "--windows"
            )

        if (-not $SkipVisualReports) {
            $collageReportRoot = "doc\reports\analysis\track2\dataset_surface_report\$datasetName\$surfaceScope\collage"
            Invoke-LoggedCondaPython `
                -StepName ("02_collage_{0}" -f $safeStepPrefix) `
                -ArgumentList @(
                    "-B",
                    $collageRunnerPath,
                    "--config-path",
                    $track2ConfigPath,
                    "--report-topic-root",
                    $collageReportRoot,
                    "--report-date",
                    $ReportDate,
                    "--dataset",
                    $datasetName,
                    "--surface-scope",
                    $surfaceScope,
                    "--windows"
                )

            if ($surfaceScope -ne "global") {
                $overlayReportRoot = "doc\reports\analysis\track2\dataset_surface_report\$datasetName\$surfaceScope\overlay"
                Invoke-LoggedCondaPython `
                    -StepName ("03_overlay_{0}" -f $safeStepPrefix) `
                    -ArgumentList @(
                        "-B",
                        $overlayRunnerPath,
                        "--config-path",
                        $track2ConfigPath,
                        "--report-topic-root",
                        $overlayReportRoot,
                        "--report-date",
                        $ReportDate,
                        "--dataset",
                        $datasetName,
                        "--surface-scope",
                        $surfaceScope,
                        "--windows"
                    )
            }
        }
    }
}

if (-not $SkipDifferenceReports) {
    foreach ($surfaceScope in $SurfaceScopeList) {
        $candidatePairList = Get-CandidatePairListForSurface -SurfaceScope $surfaceScope
        if ($candidatePairList.Count -eq 0) {
            Write-StatusLine "SKIP" ("No dataset-difference candidate pairs supplied for {0}" -f $surfaceScope)
            continue
        }
        foreach ($datasetName in $DatasetList) {
            $argumentList = @(
                "-B",
                $differenceRunnerPath,
                "--config-path",
                $track2ConfigPath,
                "--report-date",
                $ReportDate,
                "--dataset",
                $datasetName,
                "--surface-scope",
                $surfaceScope,
                "--windows"
            )
            foreach ($candidatePair in $candidatePairList) {
                $argumentList += @("--candidate-pair", $candidatePair)
            }
            Invoke-LoggedCondaPython `
                -StepName ("04_difference_{0}_{1}" -f $datasetName, $surfaceScope) `
                -ArgumentList $argumentList
        }
    }
}

if (-not $SkipPdfExport) {
    Write-StatusLine "INFO" "PDF export remains a post-generation review step for the generated split reports."
}

Write-StatusLine "DONE" ("Dataset-surface report split completed | logs={0}" -f $logRoot)
