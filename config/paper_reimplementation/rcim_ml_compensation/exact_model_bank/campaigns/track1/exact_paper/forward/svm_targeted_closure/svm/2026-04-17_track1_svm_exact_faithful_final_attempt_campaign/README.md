# Track 1 SVM Exact-Faithful Final Attempt Campaign Package

This directory contains the prepared YAML package for the final strict
paper-faithful `SVR` confirmation campaign on the residual `SVM` yellow cells.

The package is organized as one umbrella campaign with `4` explicit runs:

1. `01_track1_svr_exact_faithful_amplitude_pair_repeat.yaml`
2. `02_track1_svr_exact_faithful_amplitude_40_repeat.yaml`
3. `03_track1_svr_exact_faithful_amplitude_240_repeat.yaml`
4. `04_track1_svr_exact_faithful_phase_162_repeat.yaml`

Package rules:

- all runs keep `SVR` as the only enabled family;
- all runs keep the exact-paper split settings unchanged;
- all runs force `training.hyperparameter_search.mode` to
  `paper_reference_grid_search`;
- no run widens the recovered paper `SVR` search space;
- amplitude runs keep only the residual harmonics `40` and `240`;
- the phase run keeps only the residual harmonic `162`.
