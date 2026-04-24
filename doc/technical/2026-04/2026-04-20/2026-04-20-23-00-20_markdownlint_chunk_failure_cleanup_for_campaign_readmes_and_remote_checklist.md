# 2026-04-20-23-00-20 Markdownlint Chunk Failure Cleanup For Campaign Readmes And Remote Checklist

## Overview

This technical document covers a narrow Markdown QA repair required after the
repository chunked `markdownlint-cli2` quality check failed on a small set of
authored Markdown files.

The reported failures are limited to two structural issues:

- missing blank-line separation between the attempt-summary table and the
  following bullet list in multiple residual-closure campaign package
  `README.md` files under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`;
- an extra blank line in `doc/running/remote_training_campaign_checklist.md`.

The goal is to make the minimum structural edits needed so the touched
Markdown files pass the repository Markdown QA commands without changing the
meaning of the campaign package descriptions or the running-state checklist.

## Technical Approach

The repair should stay strictly local to the warning sites reported by CI.

For the campaign package `README.md` files, the current table is immediately
followed by the configuration-file bullet list. `markdownlint-cli2` correctly
reports this as:

- `MD058/blanks-around-tables`
- `MD032/blanks-around-lists`

The fix is to insert one blank line after the closing table row and before the
first list item in each affected campaign package `README.md`. No other
wording, headings, or file lists should be rewritten.

For `doc/running/remote_training_campaign_checklist.md`, the fix is to remove
the single repeated blank line that triggers `MD012/no-multiple-blanks`.

The currently recorded campaign state in `doc/running/active_training_campaign.yaml`
is marked `finished`. The protected-file list still includes some campaign
package files, but the reported target `doc/running/remote_training_campaign_checklist.md`
is not listed in the inspected protected-file section. The implementation will
therefore avoid unrelated protected files and only touch the exact Markdown
files required by the lint failure.

No subagent is planned for this work. The task is a local Markdown QA repair,
and any subagent use would require explicit user approval before launch.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/dt/2026-04-19_track1_dt_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/ert/2026-04-19_track1_ert_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/et/2026-04-19_track1_et_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/gbm/2026-04-19_track1_gbm_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/hgbm/2026-04-19_track1_hgbm_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/lgbm/2026-04-19_track1_lgbm_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/mlp/2026-04-19_track1_mlp_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/rf/2026-04-19_track1_rf_residual_cellwise_closure_campaign/README.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/residual_cellwise_closure/xgbm/2026-04-19_track1_xgbm_residual_cellwise_closure_campaign/README.md`
- `doc/running/remote_training_campaign_checklist.md`
- `scripts/tooling/markdown/run_markdownlint.py`
- `scripts/tooling/markdown/markdown_style_check.py`
- `doc/technical/2026-04/2026-04-20/README.md`
- `doc/README.md`

## Implementation Steps

1. Insert one separating blank line between the attempt-summary table and the
   configuration-file bullet list in each affected campaign package
   `README.md`.
2. Remove the repeated blank line in
   `doc/running/remote_training_campaign_checklist.md`.
3. Confirm that all touched Markdown files end with one normal final newline.
4. Run the repository Markdown QA commands on the touched Markdown scope:
   `python -B scripts/tooling/markdown/run_markdownlint.py` and
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`.
5. Report the repair result and stop without creating a Git commit unless the
   user later asks for one explicitly.
