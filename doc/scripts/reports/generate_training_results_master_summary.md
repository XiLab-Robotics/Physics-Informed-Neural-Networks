# Training Results Master Summary Generator

## Overview

`scripts/reports/generate_training_results_master_summary.py` builds the
canonical always-updated project summary for TE-model training results.

The report is intended to be the main colleague-facing control surface for:

- current project status;
- implemented versus planned families;
- current best result per family;
- cross-family comparison;
- family-local ranked result breakdowns;
- recent campaign changes and current operational focus.

## Main Role

The generator consolidates information from the canonical repository sources:

- `doc/running/te_model_live_backlog.md`
- `doc/running/active_training_campaign.yaml`
- `output/registries/program/current_best_solution.yaml`
- `output/registries/families/*/latest_family_best.yaml`
- `output/training_campaigns/*/campaign_manifest.yaml`
- `output/training_campaigns/*/campaign_best_run.yaml`
- `output/training_runs/*/*/metrics_summary.yaml`

## Output

By default, the generator writes:

- `doc/reports/analysis/Training Results Master Summary.md`

This file is the canonical high-level project summary that should be kept in
sync with new campaign results.

## Practical Use

Manual regeneration from the repository root:

```powershell
conda run -n standard_ml_codex_env python -B scripts/reports/generate_training_results_master_summary.py
```

Optional explicit output path:

```powershell
conda run -n standard_ml_codex_env python -B scripts/reports/generate_training_results_master_summary.py `
  --output-markdown-path "doc/reports/analysis/Training Results Master Summary.md"
```

## Automatic Update Path

The repository workflow should refresh this master summary automatically:

- after local training campaigns complete through
  `scripts/training/run_training_campaign.py`;
- after LAN-remote training campaigns finish syncing back to the local
  repository through `scripts/campaigns/run_remote_training_campaign.ps1`.

This keeps the report aligned with the latest campaign artifacts and family
registries without requiring a separate manual bookkeeping step after every
campaign.

## Notes

- The report is registry-driven, so it reflects the canonical ranking policy
  rather than ad-hoc folder inspection.
- Predictive ranking and deployment suitability remain separate concerns; the
  generated report intentionally keeps both visible.
- When the running-state backlog changes materially, regenerate this summary so
  the roadmap/status sections remain aligned with the real project plan.
