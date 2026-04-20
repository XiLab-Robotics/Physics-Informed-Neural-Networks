# Campaign Best Run

## Overview

This file serializes the bookkeeping winner for `track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21`.

## Selected Run

- Run name: `track1_svm_phase_repair_seed11`
- Run instance id: `2026-04-14-17-31-51__track1_svm_phase_repair_seed11_campaign_run`
- Scope: `phases_only`
- Harmonic targets: `4`
- Paper cells evaluated: `8`

## Ranking Policy

- Primary metric: `cell_closure_score_desc`
- First tie breaker: `met_paper_cell_count_desc`
- Second tie breaker: `open_paper_cell_count_asc`
- Third tie breaker: `mean_normalized_gap_ratio_asc`
- Fourth tie breaker: `max_normalized_gap_ratio_asc`
- Fifth tie breaker: `improved_cell_count_desc`
- Sixth tie breaker: `status_upgrade_score_desc`
- Seventh tie breaker: `run_name`

## Selected Metrics

- Closure score: `0.875`
- Met paper cells: `6`
- Near paper cells: `2`
- Open paper cells: `0`
- Improved cells vs baseline SVM row: `8`
- Status-upgrade score: `7`
- Mean normalized gap ratio: `0.020646`
- Max normalized gap ratio: `0.088894`

## Interpretation

This winner is a campaign-bookkeeping artifact only. The scientific result of the
campaign must be read from the merged post-repair `SVM` row in the canonical
benchmark, not from one isolated scoped run.
