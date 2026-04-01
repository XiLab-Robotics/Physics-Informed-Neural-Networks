# Tesseract OCR And Full Video Reports For TwinCAT Guides

## Overview

The repository already contains a first repository-owned pipeline for TwinCAT
video-guide analysis through:

- `scripts/tooling/analyze_video_guides.py`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `.temp/video_guides/_analysis/`

The user now explicitly requested the next deeper phase:

- install and use Tesseract so OCR is no longer skipped on the current
  workstation;
- rerun the analysis on the most relevant TwinCAT/TestRig videos with OCR
  enabled;
- create a complete report for each analyzed video, including summary,
  extracted key technical points, important notes, and reference images.

This work extends the current pipeline from "artifact extraction" to
"artifact extraction plus repository-owned per-video knowledge reports".

Because this phase changes repository tooling and documentation structure, it
must be approved explicitly before implementation continues.

## Technical Approach

The work should proceed in five stages after explicit approval.

### 1. Enable OCR On The Local Workstation

The current environment already has `pytesseract`, but the Tesseract
executable is missing, so OCR is skipped.

The approved implementation should:

- install Tesseract on the local machine;
- verify that the executable is discoverable by the current Python
  environment;
- rerun the repository-owned video-analysis script with OCR enabled.

This is a workstation-level dependency step, not just a repository file edit,
so it should be treated as an explicit environment modification.

### 2. Strengthen The Video-Analysis Pipeline For Report Generation

The current script produces inventory, transcript, frame-sampling, and summary
artifacts, but not yet a complete repository-owned report for each analyzed
video.

The approved implementation should extend the tooling so that each analyzed
video produces a more complete Markdown report capturing:

- video identity and scope;
- runtime metadata;
- transcript-backed summary;
- OCR-backed UI/code observations;
- extracted variables, function blocks, task-cycle references, file paths,
  model names, and workflow steps;
- important warnings, errata, and open uncertainties;
- embedded or linked reference images sampled from the video.

### 3. Create Stable Repository-Owned Per-Video Reports

The current raw artifacts should remain under `.temp/video_guides/_analysis/`.

In addition, the approved work should create stable repository-owned report
documents under a canonical documentation location such as:

- `doc/reference_codes/video_guides/`

The per-video reports should be human-readable and suitable for later TwinCAT
implementation work, rather than being only machine-oriented dumps.

Each report should include at least:

- `Overview`
- `Video Scope`
- `Key Technical Findings`
- `Important Notes And Caveats`
- `Reference Images`
- `Potential Impact On TwinCAT Model Deployment`

### 4. Build A Cross-Video Synthesis Layer

After the per-video reports are generated, the approved workflow should update
the repository-level synthesis so the most important conclusions become easier
to reuse.

This phase should update:

- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`

The updated synthesis should clearly distinguish:

- evidence confirmed by imported TwinCAT code;
- evidence confirmed by video speech or screen content;
- engineering inference drawn from combining both.

### 5. No Subagent Planned For This Extension

No subagent is planned for this extension.

The work remains tightly coupled to repository-local tooling, local
workstation setup, and repository documentation structure.

If a later documentation-review subagent becomes useful, that would require a
new explicit proposal and runtime approval.

## Involved Components

- `scripts/tooling/analyze_video_guides.py`
  Existing repository-owned video-analysis pipeline to extend.
- `.temp/video_guides/`
  Source video bundle and companion notes.
- `.temp/video_guides/_analysis/`
  Raw extraction output root to reuse and enrich.
- future `.temp/video_guides/_analysis_full_inventory/`
  Optional inventory-only output root for full-bundle scans.
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
  Current repository-owned note for the video-guide workflow.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Canonical TwinCAT/TestRig ML reference note that should absorb the most
  important reusable conclusions.
- future `doc/reference_codes/video_guides/`
  Proposed canonical location for stable per-video reports.
- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/project_usage_guide.md`
  User-facing guide that may need updated OCR and reporting usage instructions.
- local Tesseract installation path
  Workstation-level dependency required for OCR execution.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before installing Tesseract or modifying the
   current tooling.
3. Install Tesseract on the workstation and verify executable discovery from
   the Python environment used by the repository.
4. Extend `scripts/tooling/analyze_video_guides.py` so OCR-backed report
   generation is part of the repository workflow.
5. Rerun the analysis on the most relevant TwinCAT/TestRig videos with OCR
   enabled.
6. Create one complete repository-owned report for each analyzed video under
   the chosen canonical documentation location.
7. Update the cross-video TwinCAT synthesis notes with the newly OCR-backed
   findings.
8. Update user-facing usage instructions if the workflow or prerequisites
   changed materially.
9. Run Markdown warning checks on the touched Markdown files and fix local,
   straightforward issues before closing the task.
10. Report completion and wait for explicit user approval before any Git
    commit.
