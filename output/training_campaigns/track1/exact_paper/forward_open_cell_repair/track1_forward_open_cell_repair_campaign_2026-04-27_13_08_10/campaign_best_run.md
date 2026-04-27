# Campaign Best Run - track1_forward_open_cell_repair_campaign_2026-04-27_13_08_10

- Run: `track1_forward_lgbm_ampl_h81_open_cell_repair_attempt_08`
- Family: `LGBM`
- Scope: `amplitude`
- Harmonic: `81`
- Closure Score: `1.000`
- Met / Near / Open: `2` / `0` / `0`

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
