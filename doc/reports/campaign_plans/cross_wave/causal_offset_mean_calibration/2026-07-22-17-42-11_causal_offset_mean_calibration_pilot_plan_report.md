# Causal Offset Mean Calibration Pilot Campaign Plan

## Overview

This is the planning report for the prepared
`causal_offset_mean_calibration_pilot_2026_07_22` campaign. The campaign is a
small forward-only `polished_dataset` setpoint pilot designed to test whether
direct curve-mean / offset pressure is a better next branch than further
shape-only loss escalation.

The plan follows the approved technical document:

- `doc/technical/2026-07/2026-07-22/2026-07-22-17-38-44_causal_offset_mean_calibration_pilot.md`

## Scope

- dataset: `polished_dataset`
- input mode: `setpoints`
- dataset schema: `polished_setpoint_curve_v1`
- surface: `Fw`
- run count: `2`
- execution model: operator-launched local or `-Remote`
- heavy `TE Curve Verification Pipeline`: deferred until campaign closeout

## Campaign Arms

| Queue | Family | Runtime Contract | Purpose |
| --- | --- | --- | --- |
| `001` | `causal_offset_mean_gru_sequence_fw` | short causal sequence, center readout | test explicit residual-offset branch on the active windowed road |
| `002` | `causal_offset_mean_periodic_mlp_harmonic_fw` | non-windowed point inputs with sparse harmonic features | keep the non-windowed harmonic road active with offset/shape pressure |

## Baseline Comparison Policy

Campaign scalar metrics are diagnostic only. Promotion remains blocked until a
later bounded `TE Curve Verification Pipeline` screen compares the campaign
outputs against both accepted baselines:

- `polished_setpoints_periodic_gru_sequence_Fw`
- `polished_setpoints_periodic_mlp_harmonic_Fw`

The screen must use the repository multi-index curve-first selection policy and
must not promote on scalar `MAE` alone.

## Technical Approach

The windowed arm reuses `sequential_residual_offset_probe`, which sums a
pointwise base prediction with a GRU residual-offset prediction. The loss keeps
the point term dominant while adding conservative centered-shape, offset,
amplitude, and sparse-harmonic pressure.

The non-windowed arm reuses `periodic_mlp` with explicit sparse RCIM harmonic
features. Its objective mirrors the offset/shape emphasis without introducing
sequence state. This keeps the comparison fair to the non-windowed deployment
road instead of treating the GRU as the only active branch.

## Execution Package

- manifest:
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/campaign.yaml`
- queue configs:
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/001_causal_offset_mean_gru_sequence_fw.yaml`
  `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/002_causal_offset_mean_periodic_mlp_harmonic_fw.yaml`
- launcher:
  `scripts/campaigns/cross_wave/run_causal_offset_mean_calibration_pilot_campaign.ps1`
- launcher note:
  `doc/scripts/campaigns/cross_wave/run_causal_offset_mean_calibration_pilot_campaign.md`
- active state:
  `doc/running/active_training_campaign.yaml`

## Validation Steps

Before training, run:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -PreflightOnly
```

Then run one-batch validation without launching the campaign:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

Only after package approval, launch remotely with:

```powershell
.\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
  -Remote
```

## Closeout Requirements

Normal campaign closeout must produce:

- `campaign_leaderboard.yaml`
- `campaign_best_run.yaml`
- `campaign_best_run.md`
- refreshed family registries for both pilot families
- refreshed program-level registry if applicable
- campaign-results Markdown and PDF report
- updated active campaign state
- checked `Training Results Master Summary`
- checked `TE Program Status And Closeout Ledger`

The heavy bounded `TE Curve Verification Pipeline` screen remains a separate
operator-approved step after this normal closeout.
