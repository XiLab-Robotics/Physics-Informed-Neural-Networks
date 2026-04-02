# Three Stage High Quality Video Knowledge Extraction Workflow

## Overview

The current repository-owned TwinCAT/TestRig video-analysis pipeline improved
the first OCR and transcript pass, but it still does not meet the actual
knowledge-extraction goal for these Italian technical video guides.

The revised objective is to stop treating transcription, snapshots, and OCR as
rough auxiliary artifacts and instead make them three explicit workflow stages:

1. produce a full high-quality Italian transcript for each video;
2. extract only meaningful reference snapshots that capture important technical
   evidence;
3. use OCR as an analysis-side evidence source, not as a noisy report payload.

The deliverable should be one complete report per analyzed video, supported by
a corrected transcript file, curated snapshots, OCR-assisted evidence, and any
other repository-owned analysis required to improve the TwinCAT/TestRig
documentation.

## Technical Approach

The workflow will be rebuilt around three main stages.

For Stage 1, the repository will no longer rely on a local lightweight
speech-to-text pass as the canonical transcript source. The preferred path will
be a high-quality API transcription workflow for Italian technical speech, then
a second AI cleanup pass that corrects recognition errors, restores lexical and
grammatical quality in Italian, and rewrites the transcript only within the
meaning actually supported by the audio. The repository output for each video
will be a dedicated Markdown transcript file that is coherent, readable, and
context-preserving.

For Stage 2, frame extraction will change from time-based coarse sampling to
evidence-driven snapshot selection. The workflow should identify moments that
matter for TwinCAT/TestRig understanding: block diagrams, PLC task timing,
TwinCAT project trees, Beckhoff ML configuration windows, model-manager
screens, experiment programs, and simulation-support views. The selected images
must be saved under the corresponding report-local `assets/` directory and then
integrated into the final report as real supporting evidence.

For Stage 3, OCR will be retained as an analysis-side tool, but it will stop
being a direct report section. OCR output should be used to recover code
identifiers, function-block names, model file names, path fragments, screen
labels, and configuration clues that help interpret the transcript and the
snapshots. That OCR evidence should then be fused with the transcript and the
snapshot review to build the final report and to update the canonical TwinCAT
reference documentation.

Given the user's explicit request for the best available speech-to-text APIs,
the implementation should verify and select a high-quality external STT service
before coding the repository wrapper. The expected baseline is to compare at
least modern API-grade options rather than locking the workflow to the current
local-only pass.

## Involved Components

- `scripts/tooling/analyze_video_guides.py`
- `scripts/tooling/generate_video_guide_reports.py`
- `.temp/video_guides/`
- `.temp/video_guides/_analysis/`
- `doc/reference_codes/video_guides/`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`
- `doc/guide/project_usage_guide.md`
- `README.md`

## Implementation Steps

1. Review the currently generated transcript, OCR, and report artifacts and
   isolate which outputs remain too noisy to keep as canonical evidence.
2. Evaluate current high-quality speech-to-text API options for Italian
   technical speech and choose the repository default together with a fallback
   path.
3. Implement Stage 1 transcript generation so each analyzed video produces a
   full corrected Italian transcript Markdown file.
4. Implement Stage 2 snapshot selection so report-local assets are chosen from
   meaningful technical moments instead of broad time-based sampling alone.
5. Refactor Stage 3 OCR so OCR text is used internally for analysis and report
   synthesis but is no longer emitted as a noisy standalone report section.
6. Regenerate the main TwinCAT/TestRig video artifacts with the new workflow.
7. Rebuild the per-video reports so they integrate transcript evidence,
   important snapshots, OCR-assisted findings, and final engineering
   conclusions.
8. Update the TwinCAT reference documentation and usage guide to reflect the
   new three-stage workflow.
