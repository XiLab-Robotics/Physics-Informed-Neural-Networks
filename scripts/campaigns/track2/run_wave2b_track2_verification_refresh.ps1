param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "wave2b_harmonic_temporal_hybrid_track2_refresh_2026_05_26",
    [string]$ReportDate = "2026-05-26",
    [string[]]$SourceSyncPathList = @(
        "scripts",
        "config",
        "doc\scripts\campaigns\track2",
        "output\registries\families\periodic_temporal_convolution",
        "output\registries\families\periodic_temporal_convolution_fw",
        "output\registries\families\periodic_temporal_convolution_bw",
        "output\registries\families\periodic_gru_sequence",
        "output\registries\families\periodic_gru_sequence_fw",
        "output\registries\families\periodic_gru_sequence_bw",
        "output\registries\families\periodic_lstm_sequence",
        "output\registries\families\periodic_lstm_sequence_fw",
        "output\registries\families\periodic_lstm_sequence_bw",
        "output\training_runs\periodic_temporal_convolution",
        "output\training_runs\periodic_temporal_convolution_fw",
        "output\training_runs\periodic_temporal_convolution_bw",
        "output\training_runs\periodic_gru_sequence",
        "output\training_runs\periodic_gru_sequence_fw",
        "output\training_runs\periodic_gru_sequence_bw",
        "output\training_runs\periodic_lstm_sequence",
        "output\training_runs\periodic_lstm_sequence_fw",
        "output\training_runs\periodic_lstm_sequence_bw"
    ),
    [string[]]$ArtifactSyncPathList = @(
        "output\validation_checks\track2_reference_comparison",
        "output\validation_checks\track2_best_model_collage_report",
        "output\validation_checks\track2_multi_model_curve_comparison_report",
        "output\validation_checks\track2_operator_launch_logs",
        "doc\reports\analysis\track2",
        "doc\reports\campaign_results\track 2"
    ),
    [switch]$SkipVisualReports,
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
$pdfPipelinePath = "scripts\reports\pdf\run_report_pipeline.py"
$collageReportPath = "doc\reports\analysis\track2\best_model_collage_report\[$ReportDate]\track2_best_model_collage_report.md"
$overlayReportPath = "doc\reports\analysis\track2\multi_model_curve_comparison_report\[$ReportDate]\track2_multi_model_curve_comparison_report.md"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_{1}" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"), $OutputSuffix)

function Write-StatusLine {
    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
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
    $fullArgumentList = @(
        "run",
        "--no-capture-output",
        "-n",
        $CondaEnvironmentName,
        "python"
    ) + $ArgumentList
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
    $localTemporaryScriptPath = Join-Path $temporaryRoot ("track2_remote_{0}.ps1" -f $scriptIdentifier)
    $remoteTemporaryDirectoryPath = "C:\Temp\standardml_track2_remote"
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("track2_remote_{0}.ps1" -f $scriptIdentifier)
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
    param(
        [string[]]$RelativePathList
    )

    $syncRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchivePath = Join-Path $syncRoot ("track2_source_sync_{0}.tar" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\track2_source_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    $existingRelativePathList = @()
    foreach ($relativePath in $RelativePathList) {
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
    if (Test-Path -LiteralPath $localArchivePath) {
        Remove-Item -LiteralPath $localArchivePath -Force
    }

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

function Invoke-RemoteArtifactSync {
    param(
        [string[]]$RelativePathList
    )

    $syncRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchivePath = Join-Path $syncRoot ("track2_artifact_sync_{0}.tar" -f (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"))
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\track2_artifact_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath
    $remotePathBlock = ($RelativePathList | ForEach-Object { "    '$($_.Replace('\', '\\'))'" }) -join ",`n"

    Write-StatusLine "STEP" "Preparing remote artifact sync archive"
    Invoke-RemotePowerShellText -RemoteScriptText @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$pathList = @(
$remotePathBlock
)
`$existingPathList = @()
foreach (`$relativePath in `$pathList) {
    if (Test-Path -LiteralPath `$relativePath) {
        `$existingPathList += `$relativePath
    }
    else {
        Write-Host ("REMOTE_ARTIFACT_SYNC_SKIP::{0}" -f `$relativePath)
    }
}
if (`$existingPathList.Count -eq 0) {
    throw 'No remote Track 2 artifacts found to synchronize.'
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

    Write-StatusLine "INFO" ("Launching Track 2 refresh remotely | host={0} | repo={1}" -f $RemoteHostAlias, $RemoteRepositoryPath)
    Invoke-RemoteSourceSync -RelativePathList $SourceSyncPathList

    $remoteScriptPath = "scripts\campaigns\track2\run_wave2b_track2_verification_refresh.ps1"
    $remoteCommand = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& '.\$remoteScriptPath' -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix' -ReportDate '$ReportDate'$(if ($SkipVisualReports) { " -SkipVisualReports" } else { "" })$(if ($SkipPdfExport) { " -SkipPdfExport" } else { "" })
exit `$LASTEXITCODE
"@

    Invoke-RemotePowerShellText -RemoteScriptText $remoteCommand
    Invoke-RemoteArtifactSync -RelativePathList $ArtifactSyncPathList
    Write-StatusLine "DONE" "Remote Track 2 refresh completed and artifacts synchronized locally"
    exit 0
}

Write-StatusLine "INFO" "Preparing local Wave 2B Track 2 verification refresh"
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

    if (-not $SkipPdfExport) {
        Invoke-LoggedCondaPython `
            -StepName "04_track2_visual_report_pdf_export" `
            -ArgumentList @(
                "-B",
                $pdfPipelinePath,
                "--input-markdown-path",
                $collageReportPath,
                "--input-markdown-path",
                $overlayReportPath,
                "--clean-temp",
                "--windows"
            )
    }
}

Write-StatusLine "DONE" ("Track 2 operator-launched refresh completed | log_root={0}" -f $logRoot)
Write-StatusLine "DONE" "Tell Codex the run completed so the official decision report and closeout synchronization can be inspected."
