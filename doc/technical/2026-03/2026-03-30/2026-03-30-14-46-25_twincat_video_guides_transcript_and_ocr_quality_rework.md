# TwinCAT Video Guides Transcript And OCR Quality Rework

## Overview

The current TwinCAT/TestRig video-analysis pipeline is useful for frame
extraction and coarse indexing, but the transcript and OCR quality are not yet
good enough for reliable technical synthesis. The transcript contains many
recognition errors on spoken Italian technical content, and the OCR excerpts
captured from full-screen frames are often too noisy to be directly useful in
repository-owned reports.

This work reopens the pipeline with a quality-first objective: improve the
signal extracted from the existing video guides so that the resulting reports
retain only technically useful transcript and OCR content for TwinCAT model
export, Beckhoff ML deployment, and TestRig code adaptation analysis.

## Technical Approach

The rework will focus on three changes.

First, the transcription stage will be upgraded from the current lightweight
configuration to a more robust Italian technical ASR path. The pipeline will be
extended to support higher-quality Faster-Whisper models and to persist richer
transcription metadata so that we can compare output quality across model
choices before locking the default settings.

Second, the OCR stage will move away from naive full-frame extraction. The
pipeline will add TwinCAT-oriented OCR preprocessing and selection logic so that
reports prefer only the frame regions and OCR excerpts that are likely to
contain readable UI labels, block names, file names, and Beckhoff model-manager
content. Low-value OCR noise will be filtered out rather than copied verbatim
into the final reports.

Third, the report-generation stage will be refactored so that transcript and
OCR evidence are summarized through quality-gated excerpts. If OCR remains poor
for a given frame, the frame image can still be kept as a reference image, but
the unreadable OCR text will not be surfaced as if it were trustworthy
evidence.

## Involved Components

- `scripts/tooling/analyze_video_guides.py`
- `scripts/tooling/generate_video_guide_reports.py`
- `doc/reference_codes/video_guides/`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Inspect the current transcript and OCR artifacts for the analyzed videos and
   identify the main failure modes.
2. Upgrade the transcription path so the pipeline can run a higher-quality
   Italian technical ASR configuration and persist comparison-friendly metadata.
3. Improve OCR preprocessing and add filtering so noisy full-frame OCR does not
   pollute the reports.
4. Regenerate the analyzed-video artifacts for the main TwinCAT/TestRig videos.
5. Refactor the repository-owned per-video reports so they expose only useful
   transcript and OCR evidence, while preserving the frame references.
6. Update the canonical TwinCAT/TestRig reference notes and usage
   documentation if the improved extraction changes how the pipeline should be
   used.
