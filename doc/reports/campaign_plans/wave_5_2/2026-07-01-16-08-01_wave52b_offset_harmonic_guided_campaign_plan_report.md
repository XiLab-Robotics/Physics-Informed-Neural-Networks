# Wave 5.2B Offset And Harmonic Guided Campaign Plan

> Supersession note, `2026-08-04`: references to `Wave 5.2C` in this completed
> historical plan mean within-machine dirty-to-clean supervision. They do not
> refer to the separately defined Cross-Machine Backbone Adaptation extension.

## Campaign Status

Prepared package, not launched. Training must not start until the operator
explicitly runs the prepared launcher.

The implementation package has created configurations, launcher, launcher
note, manifest, validator, and active campaign state.

## Objective

Prepare a bounded `Wave 5.2B` campaign that tests whether explicit offset /
mean supervision and nonzero-harmonic guidance improve TE curve readiness on
`polished_dataset`.

The campaign is intentionally small. It should answer whether the mechanism is
useful before `Wave 5.2C` within-machine dirty-to-clean supervision or
`Wave 6` integrated multi-head work is opened.

## Scope

- campaign name:
  `wave52b_offset_harmonic_guided_campaign_2026_07_01`
- dataset: `polished_dataset`
- schema: `polished_point_v1`
- surfaces: `global`, `forward`, `backward`
- launch mode: operator-launched local or `-Remote`
- training status: prepared, not launched
- official `TE Curve Verification Pipeline` status: not part of this campaign
  plan

## Evidence Base

The campaign is justified by:

- full `Wave 5.2A` paired matrix:
  `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`;
- model-design gate:
  `doc/reports/analysis/model_development_waves/wave_5_2/model_design_gate/[2026-07-01]/wave52b_wave52c_model_design_gate.md`;
- model explanation report:
  `doc/reports/analysis/model_development_waves/wave_5_2/Wave 5.2B Offset And Harmonic Guided Model.md`.

The key `Wave 5.2A` finding is that broad curve shape and smoothness are
nearly unchanged between the paired datasets, while offset / mean and nonzero
harmonic content differ materially.

## Planned Run Matrix

The initial campaign should contain `12` runs:

| Ablation | Purpose | Surfaces |
| --- | --- | --- |
| `pointwise_control` | Verify the trunk without new auxiliary pressure. | `global`, `forward`, `backward` |
| `offset_head` | Test learned offset / mean supervision. | `global`, `forward`, `backward` |
| `offset_centered_shape` | Test offset head plus centered-shape protection. | `global`, `forward`, `backward` |
| `offset_centered_shape_harmonic` | Test full `Wave 5.2B` pressure with nonzero-harmonic guidance. | `global`, `forward`, `backward` |

The run count is deliberately smaller than full-wave retraining. If these
ablations do not improve the relevant diagnostics, `Wave 5.2B` should be
closed as exploratory rather than expanded.

## Dataset Contract

The campaign must use the polished loader contract:

- inputs: `theta`, `theta_dot`, `tau_load`, `T`;
- target: `theta_TE`;
- direction selected by the first-level `forward` / `backward` folder;
- filename setpoints are not required runtime inputs for polished training;
- target curve means and future samples are train-time diagnostics only and
  must not be inference inputs.

## Metrics And Selection

Training and closeout must report:

- pointwise `MAE` and `RMSE`;
- offset / mean error;
- centered-shape error;
- peak-to-peak error;
- nonzero-harmonic amplitude mismatch;
- smoothness or derivative-continuity surrogate;
- direction-specific results for `global`, `forward`, and `backward`.

The campaign winner must not be selected by scalar `MAE` alone. A candidate
that improves offset while degrading centered shape or harmonic behavior is
not a clean promotion candidate.

## Governance

The local active campaign state currently records no active campaign, while
the full-wave `polished_dataset` retraining package is externally active on
another workstation. This campaign must not modify or close out that external
package.

Protected or deferred surfaces:

- full-wave polished retraining manifest and launcher;
- full-wave polished outputs and registries;
- `TE Curve Verification Pipeline` refresh package;
- `Wave 5.2C` within-machine dirty-to-clean supervision;
- `Wave 6` integrated multi-head work.

## Prepared Package

The implementation package created:

- model implementation and factory registration;
- curve-aware loss reuse through the existing training module;
- campaign YAML files for the `12` planned runs;
- dedicated PowerShell launcher with local and `-Remote` paths;
- launcher note under `doc/scripts/campaigns/`;
- active campaign state with protected-file list;
- exact local and `-Remote` launch commands;
- package validation and launcher preflight entry points.

Primary paths:

- manifest:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/campaign.yaml`;
- queue root:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/queue`;
- launcher:
  `scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.ps1`;
- validator:
  `scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py`.

## Launch Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1
```

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote
```

Preflight without training:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly
```
