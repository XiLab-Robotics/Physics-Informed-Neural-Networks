# Remote High-Quality Video Rerun Launcher

## Overview

This launcher is the repository-owned wrapper for the strongest currently
validated TwinCAT/TestRig video-guide path:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` with `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for transcript cleanup and report generation;
- local OCR fallback for snapshot evidence when the remote OCR path is unstable.

Unlike a blind batch run, the launcher processes one video at a time, writes a
persistent status file, and stops immediately on the first failing video.

By default it now auto-discovers all supported source videos under
`reference/video_guides/source_bundle/` instead of assuming only the original
`.mp4` subset.

## Main Role

The launcher:

1. forces the workflow to use the remote `LM_STUDIO_BASE_URL` instead of any
   local-only `LM_STUDIO_LOCAL_URL`;
2. preserves explicit per-video progress through a repository-owned checklist;
3. reuses cached artifacts when a rerun resumes after a timeout;
4. validates the generated transcript and report Markdown before marking a
   video as complete.

## Runtime State

During execution the launcher writes:

- `doc/running/remote_high_quality_video_rerun_status.json`
- `doc/running/remote_high_quality_video_rerun_checklist.md`

These files expose the current video, current stage coverage, and the last
failure location if the batch stops.

After a rerun is reviewed, promoted, and closed out, move those files into:

- `doc/reports/analysis/twincat_video_guides/[YYYY-MM-DD]/runtime_tracking/`

The first archived closed-out bundle is:

- `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/`

## Practical Use

Start the tracked remote rerun from the repository root:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1 -PythonExecutable python
```

Override the discovered set explicitly when needed:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1 -VideoNameList "Machine_Learning_2","Controller_ADRC"
```

The launcher expects the current workstation to already expose:

- `STANDARDML_LAN_AI_TOKEN`
- `LM_STUDIO_API_KEY`
- `STANDARDML_LAN_AI_BASE_URL`
- `LM_STUDIO_BASE_URL`

The remote `LM Studio` server and the remote LAN AI node must already be
running before the launcher starts.

Supported source extensions for auto-discovery:

- `.mp4`
- `.mkv`
- `.mov`
- `.avi`
- `.m4v`
