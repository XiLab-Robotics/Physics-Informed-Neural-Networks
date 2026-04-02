param(
    [string]$PythonExecutable = "python",
    [string]$LanAiBaseUrl = $env:STANDARDML_LAN_AI_BASE_URL,
    [string]$LmStudioBaseUrl = $env:LM_STUDIO_BASE_URL,
    [string]$TranscriptModel = "large-v3",
    [string]$CleanupModel = "openai/gpt-oss-20b",
    [string]$ReportModel = "openai/gpt-oss-20b",
    [string[]]$VideoNameList = @()
)

$ErrorActionPreference = "Stop"

$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$analysisRootRelativePath = ".temp\video_guides\_analysis_hq_remote_gptoss_tracked"
$reportRootRelativePath = ".temp\video_guides\_remote_gptoss_tracked_reports"
$logRootRelativePath = ".temp\video_guides\_remote_gptoss_tracked_logs"
$videoSourceRootRelativePath = ".temp\video_guides"
$statusFileRelativePath = "doc\running\remote_high_quality_video_rerun_status.json"
$checklistFileRelativePath = "doc\running\remote_high_quality_video_rerun_checklist.md"
$validationScriptRelativePath = "scripts\tooling\markdown\markdown_style_check.py"
$workflowScriptRelativePath = "scripts\tooling\video_guides\extract_video_guide_knowledge.py"

$analysisRootPath = Join-Path $projectRoot $analysisRootRelativePath
$reportRootPath = Join-Path $projectRoot $reportRootRelativePath
$logRootPath = Join-Path $projectRoot $logRootRelativePath
$videoSourceRootPath = Join-Path $projectRoot $videoSourceRootRelativePath
$statusFilePath = Join-Path $projectRoot $statusFileRelativePath
$checklistFilePath = Join-Path $projectRoot $checklistFileRelativePath

New-Item -ItemType Directory -Force -Path $analysisRootPath | Out-Null
New-Item -ItemType Directory -Force -Path $reportRootPath | Out-Null
New-Item -ItemType Directory -Force -Path $logRootPath | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $statusFilePath) | Out-Null

function Write-StatusLine {

    param(
        [string]$Label,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Label] $Message"
}

function Convert-ToVideoSlug {

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

function Get-DefaultVideoNameList {

    $supportedExtensionList = @(".mp4", ".mkv", ".mov", ".avi", ".m4v")

    $videoFileList = Get-ChildItem -LiteralPath $videoSourceRootPath -File |
        Where-Object { $supportedExtensionList -contains $_.Extension.ToLowerInvariant() } |
        Sort-Object Name

    return @($videoFileList | ForEach-Object { $_.BaseName })
}

function Get-VideoStageState {

    param(
        [string]$VideoName
    )

    $videoSlug = Convert-ToVideoSlug $VideoName
    $analysisDirectoryPath = Join-Path $analysisRootPath $videoSlug
    $reportDirectoryPath = Join-Path $reportRootPath $videoSlug
    $assetDirectoryPath = Join-Path $reportDirectoryPath "assets"

    $rawTranscriptPath = Join-Path $analysisDirectoryPath "raw_full_transcript.txt"
    $cleanupCachePath = Join-Path $analysisDirectoryPath "corrected_transcript_cache.json"
    $snapshotRecordPath = Join-Path $analysisDirectoryPath "snapshot_records.json"
    $transcriptMarkdownPath = Join-Path $reportDirectoryPath "${videoSlug}_transcript.md"
    $reportMarkdownPath = Join-Path $reportDirectoryPath "${videoSlug}_report.md"
    $videoLogPath = Join-Path $logRootPath ("{0}.log" -f $videoSlug)

    $transcriptExtracted = (Test-Path -LiteralPath $rawTranscriptPath)
    $cleanupCompleted = (Test-Path -LiteralPath $cleanupCachePath)
    $snapshotsSelected = (Test-Path -LiteralPath $snapshotRecordPath)
    $ocrCompleted = (Test-Path -LiteralPath $assetDirectoryPath) -and ((Get-ChildItem -LiteralPath $assetDirectoryPath -Filter "*.png" -ErrorAction SilentlyContinue).Count -gt 0)
    $transcriptSaved = (Test-Path -LiteralPath $transcriptMarkdownPath)
    $reportSaved = (Test-Path -LiteralPath $reportMarkdownPath)

    $validationCompleted = $false
    if ($transcriptSaved -and $reportSaved) {
        & $PythonExecutable -B $validationScriptRelativePath $transcriptMarkdownPath $reportMarkdownPath *> $null
        $validationCompleted = ($LASTEXITCODE -eq 0)
    }

    $overallStatus = "pending"
    if ($validationCompleted) {
        $overallStatus = "completed"
    }
    elseif ($reportSaved) {
        $overallStatus = "report_pending_validation"
    }
    elseif ($transcriptSaved -or $snapshotsSelected -or $cleanupCompleted -or $transcriptExtracted) {
        $overallStatus = "partial"
    }

    return [ordered]@{
        video_name = $VideoName
        video_slug = $videoSlug
        transcript_extracted = $transcriptExtracted
        cleanup_completed = $cleanupCompleted
        snapshots_selected = $snapshotsSelected
        ocr_completed = $ocrCompleted
        transcript_saved = $transcriptSaved
        report_saved = $reportSaved
        validation_completed = $validationCompleted
        overall_status = $overallStatus
        analysis_directory = $analysisDirectoryPath
        report_directory = $reportDirectoryPath
        log_path = $videoLogPath
    }
}

function Write-RunState {

    param(
        [string]$RunStatus,
        [string]$CurrentVideoName,
        [int]$CurrentVideoIndex,
        [hashtable[]]$VideoStateList,
        [string]$LastFailureMessage = ""
    )

    $statusMap = [ordered]@{
        run_status = $RunStatus
        current_video_name = $CurrentVideoName
        current_video_index = $CurrentVideoIndex
        lan_ai_base_url = $LanAiBaseUrl
        lm_studio_base_url = $LmStudioBaseUrl
        transcript_model = $TranscriptModel
        cleanup_model = $CleanupModel
        report_model = $ReportModel
        analysis_root = $analysisRootRelativePath
        report_root = $reportRootRelativePath
        log_root = $logRootRelativePath
        last_failure_message = $LastFailureMessage
        updated_at = (Get-Date).ToString("o")
        video_state_list = $VideoStateList
    }

    $statusJson = $statusMap | ConvertTo-Json -Depth 6
    Set-Content -LiteralPath $statusFilePath -Value $statusJson -Encoding UTF8

    $checklistLineList = @(
        "# Remote High-Quality Video Rerun Checklist",
        "",
        "- Run status: $RunStatus",
        "- Current video: $CurrentVideoName",
        "- Current index: $CurrentVideoIndex",
        "- LAN AI base URL: $LanAiBaseUrl",
        "- LM Studio base URL: $LmStudioBaseUrl",
        "- Transcript model: $TranscriptModel",
        "- Cleanup model: $CleanupModel",
        "- Report model: $ReportModel",
        "- Updated at: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
        ""
    )

    if ($LastFailureMessage) {
        $checklistLineList += @(
            "## Last Failure",
            "",
            $LastFailureMessage,
            ""
        )
    }

    $checklistLineList += @(
        "## Per-Video Status",
        ""
    )

    foreach ($videoState in $VideoStateList) {
        $checklistLineList += @(
            "### $($videoState.video_name)",
            "",
            "- Overall status: $($videoState.overall_status)",
            "- [$(if ($videoState.transcript_extracted) { 'x' } else { ' ' })] Transcript extracted",
            "- [$(if ($videoState.cleanup_completed) { 'x' } else { ' ' })] Cleanup completed",
            "- [$(if ($videoState.snapshots_selected) { 'x' } else { ' ' })] Snapshots selected",
            "- [$(if ($videoState.ocr_completed) { 'x' } else { ' ' })] OCR evidence copied",
            "- [$(if ($videoState.transcript_saved) { 'x' } else { ' ' })] Transcript markdown saved",
            "- [$(if ($videoState.report_saved) { 'x' } else { ' ' })] Report markdown saved",
            "- [$(if ($videoState.validation_completed) { 'x' } else { ' ' })] Markdown validation completed",
            "- Log: $(Resolve-Path -LiteralPath $videoState.log_path -ErrorAction SilentlyContinue | ForEach-Object { $_.Path })",
            ""
        )
    }

    Set-Content -LiteralPath $checklistFilePath -Value (($checklistLineList -join "`n").TrimEnd() + "`n") -Encoding UTF8
}

function Assert-RemoteRuntime {

    Write-StatusLine "INFO" "Checking remote LAN AI node reachability"
    $lanHealthUrl = "$LanAiBaseUrl/health"
    $lanHealthHeaders = @{ Authorization = "Bearer $env:STANDARDML_LAN_AI_TOKEN" }
    $lanHealthResponse = Invoke-RestMethod -Uri $lanHealthUrl -Headers $lanHealthHeaders -Method Get -TimeoutSec 30

    Write-StatusLine "INFO" ("LAN node ok | whisper={0} | device={1} | compute={2}" -f $lanHealthResponse.default_whisper_model, $lanHealthResponse.default_whisper_device, $lanHealthResponse.default_whisper_compute_type)

    Write-StatusLine "INFO" "Checking remote LM Studio model inventory"
    $lmStudioModelsUrl = "$LmStudioBaseUrl/v1/models"
    $lmStudioHeaders = @{ Authorization = "Bearer $env:LM_STUDIO_API_KEY" }
    $lmStudioModelResponse = Invoke-RestMethod -Uri $lmStudioModelsUrl -Headers $lmStudioHeaders -Method Get -TimeoutSec 30
    $loadedModelIdList = @($lmStudioModelResponse.data | ForEach-Object { $_.id })

    if (-not ($loadedModelIdList -contains $CleanupModel)) {
        throw "Requested cleanup/report model is not loaded in remote LM Studio | model=$CleanupModel"
    }

    Write-StatusLine "INFO" ("Remote LM Studio models | {0}" -f ($loadedModelIdList -join ", "))
}

Assert-RemoteRuntime

if ($VideoNameList.Count -eq 0) {
    $VideoNameList = Get-DefaultVideoNameList
}

if ($VideoNameList.Count -eq 0) {
    throw "No supported video files were found under $videoSourceRootRelativePath"
}

Write-StatusLine "INFO" ("Tracked video set | {0}" -f ($VideoNameList -join ", "))

$videoStateList = @($VideoNameList | ForEach-Object { Get-VideoStageState -VideoName $_ })
Write-RunState -RunStatus "running" -CurrentVideoName "" -CurrentVideoIndex 0 -VideoStateList $videoStateList

for ($videoIndex = 0; $videoIndex -lt $VideoNameList.Count; $videoIndex++) {
    $videoName = $VideoNameList[$videoIndex]
    $videoState = Get-VideoStageState -VideoName $videoName

    if ($videoState.validation_completed) {
        Write-StatusLine "DONE" "Skipping completed video | $videoName"
        $videoStateList = @($VideoNameList | ForEach-Object { Get-VideoStageState -VideoName $_ })
        Write-RunState -RunStatus "running" -CurrentVideoName $videoName -CurrentVideoIndex ($videoIndex + 1) -VideoStateList $videoStateList
        continue
    }

    $videoLogPath = $videoState.log_path
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $videoLogPath) | Out-Null

    Write-StatusLine "STEP" ("Processing video {0}/{1} | {2}" -f ($videoIndex + 1), $VideoNameList.Count, $videoName)
    Write-RunState -RunStatus "running" -CurrentVideoName $videoName -CurrentVideoIndex ($videoIndex + 1) -VideoStateList @($VideoNameList | ForEach-Object { Get-VideoStageState -VideoName $_ })

    $argumentList = @(
        "-B",
        $workflowScriptRelativePath,
        "--video-filter", $videoName,
        "--limit-videos", "1",
        "--analysis-root", $analysisRootRelativePath,
        "--report-root", $reportRootRelativePath,
        "--transcript-provider", "lan",
        "--cleanup-provider", "lmstudio",
        "--report-provider", "lmstudio",
        "--ocr-provider", "local",
        "--transcript-model", $TranscriptModel,
        "--cleanup-model", $CleanupModel,
        "--report-model", $ReportModel,
        "--lan-ai-base-url", $LanAiBaseUrl,
        "--lm-studio-base-url", $LmStudioBaseUrl,
        "--lmstudio-max-report-chunk-characters", "220"
    )

    & $PythonExecutable @argumentList 2>&1 | Tee-Object -FilePath $videoLogPath
    $videoExitCode = $LASTEXITCODE

    $videoStateList = @($VideoNameList | ForEach-Object { Get-VideoStageState -VideoName $_ })
    $refreshedVideoState = $videoStateList[$videoIndex]

    if ($videoExitCode -ne 0) {
        $failureMessage = "Video failed | name=$videoName | exit_code=$videoExitCode | log=$videoLogPath"
        Write-StatusLine "FAIL" $failureMessage
        Write-RunState -RunStatus "failed" -CurrentVideoName $videoName -CurrentVideoIndex ($videoIndex + 1) -VideoStateList $videoStateList -LastFailureMessage $failureMessage
        exit $videoExitCode
    }

    if (-not $refreshedVideoState.validation_completed) {
        $failureMessage = "Video finished without complete validated artifacts | name=$videoName | log=$videoLogPath"
        Write-StatusLine "FAIL" $failureMessage
        Write-RunState -RunStatus "failed" -CurrentVideoName $videoName -CurrentVideoIndex ($videoIndex + 1) -VideoStateList $videoStateList -LastFailureMessage $failureMessage
        exit 1
    }

    Write-StatusLine "DONE" "Completed video | $videoName"
    Write-RunState -RunStatus "running" -CurrentVideoName $videoName -CurrentVideoIndex ($videoIndex + 1) -VideoStateList $videoStateList
}

$videoStateList = @($VideoNameList | ForEach-Object { Get-VideoStageState -VideoName $_ })
Write-RunState -RunStatus "completed" -CurrentVideoName "" -CurrentVideoIndex $VideoNameList.Count -VideoStateList $videoStateList
Write-StatusLine "DONE" "Remote high-quality video rerun completed"
exit 0
