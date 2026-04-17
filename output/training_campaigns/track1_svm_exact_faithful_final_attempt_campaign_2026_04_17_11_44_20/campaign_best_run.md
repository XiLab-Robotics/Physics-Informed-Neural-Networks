# Campaign Best Run

## Overview

This file serializes the bookkeeping winner for
`track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20`.

## Selected Run

- Run name: `track1_svr_exact_faithful_phase_162_repeat`
- Run instance id:
  `2026-04-17-17-03-43__track1_svr_exact_faithful_phase_162_repeat_campaign_run`
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
exact-faithful `SVR` reruns closed a paper target. The winner is therefore the
closest remaining paper-target approach under the explicit normalized-gap
policy, not a true closure run.
