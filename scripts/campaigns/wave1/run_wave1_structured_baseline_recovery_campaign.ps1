param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\wave1_structured_baselines\campaigns\2026-03-20_wave1_structured_baseline_recovery_campaign"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$recoveryPatternList = @(
    "*harmonic_order06_static_recovery.yaml"
    "*harmonic_order12_static_recovery.yaml"
    "*harmonic_order12_linear_conditioned_recovery.yaml"
    "*residual_h12_small_frozen_recovery.yaml"
    "*residual_h12_small_joint_recovery.yaml"
    "*random_forest_tabular_conservative.yaml"
)

foreach ($queueSubdirectoryName in @("pending", "running")) {
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path $queueSubdirectoryPath)) {
        continue
    }

    Get-ChildItem -Path $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
        Where-Object {
            $fileName = $_.Name
            foreach ($recoveryPattern in $recoveryPatternList) {
                if ($fileName -like $recoveryPattern) {
                    return $true
                }
            }
            return $false
        } |
        Remove-Item -Force
}

$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_harmonic_order06_static_recovery.yaml")
    (Join-Path $campaignConfigRoot "02_harmonic_order12_static_recovery.yaml")
    (Join-Path $campaignConfigRoot "03_harmonic_order12_linear_conditioned_recovery.yaml")
    (Join-Path $campaignConfigRoot "04_residual_h12_small_frozen_recovery.yaml")
    (Join-Path $campaignConfigRoot "05_residual_h12_small_joint_recovery.yaml")
    (Join-Path $campaignConfigRoot "06_random_forest_tabular_conservative.yaml")
)

$argumentList = @(
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    "wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
