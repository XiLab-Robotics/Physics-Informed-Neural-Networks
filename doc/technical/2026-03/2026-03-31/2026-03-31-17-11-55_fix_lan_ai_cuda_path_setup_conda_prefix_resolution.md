# Fix LAN AI CUDA Path Setup Conda Prefix Resolution

## Overview

The repository-owned helper `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
can resolve the wrong Conda prefix when launched through
`powershell -ExecutionPolicy Bypass -File ...` from an already activated
environment. In the validated remote workflow, the child PowerShell process may
see the base Miniconda prefix instead of `standard_ml_lan_node`, causing the
helper to look for NVIDIA CUDA DLL directories in the wrong location.

## Technical Approach

Make the helper robust against child-shell prefix drift. The script should
prefer an explicitly passed prefix, then fall back to the active Python
interpreter prefix when available, and only then use `CONDA_PREFIX`. Update the
LAN AI setup guide so the documented command passes the intended environment
prefix explicitly when needed.

## Involved Components

- `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `README.md`

## Implementation Steps

1. Update the PowerShell helper to resolve the target Conda environment prefix
   more robustly.
2. Adjust the LAN AI setup guide so the recommended command remains valid in the
   validated remote workstation setup.
3. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
