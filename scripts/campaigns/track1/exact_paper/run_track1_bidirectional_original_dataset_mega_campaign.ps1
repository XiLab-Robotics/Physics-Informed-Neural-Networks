param(
    [switch]$Remote,
    [string]$CondaEnvironmentName = "standard_ml_codex_env",
    [string]$PythonExecutable = "python",
    [string]$RemoteHostAlias = "xilab-remote",
    [string]$RemoteRepositoryPath = $(if ($env:STANDARDML_REMOTE_TRAINING_REPO_PATH) { $env:STANDARDML_REMOTE_TRAINING_REPO_PATH } else { "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" }),
    [string]$RemoteCondaEnvironmentName = $(if ($env:STANDARDML_REMOTE_TRAINING_CONDA_ENV) { $env:STANDARDML_REMOTE_TRAINING_CONDA_ENV } else { "standard_ml_lan_node" })
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$ActiveCampaignPath = Join-Path $ProjectRoot "doc\running\active_training_campaign.yaml"
$RunnerPath = Join-Path $ProjectRoot "scripts\paper_reimplementation\rcim_ml_compensation\run_original_dataset_exact_model_bank_validation.py"
Set-Location $ProjectRoot

function Get-CampaignQueueBundle {

    param(
        [string]$CampaignYamlPath,
        [string]$ProjectRootPath,
        [string]$EnvironmentName,
        [string]$PythonCommand
    )

    $TemporaryPythonScriptPath = Join-Path $env:TEMP ("track1_bidirectional_queue_bundle_{0}.py" -f ([guid]::NewGuid().ToString("N")))
    $ProjectRootPythonLiteral = $ProjectRootPath | ConvertTo-Json -Compress
    $CampaignYamlPythonLiteral = $CampaignYamlPath | ConvertTo-Json -Compress
    $PythonScriptText = @"
from pathlib import Path
import json
import yaml

project_root = Path($ProjectRootPythonLiteral)
campaign_path = Path($CampaignYamlPythonLiteral)
campaign_payload = yaml.safe_load(campaign_path.read_text(encoding="utf-8"))
queue_path_list = campaign_payload.get("queue_config_path_list", [])
run_name_list = [
    yaml.safe_load((project_root / queue_path).read_text(encoding="utf-8"))["experiment"]["run_name"]
    for queue_path in queue_path_list
]
payload = {
    "campaign_name": campaign_payload.get("campaign_name"),
    "planning_report_path": campaign_payload.get("planning_report_path"),
    "campaign_output_directory": campaign_payload.get("campaign_output_directory"),
    "queue_config_path_list": queue_path_list,
    "run_name_list": run_name_list,
}
print(json.dumps(payload))
"@

    try {
        Set-Content -LiteralPath $TemporaryPythonScriptPath -Value $PythonScriptText -Encoding UTF8
        $CampaignBundleJson = & conda run -n $EnvironmentName $PythonCommand $TemporaryPythonScriptPath
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to read active campaign YAML | $CampaignYamlPath"
        }

        return ($CampaignBundleJson | ConvertFrom-Json)
    }
    finally {
        if (Test-Path -LiteralPath $TemporaryPythonScriptPath) {
            Remove-Item -LiteralPath $TemporaryPythonScriptPath -Force -ErrorAction SilentlyContinue
        }
    }
}

$CampaignQueueBundle = Get-CampaignQueueBundle `
    -CampaignYamlPath $ActiveCampaignPath `
    -ProjectRootPath $ProjectRoot `
    -EnvironmentName $CondaEnvironmentName `
    -PythonCommand $PythonExecutable

if ($Remote) {
    & ".\scripts\campaigns\track1\exact_paper\run_exact_paper_campaign_remote.ps1" `
        -CampaignName $CampaignQueueBundle.campaign_name `
        -PlanningReportPath $CampaignQueueBundle.planning_report_path `
        -LauncherRelativePath "scripts\campaigns\track1\exact_paper\run_track1_bidirectional_original_dataset_mega_campaign.ps1" `
        -CampaignOutputRootOverride $CampaignQueueBundle.campaign_output_directory `
        -CampaignConfigPathList @($CampaignQueueBundle.queue_config_path_list) `
        -RunNameList @($CampaignQueueBundle.run_name_list) `
        -ValidationOutputRoot "output\validation_checks\paper_reimplementation_rcim_original_dataset_exact_model_bank" `
        -ValidationReportRoot "doc\reports\analysis\validation_checks" `
        -RemoteHostAlias $RemoteHostAlias `
        -RemoteRepositoryPath $RemoteRepositoryPath `
        -RemoteCondaEnvironmentName $RemoteCondaEnvironmentName
    exit $LASTEXITCODE
}

foreach ($ConfigRelativePath in @($CampaignQueueBundle.queue_config_path_list)) {
    $ConfigPath = Join-Path $ProjectRoot $ConfigRelativePath
    Write-Host "[INFO] Running mega-campaign validation | $ConfigPath" -ForegroundColor Cyan
    conda run -n $CondaEnvironmentName $PythonExecutable $RunnerPath --config-path $ConfigPath --output-suffix campaign_validation
    if ($LASTEXITCODE -ne 0) {
        throw "Mega campaign run failed | $ConfigPath"
    }
}

Write-Host "[DONE] Track 1 bidirectional original-dataset mega campaign completed" -ForegroundColor Green
