# RCIM ML Compensation Script Notes

This documentation subtree mirrors the dedicated workflow grouping used in:

- `scripts/paper_reimplementation/rcim_ml_compensation/`

Use the matching subfolders:

- `exact_paper_model_bank/`
- `original_dataset_exact_model_bank/`
- `harmonic_wise_comparison/`
- `reference_family_vs_feedforward/`
- `recovered_original_workflow/`

For the recovered-original copied pipeline, the most detailed usage guide is
the code-adjacent README at:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

Current RCIM paper-faithful documentation split:

- `recovered_original_workflow/`
  documents the recovered author pipeline as a near-literal runnable copy under
  `scripts/`, with repository-owned path and runtime handling only where
  needed for repeatability.
- `original_dataset_exact_model_bank/`
  documents the faithful repository reimplementation of that pipeline on the
  canonical dataset, including forward/backward Track 1 campaign execution,
  accepted paper-reference archives, and RCIM Tables `2`-`5` reporting.

Current accepted model archives and benchmark tables:

- `models/paper_reference/rcim_track1/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Track 1 is closed for the current full-dataset paper-faithful surface. The
closed status means both forward and backward grid-search campaigns completed,
the accepted archives were refreshed, and Tables `2`-`5` were repopulated. It
does not mean every benchmark cell is green, and future all-green or
restricted-dataset studies should be documented as separate comparison
branches.
