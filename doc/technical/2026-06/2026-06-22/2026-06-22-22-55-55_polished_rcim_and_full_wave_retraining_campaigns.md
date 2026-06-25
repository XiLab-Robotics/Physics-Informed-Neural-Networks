# Polished RCIM And Full Wave Retraining Campaigns

## Overview

This technical document defines the preparation pass for two separate
`polished_dataset` retraining campaigns:

1. a new `RCIM Model-Bank Reproduction` campaign that reruns the old
   paper-reimplementation branch on polished measured points;
2. a full model-development wave retraining campaign that reruns all
   non-paper model families visible in the current `TE Curve Verification
   Pipeline` best-model collage reference.

The split is intentional. The old `Track 1` work is now named
`RCIM Model-Bank Reproduction` and follows the paper-faithful model-bank logic.
The later Wave 1 through Wave 5.1 model-development families use the repository
training stack and should be managed as a separate cross-wave retraining
package.

The campaign preparation must use `polished_dataset` as the default dataset and
must not regress to filename-derived setpoints. For polished data, each CSV row
is a real measured point with inputs `theta`, `theta_dot`, `tau_load`, and `T`,
and target `theta_TE`.

## Technical Approach

The implementation will prepare campaign artifacts only after this technical
plan is approved.

The first campaign will audit the existing `RCIM Model-Bank Reproduction`
entry points and prepare a polished-compatible run package. If the paper-bank
code still expects the older matrix or filename-derived data representation,
the implementation will add an explicit adapter or export step that converts
the polished point schema into the required training representation without
changing the meaning of the measured columns.

The second campaign will build a canonical-name full-wave retraining package
from the current `TE Curve Verification Pipeline` collage reference:

`doc/reports/analysis/track2/best_model_collage_report/[2026-06-18]/track2_best_model_collage_report.md`

The user-provided list covers the non-paper model-development candidates in
that report. The only excluded report candidates are paper reference surfaces:

- `paper_original_best_Fw`;
- `paper_retuned_best_Fw`;
- `paper_retuned_best_Bw`.

The `rcim_model_bank_reproduction_best_fw` and
`rcim_model_bank_reproduction_best_bw` candidates are not missing from the
scope; they belong to the first dedicated `RCIM Model-Bank Reproduction`
campaign rather than the general wave retraining campaign.

Future-facing config names, run names, registry identifiers, and report labels
will follow the canonical model-family naming introduced by commit
`4dff9a28b56824da5f90e38e626e75c9348b842d`.

### Canonical Model List

The following model families will be prepared for the full-wave campaign.
Where the user supplied a legacy name, the canonical future identifier is shown
as the implementation target.

| User-facing / legacy name | Canonical campaign identifier |
| --- | --- |
| `feedforward` | `feedforward` |
| `harmonic_regression` | `harmonic_regression` |
| `periodic_mlp` | `periodic_mlp` |
| `residual_harmonic_mlp` | `residual_harmonic_mlp` |
| `tree` | `tree` |
| `periodic_mlp_harmonic` | `periodic_mlp_harmonic` |
| `temporal_convolution` | `temporal_convolution` |
| `gru_sequence` | `gru_sequence` |
| `lstm_sequence` | `lstm_sequence` |
| `periodic_temporal_convolution` | `periodic_temporal_convolution` |
| `periodic_gru_sequence` | `periodic_gru_sequence` |
| `periodic_lstm_sequence` | `periodic_lstm_sequence` |
| `residual_harmonic_gru_sequence_sparse_rcim` | `residual_harmonic_gru_sequence_sparse_rcim` |
| `residual_harmonic_gru_sequence_dense240` | `residual_harmonic_gru_sequence_dense240` |
| `residual_harmonic_gru_sequence_dense360` | `residual_harmonic_gru_sequence_dense360` |
| `residual_harmonic_lstm_sequence_sparse_rcim` | `residual_harmonic_lstm_sequence_sparse_rcim` |
| `residual_harmonic_lstm_sequence_dense240` | `residual_harmonic_lstm_sequence_dense240` |
| `residual_harmonic_lstm_sequence_dense360` | `residual_harmonic_lstm_sequence_dense360` |
| `sequential_residual_offset_probe` | `wave3_1_sequential_residual_offset_probe` |
| `track2f_bis_clean_sequential_residual_offset` | `wave3_2_clean_sequential_residual_offset` |
| `track2f_bis_harmonic_residual_offset` | `wave3_2_harmonic_residual_offset` |
| `track2g_curve_aware_pointwise_control` | `wave3_3_curve_aware_pointwise_control` |
| `track2g_curve_aware_raw_centered_shape` | `wave3_3_raw_centered_shape_curve_aware` |
| `track2g_curve_aware_raw_offset` | `wave3_3_raw_offset_curve_aware` |
| `track2g_curve_aware_full_curve_composite` | `wave3_3_full_curve_composite` |
| `track2h_mae_robust` | `wave4_1_mae_robust_loss` |
| `track2h_smooth_l1_robust` | `wave4_1_smooth_l1_robust_loss` |
| `track2h_log_cosh_robust` | `wave4_1_log_cosh_robust_loss` |
| `track2h_quantile_p10_p50_p90` | `wave4_2_quantile_p10_p50_p90` |
| `track2h_gaussian_nll` | `wave4_2_gaussian_nll` |
| `track2h_mdn_k2` | `wave4_3_mixture_density_k2` |
| `track2h_mdn_k3` | `wave4_3_mixture_density_k3` |
| `track2h_l_gru_offset_residual` | `wave4_4_gru_latent_offset_residual` |
| `track2h_l_causal_tcn_offset_residual` | `wave4_4_causal_tcn_latent_offset_residual` |
| `wave3_harmonic_prior_residual_pointwise_control` | `wave5_1_harmonic_prior_pointwise_control` |
| `wave3_harmonic_prior_residual_smooth_l1_structured` | `wave5_1_harmonic_prior_smooth_l1_structured` |

The full-wave campaign will target `fw`, `bw`, and `global` surfaces for each
model family where the current training stack supports that surface. The
nominal scope is therefore 36 model families times 3 surfaces, for up to 108
training configs.

## Involved Components

- `data/polished_dataset/`
  - polished measured-point dataset with first-level `forward` and `backward`
    folders.
- `config/datasets/transmission_error_dataset.yaml`
  - dataset selection and polished schema configuration.
- `config/training/**`
  - source training presets and campaign queues for the model families.
- `scripts/campaigns/**`
  - local and remote PowerShell launchers.
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
  - shared remote campaign launch/sync workflow.
- `doc/reports/campaign_plans/`
  - preliminary campaign plans for the two retraining packages.
- `doc/scripts/campaigns/`
  - operator-facing launcher notes.
- `doc/running/active_training_campaign.yaml`
  - persistent prepared or active campaign state.
- `output/training_campaigns/`
  - campaign runtime output roots.
- `output/registries/`
  - family and program registries updated after completed campaigns.

No subagent is planned for this implementation.

## Implementation Steps

1. Inspect the current `RCIM Model-Bank Reproduction` scripts, configs,
   historical campaign plans, and dataset assumptions.
2. Define the polished-compatible `RCIM Model-Bank Reproduction` campaign
   package, including any required point-schema adapter or export step.
3. Create the corresponding campaign plan report under
   `doc/reports/campaign_plans/`.
4. Create the RCIM polished campaign YAML files, PowerShell launcher with local
   and `-Remote` support, launcher note, and active-campaign state entry.
5. Inspect the current source configs for every canonical full-wave model
   family listed above.
6. Generate the full-wave polished campaign configs for `fw`, `bw`, and
   `global` surfaces where supported, using canonical future identifiers and
   preserving traceability to legacy names where needed.
7. Create the full-wave campaign plan report, PowerShell launcher with local
   and `-Remote` support, launcher note, and active-campaign state entry.
8. Run campaign package validation and lightweight smoke/preflight checks only;
   do not start heavy training automatically.
9. Run Markdown QA on touched documentation.
10. Report the exact launch commands and wait for the operator to launch the
    approved campaign.
