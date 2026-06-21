# Polished Dataset Default And Program Retraining

## Overview

Make `polished_dataset` the default training and verification dataset across
the repository while preserving an explicit `simplified_dataset` compatibility
mode.

The polished schema is point-based:

```text
theta,theta_dot,tau_load,T,theta_TE
```

The four model inputs must come directly from the measured or derived CSV
columns:

1. `theta`
2. `theta_dot`
3. `tau_load`
4. `T`

The target is `theta_TE`. Direction must come from the first-level
`forward/` or `backward/` folder and must not be inferred from the filename.
Filename speed, torque, and temperature remain setpoint metadata only.

After compatibility implementation and validation, prepare a staged retraining
program for every repository-owned learned family from Track 1 onward. The
recovered paper-original pipeline and paper-retuned models are explicitly
excluded from retraining.

## Technical Approach

Introduce a canonical dataset selector with supported values:

```text
polished_dataset
simplified_dataset
```

The default is `polished_dataset`. Runnable dataset consumers will accept a
`--dataset` input where they already expose a CLI, or consume the same selector
from their YAML/configuration surface when launched through campaign tooling.
Shared resolution logic will prevent each script from implementing its own
path mapping.

Implement two explicit sample builders behind one dataset interface:

- polished mode reads direction from the path and returns four pointwise input
  features plus `theta_TE`;
- simplified mode preserves the legacy five-feature contract based on
  position, nominal operating conditions, and `direction_flag`.

The feature schema and input dimension must be stored in run artifacts,
registries, exports, and Track 2 candidate metadata. Models and evaluators must
resolve input dimension from the selected dataset instead of assuming `5`.
Existing simplified-trained artifacts remain readable and evaluable with their
recorded legacy schema.

Dataset splitting must remain source-file based to prevent row leakage between
train, validation, and test sets. For polished mode, each directional CSV is
one source sample. Point and sequence collators remain top-level functions so
multi-worker PyTorch DataLoaders can pickle them safely.

Track 1 requires a separate adapter because its harmonic workflows consume
curve-level or FFT-derived targets rather than direct point targets. The
adapter will reconstruct each directional curve from polished rows and derive
the required harmonic representation without reading nominal model inputs from
filenames.

## Involved Components

- `config/datasets/transmission_error_dataset.yaml`
- the 52 current dataset-variant YAML files under `config/training/`
- `scripts/datasets/transmission_error_dataset.py`
- `scripts/datasets/export_dataset_split.py`
- `scripts/datasets/visualize_transmission_error.py`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/run_training_campaign.py`
- active Track 1 harmonic and exact-model-bank support
- active Wave 1, Wave 2, Wave 3, and Track 2H campaign tooling
- Track 2 curve construction, candidate loading, and report builders
- model and program registries under `output/registries/`
- user-facing dataset, training, campaign, and portal documentation

The audit found 11 direct Python dataset consumers, 52 dataset-root
configurations, and 21 configured model types requiring compatibility review.

## Implementation Steps

1. Add the dataset selector, canonical root mapping, schema identifiers, and
   feature-name contracts with `polished_dataset` as the default.
2. Implement polished directional discovery from
   `polished_dataset/<direction>/<temperature>/<speed>/*.csv`.
3. Implement strict polished CSV validation and pointwise tensor construction
   from the four input columns and `theta_TE`.
4. Preserve the simplified loader as a separate legacy schema selected through
   `dataset=simplified_dataset`.
5. Make datamodule splitting, normalization, point collation, sequence
   collation, model construction, reporting, exports, and registries
   schema-aware.
6. Add dataset selection to every active runnable consumer while excluding
   recovered paper-original and paper-retuned training entry points.
7. Adapt repository-owned Track 1 preprocessing to derive curve and harmonic
   targets from polished rows.
8. Update the 52 active dataset-variant configurations and replace fixed
   `input_size: 5` assumptions with validated schema-specific dimensions.
9. Add smoke tests for both schemas, all direction scopes, point models,
   sequence models, tree models, harmonic models, exports, and Track 2 curve
   evaluation.
10. Prepare the approved staged retraining campaign package, dedicated
    PowerShell launcher with local and `-Remote` modes, launcher note, campaign
    YAMLs, and persistent active-campaign state.
11. Execute no training automatically. Wait for the user to launch each
    approved stage and report completion.
12. Close out each stage before preparing the separate final Track 2 refresh
    launcher and accepting new verification artifacts.

## Compatibility And Acceptance Rules

- `polished_dataset` must be the default everywhere after migration.
- `simplified_dataset` must remain selectable and must retain legacy behavior.
- Polished model inputs are exactly four columns; no filename-derived setpoint
  values or additional direction flag may enter the model input tensor.
- Direction filters use folder provenance.
- Splits operate at file level, never at row level.
- Existing artifacts record or infer the legacy simplified schema and are not
  silently reinterpreted as polished models.
- Paper-original and paper-retuned training code, models, and registries remain
  immutable.
- Frozen paper references may remain visible in Track 2 as comparison-only
  baselines, but they are not retrained or relabeled as polished models.
- The retraining campaign must use new immutable run-instance directories and
  must not overwrite prior simplified-dataset results.
