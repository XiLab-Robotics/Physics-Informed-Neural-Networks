param(
    [switch]$Remote,
    [switch]$PreflightOnly,
    [string]$CondaEnvironmentName = "pinns_env",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks",
    [string]$RemoteCondaEnvironmentName = "pinns_env",
    [string]$OutputSuffix = "shape_first_distillation_bounded_track2_screen_polished_setpoints_fw",
    [string]$ReportDate = "2026-07-22"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$ConfigPath = "config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/shape_first_distillation_bounded_track2_screen_polished_setpoints_fw_matrix.yaml"
$MatrixRunnerPath = "scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py"
$RerankerRunnerPath = "scripts/reports/analysis/build_shape_gated_te_curve_reranker.py"
$PlotBuilderRunnerPath = "scripts/reports/analysis/build_track2_candidate_curve_plots.py"
$ActiveStatePath = "doc/running/active_training_campaign.yaml"
$RunStamp = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
$LogRoot = Join-Path $RepositoryRoot ("output/validation_checks/track2_operator_launch_logs/{0}_{1}" -f $RunStamp, $OutputSuffix)
$PlotReportRoot = "doc/reports/campaign_results/track_2/verification_plots/shape_first_distillation_bounded_track2_screen_polished_setpoints_fw"
$RerankerReportRoot = "doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[$ReportDate]"
$ActiveFamilyList = @(
    "periodic_gru_sequence",
    "periodic_mlp_harmonic",
    "shape_first_distilled_periodic_gru_sequence_fw",
    "shape_first_distilled_periodic_mlp_harmonic_fw"
)

function Write-PlainOutputLine {
    param([string]$Message)

    [Console]::Out.WriteLine($Message)
}

function Write-WrappedOutputLine {
    param([string]$Message)

    $maximumLineLength = 160
    if ($Message.Length -le $maximumLineLength) {
        Write-PlainOutputLine $Message
        return
    }

    $remainingText = $Message
    $linePrefix = ""
    while ($remainingText.Length -gt $maximumLineLength) {
        $splitIndex = $remainingText.LastIndexOfAny(@(" ", "|", "\", "/"), $maximumLineLength)
        if ($splitIndex -lt 80) {
            $splitIndex = $maximumLineLength
        }
        Write-PlainOutputLine ("{0}{1}" -f $linePrefix, $remainingText.Substring(0, $splitIndex).TrimEnd())
        $remainingText = $remainingText.Substring($splitIndex).TrimStart(" ", "|", "\", "/")
        $linePrefix = "      "
    }
    if ($remainingText.Length -gt 0) {
        Write-PlainOutputLine ("{0}{1}" -f $linePrefix, $remainingText)
    }
}

function Write-LogLine {
    param(
        [string]$Level,
        [string]$Message
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-WrappedOutputLine ("[{0}] [{1}] {2}" -f $timestamp, $Level, $Message)
}

function Assert-RelativePathExists {
    param([string]$RelativePath)

    $resolvedPath = Join-Path $RepositoryRoot $RelativePath
    if (-not (Test-Path -LiteralPath $resolvedPath)) {
        throw "Required path is missing: $RelativePath"
    }
}

function Format-CommandArgument {
    param([string]$Argument)

    if ($Argument -match "\s") {
        return '"' + ($Argument -replace '"', '\"') + '"'
    }
    return $Argument
}

function Join-CommandLine {
    param([string[]]$ArgumentList)

    return (($ArgumentList | ForEach-Object { Format-CommandArgument $_ }) -join " ")
}

function Write-CommandPreview {
    param(
        [string]$CommandName,
        [string[]]$ArgumentList
    )

    Write-LogLine "CMD" $CommandName
    $currentLine = "    conda"
    foreach ($argument in $ArgumentList) {
        $formattedArgument = Format-CommandArgument $argument
        if (($currentLine.Length + 1 + $formattedArgument.Length) -gt 118) {
            Write-PlainOutputLine $currentLine
            $currentLine = "      $formattedArgument"
        }
        else {
            $currentLine = "$currentLine $formattedArgument"
        }
    }
    Write-PlainOutputLine $currentLine
}

function New-MatrixArgumentList {
    return @(
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
}

function New-RerankerArgumentList {
    $argumentList = @(
        "-B",
        $RerankerRunnerPath,
        "--config-path",
        $ConfigPath,
        "--dataset",
        "polished_dataset",
        "--surface-scope",
        "forward",
        "--report-date",
        $ReportDate
    )

    foreach ($activeFamily in $ActiveFamilyList) {
        $argumentList += @("--active-family", $activeFamily)
    }

    return $argumentList
}

function New-PlotArgumentList {
    return @(
        "-B",
        $PlotBuilderRunnerPath,
        "--config-path",
        $ConfigPath,
        "--output-root",
        $PlotReportRoot,
        "--dataset",
        "polished_dataset",
        "--surface-scope",
        "forward",
        "--max-plots-per-candidate",
        "2",
        "--windows"
    )
}

function Test-SuppressedOutputLine {
    param([string]$OutputLine)

    if ([string]::IsNullOrWhiteSpace($OutputLine)) {
        return $true
    }
    if ($OutputLine -eq "System.Management.Automation.RemoteException") {
        return $true
    }
    if ($OutputLine -match "^TE matrix candidates:\s+\d+%.*\|.*\[[^\]]+\]") {
        return $true
    }
    return $false
}

function Invoke-LoggedCondaPython {
    param(
        [string]$StepName,
        [string[]]$PythonArgumentList
    )

    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $logPath = Join-Path $LogRoot ("{0}.log" -f $StepName)
    $condaArgumentList = @("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + $PythonArgumentList
    Write-LogLine "STEP" ("Running {0}" -f $StepName)
    Write-CommandPreview $StepName $condaArgumentList

    Push-Location $RepositoryRoot
    try {
        if (Test-Path -LiteralPath $logPath) {
            Remove-Item -LiteralPath $logPath -Force
        }
        $previousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        try {
            & conda @condaArgumentList 2>&1 | ForEach-Object {
                $outputLine = $_.ToString()
                if (-not (Test-SuppressedOutputLine -OutputLine $outputLine)) {
                    Write-WrappedOutputLine $outputLine
                    Add-Content -LiteralPath $logPath -Value $outputLine
                }
            }
            $condaExitCode = $LASTEXITCODE
        }
        finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }
        if ($condaExitCode -ne 0) {
            throw "$StepName failed with exit code $condaExitCode. See $logPath"
        }
    }
    finally {
        Pop-Location
    }
}

function Repair-TextArtifactWhitespace {
    param([string[]]$RelativeRootPathList)

    foreach ($relativeRootPath in $RelativeRootPathList) {
        $resolvedRootPath = Join-Path $RepositoryRoot $relativeRootPath
        if (-not (Test-Path -LiteralPath $resolvedRootPath)) {
            continue
        }

        $textArtifactList = Get-ChildItem -LiteralPath $resolvedRootPath -Recurse -File |
            Where-Object { $_.Extension -in @(".csv", ".log", ".md", ".txt", ".yaml", ".yml") }

        foreach ($textArtifact in $textArtifactList) {
            $originalText = [System.IO.File]::ReadAllText($textArtifact.FullName)
            $normalizedText = $originalText.Replace("`r`n", "`n").Replace("`r", "`n")
            $normalizedText = [System.Text.RegularExpressions.Regex]::Replace($normalizedText, "[`t ]+(?=`n)", "")
            $normalizedText = [System.Text.RegularExpressions.Regex]::Replace($normalizedText, "[`t ]+\z", "")
            if ($normalizedText -ne $originalText) {
                $utf8WithoutBom = [System.Text.UTF8Encoding]::new($false)
                [System.IO.File]::WriteAllText($textArtifact.FullName, $normalizedText, $utf8WithoutBom)
            }
        }
    }
}

function Repair-BoundedScreenArtifacts {
    Repair-TextArtifactWhitespace @(
        $RerankerReportRoot,
        $PlotReportRoot
    )
}

function Invoke-LocalPreflight {
    Write-LogLine "INFO" "Running local bounded TE Curve Verification Pipeline preflight."
    Assert-RelativePathExists $ConfigPath
    Assert-RelativePathExists $MatrixRunnerPath
    Assert-RelativePathExists $RerankerRunnerPath
    Assert-RelativePathExists $PlotBuilderRunnerPath
    Assert-RelativePathExists $ActiveStatePath
    Assert-RelativePathExists "output/registries/families/shape_first_distilled_periodic_gru_sequence_fw/latest_family_best.yaml"
    Assert-RelativePathExists "output/registries/families/shape_first_distilled_periodic_mlp_harmonic_fw/latest_family_best.yaml"
    Assert-RelativePathExists "output/training_runs/shape_first_training_rule_distillation"
    Assert-RelativePathExists "models/polished_dataset/setpoints/periodic_gru_sequence/forward/reference_inventory.yaml"
    Assert-RelativePathExists "models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/reference_inventory.yaml"

    $activeStateText = Get-Content -Raw -LiteralPath (Join-Path $RepositoryRoot $ActiveStatePath)
    if ($activeStateText -notmatch "shape_first_distillation_bounded_track2_screen_2026_07_22") {
        throw "Active campaign state is not registered for shape_first_distillation_bounded_track2_screen_2026_07_22."
    }

    Write-CommandPreview "reference_family_vs_feedforward_matrix" (@("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + (New-MatrixArgumentList))
    Write-CommandPreview "shape_gated_reranker" (@("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + (New-RerankerArgumentList))
    Write-CommandPreview "track2_candidate_curve_plots" (@("run", "--no-capture-output", "-n", $CondaEnvironmentName, "python") + (New-PlotArgumentList))
    Write-LogLine "INFO" "Preflight passed. No verification run was launched."
}

function Convert-ToRemotePath {
    param([string]$Path)

    return ($Path -replace "\\", "/")
}

function Convert-ToEncodedPowerShellCommand {
    param([string]$CommandText)

    $commandBytes = [System.Text.Encoding]::Unicode.GetBytes($CommandText)
    return [Convert]::ToBase64String($commandBytes)
}

function Invoke-RemoteCommand {
    param([string]$CommandText)

    $encodedCommand = Convert-ToEncodedPowerShellCommand $CommandText
    ssh $RemoteHostAlias powershell -NoProfile -NonInteractive -OutputFormat Text -EncodedCommand $encodedCommand
    if ($LASTEXITCODE -ne 0) {
        throw "Remote command failed with exit code $LASTEXITCODE."
    }
}

function Invoke-RemoteCommandWithOutput {
    param([string]$CommandText)

    $encodedCommand = Convert-ToEncodedPowerShellCommand $CommandText
    $commandOutput = ssh $RemoteHostAlias powershell -NoProfile -NonInteractive -OutputFormat Text -EncodedCommand $encodedCommand
    if ($LASTEXITCODE -ne 0) {
        throw "Remote command failed with exit code $LASTEXITCODE."
    }
    return $commandOutput
}

function Invoke-RemotePowerShellScriptWithOutput {
    param(
        [string]$ScriptText,
        [string]$ScriptName
    )

    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $localScriptPath = Join-Path $LogRoot $ScriptName
    Set-Content -LiteralPath $localScriptPath -Value $ScriptText -Encoding UTF8

    $remoteRelativeScriptPath = Join-Path ".temp" $ScriptName
    $remoteScriptPath = Convert-ToRemotePath (Join-Path $RemoteRepositoryPath $remoteRelativeScriptPath)
    $remoteScriptParent = Split-Path -Parent $remoteScriptPath
    Invoke-RemoteCommand ("New-Item -ItemType Directory -Force -Path '{0}' | Out-Null" -f $remoteScriptParent)
    scp -q $localScriptPath ("{0}:`"{1}`"" -f $RemoteHostAlias, $remoteScriptPath)
    if ($LASTEXITCODE -ne 0) {
        throw "Remote script upload failed."
    }

    try {
        return Invoke-RemoteCommandWithOutput ("& '{0}'" -f $remoteScriptPath)
    }
    finally {
        Remove-Item -LiteralPath $localScriptPath -Force -ErrorAction SilentlyContinue
        Invoke-RemoteCommand ("Remove-Item -LiteralPath '{0}' -Force -ErrorAction SilentlyContinue" -f $remoteScriptPath)
    }
}

function Copy-PathToRemote {
    param([string]$RelativePath)

    $localPath = Join-Path $RepositoryRoot $RelativePath
    if (-not (Test-Path -LiteralPath $localPath)) {
        throw "Cannot sync missing local path: $RelativePath"
    }

    $remoteTarget = Convert-ToRemotePath (Join-Path $RemoteRepositoryPath $RelativePath)
    $remoteParent = Split-Path -Parent $remoteTarget
    Write-LogLine "INFO" ("Syncing source path: {0}" -f $RelativePath)
    Invoke-RemoteCommand ("New-Item -ItemType Directory -Force -Path '{0}' | Out-Null" -f $remoteParent)
    Invoke-RemoteCommand ("if (Test-Path -LiteralPath '{0}') {{ Remove-Item -LiteralPath '{0}' -Recurse -Force }}" -f $remoteTarget)
    scp -q -r $localPath ("{0}:`"{1}`"" -f $RemoteHostAlias, $remoteTarget)
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to sync $RelativePath to $RemoteHostAlias."
    }
}

function Invoke-RemoteSourceSync {
    Write-LogLine "STEP" "Syncing bounded screen inputs to remote host."
    $sourcePathList = @(
        $ConfigPath,
        $ActiveStatePath,
        "scripts/campaigns/track_2/run_shape_first_distillation_bounded_track2_screen.ps1",
        "scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward",
        "scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison",
        "scripts/reports/analysis",
        "scripts/datasets",
        "scripts/models",
        "scripts/tooling",
        "scripts/training",
        "scripts/reports/pdf",
        "config/datasets",
        "doc/scripts/campaigns/track_2/run_shape_first_distillation_bounded_track2_screen.md",
        "doc/reports/analysis/te_curve_verification_pipeline",
        "output/registries/families/shape_first_distilled_periodic_gru_sequence_fw",
        "output/registries/families/shape_first_distilled_periodic_mlp_harmonic_fw",
        "output/training_runs/shape_first_training_rule_distillation",
        "models/polished_dataset/setpoints/periodic_gru_sequence",
        "models/polished_dataset/setpoints/periodic_mlp_harmonic"
    )

    foreach ($sourcePath in $sourcePathList) {
        Copy-PathToRemote $sourcePath
    }
}

function Invoke-RemoteArtifactSync {
    Write-LogLine "STEP" "Syncing bounded screen artifacts from remote host."
    $remotePowerShell = @"
`$ProgressPreference = 'SilentlyContinue'
`$RepositoryRoot = '$RemoteRepositoryPath'
`$OutputSuffix = '$OutputSuffix'
Set-Location -LiteralPath `$RepositoryRoot
`$artifactMap = @()
function Add-ExactArtifactPath {
  param([string]`$RelativePath)
  if (Test-Path -LiteralPath `$RelativePath) {
    `$script:artifactMap += @{ Source = `$RelativePath; Target = `$RelativePath }
  }
}
function Add-LatestArtifactDirectory {
  param([string]`$RootPath, [string]`$NamePattern)
  if (-not (Test-Path -LiteralPath `$RootPath)) {
    return
  }
  `$latestDirectory = Get-ChildItem -LiteralPath `$RootPath -Directory -Filter `$NamePattern |
    Sort-Object -Property LastWriteTime -Descending |
    Select-Object -First 1
  if (`$null -ne `$latestDirectory) {
    Add-ExactArtifactPath (Join-Path `$RootPath `$latestDirectory.Name)
  }
}
function Add-LatestArtifactFile {
  param([string]`$RootPath, [string]`$NamePattern)
  if (-not (Test-Path -LiteralPath `$RootPath)) {
    return
  }
  `$latestFile = Get-ChildItem -LiteralPath `$RootPath -File -Filter `$NamePattern |
    Sort-Object -Property LastWriteTime -Descending |
    Select-Object -First 1
  if (`$null -ne `$latestFile) {
    Add-ExactArtifactPath (Join-Path `$RootPath `$latestFile.Name)
  }
}
Add-LatestArtifactDirectory 'output/validation_checks/track2_reference_comparison' ("*{0}*" -f `$OutputSuffix)
Add-LatestArtifactDirectory 'output/validation_checks/shape_gated_te_curve_reranker' '*'
Add-LatestArtifactDirectory 'output/validation_checks/track2_operator_launch_logs' ("*{0}" -f `$OutputSuffix)
Add-LatestArtifactFile 'doc/reports/analysis/validation_checks/te_curve_verification_pipeline' ("*{0}*report.md" -f `$OutputSuffix)
Add-ExactArtifactPath '$RerankerReportRoot/${OutputSuffix}_matrix_shape_gated_te_curve_reranker_report.md'
Add-ExactArtifactPath '$PlotReportRoot'
`$bundleRoot = Join-Path `$env:TEMP ('shape_first_distillation_bounded_track2_screen_bundle_$RunStamp')
if (Test-Path -LiteralPath `$bundleRoot) {
  Remove-Item -LiteralPath `$bundleRoot -Recurse -Force
}
New-Item -ItemType Directory -Force -Path `$bundleRoot | Out-Null
`$copiedPathCount = 0
foreach (`$artifactEntry in `$artifactMap) {
  if (-not (Test-Path -LiteralPath `$artifactEntry.Source)) {
    continue
  }
  `$targetPath = Join-Path `$bundleRoot `$artifactEntry.Target
  `$targetParent = Split-Path -Parent `$targetPath
  New-Item -ItemType Directory -Force -Path `$targetParent | Out-Null
  Copy-Item -LiteralPath `$artifactEntry.Source -Destination `$targetPath -Recurse -Force
  `$copiedPathCount += 1
}
if (`$copiedPathCount -eq 0) {
  throw 'No bounded screen artifact paths were found on the remote host.'
}
`$archivePath = Join-Path `$env:TEMP ('shape_first_distillation_bounded_track2_screen_artifacts_$RunStamp.zip')
if (Test-Path -LiteralPath `$archivePath) {
  Remove-Item -LiteralPath `$archivePath -Force
}
Compress-Archive -Path (Join-Path `$bundleRoot '*') -DestinationPath `$archivePath -Force
Write-Output `$archivePath
"@
    $remoteArchivePath = Invoke-RemotePowerShellScriptWithOutput $remotePowerShell ("{0}_remote_artifact_sync_{1}.ps1" -f $OutputSuffix, $RunStamp)

    $localArchivePath = Join-Path $LogRoot "remote_artifacts.zip"
    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    Write-LogLine "INFO" "Downloading bounded screen artifact bundle."
    scp -q ("{0}:`"{1}`"" -f $RemoteHostAlias, $remoteArchivePath.Trim()) $localArchivePath
    if ($LASTEXITCODE -ne 0) {
        throw "Remote artifact download failed."
    }

    Expand-Archive -LiteralPath $localArchivePath -DestinationPath $RepositoryRoot -Force
    Remove-Item -LiteralPath $localArchivePath -Force -ErrorAction SilentlyContinue
    Repair-BoundedScreenArtifacts
    Write-LogLine "INFO" "Remote artifacts synchronized."
}

function Invoke-RemoteRun {
    Invoke-RemoteSourceSync
    $remoteScriptPath = Convert-ToRemotePath (Join-Path $RemoteRepositoryPath "scripts/campaigns/track_2/run_shape_first_distillation_bounded_track2_screen.ps1")
    $preflightFlag = ""
    if ($PreflightOnly) {
        $preflightFlag = " -PreflightOnly"
    }

    Write-LogLine "STEP" "Launching bounded screen on remote host."
    Invoke-RemoteCommand ("& '{0}' -CondaEnvironmentName '{1}' -OutputSuffix '{2}' -ReportDate '{3}'{4}" -f $remoteScriptPath, $RemoteCondaEnvironmentName, $OutputSuffix, $ReportDate, $preflightFlag)

    if (-not $PreflightOnly) {
        Invoke-RemoteArtifactSync
    }
}

if ($Remote) {
    Invoke-RemoteRun
    exit 0
}

Invoke-LocalPreflight
if ($PreflightOnly) {
    exit 0
}

Invoke-LoggedCondaPython -StepName "reference_family_vs_feedforward_matrix" -PythonArgumentList (New-MatrixArgumentList)
Invoke-LoggedCondaPython -StepName "shape_gated_reranker" -PythonArgumentList (New-RerankerArgumentList)
Invoke-LoggedCondaPython -StepName "track2_candidate_curve_plots" -PythonArgumentList (New-PlotArgumentList)
Repair-BoundedScreenArtifacts
Write-LogLine "INFO" ("Bounded screen completed. Logs: {0}" -f $LogRoot)
