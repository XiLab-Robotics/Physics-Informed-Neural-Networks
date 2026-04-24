param(
    [switch]$DirectOnRemote,
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" })
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..\.." )).Path
Set-Location $projectRoot

$campaignName = "track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43"
$familySpecificationList = @(
    @{ Name = "SVM"; CanonicalRuntimeName = "SVR"; Slug = "svm"; Expected = 180 }
    @{ Name = "MLP"; CanonicalRuntimeName = "MLP"; Slug = "mlp"; Expected = 60 }
    @{ Name = "ET"; CanonicalRuntimeName = "ET"; Slug = "et"; Expected = 60 }
    @{ Name = "ERT"; CanonicalRuntimeName = "ERT"; Slug = "ert"; Expected = 180 }
    @{ Name = "HGBM"; CanonicalRuntimeName = "HGBM"; Slug = "hgbm"; Expected = 60 }
    @{ Name = "XGBM"; CanonicalRuntimeName = "XGBM"; Slug = "xgbm"; Expected = 120 }
)

function Convert-ToPowerShellEncodedCommand {

    param(
        [string]$ScriptText
    )

    $unicodeBytes = [System.Text.Encoding]::Unicode.GetBytes($ScriptText)
    return [Convert]::ToBase64String($unicodeBytes)
}

function New-RemoteProgressCollectionScript {

    param(
        [string]$RepositoryRootPath
    )

    return @"
`$ErrorActionPreference = 'Stop'

`$campaignName = '$campaignName'
`$repositoryRootPath = '$RepositoryRootPath'
`$trainingCampaignRoot = Join-Path `$repositoryRootPath 'output\training_campaigns\track1\exact_paper\forward'
`$validationRoot = Join-Path `$repositoryRootPath 'output\validation_checks\paper_reimplementation_rcim_exact_model_bank\forward'
`$familySpecificationList = @(
    @{ Name = 'SVM'; CanonicalRuntimeName = 'SVR'; Slug = 'svm'; Expected = 180 }
    @{ Name = 'MLP'; CanonicalRuntimeName = 'MLP'; Slug = 'mlp'; Expected = 60 }
    @{ Name = 'ET'; CanonicalRuntimeName = 'ET'; Slug = 'et'; Expected = 60 }
    @{ Name = 'ERT'; CanonicalRuntimeName = 'ERT'; Slug = 'ert'; Expected = 180 }
    @{ Name = 'HGBM'; CanonicalRuntimeName = 'HGBM'; Slug = 'hgbm'; Expected = 60 }
    @{ Name = 'XGBM'; CanonicalRuntimeName = 'XGBM'; Slug = 'xgbm'; Expected = 120 }
)

function Write-MonitorLine {
    param([string]`$Text)
    Write-Output `$Text
}

Write-MonitorLine ('CAMPAIGN_NAME::{0}' -f `$campaignName)
Write-MonitorLine ('REPOSITORY_ROOT::{0}' -f `$repositoryRootPath)
Write-MonitorLine ('REMOTE_NOW::{0}' -f (Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))

foreach (`$familySpecification in `$familySpecificationList) {
    `$familyName = `$familySpecification.Name
    `$familySlug = `$familySpecification.Slug
    `$expectedCount = [int]`$familySpecification.Expected
    `$validationDirectoryList = @(
        Get-ChildItem `$validationRoot -Directory -Recurse -ErrorAction SilentlyContinue |
            Where-Object { `$_.Name -like ('*__track1_' + `$familySlug + '_*_yellow_cell_attempt_*_campaign_run') } |
            Sort-Object Name
    )
    `$distinctRunGroupList = @(
        `$validationDirectoryList |
            Group-Object { `$_.Name -replace '^[0-9-]+__', '' }
    )
    `$distinctCount = `$distinctRunGroupList.Count
    `$duplicateCount = (@(`$distinctRunGroupList | Where-Object { `$_.Count -gt 1 })).Count
    `$percentComplete = if (`$expectedCount -gt 0) {
        [Math]::Round((100.0 * `$distinctCount / `$expectedCount), 1)
    }
    else {
        0.0
    }

    Write-MonitorLine ('FAMILY_PROGRESS::{0}::{1}::{2}::{3}::{4}' -f `$familyName, `$distinctCount, `$expectedCount, `$percentComplete, `$duplicateCount)

    if (`$validationDirectoryList.Count -gt 0) {
        `$latestValidationDirectory = `$validationDirectoryList[-1]
        Write-MonitorLine ('FAMILY_LATEST_VALIDATION::{0}::{1}::{2}' -f `$familyName, `$latestValidationDirectory.Name, `$latestValidationDirectory.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss'))
    }
}

`$currentWaveValidationDirectoryList = @(
    Get-ChildItem `$validationRoot -Directory -Recurse -ErrorAction SilentlyContinue |
        Where-Object { `$_.Name -like '*__track1_*_yellow_cell_attempt_*_campaign_run' } |
        Sort-Object LastWriteTime
)
`$totalExpectedCount = 0
foreach (`$familySpecification in `$familySpecificationList) {
    `$totalExpectedCount += [int]`$familySpecification.Expected
}
`$totalDistinctCount = (
    @(
        `$currentWaveValidationDirectoryList |
            Group-Object { `$_.Name -replace '^[0-9-]+__', '' }
    ).Count
)
`$totalPercentComplete = [Math]::Round((100.0 * `$totalDistinctCount / `$totalExpectedCount), 1)
Write-MonitorLine ('TOTAL_PROGRESS::{0}::{1}::{2}' -f `$totalDistinctCount, `$totalExpectedCount, `$totalPercentComplete)

if (`$currentWaveValidationDirectoryList.Count -gt 0) {
    `$latestWaveValidationDirectory = `$currentWaveValidationDirectoryList[-1]
    Write-MonitorLine ('LATEST_WAVE_VALIDATION::{0}::{1}' -f `$latestWaveValidationDirectory.Name, `$latestWaveValidationDirectory.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss'))
}

`$campaignLogFileList = @()
foreach (`$familySpecification in `$familySpecificationList) {
    `$familyCampaignName = 'track1_' + `$familySpecification.Slug + '_remaining_yellow_cell_campaign_2026_04_22_01_40_43'
    `$familyCampaignDirectory = Get-ChildItem `$trainingCampaignRoot -Directory -Recurse -ErrorAction SilentlyContinue |
        Where-Object { `$_.Name -eq `$familyCampaignName } |
        Select-Object -First 1
    if (`$null -ne `$familyCampaignDirectory) {
        `$logRoot = Join-Path `$familyCampaignDirectory.FullName 'logs'
        if (Test-Path -LiteralPath `$logRoot) {
            `$campaignLogFileList += Get-ChildItem `$logRoot -File -ErrorAction SilentlyContinue
        }
    }
}
`$campaignLogFileList = @(`$campaignLogFileList | Sort-Object LastWriteTime)
if (`$campaignLogFileList.Count -gt 0) {
    `$latestCampaignLog = `$campaignLogFileList[-1]
    Write-MonitorLine ('LATEST_CAMPAIGN_LOG::{0}::{1}::{2}' -f `$latestCampaignLog.FullName, `$latestCampaignLog.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss'), `$latestCampaignLog.Length)
}

`$activeProcessList = @(
    Get-CimInstance Win32_Process |
        Where-Object {
            (`$_.Name -match 'python|conda|powershell') -and
            (`$_.CommandLine -match 'run_exact_paper_model_bank_validation|remaining_yellow_cell|track1_svm|track1_mlp|track1_et|track1_ert|track1_hgbm|track1_xgbm')
        } |
        Sort-Object CreationDate
)
Write-MonitorLine ('ACTIVE_PROCESS_COUNT::{0}' -f `$activeProcessList.Count)
foreach (`$processEntry in `$activeProcessList) {
    `$commandLine = [string]`$processEntry.CommandLine
    if (`$commandLine.Length -gt 500) {
        `$commandLine = `$commandLine.Substring(0, 500)
    }
    Write-MonitorLine ('ACTIVE_PROCESS::{0}::{1}::{2}::{3}' -f `$processEntry.ProcessId, `$processEntry.Name, `$processEntry.CreationDate, `$commandLine)
}

`$activeValidationProcess = `$activeProcessList |
    Where-Object { [string]`$_.CommandLine -match '--config-path' } |
    Select-Object -Last 1
if (`$null -ne `$activeValidationProcess) {
    `$activeCommandLine = [string]`$activeValidationProcess.CommandLine
    `$activeConfigPath = [regex]::Match(`$activeCommandLine, '--config-path\s+([^\s]+)').Groups[1].Value
    if (-not [string]::IsNullOrWhiteSpace(`$activeConfigPath)) {
        Write-MonitorLine ('ACTIVE_CONFIG::{0}' -f `$activeConfigPath)
        `$activeLogName = [System.IO.Path]::GetFileNameWithoutExtension(`$activeConfigPath) + '.log'
        foreach (`$familySpecification in `$familySpecificationList) {
            `$familyCampaignName = 'track1_' + `$familySpecification.Slug + '_remaining_yellow_cell_campaign_2026_04_22_01_40_43'
            `$familyCampaignDirectory = Get-ChildItem `$trainingCampaignRoot -Directory -Recurse -ErrorAction SilentlyContinue |
                Where-Object { `$_.Name -eq `$familyCampaignName } |
                Select-Object -First 1
            if (`$null -eq `$familyCampaignDirectory) {
                continue
            }

            `$candidateLogPath = Join-Path `$familyCampaignDirectory.FullName ('logs\' + `$activeLogName)
            if (Test-Path -LiteralPath `$candidateLogPath) {
                `$activeLogFile = Get-Item -LiteralPath `$candidateLogPath
                Write-MonitorLine ('ACTIVE_LOG::{0}::{1}::{2}' -f `$activeLogFile.FullName, `$activeLogFile.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss'), `$activeLogFile.Length)
                break
            }
        }
    }
}
"@
}

function Get-Track1RemainingYellowCellProgressRawLineList {

    param(
        [switch]$UseDirectOnRemote,
        [string]$RemoteAlias,
        [string]$RepositoryRootPath
    )

    $statusScript = New-RemoteProgressCollectionScript -RepositoryRootPath $RepositoryRootPath

    if ($UseDirectOnRemote) {
        $temporaryScriptPath = Join-Path $env:TEMP ("track1_remaining_yellow_monitor_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
        try {
            [System.IO.File]::WriteAllText($temporaryScriptPath, $statusScript, [System.Text.ASCIIEncoding]::new())
            return @(powershell.exe -NoProfile -ExecutionPolicy Bypass -File $temporaryScriptPath)
        }
        finally {
            if (Test-Path -LiteralPath $temporaryScriptPath) {
                Remove-Item -LiteralPath $temporaryScriptPath -Force -ErrorAction SilentlyContinue
            }
        }
    }

    $localTemporaryScriptPath = Join-Path $env:TEMP ("track1_remaining_yellow_monitor_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteTemporaryDirectoryPath = "C:\Temp"
    $remoteTemporaryScriptPath = Join-Path $remoteTemporaryDirectoryPath ("track1_remaining_yellow_monitor_{0}.ps1" -f ([guid]::NewGuid().ToString("N")))
    $remoteScpScriptPath = "/" + $remoteTemporaryScriptPath.Replace("\", "/")

    try {
        [System.IO.File]::WriteAllText($localTemporaryScriptPath, $statusScript, [System.Text.ASCIIEncoding]::new())
        & ssh $RemoteAlias ('if not exist "{0}" mkdir "{0}"' -f $remoteTemporaryDirectoryPath) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script directory prepare failed | host=$RemoteAlias | path=$remoteTemporaryDirectoryPath"
        }

        & scp $localTemporaryScriptPath ('{0}:{1}' -f $RemoteAlias, $remoteScpScriptPath) | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Remote temporary script upload failed | host=$RemoteAlias | path=$remoteTemporaryScriptPath"
        }

        return @(
            & ssh $RemoteAlias "powershell -NoProfile -ExecutionPolicy Bypass -File `"$remoteTemporaryScriptPath`""
        )
    }
    finally {
        if (Test-Path -LiteralPath $localTemporaryScriptPath) {
            Remove-Item -LiteralPath $localTemporaryScriptPath -Force -ErrorAction SilentlyContinue
        }

        & ssh $RemoteAlias ('if exist "{0}" del /f /q "{0}"' -f $remoteTemporaryScriptPath) | Out-Null
    }
}

function Get-LastMatchingLine {

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

function Remove-LinePrefix {

    param(
        [string]$LineText,
        [string]$Prefix
    )

    if ($null -eq $LineText) {
        return $null
    }

    return ($LineText -replace ('^' + [regex]::Escape($Prefix)), '')
}

$rawLineList = Get-Track1RemainingYellowCellProgressRawLineList `
    -UseDirectOnRemote:$DirectOnRemote `
    -RemoteAlias $RemoteHostAlias `
    -RepositoryRootPath $RemoteRepositoryPath

$repositoryRootLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "REPOSITORY_ROOT::"
$remoteNowLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "REMOTE_NOW::"
$totalProgressLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "TOTAL_PROGRESS::"
$latestValidationLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "LATEST_WAVE_VALIDATION::"
$latestLogLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "LATEST_CAMPAIGN_LOG::"
$activeProcessCountLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "ACTIVE_PROCESS_COUNT::"
$activeConfigLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "ACTIVE_CONFIG::"
$activeLogLine = Get-LastMatchingLine -LineList $rawLineList -Prefix "ACTIVE_LOG::"

Write-Host ""
Write-Host ("=" * 96) -ForegroundColor DarkCyan
Write-Host "[INFO] Track 1 Remaining Yellow-Cell Campaign Progress Monitor" -ForegroundColor Cyan
Write-Host ("=" * 96) -ForegroundColor DarkCyan
Write-Host "[INFO] Mode | $(if ($DirectOnRemote) { 'direct_on_remote' } else { 'ssh_remote' })" -ForegroundColor Cyan
Write-Host "[INFO] Remote Host Alias | $RemoteHostAlias" -ForegroundColor Cyan

if ($null -ne $repositoryRootLine) {
    $repositoryRootPath = Remove-LinePrefix -LineText $repositoryRootLine -Prefix "REPOSITORY_ROOT::"
    Write-Host "[INFO] Repository Root | $repositoryRootPath" -ForegroundColor Cyan
}

if ($null -ne $remoteNowLine) {
    $remoteTimestamp = Remove-LinePrefix -LineText $remoteNowLine -Prefix "REMOTE_NOW::"
    Write-Host "[INFO] Remote Time | $remoteTimestamp" -ForegroundColor Cyan
}

if ($null -ne $totalProgressLine) {
    $totalProgressParts = (Remove-LinePrefix -LineText $totalProgressLine -Prefix "TOTAL_PROGRESS::") -split "::"
    Write-Host "[INFO] Total Progress | $($totalProgressParts[0]) / $($totalProgressParts[1]) | $($totalProgressParts[2])%" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "**Family Progress**"

$familyProgressRowList = foreach ($familySpecification in $familySpecificationList) {
    $familyProgressLine = Get-LastMatchingLine -LineList $rawLineList -Prefix ("FAMILY_PROGRESS::{0}::" -f $familySpecification.Name)
    $familyLatestLine = Get-LastMatchingLine -LineList $rawLineList -Prefix ("FAMILY_LATEST_VALIDATION::{0}::" -f $familySpecification.Name)

    if ($null -eq $familyProgressLine) {
        continue
    }

    $familyProgressParts = (Remove-LinePrefix -LineText $familyProgressLine -Prefix ("FAMILY_PROGRESS::{0}::" -f $familySpecification.Name)) -split "::"
    $latestValidationName = "-"
    $latestValidationTime = "-"
    if ($null -ne $familyLatestLine) {
        $familyLatestParts = (Remove-LinePrefix -LineText $familyLatestLine -Prefix ("FAMILY_LATEST_VALIDATION::{0}::" -f $familySpecification.Name)) -split "::"
        $latestValidationName = $familyLatestParts[0]
        $latestValidationTime = $familyLatestParts[1]
    }

    [PSCustomObject]@{
        Family = $familySpecification.Name
        Done = [int]$familyProgressParts[0]
        Expected = [int]$familyProgressParts[1]
        Percent = [double]$familyProgressParts[2]
        DuplicateRunNames = [int]$familyProgressParts[3]
        LatestValidation = $latestValidationName
        LatestUpdate = $latestValidationTime
    }
}

$familyProgressRowList | Format-Table -AutoSize

Write-Host ""
Write-Host "**Active State**"

if ($null -ne $activeProcessCountLine) {
    $activeProcessCount = Remove-LinePrefix -LineText $activeProcessCountLine -Prefix "ACTIVE_PROCESS_COUNT::"
    Write-Host ('- active matching processes: `{0}`' -f $activeProcessCount)
}

if ($null -ne $activeConfigLine) {
    $activeConfigPath = Remove-LinePrefix -LineText $activeConfigLine -Prefix "ACTIVE_CONFIG::"
    Write-Host ('- active config: `{0}`' -f $activeConfigPath)
}
else {
    Write-Host '- active config: `none_detected`'
}

if ($null -ne $activeLogLine) {
    $activeLogParts = (Remove-LinePrefix -LineText $activeLogLine -Prefix "ACTIVE_LOG::") -split "::"
    Write-Host ('- active log: `{0}`' -f $activeLogParts[0])
    Write-Host ('- active log update: `{0}`' -f $activeLogParts[1])
    Write-Host ('- active log size: `{0}` bytes' -f $activeLogParts[2])
}

if ($null -ne $latestValidationLine) {
    $latestValidationParts = (Remove-LinePrefix -LineText $latestValidationLine -Prefix "LATEST_WAVE_VALIDATION::") -split "::"
    Write-Host ('- latest validation dir: `{0}`' -f $latestValidationParts[0])
    Write-Host ('- latest validation update: `{0}`' -f $latestValidationParts[1])
}

if ($null -ne $latestLogLine) {
    $latestLogParts = (Remove-LinePrefix -LineText $latestLogLine -Prefix "LATEST_CAMPAIGN_LOG::") -split "::"
    Write-Host ('- latest campaign log: `{0}`' -f $latestLogParts[0])
    Write-Host ('- latest campaign log update: `{0}`' -f $latestLogParts[1])
    Write-Host ('- latest campaign log size: `{0}` bytes' -f $latestLogParts[2])
}

$duplicateFamilyRowList = @($familyProgressRowList | Where-Object { $_.DuplicateRunNames -gt 0 })
if ($duplicateFamilyRowList.Count -gt 0) {
    Write-Host ""
    Write-Host "**Warnings**"
    foreach ($duplicateFamilyRow in $duplicateFamilyRowList) {
        Write-Host ('- `{0}` duplicate run-name groups detected: `{1}`' -f $duplicateFamilyRow.Family, $duplicateFamilyRow.DuplicateRunNames) -ForegroundColor Yellow
    }
}
