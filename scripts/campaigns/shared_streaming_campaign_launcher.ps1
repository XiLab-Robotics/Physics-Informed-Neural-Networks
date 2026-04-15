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
    $process = $null
    $interruptedByOperator = $false

    function Format-ElapsedTime {
        param(
            [TimeSpan]$ElapsedTime
        )

        return $ElapsedTime.ToString("hh\:mm\:ss")
    }

    function Stop-ProcessTree {
        param(
            [System.Diagnostics.Process]$ProcessToStop
        )

        if (($null -eq $ProcessToStop) -or $ProcessToStop.HasExited) {
            return
        }

        try {
            & taskkill.exe /PID $ProcessToStop.Id /T /F | Out-Null
        }
        catch {
            try {
                if (-not $ProcessToStop.HasExited) {
                    $ProcessToStop.Kill()
                }
            }
            catch {
                Write-Host (
                    "[WARN] Failed to terminate child process tree | " +
                    "pid=$($ProcessToStop.Id) error=$($_.Exception.Message)"
                )
            }
        }
    }

    try {
        $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $startInfo.FileName = "cmd.exe"
        $startInfo.Arguments = (
            '/c {0} run --no-capture-output -n {1} {2} {3} --config-path {4} --output-suffix {5} 2>&1' -f
            (Format-CmdArgument -Value $condaExecutablePath),
            (Format-CmdArgument -Value $EnvironmentName),
            (Format-CmdArgument -Value $PythonExecutablePath),
            (Format-CmdArgument -Value $RunnerScriptPath),
            (Format-CmdArgument -Value $ConfigPath),
            (Format-CmdArgument -Value $OutputSuffix)
        )
        $startInfo.UseShellExecute = $false
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $false
        $startInfo.CreateNoWindow = $true
        $startInfo.WorkingDirectory = (Get-Location).Path

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $startInfo

        $null = $process.Start()
        $launchStartTime = Get-Date
        $lastOutputTime = $launchStartTime
        $lastHeartbeatTime = $launchStartTime

        while (-not $process.HasExited) {
            while ($process.StandardOutput.Peek() -ge 0) {
                $outputLine = $process.StandardOutput.ReadLine()
                if ($null -eq $outputLine) {
                    continue
                }

                $logWriter.WriteLine($outputLine)
                $logWriter.Flush()
                Write-Host $outputLine
                $lastOutputTime = Get-Date
            }

            $now = Get-Date
            if (($now - $lastHeartbeatTime).TotalSeconds -ge $heartbeatIntervalSeconds) {
                $elapsedTime = $now - $launchStartTime
                $silenceTime = $now - $lastOutputTime
                Write-Host (
                    "[HEARTBEAT] Child process alive | " +
                    "pid=$($process.Id) " +
                    "elapsed=$(Format-ElapsedTime -ElapsedTime $elapsedTime) " +
                    "silent_for=$(Format-ElapsedTime -ElapsedTime $silenceTime)"
                )
                $lastHeartbeatTime = $now
            }

            $null = $process.WaitForExit(1000)
        }

        while (-not $process.StandardOutput.EndOfStream) {
            $outputLine = $process.StandardOutput.ReadLine()
            if ($null -eq $outputLine) {
                continue
            }

            $logWriter.WriteLine($outputLine)
            $logWriter.Flush()
            Write-Host $outputLine
        }

        return [int]$process.ExitCode
    }
    catch [System.Management.Automation.PipelineStoppedException] {
        $interruptedByOperator = $true
        Write-Host "[WARN] Campaign launcher interrupted by operator | terminating child process tree"
    }
    finally {
        if (($null -ne $process) -and (-not $process.HasExited)) {
            Stop-ProcessTree -ProcessToStop $process
        }

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
