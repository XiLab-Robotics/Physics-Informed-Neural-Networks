# LM Studio LAN AI Node For Video Knowledge Extraction

## Overview

This technical note defines the implementation plan for the approved local/LAN
AI setup based on:

- `LM Studio` as the local LLM server on the second workstation;
- `faster-whisper` as the canonical speech-to-text backend on the second
  workstation;
- `PaddleOCR` as the OCR backend on the second workstation;
- the current workstation as the repository host and workflow orchestrator.

The goal is to keep the repository and day-to-day work on the current PC while
delegating heavy inference workloads to the stronger LAN-accessible workstation.

The implementation target is a repository-owned workflow that can support:

- high-quality Italian transcript extraction for the TwinCAT/TestRig video
  guides;
- transcript cleanup and report generation through a local LLM endpoint;
- OCR-assisted evidence extraction for TwinCAT/TestRig screenshots;
- future reusable LAN inference for other repository tooling;
- remote operation from the current workstation terminal with minimal need to
  physically switch to the second PC after the initial bootstrap.

## Technical Approach

The architecture will use a split-node design.

### Current Workstation

The current workstation will remain responsible for:

- repository storage and versioned scripts;
- workflow orchestration;
- artifact placement under `doc/` and `.temp/`;
- report generation control flow;
- final integration of transcript, snapshots, OCR evidence, and generated
  summaries.

### Second Workstation

The second workstation will host:

- `LM Studio` server for local LLM inference over LAN;
- a repository-owned Python service for STT and OCR endpoints;
- model files and runtime environments for `faster-whisper` and `PaddleOCR`.

The planned service split is:

1. `LM Studio`
   OpenAI-compatible local LLM endpoint for cleanup and report synthesis.
2. `FastAPI` or equivalent repository-owned service
   Endpoint layer for:
   - transcript requests via `faster-whisper`;
   - OCR requests via `PaddleOCR`;
   - optional image-analysis helper endpoints when useful.

This avoids forcing all modalities into a single third-party runtime while still
giving the current workstation a clean LAN API surface.

### Remote-Operation Goal

The intended operator experience is:

1. keep the repository checkout and primary shell on the current workstation;
2. start, stop, and inspect the remote AI node from the current workstation
   whenever feasible;
3. call remote transcript, OCR, and LLM services from local repository scripts;
4. only use the second PC directly for the initial software installation,
   model provisioning, and troubleshooting when remote control is insufficient.

### Planned Access Patterns

The implementation and documentation must cover at least these access modes:

1. direct LAN API calls from the repository scripts on the current workstation;
2. remote shell access from the current workstation to the second PC for
   service startup, health checks, and log inspection;
3. a documented fallback path for manual startup on the second PC when remote
   shell access is not yet configured.

The preferred access shape is:

- use a repository-owned remote-shell procedure from the current workstation to
  bootstrap or restart services on the second PC;
- expose the `LM Studio` and repository-owned STT/OCR endpoints over LAN;
- keep all routine workflow execution on the current workstation terminal.

### Remote Access And Control Scope

The planned implementation must define and document:

- the recommended remote-shell mechanism for Windows-to-Windows operation;
- the commands needed to start or verify the remote services;
- the required hostnames, IPs, ports, and tokens;
- how to confirm service reachability from the current workstation;
- how to recover when the remote node is offline or only partially available.

## Involved Components

- `README.md`
  Register this technical note as required.
- `doc/guide/project_usage_guide.md`
  Must be updated when the LAN workflow becomes runnable.
- `requirements.txt`
  Must be updated if new repository-side dependencies are introduced.
- `scripts/tooling/extract_video_guide_knowledge.py`
  Primary workflow to be adapted from direct provider calls to LAN services.
- `scripts/tooling/analyze_video_guides.py`
  Existing OCR and frame-extraction support.
- `doc/reports/analysis/Local LAN AI Infrastructure Options for Video Knowledge Extraction.md`
  Decision report that justifies this architecture.

Planned new implementation artifacts are expected to include:

- a repository-owned server script for the LAN AI node;
- optional node setup documentation under `doc/guide/` or `doc/scripts/`;
- configuration support for LAN endpoint URLs and model names;
- documentation for remote-shell access, service lifecycle control, and
  day-to-day operator usage from the current workstation.

No subagent usage is planned for this scope.

## Implementation Steps

1. Define the concrete LAN service contract:
   - transcript endpoint;
   - OCR endpoint;
   - LM Studio endpoint configuration.
2. Implement the repository-owned Python service for `faster-whisper` and
   `PaddleOCR` on the second workstation.
3. Document the second-workstation setup procedure for `LM Studio`, model
   loading, API token configuration, LAN exposure, and remote lifecycle
   control.
4. Adapt the repository workflow on the current workstation so
   `extract_video_guide_knowledge.py` can call:
   - local/LAN transcript service;
   - local/LAN OCR service;
   - `LM Studio` for cleanup and report synthesis.
5. Add configuration flags and usage documentation so the workflow can switch
   between local-host and LAN-host execution cleanly.
6. Add a documented operating model that explains:
   - first-time setup on the second PC;
   - how to access that PC from the current workstation terminal;
   - how to start, stop, and verify the services remotely;
   - how to run the repository workflow entirely from the current workstation.
7. Validate the end-to-end path on at least one video and document the expected
   operator workflow.
