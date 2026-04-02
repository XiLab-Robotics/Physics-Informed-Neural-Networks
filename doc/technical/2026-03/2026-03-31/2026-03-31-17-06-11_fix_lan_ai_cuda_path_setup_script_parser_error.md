# Fix LAN AI CUDA Path Setup Script Parser Error

## Overview

The repository-owned helper `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
fails on Windows PowerShell before execution starts. The reported parser error
shows that the script contains invalid escaping around the `-join` expression in
the missing-directory error message, so remote users cannot complete the
persistent CUDA runtime `PATH` setup for the `standard_ml_lan_node`
environment.

## Technical Approach

Apply a minimal PowerShell syntax fix to the helper script by removing the
invalid escaped quoting inside the interpolated `throw` string. Keep the script
behavior unchanged apart from restoring valid parsing. Update the LAN AI setup
guide if needed so the documented helper remains consistent with the repaired
script.

## Involved Components

- `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `README.md`

## Implementation Steps

1. Correct the malformed PowerShell string interpolation in
   `setup_lan_ai_node_cuda_path.ps1`.
2. Verify that the helper script still documents and emits the expected Conda
   activation-hook setup.
3. Update repository documentation only where the fix changes user-visible
   setup guidance.
4. Run scoped Markdown checks on touched Markdown files and confirm normal final
   newline state before closing the task.
