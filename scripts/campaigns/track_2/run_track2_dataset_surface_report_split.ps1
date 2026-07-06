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
    [string]$ResumeFromStep = "",
    [switch]$SkipVisualReports,
    [switch]$SkipDifferenceReports,
    [switch]$SkipPdfExport,
    [switch]$ProgressSmokeTest
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
$script:resumeGateOpened = [string]::IsNullOrWhiteSpace($ResumeFromStep)

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
    $lastProgressLineLength = 0

    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    $fullArgumentList = @("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + $ArgumentList
    $commandText = (@($condaExecutablePath) + $fullArgumentList | ForEach-Object { Format-CmdArgument -Value $_ }) -join " "
    $cmdWrappedCommandText = "{0} 2>&1" -f $commandText
    Write-StatusLine "CMD" $commandText

    $previousPythonIoEncoding = $env:PYTHONIOENCODING
    $previousPythonUtf8 = $env:PYTHONUTF8
    $previousTqdmAscii = $env:TQDM_ASCII
    $previousTqdmMinInterval = $env:TQDM_MININTERVAL
    $env:PYTHONIOENCODING = "utf-8"
    $env:PYTHONUTF8 = "1"
    $env:TQDM_ASCII = "1"
    $env:TQDM_MININTERVAL = "10"

    $utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $false
    $logWriter = [System.IO.StreamWriter]::new($logPath, $false, $utf8NoBomEncoding)
    $lineBuilder = [System.Text.StringBuilder]::new()
    try {
        $processStartInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $processStartInfo.FileName = $env:ComSpec
        $processStartInfo.Arguments = "/d /c $cmdWrappedCommandText"
        $processStartInfo.UseShellExecute = $false
        $processStartInfo.RedirectStandardOutput = $true
        $processStartInfo.RedirectStandardError = $false
        $processStartInfo.CreateNoWindow = $true
        $processStartInfo.WorkingDirectory = $projectRoot
        $processStartInfo.StandardOutputEncoding = $utf8NoBomEncoding

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $processStartInfo
        [void]$process.Start()

        while ($true) {
            $readValue = $process.StandardOutput.Read()
            if ($readValue -lt 0) {
                break
            }

            $outputCharacter = [char]$readValue
            if ($outputCharacter -ne "`r" -and $outputCharacter -ne "`n") {
                [void]$lineBuilder.Append($outputCharacter)
                continue
            }

            $outputLine = $lineBuilder.ToString()
            [void]$lineBuilder.Clear()
            if ($outputLine.Length -gt 0) {
                $isProgressLine = $outputLine -match "\|\s*[# 0-9]+\|" -and $outputLine -match "\d+/\d+"
                if ($isProgressLine) {
                    $paddedOutputLine = $outputLine.PadRight($lastProgressLineLength)
                    [Console]::Write("`r{0}" -f $paddedOutputLine)
                    $lastProgressLineLength = [Math]::Max($lastProgressLineLength, $outputLine.Length)
                }
                else {
                    if ($lastProgressLineLength -gt 0) {
                        [Console]::WriteLine("")
                        $lastProgressLineLength = 0
                    }
                    Write-Host $outputLine
                }
                $logWriter.WriteLine($outputLine)
            }
            if ($outputCharacter -eq "`n" -and $lastProgressLineLength -gt 0) {
                [Console]::WriteLine("")
                $lastProgressLineLength = 0
            }
        }

        if ($lineBuilder.Length -gt 0) {
            $outputLine = $lineBuilder.ToString()
            $isProgressLine = $outputLine -match "\|\s*[# 0-9]+\|" -and $outputLine -match "\d+/\d+"
            if ($isProgressLine) {
                $paddedOutputLine = $outputLine.PadRight($lastProgressLineLength)
                [Console]::Write("`r{0}" -f $paddedOutputLine)
                $lastProgressLineLength = [Math]::Max($lastProgressLineLength, $outputLine.Length)
            }
            else {
                if ($lastProgressLineLength -gt 0) {
                    [Console]::WriteLine("")
                    $lastProgressLineLength = 0
                }
                Write-Host $outputLine
            }
            $logWriter.WriteLine($outputLine)
            [void]$lineBuilder.Clear()
        }

        $process.WaitForExit()
        $exitCode = [int]$process.ExitCode
        if ($lastProgressLineLength -gt 0) {
            [Console]::WriteLine("")
        }
    }
    finally {
        if ($null -ne $logWriter) {
            $logWriter.Dispose()
        }
        $env:PYTHONIOENCODING = $previousPythonIoEncoding
        $env:PYTHONUTF8 = $previousPythonUtf8
        $env:TQDM_ASCII = $previousTqdmAscii
        $env:TQDM_MININTERVAL = $previousTqdmMinInterval
    }

    if ($exitCode -ne 0) {
        throw ("TE Curve Verification Pipeline step failed | step={0} | exit_code={1} | log={2}" -f $StepName, $exitCode, $logPath)
    }
}

function Test-ShouldRunStep {
    param(
        [string]$StepName
    )

    if ($script:resumeGateOpened) {
        return $true
    }
    if ($StepName -eq $ResumeFromStep) {
        $script:resumeGateOpened = $true
        Write-StatusLine "RESUME" ("Reached requested resume step: {0}" -f $StepName)
        return $true
    }
    Write-StatusLine "SKIP" ("Resume gate skipping {0}; waiting for {1}" -f $StepName, $ResumeFromStep)
    return $false
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

if ($ProgressSmokeTest) {
    Invoke-LoggedCondaPython `
        -StepName "00_progress_smoke_test" `
        -ArgumentList @(
            "-B",
            "-c",
            "from pathlib import Path; from tqdm import tqdm; import time; assert (Path.cwd() / 'scripts' / 'paper_reimplementation').exists(), f'unexpected cwd: {Path.cwd()}'; [time.sleep(0.1) for _ in tqdm(range(50), desc='tqdm smoke', unit='it', ascii=True, ncols=80, dynamic_ncols=False)]"
        )
    Write-StatusLine "DONE" ("Progress smoke test completed | logs={0}" -f $logRoot)
    exit 0
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
    $isNoActiveCampaignState = $activeCampaignText -match "status:\s+none"
    $isCompletedPolishedRefreshState = (
        ($activeCampaignText -match "status:\s+completed") -and
        ($activeCampaignText -match "campaign_name:\s+polished_dataset_te_curve_verification_refresh_2026_07_02") -and
        ($activeCampaignText -match "te_curve_verification_status:\s+completed")
    )
    if ((-not $isNoActiveCampaignState) -and (-not $isCompletedPolishedRefreshState)) {
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
    if (-not [string]::IsNullOrWhiteSpace($ResumeFromStep)) {
        Write-StatusLine "PLAN" ("Resume from step: {0}" -f $ResumeFromStep)
    }
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
& '.\$remoteScriptPath' -Run -AcknowledgeFullWaveClosureMerged -CondaEnvironmentName '$RemoteCondaEnvironmentName' -ReportDate '$ReportDate'$(if (-not [string]::IsNullOrWhiteSpace($ResumeFromStep)) { " -ResumeFromStep '$ResumeFromStep'" } else { "" })$remoteCandidatePairArgumentText$(if ($SkipVisualReports) { " -SkipVisualReports" } else { "" })$(if ($SkipDifferenceReports) { " -SkipDifferenceReports" } else { "" })$(if ($SkipPdfExport) { " -SkipPdfExport" } else { "" })
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

        $matrixStepName = "01_matrix_{0}" -f $safeStepPrefix
        if (Test-ShouldRunStep -StepName $matrixStepName) {
            Invoke-LoggedCondaPython `
                -StepName $matrixStepName `
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
        }

        if (-not $SkipVisualReports) {
            $collageReportRoot = "doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\$datasetName\$surfaceScope\collage"
            $collageStepName = "02_collage_{0}" -f $safeStepPrefix
            if (Test-ShouldRunStep -StepName $collageStepName) {
                Invoke-LoggedCondaPython `
                    -StepName $collageStepName `
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
            }

            if ($surfaceScope -ne "global") {
                $overlayReportRoot = "doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\$datasetName\$surfaceScope\overlay"
                $overlayStepName = "03_overlay_{0}" -f $safeStepPrefix
                if (Test-ShouldRunStep -StepName $overlayStepName) {
                    Invoke-LoggedCondaPython `
                        -StepName $overlayStepName `
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
            $differenceStepName = "04_difference_{0}_{1}" -f $datasetName, $surfaceScope
            if (Test-ShouldRunStep -StepName $differenceStepName) {
                Invoke-LoggedCondaPython `
                    -StepName $differenceStepName `
                    -ArgumentList $argumentList
            }
        }
    }
}

if (-not $SkipPdfExport) {
    Write-StatusLine "INFO" "PDF export remains a post-generation review step for the generated split reports."
}

Write-StatusLine "DONE" ("Dataset-surface report split completed | logs={0}" -f $logRoot)
