# Campaign Best Run

## Overview

This file serializes the bookkeeping winner for
`track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48`.

## Selected Run

- Run name: `track1_svr_reference_grid_phase_162_only`
- Run instance id:
  `2026-04-17-05-57-27__track1_svr_reference_grid_phase_162_only_campaign_run`
- Scope: `phases_only`
- Harmonic targets: `1`
- Paper cells evaluated: `2`

## Ranking Policy

- Primary metric: `mean_normalized_gap_ratio_asc`
- First tie breaker: `max_normalized_gap_ratio_asc`
- Second tie breaker: `open_paper_cell_count_asc`
- Third tie breaker: `failed_target_count_asc`
- Fourth tie breaker: `run_name`

## Selected Metrics

- Closure score: `0.000`
- Met paper cells: `0`
- Near paper cells: `0`
- Open paper cells: `2`
- Mean normalized gap ratio: `1.307047`
- Max normalized gap ratio: `1.711230`
- Failed exports: `1`

## Interpretation

This winner is a campaign-bookkeeping artifact only. None of the four scoped
`SVR` reference-grid runs closed a paper target. The winner is therefore the
closest remaining paper-target approach under the explicit normalized-gap
policy, not a true closure run.
