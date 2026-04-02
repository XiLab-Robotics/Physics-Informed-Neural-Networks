# Tooling Documentation Index

This folder groups the repository-owned operational notes for tooling under
`scripts/tooling/`.

## Available Tooling Domains

### LAN AI

- [lan_ai/lan_ai_node_server.md](./lan_ai/lan_ai_node_server.md)
  Windows-first setup and runtime guide for the remote LAN AI workstation,
  including `LM Studio`, `faster-whisper`, `PaddleOCR`, CUDA runtime handling,
  health checks, and troubleshooting.

### Video Guides

- [video_guides/remote_high_quality_video_pipeline.md](./video_guides/remote_high_quality_video_pipeline.md)
  Formal process note for the strongest validated TwinCAT/TestRig video
  knowledge-extraction pipeline.
- [video_guides/run_remote_high_quality_video_rerun.md](./video_guides/run_remote_high_quality_video_rerun.md)
  Launcher note for the tracked one-video-at-a-time rerun workflow.

### Markdown QA

- [markdown/markdown_style_check.md](./markdown/markdown_style_check.md)
  Repository-owned Markdown warning checker and usage notes.
- [markdown/run_markdownlint.md](./markdown/run_markdownlint.md)
  Repository-owned Markdownlint runner and rule-profile usage notes.

### Session Management

- [session/isolated_mode.md](./session/isolated_mode.md)
  Isolated-mode session workflow and integration notes.

## Usage Notes

- Treat this index as the entry point for tooling notes, not `README.md`.
- Keep new tooling notes grouped by domain rather than re-growing a flat
  `doc/scripts/tooling/` root.
- Keep historical technical documents in `doc/technical/`; only stable usage
  notes should live here.
