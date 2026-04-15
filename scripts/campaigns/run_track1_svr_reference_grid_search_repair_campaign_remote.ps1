param(
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

# Define Campaign Identity
$campaignConfigRoot = "config\paper_reimplementation\rcim_ml_compensation\exact_model_bank\campaigns\2026-04-14_track1_svr_reference_grid_search_repair_campaign"
$planningReportPath = "doc\reports\campaign_plans\2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md"
$campaignName = "track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48"
$campaignOutputRoot = Join-Path "output\training_campaigns" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"
$remoteTrackingRoot = ".temp\remote_training_campaigns"
$remoteExecutionDrive = "R:"
$remoteExecutionRoot = "R:\"
$remoteStagingRootPath = "C:\Temp\standardml_remote_training"
$sourceSyncPathList = @(
    "scripts"
    "config"
    "doc"
    "requirements.txt"
)

# Resolve Campaign Config Paths
$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_track1_svr_reference_grid_amplitude_pair.yaml")
    (Join-Path $campaignConfigRoot "02_track1_svr_reference_grid_amplitude_40_only.yaml")
    (Join-Path $campaignConfigRoot "03_track1_svr_reference_grid_amplitude_240_only.yaml")
    (Join-Path $campaignConfigRoot "04_track1_svr_reference_grid_phase_162_only.yaml")
)
$runNameList = @(
    "track1_svr_reference_grid_amplitude_pair"
    "track1_svr_reference_grid_amplitude_40_only"
    "track1_svr_reference_grid_amplitude_240_only"
    "track1_svr_reference_grid_phase_162_only"
)

function Write-StatusLine {

    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Convert-ToSlug {

    param(
        [string]$RawText
    )

    $characterBuilder = New-Object System.Text.StringBuilder

    foreach ($character in $RawText.ToCharArray()) {
        if ([char]::IsLetterOrDigit($character)) {
            [void]$characterBuilder.Append([char]::ToLowerInvariant($character))
        }
        else {
            [void]$characterBuilder.Append("_")
        }
    }

    return $characterBuilder.ToString().Trim("_")
}

function Resolve-WindowsRelativePath {

    param(
        [string]$BasePath,
        [string]$TargetPath
    )

    $normalizedBasePath = [System.IO.Path]::GetFullPath($BasePath)
    $normalizedTargetPath = [System.IO.Path]::GetFullPath($TargetPath)

    if (-not $normalizedBasePath.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $normalizedBasePath += [System.IO.Path]::DirectorySeparatorChar
    }

    $baseUri = New-Object System.Uri($normalizedBasePath)
    $targetUri = New-Object System.Uri($normalizedTargetPath)
    $relativeUri = $baseUri.MakeRelativeUri($targetUri)
    $relativePath = [System.Uri]::UnescapeDataString($relativeUri.ToString())
    return $relativePath.Replace("/", "\")
}

function Resolve-RepositoryRelativePath {

    param(
        [string]$InputPath
    )

    $resolvedPath = (Resolve-Path -LiteralPath $InputPath).Path
    $relativePath = Resolve-WindowsRelativePath -BasePath $projectRoot -TargetPath $resolvedPath
    return $relativePath.Replace("/", "\")
}

function New-RemoteMappedRepositoryScriptText {

    param(
        [string]$ScriptText
    )

    return @"
`$remoteExecutionDrive = '$remoteExecutionDrive'
try {
    & subst.exe `$remoteExecutionDrive /d | Out-Null
} catch {}
& subst.exe `$remoteExecutionDrive '$RemoteRepositoryPath' | Out-Null
if (`$LASTEXITCODE -ne 0) {
    throw 'Remote execution root mapping failed | drive=$remoteExecutionDrive | path=$RemoteRepositoryPath'
}
try {
$ScriptText
}
finally {
    & subst.exe `$remoteExecutionDrive /d | Out-Null
}
"@
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

function Write-StreamingLine {

    param(
        [string]$LineText,
        [System.IO.StreamWriter]$LogWriter,
        [System.Collections.Generic.List[string]]$CollectedLineList
    )

    if ($null -eq $LineText) {
        return
    }

    if ($null -ne $LogWriter) {
        $LogWriter.WriteLine($LineText)
        $LogWriter.Flush()
    }

    if ($null -ne $CollectedLineList) {
        $CollectedLineList.Add($LineText) | Out-Null
    }

    Write-Host $LineText
}

function Invoke-RemotePowerShellScriptWithStreamingLog {

    param(
        [string]$RemoteScriptText,
        [string]$LogPath
    )

    $sshExecutablePath = (Get-Command ssh -ErrorAction Stop).Source
    $scpExecutablePath = (Get-Command scp -ErrorAction Stop).Source
    $resolvedLogPath = Join-Path $projectRoot $LogPath
    $logDirectoryPath = Split-Path -Parent $resolvedLogPath
    $utf8Encoding = [System.Text.ASCIIEncoding]::new()
    $logWriter = $null
    $process = $null
    $localTemporaryScriptPath = Join-Path $logDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryDirectoryPath = $remoteStagingRootPath
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryScpPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryScriptPath
    $collectedLineList = [System.Collections.Generic.List[string]]::new()

    New-Item -ItemType Directory -Force -Path $logDirectoryPath | Out-Null

    try {
        $logWriter = [System.IO.StreamWriter]::new($resolvedLogPath, $true, $utf8Encoding)
        [System.IO.File]::WriteAllText($localTemporaryScriptPath, $RemoteScriptText.TrimStart([char]0xFEFF), $utf8Encoding)

        & $sshExecutablePath $RemoteHostAlias ('cmd /d /c if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectoryPath) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script directory prepare failed | host=$RemoteHostAlias | path=$remoteTemporaryDirectoryPath"
        }

        & $scpExecutablePath $localTemporaryScriptPath ('{0}:{1}' -f $RemoteHostAlias, $remoteTemporaryScpPath) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script upload failed | host=$RemoteHostAlias | path=$remoteTemporaryScriptPath"
        }

        $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $startInfo.FileName = "cmd.exe"
        $startInfo.Arguments = (
            '/d /c ""{0}" {1} powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -OutputFormat Text -File "{2}"""' -f
            $sshExecutablePath,
            $RemoteHostAlias,
            $remoteTemporaryScriptPath
        )
        $startInfo.UseShellExecute = $false
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $true
        $startInfo.CreateNoWindow = $true
        $startInfo.WorkingDirectory = $projectRoot

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $startInfo
        $null = $process.Start()

        while (-not $process.HasExited) {
            while ($process.StandardOutput.Peek() -ge 0) {
                Write-StreamingLine -LineText $process.StandardOutput.ReadLine() -LogWriter $logWriter -CollectedLineList $collectedLineList
            }

            while ($process.StandardError.Peek() -ge 0) {
                Write-StreamingLine -LineText $process.StandardError.ReadLine() -LogWriter $logWriter -CollectedLineList $collectedLineList
            }

            $null = $process.WaitForExit(200)
        }

        while (-not $process.StandardOutput.EndOfStream) {
            Write-StreamingLine -LineText $process.StandardOutput.ReadLine() -LogWriter $logWriter -CollectedLineList $collectedLineList
        }

        while (-not $process.StandardError.EndOfStream) {
            Write-StreamingLine -LineText $process.StandardError.ReadLine() -LogWriter $logWriter -CollectedLineList $collectedLineList
        }

        return @{
            exit_code = [int]$process.ExitCode
            output_line_list = @($collectedLineList)
        }
    }
    finally {
        if ($null -ne $logWriter) {
            $logWriter.Flush()
            $logWriter.Dispose()
        }

        if (($null -ne $process) -and (-not $process.HasExited)) {
            try {
                $process.Kill()
            }
            catch {
                Write-StatusLine "WARN" "Remote SSH process cleanup failed | $($_.Exception.Message)"
            }
        }

        & $sshExecutablePath $RemoteHostAlias ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteTemporaryScriptPath) | Out-Null
        if (Test-Path -LiteralPath $localTemporaryScriptPath) {
            Remove-Item -LiteralPath $localTemporaryScriptPath -Force -ErrorAction SilentlyContinue
        }
    }
}

function Invoke-RemoteTarExtract {

    param(
        [string[]]$RelativePathList,
        [string]$LogPath
    )

    $localArchivePath = Join-Path $runTrackingDirectory "source_sync_payload.tar"
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\remote_training_source_sync.tar"
    $remoteScpArchivePath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    if (Test-Path -LiteralPath $localArchivePath) {
        Remove-Item -LiteralPath $localArchivePath -Force
    }

    & tar.exe -cf $localArchivePath @RelativePathList
    if ($LASTEXITCODE -ne 0) {
        throw "Local source archive build failed | archive=$localArchivePath"
    }

    & scp $localArchivePath "${RemoteHostAlias}:${remoteScpArchivePath}"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote source archive upload failed | host=$RemoteHostAlias | archive=$remoteArchivePath"
    }

    $remoteExtractScript = @"
New-Item -ItemType Directory -Force -Path '$remoteStagingRootPath' | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path '$RemoteRepositoryPath' '.temp') | Out-Null
Set-Location -LiteralPath '$remoteExecutionRoot'
& tar.exe -xf '$remoteArchivePath'
`$extractExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit `$extractExitCode
"@

    $extractResult = Invoke-RemotePowerShellScriptWithStreamingLog `
        -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteExtractScript) `
        -LogPath $LogPath
    if ([int]$extractResult.exit_code -ne 0) {
        throw "Remote source archive extract failed | host=$RemoteHostAlias | archive=$remoteArchivePath"
    }

    Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
}

function Test-RemoteSourcePathAvailability {

    param(
        [string[]]$RelativePathList,
        [string]$LogPath
    )

    $remoteVerificationScript = @"
Set-Location -LiteralPath '$remoteExecutionRoot'
Write-Output ('REMOTE_VERIFICATION_WORKDIR::{0}' -f (Get-Location).Path)

`$pythonVerificationScriptPath = Join-Path '$RemoteRepositoryPath' '.temp\remote_source_path_verification.py'
`$pythonVerificationScriptText = @'
from pathlib import Path
import sys

project_root = Path("R:/")
relative_path_list = [
"@

    foreach ($relativePath in $RelativePathList) {
        $normalizedPath = $relativePath.Replace("\", "/")
        $remoteVerificationScript += @"
    r'$normalizedPath',
"@
    }

    $remoteVerificationScript += @"
]

print(f"REMOTE_VERIFICATION_PROJECT_ROOT::{project_root}")
missing_path_list = []
for relative_path_text in relative_path_list:
    candidate_path = project_root / relative_path_text
    if candidate_path.exists():
        print(f"REMOTE_VERIFIED_REQUIRED_PATH::{relative_path_text}")
    else:
        print(f"REMOTE_MISSING_REQUIRED_PATH::{relative_path_text}")
        missing_path_list.append(relative_path_text)

sys.exit(1 if missing_path_list else 0)
'@

Set-Content -LiteralPath `$pythonVerificationScriptPath -Value `$pythonVerificationScriptText -Encoding UTF8
& conda run -n $RemoteCondaEnvironmentName python `$pythonVerificationScriptPath
`$verificationExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath `$pythonVerificationScriptPath -Force -ErrorAction SilentlyContinue
exit `$verificationExitCode
"@

    $verificationResult = Invoke-RemotePowerShellScriptWithStreamingLog `
        -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteVerificationScript) `
        -LogPath $LogPath

    $missingPathList = @()
    foreach ($outputLine in @($verificationResult.output_line_list)) {
        if ($outputLine -match "^REMOTE_MISSING_REQUIRED_PATH::(.+)$") {
            $missingPathList += $Matches[1].Trim()
        }
    }

    return @{
        exit_code = [int]$verificationResult.exit_code
        missing_path_list = @($missingPathList)
    }
}

function Invoke-RemoteTarCopyToLocal {

    param(
        [string[]]$RelativePathList,
        [string]$LogPath
    )

    $localArchiveDirectory = Join-Path $runTrackingDirectory "artifact_sync_payloads"
    New-Item -ItemType Directory -Force -Path $localArchiveDirectory | Out-Null

    for ($pathIndex = 0; $pathIndex -lt $RelativePathList.Count; $pathIndex++) {
        $relativePath = $RelativePathList[$pathIndex]
        $archiveSlug = "{0:D3}_{1}" -f ($pathIndex + 1), (Convert-ToSlug -RawText $relativePath)
        $localArchivePath = Join-Path $localArchiveDirectory "${archiveSlug}.tar"
        $remoteArchivePath = Join-Path $remoteStagingRootPath "${archiveSlug}.tar"
        $remoteScpArchivePath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

        if (Test-Path -LiteralPath $localArchivePath) {
            Remove-Item -LiteralPath $localArchivePath -Force
        }

        $remoteTarScript = @"
New-Item -ItemType Directory -Force -Path '$remoteStagingRootPath' | Out-Null
Set-Location -LiteralPath '$remoteExecutionRoot'
& tar.exe -cf '$remoteArchivePath' '$relativePath'
exit `$LASTEXITCODE
"@

        $remoteTarResult = Invoke-RemotePowerShellScriptWithStreamingLog `
            -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteTarScript) `
            -LogPath $LogPath
        if ([int]$remoteTarResult.exit_code -ne 0) {
            throw "Remote artifact archive build failed | host=$RemoteHostAlias | path=$relativePath"
        }

        & scp "${RemoteHostAlias}:${remoteScpArchivePath}" $localArchivePath
        if ($LASTEXITCODE -ne 0) {
            throw "Remote artifact archive download failed | host=$RemoteHostAlias | path=$relativePath"
        }

        & tar.exe -xf $localArchivePath -C $projectRoot
        if ($LASTEXITCODE -ne 0) {
            throw "Local artifact archive extract failed | archive=$localArchivePath | path=$relativePath"
        }

        $remoteCleanupScript = @"
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit 0
"@

        $remoteCleanupResult = Invoke-RemotePowerShellScriptWithStreamingLog `
            -RemoteScriptText $remoteCleanupScript `
            -LogPath $LogPath
        if ([int]$remoteCleanupResult.exit_code -ne 0) {
            throw "Remote artifact cleanup failed | host=$RemoteHostAlias | path=$relativePath"
        }

        Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
    }
}

$resolvedCampaignConfigPathList = @()
foreach ($campaignConfigPath in $campaignConfigPathList) {
    $resolvedCampaignConfigPathList += Resolve-RepositoryRelativePath -InputPath $campaignConfigPath
}

$resolvedPlanningReportPath = Resolve-RepositoryRelativePath -InputPath $planningReportPath
$resolvedSourceSyncPathList = @()
foreach ($sourceSyncPath in $sourceSyncPathList) {
    $resolvedSourceSyncPathList += Resolve-RepositoryRelativePath -InputPath $sourceSyncPath
}

$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$campaignSlug = Convert-ToSlug -RawText $campaignName
$runTrackingDirectory = Join-Path $projectRoot (Join-Path $remoteTrackingRoot "${runTimestamp}_${campaignSlug}")
$runLogPath = Resolve-WindowsRelativePath -BasePath $projectRoot -TargetPath (Join-Path $runTrackingDirectory "remote_training_campaign.log")

New-Item -ItemType Directory -Force -Path $runTrackingDirectory | Out-Null

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Exact-Paper Run Count | $($campaignConfigPathList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Remote Host Alias | $RemoteHostAlias" -ForegroundColor Cyan
Write-Host "[INFO] Remote Repository Path | $RemoteRepositoryPath" -ForegroundColor Cyan
Write-Host "[INFO] Remote Conda Environment | $RemoteCondaEnvironmentName" -ForegroundColor Cyan

# Run Local And Remote Preflight
Write-StatusLine "INFO" "Checking local SSH and tar availability"
$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar.exe -ErrorAction Stop

Write-StatusLine "INFO" "Checking remote reachability"
& ssh $RemoteHostAlias "hostname"
if ($LASTEXITCODE -ne 0) {
    throw "Remote host is not reachable | host=$RemoteHostAlias"
}

$remotePreflightScript = @"
New-Item -ItemType Directory -Force -Path '$remoteStagingRootPath' | Out-Null
Set-Location -LiteralPath '$remoteExecutionRoot'
Write-Output ('REMOTE_EXECUTION_ROOT::{0}' -f (Get-Location).Path)
& conda run -n $RemoteCondaEnvironmentName python -c "import sys; print(sys.version)"
exit `$LASTEXITCODE
"@

Write-StatusLine "INFO" "Running remote environment preflight"
$preflightResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remotePreflightScript) `
    -LogPath $runLogPath
if ([int]$preflightResult.exit_code -ne 0) {
    throw "Remote environment preflight failed | host=$RemoteHostAlias"
}

# Sync Local Workspace To Remote Repository
Write-StatusLine "STEP" "Syncing local repository state to remote workstation"
Invoke-RemoteTarExtract -RelativePathList $resolvedSourceSyncPathList -LogPath $runLogPath

$requiredRemoteSourcePathList = @($resolvedCampaignConfigPathList + @($resolvedPlanningReportPath, "scripts\campaigns\run_track1_svr_reference_grid_search_repair_campaign.ps1", "scripts\campaigns\shared_streaming_campaign_launcher.ps1"))
Write-StatusLine "STEP" "Verifying remote campaign source paths after sync"
$remoteSourceVerificationResult = Test-RemoteSourcePathAvailability -RelativePathList $requiredRemoteSourcePathList -LogPath $runLogPath
if ([int]$remoteSourceVerificationResult.exit_code -ne 0) {
    $missingPathList = @($remoteSourceVerificationResult.missing_path_list)
    $missingPathText = if ($missingPathList.Count -gt 0) { $missingPathList[0] } else { "unknown" }
    throw "Remote source sync verification failed | missing_path=$missingPathText | host=$RemoteHostAlias"
}

# Launch The Real Exact-Paper Campaign Launcher On The Remote Workstation
$remoteRunScript = @"
Set-Location -LiteralPath '$remoteExecutionRoot'
Write-Output ('REMOTE_RUN_START::{0}' -f (Get-Location).Path)

& powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File 'scripts\campaigns\run_track1_svr_reference_grid_search_repair_campaign.ps1' -CondaEnvironmentName '$RemoteCondaEnvironmentName' -PythonExecutable 'python'
`$remoteExitCode = `$LASTEXITCODE
Write-Output ('REMOTE_RUN_EXIT_CODE::{0}' -f `$remoteExitCode)
if (`$remoteExitCode -ne 0) {
    exit `$remoteExitCode
}

function Resolve-WindowsRelativePath {
    param(
        [string]`$BasePath,
        [string]`$TargetPath
    )

    `$normalizedBasePath = [System.IO.Path]::GetFullPath(`$BasePath)
    `$normalizedTargetPath = [System.IO.Path]::GetFullPath(`$TargetPath)

    if (-not `$normalizedBasePath.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        `$normalizedBasePath += [System.IO.Path]::DirectorySeparatorChar
    }

    `$baseUri = New-Object System.Uri(`$normalizedBasePath)
    `$targetUri = New-Object System.Uri(`$normalizedTargetPath)
    `$relativeUri = `$baseUri.MakeRelativeUri(`$targetUri)
    `$relativePath = [System.Uri]::UnescapeDataString(`$relativeUri.ToString())
    return `$relativePath.Replace('/', '\')
}

`$campaignOutputDirectory = 'output\training_campaigns\$campaignName'
if (-not (Test-Path -LiteralPath `$campaignOutputDirectory)) {
    throw 'Remote campaign output directory missing after exact-paper launcher completion.'
}
Write-Output ('REMOTE_SYNC_PATH::{0}' -f `$campaignOutputDirectory)

`$runNameList = @(
"@

foreach ($runName in $runNameList) {
    $remoteRunScript += @"
    '$runName'
"@
}

$remoteRunScript += @"
)

foreach (`$runName in `$runNameList) {
    `$validationDirectory = Get-ChildItem -LiteralPath 'output\validation_checks\paper_reimplementation_rcim_exact_model_bank' -Directory |
        Where-Object { `$_.Name -like "*__`${runName}_campaign_run" } |
        Sort-Object LastWriteTime |
        Select-Object -Last 1

    if (`$null -eq `$validationDirectory) {
        throw ('Missing exact-paper validation directory for run | {0}' -f `$runName)
    }

    `$validationRelativePath = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$validationDirectory.FullName
    Write-Output ('REMOTE_SYNC_PATH::{0}' -f `$validationRelativePath)

    `$reportFile = Get-ChildItem -LiteralPath 'doc\reports\analysis\validation_checks' -File |
        Where-Object { `$_.Name -like "*_`${runName}_campaign_run_exact_paper_model_bank_report.md" } |
        Sort-Object LastWriteTime |
        Select-Object -Last 1

    if (`$null -eq `$reportFile) {
        throw ('Missing exact-paper validation report for run | {0}' -f `$runName)
    }

    `$reportRelativePath = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$reportFile.FullName
    Write-Output ('REMOTE_SYNC_PATH::{0}' -f `$reportRelativePath)
}

Write-Output 'REMOTE_RUN_MARKERS_EMITTED'
exit 0
"@

Write-StatusLine "STEP" "Launching remote exact-paper campaign"
$remoteRunResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteRunScript) `
    -LogPath $runLogPath
if ([int]$remoteRunResult.exit_code -ne 0) {
    throw "Remote exact-paper campaign failed | campaign=$campaignName | host=$RemoteHostAlias | log=$(Join-Path $projectRoot $runLogPath)"
}

$artifactSyncPathList = @()
foreach ($remoteOutputLine in @($remoteRunResult.output_line_list)) {
    if ($remoteOutputLine -match "^REMOTE_SYNC_PATH::(.+)$") {
        $artifactSyncPathList += $Matches[1].Trim()
    }
}
$artifactSyncPathList = @($artifactSyncPathList | Select-Object -Unique)

if ($artifactSyncPathList.Count -eq 0) {
    throw "Remote exact-paper campaign completed without returning artifact sync paths | campaign=$campaignName"
}

Write-StatusLine "STEP" "Syncing remote campaign artifacts back to the local repository"
Invoke-RemoteTarCopyToLocal -RelativePathList $artifactSyncPathList -LogPath $runLogPath

Write-Host ""
Write-Host "[DONE] Remote exact-paper SVR reference-grid repair campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
Write-Host "[DONE] Remote wrapper log available under | $(Join-Path $projectRoot $runLogPath)" -ForegroundColor Green
exit 0
