param(
    [switch]$Run,
    [switch]$Remote,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$ReportDate = (Get-Date -Format "yyyy-MM-dd"),
    [string]$ExecutionId = (Get-Date -Format "yyyy-MM-dd-HH-mm-ss"),
    [string]$ResumeFromStep = ""
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path
Set-Location $projectRoot

$matrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$validationReportRoot = "doc\reports\analysis\validation_checks\te_curve_verification_pipeline"
$selectedReportRoot = "doc\reports\analysis\te_curve_verification_pipeline\04_selected_model_reports\[$ReportDate]"
$matrixOutputRoot = "output\validation_checks\track2_reference_comparison"
$logRoot = Join-Path $projectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_reduced_selected_track2_reports" -f $ExecutionId)
$artifactSyncManifestPath = Join-Path $logRoot "artifact_sync_manifest.txt"
$artifactSyncRelativePathList = [System.Collections.Generic.List[string]]::new()
$script:resumeGateOpened = [string]::IsNullOrWhiteSpace($ResumeFromStep)

$polishedSetpointsConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_polished_setpoints_matrix.yaml"
$simplifiedSetpointsConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_simplified_setpoints_matrix.yaml"
$polishedActualValuesConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_polished_actual_values_matrix.yaml"

$reportCellList = @(
    [pscustomobject]@{
        StepName = "01_matrix_polished_setpoints_forward"
        DatasetName = "polished_dataset"
        InputMode = "setpoints"
        SurfaceScope = "forward"
        ConfigPath = $polishedSetpointsConfigPath
    },
    [pscustomobject]@{
        StepName = "02_matrix_polished_setpoints_backward"
        DatasetName = "polished_dataset"
        InputMode = "setpoints"
        SurfaceScope = "backward"
        ConfigPath = $polishedSetpointsConfigPath
    },
    [pscustomobject]@{
        StepName = "03_matrix_simplified_setpoints_forward"
        DatasetName = "simplified_dataset"
        InputMode = "setpoints"
        SurfaceScope = "forward"
        ConfigPath = $simplifiedSetpointsConfigPath
    },
    [pscustomobject]@{
        StepName = "04_matrix_simplified_setpoints_backward"
        DatasetName = "simplified_dataset"
        InputMode = "setpoints"
        SurfaceScope = "backward"
        ConfigPath = $simplifiedSetpointsConfigPath
    },
    [pscustomobject]@{
        StepName = "05_matrix_polished_actual_values_forward"
        DatasetName = "polished_dataset"
        InputMode = "actual_values"
        SurfaceScope = "forward"
        ConfigPath = $polishedActualValuesConfigPath
    },
    [pscustomobject]@{
        StepName = "06_matrix_polished_actual_values_backward"
        DatasetName = "polished_dataset"
        InputMode = "actual_values"
        SurfaceScope = "backward"
        ConfigPath = $polishedActualValuesConfigPath
    }
)

$sourceSyncPathList = @(
    "scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1",
    "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward",
    $polishedSetpointsConfigPath,
    $simplifiedSetpointsConfigPath,
    $polishedActualValuesConfigPath,
    "config\datasets\transmission_error_dataset.yaml",
    "doc\running\active_training_campaign.yaml",
    "doc\scripts\campaigns\track_2\run_reduced_selected_track2_reports.md",
    "models\polished_dataset\setpoints",
    "models\simplified_dataset\setpoints",
    "models\polished_dataset\actual_values"
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
    if (
        $escapedValue.Contains(" ") -or
        $escapedValue.Contains("&") -or
        $escapedValue.Contains("[") -or
        $escapedValue.Contains("]")
    ) {
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

    $utf8NoBomEncoding = [System.Text.UTF8Encoding]::new($false)
    $logWriter = [System.IO.StreamWriter]::new($logPath, $false, $utf8NoBomEncoding)
    $process = $null
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
        $logWriter.Dispose()
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
    $allowedStatusPattern = "status:\s+(none|completed|closed)"
    if ($activeCampaignText -notmatch $allowedStatusPattern) {
        throw "Active campaign state is not clear. Inspect doc/running/active_training_campaign.yaml before launching."
    }
    if ($activeCampaignText -match "protected_file_list:\s*\r?\n\s*-\s+") {
        throw "The active campaign declares protected files. Inspect the campaign state before launching."
    }
}

function Move-LatestSelectedReport {
    param(
        [string]$DatasetName,
        [string]$InputMode,
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
    $destinationFileName = "track2_selected_models_{0}_{1}_{2}_report.md" -f $DatasetName, $InputMode, $SurfaceScope
    $destinationPath = Join-Path $destinationDirectory $destinationFileName
    Move-Item -LiteralPath $matchingReport.FullName -Destination $destinationPath -Force
    Add-ArtifactSyncRelativePath -RelativePath (Join-Path $selectedReportRoot $destinationFileName)
    Write-StatusLine "REPORT" ("Selected report written | {0}" -f (Resolve-Path -LiteralPath $destinationPath -Relative))
}

function Add-LatestMatrixArtifact {
    param(
        [string]$OutputSuffix
    )

    $absoluteOutputRoot = Join-Path $projectRoot $matrixOutputRoot
    $latestDirectory = Get-ChildItem -LiteralPath $absoluteOutputRoot -Directory |
        Where-Object { $_.Name -like "*$OutputSuffix*" } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $latestDirectory) {
        throw "Cannot find matrix artifact directory for output suffix: $OutputSuffix"
    }

    Add-ArtifactSyncRelativePath -RelativePath (Join-Path $matrixOutputRoot $latestDirectory.Name)
}

function Save-ArtifactSyncManifest {
    New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
    $relativeLogRoot = Resolve-Path -LiteralPath $logRoot -Relative
    Add-ArtifactSyncRelativePath -RelativePath $relativeLogRoot
    $artifactSyncRelativePathList |
        Sort-Object -Unique |
        Set-Content -LiteralPath $artifactSyncManifestPath -Encoding utf8
    Write-StatusLine "INFO" ("Artifact sync manifest: {0}" -f $artifactSyncManifestPath)
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
    $localTemporaryScriptPath = Join-Path $temporaryRoot ("reduced_track2_remote_{0}.ps1" -f $scriptIdentifier)
    $remoteTemporaryDirectoryPath = "C:\Temp\standardml_track2_remote"
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("reduced_track2_remote_{0}.ps1" -f $scriptIdentifier)
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
    $localArchivePath = Join-Path $syncRoot ("reduced_track2_source_sync_{0}.tar" -f $ExecutionId)
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\reduced_track2_source_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    foreach ($relativePath in $sourceSyncPathList) {
        if (-not (Test-Path -LiteralPath (Join-Path $projectRoot $relativePath))) {
            throw ("Missing required source sync path | {0}" -f $relativePath)
        }
    }

    Write-StatusLine "STEP" ("Syncing source, configuration, documentation, and model archives | count={0}" -f $sourceSyncPathList.Count)
    & tar.exe -cf $localArchivePath @sourceSyncPathList
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
if (-not (Test-Path -LiteralPath 'data\polished_dataset')) {
    throw 'Missing remote polished dataset root.'
}
if (-not (Test-Path -LiteralPath 'data\simplified_dataset')) {
    throw 'Missing remote simplified dataset root.'
}
exit `$extractExitCode
"@

    Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
}

function Invoke-RemoteArtifactManifestSync {
    $syncRoot = Join-Path $projectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchivePath = Join-Path $syncRoot ("reduced_track2_artifact_sync_{0}.tar" -f $ExecutionId)
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\reduced_track2_artifact_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    Invoke-RemotePowerShellText -RemoteScriptText @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$manifestRoot = 'output\validation_checks\track2_operator_launch_logs'
`$manifestPath = Get-ChildItem -LiteralPath `$manifestRoot -Recurse -Filter 'artifact_sync_manifest.txt' |
    Where-Object { `$_.FullName -like '*$ExecutionId*' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$manifestPath) {
    throw 'No remote reduced Track 2 artifact sync manifest found.'
}
`$existingPathList = @()
foreach (`$relativePath in Get-Content -LiteralPath `$manifestPath.FullName) {
    if ((-not [string]::IsNullOrWhiteSpace(`$relativePath)) -and (Test-Path -LiteralPath `$relativePath)) {
        `$existingPathList += `$relativePath
    }
}
if (`$existingPathList.Count -eq 0) {
    throw 'The remote artifact sync manifest did not contain existing paths.'
}
New-Item -ItemType Directory -Force -Path (Split-Path -Parent '$remoteArchivePath') | Out-Null
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

function Write-ExecutionPlan {
    Write-StatusLine "PLAN" ("Report date: {0}" -f $ReportDate)
    Write-StatusLine "PLAN" ("Execution ID: {0}" -f $ExecutionId)
    Write-StatusLine "PLAN" ("Execution mode: {0}" -f $(if ($Remote) { "remote" } else { "local" }))
    Write-StatusLine "PLAN" "Policy: non-MMT, direction-separated, multi-index curve-first review."
    Write-StatusLine "PLAN" "Paused by default: global, collage, overlay, dataset-difference, and official promotion."
    foreach ($reportCell in $reportCellList) {
        $outputSuffix = "track2_selected_{0}_{1}_{2}_{3}" -f $reportCell.DatasetName, $reportCell.InputMode, $reportCell.SurfaceScope, $ExecutionId.Replace("-", "_")
        Write-Host ("  {0}: {1} / {2} / {3} | config={4} | suffix={5}" -f $reportCell.StepName, $reportCell.DatasetName, $reportCell.InputMode, $reportCell.SurfaceScope, $reportCell.ConfigPath, $outputSuffix)
    }
}

Write-ExecutionPlan
if (-not $Run) {
    Write-StatusLine "DONE" "Dry run only. Re-run with -Run locally or -Remote -Run remotely."
    exit 0
}

Assert-LaunchGate

if ($Remote) {
    if ([string]::IsNullOrWhiteSpace($RemoteRepositoryPath)) {
        throw "RemoteRepositoryPath is required for -Remote. Set PINNS_REMOTE_TRAINING_REPO_PATH or pass -RemoteRepositoryPath."
    }

    Write-StatusLine "INFO" ("Launching reduced selected-model evaluation remotely | host={0} | repo={1}" -f $RemoteHostAlias, $RemoteRepositoryPath)
    Invoke-RemoteSourceSync

    $remoteScriptPath = "scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1"
    $resumeArgument = $(if ([string]::IsNullOrWhiteSpace($ResumeFromStep)) { "" } else { " -ResumeFromStep '$ResumeFromStep'" })
    $remoteCommand = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
& '.\$remoteScriptPath' -Run -CondaEnvironmentName '$RemoteCondaEnvironmentName' -ReportDate '$ReportDate' -ExecutionId '$ExecutionId'$resumeArgument
exit `$LASTEXITCODE
"@

    Invoke-RemotePowerShellText -RemoteScriptText $remoteCommand
    Invoke-RemoteArtifactManifestSync
    Write-StatusLine "DONE" "Remote reduced selected-model evaluation completed and artifacts synchronized locally."
    exit 0
}

foreach ($reportCell in $reportCellList) {
    if (-not (Test-ShouldRunStep -StepName $reportCell.StepName)) {
        continue
    }

    $outputSuffix = "track2_selected_{0}_{1}_{2}_{3}" -f $reportCell.DatasetName, $reportCell.InputMode, $reportCell.SurfaceScope, $ExecutionId.Replace("-", "_")
    Invoke-LoggedCondaPython `
        -StepName $reportCell.StepName `
        -ArgumentList @(
            "-B",
            $matrixRunnerPath,
            "--config-path",
            $reportCell.ConfigPath,
            "--output-suffix",
            $outputSuffix,
            "--dataset",
            $reportCell.DatasetName,
            "--surface-scope",
            $reportCell.SurfaceScope,
            "--windows"
        )
    Add-LatestMatrixArtifact -OutputSuffix $outputSuffix
    Move-LatestSelectedReport `
        -DatasetName $reportCell.DatasetName `
        -InputMode $reportCell.InputMode `
        -SurfaceScope $reportCell.SurfaceScope `
        -OutputSuffix $outputSuffix
}

if ((-not [string]::IsNullOrWhiteSpace($ResumeFromStep)) -and (-not $script:resumeGateOpened)) {
    throw ("Unknown ResumeFromStep value: {0}" -f $ResumeFromStep)
}

Save-ArtifactSyncManifest
Write-StatusLine "DONE" ("Six-cell reduced selected-model evaluation completed | reports={0} | logs={1}" -f $selectedReportRoot, $logRoot)
