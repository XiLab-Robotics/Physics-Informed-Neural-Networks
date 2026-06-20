# TE Curve Verification Pipeline Direction Truth And Preview Audit

## Overview

This technical document formalizes the audit requested after inspecting the
TE Curve Verification Pipeline preview image:

```text
output/validation_checks/track2_reference_comparison/2026-05-18-11-10-34__track2_full_directional_family_matrix_original_retuned_matrix_validation/preview_curves/preview_01.png
```

The preview shows `SVM19_Fw` evaluated on a forward curve, but its predicted TE
curve has the opposite sign offset from the plotted truth curve. That is a
strong indication that the curve-verification comparison may be mixing one of these
surfaces incorrectly:

- model training direction provenance;
- truth-curve direction filtering;
- harmonic amplitude/phase sign convention;
- reconstructed RCIM Model-Bank Reproduction/reference-bank TE sign convention;
- Wave 1 pointwise input or direction-label handling.

The task also asks to extend PNG generation to every evaluated model and place
the images under a report-facing folder grouped by model source and family.

No subagent use is planned. If subagent use becomes useful later, this document
must be updated with the proposed subagent name, delegated task boundary, and
approval requirement before any subagent is launched.

## Technical Approach

The work must proceed in two phases.

First, audit correctness before trusting any additional report images:

- verify that each forward paper-reference archive was trained from forward
  data only;
- verify that each backward paper-reference archive was trained from backward
  data only;
- verify that each Wave 1 `Fw` export was trained from forward data only;
- verify that each Wave 1 `Bw` export was trained from backward data only;
- verify that TE Curve Verification Pipeline filters truth curves by `direction_label == "forward"`
  for forward candidates and `direction_label == "backward"` for backward
  candidates;
- verify whether RCIM Model-Bank Reproduction/reference-bank reconstruction requires a sign or
  phase convention adjustment before comparing to repository truth curves.

Second, extend preview generation after the audit:

- generate PNG overlays for every candidate, not only the first few candidate
  entries;
- group report-facing images under:

```text
doc/reports/campaign_results/track_2/verification_plots/
```

- use source folders:
  - `original/`
  - `original retuned/`
  - `track 1/`
  - `wave 1/`
- add a family subfolder inside each source folder;
- make filenames direction-aware and condition-aware so repeated operating
  points do not overwrite each other.

The image extension must not hide a data-alignment bug. If the audit confirms a
sign-convention or direction-filtering defect, fix that first, regenerate the
TE Curve Verification Pipeline metrics, then generate the complete image tree from the corrected
comparison.

## Involved Components

- `models/paper_reference/rcim_original/`
  - inspect forward archive provenance.
- `models/paper_reference/rcim_retuned/`
  - inspect forward and backward archive provenance.
- `models/paper_reference/rcim_track1/`
  - inspect accepted RCIM Model-Bank Reproduction forward and backward archive provenance.
- `models/exported/`
  - inspect Wave 1 global, forward, and backward export provenance.
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - audit and, if needed, correct direction filtering, reconstruction, and
    preview generation.
- `output/validation_checks/track2_reference_comparison/`
  - regenerate validation artifacts if the comparison logic changes.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - update results and artifact pointers after any corrected run.
- `doc/reports/campaign_results/track_2/verification_plots/`
  - store grouped report-facing PNG overlays.

## Implementation Steps

1. Inspect the source metadata for representative and then all archive groups:
   `rcim_original`, `rcim_retuned`, `rcim_track1`, and `Wave 1`.
2. Build a compact provenance table showing each source/surface/family and
   whether its metadata declares forward-only, backward-only, or global data.
3. Inspect the TE Curve Verification Pipeline per-condition CSV and preview source row for
   `SVM19_Fw` to confirm it is paired with a forward truth curve.
4. Compare harmonic coefficients or amplitude/phase fields for the plotted
   sample to determine whether the RCIM Model-Bank Reproduction/reference-bank reconstruction sign
   convention is inverted relative to the repository truth curve.
5. If a direction or sign-convention defect is found, fix the comparison logic
   and rerun the TE Curve Verification Pipeline validation matrix.
6. Extend image generation so each candidate emits grouped PNGs under
   `doc/reports/campaign_results/track_2/verification_plots/<source>/<family>/`.
7. Regenerate the canonical TE curve-verification report and validation artifacts after any
   logic or image-output change.
8. Run Python syntax checks and a focused TE Curve Verification Pipeline validation run.
9. Run Markdown QA on touched authored Markdown.
10. Report the audit result clearly before any commit, including whether the
    prior metrics are valid or superseded.
