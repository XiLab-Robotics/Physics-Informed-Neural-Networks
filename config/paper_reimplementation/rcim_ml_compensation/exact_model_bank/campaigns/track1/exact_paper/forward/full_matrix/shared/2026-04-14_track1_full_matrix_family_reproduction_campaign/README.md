# Track 1 Full-Matrix Family Reproduction Campaign Package

This directory contains the prepared YAML package for the next `Track 1`
exact-paper family-reproduction campaign.

The package is organized as one umbrella campaign with `20` explicit runs:

1. `01_track1_svm_amplitude_full_matrix.yaml`
2. `02_track1_svm_phase_full_matrix.yaml`
3. `03_track1_mlp_amplitude_full_matrix.yaml`
4. `04_track1_mlp_phase_full_matrix.yaml`
5. `05_track1_rf_amplitude_full_matrix.yaml`
6. `06_track1_rf_phase_full_matrix.yaml`
7. `07_track1_dt_amplitude_full_matrix.yaml`
8. `08_track1_dt_phase_full_matrix.yaml`
9. `09_track1_et_amplitude_full_matrix.yaml`
10. `10_track1_et_phase_full_matrix.yaml`
11. `11_track1_ert_amplitude_full_matrix.yaml`
12. `12_track1_ert_phase_full_matrix.yaml`
13. `13_track1_gbm_amplitude_full_matrix.yaml`
14. `14_track1_gbm_phase_full_matrix.yaml`
15. `15_track1_hgbm_amplitude_full_matrix.yaml`
16. `16_track1_hgbm_phase_full_matrix.yaml`
17. `17_track1_xgbm_amplitude_full_matrix.yaml`
18. `18_track1_xgbm_phase_full_matrix.yaml`
19. `19_track1_lgbm_amplitude_full_matrix.yaml`
20. `20_track1_lgbm_phase_full_matrix.yaml`

These configs all target:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

Package rules:

- amplitude runs keep only `A_k` targets for harmonics
  `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240`;
- phase runs keep only `phi_k` targets for harmonics
  `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240`;
- each run enables exactly one paper family, so each completed artifact can
  populate one family row of the paper-matrix dashboard.
