# Fix LAN AI CUDA Hook Generation Interpolation

## Overview

The repository-owned helper `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
now resolves the correct Conda environment prefix, but the generated Conda hook
files still fail to parse on Windows. The root cause is incorrect PowerShell
escaping inside the here-strings used to write `activate.d` and `deactivate.d`
scripts: the parent script interpolates `$env:PATH` and related expressions
while generating the files, so the resulting hook content contains invalid
literalized shell fragments.

## Technical Approach

Repair hook generation by using non-interpolating here-strings for the parts of
the generated scripts that must remain as literal PowerShell code, while still
injecting the resolved NVIDIA path list explicitly. Keep the user-facing setup
flow unchanged apart from restoring valid Conda activation hooks.

## Involved Components

- `scripts/tooling/setup_lan_ai_node_cuda_path.ps1`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `README.md`

## Implementation Steps

1. Update the helper script so generated Conda hook files contain valid literal
   PowerShell statements.
2. Preserve the explicit NVIDIA path list injection for the target environment.
3. Update documentation only if the repaired script changes the recommended
   command sequence.
4. Run scoped Markdown warning checks on touched Markdown files and confirm
   normal final-newline state before closing the task.
