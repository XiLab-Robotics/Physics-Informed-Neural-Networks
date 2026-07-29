param(
    [switch]$Run,
    [switch]$Remote,
    [switch]$PreflightOnly,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "wave52r_stage15_official_forward_verification"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_stage15_official_forward_verification_matrix.yaml"
$MatrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$ValidatorPath = "scripts\analysis\wave_5_2r\validate_stage15_official_forward_verification_package.py"
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
        throw ("Required Stage 15 path is missing: {0}" -f $RelativePath)
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
    $requiredPathList = @(
        $ConfigPath,
        $MatrixRunnerPath,
        $ValidatorPath,
        "scripts\models\complex_harmonic_coefficient_residual_network.py",
        "output\training_runs\complex_harmonic_coefficient_residuals\2026-07-28-16-17-13__stage5_h04\best_model.pt",
        "output\training_runs\complex_harmonic_coefficient_residuals\2026-07-28-16-17-13__stage5_h04\training_config.yaml",
        "output\analysis\wave_5_2r\stage4_data_only_residual_capacity_ladder\stage4_causal_setpoint_pf_a_surface.yaml",
        "models\polished_dataset\setpoints\periodic_mlp_harmonic\forward\reference_inventory.yaml",
        "models\polished_dataset\setpoints\periodic_gru_sequence\forward\reference_inventory.yaml"
    )
    foreach ($requiredPath in $requiredPathList) {
        Assert-RelativePathExists $requiredPath
    }

    Invoke-CondaPython -StepName "stage15_package_preflight" -PythonArgumentList @(
        "-B",
        $ValidatorPath,
        "--config-path",
        $ConfigPath
    )
    Write-StatusLine "PASS" "Stage 15 package preflight completed; the heavy matrix has not run."
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
            throw "Could not upload the remote Stage 15 helper script."
        }
        & ssh $RemoteHostAlias powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $remoteScriptPath
        if ($LASTEXITCODE -ne 0) {
            throw "Remote Stage 15 helper script failed."
        }
    }
    finally {
        & ssh $RemoteHostAlias ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteScriptPath) | Out-Null
        Remove-Item -LiteralPath $localScriptPath -Force -ErrorAction SilentlyContinue
    }
}

function Invoke-RemoteSourceSync {
    $sourcePathList = @(
        "scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1",
        "scripts\analysis\wave_5_2r\validate_stage15_official_forward_verification_package.py",
        "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward",
        "scripts\paper_reimplementation\rcim_ml_compensation\harmonic_wise_comparison",
        "scripts\analysis\polynomial_fourier_benchmark",
        "scripts\datasets",
        "scripts\models",
        "scripts\training",
        "scripts\tooling",
        "config\datasets",
        $ConfigPath,
        "doc\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.md",
        "doc\technical\2026-07\2026-07-29\2026-07-29-23-54-57_wave52r_stage15_official_forward_verification_and_deployment_preparation.md",
        "models\polished_dataset\setpoints\periodic_mlp_harmonic\forward",
        "models\polished_dataset\setpoints\periodic_gru_sequence\forward",
        "output\training_runs\complex_harmonic_coefficient_residuals\2026-07-28-16-17-13__stage5_h04",
        "output\analysis\wave_5_2r\stage4_data_only_residual_capacity_ladder\stage4_causal_setpoint_pf_a_surface.yaml",
        "output\analysis\polynomial_fourier_benchmark\common_split_manifest.yaml"
    )
    foreach ($sourcePath in $sourcePathList) {
        Assert-RelativePathExists $sourcePath
    }

    $syncDirectory = Join-Path $ProjectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncDirectory | Out-Null
    $localArchivePath = Join-Path $syncDirectory ("stage15_source_{0}.tar" -f $RunStamp)
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\stage15_source_sync.tar"
    $remoteArchiveScpPath = Convert-ToScpRemotePath $remoteArchivePath

    Write-StatusLine "STEP" "Packaging Stage 15 source and immutable model inputs."
    Push-Location $ProjectRoot
    try {
        & tar -cf $localArchivePath @sourcePathList
        if ($LASTEXITCODE -ne 0) {
            throw "Stage 15 source archive creation failed."
        }
    }
    finally {
        Pop-Location
    }

    $prepareScript = @"
New-Item -ItemType Directory -Force -Path '$RemoteRepositoryPath\.temp' | Out-Null
"@
    Invoke-RemotePowerShellScript $prepareScript "stage15_prepare_sync"
    & scp -q $localArchivePath "${RemoteHostAlias}:${remoteArchiveScpPath}"
    if ($LASTEXITCODE -ne 0) {
        throw "Stage 15 source archive upload failed."
    }
    $extractScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
tar -xf '$remoteArchivePath'
if (`$LASTEXITCODE -ne 0) { throw 'Stage 15 remote source extraction failed.' }
Remove-Item -LiteralPath '$remoteArchivePath' -Force
"@
    Invoke-RemotePowerShellScript $extractScript "stage15_extract_sync"
    Remove-Item -LiteralPath $localArchivePath -Force
    Write-StatusLine "PASS" "Remote Stage 15 source synchronization completed."
}

function Invoke-RemoteArtifactSync {
    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\stage15_artifacts_$RunStamp.zip"
    $remoteArchiveScpPath = Convert-ToScpRemotePath $remoteArchivePath
    $bundleScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$matrixDirectory = Get-ChildItem -LiteralPath '$ValidationOutputRoot' -Directory |
    Where-Object { `$_.Name -like '*$OutputSuffix*' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$matrixDirectory) { throw 'No Stage 15 matrix output was found.' }
`$reportFile = Get-ChildItem -LiteralPath '$ValidationReportRoot' -File |
    Where-Object { `$_.Name -like '*$OutputSuffix*report.md' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
if (`$null -eq `$reportFile) { throw 'No Stage 15 matrix report was found.' }
`$bundleRoot = Join-Path `$env:TEMP 'standardml_stage15_artifacts_$RunStamp'
if (Test-Path -LiteralPath `$bundleRoot) { Remove-Item -LiteralPath `$bundleRoot -Recurse -Force }
foreach (`$sourcePath in @(`$matrixDirectory.FullName, `$reportFile.FullName)) {
    `$relativePath = [System.IO.Path]::GetRelativePath('$RemoteRepositoryPath', `$sourcePath)
    `$targetPath = Join-Path `$bundleRoot `$relativePath
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent `$targetPath) | Out-Null
    Copy-Item -LiteralPath `$sourcePath -Destination `$targetPath -Recurse -Force
}
Compress-Archive -Path (Join-Path `$bundleRoot '*') -DestinationPath '$remoteArchivePath' -Force
"@
    Invoke-RemotePowerShellScript $bundleScript "stage15_bundle_artifacts"
    $localArchivePath = Join-Path $LogRoot "remote_stage15_artifacts.zip"
    & scp -q "${RemoteHostAlias}:${remoteArchiveScpPath}" $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw "Stage 15 artifact download failed."
    }
    Expand-Archive -LiteralPath $localArchivePath -DestinationPath $ProjectRoot -Force
    Remove-Item -LiteralPath $localArchivePath -Force
    $cleanupScript = "Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue"
    Invoke-RemotePowerShellScript $cleanupScript "stage15_cleanup_artifacts"
    Write-StatusLine "PASS" "Remote Stage 15 matrix artifacts synchronized locally."
}

function Invoke-LocalRun {
    Invoke-LocalPreflight
    Invoke-CondaPython -StepName "stage15_official_forward_matrix" -PythonArgumentList @(
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
    Write-StatusLine "DONE" ("Stage 15 official forward matrix completed. Logs: {0}" -f $LogRoot)
}

if ($Remote) {
    Invoke-RemoteSourceSync
    $remoteLauncherPath = Join-Path $RemoteRepositoryPath "scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1"
    $remoteRunFlag = if ($Run) { "-Run" } else { "-PreflightOnly" }
    $remoteLaunchScript = @"
& '$remoteLauncherPath' $remoteRunFlag -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix'
"@
    Invoke-RemotePowerShellScript $remoteLaunchScript "stage15_remote_launch"
    if ($Run) {
        Invoke-RemoteArtifactSync
    }
    exit 0
}

Invoke-LocalPreflight
if ($PreflightOnly -or (-not $Run)) {
    if (-not $PreflightOnly) {
        Write-StatusLine "INFO" "Preflight only. Pass -Run to execute the official matrix."
    }
    exit 0
}

Invoke-CondaPython -StepName "stage15_official_forward_matrix" -PythonArgumentList @(
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
Write-StatusLine "DONE" ("Stage 15 official forward matrix completed. Logs: {0}" -f $LogRoot)
