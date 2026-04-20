param(
    [string]$PythonExecutable = "python"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = (Resolve-Path (Join-Path $scriptDirectory "..\..\..")).Path

Set-Location $projectRoot

$campaignConfigRoot = "config\training\residual_harmonic_mlp\campaigns\2026-03-26_wave1_residual_harmonic_family_campaign"
$planningReportPath = "doc\reports\campaign_plans\wave1\2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md"
$queueRoot = "config\training\queue"

$campaignPatternList = @(
    "*residual_h08_small_frozen.yaml"
    "*residual_h08_small_joint.yaml"
    "*residual_h12_small_frozen.yaml"
    "*residual_h12_small_joint_anchor.yaml"
    "*residual_h16_small_joint.yaml"
    "*residual_h12_medium_joint.yaml"
    "*residual_h12_wide_joint.yaml"
    "*residual_h12_deep_joint.yaml"
    "*residual_h12_small_joint_low_dropout.yaml"
    "*residual_h12_small_joint_high_dropout.yaml"
    "*residual_h12_small_joint_no_layer_norm.yaml"
    "*residual_h12_small_joint_low_lr_long.yaml"
    "*residual_h12_wide_joint_low_lr_long.yaml"
    "*residual_h12_small_joint_dense.yaml"
    "*residual_h12_small_joint_medium_dense_large_batch.yaml"
)

foreach ($queueSubdirectoryName in @("pending", "running")) {
    $queueSubdirectoryPath = Join-Path $queueRoot $queueSubdirectoryName
    if (-not (Test-Path $queueSubdirectoryPath)) {
        continue
    }

    Get-ChildItem -Path $queueSubdirectoryPath -File -ErrorAction SilentlyContinue |
        Where-Object {
            $fileName = $_.Name
            foreach ($campaignPattern in $campaignPatternList) {
                if ($fileName -like $campaignPattern) {
                    return $true
                }
            }
            return $false
        } |
        Remove-Item -Force
}

$campaignConfigPathList = @(
    (Join-Path $campaignConfigRoot "01_residual_h08_small_frozen.yaml")
    (Join-Path $campaignConfigRoot "02_residual_h08_small_joint.yaml")
    (Join-Path $campaignConfigRoot "03_residual_h12_small_frozen.yaml")
    (Join-Path $campaignConfigRoot "04_residual_h12_small_joint_anchor.yaml")
    (Join-Path $campaignConfigRoot "05_residual_h16_small_joint.yaml")
    (Join-Path $campaignConfigRoot "06_residual_h12_medium_joint.yaml")
    (Join-Path $campaignConfigRoot "07_residual_h12_wide_joint.yaml")
    (Join-Path $campaignConfigRoot "08_residual_h12_deep_joint.yaml")
    (Join-Path $campaignConfigRoot "09_residual_h12_small_joint_low_dropout.yaml")
    (Join-Path $campaignConfigRoot "10_residual_h12_small_joint_high_dropout.yaml")
    (Join-Path $campaignConfigRoot "11_residual_h12_small_joint_no_layer_norm.yaml")
    (Join-Path $campaignConfigRoot "12_residual_h12_small_joint_low_lr_long.yaml")
    (Join-Path $campaignConfigRoot "13_residual_h12_wide_joint_low_lr_long.yaml")
    (Join-Path $campaignConfigRoot "14_residual_h12_small_joint_dense.yaml")
    (Join-Path $campaignConfigRoot "15_residual_h12_small_joint_medium_dense_large_batch.yaml")
)

$argumentList = @(
    "scripts\training\run_training_campaign.py"
) + $campaignConfigPathList + @(
    "--campaign-name",
    "wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00",
    "--planning-report-path",
    $planningReportPath
)

& $PythonExecutable @argumentList
exit $LASTEXITCODE
