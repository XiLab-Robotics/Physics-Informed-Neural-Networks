# Track 1 Backward Paper-Faithful Closeout And Reference Refresh

## Overview

This technical note plans the closeout for the completed Track 1 backward
paper-faithful grid-search campaign launched with:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Backward `
  -Families "SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM" `
  -Stage Search `
  -Remote
```

The campaign artifacts were added in commit
`e03cf44d3f2887c10e084a6d6b58153e45fc4486`. The closeout must promote the
accepted backward models into the paper-reference archive, update linked
documents, and recompile RCIM Paper Reference Benchmark Tables `2`-`5`.

## Technical Approach

Reuse the forward closeout pattern and adapt it to the `backward` direction.
The closeout will resolve the latest `2026-05-15` / `2026-05-16` backward
validation summaries for the `11` operational Track 1 families, refresh
`models/paper_reference/rcim_track1/backward`, and update canonical reports.

The closeout must preserve the existing forward archives and replace only the
older backward archives trained with the previous pipeline.

The report/PDF should use the reusable styled-PDF table layout rules already
added for the forward closeout where the same table shapes appear.

## Involved Components

- `scripts/reports/closeout/track1/closeout_track1_forward_paper_faithful_grid_search_campaign.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/track1/exact_paper/backward/`
- `models/paper_reference/rcim_track1/backward/`
- `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/`

`doc/running/active_training_campaign.yaml` is listed in the active campaign
state as a protected file. The implementation must not modify it until the user
explicitly approves this technical note and the protected-file edit.

No subagent is planned for this closeout.

## Implementation Steps

1. Inspect the backward validation summaries and confirm all `11` families have
   Python and ONNX exports for all `19` targets.
2. Add or generalize a closeout script so it can run the backward
   paper-faithful closeout without disturbing the completed forward archive.
3. Refresh `models/paper_reference/rcim_track1/backward` for all accepted
   families, including `ELM`.
4. Update linked model archive READMEs and root paper-reference documentation.
5. Recompile backward rows in RCIM Paper Reference Benchmark Tables `2`-`5`
   with green/yellow/red status markers and no pending cells.
6. Update Training Results Master Summary and campaign closeout artifacts,
   including `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
   `campaign_best_run.md`.
7. Mark the active campaign state as completed for the full bidirectional
   campaign and point it to the backward closeout report.
8. Generate the Markdown and PDF closeout report, validate the exported PDF,
   and inspect the rasterized pages.
9. Run scoped Markdown, Python, Sphinx, archive-inventory, and Git size checks
   before reporting completion.
