# Wave 4A MMT Parameter Inventory

## Overview

This report classifies the inputs required by the repository-owned `MMT_TEModeling` equation chain before those equations are used as causal features, calibrated analytical baselines, or weak PINN losses.

The inventory is intentionally not a training campaign. It does not create queue YAMLs, launchers, or active-campaign state.

## Summary

| Field | Value |
| --- | ---: |
| Run ID | `2026-06-11-20-29-51__wave4a_mmt_parameter_inventory` |
| Inventory Rows | 11 |
| Train-Only Calibratable Groups | 5 |
| High Leakage-Risk Groups | 3 |
| Campaign Readiness | `not_campaign_ready` |

## Availability Summary

| Availability Class | Count |
| --- | ---: |
| `available_as_target_only` | 1 |
| `calibratable_train_only` | 5 |
| `known_dataset_metadata` | 1 |
| `known_geometry_constant` | 3 |
| `unavailable_or_ambiguous` | 1 |

## Downstream Decision Summary

| Downstream Decision | Count |
| --- | ---: |
| `allowed_for_dataset_aligned_diagnostics` | 1 |
| `allowed_for_diagnostic_and_feature_generation` | 1 |
| `allowed_for_wave4a_diagnostic_and_wave4b_features` | 1 |
| `allowed_for_wave4b_features_and_wave4c_losses` | 1 |
| `candidate_feature_or_weak_loss_after_calibration` | 1 |
| `candidate_for_offset_and_low_frequency_diagnostics` | 1 |
| `candidate_latent_state_or_hysteresis_channel` | 1 |
| `diagnostic_only_until_reconstruction_gate` | 1 |
| `evaluation_target_not_inference_input` | 1 |
| `high_priority_wave4b_and_wave4c_candidate` | 1 |
| `high_priority_wave4b_candidate_features` | 1 |

## Parameter Inventory

| Group | Availability | Leakage | Downstream Decision | Policy |
| --- | --- | --- | --- | --- |
| `tooth_counts` | `known_geometry_constant` | `none` | `allowed_for_wave4b_features_and_wave4c_losses` | locked unless the reducer hardware changes |
| `involute_gear_geometry` | `known_geometry_constant` | `none` | `allowed_for_diagnostic_and_feature_generation` | locked after geometry confirmation |
| `pin_and_crank_geometry` | `known_geometry_constant` | `none` | `allowed_for_wave4a_diagnostic_and_wave4b_features` | locked after reducer-specific geometry confirmation |
| `operating_condition_metadata` | `known_dataset_metadata` | `low if no target-derived curve mean or future TE is used at inference` | `allowed_for_dataset_aligned_diagnostics` | not calibrated; used for stratification and causal conditioning |
| `contact_geometry_state` | `unavailable_or_ambiguous` | `high if fitted directly from held-out TE curves` | `diagnostic_only_until_reconstruction_gate` | blocked until reducer-specific contact reconstruction is defined |
| `high_speed_original_errors` | `calibratable_train_only` | `medium` | `candidate_feature_or_weak_loss_after_calibration` | fit only on training groups if used; keep validation/test untouched |
| `crankshaft_and_cycloid_hole_errors` | `calibratable_train_only` | `medium` | `high_priority_wave4b_candidate_features` | fit as grouped equivalent-error channels on train only |
| `cycloidal_profile_and_pin_radius_errors` | `calibratable_train_only` | `medium` | `high_priority_wave4b_and_wave4c_candidate` | fit as bounded low-speed equivalent-error channel on train only |
| `pin_pitch_circle_and_accumulated_pitch_errors` | `calibratable_train_only` | `medium` | `candidate_for_offset_and_low_frequency_diagnostics` | fit on train by direction and load group only if stable |
| `output_disc_assembly_error` | `calibratable_train_only` | `high if tuned curve-by-curve from target mean` | `candidate_latent_state_or_hysteresis_channel` | fit only as a causal latent or grouped train-only parameter |
| `measured_te_target` | `available_as_target_only` | `high if used to normalize or calibrate held-out curves` | `evaluation_target_not_inference_input` | never use held-out target means or full curves at inference |

## High-Risk Boundaries

| Group | Reason | Required Gate |
| --- | --- | --- |
| `contact_geometry_state` | This is the main blocker for treating Wave 4A as a calibrated analytical baseline. | blocked until reducer-specific contact reconstruction is defined |
| `output_disc_assembly_error` | Paper attributes frequency component 1 to output-disc hole-position deviation. | fit only as a causal latent or grouped train-only parameter |
| `measured_te_target` | Critical boundary for Wave 4B and Wave 4C leakage-safe design. | never use held-out target means or full curves at inference |

## Interpretation

The MMT path is usable today as an auditable diagnostic and as a source of geometry-locked harmonic hypotheses. It is not yet a dataset-calibrated predictor because contact geometry and original component-error channels are not directly observed in the current Track 2 dataset.

`Wave 4B` should start with geometry-locked features plus train-only calibrated equivalent-error groups. `Wave 4C` should remain weak-loss only until the feature path proves that MMT terms explain held-out offset or fragile-harmonic structure without leakage.

The paper supports low-speed-stage error groups as high-priority candidates. The output-disc assembly channel is especially relevant to the low-order frequency-1 family, but it must be handled as a latent or grouped calibration channel, not as a per-curve target mean correction.

## Machine-Readable Artifacts

- `output/validation_checks/wave4_mmt_parameter_inventory/2026-06-11-20-29-51__wave4a_mmt_parameter_inventory/wave4a_mmt_parameter_inventory.csv`
- `output/validation_checks/wave4_mmt_parameter_inventory/2026-06-11-20-29-51__wave4a_mmt_parameter_inventory/wave4a_mmt_parameter_inventory_summary.yaml`

## Reproduction

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_wave4a_mmt_parameter_inventory_report.py
```
