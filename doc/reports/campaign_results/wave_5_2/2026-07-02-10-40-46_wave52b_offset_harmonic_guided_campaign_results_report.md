# Wave 5.2B Offset And Harmonic Guided Campaign Results Report

## Overview

This report closes out the completed `Wave 5.2B` offset and harmonic guided
campaign on `polished_dataset`.

Campaign evidence:

- Campaign: `wave52b_offset_harmonic_guided_campaign_2026_07_01`
- Dataset: `polished_dataset`
- Dataset schema: `polished_point_v1`
- Campaign output:
  `output/training_campaigns/2026-07-01-18-59-04_wave52b_offset_harmonic_guided_campaign_2026_07_01/`
- Completed runs: `12`
- Failed runs: `0`
- Generated at: `2026-07-02T02:27:12`

The campaign tested four lightweight profiles across `global`, `Fw`, and `Bw`
surfaces:

- `pointwise_control`
- `offset_head`
- `offset_centered_shape`
- `offset_centered_shape_harmonic`

This is a normal scalar training closeout. It does not run or replace the
official `TE Curve Verification Pipeline`, and it does not make a curve-first
promotion decision.

## Scalar Winner

The scalar campaign winner is:

| Field | Value |
| --- | --- |
| Run name | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` |
| Run instance | `2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` |
| Model family | `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` |
| Surface | `Fw` |
| Test MAE [deg] | `0.001391538535244763` |
| Test RMSE [deg] | `0.0017712278058752418` |
| Val MAE [deg] | `0.001809177570976317` |
| Parameters | `22593` |
| Checkpoint | `output\training_runs\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\2026-07-02-01-24-47__te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\checkpoints\wave52b_offset_harmonic_guided-epoch=116-val_mae=0.00180918.ckpt` |

The winner is the forward-surface harmonic profile, not a global model.

## Surface Winners

| Surface | Best Profile | Best Run | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `global` | `offset_centered_shape_harmonic` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | 0.002215 | 0.002799 | 0.001886 |
| `Fw` | `offset_centered_shape_harmonic` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | 0.001392 | 0.001771 | 0.001809 |
| `Bw` | `offset_centered_shape_harmonic` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | 0.001677 | 0.002151 | 0.002320 |

The same profile wins all three surfaces. That is the main technical result of
the campaign: the explicit combination of offset, centered-shape, and harmonic
guidance is consistently better than the control profiles inside this
lightweight family.

## Full Scalar Leaderboard

| Rank | Run | Surface | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `offset_centered_shape_harmonic_fw` | `Fw` | 0.001392 | 0.001771 | 0.001809 |
| 2 | `offset_centered_shape_harmonic_bw` | `Bw` | 0.001677 | 0.002151 | 0.002320 |
| 3 | `offset_centered_shape_fw` | `Fw` | 0.001931 | 0.002445 | 0.002258 |
| 4 | `offset_head_fw` | `Fw` | 0.001948 | 0.002454 | 0.002256 |
| 5 | `pointwise_control_bw` | `Bw` | 0.001979 | 0.002587 | 0.002591 |
| 6 | `offset_head_bw` | `Bw` | 0.002008 | 0.002632 | 0.002597 |
| 7 | `offset_centered_shape_bw` | `Bw` | 0.002012 | 0.002626 | 0.002604 |
| 8 | `pointwise_control_fw` | `Fw` | 0.002054 | 0.002564 | 0.002344 |
| 9 | `offset_centered_shape_harmonic_global` | `global` | 0.002215 | 0.002799 | 0.001886 |
| 10 | `pointwise_control_global` | `global` | 0.002461 | 0.003142 | 0.002210 |
| 11 | `offset_head_global` | `global` | 0.002483 | 0.003166 | 0.002249 |
| 12 | `offset_centered_shape_global` | `global` | 0.002540 | 0.003229 | 0.002271 |

## Ablation Interpretation

The internal ablation is clear:

- `offset_centered_shape_harmonic` is the strongest profile on every surface.
- The harmonic branch provides the largest forward gain, reducing forward test
  MAE from the pointwise control value of `0.002054` to `0.001392`.
- The backward gain is also material, reducing backward test MAE from
  `0.001979` to `0.001677`.
- The global surface improves relative to all other Wave 5.2B global profiles,
  but it remains weaker than the best polished early-wave global models.

This supports keeping harmonic structure in the candidate ingredient list for
later `Wave 5.2C` or `Wave 6` integration. It does not prove that this
lightweight model family should replace the stronger sequence backbones.

## Comparison Against Current Polished Leaders

The current polished early-wave scalar leaders remain stronger:

| Surface | Polished Leader | Leader MAE | W5.2B Best | W5.2B MAE |
| --- | --- | ---: | --- | ---: |
| `global` | `te_periodic_lstm_sequence_global` | 0.001187 | `offset_centered_shape_harmonic_global` | 0.002215 |
| `Fw` | `te_periodic_gru_sequence_fw` | 0.001101 | `offset_centered_shape_harmonic_fw` | 0.001392 |
| `Bw` | `te_periodic_gru_sequence_bw` | 0.001084 | `offset_centered_shape_harmonic_bw` | 0.001677 |

Therefore this campaign does not change the scalar program winner, which
remains `te_periodic_gru_sequence_bw`.

## Registry And Status Decision

The run artifacts and family registries are accepted as completed training
evidence for `Wave 5.2B`.

Closeout decisions:

- Accept the `12` completed runs and their campaign leaderboard.
- Record `offset_centered_shape_harmonic` as the strongest Wave 5.2B profile.
- Do not promote Wave 5.2B over the polished early-wave scalar leaders.
- Do not alter official `TE Curve Verification Pipeline` accepted leaders in
  this closeout.
- Keep the externally running
  `polished_dataset_full_wave_retraining_2026_06_22` campaign isolated until
  its final artifacts are synchronized on its own workstation.

## Next Steps

Recommended next actions:

1. Keep Wave 5.2B as evidence that harmonic guidance should be retained as an
   integration ingredient.
2. Treat an official `TE Curve Verification Pipeline` refresh for Wave 5.2B as
   a separate optional operator-approved step.
3. Wait for the externally running full-wave polished retraining campaign
   before drawing final clean-branch conclusions.
4. Use Wave 5.2B results to inform `Wave 5.2C` dirty-to-clean or transfer
   supervision only after curve-first evidence is available or explicitly
   deferred.
