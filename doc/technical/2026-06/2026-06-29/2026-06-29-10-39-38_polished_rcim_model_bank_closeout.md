# Polished RCIM Model-Bank Closeout

## Overview

The `polished_dataset_rcim_model_bank_reproduction_2026_06_22` campaign has
completed both direction-specific RCIM Model-Bank Reproduction runs on
`polished_dataset`. The closeout must accept the completed forward and backward
validation artifacts, preserve the campaign state, and document the result
without committing generated model bundles above GitHub's file-size limit.

## Technical Approach

Close the campaign as a normal RCIM Model-Bank Reproduction closeout. Record
the completed forward and backward surfaces separately, because they are
direction-specific model banks and not one destructive scalar competition.

The closeout report will summarize:

- polished dataset root and schema;
- forward and backward run instance identifiers;
- winner families and scalar component metrics;
- Python and ONNX export counts;
- local artifact-size constraints;
- the boundary that this closeout does not run or replace the official
  `TE Curve Verification Pipeline`.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_results/cross_wave/polished_dataset/`
- `output/training_campaigns/cross_wave/polished_dataset/rcim_model_bank_reproduction/polished_dataset_rcim_model_bank_reproduction_2026_06_22/`
- `output/registries/program/track1_exact_paper_best_hyperparameters.yaml`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/README.md`
- `.gitignore`

## Implementation Steps

1. Create campaign-level leaderboard and best-run artifacts that identify both
   directional surfaces and the accepted aggregate closeout result.
2. Create a Markdown campaign-results report and export it to PDF.
3. Validate the real exported PDF.
4. Update the active campaign state to `none` with the completed RCIM polished
   campaign recorded in `last_completed_campaign`.
5. Update the master summary, TE closeout ledger, and RCIM benchmark note.
6. Add narrow ignore rules for generated local RCIM model bundles and runtime
   logs that must not be Git-tracked.
7. Run Markdown QA and commit only GitHub-safe artifacts, leaving local model
   bundles and generated exports untracked.
