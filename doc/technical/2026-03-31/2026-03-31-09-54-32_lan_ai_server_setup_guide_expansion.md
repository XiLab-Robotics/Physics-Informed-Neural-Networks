# LAN AI Server Setup Guide Expansion

## Overview

This document defines the approved scope for expanding the repository-owned LAN
AI node documentation into a complete Windows-first setup guide for the second
workstation.

The requested guide must let a user start from a clean remote Windows 11
machine and reach a fully usable `LM Studio` plus `lan_ai_node_server.py`
deployment that can be operated from the current workstation terminal.

The expanded guidance will cover:

- shared-token generation in PowerShell;
- persistent Windows user/system environment-variable setup;
- Git cloning prerequisites, including `git config --system core.longpaths true`;
- Miniconda installation and PowerShell initialization;
- CUDA installation guidance for NVIDIA-backed machines;
- Conda environment creation and dependency installation from `requirements.txt`;
- `LM Studio` installation, server configuration, and model download guidance;
- Windows 11 `OpenSSH Server` installation and service enablement;
- first LAN health checks and first workflow commands from the current
  workstation;
- official-doc screenshots for the `LM Studio` server setup flow.

## Technical Approach

The implementation will consolidate the current LAN-node notes into a canonical,
step-by-step operational guide and update the public repository entry points so
new users do not miss machine-level prerequisites.

The guide will be grounded in current official documentation for:

- `LM Studio` local server and network serving;
- Conda Windows installation and `conda init powershell`;
- Microsoft `OpenSSH Server` on Windows 11;
- NVIDIA CUDA installation on Windows.

The implementation will likely produce:

- an expanded or newly split guide under `doc/scripts/tooling/` for the remote
  LAN node setup;
- updates to `doc/guide/project_usage_guide.md` for the runnable workstation to
  server flow;
- updates to `README.md` for cloning prerequisites and the new setup entry
  point;
- repository-owned copies of a small set of `LM Studio` official-doc images
  stored in a discoverable guide-local assets location, with clear source
  attribution inside the guide.

No subagent is planned for this task.

## Involved Components

- `README.md`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/tooling/lan_ai_node_server.md`
- optional new guide-local asset folder under `doc/scripts/tooling/assets/` or
  a similarly local path next to the LAN-node guide
- official sources:
  - `lmstudio.ai`
  - `docs.conda.io`
  - `learn.microsoft.com`
  - `docs.nvidia.com`

## Implementation Steps

1. Inspect the existing LAN-node documentation and identify what should remain
   in the script note versus what should be elevated into broader user-facing
   setup guidance.
2. Collect the current official setup details for `LM Studio`, Conda,
   `OpenSSH Server`, and CUDA, and verify that the instructions fit Windows 11.
3. Expand the LAN-node documentation into a start-to-finish setup guide that
   begins with token generation and ends with health checks from the current
   workstation.
4. Add repository-facing README guidance for cloning prerequisites, including
   `git config --system core.longpaths true`.
5. Add or refresh the detailed runnable workflow description in
   `doc/guide/project_usage_guide.md`.
6. Add the selected `LM Studio` documentation screenshots as repository-owned
   local assets with attribution.
7. Run scoped Markdown warning checks on all touched Markdown files and fix any
   local warning regressions before closing the task.
