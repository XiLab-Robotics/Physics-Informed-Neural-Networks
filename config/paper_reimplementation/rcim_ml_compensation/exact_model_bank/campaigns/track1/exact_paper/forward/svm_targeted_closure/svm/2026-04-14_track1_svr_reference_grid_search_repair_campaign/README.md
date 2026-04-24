# Track 1 SVR Reference Grid Search Repair Campaign Package

This directory contains the prepared YAML package for the first `SVR` repair
campaign that uses the recovered paper-reference `GridSearchCV` path.

The package is organized as one umbrella campaign with `4` explicit runs:

1. `01_track1_svr_reference_grid_amplitude_pair.yaml`
2. `02_track1_svr_reference_grid_amplitude_40_only.yaml`
3. `03_track1_svr_reference_grid_amplitude_240_only.yaml`
4. `04_track1_svr_reference_grid_phase_162_only.yaml`

Package rules:

- all runs keep `SVR` as the only enabled family;
- all runs keep the exact-paper split settings unchanged;
- all runs force `training.hyperparameter_search.mode` to
  `paper_reference_grid_search`;
- amplitude runs keep only the residual harmonics `40` and `240`;
- the phase run keeps only the residual harmonic `162`.
