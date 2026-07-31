param(
    [switch]$Run,
    [switch]$Remote,
    [switch]$PreflightOnly,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:PINNS_REMOTE_TRAINING_REPO_PATH) { $env:PINNS_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:PINNS_REMOTE_TRAINING_CONDA_ENV) { $env:PINNS_REMOTE_TRAINING_CONDA_ENV } else { "pinns_env" }),
    [string]$OutputSuffix = "wave52r_offline_leader_cross_surface_promotion"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$ConfigPath = "config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_offline_leader_cross_surface_promotion_matrix.yaml"
$PreparationPath = "scripts\analysis\wave_5_2r\prepare_wave52r_offline_leader_cross_surface_track2.py"
$ValidatorPath = "scripts\analysis\wave_5_2r\validate_wave52r_offline_leader_cross_surface_track2_package.py"
$MatrixRunnerPath = "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\run_reference_family_vs_feedforward_comparison.py"
$RemoteManifestPath = "output\analysis\wave_5_2r\offline_leader_cross_surface_track2\remote_source_path_list.txt"
$ValidationOutputRoot = "output\validation_checks\track2_reference_comparison"
$ValidationReportRoot = "doc\reports\analysis\validation_checks\te_curve_verification_pipeline"
$RunStamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$LogRoot = Join-Path $ProjectRoot ("output\validation_checks\track2_operator_launch_logs\{0}_{1}" -f $RunStamp, $OutputSuffix)

function Write-StatusLine {
    param([string]$Level, [string]$Message)
    Write-Host ("[{0}] [{1}] {2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Level, $Message)
}

function Assert-RelativePathExists {
    param([string]$RelativePath)
    if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot $RelativePath))) {
        throw ("Required Track 2 path is missing: {0}" -f $RelativePath)
    }
}

function Invoke-CondaPython {
    param([string]$StepName, [string[]]$PythonArgumentList)
    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $logPath = Join-Path $LogRoot ("{0}.log" -f $StepName)
    $argumentList = @("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + $PythonArgumentList
    Write-StatusLine "STEP" $StepName
    Push-Location $ProjectRoot
    try {
        $previousPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        try {
            & conda @argumentList 2>&1 | ForEach-Object {
                Write-Host $_
                Add-Content -LiteralPath $logPath -Value $_ -Encoding utf8
            }
            $exitCode = $LASTEXITCODE
        }
        finally { $ErrorActionPreference = $previousPreference }
        if ($exitCode -ne 0) { throw ("{0} failed; see {1}" -f $StepName, $logPath) }
    }
    finally { Pop-Location }
}

function Invoke-LocalPreflight {
    foreach ($path in @($PreparationPath, $ValidatorPath, $MatrixRunnerPath)) {
        Assert-RelativePathExists $path
    }
    Invoke-CondaPython "cross_surface_package_preparation" @("-B", $PreparationPath)
    Assert-RelativePathExists $ConfigPath
    Assert-RelativePathExists $RemoteManifestPath
    Invoke-CondaPython "cross_surface_package_preflight" @("-B", $ValidatorPath, "--config-path", $ConfigPath, "--windows")
    Write-StatusLine "PASS" "24 candidates passed preflight; the three matrix surfaces have not run."
}

function Invoke-LocalMatrix {
    foreach ($surfaceScope in @("forward", "backward", "global")) {
        $surfaceSuffix = "{0}_{1}" -f $OutputSuffix, $surfaceScope
        Invoke-CondaPython ("track2_matrix_{0}" -f $surfaceScope) @(
            "-B", $MatrixRunnerPath,
            "--config-path", $ConfigPath,
            "--output-suffix", $surfaceSuffix,
            "--dataset", "polished_dataset",
            "--surface-scope", $surfaceScope,
            "--windows"
        )
    }
    Write-StatusLine "DONE" ("All three Track 2 surfaces completed. Logs: {0}" -f $LogRoot)
}

function Convert-ToScpRemotePath {
    param([string]$WindowsPath)
    $normalizedPath = $WindowsPath.Replace("\", "/")
    if ($normalizedPath -match "^[A-Za-z]:/") { return "/" + $normalizedPath }
    return $normalizedPath
}

function Invoke-RemotePowerShellScript {
    param([string]$ScriptText, [string]$ScriptLabel)
    $temporaryDirectory = Join-Path $ProjectRoot "output\validation_checks\track2_operator_launch_logs\remote_temp_scripts"
    New-Item -ItemType Directory -Force -Path $temporaryDirectory | Out-Null
    $identifier = [guid]::NewGuid().ToString("N")
    $localScriptPath = Join-Path $temporaryDirectory ("{0}_{1}.ps1" -f $ScriptLabel, $identifier)
    $remoteTemporaryDirectory = "C:\Temp\standardml_track2_remote"
    $remoteScriptPath = Join-Path $remoteTemporaryDirectory ("{0}_{1}.ps1" -f $ScriptLabel, $identifier)
    [System.IO.File]::WriteAllText($localScriptPath, ("`$ErrorActionPreference = 'Stop'`n" + $ScriptText), [System.Text.UTF8Encoding]::new($false))
    try {
        & ssh $RemoteHostAlias ('cmd /d /c if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectory)
        if ($LASTEXITCODE -ne 0) { throw "Could not create remote temporary directory." }
        & scp -q $localScriptPath ("{0}:{1}" -f $RemoteHostAlias, (Convert-ToScpRemotePath $remoteScriptPath))
        if ($LASTEXITCODE -ne 0) { throw "Could not upload remote helper." }
        & ssh $RemoteHostAlias powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $remoteScriptPath
        if ($LASTEXITCODE -ne 0) { throw "Remote helper failed." }
    }
    finally {
        & ssh $RemoteHostAlias ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteScriptPath) | Out-Null
        Remove-Item -LiteralPath $localScriptPath -Force -ErrorAction SilentlyContinue
    }
}

function Invoke-RemoteSourceSync {
    $generatedPaths = Get-Content -LiteralPath (Join-Path $ProjectRoot $RemoteManifestPath) | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    $staticPaths = @(
        "scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1",
        $PreparationPath,
        $ValidatorPath,
        "scripts\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward",
        "scripts\paper_reimplementation\rcim_ml_compensation\harmonic_wise_comparison",
        "scripts\datasets", "scripts\models", "scripts\training", "scripts\tooling",
        "config\datasets", $RemoteManifestPath,
        "doc\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.md"
    )
    $sourcePaths = @($generatedPaths + $staticPaths | Sort-Object -Unique)
    foreach ($path in $sourcePaths) { Assert-RelativePathExists $path }
    $syncRoot = Join-Path $ProjectRoot "output\validation_checks\track2_operator_launch_logs\remote_sync"
    New-Item -ItemType Directory -Force -Path $syncRoot | Out-Null
    $localArchive = Join-Path $syncRoot ("wave52r_cross_surface_track2_{0}.tar" -f $RunStamp)
    $remoteArchive = Join-Path $RemoteRepositoryPath ".temp\wave52r_cross_surface_track2_sync.tar"
    Push-Location $ProjectRoot
    try { & tar -cf $localArchive @sourcePaths; if ($LASTEXITCODE -ne 0) { throw "Source archive failed." } }
    finally { Pop-Location }
    Invoke-RemotePowerShellScript "New-Item -ItemType Directory -Force -Path '$RemoteRepositoryPath\.temp' | Out-Null" "prepare_cross_surface_sync"
    & scp -q $localArchive ("{0}:{1}" -f $RemoteHostAlias, (Convert-ToScpRemotePath $remoteArchive))
    if ($LASTEXITCODE -ne 0) { throw "Source upload failed." }
    Invoke-RemotePowerShellScript "Set-Location -LiteralPath '$RemoteRepositoryPath'; tar -xf '$remoteArchive'; if (`$LASTEXITCODE -ne 0) { throw 'Extraction failed.' }; Remove-Item -LiteralPath '$remoteArchive' -Force" "extract_cross_surface_sync"
    Remove-Item -LiteralPath $localArchive -Force
}

function Invoke-RemoteArtifactSync {
    $remoteArchive = Join-Path $RemoteRepositoryPath ".temp\wave52r_cross_surface_track2_results_$RunStamp.zip"
    $bundleScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'
`$bundleRoot = Join-Path `$env:TEMP 'wave52r_cross_surface_track2_results_$RunStamp'
if (Test-Path -LiteralPath `$bundleRoot) { Remove-Item -LiteralPath `$bundleRoot -Recurse -Force }
New-Item -ItemType Directory -Force -Path `$bundleRoot | Out-Null
`$sources = @()
foreach (`$scope in @('forward','backward','global')) {
    `$suffix = '${OutputSuffix}_' + `$scope
    `$sources += Get-ChildItem -LiteralPath '$ValidationOutputRoot' -Directory | Where-Object { `$_.Name -like ('*' + `$suffix + '*') } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    `$sources += Get-ChildItem -LiteralPath '$ValidationReportRoot' -File | Where-Object { `$_.Name -like ('*' + `$suffix + '*report.md') } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
}
if (`$sources.Count -ne 6) { throw ('Expected 6 returned artifacts, found ' + `$sources.Count) }
foreach (`$source in `$sources) {
    `$relative = [System.IO.Path]::GetRelativePath('$RemoteRepositoryPath', `$source.FullName)
    `$target = Join-Path `$bundleRoot `$relative
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent `$target) | Out-Null
    Copy-Item -LiteralPath `$source.FullName -Destination `$target -Recurse -Force
}
Compress-Archive -Path (Join-Path `$bundleRoot '*') -DestinationPath '$remoteArchive' -Force
"@
    Invoke-RemotePowerShellScript $bundleScript "bundle_cross_surface_results"
    $localArchive = Join-Path $LogRoot "remote_cross_surface_track2_results.zip"
    & scp -q ("{0}:{1}" -f $RemoteHostAlias, (Convert-ToScpRemotePath $remoteArchive)) $localArchive
    if ($LASTEXITCODE -ne 0) { throw "Result download failed." }
    Expand-Archive -LiteralPath $localArchive -DestinationPath $ProjectRoot -Force
    Remove-Item -LiteralPath $localArchive -Force
    Invoke-RemotePowerShellScript "Remove-Item -LiteralPath '$remoteArchive' -Force -ErrorAction SilentlyContinue" "cleanup_cross_surface_results"
}

Invoke-LocalPreflight

if ($Remote) {
    Invoke-RemoteSourceSync
    $remoteLauncher = Join-Path $RemoteRepositoryPath "scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1"
    $remoteFlag = if ($Run) { "-Run" } else { "-PreflightOnly" }
    Invoke-RemotePowerShellScript "& '$remoteLauncher' $remoteFlag -CondaEnvironmentName '$RemoteCondaEnvironmentName' -OutputSuffix '$OutputSuffix'" "launch_cross_surface_track2"
    if ($Run) { Invoke-RemoteArtifactSync }
    exit 0
}

if ($PreflightOnly -or (-not $Run)) {
    if (-not $PreflightOnly) { Write-StatusLine "INFO" "Preflight only. Pass -Run to execute all three matrix surfaces." }
    exit 0
}

Invoke-LocalMatrix
