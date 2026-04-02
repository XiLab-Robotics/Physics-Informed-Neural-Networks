# Remote High-Quality TwinCAT Video Pipeline

## Purpose

This note formalizes the strongest currently validated repository-owned workflow
for TwinCAT/TestRig video knowledge extraction.

Use this pipeline when the goal is:

- canonical transcript quality rather than rough indexing;
- strong per-video technical reports with snapshot evidence;
- cross-video TwinCAT/TestRig knowledge synthesis for future model-export work;
- reproducible tracked reruns with explicit stop-on-failure behavior.

## Validated Runtime Topology

### Current Workstation

Keep the repository, orchestration, logs, canonical docs, and final promoted
artifacts on the current workstation.

### Remote Workstation

Run the heavier inference services on the second workstation:

- `lan_ai_node_server.py`;
- `faster-whisper` with `large-v3`;
- `LM Studio`;
- `openai/gpt-oss-20b` as the preferred cleanup/report model.

### OCR Path

Use local OCR fallback on the current workstation when the remote OCR path is
less stable than transcription and LLM inference.

## Canonical Runtime Configuration

The preferred tracked path is:

- transcript provider: `lan`
- cleanup provider: `lmstudio`
- report provider: `lmstudio`
- OCR provider: `local`
- transcript model: `large-v3`
- cleanup model: `openai/gpt-oss-20b`
- report model: `openai/gpt-oss-20b`

## Required Environment Variables

The current workstation should expose:

- `STANDARDML_LAN_AI_TOKEN`
- `STANDARDML_LAN_AI_BASE_URL`
- `LM_STUDIO_API_KEY`
- `LM_STUDIO_BASE_URL`

Optional local-only validation variable:

- `LM_STUDIO_LOCAL_URL`

## Preconditions

Before starting the tracked rerun:

1. the remote workstation must keep `LM Studio` running;
2. the remote workstation must keep `lan_ai_node_server.py` running;
3. the current workstation must reach ports `1234` and `8765`;
4. the requested cleanup/report model must be visible through
   `LM_STUDIO_BASE_URL/v1/models`.

Use these checks from the current workstation:

```powershell
Test-NetConnection 155.185.226.100 -Port 8765
Test-NetConnection 155.185.226.100 -Port 1234
curl.exe -H "Authorization: Bearer $env:STANDARDML_LAN_AI_TOKEN" "$env:STANDARDML_LAN_AI_BASE_URL/health"
curl.exe -H "Authorization: Bearer $env:LM_STUDIO_API_KEY" "$env:LM_STUDIO_BASE_URL/v1/models"
```

## Canonical Launcher

Use the tracked launcher instead of a blind loop:

```powershell
.\scripts\tooling\run_remote_high_quality_video_rerun.ps1
```

The launcher now auto-discovers supported video files under
`.temp/video_guides/` with these extensions:

- `.mp4`
- `.mkv`
- `.mov`
- `.avi`
- `.m4v`

You can still override the target set explicitly:

```powershell
.\scripts\tooling\run_remote_high_quality_video_rerun.ps1 -VideoNameList "Machine_Learning_2","Controller_ADRC"
```

## What The Launcher Guarantees

The tracked launcher:

1. forces use of the remote `LM_STUDIO_BASE_URL` instead of any local-only
   validation URL;
2. processes one video at a time;
3. writes persistent run state under `doc/running/`;
4. stops on the first failing video instead of silently continuing;
5. validates transcript/report Markdown before marking a video complete.

## Runtime Outputs

### Temporary Analysis Roots

- `.temp/video_guides/_analysis_hq_remote_gptoss_tracked/`
- `.temp/video_guides/_remote_gptoss_tracked_reports/`
- `.temp/video_guides/_remote_gptoss_tracked_logs/`

### Persistent Tracking Files

- `doc/running/remote_high_quality_video_rerun_status.json`
- `doc/running/remote_high_quality_video_rerun_checklist.md`

### Canonical Promoted Outputs

After review and promotion, the final tracked deliverables live under:

- `doc/reference_codes/video_guides/`

## Per-Video Stage Model

Each video is tracked through these stages:

- transcript extraction;
- cleanup;
- snapshot selection;
- OCR evidence copy;
- transcript Markdown save;
- report Markdown save;
- Markdown validation.

This stage model is visible in the checklist and status JSON.

## Quality Gates

Treat a rerun as canonical only when:

1. all tracked videos complete the full stage set;
2. transcript Markdown exists and passes repository checks;
3. report Markdown exists and passes repository checks;
4. the promoted reports are reviewed against the repository’s TwinCAT/TestRig
   reference notes;
5. the final promoted tree is mirrored into `doc/reference_codes/video_guides/`
   with provenance preserved.

## Failure And Recovery Policy

The pipeline is designed to fail loudly.

Typical failure classes:

- remote LAN node timeout;
- remote `LM Studio` model crash or reload;
- malformed cleanup JSON;
- transcript/report Markdown not saved or not validated.

Recovery policy:

1. fix the remote runtime problem;
2. rerun the tracked launcher;
3. let the launcher skip already validated videos and resume from the first
   incomplete one.

## When To Use Local Validation Instead

Use the local-only path only for:

- smoke-testing workflow changes;
- prompt-budget debugging for small local models;
- validation of fallback URL or model-selection behavior.

Do not treat the local path as the canonical knowledge-refresh route when the
remote runtime is available.

## Integration Targets

The outputs of this pipeline should feed:

- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`
- `doc/reports/analysis/twincat_video_guides/`

That is the intended chain:

video artifacts -> per-video reports -> cross-video synthesis -> TwinCAT/TestRig
implementation knowledge.
