# Move Closed Video Rerun Tracking Into Analysis Bundle

## Overview

This scope corrects the location chosen for the archived bookkeeping of the
completed remote high-quality TwinCAT/TestRig video rerun.

The previous archival pass moved the closed rerun files out of the live
`doc/running/` root, but still kept them under `doc/running/completed_video_reruns/`.
That is better than leaving them in the live root, but it is still the wrong
semantic home because the rerun is no longer operational state.

The user approved moving that closed bookkeeping into the dated analysis bundle
for the corresponding rerun, so the final archive should live beside the
campaign sum-up rather than under `doc/running/`.

## Technical Approach

Treat the completed rerun tracking as analysis companion artifacts.

The fix is:

1. move the archived status JSON and checklist from
   `doc/running/completed_video_reruns/...` into
   `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/`;
2. remove the temporary `completed_video_reruns/` location introduced by the
   previous pass;
3. update every live reference that currently points to the temporary archive;
4. keep `doc/running/` reserved only for active or resumable runtime state.

## Involved Components

- `doc/reports/analysis/twincat_video_guides/[2026-04-02]/`
  Target dated analysis bundle for the closed rerun bookkeeping.
- `doc/running/`
  Must no longer host the archived completed rerun bundle.
- `doc/reference_codes/video_guides/README.md`
  Canonical provenance entry point for promoted artifacts.
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
  Cross-reference note that points to the canonical rerun provenance.
- `doc/scripts/tooling/run_remote_high_quality_video_rerun.md`
  Launcher note that must distinguish live files from archived files.
- `doc/scripts/tooling/remote_high_quality_video_pipeline.md`
  Formal pipeline note that must point to the correct closed-bundle location.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that references the rerun tracking files.
- `.codex/skills/twincat-video-knowledge-pipeline/SKILL.md`
  Skill instructions that should point to the correct provenance and archive.
- `README.md`
  Main index that must register this technical note.

## Implementation Steps

1. Move the closed rerun status JSON and checklist into
   `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/`.
2. Remove the temporary completed-rerun archive location under `doc/running/`.
3. Update all references from the temporary archive to the dated analysis
   bundle.
4. Re-check the archived checklist so the three later `.mkv` videos still have
   explicit log paths and the archive semantics stay clear.
5. Run scoped Markdown checks on every touched Markdown file before closing.
