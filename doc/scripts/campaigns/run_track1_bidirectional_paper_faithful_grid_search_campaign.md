# Track 1 Bidirectional Paper-Faithful Grid-Search Campaign Launcher

## Overview

This launcher executes the prepared `Track 1` bidirectional paper-faithful
campaign that replaces the old `400`-run literal-refresh wave.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches the exact-paper queue
through the canonical remote wrapper when `-Remote` is used.

The prepared package covers:

- `forward` and `backward`;
- all `10` exact-paper families;
- exactly `1` grid-search run per family-direction surface;
- total queue size `20`.

This campaign also depends on the restored historical search protocol in the
shared exact-paper training path:

- `GridSearchCV` fit on the prepared training split;
- global `cross_validate(...)` replay on the search wrapper;
- target-wise `cross_validate(...)` replay on the best wrapped estimators.

Each prepared campaign instance writes to a fresh campaign-specific output root
under:

- `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/<campaign_name>/`

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py
```

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 -Remote
```

## Operator View

The remote operator console remains compact:

- the progress bar advances on real config boundaries;
- the active run log remains visible under `output/training_campaigns/.../logs/`;
- the queue is intentionally small because the paper-faithful design uses one
  search pass per family-direction surface instead of a seed-sweep campaign.
