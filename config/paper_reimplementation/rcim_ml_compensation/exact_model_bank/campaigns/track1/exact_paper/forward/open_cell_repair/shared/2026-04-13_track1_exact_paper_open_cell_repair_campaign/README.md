# Track 1 Exact-Paper Open-Cell Repair Campaign Package

This directory contains the prepared YAML package for the next `Track 1`
exact-paper campaign under the paper-table-first closure rule.

The campaign launcher should run these files in order:

1. `01_exact_open_cell_refresh_full_bank.yaml`
2. `02_exact_open_cell_low_order_repair.yaml`
3. `03_exact_open_cell_high_order_tree_repair.yaml`
4. `04_exact_open_cell_paper_family_reference.yaml`
5. `05_exact_open_cell_phase_gap_bridge.yaml`
6. `06_exact_open_cell_tree_control_bank.yaml`

These configs all target:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`

The purpose of the package is to close still-open exact-paper cells in Tables
`3-6`, especially around harmonics `0`, `1`, `3`, `81`, `162`, and `240`.
