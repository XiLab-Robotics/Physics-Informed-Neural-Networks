# Polished Early-Wave Parallel Training Campaign Plan

## Campaign Status

Planning gate only. Training must not start until this plan and the matching
technical document are explicitly approved.

## Objective

Start `polished_dataset` model-development retraining on this workstation while
the `RCIM Model-Bank Reproduction` polished run continues on another machine.

The campaign is intentionally limited to the first prepared full-wave block so
that progress can begin without committing this machine to the entire 108-run
full-wave package.

## Scope

- campaign name: `polished_dataset_early_wave_parallel_training_2026_06_25`
- source campaign: `polished_dataset_full_wave_retraining_2026_06_22`
- dataset: `polished_dataset`
- schema: `polished_point_v1`
- surfaces: `global`, `fw`, `bw`
- run count: `36`
- execution mode: operator-launched local or `-Remote`

## Included Families

| Config range | Families | Surfaces |
| --- | --- | --- |
| `001`-`018` | `tree`, `residual_harmonic_mlp`, `feedforward`, `periodic_mlp`, `harmonic_regression`, `periodic_mlp_harmonic` | `global`, `fw`, `bw` |
| `019`-`036` | `temporal_convolution`, `gru_sequence`, `lstm_sequence`, `periodic_temporal_convolution`, `periodic_gru_sequence`, `periodic_lstm_sequence` | `global`, `fw`, `bw` |

## Excluded Families

The following prepared full-wave groups remain excluded from this early batch:

- residual harmonic temporal hybrids from configs `037`-`054`;
- Wave `3.x` offset and curve-aware families from configs `055`-`075`;
- Wave `4.x` robust, probabilistic, mixture-density, and latent-state
  families from configs `076`-`102`;
- Wave `5.1` harmonic-prior residual families from configs `103`-`108`;
- all paper-original and paper-retuned surfaces.

## Dataset Contract

The run must use the polished loader contract:

- inputs: `theta`, `theta_dot`, `tau_load`, `T`;
- target: `theta_TE`;
- direction is selected by the first-level `forward` / `backward` folder;
- filename setpoints are not model inputs for polished training.

## Governance And Collision Avoidance

`doc/running/active_training_campaign.yaml` currently protects the prepared
`RCIM Model-Bank Reproduction` campaign. This early-wave campaign must be
treated as a deliberate parallel operator run, not as normal sequential
campaign closeout.

Before launch, the operator must approve:

1. preparing a dedicated early-wave campaign package;
2. updating or recording campaign state without erasing RCIM provenance;
3. running this 36-run batch while the RCIM run is active on another machine.

## Planned Launch Commands

Local:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1
```

Remote:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -Remote
```

Preflight:

```powershell
.\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -PreflightOnly
```
