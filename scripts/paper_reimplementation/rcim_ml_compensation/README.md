# RCIM ML Compensation Script Surface

This subtree groups the repository-owned RCIM paper-reimplementation workflows
by dedicated branch instead of leaving unrelated runners and support modules in
one flat folder.

## Dedicated Workflow Folders

- `exact_paper_model_bank/`
  Strict recovered-CSV exact-paper family-bank validation.
- `original_dataset_exact_model_bank/`
  Direction-specific exact-paper family-bank validation rebuilt from the
  canonical repository dataset.
- `harmonic_wise_comparison/`
  Repository-owned harmonic-wise comparison and playback workflow.
- `reference_family_vs_feedforward/`
  Track 2 comparison between one archived reference bank and the feedforward
  best model.
- `recovered_original_workflow/`
  Copied recovered-original code surface reorganized into the three original
  stages: dataframe creation, training, and evaluation.

## Entry Points

- `exact_paper_model_bank/run_exact_paper_model_bank_validation.py`
- `original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `original_dataset_exact_model_bank/generate_original_dataset_exact_smoke_configs.py`
- `harmonic_wise_comparison/run_harmonic_wise_comparison_pipeline.py`
- `reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `recovered_original_workflow/run_recovered_original_workflow.py`

## Notes

- Support modules now live beside the runner that owns them.
- The recovered-original workflow is intentionally separated from the
  repository-designed workflows because it preserves copied paper-era code and
  original-style runtime assumptions.
- The detailed recovered-original usage guide lives in
  `recovered_original_workflow/README.md`.
