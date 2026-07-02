# Wave 5.2B Offset And Harmonic Guided Model

## Model Description

`Wave 5.2B` is the planned lightweight offset and nonzero-harmonic guided
model branch for the dataset-aware `Wave 5.2` program.

The branch exists because the completed `Wave 5.2A` full paired-dataset matrix
showed that `simplified_dataset` and `polished_dataset` are well aligned at
the curve-shape level but differ materially in mean / offset and nonzero
harmonic content:

| Signal | Value |
| --- | ---: |
| Evaluated paired directional records | 1938 |
| Mean absolute offset delta [deg] | 0.003216838 |
| Mean absolute peak-to-peak delta [deg] | 0.000000134 |
| Mean absolute smoothness delta [deg] | 0.000000003 |
| Mean maximum nonzero-harmonic delta [deg] | 0.001749405 |
| Offset-shifted pairs | 901 |
| Nonzero-harmonic changed pairs | 944 |
| Shape-changed pairs | 0 |

The model should not start as a complete physics-informed neural network. It
should first test whether a causal neural model improves the observed offset
and harmonic gaps without degrading raw TE prediction or centered curve shape.

## Operating Principle

The planned model keeps the repository's causal runtime boundary:

- current point state;
- explicit short causal history if the selected trunk requires a sequence;
- causal operating-condition features;
- no future TE samples;
- no measured full-curve target mean at inference;
- no offline polishing operation inside runtime inference.

The intended prediction structure is:

```text
te_prediction = pointwise_te_head(causal_features)
offset_prediction = offset_head(causal_features)
guided_te_prediction = te_prediction + offset_prediction
```

The offset head is a learned auxiliary path. It may be trained against
train-time curve-mean or low-frequency targets, but the deployed path must use
only the model's predicted offset output.

Nonzero-harmonic guidance is treated as a train-time or validation constraint.
It can penalize harmonic-amplitude mismatch over validation windows, but it
must not require future measured TE samples at inference.

## Conceptual Structure

The implemented first package stays compact:

| Component | Role |
| --- | --- |
| Causal trunk | Reuse an existing pointwise, periodic, or sequence-capable TE feature path. |
| Primary TE head | Predict the normalized or physical TE target used by the current training module. |
| Offset / mean head | Predict condition-linked low-frequency correction. |
| Centered-shape loss | Keep waveform quality visible when offset improves. |
| Harmonic consistency metric or loss | Track the nonzero-harmonic difference exposed by `Wave 5.2A`. |
| Sampling mask | Exclude or downweight the `27` paired sampling anomalies when paired evidence is used. |

The branch exposes auxiliary outputs for diagnostics. Those outputs are
not optional: without them, the campaign cannot prove whether improvement came
from raw pointwise fitting, offset correction, centered-shape behavior, or
harmonic consistency.

## Project Context

`Wave 5.2B` sits after four relevant evidence layers:

| Evidence | Consequence |
| --- | --- |
| `CVP 1.4` and `CVP 1.5` | Offset is real and partly condition-linked, but not sufficient alone. |
| `Wave 4.1`-`Wave 4.4` | Robust, probabilistic, MDN, and stateful heads remain integration evidence, not immediate defaults. |
| `Wave 5.1` | Compact harmonic-prior residual structure is useful, but not promoted. |
| `Wave 5.2A` | Dataset differences point to offset and nonzero harmonics, not broad shape or smoothness drift. |

The first `Wave 5.2B` campaign should therefore be an ablation, not a large
architecture contest.

## Advantages

- Directly targets the strongest paired-dataset signals.
- Keeps the causal deployment boundary explicit.
- Separates raw TE prediction from offset correction for diagnostics.
- Keeps centered shape visible so offset improvement cannot hide waveform
  degradation.
- Preserves `global`, `forward`, and `backward` surfaces.
- Leaves `Wave 5.2C` dirty-to-clean transfer and `Wave 6` integration as
  follow-up branches instead of mixing all mechanisms at once.

## Disadvantages

- Requires train-time curve grouping to define offset and centered-shape
  losses safely.
- Harmonic consistency can only be a training or validation diagnostic unless
  reformulated as a causal predicted quantity.
- The first campaign may show that offset/harmonic guidance helps only one
  direction surface.
- It will not by itself answer reduced-point robustness or dirty-to-clean
  transfer.
- It must wait for official polished full-wave evidence before final
  deployability decisions.

## Implemented Components

The prepared package introduces or extends:

- model code:
  `scripts/models/wave52b_offset_harmonic_guided_network.py`;
- model factory registration:
  `scripts/models/model_factory.py`;
- campaign runner registration:
  `scripts/training/run_training_campaign.py`;
- prepared 12-run package:
  `config/training/wave52b_offset_harmonic_guided/campaigns/2026-07-01_wave52b_offset_harmonic_guided_campaign/`;
- package preparer and validator:
  `scripts/campaigns/wave_5_2/prepare_wave52b_offset_harmonic_guided_campaign.py`
  and
  `scripts/campaigns/wave_5_2/validate_wave52b_offset_harmonic_guided_campaign.py`;
- dedicated launcher and note:
  `scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.ps1`
  and
  `doc/scripts/campaigns/wave_5_2/run_wave52b_offset_harmonic_guided_campaign.md`;
- active campaign state with protected-file tracking:
  `doc/running/active_training_campaign.yaml`.

The model returns `base_prediction_tensor`,
`residual_offset_prediction_tensor`, `structured_prediction_tensor`,
`wave52b_harmonic_prediction_tensor`, and `prediction_tensor`. The training
module's existing curve-aware loss terms provide pointwise, offset,
centered-shape, amplitude, and sparse-harmonic pressure.

## Verification Plan

Before training, the package should pass:

- Python compile checks for new or modified model and training files;
- one-batch validation on each surface;
- fast-dev-run smoke for at least the `global` entry;
- campaign package validation;
- launcher preflight;
- Markdown QA for authored documentation.

The prepared package is not a completed training result. No training run,
fast-dev-run smoke, campaign closeout, PDF result report, or official
`TE Curve Verification Pipeline` refresh is produced by this preparation step.

After training, normal campaign closeout must produce campaign winner
artifacts and a Markdown/PDF campaign-results report. Official `TE Curve
Verification Pipeline` refresh remains a separate optional operator-approved
step after normal closeout.
