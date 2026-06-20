# RCIM Archive Parity Interpretation And GBM Grid Fix

## Overview

This document plans a narrow correction after the `rcim_original`,
`rcim_retuned`, and `rcim_track1` archive parity review.

The current evidence shows that `rcim_original` and `rcim_retuned` forward
archives are substantially equivalent as recovered-pipeline implementations,
with expected retune and stochastic differences. `rcim_track1` is intentionally
different because it is the faithful RCIM Model-Bank Reproduction reimplementation aligned with the
Wave 1 split policy rather than the recovered original row-level split.

Two technical checks were also performed:

- the TE Curve Verification Pipeline curve reconstruction already applies the required `h0` sign
  multiplier for `rcim_track1` forward candidates;
- the RCIM Model-Bank Reproduction GBM grid contains a transcription bug where the GBM
  `learning_rate` candidate list appends `min_samples_split` instead of the
  base estimator `learning_rate`.

## Technical Approach

The implementation will make two repository changes:

1. Correct the GBM grid in
   `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
   so the appended base value is `learning_rate`, matching the recovered
   `predictorML.py` grid.
2. Update
   `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Archive Parity Interpretation.md`
   to record the refined interpretation:
   `rcim_original` and `rcim_retuned` are substantially equivalent forward
   archives, while `rcim_track1` is intentionally split-aligned with Wave 1 and
   should not be expected to numerically match the recovered original split.

No training campaign will be launched by this change. The existing GBM
forward/backward best-parameter summaries selected `learning_rate: 0.1`, so the
grid typo is treated as a pipeline correctness fix for future runs rather than
proof that the accepted GBM archives are invalid.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Archive Parity Interpretation.md`
- `doc/README.md`

## Implementation Steps

1. Replace the GBM grid appended base value with
   `base_estimator.get_params()["learning_rate"]`.
2. Update the parity interpretation report with the split-policy distinction,
   the substantial-equivalence conclusion for `rcim_original` versus
   `rcim_retuned`, and the residual outlier notes for RCIM Model-Bank Reproduction `LGBM` and
   `MLP`.
3. Keep the TE Curve Verification Pipeline `h0` sign handling unchanged, because the current
   reconstruction logic is correct.
4. Run focused checks on the touched Python and Markdown scope.
5. Stop for final review before any commit.
