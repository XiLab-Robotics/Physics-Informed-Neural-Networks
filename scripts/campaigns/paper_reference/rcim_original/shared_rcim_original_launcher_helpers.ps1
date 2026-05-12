function Format-RcimOriginalCommandPreview {
    param(
        [string]$ExecutablePath,
        [string[]]$ArgumentList
    )

    $quotedArgumentList = $ArgumentList | ForEach-Object {
        if ($_ -match '\s') { '"' + $_ + '"' }
        else { $_ }
    }
    return '"' + $ExecutablePath + '" ' + ($quotedArgumentList -join " ")
}

function ConvertTo-RcimOriginalArgumentString {
    param(
        [string[]]$ArgumentList
    )

    $quotedArgumentList = $ArgumentList | ForEach-Object {
        if ($_ -match '[\s"]') {
            '"' + ($_.Replace('"', '\"')) + '"'
        }
        else {
            $_
        }
    }
    return ($quotedArgumentList -join " ")
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

function Initialize-RcimOriginalStageLogSurface {
    param(
        [string]$StdoutLogPath,
        [string]$StderrLogPath,
        [string]$CombinedLogPath,
        [string[]]$MetadataLineList
    )

    foreach ($path in @($StdoutLogPath, $StderrLogPath, $CombinedLogPath)) {
        if (Test-Path $path) {
            Remove-Item -LiteralPath $path -Force
        }
    }

    foreach ($path in @($StdoutLogPath, $StderrLogPath, $CombinedLogPath)) {
        New-Item -ItemType File -Path $path -Force | Out-Null
        Set-Content -LiteralPath $path -Value $MetadataLineList -Encoding UTF8
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
        [int]$RetuneGridSearchVerbose = 10,
        [int]$RetuneCrossValidateVerbose = 10,
        [ref]$StageResult,
        [switch]$PrintOnly
    )

    $condaExecutablePath = (where.exe conda.exe | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
        throw "Unable to resolve conda.exe on PATH."
    }

    $environmentPythonPath = Get-RcimOriginalEnvironmentPythonPath -CondaEnvironmentName $CondaEnvironmentName
    $useDirectEnvironmentPython = -not [string]::IsNullOrWhiteSpace($environmentPythonPath)
    $trainingArgumentList = @(
        "--mode", $ModeName,
        "--direction", $DirectionName,
        "--test-size", $TestSize.ToString([System.Globalization.CultureInfo]::InvariantCulture),
        "--output-root", $StageRoot
    )
    if (-not [string]::IsNullOrWhiteSpace($Families)) {
        $trainingArgumentList += @("--families", $Families)
    }

    if (-not [string]::IsNullOrWhiteSpace($DataframePath)) {
        $trainingArgumentList += @("--dataframe-path", $DataframePath)
    }

    if (-not [string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) {
        $trainingArgumentList += @("--best-parameter-summary-path", $BestParameterSummaryPath)
    }

    if ($ModeName -eq "retune") {
        $trainingArgumentList += @("--retune-grid-search-verbose", $RetuneGridSearchVerbose)
        $trainingArgumentList += @("--retune-cross-validate-verbose", $RetuneCrossValidateVerbose)
    }

    $stdoutLogPath = Join-Path $LogsRoot ($StageName + ".stdout.log")
    $stderrLogPath = Join-Path $LogsRoot ($StageName + ".stderr.log")
    $combinedLogPath = Join-Path $LogsRoot ($StageName + ".combined.log")

    if ($useDirectEnvironmentPython) {
        $commandExecutablePath = $environmentPythonPath
        $argumentList = @(
            "-u",
            "-B",
            "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py"
        ) + $trainingArgumentList
    }
    else {
        $commandExecutablePath = $condaExecutablePath
        $argumentList = @(
            "run", "-n", $CondaEnvironmentName,
            $PythonExecutable,
            "-u",
            "-B",
            "scripts\paper_reimplementation\rcim_ml_compensation\recovered_original_workflow\training_models.py"
        ) + $trainingArgumentList
    }

    $commandPreview = Format-RcimOriginalCommandPreview `
        -ExecutablePath $commandExecutablePath `
        -ArgumentList $argumentList

    Write-Host "[INFO] Stage | $StageName" -ForegroundColor Cyan
    Write-Host "[INFO] Mode | $ModeName" -ForegroundColor Cyan
    Write-Host "[INFO] Direction | $DirectionName" -ForegroundColor Cyan
    Write-Host "[INFO] Stage Root | $StageRoot" -ForegroundColor Cyan
    Write-Host "[INFO] Stdout Log | $stdoutLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Stderr Log | $stderrLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Combined Log | $combinedLogPath" -ForegroundColor Cyan
    Write-Host "[INFO] Command | $commandPreview" -ForegroundColor DarkCyan

    if ($PrintOnly) {
        $resultObject = [pscustomobject]@{
            ExitCode = 0
            StdoutLogPath = $stdoutLogPath
            StderrLogPath = $stderrLogPath
            CombinedLogPath = $combinedLogPath
            SuppressedStdoutLineCount = 0
            SuppressedStderrLineCount = 0
        }
        if ($null -ne $StageResult) {
            $StageResult.Value = $resultObject
            return
        }
        return $resultObject
    }

    $compatibilityLogLines = @(
        "[INFO] RCIM Original Launcher Mirrored Live Log Mode",
        "[INFO] Stage | $StageName",
        "[INFO] Mode | $ModeName",
        "[INFO] Direction | $DirectionName",
        "[INFO] Stage Root | $StageRoot",
        "[INFO] Command | $commandPreview",
        "[INFO] Stdout Compatibility Log Path | $stdoutLogPath",
        "[INFO] Stderr Compatibility Log Path | $stderrLogPath",
        "[INFO] Combined Log Path | $combinedLogPath",
        "[INFO] The child training process output is mirrored to console, stdout compatibility log, and combined log.",
        "[INFO] The combined log is the authoritative persistent live log surface."
    )
    Initialize-RcimOriginalStageLogSurface `
        -StdoutLogPath $stdoutLogPath `
        -StderrLogPath $stderrLogPath `
        -CombinedLogPath $combinedLogPath `
        -MetadataLineList $compatibilityLogLines

    $exitCode = 0
    $stageInterrupted = $false

    try {
        Push-Location $ProjectRoot

        # Start-Transcript Does Not Reliably Capture Native Python Output On Windows
        # PowerShell 5. Mirror The Merged Native Output Explicitly As UTF-8 Text.
        & $commandExecutablePath @argumentList 2>&1 |
            ForEach-Object {
                $outputLine = $_.ToString()
                [Console]::Out.WriteLine($outputLine)
                Add-Content -LiteralPath $combinedLogPath -Value $outputLine -Encoding UTF8
                Add-Content -LiteralPath $stdoutLogPath -Value $outputLine -Encoding UTF8
            }
        $exitCode = $LASTEXITCODE
    }
    catch [System.Management.Automation.PipelineStoppedException] {
        $stageInterrupted = $true
        $exitCode = 130
    }
    finally {
        if ($transcriptStarted) {
            try {
                Stop-Transcript | Out-Null
            }
            catch {
            }
        }

        Pop-Location

        $completionLogLines = @(
            "[INFO] Mirrored Live Log Stage Completed | $(-not $stageInterrupted)",
            "[INFO] Stage Exit Code | $exitCode"
        )
        Add-Content -LiteralPath $combinedLogPath -Value $completionLogLines -Encoding UTF8
        Add-Content -LiteralPath $stdoutLogPath -Value $completionLogLines -Encoding UTF8
        Add-Content -LiteralPath $stderrLogPath -Value $completionLogLines -Encoding UTF8
    }

    Write-Host "[INFO] Stage Exit Code | $exitCode" -ForegroundColor DarkGray

    $resultObject = [pscustomobject]@{
        ExitCode = $exitCode
        StdoutLogPath = $stdoutLogPath
        StderrLogPath = $stderrLogPath
        CombinedLogPath = $combinedLogPath
        SuppressedStdoutLineCount = 0
        SuppressedStderrLineCount = 0
    }
    if ($null -ne $StageResult) {
        $StageResult.Value = $resultObject
        return
    }
    return $resultObject
}

function Get-RcimOriginalBestParameterRegistryPath {
    param(
        [string]$ProjectRoot
    )

    return (Join-Path $ProjectRoot "output\registries\program\rcim_original_best_hyperparameters.yaml")
}

function Get-RcimOriginalRetuneBestParameterSummaryPath {
    param(
        [string]$RetuneRoot
    )

    return (Join-Path $RetuneRoot "output_prediction\summaryBestParameter+_3.8_allFreq.csv")
}

function Get-RcimOriginalRetuneCrossValidationSummaryPath {
    param(
        [string]$RetuneRoot
    )

    return (Join-Path $RetuneRoot "output_prediction\summaryCrossValidation+_3.8_allFreq.csv")
}

function Get-RcimOriginalEnvironmentPythonPath {
    param(
        [string]$CondaEnvironmentName
    )

    if ([string]::IsNullOrWhiteSpace($CondaEnvironmentName)) {
        return $null
    }

    $condaExecutablePath = (where.exe conda.exe 2>$null | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
        throw "Unable to resolve conda.exe on PATH."
    }

    # Resolve The Environment Python Path From Conda's Registered Environment List.
    try {
        $environmentListJson = (& $condaExecutablePath env list --json 2>$null | Out-String)
        if (-not [string]::IsNullOrWhiteSpace($environmentListJson)) {
            $environmentList = $environmentListJson | ConvertFrom-Json

            foreach ($environmentPath in $environmentList.envs) {
                if ((Split-Path -Leaf $environmentPath) -eq $CondaEnvironmentName) {
                    $candidatePythonPath = Join-Path $environmentPath "python.exe"
                    if (Test-Path $candidatePythonPath) {
                        return (Resolve-Path $candidatePythonPath).Path
                    }
                }
            }
        }
    }
    catch {
        # Fall Back To Conda Base Resolution If The Environment Registry Cannot Be Parsed.
    }

    # Fall Back To The Standard Conda Base Environment Layout.
    $condaBasePath = (& $condaExecutablePath info --base 2>$null | Select-Object -Last 1)
    if (-not [string]::IsNullOrWhiteSpace($condaBasePath)) {
        $condaBasePath = $condaBasePath.Trim()
        $environmentPythonPath = Join-Path $condaBasePath ("envs\" + $CondaEnvironmentName + "\python.exe")
        if (Test-Path $environmentPythonPath) {
            return (Resolve-Path $environmentPythonPath).Path
        }
    }

    return $null
}

function Invoke-RcimOriginalRegistryHelper {
    param(
        [string]$ProjectRoot,
        [string]$CondaEnvironmentName,
        [string]$PythonExecutable,
        [string[]]$ArgumentList
    )

    $environmentPythonPath = Get-RcimOriginalEnvironmentPythonPath -CondaEnvironmentName $CondaEnvironmentName
    $useDirectEnvironmentPython = -not [string]::IsNullOrWhiteSpace($environmentPythonPath)
    if ($useDirectEnvironmentPython) {
        $commandExecutablePath = $environmentPythonPath
        $fullArgumentList = @(
            "-B",
            "scripts\campaigns\paper_reference\rcim_original\rcim_original_best_parameter_registry.py"
        ) + $ArgumentList
    }
    else {
        $condaExecutablePath = (where.exe conda.exe | Select-Object -First 1)
        if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
            throw "Unable to resolve conda.exe on PATH."
        }

        $commandExecutablePath = $condaExecutablePath
        $fullArgumentList = @(
            "run", "-n", $CondaEnvironmentName,
            $PythonExecutable,
            "-B",
            "scripts\campaigns\paper_reference\rcim_original\rcim_original_best_parameter_registry.py"
        ) + $ArgumentList
    }

    $outputLineList = @()
    Push-Location $ProjectRoot
    try {
        $previousErrorActionPreference = $ErrorActionPreference
        $previousNativePreference = $PSNativeCommandUseErrorActionPreference
        $ErrorActionPreference = "Continue"
        $PSNativeCommandUseErrorActionPreference = $false

        & $commandExecutablePath @fullArgumentList 2>&1 | ForEach-Object {
            $line = $_.ToString()
            $outputLineList += $line
            Write-Host $line -ForegroundColor DarkCyan
        }
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
        $PSNativeCommandUseErrorActionPreference = $previousNativePreference
        Pop-Location
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        OutputLines = $outputLineList
    }
}

function Resolve-RcimOriginalStoredBestSummary {
    param(
        [string]$ProjectRoot,
        [string]$CondaEnvironmentName,
        [string]$PythonExecutable,
        [string]$BranchName,
        [string]$Families,
        [string]$OutputSummaryPath
    )

    $registryPath = Get-RcimOriginalBestParameterRegistryPath -ProjectRoot $ProjectRoot
    $argumentList = @(
        "--registry-path", $registryPath,
        "materialize-summary",
        "--branch", $BranchName,
        "--output-summary-path", $OutputSummaryPath
    )
    if (-not [string]::IsNullOrWhiteSpace($Families)) {
        $argumentList += @("--families", $Families)
    }

    $helperResult = Invoke-RcimOriginalRegistryHelper `
        -ProjectRoot $ProjectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -ArgumentList $argumentList

    if ($helperResult.ExitCode -eq 0) {
        return [pscustomobject]@{
            HasCoverage = $true
            SummaryPath = $OutputSummaryPath
            RegistryPath = $registryPath
        }
    }
    if ($helperResult.ExitCode -eq 2) {
        return [pscustomobject]@{
            HasCoverage = $false
            SummaryPath = $null
            RegistryPath = $registryPath
        }
    }

    throw "Failed to materialize the stored best-parameter summary for branch $BranchName."
}

function Update-RcimOriginalStoredBestRegistry {
    param(
        [string]$ProjectRoot,
        [string]$CondaEnvironmentName,
        [string]$PythonExecutable,
        [string]$BranchName,
        [string]$BestParameterSummaryPath,
        [string]$CrossValidationSummaryPath,
        [switch]$PrintOnly
    )

    $registryPath = Get-RcimOriginalBestParameterRegistryPath -ProjectRoot $ProjectRoot
    if ($PrintOnly) {
        return [pscustomobject]@{
            RegistryPath = $registryPath
            Updated = $false
            PrintOnly = $true
        }
    }

    $helperResult = Invoke-RcimOriginalRegistryHelper `
        -ProjectRoot $ProjectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -ArgumentList @(
            "--registry-path", $registryPath,
            "update-from-retune",
            "--branch", $BranchName,
            "--best-parameter-summary-path", $BestParameterSummaryPath,
            "--cross-validation-summary-path", $CrossValidationSummaryPath
        )

    if ($helperResult.ExitCode -ne 0) {
        throw "Failed to update the stored best-parameter registry for branch $BranchName."
    }

    return [pscustomobject]@{
        RegistryPath = $registryPath
        Updated = $true
        PrintOnly = $false
    }
}
