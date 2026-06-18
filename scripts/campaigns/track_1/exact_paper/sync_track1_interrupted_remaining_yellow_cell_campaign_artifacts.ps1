param(
    [string]$RemoteHostAlias = "",
    [string]$RemoteRepositoryPath = "",
    [string]$ActiveCampaignPath = "doc\running\active_training_campaign.yaml",
    [string]$LocalStagingRoot = ".temp\manual_sync_track1_svm",
    [switch]$SkipRemoteCleanup
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\.." )).Path
Set-Location $projectRoot

$expectedCampaignName = "track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43"
$expectedRemoteCampaignDirectory = "output\training_campaigns\track1\exact_paper\forward\remaining_yellow_cells\svm\track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43"
$validationPattern = "*__track1_svm_*_yellow_cell_attempt_*_campaign_run"
$reportPattern = "*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md"
$remoteTemporaryRoot = "C:\Temp\standardml_manual_sync"

function Write-StatusLine {

    param(
        [string]$Label,
        [string]$Message
    )

    Write-Host ("[{0}] [{1}] {2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Label, $Message)
}

function Resolve-RepositoryRelativePath {

    param(
        [string]$RelativePath
    )

    return (Join-Path $projectRoot $RelativePath)
}

function Get-ActiveCampaignScalarValue {

    param(
        [string]$YamlPath,
        [string]$KeyName
    )

    $matchingLine = Get-Content -LiteralPath $YamlPath | Where-Object { $_ -match ('^{0}:' -f [regex]::Escape($KeyName)) } | Select-Object -First 1
    if ($null -eq $matchingLine) {
        return ""
    }

    return (($matchingLine -replace ('^{0}:\s*' -f [regex]::Escape($KeyName)), "") -replace '^''|''$', '').Trim()
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

function Invoke-RemotePowerShellFile {

    param(
        [string]$ScriptText,
        [string]$RemoteAlias
    )

    $localTemporaryScriptPath = Join-Path $env:TEMP ("track1_interrupted_manual_sync_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryRoot ("track1_interrupted_manual_sync_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteScpScriptPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryScriptPath

    try {
        [System.IO.File]::WriteAllText($localTemporaryScriptPath, $ScriptText, [System.Text.ASCIIEncoding]::new())

        & ssh $RemoteAlias ('if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryRoot) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary directory prepare failed | host=$RemoteAlias | path=$remoteTemporaryRoot"
        }

        & scp $localTemporaryScriptPath ('{0}:{1}' -f $RemoteAlias, $remoteScpScriptPath) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script upload failed | host=$RemoteAlias | path=$remoteTemporaryScriptPath"
        }

        return @(& ssh $RemoteAlias "powershell -NoProfile -ExecutionPolicy Bypass -File `"$remoteTemporaryScriptPath`"")
    }
    finally {
        if (Test-Path -LiteralPath $localTemporaryScriptPath) {
            Remove-Item -LiteralPath $localTemporaryScriptPath -Force -ErrorAction SilentlyContinue
        }

        & ssh $RemoteAlias ('if exist "{0}" del /f /q "{0}"' -f $remoteTemporaryScriptPath) | Out-Null
    }
}

function New-RemoteArchiveBuildScript {

    param(
        [string]$RepositoryRootPath
    )

    return @"
`$ErrorActionPreference = 'Stop'
`$repositoryRoot = '$RepositoryRootPath'
`$temporaryRoot = '$remoteTemporaryRoot'
`$campaignDirectoryRelativePath = '$expectedRemoteCampaignDirectory'
`$validationPattern = '$validationPattern'
`$reportPattern = '$reportPattern'

function Write-MarkerLine {
    param([string]`$Text)
    Write-Output `$Text
}

function New-TarArchiveFromRelativePathList {
    param(
        [string]`$ArchivePath,
        [string[]]`$RelativePathList
    )

    if (`$RelativePathList.Count -eq 0) {
        return 0
    }

    if (Test-Path -LiteralPath `$ArchivePath) {
        Remove-Item -LiteralPath `$ArchivePath -Force -ErrorAction SilentlyContinue
    }

    & tar.exe -cf `$ArchivePath `$RelativePathList[0]
    if (`$LASTEXITCODE -ne 0) {
        throw ('Remote tar creation failed | archive=' + `$ArchivePath + ' | path=' + `$RelativePathList[0])
    }

    for (`$pathIndex = 1; `$pathIndex -lt `$RelativePathList.Count; `$pathIndex++) {
        & tar.exe -rf `$ArchivePath `$RelativePathList[`$pathIndex]
        if (`$LASTEXITCODE -ne 0) {
            throw ('Remote tar append failed | archive=' + `$ArchivePath + ' | path=' + `$RelativePathList[`$pathIndex])
        }
    }

    return `$RelativePathList.Count
}

New-Item -ItemType Directory -Force -Path `$temporaryRoot | Out-Null
Set-Location -LiteralPath `$repositoryRoot

`$campaignArchivePath = Join-Path `$temporaryRoot 'track1_svm_campaign_output.tar'
`$validationArchivePath = Join-Path `$temporaryRoot 'track1_svm_validation_dirs.tar'
`$reportArchivePath = Join-Path `$temporaryRoot 'track1_svm_validation_reports.tar'

`$campaignDirectoryExists = Test-Path -LiteralPath `$campaignDirectoryRelativePath
Write-MarkerLine ('REMOTE_CAMPAIGN_DIRECTORY_EXISTS::{0}' -f `$campaignDirectoryExists)
if (-not `$campaignDirectoryExists) {
    throw ('Remote campaign directory missing | path=' + `$campaignDirectoryRelativePath)
}

`$null = New-TarArchiveFromRelativePathList -ArchivePath `$campaignArchivePath -RelativePathList @(`$campaignDirectoryRelativePath)
Write-MarkerLine ('REMOTE_ARCHIVE_READY::campaign_output::{0}::{1}' -f `$campaignArchivePath, 1)

`$validationRelativePathList = @(
    Get-ChildItem 'output\validation_checks\paper_reimplementation_rcim_exact_model_bank\forward' -Directory -Recurse -ErrorAction SilentlyContinue |
        Where-Object { `$_.Name -like `$validationPattern } |
        Sort-Object Name |
        ForEach-Object { `$_.FullName.Substring(`$repositoryRoot.Length + 1) }
)
`$validationCount = New-TarArchiveFromRelativePathList -ArchivePath `$validationArchivePath -RelativePathList `$validationRelativePathList
Write-MarkerLine ('REMOTE_ARCHIVE_READY::validation_dirs::{0}::{1}' -f `$validationArchivePath, `$validationCount)

`$reportRelativePathList = @(
    Get-ChildItem 'doc\reports\analysis\validation_checks' -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { `$_.Name -like `$reportPattern } |
        Sort-Object Name |
        ForEach-Object { `$_.FullName.Substring(`$repositoryRoot.Length + 1) }
)
`$reportCount = New-TarArchiveFromRelativePathList -ArchivePath `$reportArchivePath -RelativePathList `$reportRelativePathList
Write-MarkerLine ('REMOTE_ARCHIVE_READY::validation_reports::{0}::{1}' -f `$reportArchivePath, `$reportCount)
"@
}

function Get-LastMarkerLine {

    param(
        [string[]]$LineList,
        [string]$Prefix
    )

    $matchingLineList = @($LineList | Where-Object { $_ -like ($Prefix + "*") })
    if ($matchingLineList.Count -eq 0) {
        return $null
    }

    return $matchingLineList[-1]
}

function Copy-RemoteArchiveToLocalAndExtract {

    param(
        [string]$ArchiveLabel,
        [string]$RemoteArchivePath,
        [int]$ExpectedItemCount,
        [string]$LocalRunStageDirectory
    )

    if ($ExpectedItemCount -le 0) {
        Write-StatusLine "INFO" "Skipping empty archive group | label=$ArchiveLabel"
        return
    }

    $localArchivePath = Join-Path $LocalRunStageDirectory ([System.IO.Path]::GetFileName($RemoteArchivePath))
    $remoteArchiveScpPath = Convert-ToScpRemotePath -WindowsPath $RemoteArchivePath

    Write-StatusLine "STEP" "Downloading remote archive | label=$ArchiveLabel | items=$ExpectedItemCount"
    & scp ('{0}:{1}' -f $resolvedRemoteHostAlias, $remoteArchiveScpPath) $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw "Remote archive download failed | label=$ArchiveLabel | path=$RemoteArchivePath"
    }

    Write-StatusLine "STEP" "Extracting archive into local repository | label=$ArchiveLabel"
    & tar.exe -xf $localArchivePath -C $projectRoot
    if ($LASTEXITCODE -ne 0) {
        throw "Local archive extract failed | label=$ArchiveLabel | path=$localArchivePath"
    }
}

function Remove-RemoteArchiveList {

    param(
        [string[]]$ArchivePathList,
        [string]$RemoteAlias
    )

    $quotedArchivePathList = @($ArchivePathList | ForEach-Object { "'" + $_.Replace("'", "''") + "'" })
    $archiveArrayText = [string]::Join(", ", $quotedArchivePathList)

    $cleanupScript = @"
`$ErrorActionPreference = 'Stop'
`$archivePathList = @($archiveArrayText)
foreach (`$archivePath in `$archivePathList) {
    Remove-Item -LiteralPath `$archivePath -Force -ErrorAction SilentlyContinue
}
"@

    $null = Invoke-RemotePowerShellFile -ScriptText $cleanupScript -RemoteAlias $RemoteAlias
}

$activeCampaignAbsolutePath = Resolve-RepositoryRelativePath -RelativePath $ActiveCampaignPath
if (-not (Test-Path -LiteralPath $activeCampaignAbsolutePath)) {
    throw "Active campaign state file does not exist | $activeCampaignAbsolutePath"
}

$resolvedCampaignName = Get-ActiveCampaignScalarValue -YamlPath $activeCampaignAbsolutePath -KeyName "campaign_name"
$resolvedCampaignStatus = Get-ActiveCampaignScalarValue -YamlPath $activeCampaignAbsolutePath -KeyName "status"
$resolvedRemoteHostAlias = if ([string]::IsNullOrWhiteSpace($RemoteHostAlias)) { Get-ActiveCampaignScalarValue -YamlPath $activeCampaignAbsolutePath -KeyName "remote_host_alias" } else { $RemoteHostAlias }
$resolvedRemoteRepositoryPath = if ([string]::IsNullOrWhiteSpace($RemoteRepositoryPath)) { Get-ActiveCampaignScalarValue -YamlPath $activeCampaignAbsolutePath -KeyName "remote_repository_path" } else { $RemoteRepositoryPath }

if ($resolvedCampaignName -ne $expectedCampaignName) {
    throw "Unexpected active campaign identity | expected=$expectedCampaignName | actual=$resolvedCampaignName"
}
if ([string]::IsNullOrWhiteSpace($resolvedRemoteHostAlias)) {
    throw "Remote host alias is empty"
}
if ([string]::IsNullOrWhiteSpace($resolvedRemoteRepositoryPath)) {
    throw "Remote repository path is empty"
}

$localStagingRootPath = Resolve-RepositoryRelativePath -RelativePath $LocalStagingRoot
$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$localRunStageDirectory = Join-Path $localStagingRootPath $runTimestamp
New-Item -ItemType Directory -Force -Path $localRunStageDirectory | Out-Null

Write-StatusLine "INFO" "Track 1 interrupted SVM manual sync starting"
Write-StatusLine "INFO" "Campaign | $resolvedCampaignName"
Write-StatusLine "INFO" "Canonical local campaign status | $resolvedCampaignStatus"
Write-StatusLine "INFO" "Remote host alias | $resolvedRemoteHostAlias"
Write-StatusLine "INFO" "Remote repository path | $resolvedRemoteRepositoryPath"
Write-StatusLine "INFO" "Local staging directory | $localRunStageDirectory"

$null = Get-Command ssh -ErrorAction Stop
$null = Get-Command scp -ErrorAction Stop
$null = Get-Command tar.exe -ErrorAction Stop

Write-StatusLine "STEP" "Checking remote reachability"
& ssh $resolvedRemoteHostAlias "hostname"
if ($LASTEXITCODE -ne 0) {
    throw "Remote host is not reachable from this workstation | host=$resolvedRemoteHostAlias"
}

Write-StatusLine "STEP" "Building remote tar archives"
$remoteOutputLineList = Invoke-RemotePowerShellFile -ScriptText (New-RemoteArchiveBuildScript -RepositoryRootPath $resolvedRemoteRepositoryPath) -RemoteAlias $resolvedRemoteHostAlias
$campaignArchiveMarker = Get-LastMarkerLine -LineList $remoteOutputLineList -Prefix "REMOTE_ARCHIVE_READY::campaign_output::"
$validationArchiveMarker = Get-LastMarkerLine -LineList $remoteOutputLineList -Prefix "REMOTE_ARCHIVE_READY::validation_dirs::"
$reportArchiveMarker = Get-LastMarkerLine -LineList $remoteOutputLineList -Prefix "REMOTE_ARCHIVE_READY::validation_reports::"

if ($null -eq $campaignArchiveMarker) {
    throw "Remote campaign archive marker missing"
}
if ($null -eq $validationArchiveMarker) {
    throw "Remote validation archive marker missing"
}
if ($null -eq $reportArchiveMarker) {
    throw "Remote report archive marker missing"
}

$campaignArchiveParts = ($campaignArchiveMarker -replace '^REMOTE_ARCHIVE_READY::campaign_output::', '') -split "::"
$validationArchiveParts = ($validationArchiveMarker -replace '^REMOTE_ARCHIVE_READY::validation_dirs::', '') -split "::"
$reportArchiveParts = ($reportArchiveMarker -replace '^REMOTE_ARCHIVE_READY::validation_reports::', '') -split "::"

$remoteArchivePathList = @($campaignArchiveParts[0], $validationArchiveParts[0], $reportArchiveParts[0])

Copy-RemoteArchiveToLocalAndExtract -ArchiveLabel "campaign_output" -RemoteArchivePath $campaignArchiveParts[0] -ExpectedItemCount ([int]$campaignArchiveParts[1]) -LocalRunStageDirectory $localRunStageDirectory
Copy-RemoteArchiveToLocalAndExtract -ArchiveLabel "validation_dirs" -RemoteArchivePath $validationArchiveParts[0] -ExpectedItemCount ([int]$validationArchiveParts[1]) -LocalRunStageDirectory $localRunStageDirectory
Copy-RemoteArchiveToLocalAndExtract -ArchiveLabel "validation_reports" -RemoteArchivePath $reportArchiveParts[0] -ExpectedItemCount ([int]$reportArchiveParts[1]) -LocalRunStageDirectory $localRunStageDirectory

if (-not $SkipRemoteCleanup) {
    Write-StatusLine "STEP" "Cleaning up temporary remote tar archives"
    Remove-RemoteArchiveList -ArchivePathList $remoteArchivePathList -RemoteAlias $resolvedRemoteHostAlias
}

$localValidationDirectoryList = @(
    Get-ChildItem -LiteralPath (Join-Path $projectRoot "output\validation_checks\paper_reimplementation_rcim_exact_model_bank\forward") -Directory -Recurse -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like $validationPattern } |
        Sort-Object Name
)
$localReportFileList = @(
    Get-ChildItem -LiteralPath (Join-Path $projectRoot "doc\reports\analysis\validation_checks") -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -like $reportPattern } |
        Sort-Object Name
)
$localCampaignLogRoot = Join-Path $projectRoot (Join-Path $expectedRemoteCampaignDirectory "logs")
$localCampaignLogFileList = @()
if (Test-Path -LiteralPath $localCampaignLogRoot) {
    $localCampaignLogFileList = @(Get-ChildItem -LiteralPath $localCampaignLogRoot -File | Sort-Object Name)
}

Write-Host ""
Write-Host ("=" * 96) -ForegroundColor DarkCyan
Write-Host "[INFO] Interrupted SVM Manual Sync Summary" -ForegroundColor Cyan
Write-Host ("=" * 96) -ForegroundColor DarkCyan
Write-Host "[INFO] Local validation directory count | $($localValidationDirectoryList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Local validation report count | $($localReportFileList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Local campaign log count | $($localCampaignLogFileList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Local campaign log root | $localCampaignLogRoot" -ForegroundColor Cyan
if ($localValidationDirectoryList.Count -gt 0) {
    Write-Host "[INFO] Latest validation directory | $($localValidationDirectoryList[-1].Name)" -ForegroundColor Cyan
}
if ($localReportFileList.Count -gt 0) {
    Write-Host "[INFO] Latest validation report | $($localReportFileList[-1].Name)" -ForegroundColor Cyan
}

Write-StatusLine "DONE" "Interrupted SVM manual artifact sync completed"
