# Campaign Best Run

## Overview

This file serializes the bookkeeping winner for `track1_svm_micro_closure_campaign_2026_04_14_21_42_47`.

## Selected Run

- Run name: `track1_svm_amplitude_240_only`
- Run instance id: `2026-04-14-21-52-08__track1_svm_amplitude_240_only_campaign_run`
- Scope: `amplitudes_only`
- Harmonic targets: `1`
- Paper cells evaluated: `2`

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

- Closure score: `0.750`
- Met paper cells: `1`
- Near paper cells: `1`
- Open paper cells: `0`
- Improved cells vs baseline SVM row: `0`
- Status-upgrade score: `0`
- Mean normalized gap ratio: `0.034580`
- Max normalized gap ratio: `0.034580`

## Interpretation

This winner is a campaign-bookkeeping artifact only. The scientific result of the
campaign must be read from the merged post-micro-closure `SVM` row in the canonical
benchmark, not from one isolated scoped run.
