param(
    [switch]$PreflightOnly,
    [switch]$Sequential,
    [ValidateSet("all", "global", "fw", "bw")]
    [string]$Surface = "all",
    [string]$PythonExecutable = "",
    [string]$CondaEnvironmentName = "pinns_env"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $ProjectRoot

$CampaignName = "dataset_input_mode_retraining__rcim_track1__polished_setpoints"
$CampaignManifestPath = "config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_setpoints/campaign.yaml"
$ValidatorPath = "scripts/campaigns/cross_wave/validate_rcim_track1_input_mode_campaign.py"
$RunnerPath = "scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"
$ConfigPathList = @(
    "config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_setpoints/queue/001_rcim_track1_global.yaml",
    "config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_setpoints/queue/002_rcim_track1_fw.yaml",
    "config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_setpoints/queue/003_rcim_track1_bw.yaml"
)
$SurfaceList = @("global", "fw", "bw")
$script:LastPythonExitCode = 0

function Resolve-CondaEnvironmentPythonExecutable {
    $condaExecutablePath = (Get-Command conda -ErrorAction Stop).Source
    $condaEnvironmentJson = & $condaExecutablePath info --envs --json
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to inspect Conda environments | exit_code=$LASTEXITCODE"
    }

    $condaEnvironmentInfo = $condaEnvironmentJson | ConvertFrom-Json
    foreach ($condaEnvironmentPath in $condaEnvironmentInfo.envs) {
        if ((Split-Path -Leaf $condaEnvironmentPath) -eq $CondaEnvironmentName) {
            $candidatePythonPath = Join-Path $condaEnvironmentPath "python.exe"
            if (Test-Path $candidatePythonPath) {
                return $candidatePythonPath
            }
        }
    }

    throw "Conda environment Python executable not found | environment=$CondaEnvironmentName"
}

function Invoke-CampaignPython {
    param([string[]]$ArgumentList)

    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        & $PythonExecutable @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        & python @ArgumentList
        $script:LastPythonExitCode = $LASTEXITCODE
        return
    }

    $resolvedPythonExecutable = Resolve-CondaEnvironmentPythonExecutable
    & $resolvedPythonExecutable @ArgumentList
    $script:LastPythonExitCode = $LASTEXITCODE
}

function Resolve-SelectedSurfaceIndexes {
    if ($Surface -eq "all") {
        return @(0..($SurfaceList.Count - 1))
    }
    $SelectedIndex = [Array]::IndexOf($SurfaceList, $Surface)
    if ($SelectedIndex -lt 0) {
        throw "Unsupported surface selector | $Surface"
    }
    return @($SelectedIndex)
}

function Resolve-PythonCommand {
    if (-not [string]::IsNullOrWhiteSpace($PythonExecutable)) {
        return @{
            Executable = $PythonExecutable
            PrefixArgumentList = @()
        }
    }

    if ($env:CONDA_DEFAULT_ENV -eq $CondaEnvironmentName) {
        return @{
            Executable = "python"
            PrefixArgumentList = @()
        }
    }

    return @{
        Executable = Resolve-CondaEnvironmentPythonExecutable
        PrefixArgumentList = @()
    }
}

function Invoke-ParallelCampaignSurfaceRuns {
    param([int[]]$SelectedIndexList)

    $pythonCommand = Resolve-PythonCommand
    $runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
    $logDirectory = Join-Path $ProjectRoot "output\training_campaigns\$($runTimestamp)_$CampaignName\launcher_logs"
    New-Item -ItemType Directory -Force -Path $logDirectory | Out-Null

    $processRecordList = @()
    foreach ($ConfigIndex in $SelectedIndexList) {
        $surfaceName = $SurfaceList[$ConfigIndex]
        $configPath = $ConfigPathList[$ConfigIndex]
        $stdoutPath = Join-Path $logDirectory "$surfaceName.stdout.log"
        $stderrPath = Join-Path $logDirectory "$surfaceName.stderr.log"
        $argumentList = @(
            $pythonCommand.PrefixArgumentList
            "-B"
            $RunnerPath
            "--config-path"
            $configPath
            "--output-suffix"
            "rcim_track1_polished_input_mode_campaign_validation"
        )

        Write-Host ("[START] RCIM track1 polished setpoints parallel surface | surface={0} | {1}" -f $surfaceName, $configPath)
        $process = Start-Process `
            -FilePath $pythonCommand.Executable `
            -ArgumentList $argumentList `
            -WorkingDirectory $ProjectRoot `
            -RedirectStandardOutput $stdoutPath `
            -RedirectStandardError $stderrPath `
            -PassThru
        $processRecordList += [PSCustomObject]@{
            Surface = $surfaceName
            Process = $process
            StdoutPath = $stdoutPath
            StderrPath = $stderrPath
        }
    }

    $failedSurfaceList = @()
    foreach ($processRecord in $processRecordList) {
        $processRecord.Process.WaitForExit()
        $processRecord.Process.Refresh()
        $exitCode = $processRecord.Process.ExitCode
        if ($null -eq $exitCode) {
            throw "Missing process exit code | surface=$($processRecord.Surface)"
        }
        Write-Host ("[DONE] surface={0} | exit_code={1} | stdout={2} | stderr={3}" -f $processRecord.Surface, $exitCode, $processRecord.StdoutPath, $processRecord.StderrPath)
        if ($exitCode -ne 0) {
            $failedSurfaceList += $processRecord.Surface
        }
    }

    if ($failedSurfaceList.Count -gt 0) {
        throw "Parallel RCIM track1 surface run failed | surfaces=$($failedSurfaceList -join ', ')"
    }
}

Write-Host "[INFO] Campaign: $CampaignName"
Write-Host "[INFO] Dataset: polished_dataset"
Write-Host "[INFO] Input mode: setpoints"
Write-Host "[INFO] Surface: $Surface"
Write-Host "[INFO] Local execution mode: $(if ($Sequential -or $Surface -ne 'all') { 'sequential' } else { 'parallel' })"

Invoke-CampaignPython -ArgumentList @(
    "-B",
    $ValidatorPath,
    "--campaign-manifest-path",
    $CampaignManifestPath
)
if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }

if ($PreflightOnly) {
    Write-Host "[DONE] Preflight completed without training."
    exit 0
}

if ((-not $Sequential) -and $Surface -eq "all") {
    Invoke-ParallelCampaignSurfaceRuns -SelectedIndexList (Resolve-SelectedSurfaceIndexes)
    Write-Host "[DONE] RCIM track1 polished setpoints campaign completed"
    exit 0
}

foreach ($ConfigIndex in (Resolve-SelectedSurfaceIndexes)) {
    $ConfigPath = $ConfigPathList[$ConfigIndex]
    Write-Host ("[STEP] RCIM track1 polished setpoints {0}/{1} | surface={2} | {3}" -f ($ConfigIndex + 1), $ConfigPathList.Count, $SurfaceList[$ConfigIndex], $ConfigPath)
    Invoke-CampaignPython -ArgumentList @(
        "-B",
        $RunnerPath,
        "--config-path",
        $ConfigPath,
        "--output-suffix",
        "rcim_track1_polished_input_mode_campaign_validation"
    )
    if ($script:LastPythonExitCode -ne 0) { exit $script:LastPythonExitCode }
}

Write-Host "[DONE] RCIM track1 polished setpoints campaign completed"
