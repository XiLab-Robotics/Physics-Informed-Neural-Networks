param(
    [ValidateSet("Forward", "Backward", "Both")]
    [string]$Branch = "Forward",
    [ValidateSet("Original", "Retune", "Eval", "Export", "LoadBest")]
    [string]$Stage = "LoadBest",
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$PythonExecutable = "python",
    [string]$Families = "",
    [double]$TestSize = 0.20,
    [string]$OutputSuffix = "",
    [string]$DataframePath = "",
    [string]$BestParameterSummaryPath = "",
    [int]$RetuneGridSearchVerbose = 10,
    [int]$RetuneCrossValidateVerbose = 10,
    [switch]$NoEval,
    [switch]$NoExport,
    [switch]$PrintOnly
)

$ErrorActionPreference = "Stop"

function Invoke-RcimOriginalReferenceBranchRun {
    param(
        [string]$ProjectRoot,
        [string]$CondaEnvironmentName,
        [string]$PythonExecutable,
        [string]$DirectionName,
        [string]$StageName,
        [string]$Families,
        [double]$TestSize,
        [string]$OutputSuffix,
        [string]$DataframePath,
        [string]$BestParameterSummaryPath,
        [int]$RetuneGridSearchVerbose,
        [int]$RetuneCrossValidateVerbose,
        [switch]$NoEval,
        [switch]$NoExport,
        [switch]$PrintOnly
    )

    # Build The Campaign Root For The Selected Branch And Operator Stage.
    $directionLabel = $DirectionName.ToLowerInvariant()
    $stageLabel = $StageName.ToLowerInvariant()
    $directionPrefix = if ($directionLabel -eq "forward") { "fw" } else { "bw" }
    $runLabel = "{0}_{1}_bundle" -f $directionPrefix, $stageLabel
    $runContext = New-RcimOriginalRunRoot `
        -ProjectRoot $ProjectRoot `
        -DirectionLabel $directionLabel `
        -RunLabel $runLabel `
        -OutputSuffix $OutputSuffix `
        -CreateDirectories:(-not $PrintOnly)

    Write-Host "[INFO] RCIM Original Reference Training" -ForegroundColor Cyan
    Write-Host "[INFO] Branch | $DirectionName" -ForegroundColor Cyan
    Write-Host "[INFO] Stage | $StageName" -ForegroundColor Cyan
    Write-Host "[INFO] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Cyan
    Write-Host "[INFO] Logs Root | $($runContext.LogsRoot)" -ForegroundColor Cyan

    $stageResultList = New-Object System.Collections.ArrayList
    $resolvedBestParameterSummaryPath = ""
    $resolvedParameterSourceName = "none"
    $registryPath = Get-RcimOriginalBestParameterRegistryPath -ProjectRoot $ProjectRoot
    $registryUpdateSummary = $null
    $noteList = @()
    $performedRetune = $false

    function Add-StageResult {
        param(
            [string]$StageLabel,
            [object]$StageResult,
            [string]$StageRoot
        )

        [void]$stageResultList.Add([pscustomobject]@{
            Stage = $StageLabel
            ExitCode = $StageResult.ExitCode
            StdoutLogPath = $StageResult.StdoutLogPath
            StderrLogPath = $StageResult.StderrLogPath
            CombinedLogPath = $StageResult.CombinedLogPath
            StageRoot = $StageRoot
        })
    }

    function Invoke-EvalExportChain {
        param(
            [bool]$UseBuiltInTunedMap,
            [string]$BestSummaryPath
        )

        # Resolve Which Downstream Stages Should Run For The Current Bundle.
        $shouldRunEval = -not $NoEval
        $shouldRunExport = -not $NoExport
        if (-not $shouldRunEval -and -not $shouldRunExport) {
            Write-Host "[WARNING] No Downstream Eval Or Export Stage Was Requested." -ForegroundColor Yellow
            $script:noteList += "No downstream eval/export stage was requested."
            return
        }

        if ($shouldRunEval) {
            $evalRoot = Join-Path $runContext.CampaignRoot "eval"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $evalRoot | Out-Null
            }

            $evalResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "eval" `
                -StageRoot $evalRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_eval" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath $(if ($UseBuiltInTunedMap) { "" } else { $BestSummaryPath }) `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$evalResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "eval" -StageResult $evalResult -StageRoot $evalRoot
            if ($evalResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Eval Stage Failed." -ForegroundColor Red
                exit $evalResult.ExitCode
            }
        }

        if ($shouldRunExport) {
            $exportRoot = Join-Path $runContext.CampaignRoot "export"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $exportRoot | Out-Null
            }

            $exportResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "export" `
                -StageRoot $exportRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_export" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath $(if ($UseBuiltInTunedMap) { "" } else { $BestSummaryPath }) `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$exportResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "export" -StageResult $exportResult -StageRoot $exportRoot
            if ($exportResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Export Stage Failed." -ForegroundColor Red
                exit $exportResult.ExitCode
            }
        }
    }

    function Resolve-StoredBestSummaryPath {
        param(
            [string]$RequestedStageName
        )

        # Respect One Explicit Best-Parameter Summary Path Before Falling Back To The Registry.
        if (-not [string]::IsNullOrWhiteSpace($BestParameterSummaryPath)) {
            $resolvedPath = (Resolve-Path $BestParameterSummaryPath).Path
            Write-Host "[INFO] Best-Parameter Summary Path | $resolvedPath" -ForegroundColor Cyan
            return [pscustomobject]@{
                HasCoverage = $true
                SourceName = "explicit_summary"
                SummaryPath = $resolvedPath
            }
        }

        $materializedSummaryPath = Join-Path $runContext.CampaignRoot "resolved_best_parameter_summary.csv"
        $materializeResult = Resolve-RcimOriginalStoredBestSummary `
            -ProjectRoot $ProjectRoot `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable `
            -BranchName $directionLabel `
            -Families $Families `
            -OutputSummaryPath $materializedSummaryPath

        if ($materializeResult.HasCoverage) {
            Write-Host "[INFO] Stored Best-Parameter Summary | $($materializeResult.SummaryPath)" -ForegroundColor Cyan
            return [pscustomobject]@{
                HasCoverage = $true
                SourceName = "stored_registry"
                SummaryPath = $materializeResult.SummaryPath
            }
        }

        if ($RequestedStageName -eq "LoadBest") {
            Write-Host "[WARNING] No Stored Best Parameters Were Found For $DirectionName. Falling Back To Retune." -ForegroundColor Yellow
            $script:noteList += "LoadBest fell back to Retune because the stored registry did not cover the requested family surface."
            return [pscustomobject]@{
                HasCoverage = $false
                SourceName = "missing_registry"
                SummaryPath = ""
            }
        }

        if ($directionLabel -eq "forward") {
            Write-Host "[WARNING] No Stored Best Parameters Were Found For Forward. Falling Back To The Original Built-In Tuned Map." -ForegroundColor Yellow
            $script:noteList += "Forward $RequestedStageName fell back to the built-in original tuned map because no stored best registry coverage was available."
            return [pscustomobject]@{
                HasCoverage = $true
                SourceName = "built_in_original"
                SummaryPath = ""
            }
        }

        throw "No best-parameter source is available for backward $RequestedStageName. Run -Stage Retune first or provide -BestParameterSummaryPath."
    }

    if ($StageName -eq "Original") {
        if ($directionLabel -eq "backward") {
            Write-Host "[WARNING] No Original Paper Backward Hyperparameter Map Is Available. Use -Stage Retune Or -Stage LoadBest Instead." -ForegroundColor Yellow
            $noteList += "Backward Original stage is unsupported because no recovered paper backward tuned hyperparameter map exists."
        }
        else {
            $resolvedParameterSourceName = "built_in_original"
            Invoke-EvalExportChain -UseBuiltInTunedMap $true -BestSummaryPath ""
        }
    }
    elseif ($StageName -eq "Retune") {
        $retuneRoot = Join-Path $runContext.CampaignRoot "retune"
        if (-not $PrintOnly) {
            New-Item -ItemType Directory -Force -Path $retuneRoot | Out-Null
        }

        $retuneResult = $null
        Invoke-RcimOriginalPythonStage `
            -ProjectRoot $ProjectRoot `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable `
            -StageName "retune" `
            -StageRoot $retuneRoot `
            -LogsRoot $runContext.LogsRoot `
            -ModeName "retune" `
            -DirectionName $directionLabel `
            -Families $Families `
            -TestSize $TestSize `
            -DataframePath $DataframePath `
            -BestParameterSummaryPath "" `
            -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
            -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
            -StageResult ([ref]$retuneResult) `
            -PrintOnly:$PrintOnly

        Add-StageResult -StageLabel "retune" -StageResult $retuneResult -StageRoot $retuneRoot
        if ($retuneResult.ExitCode -ne 0) {
            Write-Host "[ERROR] Retune Stage Failed." -ForegroundColor Red
            exit $retuneResult.ExitCode
        }

        $performedRetune = $true
        $resolvedBestParameterSummaryPath = Get-RcimOriginalRetuneBestParameterSummaryPath -RetuneRoot $retuneRoot
        $crossValidationSummaryPath = Get-RcimOriginalRetuneCrossValidationSummaryPath -RetuneRoot $retuneRoot
        $registryUpdateSummary = Update-RcimOriginalStoredBestRegistry `
            -ProjectRoot $ProjectRoot `
            -CondaEnvironmentName $CondaEnvironmentName `
            -PythonExecutable $PythonExecutable `
            -BranchName $directionLabel `
            -BestParameterSummaryPath $resolvedBestParameterSummaryPath `
            -CrossValidationSummaryPath $crossValidationSummaryPath `
            -PrintOnly:$PrintOnly

        $resolvedParameterSourceName = "retune_summary"
        Invoke-EvalExportChain -UseBuiltInTunedMap $false -BestSummaryPath $resolvedBestParameterSummaryPath
    }
    elseif ($StageName -eq "LoadBest") {
        $bestSummaryResolution = Resolve-StoredBestSummaryPath -RequestedStageName $StageName
        if (-not $bestSummaryResolution.HasCoverage) {
            $StageName = "Retune"
            $retuneRoot = Join-Path $runContext.CampaignRoot "retune"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $retuneRoot | Out-Null
            }

            $retuneResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "retune" `
                -StageRoot $retuneRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "retune" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath "" `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$retuneResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "retune" -StageResult $retuneResult -StageRoot $retuneRoot
            if ($retuneResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Retune Fallback Stage Failed." -ForegroundColor Red
                exit $retuneResult.ExitCode
            }

            $performedRetune = $true
            $resolvedBestParameterSummaryPath = Get-RcimOriginalRetuneBestParameterSummaryPath -RetuneRoot $retuneRoot
            $crossValidationSummaryPath = Get-RcimOriginalRetuneCrossValidationSummaryPath -RetuneRoot $retuneRoot
            $registryUpdateSummary = Update-RcimOriginalStoredBestRegistry `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -BranchName $directionLabel `
                -BestParameterSummaryPath $resolvedBestParameterSummaryPath `
                -CrossValidationSummaryPath $crossValidationSummaryPath `
                -PrintOnly:$PrintOnly

            $resolvedParameterSourceName = "retune_summary"
            Invoke-EvalExportChain -UseBuiltInTunedMap $false -BestSummaryPath $resolvedBestParameterSummaryPath
        }
        elseif ($bestSummaryResolution.SourceName -eq "built_in_original") {
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            Invoke-EvalExportChain -UseBuiltInTunedMap $true -BestSummaryPath ""
        }
        else {
            $resolvedBestParameterSummaryPath = $bestSummaryResolution.SummaryPath
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            Invoke-EvalExportChain -UseBuiltInTunedMap $false -BestSummaryPath $resolvedBestParameterSummaryPath
        }
    }
    elseif ($StageName -eq "Eval") {
        $bestSummaryResolution = Resolve-StoredBestSummaryPath -RequestedStageName $StageName
        if ($bestSummaryResolution.SourceName -eq "built_in_original") {
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            $evalRoot = Join-Path $runContext.CampaignRoot "eval"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $evalRoot | Out-Null
            }

            $evalResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "eval" `
                -StageRoot $evalRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_eval" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath "" `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$evalResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "eval" -StageResult $evalResult -StageRoot $evalRoot
            if ($evalResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Eval Stage Failed." -ForegroundColor Red
                exit $evalResult.ExitCode
            }
        }
        else {
            $resolvedBestParameterSummaryPath = $bestSummaryResolution.SummaryPath
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            $evalRoot = Join-Path $runContext.CampaignRoot "eval"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $evalRoot | Out-Null
            }

            $evalResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "eval" `
                -StageRoot $evalRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_eval" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath $resolvedBestParameterSummaryPath `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$evalResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "eval" -StageResult $evalResult -StageRoot $evalRoot
            if ($evalResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Eval Stage Failed." -ForegroundColor Red
                exit $evalResult.ExitCode
            }
        }
    }
    else {
        $bestSummaryResolution = Resolve-StoredBestSummaryPath -RequestedStageName $StageName
        if ($bestSummaryResolution.SourceName -eq "built_in_original") {
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            $exportRoot = Join-Path $runContext.CampaignRoot "export"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $exportRoot | Out-Null
            }

            $exportResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "export" `
                -StageRoot $exportRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_export" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath "" `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$exportResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "export" -StageResult $exportResult -StageRoot $exportRoot
            if ($exportResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Export Stage Failed." -ForegroundColor Red
                exit $exportResult.ExitCode
            }
        }
        else {
            $resolvedBestParameterSummaryPath = $bestSummaryResolution.SummaryPath
            $resolvedParameterSourceName = $bestSummaryResolution.SourceName
            $exportRoot = Join-Path $runContext.CampaignRoot "export"
            if (-not $PrintOnly) {
                New-Item -ItemType Directory -Force -Path $exportRoot | Out-Null
            }

            $exportResult = $null
            Invoke-RcimOriginalPythonStage `
                -ProjectRoot $ProjectRoot `
                -CondaEnvironmentName $CondaEnvironmentName `
                -PythonExecutable $PythonExecutable `
                -StageName "export" `
                -StageRoot $exportRoot `
                -LogsRoot $runContext.LogsRoot `
                -ModeName "paper_export" `
                -DirectionName $directionLabel `
                -Families $Families `
                -TestSize $TestSize `
                -DataframePath $DataframePath `
                -BestParameterSummaryPath $resolvedBestParameterSummaryPath `
                -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
                -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
                -StageResult ([ref]$exportResult) `
                -PrintOnly:$PrintOnly

            Add-StageResult -StageLabel "export" -StageResult $exportResult -StageRoot $exportRoot
            if ($exportResult.ExitCode -ne 0) {
                Write-Host "[ERROR] Export Stage Failed." -ForegroundColor Red
                exit $exportResult.ExitCode
            }
        }
    }

    if (-not $PrintOnly) {
        $launcherSummaryPath = Join-Path $runContext.CampaignRoot "launcher_summary.json"
        [pscustomobject]@{
            branch = $directionLabel
            requested_stage = $Stage
            effective_stage = $StageName
            run_instance_id = $runContext.RunInstanceId
            campaign_root = $runContext.CampaignRoot
            logs_root = $runContext.LogsRoot
            dataframe_path = $(if ([string]::IsNullOrWhiteSpace($DataframePath)) { $null } else { $DataframePath })
            best_parameter_summary_path = $(if ([string]::IsNullOrWhiteSpace($resolvedBestParameterSummaryPath)) { $null } else { $resolvedBestParameterSummaryPath })
            best_parameter_source = $resolvedParameterSourceName
            best_parameter_registry_path = $registryPath
            no_eval = [bool]$NoEval
            no_export = [bool]$NoExport
            performed_retune = [bool]$performedRetune
            registry_update = $registryUpdateSummary
            notes = $noteList
            stage_results = $stageResultList
        } | ConvertTo-Json -Depth 8 | Set-Content -Path $launcherSummaryPath -Encoding UTF8

        Write-Host "[DONE] RCIM Original Reference Training Completed." -ForegroundColor Green
        Write-Host "[DONE] Launcher Summary | $launcherSummaryPath" -ForegroundColor Green
    }
    else {
        Write-Host "[DONE] RCIM Original Reference Training Preview Completed." -ForegroundColor Green
        Write-Host "[DONE] No Files Were Written Because -PrintOnly Was Used." -ForegroundColor Green
    }

    Write-Host "[DONE] Campaign Root | $($runContext.CampaignRoot)" -ForegroundColor Green
}

# Resolve The Repository Root From The Script Location.
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path
Set-Location $projectRoot
. (Join-Path $scriptDirectory "shared_rcim_original_launcher_helpers.ps1")

# Expand The Requested Branch Surface Before Executing Any Campaign Bundle.
$branchNameList = switch ($Branch) {
    "Forward" { @("forward") }
    "Backward" { @("backward") }
    default { @("forward", "backward") }
}

foreach ($branchName in $branchNameList) {
    Invoke-RcimOriginalReferenceBranchRun `
        -ProjectRoot $projectRoot `
        -CondaEnvironmentName $CondaEnvironmentName `
        -PythonExecutable $PythonExecutable `
        -DirectionName $branchName `
        -StageName $Stage `
        -Families $Families `
        -TestSize $TestSize `
        -OutputSuffix $OutputSuffix `
        -DataframePath $DataframePath `
        -BestParameterSummaryPath $BestParameterSummaryPath `
        -RetuneGridSearchVerbose $RetuneGridSearchVerbose `
        -RetuneCrossValidateVerbose $RetuneCrossValidateVerbose `
        -NoEval:$NoEval `
        -NoExport:$NoExport `
        -PrintOnly:$PrintOnly
}

exit 0
