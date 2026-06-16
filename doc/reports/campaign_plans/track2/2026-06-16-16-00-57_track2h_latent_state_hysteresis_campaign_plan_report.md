# Track 2H-L Latent-State Hysteresis Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the `Track 2H-L` probe:
latent-state / hysteresis-aware models for preload, elastic release, protocol
state, and causal-history effects in TE prediction.

Completed `Track 2H` robust, probabilistic, and MDN probes show that
dispersion-aware training pressure is useful but not sufficient. Completed
`Wave 3` harmonic-prior residual models are verified exploratory baselines,
not promoted. The strongest accepted repository-owned practical branch remains
history/sequence-based, which justifies a narrow test of whether causal hidden
state explains the remaining offset and fragile-harmonic behavior.

Training is not approved by this report. The executable campaign package must
be generated only after this plan and the paired technical document are
explicitly approved.

## Paired Technical Document

- [technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md](../../../technical/2026-06/2026-06-16/2026-06-16-16-00-57_track2h_latent_state_hysteresis_package.md)

## Baseline Interpretation

| Evidence | Interpretation |
| --- | --- |
| `Track 2H` robust losses | Robust losses help specific branches but do not solve offset or curve-following behavior alone. |
| `Track 2H` probabilistic heads | Quantile and Gaussian heads improve some dispersion-aware surfaces but do not beat accepted leaders. |
| `Track 2H` MDN heads | MDN improves `Bw`, but near-single-component usage argues against confirmed multimodality. |
| `Wave 3` harmonic-prior residual | Lightweight structure is trainable and inspectable, but official `Track 2` closes it as exploratory. |
| `periodic_gru_sequence_Bw` | The strongest practical repository-owned branch is sequence/history based, supporting a latent-state probe. |
| Experimental repeatability feedback | Preload, elastic release, protocol state, or hysteresis-like internal state remain plausible unobserved contributors. |

## Candidate Matrix

The first `Track 2H-L` campaign should remain narrow:

| Candidate Group | Surfaces | Main Test |
| --- | --- | --- |
| `latent_state_gru_offset_residual` | `global`, `Fw`, `Bw` | Tests whether a compact causal GRU state over operating-condition history improves offset and residual curve prediction. |
| `latent_state_tcn_offset_residual` | `global`, `Fw`, `Bw` | Optional second profile if implementation cost is low; tests whether a causal temporal convolution state is enough without recurrent state. |

If scope or runtime must be reduced, prefer the `GRU` profile across all three
surfaces over a broader model sweep. Direction coverage is mandatory.

## Model And Input Requirements

Required behavior:

- consume only current and previous operating-state information available at
  runtime;
- preserve `global`, `Fw`, and `Bw` training and reporting surfaces;
- expose the latent-state vector or summary as an auxiliary diagnostic output;
- expose offset/low-order and residual predictions separately when practical;
- keep deterministic playback as the standard scalar and official `Track 2`
  comparison curve;
- fail fast if a config uses measured TE, full-curve statistics, future
  samples, or post-prediction mean centering as model inputs.

Preferred implementation:

- reuse the existing sequence datamodule and training stack;
- reuse established temporal readout conventions from existing sequence
  models;
- add a narrow model/factory key only if the existing model families cannot
  express the latent-state plus offset/residual split cleanly;
- keep the first hidden-state model compact enough to be diagnostic rather
  than a broad high-capacity sweep.

## Evaluation Plan

Required scalar checks:

- validation and test `MAE`;
- validation and test `RMSE`;
- parameter count and artifact size;
- branch comparison versus completed `Track 2H` and `Wave 3` candidates.

Required curve-first checks after normal closeout:

- separate official `Track 2` verification refresh;
- direction-specific curve `MAE`, `RMSE`, mean percentage error, and P95;
- offset / mean-surface diagnostics;
- centered-shape diagnostics;
- high-fragility harmonic checks for low-order and high-order groups;
- collage and overlay reports.

The campaign should be interpreted as evidence for or against hidden-state
modeling, not as a final integrated multi-head solution.

## Expected Campaign Package After Approval

After this planning gate is approved, the implementation step should prepare:

- a dedicated package root under
  `config/training/track2h_latent_state_hysteresis/campaigns/`;
- generated queue YAML files for `global`, `Fw`, and `Bw`;
- `scripts/campaigns/track2/prepare_track2h_latent_state_hysteresis_campaign.py`;
- `scripts/campaigns/track2/validate_track2h_latent_state_hysteresis_package.py`;
- `scripts/campaigns/track2/run_track2h_latent_state_hysteresis_campaign.ps1`;
- `doc/scripts/campaigns/track2/run_track2h_latent_state_hysteresis_campaign.md`;
- updated prepared campaign state in `doc/running/active_training_campaign.yaml`;
- exact local and `-Remote` launch commands.

The launcher must support:

- `-PreflightOnly`;
- `-EnqueueOnly`;
- `-Remote` through the repository-owned remote training infrastructure.

## Verification Plan

Before training launch:

- use Context7 for PyTorch-facing implementation details;
- run Python compile checks on touched scripts and model modules;
- validate generated YAML files and dataset variants;
- validate causal input metadata and absence of target-leakage fields;
- validate model construction and finite one-batch loss;
- validate auxiliary latent-state and offset/residual outputs when present;
- run the dedicated launcher in `-PreflightOnly`;
- run Markdown QA on touched documentation;
- run Sphinx QA when documentation indices or guide scope change;
- confirm `doc/running/active_training_campaign.yaml` is in `prepared` state;
- provide exact local and `-Remote` commands.

After training completion:

- close out the campaign with Markdown and PDF results;
- export and validate the real PDF deliverable;
- update family and program registries;
- clean active campaign state;
- update the live backlog and training master summary;
- propose official `Track 2` refresh as a separate operator-launched step.

## Decision Gates

| Gate | Decision |
| --- | --- |
| Planning approval | Authorize generation of the `Track 2H-L` package. |
| Package validation | Authorize local or remote campaign launch. |
| Campaign closeout | Decide whether latent-state modeling improves scalar metrics over `Track 2H` and `Wave 3` baselines. |
| Official `Track 2` refresh | Decide whether latent-state behavior should feed Wave 4 or the integrated multi-head design. |

## Non-Goals

- No measured TE, target curve mean, or future samples as model input.
- No post-prediction mean-centering as a deployed correction.
- No Wave 4 PINN / physics-informed loss in this package.
- No integrated multi-task / multi-head architecture in this package.
- No PLC-friendly export optimization in this package.
