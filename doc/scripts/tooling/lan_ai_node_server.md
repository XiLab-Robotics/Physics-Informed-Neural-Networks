# `lan_ai_node_server.py`

## Purpose

`scripts/tooling/lan_ai_node_server.py` exposes a repository-owned LAN service
for:

- audio transcription through `faster-whisper`;
- OCR through `PaddleOCR`;
- health checks used by the current workstation before running the video
  workflow.

This server is intended to run on the stronger second workstation, while the
repository and the main terminal remain on the current workstation.

## Recommended Deployment Shape

### Current Workstation

Use the current workstation for:

- repository editing;
- workflow execution;
- report generation;
- final artifact review.

### Second Workstation

Use the second workstation for:

- `LM Studio`;
- `lan_ai_node_server.py`;
- Whisper model downloads;
- OCR runtime installation;
- heavy inference.

## First-Time Setup On The Second Workstation

### 1. Install The Repository Runtime

Create and activate a Python environment:

```powershell
conda create -y -n standard_ml_lan_node python=3.12
conda activate standard_ml_lan_node
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If GPU-backed Paddle is desired, install the appropriate Paddle runtime for that
machine after the base requirements are installed. The exact package depends on
the supported CUDA build for the remote node.

### 2. Install And Prepare LM Studio

On the second workstation:

1. install `LM Studio`;
2. enable the local server;
3. enable LAN exposure only on the trusted local network;
4. configure an API token;
5. download the chosen cleanup/report model.

Recommended starting point:

- one general text model for cleanup and report synthesis;
- optional later addition of a vision-capable model if snapshot analysis is
  extended beyond OCR.

### 3. Choose Network Ports

Recommended default ports:

- `1234` for `LM Studio`
- `8765` for `lan_ai_node_server.py`

### 4. Set The Shared Bearer Token

Set a shared bearer token on the second workstation before starting the server:

```powershell
$env:STANDARDML_LAN_AI_TOKEN="choose_a_strong_token_here"
```

For persistent setup, store the same value as a user environment variable.

## Starting The LAN AI Node Server

Run this on the second workstation:

```powershell
conda activate standard_ml_lan_node
python -B scripts/tooling/lan_ai_node_server.py --host 0.0.0.0 --port 8765 --whisper-model large-v3 --whisper-device cuda --whisper-compute-type float16
```

If CUDA is not ready yet, use:

```powershell
python -B scripts/tooling/lan_ai_node_server.py --host 0.0.0.0 --port 8765 --whisper-model large-v3 --whisper-device cpu --whisper-compute-type int8
```

## Recommended Remote Access From The Current Workstation

### Preferred Method: OpenSSH Server On Windows

Enable `OpenSSH Server` on the second workstation and allow inbound port `22`
on the local network.

Then, from the current workstation:

```powershell
ssh remote_user@remote_host
```

This gives one consistent terminal-centric operating model and avoids requiring
PowerShell remoting configuration up front.

### Start The Server Remotely

Once `ssh` works, launch the server from the current workstation:

```powershell
ssh remote_user@remote_host "cd 'C:\path\to\StandardML - Codex'; conda activate standard_ml_lan_node; python -B scripts/tooling/lan_ai_node_server.py --host 0.0.0.0 --port 8765 --whisper-model large-v3 --whisper-device cuda --whisper-compute-type float16"
```

If the shell on the remote host does not inherit `conda activate` correctly,
use the explicit interpreter path from the environment instead.

### Check Health From The Current Workstation

```powershell
curl.exe -H "Authorization: Bearer YOUR_TOKEN" http://REMOTE_HOST:8765/health
```

Expected response shape:

```json
{
  "status": "ok",
  "faster_whisper_available": true,
  "paddleocr_available": true
}
```

## Environment Variables On The Current Workstation

The repository workflow can use these variables:

```powershell
$env:STANDARDML_LAN_AI_BASE_URL="http://REMOTE_HOST:8765"
$env:STANDARDML_LAN_AI_TOKEN="YOUR_TOKEN"
$env:LM_STUDIO_BASE_URL="http://REMOTE_HOST:1234"
$env:LM_STUDIO_API_KEY="YOUR_LM_STUDIO_TOKEN"
```

These can also be stored as persistent user environment variables.

## Running The Video Workflow From The Current Workstation

Once the remote services are available, the current workstation can run the
high-quality workflow directly:

```powershell
python -B scripts/tooling/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider lan --transcript-model large-v3 --cleanup-model qwen3:14b --report-model qwen3:14b
```

This keeps all orchestration, files, and final reports on the current
workstation while using the second workstation only as the inference backend.

## Suggested Operational Routine

1. Start `LM Studio` on the second workstation.
2. Start `lan_ai_node_server.py` on the second workstation.
3. Verify `/health` and the `LM Studio` endpoint from the current workstation.
4. Run the repository workflow from the current workstation.
5. Stop or leave the remote services running depending on your normal usage.

## Fallback Behavior

If the remote node is not available:

- switch transcript provider back to `google` or a future local-only mode;
- switch OCR provider back to `local`;
- keep the generated analysis and reports on the current workstation.

The repository workflow should treat the LAN node as the preferred production
path, not as the only possible path.
