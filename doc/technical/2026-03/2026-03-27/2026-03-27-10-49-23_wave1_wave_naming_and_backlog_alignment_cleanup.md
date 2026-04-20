# Wave1 Wave Naming And Backlog Alignment Cleanup

## Overview

The completed residual-harmonic family campaign originally used second-wave
style identifiers even though the live roadmap still reserves `Wave 2` for
temporal-model work.

That mismatch is now operationally misleading because:

- the campaign has finished, so the earlier reason for deferring cleanup is no
  longer valid;
- the live backlog should continue to treat residual-harmonic optimization as
  part of the `Wave 1` structured-baseline effort;
- repository-facing launcher names and guide references should not imply that
  temporal-model `Wave 2` work has already started.

This cleanup should preserve historical traceability for the completed campaign
artifacts while aligning the current repository surfaces with the intended wave
taxonomy.

## Technical Approach

The cleanup should separate historical artifact identity from current
repository-facing naming.

The recommended approach is:

1. preserve already-executed artifact identifiers when they are part of stored
   manifests, campaign outputs, or immutable run metadata;
2. update live backlog wording so `Wave 1` reflects the completed residual
   optimization pass and `Wave 2` remains reserved for temporal models;
3. introduce a canonical `Wave 1` residual launcher surface for future user
   references and align the campaign assets to the same naming;
4. correct technical/planning document framing so their narrative matches the
   intended roadmap, without erasing the historical fact that the original
   filenames were created before the mismatch was noticed;
5. update user-facing repository entry points so README and usage-guide wording
   no longer present the residual family pass as `Wave 2`.

This approach avoids breaking stored campaign manifests while still cleaning up
the repository guidance that future users will read and follow.

## Involved Components

- `doc/running/te_model_live_backlog.md`
  Live operational roadmap that must remain the authoritative wave-status view.
- `doc/running/active_training_campaign.yaml`
  Campaign-state record that may need wording notes while preserving historical
  artifact references.
- `doc/technical/2026-03/2026-03-26/2026-03-26-13-44-27_wave1_familywise_hyperparameter_optimization_campaign.md`
  Historical technical note whose framing should be aligned to `Wave 1`.
- `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
  Historical planning report whose wording should be aligned to `Wave 1`.
- `scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.ps1`
  Canonical launcher for the aligned residual-harmonic family campaign.
- `doc/scripts/campaigns/run_wave1_residual_harmonic_family_campaign.md`
  Canonical launcher note for the aligned residual-harmonic family campaign.
- `README.md`
  Main project landing page that should reference the canonical `Wave 1`
  framing.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that should reflect the corrected roadmap and
  launcher naming.

## Implementation Steps

1. Review the completed campaign state and confirm that the cleanup is no
   longer blocked by an active run.
2. Update the live backlog so the residual-harmonic family optimization is
   recorded inside `Wave 1`, while `Wave 2` remains reserved for temporal
   models.
3. Add the canonical `Wave 1` launcher surface and align the finished campaign
   artifacts to the same naming.
4. Align the narrative wording in the affected technical and planning documents
   without invalidating historical artifact references.
5. Update README and project-usage guidance so future repository users see the
   corrected wave taxonomy.
6. Only after this alignment pass, proceed with the final post-training results
   report for the completed residual-harmonic family campaign.
