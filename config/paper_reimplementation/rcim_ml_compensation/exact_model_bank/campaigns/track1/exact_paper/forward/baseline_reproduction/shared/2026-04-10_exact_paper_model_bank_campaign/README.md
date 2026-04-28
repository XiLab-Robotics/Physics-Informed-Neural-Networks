# Exact Paper Model Bank Campaign Package

This directory contains the prepared YAML package for the first batch campaign
of the strict RCIM exact-paper branch.

The campaign launcher should run these files in order:

1. `01_exact_full_bank_diagnostic_continue.yaml`
2. `02_exact_full_bank_strict_reference.yaml`
3. `03_exact_svr_export_diagnostic.yaml`
4. `04_exact_non_svr_export_reference.yaml`

These configs all target:

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/run_exact_paper_model_bank_validation.py`

The purpose of the package is to stabilize the exact-paper export surface while
keeping the full recovered family bank as the main reference branch.
