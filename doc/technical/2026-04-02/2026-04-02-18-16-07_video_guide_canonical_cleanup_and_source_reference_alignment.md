# Video Guide Canonical Cleanup And Source Reference Alignment

## Overview

The repository now tracks the canonical TwinCAT/TestRig source media bundle
under `reference/video_guides/source_bundle/` with Git LFS and deduplicated
filenames. However, the promoted canonical report tree under
`doc/reference_codes/video_guides/` still contains three legacy alias-derived
slug folders:

- `testrig___machine_learning_1`
- `testrig___machine_learning_2`
- `testrig___overview`

Those folders no longer correspond to canonical source filenames and now create
an avoidable mismatch between the tracked source bundle and the promoted
documentation surface.

This task will clean up that canonical mismatch, reference each remaining video
guide explicitly to the corresponding tracked source file under
`reference/video_guides/source_bundle/`, and perform a narrow audit pass on the
main repository documentation surface that exposes the video-guide pipeline.

## Technical Approach

The cleanup will treat `reference/video_guides/source_bundle/` as the only
canonical source of truth for the video filenames. The promoted video-guide
tree will be reduced from `11` slug folders to the `8` canonical unique-video
slug folders that correspond to the tracked source media bundle.

For the surviving video-guide folders, the transcript and report Markdown files
will be updated to expose explicit source-video provenance. The preferred shape
is a short source reference block near the top of each document, linking the
guide artifact to its canonical tracked video file and the source-bundle
manifest.

The same pass will update the directory-level index in
`doc/reference_codes/video_guides/README.md` so the canonical report list and
transcript list match the canonical source bundle exactly. The broader
repository surface will be checked briefly so the root README, reference
indices, and pipeline notes remain internally coherent after the duplicate
guide removal.

## Involved Components

- `doc/reference_codes/video_guides/`
- `doc/reference_codes/video_guides/README.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/reference_codes/testrig_twincat_ml_reference.md`
- `doc/guide/project_usage_guide.md`
- `README.md`
- `reference/video_guides/source_bundle/`
- `reference/video_guides/source_bundle/README.md`
- `reference/video_guides/source_bundle/source_manifest.json`

## Implementation Steps

1. Audit the current canonical slug set under `doc/reference_codes/video_guides/`
   against the tracked source bundle under `reference/video_guides/source_bundle/`.
2. Remove the three alias-derived canonical guide folders that no longer map to
   canonical source files.
3. Add explicit source-video provenance references to each remaining canonical
   transcript and report Markdown file.
4. Update `doc/reference_codes/video_guides/README.md` so its promoted-artifact
   description and lists match the canonical `8`-video bundle.
5. Perform a narrow consistency pass across the main reference and usage
   documents that mention the canonical video-guide set.
6. Run Markdown warning checks on the touched Markdown scope and verify final
   newline hygiene before closing the task.
