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
$syncManifestBuilderRelativePath = "scripts\training\build_remote_training_sync_manifest.py"

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

function New-EncodedRemotePowerShellCommand {

    param(
        [string]$ScriptText
    )

    $wrappedScriptText = @"
`$ProgressPreference = 'SilentlyContinue'
$ScriptText
"@

    $scriptBytes = [System.Text.Encoding]::Unicode.GetBytes($wrappedScriptText)
    $encodedCommand = [Convert]::ToBase64String($scriptBytes)
    return "powershell -NoProfile -NonInteractive -OutputFormat Text -EncodedCommand $encodedCommand"
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
Set-Location -LiteralPath '$RemoteRepositoryPath'
& tar.exe -xf '$remoteArchivePath'
`$extractExitCode = `$LASTEXITCODE
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit `$extractExitCode
"@

    & ssh $RemoteHostAlias (New-EncodedRemotePowerShellCommand -ScriptText $remoteExtractScript)
    if ($LASTEXITCODE -ne 0) {
        throw "Remote source sync failed | host=$RemoteHostAlias"
    }
}

function Invoke-RemoteTarCopyToLocal {

    param(
        [string[]]$RelativePathList
    )

    $localArchivePath = Join-Path $runTrackingDirectory "artifact_sync_payload.tar"
    $remoteArchivePath = Join-Path $RemoteRepositoryPath ".temp\remote_training_artifact_sync.tar"
    $remoteScpArchivePath = Convert-ToScpRemotePath -WindowsPath $remoteArchivePath
    $remoteTarArgumentList = @($RelativePathList | ForEach-Object { '"{0}"' -f $_ })
    $remoteTarScript = @"
New-Item -ItemType Directory -Force -Path (Join-Path '$RemoteRepositoryPath' '.temp') | Out-Null
Set-Location -LiteralPath '$RemoteRepositoryPath'
& tar.exe -cf '$remoteArchivePath' $($remoteTarArgumentList -join ' ')
exit `$LASTEXITCODE
"@

    if (Test-Path -LiteralPath $localArchivePath) {
        Remove-Item -LiteralPath $localArchivePath -Force
    }

    $encodedRemoteCommand = New-EncodedRemotePowerShellCommand -ScriptText $remoteTarScript
    & ssh $RemoteHostAlias $encodedRemoteCommand
    if ($LASTEXITCODE -ne 0) {
        throw "Remote artifact archive build failed | host=$RemoteHostAlias"
    }

    & scp "${RemoteHostAlias}:${remoteScpArchivePath}" $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw "Remote artifact archive download failed | host=$RemoteHostAlias"
    }

    & tar.exe -xf $localArchivePath -C $projectRoot
    if ($LASTEXITCODE -ne 0) {
        throw "Local artifact archive extract failed | archive=$localArchivePath"
    }

    $remoteCleanupScript = @"
Remove-Item -LiteralPath '$remoteArchivePath' -Force -ErrorAction SilentlyContinue
exit 0
"@

    & ssh $RemoteHostAlias (New-EncodedRemotePowerShellCommand -ScriptText $remoteCleanupScript) | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Remote artifact sync failed | host=$RemoteHostAlias"
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
if (-not (Test-Path -LiteralPath '$RemoteRepositoryPath')) {
    throw 'Remote repository path does not exist | $RemoteRepositoryPath'
}

Set-Location -LiteralPath '$RemoteRepositoryPath'
& tar.exe --version | Out-Null
& conda run -n $RemoteCondaEnvironmentName python -c "import sys; print(sys.version)"
exit `$LASTEXITCODE
"@

Write-StatusLine "INFO" "Running remote environment preflight"
& ssh $RemoteHostAlias (New-EncodedRemotePowerShellCommand -ScriptText $remotePreflightScript)
if ($LASTEXITCODE -ne 0) {
    throw "Remote environment preflight failed | host=$RemoteHostAlias"
}

# Sync Local Workspace To Remote Repository
Write-StatusLine "STEP" "Syncing local repository state to remote workstation"
Write-RunState -RunStatus "running" -Stage "sync_up" -LocalLogPath $runLogPath
Invoke-RemoteTarExtract -RelativePathList $resolvedSourceSyncPathList

$remoteRunScript = @"
Set-Location -LiteralPath '$RemoteRepositoryPath'

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
if (`$remoteExitCode -ne 0) {
    exit `$remoteExitCode
}

`$matchingDirectory = Get-ChildItem -LiteralPath 'output\training_campaigns' -Directory |
    Where-Object { `$_.Name -like '*$CampaignName*' } |
    Sort-Object LastWriteTime |
    Select-Object -Last 1

if (`$null -eq `$matchingDirectory) {
    throw 'Could not resolve the remote campaign output directory after campaign completion.'
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

`$relativeCampaignOutputDirectory = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$matchingDirectory.FullName
`$relativeManifestPath = [System.IO.Path]::Combine(`$relativeCampaignOutputDirectory, 'campaign_manifest.yaml')

Write-Output ('REMOTE_CAMPAIGN_OUTPUT_DIRECTORY::{0}' -f `$relativeCampaignOutputDirectory)
Write-Output ('REMOTE_CAMPAIGN_MANIFEST_PATH::{0}' -f `$relativeManifestPath)
exit 0
"@

Write-StatusLine "STEP" "Launching remote training campaign"
Write-RunState -RunStatus "running" -Stage "remote_run" -LocalLogPath $runLogPath

$remoteOutputLineList = @()
& ssh $RemoteHostAlias (New-EncodedRemotePowerShellCommand -ScriptText $remoteRunScript) 2>&1 |
    Tee-Object -Variable remoteOutputLineList |
    Tee-Object -FilePath $runLogPath

$remoteExitCode = $LASTEXITCODE
if ($remoteExitCode -ne 0) {
    $failureMessage = "Remote training campaign failed | campaign=$CampaignName | host=$RemoteHostAlias | log=$runLogPath"
    Write-RunState -RunStatus "failed" -Stage "remote_run" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

$remoteCampaignOutputDirectory = ""
$remoteManifestPath = ""

foreach ($remoteOutputLine in $remoteOutputLineList) {
    if ($remoteOutputLine -match "^REMOTE_CAMPAIGN_OUTPUT_DIRECTORY::(.+)$") {
        $remoteCampaignOutputDirectory = $Matches[1].Trim()
    }
    elseif ($remoteOutputLine -match "^REMOTE_CAMPAIGN_MANIFEST_PATH::(.+)$") {
        $remoteManifestPath = $Matches[1].Trim()
    }
}

if ([string]::IsNullOrWhiteSpace($remoteManifestPath)) {
    $failureMessage = "Remote campaign completed without returning a manifest path marker | campaign=$CampaignName"
    Write-RunState -RunStatus "failed" -Stage "remote_run" -LocalLogPath $runLogPath -LastFailureMessage $failureMessage
    throw $failureMessage
}

# Sync Manifest, Resolve Artifact List, And Pull Results Back
Write-StatusLine "STEP" "Syncing remote campaign manifest to local workstation"
Write-RunState -RunStatus "running" -Stage "sync_manifest" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath
Invoke-RemoteTarCopyToLocal -RelativePathList @($remoteManifestPath)

$localResolvedManifestPath = Join-Path $projectRoot $remoteManifestPath
Copy-Item -LiteralPath $localResolvedManifestPath -Destination $localManifestCopyPath -Force

Write-StatusLine "STEP" "Building artifact sync list from remote campaign manifest"
& python -B $syncManifestBuilderRelativePath --campaign-manifest-path $localManifestCopyPath --output-path $localSyncPayloadPath
if ($LASTEXITCODE -ne 0) {
    throw "Failed to build the local sync manifest from $localManifestCopyPath"
}

$syncPayload = Get-Content -LiteralPath $localSyncPayloadPath -Raw | ConvertFrom-Json
$artifactSyncPathList = @($syncPayload.sync_path_list)

Write-StatusLine "STEP" "Syncing remote campaign artifacts back to the local repository"
Write-RunState -RunStatus "running" -Stage "sync_down" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath -SyncedPathList $artifactSyncPathList
Invoke-RemoteTarCopyToLocal -RelativePathList $artifactSyncPathList

Write-RunState -RunStatus "completed" -Stage "completed" -LocalLogPath $runLogPath -RemoteCampaignOutputDirectory $remoteCampaignOutputDirectory -RemoteManifestPath $remoteManifestPath -SyncedPathList $artifactSyncPathList
Write-StatusLine "DONE" "Remote training campaign completed and artifacts synchronized"
exit 0
