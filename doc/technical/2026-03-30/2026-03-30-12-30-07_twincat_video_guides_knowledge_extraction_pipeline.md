# TwinCAT Video Guides Knowledge Extraction Pipeline

## Overview

The repository already contains TwinCAT deployment context in:

- `doc/technical/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
- `doc/technical/2026-03-26/2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`

The user has now provided additional repository-local source material under
`.temp/video_guides/`.

Those videos and companion notes appear to document how the TestRig TwinCAT
code was created, how the current machine-learning integration works in
practice, how simulation assets are prepared, and what implementation caveats
or errata must be preserved.

The requested outcome is to define the best practical path to analyze those
videos automatically, extract the TwinCAT-relevant knowledge they contain, and
integrate the resulting facts into repository-owned documentation so that
future work can:

- generate ML models in a TwinCAT-usable form with fewer blind spots;
- understand how the existing TestRig PLC code expects those models;
- adapt the TwinCAT code for model families that differ from the paper's
  original deployment path.

No implementation code should be written before explicit approval of this
technical document.

## Technical Approach

The recommended path is a staged, repository-owned extraction pipeline rather
than direct manual note-taking from the videos.

### 1. Build A Reproducible Video-Ingestion Workflow

The first approved implementation should create a local analysis pipeline for
the contents of `.temp/video_guides/`.

That pipeline should process each video through four extraction layers:

- media inventory and duration metadata;
- audio transcription with timestamps;
- scene or keyframe extraction for visually meaningful steps;
- OCR or slide-text extraction from the selected frames.

This path is preferable to a transcript-only workflow because the TwinCAT
videos likely contain:

- code windows;
- block-diagram screens;
- file-path references;
- variable names;
- simulation table columns;
- TwinCAT project views;
- configuration values not reliably recoverable from speech alone.

### 2. Produce Structured Per-Video Knowledge Notes

The pipeline should not stop at raw transcript generation.

For each video, it should produce a repository-owned Markdown note that
separates:

- confirmed spoken claims;
- visually confirmed code or UI evidence;
- inferred conclusions that still need manual confirmation;
- extracted identifiers such as function-block names, file paths, variables,
  model artifacts, simulation columns, and operating assumptions.

The companion text files already present in `.temp/video_guides/` should be
ingested as first-class evidence because they contain immediate corrections and
schema hints, including:

- simulation column names;
- clarification that `TE_Calc` is computed directly in TwinCAT rather than read
  from a Matlab-produced variable in the way the video suggests;
- the Matlab helper file `Extra_Data_For_Simul_TC_Cam` as a relevant artifact
  for simulation-vector preparation.

### 3. Synthesize A TwinCAT-Facing Consolidated Reference

After per-video extraction, the approved workflow should generate one
consolidated repository-owned reference note that answers the project's actual
deployment questions:

- how models must be prepared to match the current TwinCAT/TestRig runtime;
- which parts of the current pipeline are paper-specific versus more general;
- which assumptions are hard-coded in the PLC side;
- what would have to change to support different model structures.

This synthesis should update or extend
`doc/reference_codes/testrig_twincat_ml_reference.md` rather than leaving the
video knowledge isolated in `.temp/`.

If the extracted content becomes large, a companion note tree under
`doc/reference_codes/video_guides/` should be added, with the main
`testrig_twincat_ml_reference.md` note remaining the canonical summary.

### 4. Capture Adaptation Rules For New Model Families

The final synthesized documentation should explicitly distinguish at least
three deployment cases:

- current legacy harmonic multi-engine deployment already evidenced by the
  TestRig PLC code;
- model families that can be reduced to the same harmonic-amplitude and
  phase-based runtime contract;
- model families that would require TwinCAT-side code changes because they do
  not match the current multi-model harmonic reconstruction structure.

This is the part that matters most for future engineering decisions.

The documentation should aim to answer:

- when a trained Python model can be exported without changing TwinCAT logic;
- when a model must be decomposed or approximated before export;
- when the PLC code itself must be modified;
- which intermediate quantities must stay inspectable for deployment safety.

### 5. Package The Workflow Only After It Stabilizes

A repository skill may be useful, but only after the workflow is proven once on
the current video bundle.

The recommended order is:

1. implement a first repository-owned extraction pipeline;
2. validate the output quality on the current `.temp/video_guides/` set;
3. only then create a dedicated skill if the workflow is repeatable enough to
   deserve a permanent operational guide.

Creating the skill first would lock in a workflow before the extraction and
documentation stages have been validated on real repository material.

### 6. No Subagent Planned For The Initial Approved Implementation

No subagent is planned for the initial implementation scope.

The work is tightly coupled to repository documentation structure and the user
explicitly requires a controlled evaluation of the feasible paths before any
automation is built.

If later validation would benefit from a dedicated documentation-review or
tooling-review subagent, that future proposal must be documented separately and
still requires explicit user approval at runtime.

## Involved Components

- `.temp/video_guides/`
  Source videos and companion notes to analyze.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Canonical TwinCAT/TestRig ML reference note that should absorb the relevant
  extracted knowledge.
- `doc/technical/2026-03-26/2026-03-26-15-43-43_twincat_ml_export_and_testrig_reference_analysis.md`
  Existing TwinCAT/TestRig technical rationale that defines the current legacy
  deployment baseline.
- `doc/technical/2026-03-26/2026-03-26-15-59-15_post_campaign_twincat_deployment_evaluation_and_isolated_parallel_track.md`
  Existing note that frames the legacy and newer Beckhoff deployment branches.
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
  Summary source for the paper-backed feature set and deployment assumptions.
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
  Summary source for `DataValid`, warm-up, target temperature, and encoder
  zeroing workflow.
- `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`
  Summary source for encoder semantics, cumulative angle meaning, and `DataValid`
  extraction boundaries.
- future repository tooling script
  Expected implementation location for the approved video-analysis pipeline.
- future repository documentation notes
  Expected destination for per-video extraction notes and consolidated
  TwinCAT-facing synthesis.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before implementing any extraction tooling or
   modifying repository code beyond this planning note.
3. After approval, inspect the available local tooling for media probing,
   transcription, frame extraction, and OCR feasibility.
4. Implement a first-pass repository-owned video-analysis pipeline that
   generates:
   - media inventory metadata;
   - timestamped transcripts;
   - selected keyframes;
   - OCR text;
   - per-video structured Markdown notes.
5. Run the pipeline on the current `.temp/video_guides/` bundle and review the
   quality of the extracted evidence.
6. Synthesize the relevant findings into the canonical TwinCAT/TestRig
   reference documentation and clearly separate confirmed facts from inference.
7. Add explicit guidance on how to:
   - prepare models that fit the current TwinCAT runtime contract;
   - recognize when TwinCAT code changes are required for different model
     families.
8. Decide whether the now-validated workflow should be formalized as a new
   repository skill for future reuse.
9. Run Markdown warning checks on the touched Markdown files and fix local,
   straightforward issues before closing the task.
10. Report completion and wait for explicit user approval before any Git
    commit.
