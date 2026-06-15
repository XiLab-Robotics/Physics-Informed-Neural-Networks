# Wave 3 Track 2 Verification Refresh

## Overview

This technical document defines the separate official `Track 2` verification
refresh for the completed first real `Wave 3` harmonic-prior residual
campaign. The campaign closeout is complete, the active campaign state is
`none`, and the closeout report explicitly leaves official curve verification
as a separate operator-launched acceptance gate.

The refresh will decide whether the scalar `Wave 3` training results translate
into useful held-out transmission-error curve behavior. The decision must not
be inferred from scalar training `MAE` alone.

The refresh keeps the required direction-parallel surfaces:

- `global`;
- `Fw`;
- `Bw`.

No subagent is planned for this step. If a subagent becomes useful later, its
name, task boundary, and approval requirement must be documented before launch.

## Technical Approach

The work will add six registry-backed `Wave 3` candidates to the official
direction-aware `Track 2` matrix and prepare a PowerShell launcher that the
operator can run locally or with `-Remote`. Codex will not run the heavy
matrix during preparation.

The candidate set is:

| Profile | Surface | Family Registry |
| --- | --- | --- |
| `pointwise_control` | `global` | `wave3_harmonic_prior_residual_pointwise_control_global` |
| `pointwise_control` | `Fw` | `wave3_harmonic_prior_residual_pointwise_control_fw` |
| `pointwise_control` | `Bw` | `wave3_harmonic_prior_residual_pointwise_control_bw` |
| `smooth_l1_structured` | `global` | `wave3_harmonic_prior_residual_smooth_l1_structured_global` |
| `smooth_l1_structured` | `Fw` | `wave3_harmonic_prior_residual_smooth_l1_structured_fw` |
| `smooth_l1_structured` | `Bw` | `wave3_harmonic_prior_residual_smooth_l1_structured_bw` |

Direction semantics remain unchanged:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

The `wave3_harmonic_prior_residual` model emits deterministic scalar TE
predictions and can use the existing registry-backed
`TransmissionErrorRegressionModule` inference path. The matrix generation code
still needs a new compact registry group so the six candidates are expanded
from the template.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/campaigns/track2/run_wave3_harmonic_prior_residual_track2_verification_refresh.ps1`
- `doc/scripts/campaigns/track2/run_wave3_harmonic_prior_residual_track2_verification_refresh.md`
- `output/registries/families/wave3_harmonic_prior_residual_*`
- `output/training_runs/wave3_harmonic_prior_residual_*`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/track2/best_model_collage_report/[YYYY-MM-DD]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[YYYY-MM-DD]/`
- `doc/reports/analysis/track2/official_model_verification_report/[YYYY-MM-DD]/`

## Implementation Steps

1. Confirm active campaign status is `none` and the six `Wave 3` family
   registries exist.
2. Add a compact `Wave 3` registry group to the official full `Track 2`
   matrix template.
3. Extend the matrix candidate-generation support code so the new registry
   group is expanded into `global`, `Fw`, and `Bw` candidates.
4. Create a dedicated operator launcher with local and `-Remote` execution.
5. Create the matching launcher documentation with exact commands and expected
   outputs.
6. Register this technical document and launcher note from `doc/README.md`.
7. Run syntax and Markdown checks on the touched scope.
8. Stop after providing the exact launch commands and wait for the operator to
   run the refresh.
