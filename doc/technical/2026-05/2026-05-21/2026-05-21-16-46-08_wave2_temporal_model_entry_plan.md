# Wave 2.1 Temporal Model Entry Plan

## Overview

Open `Wave 2.1` as the temporal-model branch of the TE modeling program.

`Wave 1` closed the structured static baseline surface and `TE Curve Verification Pipeline` is now the
official offline model-verification report. `Wave 2.1` should therefore test
whether lightweight temporal context improves curve prediction beyond the
closed `Wave 1` baselines without losing the direction-aware reporting contract
or the future TwinCAT deployment discipline.

The initial Wave 2.1 scope is planning and implementation preparation only. No
training campaign will be executed until a separate campaign plan under
`doc/reports/campaign_plans/` is created and explicitly approved.

No subagent use is planned for this task.

## Technical Approach

Use a staged temporal-model entry instead of jumping directly to the most
complex sequence family.

The first implementation branch should introduce three lightweight sequence
families:

- `temporal_convolution`: a compact temporal convolutional network candidate
  for short-window curve context;
- `gru_sequence`: a compact gated recurrent candidate using the simpler
  recurrent memory baseline;
- `lstm_sequence`: a compact gated recurrent candidate using the more
  expressive hidden-state plus cell-state memory baseline.

The `State-Space Sequence Model` branch remains planned, but should not be the
first Wave 2.1 implementation unless the lightweight baseline fails for a reason
that specifically motivates state-space memory. This keeps the first Wave 2.1
campaign inspectable, fast to debug, and comparable to the closed Wave 1
surfaces.

Every Wave 2.1 family must preserve the repository direction rule:

| Surface | Training scope | Evaluation scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

Wave 2.1 candidates must be evaluated back through the official `TE Curve Verification Pipeline`
verification workflow. A model is not accepted only because its training MAE is
good; it must refresh the direction-aware matrix, visual reports, and official
TE Curve Verification Pipeline update ledger when promoted.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-05-21]/track2_official_model_verification_report.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/`
- `config/training/hydra/wave1/`
- future `config/training/hydra/wave2/`
- `scripts/models/model_factory.py`
- `scripts/models/`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/validate_training_setup.py`
- `scripts/training/run_training_smoke_test.py`
- `output/training_runs/`
- `output/validation_checks/`
- `output/registries/`

## Implementation Steps

1. Inspect the current dataset windowing, batching, and curve metadata flow in
   `transmission_error_datamodule.py` and the current model output contract in
   `transmission_error_regression_module.py`.
2. Define the Wave 2.1 data-window contract:
   - input sequence length;
   - stride or neighborhood sampling;
   - angular-position handling;
   - preservation of speed, torque, oil temperature, encoder zeroing, and
     `DataValid` semantics;
   - output shape compatible with the existing TE regression objective.
3. Add Wave 2.1 model-family scaffolding only after approval:
   - `temporal_convolution`;
   - `temporal_convolution_fw`;
   - `temporal_convolution_bw`;
   - `gru_sequence`;
   - `gru_sequence_fw`;
   - `gru_sequence_bw`;
   - `lstm_sequence`;
   - `lstm_sequence_fw`;
   - `lstm_sequence_bw`.
4. Add Wave 2.1 Hydra configuration roots under `config/training/hydra/wave2/`
   using the existing Wave 1 pattern where practical.
5. Prepare a preliminary campaign report under
   `doc/reports/campaign_plans/wave_2/` before any training execution.
6. For the first campaign, keep the run count narrow:
   - three `temporal_convolution` surfaces;
   - three `gru_sequence` surfaces;
   - three `lstm_sequence` surfaces;
   - optional one-batch validation and smoke-test entries before full runs.
7. After campaign approval and execution, route promoted results through:
   - family and program registries;
   - `Training Results Master Summary.md`;
   - the official `TE Curve Verification Pipeline` model-verification report;
   - the best-model collage and multi-model curve comparison reports.
8. Keep `Track 3` and online compensation out of Wave 2.1 unless a later
   approved technical document explicitly promotes deployment evaluation.
