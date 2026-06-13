# Track 2 Visual Builder Auto Group Coverage

## Overview

`Track 2` refresh launchers already run the matrix, collage report, overlay
report, and visual PDF export in one operator command. The repeated closure
gap is that the matrix can include a newly approved registry source while the
visual builders still expose only the previous hardcoded source groups. The
matrix is therefore current, but the visual reports can miss explicit sections
for the newest candidates until a manual builder patch is made during closure.

This document plans a tooling fix for future `Track 2` refreshes: visual
reports should discover current registry-model groups from the same matrix
configuration used by the official `Track 2` run, and the launcher should fail
early if visual coverage is incomplete.

## Technical Approach

The current `Track 2H` quantile/probabilistic refresh showed the failure mode:
`run_track2h_quantile_probabilistic_track2_verification_refresh.ps1` executed
the visual builders, but the builders were still organized around the previous
`Track 2H` robust-loss groups. The fix should remove that manual update point.

Implement three changes:

1. Add shared candidate-group extraction in the two visual builders so
   `registry_model_groups` entries from
   `full_track2_matrix_template.yaml` can become visual groups without adding
   a new Python constant and report-group block for every new wave.
2. Preserve the curated legacy sections, but append automatically generated
   source-specific groups for registry-model sources not already covered by
   explicit visual groups.
3. Add a launcher-level visual coverage check after collage and overlay
   generation. The check must compare the matrix-config `source_label` values
   against generated Markdown sections and fail the operator command if a new
   source was evaluated by the matrix but not exposed in the visual reports.

The intended result is that future launchers such as a mixture-density,
latent-state, or later multi-head `Track 2` refresh can run once: when the
operator command finishes, the visual reports either already contain the new
candidate groups or the launcher fails with a precise missing-source message
before closure.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
  builds the candidate collage report and currently contains explicit group
  construction for prior Track 2 branches.
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
  builds the overlay report and has the same hardcoded group-coverage issue.
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
  is the canonical source for matrix registry groups and their
  `source_label`, `candidate_id_prefix`, `global_family`, `fw_family`, and
  `bw_family` fields.
- `scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.ps1`
  is the concrete launcher where the issue was observed and should gain a
  generic coverage check that future launchers can copy or reuse.
- `doc/scripts/campaigns/track2/run_track2h_quantile_probabilistic_track2_verification_refresh.md`
  should document that visual coverage is validated during the operator run.

No subagent is planned for this implementation.

## Implementation Steps

1. Add reusable helper functions to both visual builders to read
   `registry_model_groups` from the matrix config and create registry-backed
   candidate configurations from `base_family_list`.
2. Mark explicit hand-curated report groups with their covered source labels,
   then generate fallback source-specific visual groups only for uncovered
   registry sources.
3. Keep report titles deterministic and readable, using normalized source-label
   names when a source has no custom title.
4. Add a lightweight visual-coverage validation script or builder option that
   checks generated collage and overlay Markdown for every active
   registry-model `source_label` requested by the matrix config.
5. Wire that validation into the Track 2H quantile/probabilistic launcher after
   visual-report generation and before PDF export.
6. Update the launcher note to state that a successful launcher run now means
   matrix, visual groups, and PDFs are mutually consistent.
7. Validate with Python compilation, targeted dry-run/coverage checks,
   Markdown QA on touched docs, and Sphinx if portal-scoped documents change.
