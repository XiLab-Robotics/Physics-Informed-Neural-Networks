# Video Source Bundle Git LFS Dedup And Renaming

## Overview

The current TwinCAT/TestRig video source bundle lives under
`.temp/video_guides/`. The repository already tracks the derived canonical
artifacts, but the original source media remains outside the Git-tracked
surface.

The bundle now needs a durable repository policy because:

- the source videos are useful reference material for future reruns;
- several files exceed GitHub's regular object-size limit;
- the current naming is inconsistent;
- the bundle contains byte-identical duplicates;
- the reference notes still describe the source bundle informally instead of as
  a canonical tracked asset set.

## Technical Approach

The recommended approach is to move the source bundle into a dedicated
reference-owned location, deduplicate the byte-identical files, introduce Git
LFS for the large media files, and rename the surviving source files to a
clearer canonical naming scheme.

The migration should keep the original technical meaning explicit:

1. preserve the `11` unique source artifacts plus the two companion `.txt`
   notes;
2. remove only true duplicates verified by content hash;
3. use a stable naming convention that matches the promoted video-guide slugs;
4. track large video files through Git LFS rather than normal Git objects;
5. update the reference notes and source-manifest documentation so future users
   know exactly which original media file produced each promoted guide.

The current verified duplicate pairs are:

- `Machine_Learning_1.mp4` and `TestRig - Machine_Learning 1.mp4`
- `Machine_Learning_2.mp4` and `TestRig - Machine_Learning 2.mp4`
- `Overview Test Rig.mp4` and `TestRig - Overview.mp4`

The larger files that require LFS rather than regular Git are:

- `Controller_ADRC.mkv` (`704.58 MB`)
- `ML_Simulation_and_Generator_Cam.mkv` (`510.06 MB`)
- `Overview Test Rig.mp4` (`219.08 MB`)
- `Machine_Learning_1.mp4` (`144.13 MB`)
- `FB_ADRC_and_PID.mp4` (`104.49 MB`)

Git LFS is not currently configured in this repository and `git lfs` is not
installed in the current environment, so the implementation must also
initialize the repository policy and document the prerequisite.

## Involved Components

- `.temp/video_guides/`
- `reference/`
- `.gitattributes`
- `.gitignore`
- `doc/reference_codes/video_guides/README.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Define the canonical tracked destination for the source bundle under
   `reference/`.
2. Create a manifest that records source filename, canonical filename,
   extension, size, SHA256 hash, and duplicate relationships.
3. Remove the byte-identical duplicates from the canonical tracked set while
   keeping their duplicate mapping documented.
4. Introduce Git LFS tracking for the video file extensions used by this source
   bundle.
5. Move and rename the unique source files into the canonical reference-owned
   location.
6. Update the relevant reference notes, guide documentation, and pipeline notes
   to point to the new canonical source-bundle location and naming.
