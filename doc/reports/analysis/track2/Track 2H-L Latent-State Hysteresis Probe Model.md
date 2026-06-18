# Track 2H-L Latent-State Hysteresis Probe Model

## Overview

`latent_state_hysteresis_probe` is the approved `Track 2H-L` diagnostic model
family for testing whether causal operating-history state helps explain the
offset, preload, elastic-release, and fragile-harmonic behavior observed in
`Track 2`.

The model is not an integrated multi-task / multi-head solution. It is a
narrow probe that must be compared against completed `Track 2H` robust,
probabilistic, mixture-density probes and the first real `Wave 3`
harmonic-prior residual branch.

## Operating Principle

The model receives a sequence window of operating-state features:

- angular position;
- input speed;
- input torque;
- oil temperature;
- direction flag.

The campaign package enforces `sequence_target_position: last` and model
`readout_position: last`. This means the prediction at the current point uses
only the current and previous samples in the window. Future TE samples,
measured TE, curve means, full-curve held-out statistics, and post-prediction
centering are not valid inputs.

The latent-state encoder compresses the causal window into one state vector.
That vector is interpreted as a diagnostic proxy for unobserved protocol state:
preload, elastic release, direction-transition memory, or hysteresis-like
internal state.

## Conceptual Structure

The implemented backbone has three additive branches:

| Branch | Input | Purpose |
| --- | --- | --- |
| base branch | current normalized operating state | local point estimate |
| offset head | current state plus latent state | low-order / mean-like correction |
| residual head | current state plus latent state | remaining local TE correction |

The final normalized prediction is:

```text
prediction = base_prediction + offset_prediction + residual_prediction
```

The auxiliary outputs expose:

- `base_prediction_tensor`;
- `latent_state_tensor`;
- `residual_offset_prediction_tensor`;
- `hysteresis_residual_prediction_tensor`.

These diagnostics allow campaign closeout and later `Track 2` verification to
inspect whether the latent state is actually carrying useful offset or residual
information.

## Campaign Profiles

The prepared `Track 2H-L` package contains two profiles:

| Profile | Encoder | Test |
| --- | --- | --- |
| `gru_offset_residual` | unidirectional `GRU` | Whether recurrent hidden state captures protocol memory. |
| `causal_tcn_offset_residual` | left-padded causal temporal convolution | Whether a simpler finite-history state is enough without recurrence. |

Each profile is trained on `global`, `Fw`, and `Bw` surfaces.

## Advantages

- Tests the physical hypothesis that some offset is state/history dependent.
- Keeps runtime inputs deployment-valid and causal.
- Exposes latent and branch diagnostics for closeout interpretation.
- Reuses the existing sequence datamodule, Lightning module, campaign runner,
  registry flow, and `Track 2` verification path.

## Disadvantages And Risks

- The latent state is inferred from operating metadata only; if the real
  preload state is not observable from those variables, the model may not
  improve.
- The campaign adds capacity and may overfit local dispersion unless official
  `Track 2` curve verification confirms the scalar result.
- The latent vector is not yet constrained by physics or repeatability
  measurements.
- This is still Python-side modeling; PLC-friendly export is intentionally
  deferred.

## Implemented Components

- `scripts/models/latent_state_hysteresis_network.py`
  - `CausalTemporalStateEncoder`
  - `LatentStateHysteresisNetwork`
- `scripts/models/model_factory.py`
  - registers `latent_state_hysteresis_probe`
- `scripts/training/train_feedforward_network.py`
  - prints model-specific `Track 2H-L` configuration fields
- `scripts/training/run_training_campaign.py`
  - routes `latent_state_hysteresis_probe` through the standard neural trainer
- `scripts/campaigns/track_2/prepare_track2h_latent_state_hysteresis_campaign.py`
  - generates the campaign package and prepared active state
- `scripts/campaigns/track_2/validate_track2h_latent_state_hysteresis_package.py`
  - validates queue matrix, causal contract, model construction, and optional
    one-batch loss/output behavior
- `scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_campaign.ps1`
  - launches local, `-Remote`, `-PreflightOnly`, and `-EnqueueOnly` workflows
- `doc/scripts/campaigns/track_2/run_track2h_latent_state_hysteresis_campaign.md`
  - documents operator-facing commands

## Interpretation Rule

`Track 2H-L` should be treated as successful only if it improves normal
campaign metrics and then survives a separate official `Track 2` curve-first
verification refresh. Scalar improvement alone is not enough to promote it.
