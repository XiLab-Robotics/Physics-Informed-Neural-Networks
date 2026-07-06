# Hard Dataset-First Model Archive Migration

## Overview

Replace the temporary compatibility-preserving model layout with a strict
dataset-first artifact layout:

- keep `models/polished_dataset/`;
- keep `models/simplified_dataset/`;
- remove the old top-level `models/paper_reference/`;
- remove the old top-level `models/exported/`;
- remove the old top-level `models/checkpoints/`.

This document supersedes the compatibility-preserving part of
`doc/technical/2026-07/2026-07-06/2026-07-06-14-28-29_dataset_separated_model_artifact_roots.md`.
The previous document correctly established dataset-separated roots, but it
kept duplicate top-level roots for compatibility. The corrected requirement is
to remove those duplicates after the dataset roots contain the required
artifacts.

No subagent is planned for this implementation.

## Technical Approach

The migration must distinguish three artifact classes:

1. Paper-reference RCIM archives:
   - `simplified_dataset` should contain the existing paper-reference model
     archives that are truly tied to the historical simplified or
     pre-polished surface.
   - `polished_dataset` should contain a paper-reference RCIM archive using the
     same naming convention as the simplified tree. The polished retrained RCIM
     Model-Bank Reproduction archive should be named `rcim_track1`, because it
     is the compatible retrained bank, not a recovered original or retuned
     legacy bank.
2. Model-development exports:
   - existing `models/exported/` is not complete for the polished campaign
     history. The current folder contains only a small Wave 1 curated export
     surface: 15 ONNX, 3 PKL, 12 CKPT, plus metadata.
   - the polished 36-run early-wave campaign and 108-run full-wave campaign
     produced best checkpoints and metadata under `output/training_runs/`, not
     a complete `models/exported/` tree.
   - the expected polished target inventory is therefore 144 model-development
     runs: 48 `global`, 48 `forward`, and 48 `backward` surfaces. Each run
     should receive a Python-side artifact and an ONNX artifact when export is
     supported.
3. Legacy simplified model-development exports:
   - before claiming `simplified_dataset/exported/` is complete, the
     implementation must inventory which historical campaigns actually used
     `simplified_dataset` and which ones have exportable best checkpoints.
   - if only the existing 15 Wave 1 curated exports are available, the
     inventory must say so explicitly instead of implying a 48/48/48 archive.

The final target naming should be consistent across datasets:

- `models/<dataset_id>/paper_reference/rcim_track1/<surface>/...`
- `models/<dataset_id>/exported/<model_family>/<surface>/...`

Surface names should be normalized to:

- `global`;
- `forward`;
- `backward`.

For neural families, the Python-side artifact should be the best `.ckpt`
checkpoint plus the required source-run snapshots (`training_config.yaml`,
`run_metadata.yaml`, `metrics_summary.yaml`, `best_checkpoint_path.txt`). For
tree or scikit-learn families, the Python-side artifact may be the fitted
`.pkl` model where available. Every exported model folder must include
provenance so the dataset identity can be audited without relying on folder
names alone.

The implementation may reuse the existing Wave 1 export functions in
`scripts/reports/closeout/wave1/closeout_wave1_directional_retraining_campaign.py`
as the local pattern for checkpoint-to-ONNX export, but broad polished export
generation should be done through a dedicated repository-owned script rather
than ad hoc shell commands. Because this touches PyTorch/Lightning export
logic, Context7 must be consulted before implementing new library-specific
export code.

## Involved Components

- `models/README.md`
- `models/polished_dataset/`
- `models/simplified_dataset/`
- `models/paper_reference/`
- `models/exported/`
- `models/checkpoints/`
- `output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/`
- `output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/`
- `output/training_runs/`
- `output/registries/families/`
- `scripts/reports/closeout/wave1/closeout_wave1_directional_retraining_campaign.py`
- a new dedicated export/inventory script under `scripts/models/` or
  `scripts/reports/closeout/`
- `doc/README.md`

The active campaign state was checked. The current campaign is completed, but
the protected file list in `doc/running/active_training_campaign.yaml` must not
be modified by this task.

## Implementation Steps

1. Keep the already-created dataset roots, but treat the compatibility-preserved
   top-level copies as temporary.
2. Rename the polished paper-reference archive from
   `models/polished_dataset/paper_reference/rcim_model_bank_reproduction/` to
   `models/polished_dataset/paper_reference/rcim_track1/`.
3. Ensure the simplified paper-reference tree uses the same naming convention:
   `models/simplified_dataset/paper_reference/rcim_track1/` for the accepted
   RCIM Model-Bank Reproduction archive.
4. Inventory the existing simplified paper-reference subtrees and preserve only
   the dataset-relevant paper-reference models under
   `models/simplified_dataset/paper_reference/`.
5. Inventory the 36-run polished early-wave campaign and the 108-run polished
   full-wave campaign from their `campaign_manifest.yaml` and leaderboard
   artifacts. Confirm the expected 48 `global`, 48 `forward`, and 48
   `backward` run split before exporting.
6. Build or adapt a repository-owned export script that:
   - reads campaign manifests;
   - verifies each run has `dataset_id: polished_dataset` and
     `dataset_schema: polished_point_v1`;
   - resolves each best checkpoint;
   - writes a Python-side artifact/provenance bundle;
   - exports an ONNX model where the family supports export;
   - records failures explicitly instead of silently skipping.
7. Run the polished export workflow into
   `models/polished_dataset/exported/<model_family>/<surface>/`.
8. Inventory historical simplified model-development candidates. If no
   complete 48/48/48 simplified export source exists, keep the available
   simplified exports and write the gap into
   `models/simplified_dataset/artifact_inventory.yaml`.
9. Remove the old duplicate top-level roots after the dataset roots have been
   validated:
   - `models/paper_reference/`;
   - `models/exported/`;
   - `models/checkpoints/`.
10. Update `models/README.md`, dataset README files, and inventories to reflect
    the final non-duplicated layout.
11. Verify:
    - no top-level duplicate roots remain;
    - polished paper-reference ONNX source/destination names still match;
    - polished model-development export count matches the expected campaign
      inventory or reports exact unsupported/failure counts;
    - all exported polished entries trace back to `polished_dataset`;
    - simplified entries trace back to `simplified_dataset` or are explicitly
      marked historical/pre-polished.
12. Run Markdown QA on touched Markdown files.
13. Run Python syntax checks and the export script dry-run or inventory mode if
    a new script is added.
14. Check individual files above 100 MB and aggregate staged size before any
    commit request.
