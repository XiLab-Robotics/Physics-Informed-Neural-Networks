param(
    [switch]$Run,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$ReportDate = (Get-Date -Format "yyyy-MM-dd"),
    [string[]]$DatasetList = @("polished_dataset", "simplified_dataset"),
    [string[]]$SurfaceScopeList = @("forward", "backward"),
    [string]$ResumeFromStep = ""
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
Set-Location $projectRoot

$track2ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\reduced_selected_track2_matrix.yaml"
$matrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$validationReportRoot = "doc\reports\analysis\validation_checks\te_curve_verification_pipeline"
$selectedReportRoot = "doc\reports\analysis\te_curve_verification_pipeline\04_selected_model_reports\[$ReportDate]"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_reduced_selected_track2_reports" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))
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

        while (-not $process.StandardOutput.EndOfStream) {
            $outputLine = $process.StandardOutput.ReadLine()
            if ($null -ne $outputLine) {
                Write-Host $outputLine
                $logWriter.WriteLine($outputLine)
            }
        }

        $process.WaitForExit()
        $exitCode = [int]$process.ExitCode
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
        throw ("Reduced TE Curve Verification Pipeline step failed | step={0} | exit_code={1} | log={2}" -f $StepName, $exitCode, $logPath)
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

function Assert-LaunchGate {
    $activeCampaignText = Get-Content -Raw -LiteralPath "doc\running\active_training_campaign.yaml"
    $isNoActiveCampaignState = $activeCampaignText -match "status:\s+none"
    $isCompletedRefreshState = (
        ($activeCampaignText -match "status:\s+completed") -and
        ($activeCampaignText -match "te_curve_verification_status:\s+completed")
    )
    if ((-not $isNoActiveCampaignState) -and (-not $isCompletedRefreshState)) {
        throw "Active campaign state is not clear. Inspect doc/running/active_training_campaign.yaml before launching."
    }
}

function Move-LatestSelectedReport {
    param(
        [string]$DatasetName,
        [string]$SurfaceScope,
        [string]$OutputSuffix
    )

    $reportSearchRoot = Join-Path $projectRoot $validationReportRoot
    $matchingReport = Get-ChildItem -LiteralPath $reportSearchRoot -Filter "*$OutputSuffix*_report.md" |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $matchingReport) {
        throw "Cannot find generated selected-model report for output suffix: $OutputSuffix"
    }

    $destinationDirectory = Join-Path $projectRoot $selectedReportRoot
    New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
    $destinationFileName = "track2_selected_models_{0}_{1}_report.md" -f $DatasetName, $SurfaceScope
    $destinationPath = Join-Path $destinationDirectory $destinationFileName
    Move-Item -LiteralPath $matchingReport.FullName -Destination $destinationPath -Force
    Write-StatusLine "REPORT" ("Selected report written | {0}" -f (Resolve-Path -LiteralPath $destinationPath -Relative))
}

function Write-ExecutionPlan {
    Write-StatusLine "PLAN" ("Report date: {0}" -f $ReportDate)
    Write-StatusLine "PLAN" ("Config: {0}" -f $track2ConfigPath)
    Write-StatusLine "PLAN" ("Datasets: {0}" -f ($DatasetList -join ", "))
    Write-StatusLine "PLAN" ("Surface scopes: {0}" -f ($SurfaceScopeList -join ", "))
    Write-StatusLine "PLAN" "Paused by default: global, collage, overlay, and simplified-vs-polished dataset-difference reports."
    foreach ($datasetName in $DatasetList) {
        foreach ($surfaceScope in $SurfaceScopeList) {
            $outputSuffix = "track2_selected_{0}_{1}_{2}" -f $datasetName, $surfaceScope, $ReportDate.Replace("-", "_")
            Write-Host ("  report: {0} / {1} / {2}" -f $datasetName, $surfaceScope, $outputSuffix)
        }
    }
}

Write-ExecutionPlan
if (-not $Run) {
    Write-StatusLine "DONE" "Dry run only. Re-run with -Run to generate the four reduced selected-model reports."
    exit 0
}

Assert-LaunchGate

foreach ($datasetName in $DatasetList) {
    foreach ($surfaceScope in $SurfaceScopeList) {
        if ($surfaceScope -eq "global") {
            throw "The reduced selected-model launcher does not generate global reports."
        }

        $outputSuffix = "track2_selected_{0}_{1}_{2}" -f $datasetName, $surfaceScope, $ReportDate.Replace("-", "_")
        $stepName = "01_matrix_{0}_{1}" -f $datasetName, $surfaceScope
        if (Test-ShouldRunStep -StepName $stepName) {
            Invoke-LoggedCondaPython `
                -StepName $stepName `
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
            Move-LatestSelectedReport -DatasetName $datasetName -SurfaceScope $surfaceScope -OutputSuffix $outputSuffix
        }
    }
}

Write-StatusLine "DONE" ("Reduced selected-model reports completed | reports={0} | logs={1}" -f $selectedReportRoot, $logRoot)
