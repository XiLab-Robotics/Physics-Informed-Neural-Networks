function Format-RcimOriginalCommandPreview {
    param(
        [string]$CondaBatchPath,
        [string[]]$ArgumentList
    )

    $quotedArgumentList = $ArgumentList | ForEach-Object {
        if ($_ -match '\s') { '"' + $_ + '"' }
        else { $_ }
    }
    return '"' + $CondaBatchPath + '" ' + ($quotedArgumentList -join " ")
}

function Test-RcimOriginalProgressLine {
    param(
        [string]$Line
    )

    if ([string]::IsNullOrWhiteSpace($Line)) { return $false }
    return (
        $Line.StartsWith("[PROGRESS]") -or
        $Line.StartsWith("[INFO]") -or
        $Line.StartsWith("[DONE]") -or
        $Line.StartsWith("[ERROR]") -or
        $Line.StartsWith("MODEL:") -or
        $Line.StartsWith("TRAINING START:") -or
        $Line.StartsWith("TRAINING END:")
    )
}

function New-RcimOriginalRunRoot {
    param(
        [string]$ProjectRoot,
        [string]$DirectionLabel,
        [string]$RunLabel,
        [string]$OutputSuffix,
        [switch]$CreateDirectories
    )

    $runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
    $runInstanceId = $runTimestamp + "__" + $RunLabel
    if (-not [string]::IsNullOrWhiteSpace($OutputSuffix)) {
        $runInstanceId = $runInstanceId + "_" + $OutputSuffix
    }

    $campaignRoot = Join-Path $ProjectRoot ("output\training_campaigns\rcim_original\" + $DirectionLabel + "\" + $runInstanceId)
    $logsRoot = Join-Path $campaignRoot "logs"
    if ($CreateDirectories) {
        New-Item -ItemType Directory -Force -Path $campaignRoot | Out-Null
        New-Item -ItemType Directory -Force -Path $logsRoot | Out-Null
    }

    return [pscustomobject]@{
        RunInstanceId = $runInstanceId
        CampaignRoot = $campaignRoot
        LogsRoot = $logsRoot
    }
}

function Invoke-RcimOriginalPythonStage {
    param(
        [string]$ProjectRoot,
        [string]$CondaEnvironmentName,
        [string]$PythonExecutable,
        [string]$StageName,
        [string]$StageRoot,
        [string]$LogsRoot,
        [string]$ModeName,
        [string]$DirectionName,
        [string]$Families,
        [double]$TestSize,
        [string]$DataframePath,
        [string]$BestParameterSummaryPath,
        [switch]$PrintOnly
    )

    $condaExecutablePath = (where.exe conda.exe | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
        throw "Unable to resolve conda.exe on PATH."
    }

    $argumentList = @(
        "run", "-n", $CondaEnvironmentName,
        $PythonExecutable,
        "-B",
        "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py",
        "--mode", $ModeName,
        "--direction", $DirectionName,
        "--test-size", $TestSize.ToString([System.Globalization.CultureInfo]::InvariantCulture),
        "--output-root", $StageRoot
    )

    if (-not [string]::IsNullOrWhiteSpace($Families)) {
        $argumentList += @("--families", $Families)
    }

    if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
        $argumentList += @("--dataframe-path", $DataframePath)
    }

    if (-not [string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) {
        $argumentList += @("--best-parameter-summary-path", $BestParameterSummaryPath)
    }

    $commandPreview = Format-RcimOriginalCommandPreview -CondaBatchPath $condaExecutablePath -ArgumentList $argumentList
    $stdoutLogPath = Join-Path $LogsRoot ($StageName + ".stdout.log")
    $stderrLogPath = Join-Path $LogsRoot ($StageName + ".stderr.log")
    $combinedLogPath = Join-Path $LogsRoot ($StageName + ".combined.log")

    Write-Host "[INFO] Stage | $StageName" -ForegroundColor Cyan
    Write-Host "[INFO] Mode | $ModeName" -ForegroundColor Cyan
    Write-Host "[INFO] Direction | $DirectionName" -ForegroundColor Cyan
    Write-Host "[INFO] Stage Root | $StageRoot" -ForegroundColor Cyan
    Write-Host "[INFO] Stdout Log | $stdoutLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Stderr Log | $stderrLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Combined Log | $combinedLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Command | $commandPreview" -ForegroundColor DarkCyan

    if ($PrintOnly) {
        return [pscustomobject]@{
            ExitCode = 0
            StdoutLogPath = $stdoutLogPath
            StderrLogPath = $stderrLogPath
            CombinedLogPath = $combinedLogPath
            SuppressedStdoutLineCount = 0
            SuppressedStderrLineCount = 0
        }
    }

    $stdoutWriter = New-Object System.IO.StreamWriter($stdoutLogPath, $false, [System.Text.Encoding]::UTF8)
    $stderrWriter = New-Object System.IO.StreamWriter($stderrLogPath, $false, [System.Text.Encoding]::UTF8)
    $combinedWriter = New-Object System.IO.StreamWriter($combinedLogPath, $false, [System.Text.Encoding]::UTF8)
    $counterState = [pscustomobject]@{
        SuppressedStdoutLineCount = 0
        SuppressedStderrLineCount = 0
    }
    $exitCode = 0

    try {
        Push-Location $ProjectRoot
        $previousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"

        # Run the training stage through PowerShell native process handling so the wrapper can
        # stream output reliably without the fragile .NET async event plumbing used before.
        & $condaExecutablePath @argumentList 2>&1 | ForEach-Object {
            $record = $_
            $line = $record.ToString()
            $isErrorRecord = $record -is [System.Management.Automation.ErrorRecord]

            if ($isErrorRecord) {
                $stderrWriter.WriteLine($line)
                $stderrWriter.Flush()
                $combinedWriter.WriteLine("[STDERR] " + $line)
                $combinedWriter.Flush()

                if (Test-RcimOriginalProgressLine -Line $line) {
                    Write-Host $line -ForegroundColor Yellow
                }
                else {
                    $counterState.SuppressedStderrLineCount++
                }
            }
            else {
                $stdoutWriter.WriteLine($line)
                $stdoutWriter.Flush()
                $combinedWriter.WriteLine("[STDOUT] " + $line)
                $combinedWriter.Flush()

                if (Test-RcimOriginalProgressLine -Line $line) {
                    Write-Host $line -ForegroundColor Cyan
                }
                else {
                    $counterState.SuppressedStdoutLineCount++
                }
            }
        }

        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
        Pop-Location
        $stdoutWriter.Flush()
        $stderrWriter.Flush()
        $combinedWriter.Flush()
        $stdoutWriter.Close()
        $stderrWriter.Close()
        $combinedWriter.Close()
    }

    Write-Host "[INFO] Suppressed Stdout Lines | $($counterState.SuppressedStdoutLineCount)" -ForegroundColor DarkGray
    Write-Host "[INFO] Suppressed Stderr Lines | $($counterState.SuppressedStderrLineCount)" -ForegroundColor DarkGray
    Write-Host "[INFO] Stage Exit Code | $exitCode" -ForegroundColor DarkGray

    return [pscustomobject]@{
        ExitCode = $exitCode
        StdoutLogPath = $stdoutLogPath
        StderrLogPath = $stderrLogPath
        CombinedLogPath = $combinedLogPath
        SuppressedStdoutLineCount = $counterState.SuppressedStdoutLineCount
        SuppressedStderrLineCount = $counterState.SuppressedStderrLineCount
    }
}
