# Campaign Best Run

## Overview

This file serializes the bookkeeping winner for `track1_svm_final_closure_campaign_2026_04_14_20_50_01`.

## Selected Run

- Run name: `track1_svm_amplitude_full_closure_split15`
- Run instance id: `2026-04-14-21-09-51__track1_svm_amplitude_full_closure_split15_campaign_run`
- Scope: `amplitudes_only`
- Harmonic targets: `3`
- Paper cells evaluated: `6`

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

- Closure score: `0.583`
- Met paper cells: `2`
- Near paper cells: `3`
- Open paper cells: `1`
- Improved cells vs baseline SVM row: `3`
- Status-upgrade score: `2`
- Mean normalized gap ratio: `0.145037`
- Max normalized gap ratio: `0.301930`

## Interpretation

This winner is a campaign-bookkeeping artifact only. The scientific result of the
campaign must be read from the merged post-final-closure `SVM` row in the canonical
benchmark, not from one isolated scoped run.
