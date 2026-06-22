# Canonical Wave Model Family Renaming

## Overview

This technical document defines the next repository renaming pass for the TE
model-development line after the broader `Track 2` to `TE Curve Verification
Pipeline` taxonomy migration.

The current repository state already uses the new wave taxonomy in many report
headings, but several model-family identifiers, registry identifiers, report
sections, and collage asset paths still expose historical development labels
such as `track2f`, `track2g`, `track2h`, and `wave3_harmonic_prior_residual`.
Those identifiers are now misleading because `Track 2` is the verification
pipeline, not the model-development namespace.

The implementation will establish canonical future names for the affected model
families, define one stable ordering rule for future comparison reports, and
refresh the current TE Curve Verification Pipeline reports without rewriting
completed training artifacts as if they had originally used the new names.

## Technical Approach

The repair will use a controlled compatibility boundary.

Historical artifacts remain traceable:

- completed training run folders;
- completed campaign manifests;
- completed validation-check folders;
- checkpoint references;
- dated report bundles that record an executed historical run;
- technical documents whose purpose is to describe the historical work as it
  happened.

Current and future-facing surfaces will move to canonical names:

- report display names;
- report section headings;
- current/canonical report bundles;
- report generators and ordering logic;
- future training campaign configs;
- future `run_name`, `model_family`, and `campaign_config_id` values;
- future registry group names;
- backlog, ledger, and master-summary descriptions that describe the current
  program state rather than historical filenames.

Where a current report references historical evidence, it should expose both
the canonical display name and the legacy candidate id when useful. This avoids
breaking reproducibility while making the reader-facing taxonomy consistent.

### Canonical Model-Family Mapping

| Legacy identifier | Canonical future identifier |
| --- | --- |
| `track2f_bis_clean_sequential_residual_offset` | `wave3_2_clean_sequential_residual_offset` |
| `track2f_bis_harmonic_residual_offset` | `wave3_2_harmonic_residual_offset` |
| `track2g_curve_aware_pointwise_control` | `wave3_3_curve_aware_pointwise_control` |
| `track2g_curve_aware_raw_centered_shape` | `wave3_3_raw_centered_shape_curve_aware` |
| `track2g_curve_aware_raw_offset` | `wave3_3_raw_offset_curve_aware` |
| `track2g_curve_aware_full_curve_composite` | `wave3_3_full_curve_composite` |
| `track2h_mae_robust` | `wave4_1_mae_robust_loss` |
| `track2h_smooth_l1_robust` | `wave4_1_smooth_l1_robust_loss` |
| `track2h_log_cosh_robust` | `wave4_1_log_cosh_robust_loss` |
| `track2h_quantile_p10_p50_p90` | `wave4_2_quantile_p10_p50_p90` |
| `track2h_gaussian_nll` | `wave4_2_gaussian_nll` |
| `track2h_mdn_k2` | `wave4_3_mixture_density_k2` |
| `track2h_mdn_k3` | `wave4_3_mixture_density_k3` |
| `track2h_l_gru_offset_residual` | `wave4_4_gru_latent_offset_residual` |
| `track2h_l_causal_tcn_offset_residual` | `wave4_4_causal_tcn_latent_offset_residual` |
| `wave3_harmonic_prior_residual_pointwise_control` | `wave5_1_harmonic_prior_pointwise_control` |
| `wave3_harmonic_prior_residual_smooth_l1_structured` | `wave5_1_harmonic_prior_smooth_l1_structured` |

Future candidate ids will use lowercase surface suffixes:

- `_fw`;
- `_bw`;
- `_global`.

Example: `wave4_3_mixture_density_k2_fw`.

### Canonical Report Ordering

Future TE Curve Verification Pipeline comparison reports will group rows and
collage sections by model family progression first, then by surface:

1. `Forward Reference`;
2. `Backward Reference`;
3. `Global Reference`;
4. `Forward Wave 1`;
5. `Backward Wave 1`;
6. `Global Wave 1`;
7. `Forward Wave 2.1`;
8. `Backward Wave 2.1`;
9. `Global Wave 2.1`;
10. continue with `Forward`, `Backward`, and `Global` for each subsequent wave.

This keeps each wave readable as one model-development block while preserving
surface-level comparison inside the block.

## Involved Components

The implementation will inspect and update the following component classes:

- `doc/reports/analysis/track2/best_model_collage_report/` report source,
  generated PDF, and generated assets when the current report is refreshed;
- `doc/reports/analysis/track2/official_model_verification_report/` current
  report source and PDF where it exposes future-facing candidate names;
- TE Curve Verification Pipeline report-generation scripts and sorting helpers
  under `scripts/`;
- future campaign configs under `config/training/` for the affected model
  families, without mutating completed run evidence as if it had been produced
  under new ids;
- documentation indices and current-state documents under `doc/`, especially
  the backlog, program ledger, training master summary, and report index;
- PDF export tooling under `scripts/reports/pdf/` only if the renamed report
  tables or section headings need layout tuning.

The active campaign state is currently `status: none`, so no protected active
campaign files are expected. If that changes before implementation, the
protected-file list in `doc/running/active_training_campaign.yaml` must be
checked again before editing campaign-related files.

## Implementation Steps

1. Audit the current best-model collage report, official verification report,
   report-generation scripts, future campaign configs, registries, and
   current-state documentation for `track2f`, `track2g`, `track2h`, and
   inconsistent `wave3_harmonic_prior_residual` reader-facing usages.
2. Add a repository-owned mapping layer for canonical model-family display
   names and future candidate ids, preserving legacy ids where they identify
   historical artifacts.
3. Update report-generation ordering so TE Curve Verification Pipeline reports
   sort as `Reference Fw/Bw/global`, then each wave with `Fw/Bw/global`.
4. Refresh the current best-model collage report so candidate tables and
   collage headings use canonical display names and, where necessary, legacy
   ids in a separate column or annotation.
5. Refresh the current official verification report if its reader-facing
   sections still present historical development labels as current model-family
   names.
6. Update future-facing campaign/config templates and current-state
   documentation so new retraining work uses canonical ids such as
   `wave4_3_mixture_density_k2_fw`, not `track2h_mdn_k2_Fw`.
7. Regenerate the affected Markdown/PDF report outputs with repository-owned
   report tooling.
8. Validate the real exported PDFs by rasterizing pages and visually checking
   ordering, table fit, heading hierarchy, clipped borders, and identifier
   readability.
9. Run repository Markdown checks on the touched authored Markdown scope.
10. Run `git diff --check` and focused residue scans for the affected legacy
    identifiers, separating intentional historical references from unresolved
    future-facing residues.
11. Stop and report completion before any commit, per the final approval gate.
