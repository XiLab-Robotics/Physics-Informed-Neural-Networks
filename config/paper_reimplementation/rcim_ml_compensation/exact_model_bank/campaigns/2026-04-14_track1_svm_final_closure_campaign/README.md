# Track 1 SVM Final Closure Campaign Package

This directory contains the prepared YAML package for the dedicated `SVR`
final-closure campaign against the residual yellow `SVM` cells in the
canonical `Track 1` benchmark.

The package is organized as one umbrella campaign with `12` explicit runs:

1. `01_track1_svm_amplitude_final_closure_baseline.yaml`
2. `02_track1_svm_amplitude_final_closure_seed11.yaml`
3. `03_track1_svm_amplitude_final_closure_seed23.yaml`
4. `04_track1_svm_amplitude_hard_tail_focus.yaml`
5. `05_track1_svm_amplitude_hard_tail_seed11.yaml`
6. `06_track1_svm_amplitude_40_bridge.yaml`
7. `07_track1_svm_amplitude_full_closure_split15.yaml`
8. `08_track1_svm_phase_final_closure_baseline.yaml`
9. `09_track1_svm_phase_final_closure_seed11.yaml`
10. `10_track1_svm_phase_final_closure_seed23.yaml`
11. `11_track1_svm_phase_final_closure_split15.yaml`
12. `12_track1_svm_phase_final_closure_split25.yaml`

Package rules:

- all runs keep `SVR` as the only enabled family;
- amplitude runs keep only `A_k` targets on harmonics `40`, `156`, `240`;
- phase runs keep only `phi_k` targets on harmonic `162`;
- each run uses a targeted `harmonic_order_filter` so the closure budget stays
  concentrated on the last residual cells.
