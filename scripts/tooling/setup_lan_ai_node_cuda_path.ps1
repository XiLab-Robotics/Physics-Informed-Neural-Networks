param(
    [string]$CondaPrefix = $env:CONDA_PREFIX
)

if ([string]::IsNullOrWhiteSpace($CondaPrefix)) {
    throw "CONDA_PREFIX is not set. Activate the target Conda environment first."
}

$activateDirectory = Join-Path $CondaPrefix "etc\\conda\\activate.d"
$deactivateDirectory = Join-Path $CondaPrefix "etc\\conda\\deactivate.d"

New-Item -ItemType Directory -Force -Path $activateDirectory | Out-Null
New-Item -ItemType Directory -Force -Path $deactivateDirectory | Out-Null

$cudaBinPathList = @(
    (Join-Path $CondaPrefix "Lib\\site-packages\\nvidia\\cublas\\bin"),
    (Join-Path $CondaPrefix "Lib\\site-packages\\nvidia\\cuda_runtime\\bin"),
    (Join-Path $CondaPrefix "Lib\\site-packages\\nvidia\\cudnn\\bin")
)

$missingCudaBinPathList = $cudaBinPathList | Where-Object { -not (Test-Path $_) }
if ($missingCudaBinPathList.Count -gt 0) {
    throw "Missing expected NVIDIA runtime directories:`n$($missingCudaBinPathList -join \"`n\")"
}

$activateScriptPath = Join-Path $activateDirectory "standardml_lan_ai_node_cuda_path.ps1"
$deactivateScriptPath = Join-Path $deactivateDirectory "standardml_lan_ai_node_cuda_path.ps1"

$activateScriptText = @"
\$env:STANDARDML_PREPEND_NVIDIA_PATH = "$($cudaBinPathList -join ';')"
\$env:STANDARDML_PREVIOUS_PATH = \$env:PATH
\$env:PATH = "\$env:STANDARDML_PREPEND_NVIDIA_PATH;\$env:PATH"
"@

$deactivateScriptText = @"
if (\$env:STANDARDML_PREVIOUS_PATH) {
    \$env:PATH = \$env:STANDARDML_PREVIOUS_PATH
}
Remove-Item Env:STANDARDML_PREVIOUS_PATH -ErrorAction SilentlyContinue
Remove-Item Env:STANDARDML_PREPEND_NVIDIA_PATH -ErrorAction SilentlyContinue
"@

Set-Content -Path $activateScriptPath -Value $activateScriptText -NoNewline
Set-Content -Path $deactivateScriptPath -Value $deactivateScriptText -NoNewline

Write-Host "Configured activate hook:" $activateScriptPath
Write-Host "Configured deactivate hook:" $deactivateScriptPath
Write-Host "CUDA runtime PATH entries:" -ForegroundColor Cyan
$cudaBinPathList | ForEach-Object { Write-Host " - $_" }
