# TwinCAT Video Source Bundle

## Overview

This folder is the canonical Git-tracked source bundle for the repository-owned
TwinCAT/TestRig video-analysis workflow.

Keep the original source media here and keep runtime-generated intermediate
artifacts under `.temp/video_guides/`.

The large video files in this folder are tracked through Git LFS.

## Runtime Boundary

- Canonical source bundle: `reference/video_guides/source_bundle/`
- Runtime analysis caches: `.temp/video_guides/_analysis*/`
- Runtime tracked rerun logs: `.temp/video_guides/_remote_gptoss_tracked_logs/`
- Runtime tracked rerun intermediate reports: `.temp/video_guides/_remote_gptoss_tracked_reports/`
- Canonical promoted deliverables: `doc/reference_codes/video_guides/`

## Canonical Files

| Canonical file | Original source name | Size bytes | SHA256 |
| --- | --- | ---: | --- |
| `automatic_exp_te.mp4` | `Automatic_Exp_TE.mp4` | `86515204` | `5456eb844a6b4826c7fec1dd31843eead0a83dbaf97cffccb8262a99f1c192dc` |
| `controller_adrc.mkv` | `Controller_ADRC.mkv` | `738810492` | `4dfb6982d01f33d9878151db9bf51e8ba669342dd9b8fe41ea17d15fe6fb00fa` |
| `fb_adrc_and_pid.mp4` | `FB_ADRC_and_PID.mp4` | `109564589` | `c6b40eca7b60a0433b391782c4806d9d82dba0587cea5b3c304966e730587c6f` |
| `machine_learning_1.mp4` | `Machine_Learning_1.mp4` | `151130738` | `72470951ee9b11bcb1c3ce564f78d2d0b05b953db6e26732933d70631b999590` |
| `machine_learning_2.mp4` | `Machine_Learning_2.mp4` | `103270496` | `a7f48dc9469315ac2947df6ee42d4c1e12d1929d00e8eb15d18fc39b4949ae72` |
| `machine_learning_notes.txt` | `Machine Learning - read me.txt` | `445` | `938ccba657df9b3d94b668ff7364ddb025a05b2474274194f98062cba54bc8eb` |
| `ml_simulation_and_generator_cam.mkv` | `ML_Simulation_and_Generator_Cam.mkv` | `534833985` | `420daedabb48bf257680a69a1ec14934fbd36187004ed154c70f0e6bd0fecad3` |
| `ml_simulation_and_generator_cam_errata.txt` | `Errata_Corrige Video ML_Simulation_and_Generation_Cam.txt` | `570` | `e9975e0016720e1dda08c95336e6c76d02cb5f06550b046a771cb3e82fb31e68` |
| `overview_test_rig.mp4` | `Overview Test Rig.mp4` | `229726465` | `519e355ac0ba20800a2488bf2d13710db6f60681575a7d2fe694f9c7d87ff365` |
| `video_errata_corrige_adrc.mkv` | `Video_Errata_Corrige_ADRC.mkv` | `86777083` | `4727a912b19b265bb19bed0699b4e823ede4e155d1565098828116362c457cfa` |

## Deduplication Notes

The source bundle previously contained three duplicate aliases. They were
removed during canonicalization because they were byte-identical to the tracked
canonical files:

- `TestRig - Machine_Learning 1.mp4` -> duplicate of `machine_learning_1.mp4`
- `TestRig - Machine_Learning 2.mp4` -> duplicate of `machine_learning_2.mp4`
- `TestRig - Overview.mp4` -> duplicate of `overview_test_rig.mp4`

The promoted report tree still contains some historical alias-derived slug
folders from the pre-dedup rerun. Treat those as legacy promoted outputs, not
as canonical source filenames.
