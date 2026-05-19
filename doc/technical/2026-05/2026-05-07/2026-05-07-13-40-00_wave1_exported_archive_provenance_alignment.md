# Wave 1 Exported Archive Provenance Alignment

## Overview

The current `Wave 1` directional closeout already materializes the requested
`models/exported/` surface for every family and direction scope, but it only
stores the deployment-facing model binaries:

- `python/` model artifacts (`.pkl` for tree estimators and `.ckpt` for
  PyTorch Lightning models);
- `onnx/` deployment exports;
- one root inventory describing the selected winners.

This is intentionally lighter than the curated archive contract already used in
`models/paper_reference/rcim_original/` and
`models/paper_reference/rcim_track1/`, where every promoted model bundle also
preserves provenance, source-run snapshots, and human-auditable archive
documentation.

The requested follow-up is to align the `Wave 1` exported archive with that
fuller archival discipline instead of keeping it as a binary-only delivery
surface.

## Technical Approach

The implementation should extend `models/exported/` from a simple export drop
to a curated archive bundle with the same traceability principles used by the
paper-reference branches, while preserving the current Wave 1 family and scope
taxonomy:

- `models/exported/<family>/global/`
- `models/exported/<family>/forward/`
- `models/exported/<family>/backward/`

For each family/scope archive, the closeout pipeline should preserve:

1. the selected winner identity and ranking metrics;
2. the copied `python/` and `onnx/` model artifacts;
3. the canonical source-run metadata needed to reconstruct where the winner
   came from;
4. the dataset-configuration provenance associated with that scope;
5. a local README and inventory file that make the archive human-auditable.

The goal is not to force every Python artifact into `.pkl`. Instead, the
archive should preserve the model family's canonical Python-usable format:

- tree families keep `tree_model.pkl`;
- PyTorch families keep `.ckpt` checkpoints;
- all families continue to expose ONNX exports beside the Python artifacts.

This keeps the archive technically correct while matching the provenance and
reconstruction expectations already established by the repository's
paper-reference surfaces.

## Involved Components

- `models/exported/`
- `models/README.md`
- `scripts/reports/closeout/wave1/closeout_wave1_directional_retraining_campaign.py`
- `doc/reports/campaign_results/wave1/`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `output/training_runs/*`
- `output/training_campaigns/wave1/directional_retraining/2026-05-06-16-58-54_wave1_directional_retraining_campaign_2026_05_06_16_07_16/`

## Implementation Steps

1. Extend the Wave 1 closeout archive writer so each family/scope folder under
   `models/exported/` gets its own README and machine-readable inventory.
2. Materialize source-run provenance snapshots inside each family/scope archive,
   using a stable structure such as `source_runs/<run_instance_id>/`.
3. Copy the canonical source-run metadata bundle for each winner, including at
   least:
   - `training_config.yaml`
   - `metrics_summary.yaml`
   - `run_metadata.yaml`
   - `training_test_report.md`
4. Add scope-local dataset provenance, at minimum the dataset config YAML used
   by that winner and any closeout-owned manifest or summary needed to
   reconstruct the direction scope.
5. Refresh the root `models/exported/README.md` and inventory so they describe
   the stronger archive contract instead of only listing the exported model
   binaries.
6. Update the final Wave 1 campaign-results report if necessary so it points to
   the richer archive structure.
7. Run Markdown QA on all touched repository-authored Markdown files.
8. Stop after implementation and report completion without committing, waiting
   for explicit user approval before any Git commit.
