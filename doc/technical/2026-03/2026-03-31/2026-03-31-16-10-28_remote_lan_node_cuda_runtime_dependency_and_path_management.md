# Remote LAN Node CUDA Runtime Dependency And Path Management

## Overview

This document defines the approved scope for fixing the remote LAN AI node
environment so that `faster-whisper` GPU execution works reproducibly on the
remote Windows workstation.

The validated runtime issue is:

- the remote workstation has NVIDIA drivers and CUDA `13.x` installed;
- `faster-whisper` through `ctranslate2` requires CUDA `12` runtime libraries
  such as `cublas64_12.dll`;
- those DLLs are available only after installing Python-distributed NVIDIA CUDA
  runtime packages into the remote Conda environment;
- the DLL directories must also be added to `PATH` for the active environment,
  otherwise the server still fails at runtime.

## Technical Approach

The cleanest repository-owned fix is to separate the remote LAN node runtime
dependencies from the main project `requirements.txt`.

The main `requirements.txt` should remain focused on the canonical repository
environment used on the current workstation and on generic repository
reproducibility. It should not be burdened with Windows-only, GPU-runtime,
large-download packages that are required only by the remote LAN node.

The recommended implementation is:

- create a dedicated dependency file for the remote LAN AI node, for example:
  - `requirements-lan-ai-node.txt`
- include in that file the NVIDIA CUDA runtime packages required by the remote
  `faster-whisper` GPU path:
  - `nvidia-cuda-runtime-cu12`
  - `nvidia-cublas-cu12`
  - `nvidia-cudnn-cu12`
- add Conda environment activation and deactivation scripts under the remote
  node environment workflow so the required `site-packages\\nvidia\\...\\bin`
  folders are appended to `PATH` automatically when the environment is active;
- update the LAN-node guide so the remote setup uses this dedicated dependency
  file and explains the persistent `PATH` handling.

This keeps the main repository environment cleaner while making the remote GPU
node reproducible and less fragile.

No subagent is planned for this task.

## Involved Components

- new remote-node dependency file, recommended:
  - `requirements-lan-ai-node.txt`
- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md` if the LAN section should mention the
  dedicated remote requirements file
- `README.md` if the new remote dependency file should be surfaced as a main
  setup entry point

## Implementation Steps

1. Add a dedicated dependency file for the remote LAN AI node.
2. Include the validated NVIDIA CUDA runtime packages required by the remote
   `faster-whisper` GPU path.
3. Add repository-owned environment-hook files or documented commands that make
   the NVIDIA DLL directories persistently available in `PATH` for the remote
   environment.
4. Update the LAN-node setup guide to use the dedicated remote dependency file
   and the persistent `PATH` mechanism.
5. Update any user-facing usage note that benefits from referencing the remote
   dependency file.
6. Run scoped Markdown warning checks on all touched Markdown files and confirm
   normal final-newline state before closing the task.
