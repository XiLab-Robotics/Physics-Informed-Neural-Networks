function Invoke-CondaRunWithStreamingLog {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix,
        [string]$LogPath
    )

    $heartbeatIntervalSeconds = 15

    if (-not [string]::IsNullOrWhiteSpace($env:CONDA_EXE)) {
        $condaExecutablePath = $env:CONDA_EXE
    }
    else {
        $condaExecutablePath = (Get-Command conda.exe -ErrorAction Stop).Source
    }
    if ([System.IO.Path]::IsPathRooted($LogPath)) {
        $resolvedLogPath = $LogPath
    }
    else {
        $resolvedLogPath = Join-Path (Get-Location).Path $LogPath
    }

    $logDirectoryPath = Split-Path -Parent $resolvedLogPath
    if (-not [string]::IsNullOrWhiteSpace($logDirectoryPath)) {
        New-Item -ItemType Directory -Path $logDirectoryPath -Force | Out-Null
    }

    function Format-CmdArgument {
        param(
            [string]$Value
        )

        if ([string]::IsNullOrWhiteSpace($Value)) {
            return '""'
        }

        if ($Value.Contains(' ')) {
            return ('"{0}"' -f $Value)
        }

        return $Value
    }

    $utf8Encoding = [System.Text.UTF8Encoding]::new($false)
    $logWriter = [System.IO.StreamWriter]::new($resolvedLogPath, $false, $utf8Encoding)
    $interruptedByOperator = $false
    $previousErrorActionPreference = $ErrorActionPreference

    try {
        $ErrorActionPreference = "Continue"
        & $condaExecutablePath run --no-capture-output -n $EnvironmentName $PythonExecutablePath $RunnerScriptPath --config-path $ConfigPath --output-suffix $OutputSuffix 2>&1 | ForEach-Object {
            if ($null -eq $_) {
                return
            }

            $outputLine = $_.ToString()
            if ([string]::IsNullOrWhiteSpace($outputLine)) {
                return
            }

            $logWriter.WriteLine($outputLine)
            $logWriter.Flush()
            Write-Host $outputLine
        }

        return [int]$LASTEXITCODE
    }
    catch [System.Management.Automation.PipelineStoppedException] {
        $interruptedByOperator = $true
        Write-Host "[WARN] Campaign launcher interrupted by operator"
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference

        if ($null -ne $logWriter) {
            $logWriter.Flush()
            $logWriter.Dispose()
        }
    }

    if ($interruptedByOperator) {
        return 130
    }
}


function Invoke-CondaRunWithLoggedOutput {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix,
        [string]$LogPath
    )

    return Invoke-CondaRunWithStreamingLog `
        -EnvironmentName $EnvironmentName `
        -PythonExecutablePath $PythonExecutablePath `
        -RunnerScriptPath $RunnerScriptPath `
        -ConfigPath $ConfigPath `
        -OutputSuffix $OutputSuffix `
        -LogPath $LogPath
}


function Invoke-CondaRun {
    param(
        [string]$EnvironmentName,
        [string]$PythonExecutablePath,
        [string]$RunnerScriptPath,
        [string]$ConfigPath,
        [string]$OutputSuffix,
        [string]$LogPath
    )

    return Invoke-CondaRunWithStreamingLog `
        -EnvironmentName $EnvironmentName `
        -PythonExecutablePath $PythonExecutablePath `
        -RunnerScriptPath $RunnerScriptPath `
        -ConfigPath $ConfigPath `
        -OutputSuffix $OutputSuffix `
        -LogPath $LogPath
}
