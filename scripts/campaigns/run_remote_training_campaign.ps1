param(
    [Parameter(Mandatory = $true)]
    [string[]]$CampaignConfigPathList,

    [Parameter(Mandatory = $true)]
    [string]$CampaignName,

    [Parameter(Mandatory = $true)]
    [string]$PlanningReportPath,

    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $env:STANDARDML_REMOTE_TRAINING_REPO_PATH,
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_codex_env" }),
    [string[]]$SourceSyncPathList = @("scripts", "config", "doc", "requirements.txt")
)

$ErrorActionPreference = "Stop"

$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..")).Path

Set-Location $projectRoot

# Define Local Tracking Paths
$localTrackingRootRelativePath = ".temp\remote_training_campaigns"
$localTrackingRootPath = Join-Path $projectRoot $localTrackingRootRelativePath
$statusFileRelativePath = "doc\running\remote_training_campaign_status.json"
$checklistFileRelativePath = "doc\running\remote_training_campaign_checklist.md"
$remoteStagingRootPath = "C:\Temp\standardml_remote_training"
$remoteExecutionDrive = "R:"
$remoteExecutionRoot = "R:\"

New-Item -ItemType Directory -Force -Path $localTrackingRootPath | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $projectRoot "doc\running") | Out-Null

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

function Resolve-RepositoryRelativePath {

    param(
        [string]$InputPath
    )

    $resolvedPath = (Resolve-Path -LiteralPath $InputPath).Path
    $relativePath = Resolve-WindowsRelativePath -BasePath $projectRoot -TargetPath $resolvedPath
    return $relativePath.Replace("/", "\")
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

function New-RemotePowerShellScriptText {

    param(
        [string]$ScriptText
    )

    return ("`$ProgressPreference = 'SilentlyContinue'`n{0}" -f $ScriptText)
}

function Get-RemotePowerShellCommand {

    return "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -OutputFormat Text -Command -"
}

function Get-RemotePowerShellFileCommand {

    param(
        [string]$RemoteScriptPath
    )

    return ('powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -OutputFormat Text -File "{0}"' -f $RemoteScriptPath)
}

function New-RemoteMappedRepositoryScriptText {

    param(
        [string]$ScriptText
    )

    return @"
`$remoteExecutionDrive = '$remoteExecutionDrive'
`$remoteExecutionRoot = '$remoteExecutionRoot'
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

function Write-RunState {

    param(
        [string]$RunStatus,
        [string]$Stage,
        [string]$LocalLogPath,
        [string]$RemoteCampaignOutputDirectory = "",
        [string]$RemoteManifestPath = "",
        [string]$LastFailureMessage = "",
        [string[]]$SyncedPathList = @()
    )

    $statusMap = [ordered]@{
        run_status = $RunStatus
        stage = $Stage
        remote_host_alias = $RemoteHostAlias
        remote_repository_path = $RemoteRepositoryPath
        remote_conda_environment_name = $RemoteCondaEnvironmentName
        campaign_name = $CampaignName
        planning_report_path = $PlanningReportPath
        campaign_config_path_list = $CampaignConfigPathList
        source_sync_path_list = $SourceSyncPathList
        local_log_path = $LocalLogPath
        remote_campaign_output_directory = $RemoteCampaignOutputDirectory
        remote_manifest_path = $RemoteManifestPath
        last_failure_message = $LastFailureMessage
        synced_path_list = $SyncedPathList
        updated_at = (Get-Date).ToString("o")
    }

    $statusJson = $statusMap | ConvertTo-Json -Depth 6
    Set-Content -LiteralPath (Join-Path $projectRoot $statusFileRelativePath) -Value $statusJson -Encoding UTF8

    $checklistLineList = @(
        "# Remote Training Campaign Checklist",
        "",
        "- Run status: $RunStatus",
        "- Stage: $Stage",
        "- Remote host alias: $RemoteHostAlias",
        "- Remote repository path: $RemoteRepositoryPath",
        "- Remote Conda environment: $RemoteCondaEnvironmentName",
        "- Campaign name: $CampaignName",
        "- Planning report path: $PlanningReportPath",
        "- Local log path: $LocalLogPath",
        "- Remote campaign output directory: $RemoteCampaignOutputDirectory",
        "- Remote manifest path: $RemoteManifestPath",
        "- Updated at: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
        "",
        "## Campaign Config Paths",
        ""
    )

    foreach ($campaignConfigPath in $CampaignConfigPathList) {
        $checklistLineList += "- $campaignConfigPath"
    }

    $checklistLineList += @(
        "",
        "## Source Sync Paths",
        ""
    )

    foreach ($sourceSyncPath in $SourceSyncPathList) {
        $checklistLineList += "- $sourceSyncPath"
    }

    if ($SyncedPathList.Count -gt 0) {
        $checklistLineList += @(
            "",
            "## Synced Artifact Paths",
            ""
        )

        foreach ($syncedPath in $SyncedPathList) {
            $checklistLineList += "- $syncedPath"
        }
    }

    if ($LastFailureMessage) {
        $checklistLineList += @(
            "",
            "## Last Failure",
            "",
            $LastFailureMessage
        )
    }

    $checklistText = (($checklistLineList -join "`n").TrimEnd() + "`n")
    Set-Content -LiteralPath (Join-Path $projectRoot $checklistFileRelativePath) -Value $checklistText -Encoding UTF8
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
    if ([System.IO.Path]::IsPathRooted($LogPath)) {
        $resolvedLogPath = $LogPath
    }
    else {
        $resolvedLogPath = Join-Path $projectRoot $LogPath
    }

    $logDirectoryPath = Split-Path -Parent $resolvedLogPath
    if (-not [string]::IsNullOrWhiteSpace($logDirectoryPath)) {
        New-Item -ItemType Directory -Force -Path $logDirectoryPath | Out-Null
    }

    $utf8Encoding = [System.Text.ASCIIEncoding]::new()
    $logWriter = [System.IO.StreamWriter]::new($resolvedLogPath, $true, $utf8Encoding)
    $collectedLineList = [System.Collections.Generic.List[string]]::new()
    $process = $null
    $normalizedRemoteScriptText = $RemoteScriptText.TrimStart([char]0xFEFF)
    $localTemporaryScriptPath = Join-Path $logDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryDirectoryPath = $remoteStagingRootPath
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryScpPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryScriptPath

    try {
        [System.IO.File]::WriteAllText($localTemporaryScriptPath, $normalizedRemoteScriptText, $utf8Encoding)

        $remoteDirectoryEnsureArgumentList = @(
            $RemoteHostAlias,
            ('cmd /d /c if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectoryPath)
        )
        & $sshExecutablePath @remoteDirectoryEnsureArgumentList | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script directory prepare failed | host=$RemoteHostAlias | path=$remoteTemporaryDirectoryPath"
        }

        $scpArgumentList = @(
            $localTemporaryScriptPath,
            ('{0}:{1}' -f $RemoteHostAlias, $remoteTemporaryScpPath)
        )
        & $scpExecutablePath @scpArgumentList | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script upload failed | host=$RemoteHostAlias | path=$remoteTemporaryScriptPath"
        }

        $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $startInfo.FileName = "cmd.exe"
        $startInfo.Arguments = (
            '/d /c ""{0}" {1} {2}""' -f
            $sshExecutablePath,
            $RemoteHostAlias,
            (Get-RemotePowerShellFileCommand -RemoteScriptPath $remoteTemporaryScriptPath)
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
                Write-StreamingLine `
                    -LineText $process.StandardOutput.ReadLine() `
                    -LogWriter $logWriter `
                    -CollectedLineList $collectedLineList
            }

            while ($process.StandardError.Peek() -ge 0) {
                Write-StreamingLine `
                    -LineText $process.StandardError.ReadLine() `
                    -LogWriter $logWriter `
                    -CollectedLineList $collectedLineList
            }

            $null = $process.WaitForExit(200)
        }

        while (-not $process.StandardOutput.EndOfStream) {
            Write-StreamingLine `
                -LineText $process.StandardOutput.ReadLine() `
                -LogWriter $logWriter `
                -CollectedLineList $collectedLineList
        }

        while (-not $process.StandardError.EndOfStream) {
            Write-StreamingLine `
                -LineText $process.StandardError.ReadLine() `
                -LogWriter $logWriter `
                -CollectedLineList $collectedLineList
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
        $remoteCleanupArgumentList = @(
            $RemoteHostAlias,
            ('cmd /d /c if exist "{0}" del /f /q "{0}"' -f $remoteTemporaryScriptPath)
        )
        & $sshExecutablePath @remoteCleanupArgumentList | Out-Null
        if (Test-Path -LiteralPath $localTemporaryScriptPath) {
            Remove-Item -LiteralPath $localTemporaryScriptPath -Force -ErrorAction SilentlyContinue
        }
    }
}

function Invoke-RemoteTarExtract {

    param(
        [string[]]$RelativePathList
    )

    $localArchivePath = Join-Path $runTrackingDirectory "source_sync_payload.tar"
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\remote_training_source_sync.tar"
    $remoteScpArchivePath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath

    if (Test-Path -LiteralPath $localArchivePath) {
        Remove-Item -LiteralPath $localArchivePath -Force
    }

    & tar.exe -cf $localArchivePath @RelativePathList
    if ($LASTEXITCODE -ne 0) {
        throw "Local source archive build failed | path=$localArchivePath"
    }

    & scp $localArchivePath "${RemoteHostAlias}:${remoteScpArchivePath}"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote source archive upload failed | host=$RemoteHostAlias"
    }

    $remoteExtractScript = @"
New-Item -ItemType Directory -Force -Path (Join-Path '$RemoteRepositoryPath' '.temp') | Out-Null
Set-Location -LiteralPath '$remoteExecutionRoot'
& tar.exe -xf '$remoteArchivePath'
`$extractExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit `$extractExitCode
"@

    $extractResult = Invoke-RemotePowerShellScriptWithStreamingLog `
        -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteExtractScript)) `
        -LogPath $runLogPath
    if ([int]$extractResult.exit_code -ne 0) {
        throw "Remote source sync failed | host=$RemoteHostAlias"
    }
}

function Invoke-RemoteSourceFileSync {

    param(
        [string[]]$RelativeFilePathList
    )

    foreach ($relativeFilePath in $RelativeFilePathList) {

        # Resolve Local And Remote File Paths
        $localSourceFilePath = Join-Path $projectRoot $relativeFilePath
        if (-not (Test-Path -LiteralPath $localSourceFilePath)) {
            throw "Local source file does not exist | $localSourceFilePath"
        }

        $sourceLeafName = Split-Path -Leaf $relativeFilePath
        $remoteDestinationFilePath = Join-Path $RemoteRepositoryPath $relativeFilePath
        $remoteDestinationParentPath = Split-Path -Parent $remoteDestinationFilePath
        $remoteTemporaryDirectoryPath = Join-Path $RemoteRepositoryPath ".temp\source_sync_stage"
        $remoteTemporaryDirectoryScpPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryDirectoryPath
        $remoteTemporaryFilePath = Join-Path $remoteTemporaryDirectoryPath $sourceLeafName

        # Prepare Remote Destination
        $remotePrepareScript = @"
New-Item -ItemType Directory -Force -Path '$remoteDestinationParentPath' | Out-Null
New-Item -ItemType Directory -Force -Path '$remoteTemporaryDirectoryPath' | Out-Null

cmd.exe /d /c "if exist ""$remoteDestinationFilePath"" del /f /q ""$remoteDestinationFilePath""" | Out-Null
cmd.exe /d /c "if exist ""$remoteDestinationFilePath"" rmdir /s /q ""$remoteDestinationFilePath""" | Out-Null
Remove-Item -LiteralPath '$remoteDestinationFilePath' -Force -Recurse -ErrorAction SilentlyContinue
Remove-Item -LiteralPath '$remoteTemporaryFilePath' -Force -Recurse -ErrorAction SilentlyContinue
exit 0
"@

        $prepareResult = Invoke-RemotePowerShellScriptWithStreamingLog `
            -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText $remotePrepareScript) `
            -LogPath $runLogPath
        if ([int]$prepareResult.exit_code -ne 0) {
            throw "Remote source-file sync prepare failed | host=$RemoteHostAlias | path=$relativeFilePath"
        }

        # Upload Local Source File To Remote Temporary Path
        & scp $localSourceFilePath "${RemoteHostAlias}:${remoteTemporaryDirectoryScpPath}"
        if ($LASTEXITCODE -ne 0) {
            throw "Remote source-file upload failed | host=$RemoteHostAlias | path=$relativeFilePath"
        }

        # Materialize Final Destination
        $remoteFinalizeScript = @"
`$remoteTemporaryFilePath = '$remoteTemporaryFilePath'
`$remoteDestinationFilePath = '$remoteDestinationFilePath'
`$remoteVerificationScriptPath = Join-Path '$RemoteRepositoryPath' '.temp\remote_source_file_finalize.py'

`$pythonFinalizeScriptText = @'
from pathlib import Path
import os
import subprocess
import shutil
import sys

source_path = Path(r'''$remoteTemporaryFilePath''')
destination_path = Path(r'''$remoteDestinationFilePath''')

if not source_path.exists():
    print(f"REMOTE_SOURCE_TEMP_MISSING::{source_path}")
    print(f"REMOTE_SOURCE_TEMP_PARENT::{source_path.parent}")
    print(f"REMOTE_SOURCE_TEMP_PARENT_EXISTS::{source_path.parent.exists()}")
    if source_path.parent.exists():
        for child in sorted(source_path.parent.iterdir()):
            print(f"REMOTE_SOURCE_TEMP_ENTRY::{child.name}::{child.exists()}::{child.is_file()}")
    sys.exit(5)

destination_path.parent.mkdir(parents=True, exist_ok=True)
print(f"REMOTE_DESTINATION_PARENT::{destination_path.parent}")
print(f"REMOTE_DESTINATION_PARENT_EXISTS::{destination_path.parent.exists()}")

subprocess.run(f'cmd /d /c del /f /q \"{destination_path}\" 2>nul', shell=True)
subprocess.run(f'cmd /d /c rmdir /s /q \"{destination_path}\" 2>nul', shell=True)

destination_path.write_bytes(source_path.read_bytes())

if not destination_path.exists() or not destination_path.is_file():
    print(f"REMOTE_SOURCE_DESTINATION_INVALID::{destination_path}")
    sys.exit(6)

print(f"REMOTE_SOURCE_DESTINATION_READY::{destination_path}")
sys.exit(0)
'@

Set-Content -LiteralPath `$remoteVerificationScriptPath -Value `$pythonFinalizeScriptText -Encoding UTF8
& conda run -n $RemoteCondaEnvironmentName python `$remoteVerificationScriptPath
`$finalizeExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath `$remoteVerificationScriptPath -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath `$remoteTemporaryFilePath -Force -ErrorAction SilentlyContinue
exit `$finalizeExitCode
"@

        $finalizeResult = Invoke-RemotePowerShellScriptWithStreamingLog `
            -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText $remoteFinalizeScript) `
            -LogPath $runLogPath
        if ([int]$finalizeResult.exit_code -ne 0) {
            throw "Remote source-file materialization failed | host=$RemoteHostAlias | path=$relativeFilePath"
        }
    }
}

function Test-RemoteSourcePathAvailability {

    param(
        [string[]]$RelativePathList,
        [string]$LogPath
    )

    $pythonRequiredPathEntryList = @()
    foreach ($relativePath in $RelativePathList) {
        $pythonFriendlyRelativePath = $relativePath.Replace("\", "/")
        $pythonRequiredPathEntryList += ("    '{0}'" -f $pythonFriendlyRelativePath)
    }
    $pythonRequiredPathBlock = [string]::Join(",`n", $pythonRequiredPathEntryList)
    $pythonProjectRoot = $remoteExecutionRoot.Replace("\", "/")

    $remoteVerificationScript = @"
Set-Location -LiteralPath '$remoteExecutionRoot'
Write-Output ('REMOTE_VERIFICATION_WORKDIR::{0}' -f (Get-Location).Path)

`$pythonVerificationScriptPath = Join-Path '$remoteExecutionRoot' '.temp\remote_source_path_verification.py'
New-Item -ItemType Directory -Force -Path (Split-Path -Parent `$pythonVerificationScriptPath) | Out-Null

`$pythonVerificationScriptText = @'
from pathlib import Path
import sys

project_root = Path('$pythonProjectRoot')
required_paths = [
$pythonRequiredPathBlock
]

print(f"REMOTE_VERIFICATION_PROJECT_ROOT::{project_root}")

for relative_path in required_paths:
    resolved_path = (project_root / relative_path).resolve()
    if not resolved_path.exists():
        parent_path = resolved_path.parent
        print(f"REMOTE_MISSING_REQUIRED_PATH::{relative_path}")
        print(f"REMOTE_MISSING_RESOLVED_PATH::{resolved_path}")
        print(f"REMOTE_MISSING_PARENT_PATH::{parent_path}")
        print(f"REMOTE_MISSING_PARENT_EXISTS::{parent_path.exists()}")
        if parent_path.exists():
            for child in sorted(parent_path.iterdir()):
                print(f"REMOTE_PARENT_ENTRY::{child.name}::{child.exists()}::{child.is_file()}")
        sys.exit(3)

    print(f"REMOTE_VERIFIED_REQUIRED_PATH::{relative_path}")

sys.exit(0)
'@

Set-Content -LiteralPath `$pythonVerificationScriptPath -Value `$pythonVerificationScriptText -Encoding UTF8
& conda run -n $RemoteCondaEnvironmentName python `$pythonVerificationScriptPath
`$verificationExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath `$pythonVerificationScriptPath -Force -ErrorAction SilentlyContinue
exit `$verificationExitCode
"@

    $verificationResult = Invoke-RemotePowerShellScriptWithStreamingLog `
        -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteVerificationScript)) `
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
        [string[]]$RelativePathList
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
            -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteTarScript)) `
            -LogPath $runLogPath
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
            -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText $remoteCleanupScript) `
            -LogPath $runLogPath
        if ([int]$remoteCleanupResult.exit_code -ne 0) {
            throw "Remote artifact cleanup failed | host=$RemoteHostAlias | path=$relativePath"
        }

        Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
    }
}

if ([string]::IsNullOrWhiteSpace($RemoteRepositoryPath)) {
    throw "RemoteRepositoryPath is required. Set STANDARDML_REMOTE_TRAINING_REPO_PATH or pass -RemoteRepositoryPath."
}

# Resolve Repository-Relative Inputs
$resolvedCampaignConfigPathList = @()
foreach ($campaignConfigPath in $CampaignConfigPathList) {
    $resolvedCampaignConfigPathList += Resolve-RepositoryRelativePath -InputPath $campaignConfigPath
}

$resolvedPlanningReportPath = Resolve-RepositoryRelativePath -InputPath $PlanningReportPath
$resolvedSourceSyncPathList = @()
foreach ($sourceSyncPath in $SourceSyncPathList) {
    $resolvedSourceSyncPathList += Resolve-RepositoryRelativePath -InputPath $sourceSyncPath
}

$campaignSlug = Convert-ToSlug $CampaignName
$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$runTrackingDirectory = Join-Path $localTrackingRootPath "${runTimestamp}_${campaignSlug}"
$runLogPath = Join-Path $runTrackingDirectory "remote_training_campaign.log"
$localManifestCopyPath = Join-Path $runTrackingDirectory "campaign_manifest.yaml"
$localSyncPayloadPath = Join-Path $runTrackingDirectory "sync_manifest.json"

New-Item -ItemType Directory -Force -Path $runTrackingDirectory | Out-Null
Write-RunState -RunStatus "running" -Stage "preflight" -LocalLogPath $runLogPath

# Run Local And Remote Preflight
Write-StatusLine "INFO" "Checking local SSH and tar availability"
$null = Get-Command ssh -ErrorAction Stop
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
& tar.exe --version | Out-Null
& conda run -n $RemoteCondaEnvironmentName python -c "import sys; print(sys.version)"
exit `$LASTEXITCODE
"@

Write-StatusLine "INFO" "Running remote environment preflight"
$preflightResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remotePreflightScript)) `
    -LogPath $runLogPath
if ([int]$preflightResult.exit_code -ne 0) {
    throw "Remote environment preflight failed | host=$RemoteHostAlias"
}

# Sync Local Workspace To Remote Repository
Write-StatusLine "STEP" "Syncing local repository state to remote workstation"
Write-RunState -RunStatus "running" -Stage "sync_up" -LocalLogPath $runLogPath
Invoke-RemoteTarExtract -RelativePathList $resolvedSourceSyncPathList

$requiredRemoteSourcePathList = @($resolvedCampaignConfigPathList + @($resolvedPlanningReportPath))
Write-StatusLine "STEP" "Verifying remote campaign source paths after sync"
$remoteSourceVerificationResult = Test-RemoteSourcePathAvailability `
    -RelativePathList $requiredRemoteSourcePathList `
    -LogPath $runLogPath
if ([int]$remoteSourceVerificationResult.exit_code -ne 0) {
    $missingPathList = @($remoteSourceVerificationResult.missing_path_list)
    if ($missingPathList.Count -gt 0) {
        $failureMessage = "Remote source sync verification failed | missing_path=$($missingPathList[0]) | host=$RemoteHostAlias"
    }
    else {
        $failureMessage = "Remote source sync verification failed | host=$RemoteHostAlias"
    }

    Write-RunState -RunStatus "failed" -Stage "sync_up" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

$remoteRunScript = @"
Set-Location -LiteralPath '$remoteExecutionRoot'
Write-Output ('REMOTE_RUN_START::{0}' -f (Get-Location).Path)

`$argumentList = @(
    '-B',
    'scripts/training/run_training_campaign.py'
"@

foreach ($campaignConfigPath in $resolvedCampaignConfigPathList) {
    $remoteRunScript += @"
    ,'$campaignConfigPath'
"@
}

$remoteRunScript += @"
    ,'--campaign-name'
    ,'$CampaignName'
    ,'--planning-report-path'
    ,'$resolvedPlanningReportPath'
)

& conda run -n $RemoteCondaEnvironmentName python @argumentList
`$remoteExitCode = `$LASTEXITCODE
Write-Output ('REMOTE_RUN_EXIT_CODE::{0}' -f `$remoteExitCode)
if (`$remoteExitCode -ne 0) {
    exit `$remoteExitCode
}

Write-Output 'REMOTE_RUN_RESOLVE_OUTPUT_START'
`$matchingDirectory = Get-ChildItem -LiteralPath 'output\training_campaigns' -Directory |
    Where-Object { `$_.Name -like '*$CampaignName*' } |
    Sort-Object LastWriteTime |
    Select-Object -Last 1

if (`$null -eq `$matchingDirectory) {
    Write-Output 'REMOTE_RUN_OUTPUT_DIRECTORY_NOT_FOUND'
    throw 'Could not resolve the remote campaign output directory after campaign completion.'
}

Write-Output ('REMOTE_RUN_OUTPUT_DIRECTORY_FOUND::{0}' -f `$matchingDirectory.FullName)

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

`$relativeCampaignOutputDirectory = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$matchingDirectory.FullName
`$relativeManifestPath = [System.IO.Path]::Combine(`$relativeCampaignOutputDirectory, 'campaign_manifest.yaml')
`$relativeSyncManifestPath = [System.IO.Path]::Combine('.temp', 'remote_training_sync_manifest.json')
Write-Output ('REMOTE_RUN_MANIFEST_CANDIDATE::{0}' -f `$relativeManifestPath)
Write-Output ('REMOTE_RUN_SYNC_MANIFEST_CANDIDATE::{0}' -f `$relativeSyncManifestPath)

& conda run -n $RemoteCondaEnvironmentName python -B scripts/training/build_remote_training_sync_manifest.py --campaign-manifest-path `$relativeManifestPath --output-path `$relativeSyncManifestPath
`$syncManifestExitCode = `$LASTEXITCODE
Write-Output ('REMOTE_RUN_SYNC_MANIFEST_EXIT_CODE::{0}' -f `$syncManifestExitCode)
if (`$syncManifestExitCode -ne 0) {
    exit `$syncManifestExitCode
}

Write-Output ('REMOTE_CAMPAIGN_OUTPUT_DIRECTORY::{0}' -f `$relativeCampaignOutputDirectory)
Write-Output ('REMOTE_CAMPAIGN_MANIFEST_PATH::{0}' -f `$relativeManifestPath)
Write-Output ('REMOTE_SYNC_MANIFEST_PATH::{0}' -f `$relativeSyncManifestPath)
Write-Output 'REMOTE_RUN_MARKERS_EMITTED'
exit 0
"@

Write-StatusLine "STEP" "Launching remote training campaign"
Write-RunState -RunStatus "running" -Stage "remote_run" -LocalLogPath $runLogPath

$remoteRunResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemotePowerShellScriptText -ScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteRunScript)) `
    -LogPath $runLogPath
$remoteOutputLineList = @($remoteRunResult.output_line_list)
$remoteExitCode = [int]$remoteRunResult.exit_code
if ($remoteExitCode -ne 0) {
    $failureMessage = "Remote training campaign failed | campaign=$CampaignName | host=$RemoteHostAlias | log=$runLogPath"
    Write-RunState -RunStatus "failed" -Stage "remote_run" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

$remoteCampaignOutputDirectory = ""
$remoteManifestPath = ""
$remoteSyncManifestPath = ""

foreach ($remoteOutputLine in $remoteOutputLineList) {
    if ($remoteOutputLine -match "^REMOTE_CAMPAIGN_OUTPUT_DIRECTORY::(.+)$") {
        $remoteCampaignOutputDirectory = $Matches[1].Trim()
    }
    elseif ($remoteOutputLine -match "^REMOTE_CAMPAIGN_MANIFEST_PATH::(.+)$") {
        $remoteManifestPath = $Matches[1].Trim()
    }
    elseif ($remoteOutputLine -match "^REMOTE_SYNC_MANIFEST_PATH::(.+)$") {
        $remoteSyncManifestPath = $Matches[1].Trim()
    }
}

if ([string]::IsNullOrWhiteSpace($remoteManifestPath)) {
    $remoteOutputTail = @($remoteOutputLineList | Select-Object -Last 20)
    $tailSummary = if ($remoteOutputTail.Count -gt 0) { ($remoteOutputTail -join " || ") } else { "no_remote_output_captured" }
    $failureMessage = "Remote campaign completed without returning a manifest path marker | campaign=$CampaignName | remote_output_tail=$tailSummary"
    Write-RunState -RunStatus "failed" -Stage "remote_run" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

# Sync Manifest And Remote Sync Payload Back To The Local Workstation
if ([string]::IsNullOrWhiteSpace($remoteSyncManifestPath)) {
    $remoteOutputTail = @($remoteOutputLineList | Select-Object -Last 20)
    $tailSummary = if ($remoteOutputTail.Count -gt 0) { ($remoteOutputTail -join " || ") } else { "no_remote_output_captured" }
    $failureMessage = "Remote campaign completed without returning a sync manifest path marker | campaign=$CampaignName | remote_output_tail=$tailSummary"
    Write-RunState -RunStatus "failed" -Stage "remote_run" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

Write-StatusLine "STEP" "Syncing remote campaign manifest and sync payload to local workstation"
Write-RunState -RunStatus "running" -Stage "sync_manifest" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath
Invoke-RemoteTarCopyToLocal -RelativePathList @($remoteManifestPath, $remoteSyncManifestPath)

$localResolvedManifestPath = Join-Path $projectRoot $remoteManifestPath
Copy-Item -LiteralPath $localResolvedManifestPath -Destination $localManifestCopyPath -Force
$localResolvedSyncManifestPath = Join-Path $projectRoot $remoteSyncManifestPath
Copy-Item -LiteralPath $localResolvedSyncManifestPath -Destination $localSyncPayloadPath -Force

$syncPayload = Get-Content -LiteralPath $localSyncPayloadPath -Raw | ConvertFrom-Json
$artifactSyncPathList = @($syncPayload.sync_path_list)

Write-StatusLine "STEP" "Syncing remote campaign artifacts back to the local repository"
Write-RunState -RunStatus "running" -Stage "sync_down" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath -SyncedPathList $artifactSyncPathList
Invoke-RemoteTarCopyToLocal -RelativePathList $artifactSyncPathList

$remoteCleanupScript = @"
Remove-Item -LiteralPath (Join-Path '$RemoteRepositoryPath' '$remoteSyncManifestPath') -Force -ErrorAction SilentlyContinue
exit 0
"@

(New-RemotePowerShellScriptText -ScriptText $remoteCleanupScript) |
    & ssh $RemoteHostAlias (Get-RemotePowerShellCommand) | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-StatusLine "WARN" "Remote sync-manifest cleanup failed | path=$remoteSyncManifestPath"
}

Write-RunState -RunStatus "completed" -Stage "completed" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath -SyncedPathList $artifactSyncPathList

try {

    # Refresh Local Master Summary After Remote Artifact Sync
    Write-StatusLine "STEP" "Refreshing local training results master summary"
    & python -B ".\scripts\reports\generate_training_results_master_summary.py"
    if ($LASTEXITCODE -ne 0) {
        Write-StatusLine "WARN" "Local training results master summary refresh returned a non-zero exit code"
    }

} catch {

    # Preserve Campaign Completion And Surface the Summary Failure
    Write-StatusLine "WARN" "Local training results master summary refresh failed | $($_.Exception.Message)"
}

Write-StatusLine "DONE" "Remote training campaign completed and artifacts synchronized"
exit 0
