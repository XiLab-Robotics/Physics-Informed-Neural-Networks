# Wave 5.2B And Wave 5.2C Model Design Gate

> Supersession note, `2026-08-04`: `Wave 5.2C` in this historical design is a
> within-machine dirty-to-clean hypothesis. It is separate from the canonical
> Cross-Machine Backbone Adaptation extension, which uses a source-machine
> checkpoint and a smaller dataset measured on a different target machine.

## Overview

This technical document prepares the next step after the completed `Wave 5.2A`
full paired-dataset matrix.

`Wave 5.2A` compared all `1938` paired directional records between
`simplified_dataset` and `polished_dataset`. The diagnostic found near-zero
peak-to-peak and smoothness deltas, mean absolute offset delta
`0.003216838 deg`, and a split between `901` offset-shifted pairs, `944`
nonzero-harmonic changed pairs, `65` nearly identical pairs, `27` sampling
anomalies, and `1` smoothness-changed pair.

The next step is a model-design gate, not a training campaign. Its purpose is
to translate the `Wave 5.2A` evidence into an implementable `Wave 5.2B` and
`Wave 5.2C` design specification before any new model class, training
configuration, or launcher is created.

No subagent is planned. If later review help is useful, the proposed subagent
name, reason, and delegated scope will be declared before asking for approval.

## Technical Approach

The design gate should produce a repository-authored analysis report that
chooses the next implementable branch based on the full paired matrix.

The current evidence argues against starting with a heavy full-physics PINN.
Instead, the first model-design candidate should be a lightweight,
causal-input-compatible architecture that can test the specific dataset
differences observed in `Wave 5.2A`:

- a primary TE prediction head;
- an offset / mean auxiliary head;
- a centered-shape loss term;
- a low-order and nonzero-harmonic consistency diagnostic or loss term;
- optional dirty-to-clean supervision from `simplified_dataset` toward
  `polished_dataset`;
- sampling-anomaly masks or exclusions;
- direction-aware reporting for `global`, `forward`, and `backward` surfaces.

The report should separate two implementation candidates:

| Candidate | Purpose |
| --- | --- |
| `Wave 5.2B` offset and harmonic guided model | Test offset / mean supervision, centered-shape loss, and harmonic-consistency penalties on the clean `polished_dataset` branch. |
| `Wave 5.2C` within-machine dirty-to-clean model | Test whether paired `simplified_dataset` evidence can improve robustness through dirty-to-clean auxiliary supervision or initialization. |

The design gate must also define what is deferred to `Wave 6`: integrated
multi-task / multi-head training, uncertainty heads, mixture heads, and final
clean deployment comparison after
the externally running full-wave `polished_dataset` retraining campaign is
closed and synchronized.

## Involved Components

Expected read-only inputs:

- `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/[2026-07-01]/wave52a_paired_dataset_diagnostics.md`;
- `output/validation_checks/wave52a_paired_dataset_diagnostics/2026-07-01-14-43-05__wave52a_full_paired_dataset_matrix/`;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- existing model-family reports for `Wave 3.3`, `Wave 4.1` through
  `Wave 4.4`, and `Wave 5.1`.

Expected output after approval:

- a model-design gate report under
  `doc/reports/analysis/model_development_waves/wave_5_2/model_design_gate/[YYYY-MM-DD]/`;
- optional machine-readable design tables under
  `output/validation_checks/wave52_model_design_gate/<run_instance_id>/`;
- synchronized entries in `doc/README.md`,
  `doc/running/te_model_live_backlog.md`,
  `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`, and
  `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Approved implementation output:

- `doc/reports/analysis/model_development_waves/wave_5_2/model_design_gate/[2026-07-01]/wave52b_wave52c_model_design_gate.md`;
- `output/validation_checks/wave52_model_design_gate/2026-07-01-15-30-07__wave52b_wave52c_model_design_gate/`.

Protected or deferred components:

- full-wave `polished_dataset` retraining campaign manifests, launchers,
  outputs, registries, and closeout artifacts;
- any `TE Curve Verification Pipeline` refresh package;
- new training campaign plans;
- model implementation files;
- training YAML files;
- campaign launchers.

## Implementation Steps

1. Read the full `Wave 5.2A` report and machine-readable aggregates.
2. Extract the model-design implications for offset, centered shape, harmonic
   consistency, sampling masks, dirty-to-clean supervision, and direction
   separation.
3. Compare those implications against the completed `Wave 3.3`, `Wave 4`
   series, and `Wave 5.1` lessons.
4. Draft the `Wave 5.2B` candidate specification:
   inputs, heads, losses, diagnostics, acceptance metrics, and deferred
   pieces.
5. Draft the `Wave 5.2C` candidate specification:
   paired-data usage, leakage-safe within-machine dirty-to-clean targets,
   initialization boundary, diagnostics, and rejection criteria.
6. Define what remains blocked until the externally running full-wave
   `polished_dataset` campaign closes.
7. Generate the model-design gate report and any compact design tables.
8. Synchronize the backlog, ledger, master summary, and documentation index.
9. Run Markdown QA on all touched authored Markdown files.

This step must stop after the design gate unless a later explicit approval
authorizes model implementation or training-campaign preparation.
