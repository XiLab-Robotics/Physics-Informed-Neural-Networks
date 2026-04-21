param(
    [Parameter(Mandatory = $true)]
    [string]$CampaignName,

    [Parameter(Mandatory = $true)]
    [string]$PlanningReportPath,

    [Parameter(Mandatory = $true)]
    [string]$LauncherRelativePath,

    [Parameter(Mandatory = $true)]
    [string[]]$CampaignConfigPathList,

    [Parameter(Mandatory = $true)]
    [string[]]$RunNameList,

    [string]$ValidationOutputRoot = "output\\validation_checks\\paper_reimplementation_rcim_exact_model_bank",
    [string]$ValidationReportRoot = "doc\\reports\\analysis\\validation_checks",
    [string[]]$SourceSyncPathList = @(
        "scripts"
        "config"
        "doc"
        "requirements.txt"
    ),
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\..")).Path

Set-Location $projectRoot

# Define Campaign Identity
$campaignOutputRoot = Join-Path "output\training_campaigns\track1\exact_paper" $campaignName
$campaignLogRoot = Join-Path $campaignOutputRoot "logs"
$remoteTrackingRoot = ".temp\remote_training_campaigns"
$remoteExecutionDrive = "R:"
$remoteExecutionRoot = "R:\"
$remoteStagingRootPath = "C:\Temp\standardml_remote_training"

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

function Get-OptionalExactPaperDependencySpecificationList {

    param(
        [string[]]$RunNameList,
        [string[]]$CampaignConfigPathList,
        [string]$LauncherRelativePath
    )

    $dependencySpecificationList = @()
    $inspectionTokenList = @()

    $inspectionTokenList += @($RunNameList)
    $inspectionTokenList += @($CampaignConfigPathList)
    if (-not [string]::IsNullOrWhiteSpace($LauncherRelativePath)) {
        $inspectionTokenList += $LauncherRelativePath
    }

    $inspectionText = (@($inspectionTokenList) -join " ").ToLowerInvariant()

    if ($inspectionText.Contains("xgbm")) {
        $dependencySpecificationList += [PSCustomObject]@{
            family_name  = "XGBM"
            package_name = "xgboost"
            symbol_name  = "XGBRegressor"
        }
    }

    if ($inspectionText.Contains("lgbm")) {
        $dependencySpecificationList += [PSCustomObject]@{
            family_name  = "LGBM"
            package_name = "lightgbm"
            symbol_name  = "LGBMRegressor"
        }
    }

    return @($dependencySpecificationList)
}

function New-RemoteCondaPythonCommandText {

    param(
        [string]$CondaEnvironmentName,
        [string]$PythonInlineCode
    )

    $escapedInlineCode = $PythonInlineCode.Replace('"', '\"')
    return 'cmd.exe /d /c ""conda run -n {0} python -c ""{1}""""' -f $CondaEnvironmentName, $escapedInlineCode
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

function Convert-ToPowerShellEncodedCommand {

    param(
        [string]$ScriptText
    )

    $unicodeBytes = [System.Text.Encoding]::Unicode.GetBytes($ScriptText)
    return [Convert]::ToBase64String($unicodeBytes)
}

function Invoke-RemotePowerShellEncodedCommand {

    param(
        [string]$RemoteScriptText,
        [switch]$IgnoreExitCode
    )

    $sshExecutablePath = (Get-Command ssh -ErrorAction Stop).Source
    $encodedCommand = Convert-ToPowerShellEncodedCommand -ScriptText $RemoteScriptText
    & $sshExecutablePath $RemoteHostAlias "powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand $encodedCommand" | Out-Null

    if ((-not $IgnoreExitCode) -and ($LASTEXITCODE -ne 0)) {
        throw "Remote encoded PowerShell command failed | host=$RemoteHostAlias | exit_code=$LASTEXITCODE"
    }

    return [int]$LASTEXITCODE
}

function Invoke-RemotePowerShellScriptWithStreamingLog {

    param(
        [string]$RemoteScriptText,
        [string]$LogPath,
        [string]$ProgressActivity = "Remote command",
        [string[]]$RemoteKillMatchPatternList = @(),
        [int]$InitialConfigCount = 0,
        [string]$InitialConfigPath = "",
        [string]$InitialLogPath = ""
    )

    $sshExecutablePath = (Get-Command ssh -ErrorAction Stop).Source
    $scpExecutablePath = (Get-Command scp -ErrorAction Stop).Source
    $resolvedLogPath = Join-Path $projectRoot $LogPath
    $logDirectoryPath = Split-Path -Parent $resolvedLogPath
    $utf8Encoding = [System.Text.ASCIIEncoding]::new()
    $logWriter = $null
    $localTemporaryScriptPath = Join-Path $logDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryDirectoryPath = $remoteStagingRootPath
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("remote_command_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryScpPath = Convert-ToScpRemotePath -WindowsPath $remoteTemporaryScriptPath
    $collectedLineList = [System.Collections.Generic.List[string]]::new()
    $progressId = [Math]::Abs([int](Get-Random -Minimum 1000 -Maximum 32767))
    $currentConfigIndex = if (($InitialConfigCount -gt 0) -and (-not [string]::IsNullOrWhiteSpace($InitialConfigPath))) { 1 } else { 0 }
    $configCount = $InitialConfigCount
    $currentConfigPath = $InitialConfigPath
    $currentLogPath = $InitialLogPath
    $currentOperation = if ($currentConfigIndex -gt 0) { "Waiting for first remote line from exact-paper runner" } else { "Waiting for remote output" }
    $lastProgressUpdateTime = Get-Date
    $script:remoteCancelRequested = $false
    $cancelHandler = $null
    $previousErrorActionPreference = $ErrorActionPreference

    New-Item -ItemType Directory -Force -Path $logDirectoryPath | Out-Null

    try {
        $cancelHandler = [ConsoleCancelEventHandler]{
            param($sender, $eventArgs)
            $eventArgs.Cancel = $true
            $script:remoteCancelRequested = $true
        }
        [Console]::add_CancelKeyPress($cancelHandler)
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

        $ErrorActionPreference = "Continue"
        $remoteCommandLine = (
            'powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -OutputFormat Text -File "{0}"' -f
            $remoteTemporaryScriptPath
        )

        & $sshExecutablePath $RemoteHostAlias $remoteCommandLine 2>&1 | ForEach-Object {
            if ($script:remoteCancelRequested) {
                throw [System.Management.Automation.PipelineStoppedException]::new("Remote command interrupted by operator")
            }

            if ($null -eq $_) {
                return
            }

            $outputLine = $_.ToString()
            Write-StreamingLine -LineText $outputLine -LogWriter $logWriter -CollectedLineList $collectedLineList

            if ($outputLine -match "^REMOTE_ACTIVE_CONFIG::(\d+)::(\d+)::(.+)$") {
                $currentConfigIndex = [int]$Matches[1]
                $configCount = [int]$Matches[2]
                $currentConfigPath = $Matches[3].Trim()
                $currentOperation = "Running exact-paper config"
            }
            elseif ($outputLine -match "^REMOTE_ACTIVE_LOG::(.+)$") {
                $currentLogPath = $Matches[1].Trim()
            }
            elseif ($outputLine -match "^REMOTE_ACTIVE_STAGE::(.+)$") {
                $currentOperation = $Matches[1].Trim()
            }
            elseif ($outputLine -match "^\[INFO\] Grid search configured \| (.+)$") {
                $currentOperation = "Grid search configured | $($Matches[1].Trim())"
            }
            elseif ($outputLine -match "^\[DONE\]") {
                $currentOperation = $outputLine.Trim()
            }

            $now = Get-Date
            if (($now - $lastProgressUpdateTime).TotalSeconds -ge 1) {
                $percentComplete = 0
                if ($configCount -gt 0) {
                    $percentComplete = [Math]::Max(0, [Math]::Min(99, [int]((100.0 * [Math]::Max(0, ($currentConfigIndex - 1))) / $configCount)))
                }

                $statusText = if ($configCount -gt 0) {
                    "Config $currentConfigIndex/$configCount | $currentConfigPath"
                }
                else {
                    "Waiting for remote output"
                }

                $operationText = if ([string]::IsNullOrWhiteSpace($currentLogPath)) {
                    $currentOperation
                }
                else {
                    "$currentOperation | log $currentLogPath"
                }

                Write-Progress -Id $progressId -Activity $ProgressActivity -Status $statusText -CurrentOperation $operationText -PercentComplete $percentComplete
                $lastProgressUpdateTime = $now
            }
        }

        Write-Progress -Id $progressId -Activity $ProgressActivity -Completed
        return @{
            exit_code = [int]$LASTEXITCODE
            output_line_list = @($collectedLineList)
        }
    }
    catch [System.Management.Automation.PipelineStoppedException] {
        Write-StatusLine "WARN" "Ctrl+C received | terminating remote command and remote child processes"

        $remoteCleanupScript = @"
`$killPatternList = @(
    '$remoteTemporaryScriptPath'
"@
        foreach ($killPattern in $RemoteKillMatchPatternList) {
            $remoteCleanupScript += @"
    '$killPattern'
"@
        }
        $remoteCleanupScript += @"
)
`$stoppedProcessCount = 0
`$processList = Get-CimInstance Win32_Process
foreach (`$processEntry in `$processList) {
    `$commandLine = [string]`$processEntry.CommandLine
    if ([string]::IsNullOrWhiteSpace(`$commandLine)) {
        continue
    }

    `$shouldStop = `$false
    foreach (`$pattern in `$killPatternList) {
        if (`$commandLine -like ('*' + `$pattern + '*')) {
            `$shouldStop = `$true
            break
        }
    }

    if (-not `$shouldStop) {
        continue
    }

    Stop-Process -Id `$processEntry.ProcessId -Force -ErrorAction SilentlyContinue
    `$stoppedProcessCount += 1
}

Write-Output ('REMOTE_CANCEL_STOPPED_PROCESSES::{0}' -f `$stoppedProcessCount)
exit 0
"@
        try {
            Invoke-RemotePowerShellEncodedCommand -RemoteScriptText $remoteCleanupScript -IgnoreExitCode | Out-Null
        }
        catch {
            Write-StatusLine "WARN" "Remote cleanup after Ctrl+C failed | $($_.Exception.Message)"
        }

        throw "Remote command interrupted by operator"
    }
    finally {
        Write-Progress -Id $progressId -Activity $ProgressActivity -Completed
        $ErrorActionPreference = $previousErrorActionPreference
        if ($null -ne $cancelHandler) {
            [Console]::remove_CancelKeyPress($cancelHandler)
        }

        if ($null -ne $logWriter) {
            $logWriter.Flush()
            $logWriter.Dispose()
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
foreach ($campaignConfigPath in $CampaignConfigPathList) {
    $resolvedCampaignConfigPathList += Resolve-RepositoryRelativePath -InputPath $campaignConfigPath
}

$resolvedPlanningReportPath = Resolve-RepositoryRelativePath -InputPath $PlanningReportPath
$resolvedLauncherRelativePath = Resolve-RepositoryRelativePath -InputPath $LauncherRelativePath
$resolvedValidationOutputRoot = Resolve-RepositoryRelativePath -InputPath $ValidationOutputRoot
$resolvedValidationReportRoot = Resolve-RepositoryRelativePath -InputPath $ValidationReportRoot
$resolvedValidationReportCandidateRootList = @()
foreach ($candidateRoot in @(
        $resolvedValidationReportRoot
        "doc\reports\analysis\validation_checks"
        "doc\reports\analysis\validation_checks\track1\exact_paper"
    )) {
    if ($resolvedValidationReportCandidateRootList -notcontains $candidateRoot) {
        $resolvedValidationReportCandidateRootList += $candidateRoot
    }
}
$resolvedSourceSyncPathList = @()
foreach ($sourceSyncPath in $sourceSyncPathList) {
    $resolvedSourceSyncPathList += Resolve-RepositoryRelativePath -InputPath $sourceSyncPath
}
$optionalDependencySpecificationList = Get-OptionalExactPaperDependencySpecificationList `
    -RunNameList $RunNameList `
    -CampaignConfigPathList $resolvedCampaignConfigPathList `
    -LauncherRelativePath $resolvedLauncherRelativePath
$remoteRunNameLiteralListText = ($RunNameList | ForEach-Object { "'$_'" }) -join ",`n    "
$optionalDependencyLabelText = if ($optionalDependencySpecificationList.Count -gt 0) {
    ($optionalDependencySpecificationList | ForEach-Object { "$($_.family_name):$($_.package_name)" }) -join ", "
}
else {
    "none"
}
$remoteValidationReportRootLiteralListText = ($resolvedValidationReportCandidateRootList | ForEach-Object { "'$_'" }) -join ",`n    "

$runTimestamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$campaignSlug = Convert-ToSlug -RawText $campaignName
$runTrackingDirectory = Join-Path $projectRoot (Join-Path $remoteTrackingRoot "${runTimestamp}_${campaignSlug}")
$runLogPath = Resolve-WindowsRelativePath -BasePath $projectRoot -TargetPath (Join-Path $runTrackingDirectory "remote_training_campaign.log")
$initialRemoteRunLogPath = Join-Path $campaignLogRoot (([System.IO.Path]::GetFileNameWithoutExtension($resolvedCampaignConfigPathList[0])) + ".log")

New-Item -ItemType Directory -Force -Path $runTrackingDirectory | Out-Null

Write-Host "[INFO] Campaign Name | $campaignName" -ForegroundColor Cyan
Write-Host "[INFO] Planning Report | $planningReportPath" -ForegroundColor Cyan
Write-Host "[INFO] Campaign Output Root | $campaignOutputRoot" -ForegroundColor Cyan
Write-Host "[INFO] Exact-Paper Run Count | $($campaignConfigPathList.Count)" -ForegroundColor Cyan
Write-Host "[INFO] Remote Host Alias | $RemoteHostAlias" -ForegroundColor Cyan
Write-Host "[INFO] Remote Repository Path | $RemoteRepositoryPath" -ForegroundColor Cyan
Write-Host "[INFO] Remote Conda Environment | $RemoteCondaEnvironmentName" -ForegroundColor Cyan
Write-Host "[INFO] Optional Remote Dependencies | $optionalDependencyLabelText" -ForegroundColor Cyan

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
& $(New-RemoteCondaPythonCommandText -CondaEnvironmentName '$RemoteCondaEnvironmentName' -PythonInlineCode 'import sys; print(sys.version)')
"@

$remotePreflightScript += @"
if (`$LASTEXITCODE -ne 0) {
    exit `$LASTEXITCODE
}
"@

if ($optionalDependencySpecificationList.Count -gt 0) {
    foreach ($dependencySpecification in $optionalDependencySpecificationList) {
        $familyName = $dependencySpecification.family_name
        $packageName = $dependencySpecification.package_name
        $symbolName = $dependencySpecification.symbol_name
        $pythonDependencyCheck = @(
            "import importlib"
            "module = importlib.import_module('$packageName')"
            "getattr(module, '$symbolName')"
            "print('REMOTE_OPTIONAL_DEPENDENCY_OK::$packageName|$symbolName|$familyName')"
        ) -join "; "
        $remoteDependencyCheckCommandText = New-RemoteCondaPythonCommandText `
            -CondaEnvironmentName $RemoteCondaEnvironmentName `
            -PythonInlineCode $pythonDependencyCheck

        $remotePreflightScript += @"
Write-Output ('REMOTE_OPTIONAL_DEPENDENCY_CHECK::{0}|{1}|{2}' -f '$packageName', '$symbolName', '$familyName')
& $remoteDependencyCheckCommandText
if (`$LASTEXITCODE -ne 0) {
    throw 'Remote optional dependency preflight failed | package=$packageName | symbol=$symbolName | family=$familyName | conda_env=$RemoteCondaEnvironmentName'
}
"@
    }
}

$remotePreflightScript += @"
exit 0
"@

Write-StatusLine "INFO" "Running remote environment preflight"
$preflightResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remotePreflightScript) `
    -LogPath $runLogPath `
    -ProgressActivity "Remote exact-paper preflight"
if ([int]$preflightResult.exit_code -ne 0) {
    throw "Remote environment preflight failed | host=$RemoteHostAlias"
}

# Sync Local Workspace To Remote Repository
Write-StatusLine "STEP" "Syncing local repository state to remote workstation"
Invoke-RemoteTarExtract -RelativePathList $resolvedSourceSyncPathList -LogPath $runLogPath

$requiredRemoteSourcePathList = @(
    $resolvedCampaignConfigPathList + @(
        $resolvedPlanningReportPath
        $resolvedLauncherRelativePath
        "scripts\campaigns\track1\exact_paper\invoke_exact_paper_campaign_local.ps1"
        "scripts\campaigns\infrastructure\shared_streaming_campaign_launcher.ps1"
    )
)
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

function Emit-RemoteStatusLine {
    param(
        [string]`$LineText
    )

    Write-Output `$LineText
    [Console]::Out.Flush()
}

Emit-RemoteStatusLine ('REMOTE_RUN_START::{0}' -f (Get-Location).Path)

`$campaignName = '$campaignName'
`$planningReportPath = '$resolvedPlanningReportPath'
`$campaignOutputRoot = Join-Path 'output\training_campaigns' `$campaignName
`$campaignLogRoot = Join-Path `$campaignOutputRoot 'logs'
New-Item -ItemType Directory -Path `$campaignLogRoot -Force | Out-Null
Emit-RemoteStatusLine ('REMOTE_ACTIVE_STAGE::{0}' -f 'Initialized remote campaign log root')
Emit-RemoteStatusLine ('[INFO] Campaign Name | {0}' -f `$campaignName)
Emit-RemoteStatusLine ('[INFO] Planning Report | {0}' -f `$planningReportPath)
Emit-RemoteStatusLine ('[INFO] Campaign Output Root | {0}' -f `$campaignOutputRoot)

`$launcherPath = Join-Path '$remoteExecutionRoot' '$resolvedLauncherRelativePath'
if (-not (Test-Path -LiteralPath `$launcherPath)) {
    throw ('Remote exact-paper launcher missing | {0}' -f `$launcherPath)
}

Emit-RemoteStatusLine ('REMOTE_ACTIVE_STAGE::{0}' -f 'Launching canonical exact-paper campaign launcher')
& powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File `$launcherPath -CondaEnvironmentName '$RemoteCondaEnvironmentName'
`$nativeExitCode = if (`$LASTEXITCODE -eq `$null) { 0 } else { [int]`$LASTEXITCODE }

if (`$nativeExitCode -ne 0) {
    Emit-RemoteStatusLine ('REMOTE_RUN_EXIT_CODE::{0}' -f `$nativeExitCode)
    exit `$nativeExitCode
}

Emit-RemoteStatusLine ''
Emit-RemoteStatusLine ('[DONE] Exact-paper campaign completed successfully')
Emit-RemoteStatusLine ('[DONE] Campaign logs available under | {0}' -f `$campaignLogRoot)
Emit-RemoteStatusLine 'REMOTE_RUN_EXIT_CODE::0'

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
Emit-RemoteStatusLine ('REMOTE_SYNC_PATH::{0}' -f `$campaignOutputDirectory)

`$runNameList = @(
    $remoteRunNameLiteralListText
)

foreach (`$runName in `$runNameList) {
    `$validationDirectory = Get-ChildItem -LiteralPath '$resolvedValidationOutputRoot' -Directory |
        Where-Object { `$_.Name -like "*__`${runName}_campaign_run" } |
        Sort-Object LastWriteTime |
        Select-Object -Last 1

    if (`$null -eq `$validationDirectory) {
        throw ('Missing exact-paper validation directory for run | {0}' -f `$runName)
    }

    `$validationRelativePath = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$validationDirectory.FullName
    Emit-RemoteStatusLine ('REMOTE_SYNC_PATH::{0}' -f `$validationRelativePath)

    `$validationReportRootList = @(
        $remoteValidationReportRootLiteralListText
    )
    `$candidateReportFileList = @()
    foreach (`$validationReportRoot in `$validationReportRootList) {
        if (-not (Test-Path -LiteralPath `$validationReportRoot)) {
            continue
        }

        `$candidateReportFileList += Get-ChildItem -LiteralPath `$validationReportRoot -File |
            Where-Object { `$_.Name -like "*_`${runName}_campaign_run_exact_paper_model_bank_report.md" }
    }

    `$reportFile = `$candidateReportFileList |
        Sort-Object LastWriteTime |
        Select-Object -Last 1

    if (`$null -eq `$reportFile) {
        `$searchedRootText = (`$validationReportRootList -join '; ')
        throw ('Missing exact-paper validation report for run | {0} | searched_roots={1}' -f `$runName, `$searchedRootText)
    }

    `$reportRelativePath = Resolve-WindowsRelativePath -BasePath (Get-Location).Path -TargetPath `$reportFile.FullName
    Emit-RemoteStatusLine ('REMOTE_SYNC_PATH::{0}' -f `$reportRelativePath)
}

Emit-RemoteStatusLine 'REMOTE_RUN_MARKERS_EMITTED'
exit 0
"@

Write-StatusLine "STEP" "Launching remote exact-paper campaign"
$remoteRunResult = Invoke-RemotePowerShellScriptWithStreamingLog `
    -RemoteScriptText (New-RemoteMappedRepositoryScriptText -ScriptText $remoteRunScript) `
    -LogPath $runLogPath `
    -ProgressActivity "Remote exact-paper campaign" `
    -RemoteKillMatchPatternList @(
        "run_exact_paper_model_bank_validation.py"
        $campaignName
        ([System.IO.Path]::GetFileName($resolvedLauncherRelativePath))
    ) `
    -InitialConfigCount $resolvedCampaignConfigPathList.Count `
    -InitialConfigPath $resolvedCampaignConfigPathList[0] `
    -InitialLogPath $initialRemoteRunLogPath
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
Write-Host "[DONE] Remote exact-paper campaign completed successfully" -ForegroundColor Green
Write-Host "[DONE] Campaign logs available under | $campaignLogRoot" -ForegroundColor Green
Write-Host "[DONE] Remote wrapper log available under | $(Join-Path $projectRoot $runLogPath)" -ForegroundColor Green
exit 0
