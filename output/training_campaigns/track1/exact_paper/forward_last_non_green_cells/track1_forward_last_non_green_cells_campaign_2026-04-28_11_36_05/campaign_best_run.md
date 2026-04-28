# Campaign Best Run - track1_forward_last_non_green_cells_campaign_2026-04-28_11_36_05

- Run: `track1_forward_xgbm_ampl_h240_last_non_green_cells_attempt_08`
- Family: `XGBM`
- Scope: `amplitude`
- Harmonic: `240`
- Closure Score: `0.750`
- Met / Near / Open: `1` / `1` / `0`

## Selection Policy

- Primary metric: `closure_score_desc`
- First tie-breaker: `met_paper_cell_count_desc`
- Second tie-breaker: `near_paper_cell_count_desc`
- Third tie-breaker: `open_paper_cell_count_asc`
- Fourth tie-breaker: `mean_normalized_gap_ratio_asc`
- Fifth tie-breaker: `max_normalized_gap_ratio_asc`
- Sixth tie-breaker: `winning_mean_component_mae_asc`
- Seventh tie-breaker: `winning_mean_component_rmse_asc`
- Eighth tie-breaker: `run_name`
