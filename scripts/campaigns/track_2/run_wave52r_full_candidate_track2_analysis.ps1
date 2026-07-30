param(
    [switch]$Run,
    [switch]$Remote,
    [switch]$PreflightOnly,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "wave52r_full_candidate_parallel_temporal_non_temporal"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_full_candidate_parallel_temporal_non_temporal_matrix.yaml"
$PackagePreparationPath = "scripts\analysis\wave_5_2r\prepare_wave52r_full_candidate_track2_analysis.py"
$PackageValidatorPath = "scripts\analysis\wave_5_2r\validate_wave52r_full_candidate_track2_package.py"
$MatrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$RemoteSourceManifestPath = "output\analysis\wave_5_2r\full_candidate_track2_analysis\remote_source_path_list.txt"
$ValidationOutputRoot = "output\validation_checks\track2_reference_comparison"
$ValidationReportRoot = "doc\reports\analysis\validation_checks\te_curve_verification_pipeline"
$RunStamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$LogRoot = Join-Path $ProjectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_{1}" -f $RunStamp, $OutputSuffix)

function Write-StatusLine {
    param(
        [string]$Level,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host ("[{0}] [{1}] {2}" -f $timestamp, $Level, $Message)
}

function Assert-RelativePathExists {
    param([string]$RelativePath)

    if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot $RelativePath))) {
        throw ("Required full-candidate Track 2 path is missing: {0}" -f $RelativePath)
    }
}

function Invoke-CondaPython {
    param(
        [string]$StepName,
        [string[]]$PythonArgumentList
    )

    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $logPath = Join-Path $LogRoot ("{0}.log" -f $StepName)
    $argumentList = @(
        "run",
        "--no-capture-output",
        "-n",
        $CondaEnvironmentName,
        "python"
    ) + $PythonArgumentList
    Write-StatusLine "STEP" ("Running {0}" -f $StepName)
    Write-StatusLine "CMD" ("conda {0}" -f ($argumentList -join " "))

    Push-Location $ProjectRoot
    try {
        $previousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        try {
            & conda @argumentList 2>&1 | ForEach-Object {
                $outputLine = $_.ToString()
                Write-Host $outputLine
                Add-Content -LiteralPath $logPath -Value $outputLine -Encoding utf8
            }
            $condaExitCode = $LASTEXITCODE
        }
        finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }
        if ($condaExitCode -ne 0) {
            throw (
                "{0} failed with exit code {1}. See {2}" -f
                $StepName,
                $condaExitCode,
                $logPath
            )
        }
    }
    finally {
        Pop-Location
    }
}

function Invoke-LocalPreflight {
    foreach ($requiredPath in @(
        $PackagePreparationPath,
        $PackageValidatorPath,
        $MatrixRunnerPath,
        "doc\technical\2026-07\2026-07-30\2026-07-30-10-12-13_wave52r_full_candidate_track2_parallel_temporal_non_temporal_analysis.md",
        "models\polished_dataset\setpoints\periodic_mlp_harmonic\forward\reference_inventory.yaml",
        "models\polished_dataset\setpoints\periodic_gru_sequence\forward\reference_inventory.yaml"
    )) {
        Assert-RelativePathExists $requiredPath
    }

    Invoke-CondaPython -StepName "full_candidate_package_preparation" -PythonArgumentList @(
        "-B",
        $PackagePreparationPath
    )
    Assert-RelativePathExists $ConfigPath
    Assert-RelativePathExists $RemoteSourceManifestPath
    Invoke-CondaPython -StepName "full_candidate_package_preflight" -PythonArgumentList @(
        "-B",
        $PackageValidatorPath,
        "--config-path",
        $ConfigPath
    )
    Write-StatusLine "PASS" "The 98-candidate package passed preflight; the heavy matrix has not run."
}

function Convert-ToScpRemotePath {
    param([string]$WindowsPath)

    $normalizedPath = $WindowsPath.Replace("\", "/")
    if ($normalizedPath -match "^[A-Za-z]:/") {
        return "/" + $normalizedPath
    }
    return $normalizedPath
}

function Invoke-RemotePowerShellScript {
    param(
        [string]$ScriptText,
        [string]$ScriptLabel
    )

    $temporaryDirectory = Join-Path $ProjectRoot "output\validation_checks\track2_operator_launch_logs\remote_temp_scripts"
    New-Item -ItemType Directory -Force -Path $temporaryDirectory | Out-Null
    $identifier = [guid]::NewGuid().ToString("N")
    $localScriptPath = Join-Path $temporaryDirectory ("{0}_{1}.ps1" -f $ScriptLabel, $identifier)
    $remoteTemporaryDirectory = "C:\Temp\standardml_track2_remote"
    $remoteScriptPath = Join-Path $remoteTemporaryDirectory ("{0}_{1}.ps1" -f $ScriptLabel, $identifier)
    $remoteScriptScpPath = Convert-ToScpRemotePath $remoteScriptPath
    $utf8Encoding = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllText(
        $localScriptPath,
        ("`$ErrorActionPreference = 'Stop'`n" + $ScriptText),
        $utf8Encoding
    )

    try {
        & ssh $RemoteHostAlias ('cmd /d /c if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectory)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not create the remote temporary directory."
        }
        & scp -q $localScriptPath "${RemoteHostAlias}:${remoteScriptScpPath}"
        if ($LASTEXITCODE -ne 0) {
            throw "Could not upload the remote Track 2 helper script."
        }
        & ssh $RemoteHostAlias powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $remoteScriptPath
        if ($LASTEXITCODE -ne 0) {
            throw "Remote Track 2 helper script failed."
        }
    }
    finally {
        & ssh $RemoteHostAlias ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteScriptPath) | Out-Null
        Remove-Item -LiteralPath $localScriptPath -Force -ErrorAction SilentlyContinue
    }
}

function Resolve-RemoteSourcePathList {
    Assert-RelativePathExists $RemoteSourceManifestPath
    $manifestPath = Join-Path $ProjectRoot $RemoteSourceManifestPath
    $generatedSourcePathList = @(
        Get-Content -LiteralPath $manifestPath |
            ForEach-Object { $_.Trim() } |
            Where-Object { $_ }
    )
    $staticSourcePathList = @(
        "scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1",
        $PackagePreparationPath,
        $PackageValidatorPath,
        "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward",
        "scripts\paper_reimplementation\rcim_ml_compensation\harmonic_wise_comparison",
        "scripts\analysis\polynomial_fourier_benchmark",
        "scripts\datasets",
        "scripts\models",
        "scripts\training",
        "scripts\tooling",
        "config\datasets",
        "doc\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.md",
        "doc\technical\2026-07\2026-07-30\2026-07-30-10-12-13_wave52r_full_candidate_track2_parallel_temporal_non_temporal_analysis.md",
        $RemoteSourceManifestPath
    )
    $sourcePathList = @(
        $generatedSourcePathList + $staticSourcePathList |
            Sort-Object -Unique
    )
    foreach ($sourcePath in $sourcePathList) {
        Assert-RelativePathExists $sourcePath
    }
    return $sourcePathList
}

function Invoke-RemoteSourceSync {
    $sourcePathList = Resolve-RemoteSourcePathList
    $syncDirectory = Join-Path $ProjectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncDirectory | Out-Null
    $localArchivePath = Join-Path $syncDirectory ("wave52r_full_candidate_source_{0}.tar" -f $RunStamp)
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\wave52r_full_candidate_source_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath $remoteArchivePath

    Write-StatusLine "STEP" ("Packaging {0} source and immutable artifact paths." -f $sourcePathList.Count)
    Push-Location $ProjectRoot
    try {
        & tar -cf $localArchivePath @sourcePathList
        if ($LASTEXITCODE -ne 0) {
            throw "Full-candidate Track 2 source archive creation failed."
        }
    }
    finally {
        Pop-Location
    }

    $prepareScript = @"
New-Item -ItemType Directory -Force -Path '$RemoteRepositoryPath\.temp' | Out-Null
"@
    Invoke-RemotePowerShellScript $prepareScript "wave52r_full_candidate_prepare_sync"
    & scp -q $localArchivePath "${RemoteHostAlias}:${remoteArchiveScpPath}"
    if ($LASTEXITCODE -ne 0) {
        throw "Full-candidate Track 2 source archive upload failed."
    }
    $extractScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
tar -xf '$remoteArchivePath'
if (`$LASTEXITCODE -ne 0) { throw 'Remote source extraction failed.' }
Remove-Item -LiteralPath '$remoteArchivePath' -Force
"@
    Invoke-RemotePowerShellScript $extractScript "wave52r_full_candidate_extract_sync"
    Remove-Item -LiteralPath $localArchivePath -Force
    Write-StatusLine "PASS" "Remote full-candidate Track 2 source synchronization completed."
}

function Invoke-RemoteArtifactSync {
    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\wave52r_full_candidate_artifacts_$RunStamp.zip"
    $remoteArchiveScpPath = Convert-ToScpRemotePath $remoteArchivePath
    $bundleScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$matrixDirectory = Get-ChildItem -LiteralPath '$ValidationOutputRoot' -Directory |
    Where-Object { `$_.Name -like '*$OutputSuffix*' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$matrixDirectory) { throw 'No full-candidate matrix output was found.' }
`$reportFile = Get-ChildItem -LiteralPath '$ValidationReportRoot' -File |
    Where-Object { `$_.Name -like '*$OutputSuffix*report.md' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$reportFile) { throw 'No full-candidate matrix report was found.' }
`$bundleRoot = Join-Path `$env:TEMP 'standardml_wave52r_full_candidate_artifacts_$RunStamp'
if (Test-Path -LiteralPath `$bundleRoot) { Remove-Item -LiteralPath `$bundleRoot -Recurse -Force }
foreach (`$sourcePath in @(`$matrixDirectory.FullName, `$reportFile.FullName)) {
    `$relativePath = [System.IO.Path]::GetRelativePath('$RemoteRepositoryPath', `$sourcePath)
    `$targetPath = Join-Path `$bundleRoot `$relativePath
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent `$targetPath) | Out-Null
    Copy-Item -LiteralPath `$sourcePath -Destination `$targetPath -Recurse -Force
}
Compress-Archive -Path (Join-Path `$bundleRoot '*') -DestinationPath '$remoteArchivePath' -Force
"@
    Invoke-RemotePowerShellScript $bundleScript "wave52r_full_candidate_bundle_artifacts"
    $localArchivePath = Join-Path $LogRoot "remote_wave52r_full_candidate_artifacts.zip"
    & scp -q "${RemoteHostAlias}:${remoteArchiveScpPath}" $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw "Full-candidate Track 2 artifact download failed."
    }
    Expand-Archive -LiteralPath $localArchivePath -DestinationPath $ProjectRoot -Force
    Remove-Item -LiteralPath $localArchivePath -Force
    $cleanupScript = "Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue"
    Invoke-RemotePowerShellScript $cleanupScript "wave52r_full_candidate_cleanup_artifacts"
    Write-StatusLine "PASS" "Remote full-candidate Track 2 artifacts synchronized locally."
}

function Invoke-LocalMatrix {
    Invoke-CondaPython -StepName "wave52r_full_candidate_track2_matrix" -PythonArgumentList @(
        "-B",
        $MatrixRunnerPath,
        "--config-path",
        $ConfigPath,
        "--output-suffix",
        $OutputSuffix,
        "--dataset",
        "polished_dataset",
        "--surface-scope",
        "forward",
        "--windows"
    )
    Write-StatusLine "DONE" ("Full-candidate Track 2 matrix completed. Logs: {0}" -f $LogRoot)
}

Invoke-LocalPreflight

if ($Remote) {
    Invoke-RemoteSourceSync
    $remoteLauncherPath = Join-Path $RemoteRepositoryPath "scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1"
    $remoteRunFlag = if ($Run) { "-Run" } else { "-PreflightOnly" }
    $remoteLaunchScript = @"
& '$remoteLauncherPath' $remoteRunFlag -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix'
"@
    Invoke-RemotePowerShellScript $remoteLaunchScript "wave52r_full_candidate_remote_launch"
    if ($Run) {
        Invoke-RemoteArtifactSync
    }
    exit 0
}

if ($PreflightOnly -or (-not $Run)) {
    if (-not $PreflightOnly) {
        Write-StatusLine "INFO" "Preflight only. Pass -Run to execute the 98-candidate matrix."
    }
    exit 0
}

Invoke-LocalMatrix
