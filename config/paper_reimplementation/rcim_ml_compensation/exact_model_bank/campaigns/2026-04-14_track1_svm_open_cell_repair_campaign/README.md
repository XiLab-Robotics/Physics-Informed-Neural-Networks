# Track 1 SVM Open-Cell Repair Campaign Package

This directory contains the prepared YAML package for the dedicated `SVR`
repair campaign against the currently open `SVM` cells in the canonical
`Track 1` benchmark.

The package is organized as one umbrella campaign with `12` explicit runs:

1. `01_track1_svm_amplitude_repair_baseline.yaml`
2. `02_track1_svm_amplitude_repair_seed11.yaml`
3. `03_track1_svm_amplitude_repair_seed23.yaml`
4. `04_track1_svm_amplitude_156_focus.yaml`
5. `05_track1_svm_amplitude_156_240_focus.yaml`
6. `06_track1_svm_amplitude_low_mid_bridge.yaml`
7. `07_track1_svm_phase_repair_baseline.yaml`
8. `08_track1_svm_phase_repair_seed11.yaml`
9. `09_track1_svm_phase_repair_seed23.yaml`
10. `10_track1_svm_phase_240_focus.yaml`
11. `11_track1_svm_phase_162_240_focus.yaml`
12. `12_track1_svm_phase_1_39_bridge.yaml`

Package rules:

- all runs keep `SVR` as the only enabled family;
- amplitude runs keep only `A_k` targets;
- phase runs keep only `phi_k` targets and exclude `phase_0`;
- each run uses a targeted `harmonic_order_filter` so the repair budget stays
  concentrated on currently open cells.
