param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "track2h_robust_loss_track2_refresh_2026_06_11",
    [string]$ReportDate = "2026-06-11",
    [switch]$SkipVisualReports,
    [switch]$SkipPdfExport,
    [switch]$SyncFullTrack2CampaignResultPlots
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
Set-Location $projectRoot

$track2ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\full_track2_matrix_template.yaml"
$matrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$collageRunnerPath = "scripts\reports\analysis\build_track2_best_model_collage_report.py"
$overlayRunnerPath = "scripts\reports\analysis\build_track2_multi_model_curve_comparison_report.py"
$visualCoverageValidatorPath = "scripts\reports\analysis\validate_track2_visual_source_coverage.py"
$officialReportBuilderPath = "scripts\reports\analysis\build_track2_official_model_verification_report.py"
$pdfPipelinePath = "scripts\reports\pdf\run_report_pipeline.py"
$collageReportPath = "doc\reports\analysis\track2\best_model_collage_report\[$ReportDate]\track2_best_model_collage_report.md"
$overlayReportPath = "doc\reports\analysis\track2\multi_model_curve_comparison_report\[$ReportDate]\track2_multi_model_curve_comparison_report.md"
$officialReportPath = "doc\reports\analysis\track2\official_model_verification_report\[$ReportDate]\track2_official_model_verification_report.md"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_{1}" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"), $OutputSuffix)
$matrixOutputRoot = "output\validation_checks\track2_reference_comparison"
$collageOutputRoot = "output\validation_checks\track2_best_model_collage_report"
$overlayOutputRoot = "output\validation_checks\track2_multi_model_curve_comparison_report"
$canonicalTrack2ReportPath = "doc\reports\analysis\track2\Track 2 Directional Model Comparison.md"
$collageReportDirectory = "doc\reports\analysis\track2\best_model_collage_report\[$ReportDate]"
$overlayReportDirectory = "doc\reports\analysis\track2\multi_model_curve_comparison_report\[$ReportDate]"
$officialReportDirectory = "doc\reports\analysis\track2\official_model_verification_report\[$ReportDate]"
$newCandidateCampaignResultPlotDirectory = "doc\reports\campaign_results\track 2\track2h_dispersion_aware_modeling_registry"
$artifactSyncManifestPath = Join-Path $logRoot "artifact_sync_manifest.txt"
$artifactSyncRelativePathList = [System.Collections.Generic.List[string]]::new()

$sourceSyncPathList = @(
    "scripts",
    "config",
    "doc\scripts\campaigns\track2",
    "output\registries\families\track2h_dispersion_aware_mae_robust_global",
    "output\registries\families\track2h_dispersion_aware_mae_robust_fw",
    "output\registries\families\track2h_dispersion_aware_mae_robust_bw",
    "output\registries\families\track2h_dispersion_aware_smooth_l1_robust_global",
    "output\registries\families\track2h_dispersion_aware_smooth_l1_robust_fw",
    "output\registries\families\track2h_dispersion_aware_smooth_l1_robust_bw",
    "output\registries\families\track2h_dispersion_aware_log_cosh_robust_global",
    "output\registries\families\track2h_dispersion_aware_log_cosh_robust_fw",
    "output\registries\families\track2h_dispersion_aware_log_cosh_robust_bw",
    "output\training_runs\track2h_dispersion_aware_mae_robust_global",
    "output\training_runs\track2h_dispersion_aware_mae_robust_fw",
    "output\training_runs\track2h_dispersion_aware_mae_robust_bw",
    "output\training_runs\track2h_dispersion_aware_smooth_l1_robust_global",
    "output\training_runs\track2h_dispersion_aware_smooth_l1_robust_fw",
    "output\training_runs\track2h_dispersion_aware_smooth_l1_robust_bw",
    "output\training_runs\track2h_dispersion_aware_log_cosh_robust_global",
    "output\training_runs\track2h_dispersion_aware_log_cosh_robust_fw",
    "output\training_runs\track2h_dispersion_aware_log_cosh_robust_bw",
    "output\validation_checks\track2_reference_comparison\2026-05-28-12-22-56__track2_full_directional_family_matrix_wave2c_residual_harmonic_temporal_hybrid_track2_refresh_2026_05_28\validation_summary.yaml",
    "output\validation_checks\track2_reference_comparison\2026-05-28-12-22-56__track2_full_directional_family_matrix_wave2c_residual_harmonic_temporal_hybrid_track2_refresh_2026_05_28\per_condition_metrics.csv"
)

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

function Add-ArtifactSyncRelativePath {
    param(
        [string]$RelativePath
    )

    if ([string]::IsNullOrWhiteSpace($RelativePath)) {
        return
    }

    $normalizedRelativePath = $RelativePath.Trim().TrimStart(".", "\", "/")
    if (-not (Test-Path -LiteralPath (Join-Path $projectRoot $normalizedRelativePath))) {
        return
    }

    if (-not $artifactSyncRelativePathList.Contains($normalizedRelativePath)) {
        $artifactSyncRelativePathList.Add($normalizedRelativePath) | Out-Null
    }
}

function Add-LatestArtifactDirectory {
    param(
        [string]$RelativeRootPath,
        [string]$NamePattern
    )

    $absoluteRootPath = Join-Path $projectRoot $RelativeRootPath
    if (-not (Test-Path -LiteralPath $absoluteRootPath)) {
        return
    }

    $latestDirectory = Get-ChildItem -LiteralPath $absoluteRootPath -Directory |
        Where-Object { $_.Name -like $NamePattern } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $latestDirectory) {
        return
    }

    Add-ArtifactSyncRelativePath -RelativePath (Join-Path $RelativeRootPath $latestDirectory.Name)
}

function Get-LatestArtifactDirectory {
    param(
        [string]$RelativeRootPath,
        [string]$NamePattern
    )

    $absoluteRootPath = Join-Path $projectRoot $RelativeRootPath
    if (-not (Test-Path -LiteralPath $absoluteRootPath)) {
        throw ("Missing artifact root | {0}" -f $RelativeRootPath)
    }

    $latestDirectory = Get-ChildItem -LiteralPath $absoluteRootPath -Directory |
        Where-Object { $_.Name -like $NamePattern } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $latestDirectory) {
        throw ("Missing generated artifact directory | root={0} | pattern={1}" -f $RelativeRootPath, $NamePattern)
    }

    return $latestDirectory.FullName
}

function Save-ArtifactSyncManifest {
    New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
    Add-ArtifactSyncRelativePath -RelativePath $canonicalTrack2ReportPath
    Add-ArtifactSyncRelativePath -RelativePath $collageReportDirectory
    Add-ArtifactSyncRelativePath -RelativePath $overlayReportDirectory
    Add-ArtifactSyncRelativePath -RelativePath $officialReportDirectory
    if ($SyncFullTrack2CampaignResultPlots) {
        Add-ArtifactSyncRelativePath -RelativePath "doc\reports\campaign_results\track 2"
    }
    else {
        Add-ArtifactSyncRelativePath -RelativePath $newCandidateCampaignResultPlotDirectory
    }
    Add-ArtifactSyncRelativePath -RelativePath (Resolve-Path -LiteralPath $logRoot | ForEach-Object { Resolve-Path -LiteralPath $_ -Relative })

    $artifactSyncRelativePathList |
        Sort-Object -Unique |
        Set-Content -LiteralPath $artifactSyncManifestPath -Encoding utf8
    Write-StatusLine "INFO" ("Artifact sync manifest: {0}" -f $artifactSyncManifestPath)
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
    $processStartInfo.RedirectStandardOutput = $false
    $processStartInfo.RedirectStandardError = $false
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

    $exitCode = [int]$process.ExitCode
    if ($exitCode -ne 0) {
        throw ("Track 2 step failed | step={0} | exit_code={1} | log={2}" -f $StepName, $exitCode, $logPath)
    }
}

function Convert-ToScpRemotePath {
    param(
        [string]$WindowsPath
    )

    $normalizedPath = $WindowsPath.Replace("\", "/")
    if ($normalizedPath -match "^[A-Za-z]:/") {
        return "/" + $normalizedPath
    }

    return $normalizedPath
}

function Invoke-RemotePowerShellText {
    param(
        [string]$RemoteScriptText
    )

    $temporaryRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_temp_scripts"
    New-Item -ItemType Directory -Force -Path $temporaryRoot | Out-Null
    $scriptIdentifier = [guid]::NewGuid().ToString("N")
    $localTemporaryScriptPath = Join-Path $temporaryRoot ("track2h_remote_{0}.ps1" -f $scriptIdentifier)
    $remoteTemporaryDirectoryPath = "C:\Temp\standardml_track2_remote"
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("track2h_remote_{0}.ps1" -f $scriptIdentifier)
    $remoteTemporaryScriptScpPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryScriptPath

    $wrappedRemoteScriptText = @"
`$ErrorActionPreference = 'Stop'
try {
$RemoteScriptText
}
catch {
    Write-Error `$_.Exception.Message
    exit 1
}
"@

    $utf8Encoding = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllText($localTemporaryScriptPath, $wrappedRemoteScriptText, $utf8Encoding)

    try {
        & ssh $RemoteHostAlias ('cmd /d /c if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectoryPath)
        if ($LASTEXITCODE -ne 0) {
            throw ("Remote temporary directory prepare failed | host={0} | path={1}" -f $RemoteHostAlias, $remoteTemporaryDirectoryPath)
        }

        & scp $localTemporaryScriptPath "${RemoteHostAlias}:${remoteTemporaryScriptScpPath}"
        if ($LASTEXITCODE -ne 0) {
            throw ("Remote temporary script upload failed | host={0} | path={1}" -f $RemoteHostAlias, $remoteTemporaryScriptPath)
        }

        & ssh $RemoteHostAlias ("powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File {0}" -f $remoteTemporaryScriptPath)
        if ($LASTEXITCODE -ne 0) {
            throw ("Remote PowerShell command failed | host={0} | script={1}" -f $RemoteHostAlias, $remoteTemporaryScriptPath)
        }
    }
    finally {
        & ssh $RemoteHostAlias ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteTemporaryScriptPath) | Out-Null
        Remove-Item -LiteralPath $localTemporaryScriptPath -Force -ErrorAction SilentlyContinue
    }
}

function Invoke-RemoteSourceSync {
    $syncRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchivePath = Join-Path $syncRoot ("track2h_source_sync_{0}.tar" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\track2h_source_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath
    $existingRelativePathList = @()

    foreach ($relativePath in $sourceSyncPathList) {
        if (Test-Path -LiteralPath (Join-Path $projectRoot $relativePath)) {
            $existingRelativePathList += $relativePath
        }
        else {
            Write-StatusLine "WARN" ("Skipping missing source sync path | {0}" -f $relativePath)
        }
    }

    if ($existingRelativePathList.Count -eq 0) {
        throw "No source sync paths are available."
    }

    Write-StatusLine "STEP" ("Syncing source paths to remote | count={0}" -f $existingRelativePathList.Count)
    & tar.exe -cf $localArchivePath @existingRelativePathList
    if ($LASTEXITCODE -ne 0) {
        throw ("Local source sync archive build failed | {0}" -f $localArchivePath)
    }

    Invoke-RemotePowerShellText -RemoteScriptText @"
New-Item -ItemType Directory -Force -Path (Join-Path '$RemoteRepositoryPath' '.temp') | Out-Null
if (Test-Path -LiteralPath '$remoteArchivePath') {
    Remove-Item -LiteralPath '$remoteArchivePath' -Force
}
"@

    & scp $localArchivePath "${RemoteHostAlias}:${remoteArchiveScpPath}"
    if ($LASTEXITCODE -ne 0) {
        throw ("Remote source sync upload failed | host={0}" -f $RemoteHostAlias)
    }

    Invoke-RemotePowerShellText -RemoteScriptText @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& tar.exe -xf '$remoteArchivePath'
`$extractExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit `$extractExitCode
"@

    Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
}

function Invoke-RemoteArtifactManifestSync {
    $syncRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchivePath = Join-Path $syncRoot ("track2h_artifact_sync_{0}.tar" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\track2h_artifact_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    Invoke-RemotePowerShellText -RemoteScriptText @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$manifestRoot = 'output\validation_checks\track2_operator_launch_logs'
`$manifestPath = Get-ChildItem -LiteralPath `$manifestRoot -Recurse -Filter 'artifact_sync_manifest.txt' |
    Where-Object { `$_.FullName -like '*$OutputSuffix*' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$manifestPath) {
        throw 'No remote Track 2H artifact sync manifest found.'
}
`$existingPathList = @()
foreach (`$relativePath in Get-Content -LiteralPath `$manifestPath.FullName) {
    if ([string]::IsNullOrWhiteSpace(`$relativePath)) {
        continue
    }
    if (Test-Path -LiteralPath `$relativePath) {
        `$existingPathList += `$relativePath
    }
    else {
        Write-Host ("REMOTE_ARTIFACT_SYNC_SKIP::{0}" -f `$relativePath)
    }
}
if (`$existingPathList.Count -eq 0) {
        throw 'The remote Track 2H artifact sync manifest did not contain existing paths.'
}
New-Item -ItemType Directory -Force -Path (Split-Path -Parent '$remoteArchivePath') | Out-Null
if (Test-Path -LiteralPath '$remoteArchivePath') {
    Remove-Item -LiteralPath '$remoteArchivePath' -Force
}
& tar.exe -cf '$remoteArchivePath' @existingPathList
exit `$LASTEXITCODE
"@

    & scp "${RemoteHostAlias}:${remoteArchiveScpPath}" $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw ("Remote artifact archive download failed | host={0}" -f $RemoteHostAlias)
    }

    & tar.exe -xf $localArchivePath -C $projectRoot
    if ($LASTEXITCODE -ne 0) {
        throw ("Local artifact archive extract failed | {0}" -f $localArchivePath)
    }

    Invoke-RemotePowerShellText -RemoteScriptText @"
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit 0
"@

    Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
}

if ($Remote) {
    if ([string]::IsNullOrWhiteSpace($RemoteRepositoryPath)) {
        throw "RemoteRepositoryPath is required for -Remote. Set PINNS_REMOTE_TRAINING_REPO_PATH or pass -RemoteRepositoryPath."
    }

    Write-StatusLine "INFO" ("Launching Track 2H refresh remotely | host={0} | repo={1}" -f $RemoteHostAlias, $RemoteRepositoryPath)
    Invoke-RemoteSourceSync

    $remoteScriptPath = "scripts\campaigns\track2\run_track2h_track2_verification_refresh.ps1"
    $remoteCommand = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& '.\$remoteScriptPath' -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix' -ReportDate '$ReportDate'$(if ($SkipVisualReports) { " -SkipVisualReports" } else { "" })$(if ($SkipPdfExport) { " -SkipPdfExport" } else { "" })$(if ($SyncFullTrack2CampaignResultPlots) { " -SyncFullTrack2CampaignResultPlots" } else { "" })
exit `$LASTEXITCODE
"@

    Invoke-RemotePowerShellText -RemoteScriptText $remoteCommand
    Invoke-RemoteArtifactManifestSync
    Write-StatusLine "DONE" "Remote Track 2H refresh completed and artifacts synchronized locally"
    exit 0
}

Write-StatusLine "INFO" "Preparing local Track 2H verification refresh"
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
Add-LatestArtifactDirectory -RelativeRootPath $matrixOutputRoot -NamePattern ("*{0}" -f $OutputSuffix)

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
    Add-LatestArtifactDirectory -RelativeRootPath $collageOutputRoot -NamePattern "*__track2_best_model_collage_report"

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
    Add-LatestArtifactDirectory -RelativeRootPath $overlayOutputRoot -NamePattern "*__track2_multi_model_curve_comparison_report"

    Invoke-LoggedCondaPython `
        -StepName "04_track2_visual_source_coverage" `
        -ArgumentList @(
            "-B",
            $visualCoverageValidatorPath,
            "--config-path",
            $track2ConfigPath,
            "--collage-report-path",
            $collageReportPath,
            "--overlay-report-path",
            $overlayReportPath,
            "--windows"
        )

    $matrixArtifactDirectory = Get-LatestArtifactDirectory -RelativeRootPath $matrixOutputRoot -NamePattern ("*{0}" -f $OutputSuffix)
    $collageArtifactDirectory = Get-LatestArtifactDirectory -RelativeRootPath $collageOutputRoot -NamePattern "*__track2_best_model_collage_report"
    $overlayArtifactDirectory = Get-LatestArtifactDirectory -RelativeRootPath $overlayOutputRoot -NamePattern "*__track2_multi_model_curve_comparison_report"
    $matrixSummaryPath = Join-Path $matrixArtifactDirectory "validation_summary.yaml"
    $collageSummaryPath = Join-Path $collageArtifactDirectory "track2_best_model_collage_summary.yaml"
    $overlaySummaryPath = Join-Path $overlayArtifactDirectory "track2_multi_model_curve_comparison_summary.yaml"

    Invoke-LoggedCondaPython `
        -StepName "05_track2_official_verification_report" `
        -ArgumentList @(
            "-B",
            $officialReportBuilderPath,
            "--matrix-summary-path",
            $matrixSummaryPath,
            "--collage-summary-path",
            $collageSummaryPath,
            "--overlay-summary-path",
            $overlaySummaryPath,
            "--report-date",
            $ReportDate,
            "--refresh-label",
            "Track 2H robust-loss refresh",
            "--candidate-source-label",
            "track2h_dispersion_aware_modeling_registry",
            "--decision",
            "verified exploratory baseline; not promoted over the accepted direction-parallel leaders",
            "--next-step",
            "Use the robust-loss evidence as one dispersion-aware ingredient when comparing later probabilistic, mixture, and structured branches.",
            "--output-report-path",
            $officialReportPath,
            "--operator-log-root",
            $logRoot
        )

    if (-not $SkipPdfExport) {
        Invoke-LoggedCondaPython `
            -StepName "06_track2_visual_report_pdf_export" `
            -ArgumentList @(
                "-B",
                $pdfPipelinePath,
                "--input-markdown-path",
                $collageReportPath,
                "--input-markdown-path",
                $overlayReportPath,
                "--input-markdown-path",
                $officialReportPath,
                "--clean-temp",
                "--windows"
            )
    }
}

Save-ArtifactSyncManifest
Write-StatusLine "DONE" "Track 2H verification refresh completed"
