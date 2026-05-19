param(
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$PythonExecutable = "python",
    [string[]]$GpuIdList = @("0"),
    [switch]$SkipGridPhase
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

function Get-EnvironmentPythonPath {
    param(
        [string]$RequestedCondaEnvironmentName
    )

    if ([string]::IsNullOrWhiteSpace($RequestedCondaEnvironmentName)) {
        return $null
    }

    $condaExecutablePath = (where.exe conda.exe 2>$null | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($condaExecutablePath)) {
        return $null
    }

    try {
        $environmentListJson = (& $condaExecutablePath env list --json 2>$null | Out-String)
        if (-not [string]::IsNullOrWhiteSpace($environmentListJson)) {
            $environmentList = $environmentListJson | ConvertFrom-Json
            foreach ($environmentPath in $environmentList.envs) {
                if ((Split-Path -Leaf $environmentPath) -eq $RequestedCondaEnvironmentName) {
                    $candidatePythonPath = Join-Path $environmentPath "python.exe"
                    if (Test-Path $candidatePythonPath) {
                        return (Resolve-Path $candidatePythonPath).Path
                    }
                }
            }
        }
    }
    catch {
        # Fall back to the standard Conda base layout.
    }

    $condaBasePath = (& $condaExecutablePath info --base 2>$null | Select-Object -Last 1)
    if (-not [string]::IsNullOrWhiteSpace($condaBasePath)) {
        $environmentPythonPath = Join-Path $condaBasePath.Trim() ("envs\" + $RequestedCondaEnvironmentName + "\python.exe")
        if (Test-Path $environmentPythonPath) {
            return (Resolve-Path $environmentPythonPath).Path
        }
    }

    return $null
}

function Resolve-PythonExecutablePath {
    param(
        [string]$RequestedPythonExecutable,
        [string]$RequestedCondaEnvironmentName
    )

    if (-not [string]::IsNullOrWhiteSpace($env:CONDA_PREFIX)) {
        $activeEnvironmentPythonPath = Join-Path $env:CONDA_PREFIX "python.exe"
        if (
            (Test-Path $activeEnvironmentPythonPath) -and
            ((Split-Path -Leaf $env:CONDA_PREFIX) -eq $RequestedCondaEnvironmentName) -and
            [string]::Equals($RequestedPythonExecutable, "python", [System.StringComparison]::OrdinalIgnoreCase)
        ) {
            return (Resolve-Path $activeEnvironmentPythonPath).Path
        }
    }

    $environmentPythonPath = Get-EnvironmentPythonPath -RequestedCondaEnvironmentName $RequestedCondaEnvironmentName
    if (
        -not [string]::IsNullOrWhiteSpace($environmentPythonPath) -and
        [string]::Equals($RequestedPythonExecutable, "python", [System.StringComparison]::OrdinalIgnoreCase)
    ) {
        return $environmentPythonPath
    }

    if (Test-Path $RequestedPythonExecutable) {
        return (Resolve-Path $RequestedPythonExecutable).Path
    }

    $resolvedCommand = Get-Command $RequestedPythonExecutable -ErrorAction SilentlyContinue
    if ($null -ne $resolvedCommand) {
        return $resolvedCommand.Source
    }

    throw "Unable to resolve Python executable | requested=$RequestedPythonExecutable"
}

function Test-OptunaAvailability {
    param(
        [string]$ResolvedPythonExecutablePath
    )

    & $ResolvedPythonExecutablePath -c "import optuna, sys; print(sys.executable)"
    if ($LASTEXITCODE -ne 0) {
        throw "Optuna import preflight failed for Python executable | $ResolvedPythonExecutablePath"
    }
}

function Format-ProcessArgumentToken {
    param(
        [string]$ArgumentToken
    )

    if ($null -eq $ArgumentToken) {
        return '""'
    }

    $normalizedArgumentToken = [string]$ArgumentToken
    if ($normalizedArgumentToken -notmatch '[\s"]') {
        return $normalizedArgumentToken
    }

    $escapedArgumentToken = $normalizedArgumentToken.Replace('"', '\"')
    return ('"{0}"' -f $escapedArgumentToken)
}

function Invoke-InteractiveOptunaStudy {
    param(
        [string]$ResolvedPythonExecutablePath,
        [string]$StudyConfigPath,
        [string]$GpuId,
        [string]$ProjectRoot,
        [string]$LauncherLogRoot
    )

    $studyStem = [System.IO.Path]::GetFileNameWithoutExtension($StudyConfigPath)
    $stdoutPath = Join-Path $LauncherLogRoot "$studyStem.stdout.log"
    $stderrPath = Join-Path $LauncherLogRoot "$studyStem.stderr.log"
    $transcriptPath = Join-Path $LauncherLogRoot "$studyStem.console.log"
    $previousCudaVisibleDevices = $env:CUDA_VISIBLE_DEVICES

    New-Item -ItemType File -Path $stdoutPath -Force | Out-Null
    New-Item -ItemType File -Path $stderrPath -Force | Out-Null
    Remove-Item $transcriptPath -Force -ErrorAction SilentlyContinue

    Write-Host (
        "[INFO] Interactive Optuna study | gpu={0} | config={1}" -f `
        $GpuId, `
        $StudyConfigPath
    ) -ForegroundColor Cyan

    try {
        $env:CUDA_VISIBLE_DEVICES = [string]$GpuId
        Start-Transcript -Path $transcriptPath -Force | Out-Null

        & $ResolvedPythonExecutablePath `
            "scripts\training\run_optuna_neural_hpo_study.py" `
            "--study-config-path" $StudyConfigPath `
            "--gpu-id" $GpuId

        $exitCode = $LASTEXITCODE
        if ($exitCode -ne 0) {
            Add-Content -Path $stderrPath -Value (
                "Optuna study failed | gpu={0} | config={1} | exit_code={2}" -f `
                $GpuId, `
                $StudyConfigPath, `
                $exitCode
            )
            throw (
                "Optuna study failed | gpu={0} | config={1} | stdout={2} | stderr={3} | exit_code={4}" -f `
                $GpuId, `
                $StudyConfigPath, `
                $transcriptPath, `
                $stderrPath, `
                $exitCode
            )
        }
    }
    finally {
        try {
            Stop-Transcript | Out-Null
        }
        catch {
            # Ignore transcript shutdown noise when no transcript is active.
        }

        if (Test-Path $transcriptPath) {
            Copy-Item -Path $transcriptPath -Destination $stdoutPath -Force
        }

        if ($null -eq $previousCudaVisibleDevices) {
            Remove-Item Env:CUDA_VISIBLE_DEVICES -ErrorAction SilentlyContinue
        }
        else {
            $env:CUDA_VISIBLE_DEVICES = $previousCudaVisibleDevices
        }
    }
}

Set-Location $projectRoot

$campaignRoot = "config\training\wave1_directional_best_hyperparameter_search\campaigns\2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
$gridQueueRoot = Join-Path $campaignRoot "grid_queue"
$optunaStudyRoot = Join-Path $campaignRoot "optuna_studies"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md"
$campaignName = "wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11"
$campaignOutputRoot = "output\training_campaigns\wave1\directional_best_hyperparameter_search\$campaignName"
$launcherLogRoot = Join-Path $campaignOutputRoot "launcher_logs"
$resolvedPythonExecutablePath = Resolve-PythonExecutablePath `
    -RequestedPythonExecutable $PythonExecutable `
    -RequestedCondaEnvironmentName $CondaEnvironmentName

New-Item -ItemType Directory -Path $launcherLogRoot -Force | Out-Null
Write-Host "[INFO] Resolved Python executable | $resolvedPythonExecutablePath" -ForegroundColor Cyan

$gridQueueConfigPathList = Get-ChildItem -Path $gridQueueRoot -Filter *.yaml -File | Sort-Object Name | ForEach-Object { $_.FullName }
$optunaStudyConfigPathList = Get-ChildItem -Path $optunaStudyRoot -Filter *.yaml -File | Sort-Object Name | ForEach-Object { $_.FullName }

if ((-not $SkipGridPhase) -and $gridQueueConfigPathList.Count -gt 0) {
    Write-Host "[INFO] Running bounded CPU grid phase | $($gridQueueConfigPathList.Count) configs" -ForegroundColor Cyan
    $gridArgumentList = @("scripts\training\run_training_campaign.py") + $gridQueueConfigPathList + @(
        "--campaign-name", $campaignName,
        "--planning-report-path", $planningReportPath
    )
    & $resolvedPythonExecutablePath @gridArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "Bounded grid phase failed | exit_code=$LASTEXITCODE"
    }
}
elseif ($SkipGridPhase) {
    Write-Host "[INFO] Grid phase skipped on request" -ForegroundColor Yellow
}

if ($optunaStudyConfigPathList.Count -eq 0) {
    Write-Host "[INFO] No Optuna study configs found | neural HPO phase skipped" -ForegroundColor Yellow
    exit 0
}

if ($GpuIdList.Count -le 0) {
    throw "GpuIdList must contain at least one GPU id."
}

Test-OptunaAvailability -ResolvedPythonExecutablePath $resolvedPythonExecutablePath

if ($GpuIdList.Count -eq 1) {
    Write-Host (
        "[INFO] Interactive terminal streaming enabled | gpu={0} | native Lightning progress visible | CTRL+C supported" -f `
        $GpuIdList[0]
    ) -ForegroundColor Cyan

    foreach ($studyConfigPath in $optunaStudyConfigPathList) {
        Invoke-InteractiveOptunaStudy `
            -ResolvedPythonExecutablePath $resolvedPythonExecutablePath `
            -StudyConfigPath $studyConfigPath `
            -GpuId $GpuIdList[0] `
            -ProjectRoot $projectRoot `
            -LauncherLogRoot $launcherLogRoot
    }

    Write-Host "[DONE] Wave 1 directional best-hyperparameter search launcher completed" -ForegroundColor Green
    exit 0
}

Write-Host (
    "[WARNING] Multiple GPU ids requested. Falling back to detached parallel launcher mode; native terminal progress bars and CTRL+C propagation are only guaranteed in single-GPU interactive mode."
) -ForegroundColor Yellow

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
        $argumentLine = ($argumentList | ForEach-Object {
            Format-ProcessArgumentToken -ArgumentToken ([string]$_)
        }) -join " "

        $process = Start-Process `
            -FilePath $resolvedPythonExecutablePath `
            -ArgumentList $argumentLine `
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
        $processRecord.Process.Refresh()
        $exitCode = $processRecord.Process.ExitCode
        if ($exitCode -ne 0) {
            throw ("Optuna study failed | gpu={0} | config={1} | stdout={2} | stderr={3} | exit_code={4}" -f `
                $processRecord.GpuId, `
                $processRecord.StudyConfigPath, `
                $processRecord.StdoutPath, `
                $processRecord.StderrPath, `
                $exitCode)
        }
    }
}

Write-Host "[DONE] Wave 1 directional best-hyperparameter search launcher completed" -ForegroundColor Green
