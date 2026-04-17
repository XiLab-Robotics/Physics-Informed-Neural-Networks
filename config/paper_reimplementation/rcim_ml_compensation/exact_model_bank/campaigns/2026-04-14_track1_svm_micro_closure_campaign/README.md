# Track 1 SVM Micro-Closure Campaign Package

This directory contains the prepared YAML package for the dedicated `SVR`
micro-closure campaign against the last residual yellow `SVM` cells in the
canonical `Track 1` benchmark.

The package is organized as one umbrella campaign with `8` explicit runs:

1. `01_track1_svm_amplitude_micro_closure_baseline.yaml`
2. `02_track1_svm_amplitude_micro_closure_seed23.yaml`
3. `03_track1_svm_amplitude_micro_closure_split15.yaml`
4. `04_track1_svm_amplitude_40_only.yaml`
5. `05_track1_svm_amplitude_240_only.yaml`
6. `06_track1_svm_phase_micro_closure_baseline.yaml`
7. `07_track1_svm_phase_micro_closure_split15.yaml`
8. `08_track1_svm_phase_micro_closure_seed23.yaml`

Package rules:

- all runs keep `SVR` as the only enabled family;
- amplitude runs keep only `A_k` targets on harmonics `40` and `240`;
- phase runs keep only `phi_k` targets on harmonic `162`;
- each run uses a targeted `harmonic_order_filter` so the closure budget stays
  concentrated on the last residual cells.
