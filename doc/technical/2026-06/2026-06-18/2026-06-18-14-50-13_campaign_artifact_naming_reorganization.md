# Campaign Artifact Naming Reorganization

## Overview

The campaign-result and TE Curve Verification Pipeline artifact tree has accumulated inconsistent
filesystem names and experiment labels. The immediate symptoms are:

- both `doc/reports/campaign_results/track_2/campaign_closeouts/` and
  `doc/reports/campaign_results/track_2/verification_plots/` exist;
- top-level result folders mix compact names (`wave1`, `wave2`), spaced names
  (`track 2`), and combined names (`wave3_wave4`);
- model and campaign identifiers use opaque continuation labels such as
  `track2f`, `track2g`, `track2h`, `track2h_l`, and `track2h_m`;
- plot roots, final campaign reports, analysis reports, registries, launcher
  notes, and active-campaign history refer to different naming conventions.

The goal is to remove duplicate semantic roots, make the hierarchy predictable,
and preserve enough compatibility metadata that historical results remain
traceable after migration.

No subagent is planned for this reorganization. If a later audit needs a
subagent for broad reference discovery, that subagent must be named, scoped, and
approved explicitly before launch.

## Technical Approach

Use one canonical naming policy for filesystem paths, report titles, and model
identifiers:

- filesystem paths use lowercase snake_case slugs with numeric separators,
  such as `track_2`, `wave_1`, `wave_2`, `wave_3`, and `wave_4`;
- human-facing report titles use display names with spaces, such as `TE Curve Verification Pipeline`
  and `Wave 2.1`;
- historical compact spellings such as `track2`, `wave1`, and `wave3_wave4`
  are treated as legacy aliases, not future canonical names;
- literal filesystem spaces, such as `track 2`, are migrated away because they
  increase quoting burden and make cross-tool path handling more fragile;
- combined roots such as `wave3_wave4` are split unless an artifact truly spans
  both waves, in which case it moves under an explicit
  `cross_wave/wave_3_wave_4/` topic;
- alphabetic TE Curve Verification Pipeline experiment suffixes become explicit experiment-family
  names in paths and display titles.

The migration should be performed as an audited rename/update pass rather than
as manual folder cleanup. The implementation should produce and use a migration
manifest with old paths, new paths, artifact type, owning report or script, and
verification status.

## Involved Components

- `doc/reports/campaign_results/`
- `doc/reports/campaign_plans/`
- `doc/reports/analysis/`
- `doc/technical/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/`
- `scripts/reports/`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- `config/training/`
- `output/training_campaigns/`
- `output/validation_checks/`
- `output/registries/`
- `models/exported/`
- `site/` if affected documentation is in the Sphinx portal scope

## Implementation Steps

1. Build a read-only inventory of current Track, Wave, campaign-result, plot,
   registry, launcher, and report paths.
2. Classify every naming issue into one of these groups:
   duplicate semantic root, compact slug, literal-space slug, combined wave
   root, opaque experiment code, or historical reference that should stay as
   provenance text.
3. Define the approved canonical root layout. Initial proposed layout:
   `track_1/`, `track_2/`, `wave_1/`, `wave_2/`, `wave_3/`, `wave_4/`, and
   `cross_wave/`.
4. Define TE Curve Verification Pipeline experiment-family names that replace opaque suffixes in new
   paths while preserving old IDs in metadata. Initial examples:
   `offset_aware_probe`, `harmonic_offset_probe`, `curve_aware_training`,
   `dispersion_aware_robust_loss`, `probabilistic_quantile`,
   `mixture_density_heads`, and `latent_state_hysteresis`.
5. Generate a migration manifest before moving files. The manifest must include
   all affected Markdown links, YAML paths, script constants, report asset
   paths, PDF sidecars, and registry references.
6. Apply path migrations with a repository-owned script so the operation is
   repeatable and reviewable.
7. Update report generators and campaign closeout helpers so future outputs use
   the canonical layout automatically.
8. Update documentation indices and analysis references. Historical prose may
   mention old IDs, but active links and artifact roots should point to the
   canonical paths.
9. Run Markdown warning checks on touched Markdown files:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
10. Run targeted repository checks for broken links, missing expected artifacts,
    and stale references to deprecated roots.
11. If Sphinx-scoped documentation changes, rebuild the portal with
    `python -m sphinx -W -b html site site/_build/html`.
12. Stop after verification and report completion. Do not commit until the user
    gives explicit commit approval.
