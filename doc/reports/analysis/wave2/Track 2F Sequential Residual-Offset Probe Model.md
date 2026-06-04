# Track 2F Sequential Residual-Offset Probe Model

## Model Description

`sequential_residual_offset_probe` is the first learned `Track 2F`
offset-aware candidate.

It is designed to test whether the persistent curve-level vertical offset
found by `Track 2D` and `Track 2E` can be reduced by a trainable causal branch
without changing the deployment input contract.

The model predicts normalized transmission error as:

```text
final_te_prediction = base_te_prediction + residual_offset_prediction
```

The base branch uses the current sequence readout point. The residual-offset
branch uses a short sequence window built from already available runtime
features. The model does not consume future TE samples, true full-curve means,
or complete-curve normalization at inference time.

This first Track 2F model is deliberately non-harmonic. It does not use the
explicit periodic `sin`/`cos` feature expansion used by periodic MLP or
periodic sequence families, and it does not embed the `RCIM` harmonic index
bank used by harmonic or residual-harmonic families. That makes it a clean
baseline for later tests where the new ingredient is a curve index,
multi-head structure, or composite loss rather than forced harmonic shape.

## Operating Principle

The branch split is intentionally simple:

- `base_te_prediction` learns the local point-level TE mapping from the
  readout state;
- `residual_offset_prediction` learns a lower-frequency correction from the
  supported short causal history;
- the summed output is trained with the existing normalized-space regression
  loss.

The first implementation keeps the loss compatible with the current
`TransmissionErrorRegressionModule`. Curve-first acceptance is deferred to
post-training `Track 2` verification rather than embedded into the first
training loss.

## Conceptual Structure

The implemented PyTorch module contains:

- a feedforward readout branch for `base_te_prediction`;
- a `GRU` sequence branch for `residual_offset_prediction`;
- branch-level auxiliary outputs used for diagnostics;
- one final summed normalized TE prediction.

The campaign materializes three direction-parallel training entries:

| Surface | Model Family | Dataset Scope |
| --- | --- | --- |
| `global` | `sequential_residual_offset_probe` | forward and backward |
| `Fw` | `sequential_residual_offset_probe_fw` | forward only |
| `Bw` | `sequential_residual_offset_probe_bw` | backward only |

## Advantages

- Preserves the practical runtime input boundary.
- Keeps `Fw`, `Bw`, and `global` branches in parallel.
- Separates base prediction from residual-offset correction for diagnostics.
- Reuses the existing Lightning training and campaign infrastructure.
- Creates a direct learned comparator against the post-hoc
  `direction_torque` baseline from `Track 2E`.

## Disadvantages

- The first loss is still pointwise normalized MSE, so final acceptance still
  depends on later curve-first `Track 2` verification.
- The model is not forced to preserve harmonic TE waveform shape; visually it
  can behave similarly to a feedforward baseline when the residual branch
  learns mostly low-frequency correction.
- The branch split is not guaranteed to make the residual branch learn only
  offset; it is encouraged by structure and diagnostics, not hard constrained.
- It does not yet implement the planned multi-head centered-shape/offset
  architecture.
- It may improve raw curve error while still leaving amplitude or phase
  limitations, which must be checked after training.

## Baseline Role

Track 2F should remain in the comparison matrix even if the next family moves
to harmonic-offset or periodic multi-head structures. It answers a different
question from harmonic models:

- clean Track 2F baseline: what can a causal non-harmonic residual structure
  do with the current input contract?
- harmonic-offset follow-up: what improves when the shape branch is explicitly
  periodic or harmonic and the offset branch is trained separately?

Future new-index, multi-head, or composite-loss campaigns should keep a
Track 2F-like clean branch in parallel with `global`, `Fw`, and `Bw` surfaces
so the effect of the objective can be separated from the effect of harmonic
feature forcing.

## Implemented Components

Core model implementation:

- `scripts/models/sequential_residual_offset_network.py`
  - `SequentialResidualOffsetNetwork`
  - `compute_auxiliary_output_dictionary`
  - `forward_with_input_context`

Model and training registration:

- `scripts/models/model_factory.py`
  - `create_model`
- `scripts/models/__init__.py`
- `scripts/training/run_training_campaign.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/transmission_error_regression_module.py`

Campaign preparation and launcher:

- `scripts/campaigns/track2/prepare_track2f_offset_aware_probe_campaign.py`
- `scripts/campaigns/track2/run_track2f_offset_aware_probe_campaign.ps1`
- `scripts/campaigns/track2/validate_track2f_offset_aware_probe_package.py`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/`

## Verification Status

The implementation has passed:

- Python compile checks for touched model, training, and campaign scripts;
- package preflight validation through the Track 2F launcher;
- one-batch validation setup checks for `global`, `Fw`, and `Bw`;
- one fast-dev smoke training pass for the `global` entry.

Full campaign training is still an operator-launched step. After completion,
the resulting models must return through official `Track 2` curve-first
verification before any promotion decision.
