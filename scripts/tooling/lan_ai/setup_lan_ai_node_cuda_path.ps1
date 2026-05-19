param(
    [string]$CondaPrefix = $env:CONDA_PREFIX
)

if ([string]::IsNullOrWhiteSpace($CondaPrefix)) {
    $pythonPrefix = (& python -c "import sys; print(sys.prefix)" 2>$null)
    if ($LASTEXITCODE -eq 0) {
        $CondaPrefix = $pythonPrefix.Trim()
    }
}

if ([string]::IsNullOrWhiteSpace($CondaPrefix)) {
    throw "Could not resolve the target Conda environment prefix. Pass -CondaPrefix explicitly or activate the target environment first."
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
    throw "Missing expected NVIDIA runtime directories:`n$($missingCudaBinPathList -join '`n')"
}

$activateScriptPath = Join-Path $activateDirectory "standardml_lan_ai_node_cuda_path.ps1"
$deactivateScriptPath = Join-Path $deactivateDirectory "standardml_lan_ai_node_cuda_path.ps1"

$activateScriptText = @'
$env:PINNS_PREPEND_NVIDIA_PATH = "__PINNS_NVIDIA_PATHS__"
$env:PINNS_PREVIOUS_PATH = $env:PATH
$env:PATH = "$env:PINNS_PREPEND_NVIDIA_PATH;$env:PATH"
'@ -replace "__PINNS_NVIDIA_PATHS__", ($cudaBinPathList -join ';')

$deactivateScriptText = @'
if ($env:PINNS_PREVIOUS_PATH) {
    $env:PATH = $env:PINNS_PREVIOUS_PATH
}
Remove-Item Env:PINNS_PREVIOUS_PATH -ErrorAction SilentlyContinue
Remove-Item Env:PINNS_PREPEND_NVIDIA_PATH -ErrorAction SilentlyContinue
'@

Set-Content -Path $activateScriptPath -Value $activateScriptText -NoNewline
Set-Content -Path $deactivateScriptPath -Value $deactivateScriptText -NoNewline

Write-Host "Resolved Conda prefix:" $CondaPrefix -ForegroundColor Cyan
Write-Host "Configured activate hook:" $activateScriptPath
Write-Host "Configured deactivate hook:" $deactivateScriptPath
Write-Host "CUDA runtime PATH entries:" -ForegroundColor Cyan
$cudaBinPathList | ForEach-Object { Write-Host " - $_" }
