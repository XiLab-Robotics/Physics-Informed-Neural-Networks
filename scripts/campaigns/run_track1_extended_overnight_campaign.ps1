param(
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

function Invoke-CondaRunWithLoggedOutput {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix,
        [string]$LogPath
    )

    $previousErrorActionPreference = $ErrorActionPreference
    $global:ErrorActionPreference = "Continue"

    try {
        $commandOutput = & conda run -n $EnvironmentName $PythonExecutablePath `
            $RunnerScriptPath `
            --config-path $ConfigPath `
            --output-suffix $OutputSuffix 2>&1
        $nativeExitCode = $LASTEXITCODE
    }
    finally {
        $global:ErrorActionPreference = $previousErrorActionPreference
    }

    $commandOutput | Tee-Object -FilePath $LogPath | ForEach-Object {
        Write-Host $_
    }
    return $nativeExitCode
}

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\harmonic_wise\campaigns\2026-04-13_track1_extended_overnight_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md"
$campaignName = "track1_extended_overnight_campaign_2026_04_13_13_31_57"
$campaignOutputRoot = Join-Path "output\training_campaigns" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"

New-Item -ItemType Directory -Path $campaignLogRoot -Force | Out-Null

# Resolve Coordinated Run Matrix
$campaignConfigPathList = Get-ChildItem -Path $campaignConfigRoot -Filter "*.yaml" | Sort-Object Name | ForEach-Object { $_.FullName }
$campaignRunList = @()

for ($runIndex = 0; $runIndex -lt $campaignConfigPathList.Count; $runIndex++) {
    $groupLabel = switch ($runIndex + 1) {
        { $_ -le 12 } { "Block A"; break }
        { $_ -le 18 } { "Block B"; break }
        { $_ -le 26 } { "Block C"; break }
        { $_ -le 34 } { "Block D"; break }
        { $_ -le 40 } { "Block E"; break }
        default { "Block F" }
    }
    $campaignRunList += @{
        ConfigPath = $campaignConfigPathList[$runIndex]
        GroupLabel = $groupLabel
        RunnerLabel = "Harmonic-Wise"
    }
}

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Coordinated Run Count | $($campaignRunList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Logical Campaign Blocks | Block A, Block B, Block C, Block D, Block E, Block F" -ForegroundColor Cyan

for ($runIndex = 0; $runIndex -lt $campaignRunList.Count; $runIndex++) {
    $campaignRun = $campaignRunList[$runIndex]
    $configPath = $campaignRun.ConfigPath
    $groupLabel = $campaignRun.GroupLabel
    $configFileName = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
    $runLogPath = Join-Path $campaignLogRoot ($configFileName + ".log")

    Write-Host ""
    Write-Host ("=" * 96) -ForegroundColor DarkCyan
    Write-Host ("[INFO] Campaign Progress {0}/{1} | {2} | {3}" -f ($runIndex + 1), $campaignRunList.Count, $groupLabel, $configPath) -ForegroundColor Cyan
    Write-Host "[INFO] Runner Script | scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py" -ForegroundColor Cyan
    Write-Host ("[INFO] Log Path | {0}" -f $runLogPath) -ForegroundColor Cyan
    Write-Host ("=" * 96) -ForegroundColor DarkCyan

    $nativeExitCode = Invoke-CondaRunWithLoggedOutput `
        -EnvironmentName $CondaEnvironmentName `
        -PythonExecutablePath $PythonExecutable `
        -RunnerScriptPath "scripts\paper_reimplementation\rcim_ml_compensation\run_harmonic_wise_comparison_pipeline.py" `
        -ConfigPath $configPath `
        -OutputSuffix "campaign_run" `
        -LogPath $runLogPath

    if ($nativeExitCode -ne 0) {
        Write-Host "[ERROR] Track 1 extended overnight campaign run failed | $configPath" -ForegroundColor Red
        Write-Host "[ERROR] Failing log file | $runLogPath" -ForegroundColor Red
        exit $nativeExitCode
    }
}

Write-Host ""
Write-Host "[DONE] Track 1 extended overnight campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
exit 0

