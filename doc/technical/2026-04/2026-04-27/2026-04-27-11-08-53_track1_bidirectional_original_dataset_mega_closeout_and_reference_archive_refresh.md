# Track 1 Bidirectional Original-Dataset Mega Closeout And Reference Archive Refresh

## Overview

This technical document defines the closeout workflow for the completed
bidirectional original-dataset `Track 1` mega-campaign
`track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17`.

The requested closeout must do four things in one canonical pass:

1. verify and record the real completion state of the `400`-run mega-campaign;
2. publish the campaign closeout report and update the durable campaign state;
3. refresh the canonical `RCIM Paper Reference Benchmark` colored
   forward/backward tables with the results produced by this wave;
4. refresh the curated paper-reference model archives under
   `models/paper_reference/rcim_track1/` so the stored `forward` and
   `backward` family archives reflect the current best accepted canonical
   models from the new campaign.

The user also requested an explicit audit of whether the repository already
formalizes model-archive refresh as a mandatory closeout step. The current
repository does already contain that rule in the earlier `Track 1`
family-archive integration documentation, but this closeout must verify the
current wording and extend it if the new bidirectional original-dataset
workflow needs a stricter or clearer formulation.

No Codex subagent is planned for this work. If subagent use becomes desirable
later, it must be proposed explicitly and approved before launch.

## Technical Approach

The closeout will treat the finished mega-campaign as the canonical source of
truth for accepted exact-paper `Track 1` results across both directions.

The implementation should:

1. inspect the finished campaign outputs and validation summaries to determine
   completion, family-by-family outcomes, accepted best runs, and any residual
   failed or partial artifacts that must be excluded from promotion;
2. update `doc/running/active_training_campaign.yaml` from `running` to the
   appropriate completed state, with finish timestamp, results report path, and
   campaign completion metadata;
3. create a formal campaign-results closeout report under
   `doc/reports/campaign_results/track1/exact_paper/` that documents:
   - campaign scope;
   - completion status;
   - family winners for `forward` and `backward`;
   - benchmark-cell outcomes;
   - archive-promotion consequences;
4. refresh the canonical benchmark report
   `doc/reports/analysis/RCIM Paper Reference Benchmark.md` so the colored
   status tables and related summary text reflect the accepted results from
   this bidirectional wave rather than the previous restart baseline;
5. refresh the curated model archives under
   `models/paper_reference/rcim_track1/` by replacing older promoted
   family-target artifacts with the newly accepted better canonical models
   whenever this campaign improved the stored reference result;
6. ensure both `forward` and `backward` archive branches expose the expected
   `10 x 19` reference inventory, with updated provenance manifests and linked
   source-run snapshots;
7. verify whether the existing closeout-governance documents already state the
   model-archive refresh rule strongly enough, and if not, update the relevant
   repository-owned documentation so future closeouts must repeat this refresh
   behavior whenever a better canonical family result appears.

The archive refresh remains selective. A stored reference model should change
only when the new closeout produces a better accepted canonical result than
the currently archived family-target entry. Mere re-runs or ties must not
cause unnecessary archive churn.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-26-00-43-19_track1_bidirectional_original_dataset_mega_relaunch_after_micro_gate_plan_report.md`
- `doc/reports/campaign_results/track1/exact_paper/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/README.md`
- `models/paper_reference/rcim_track1/forward/`
- `models/paper_reference/rcim_track1/backward/`
- `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/track1_bidirectional_original_dataset_mega_campaign_2026-04-26_00_49_17/`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/`
- repository-owned exact-paper archive and closeout tooling under
  `scripts/paper_reimplementation/rcim_ml_compensation/` and `scripts/reports/`
- prior governance document
  `doc/technical/2026-04/2026-04-22/2026-04-22-17-51-21_track1_family_reference_archives_and_closeout_integration.md`

## Implementation Steps

1. Inspect the completed campaign outputs and validation artifacts to confirm
   the real end state, promoted best runs, and any exclusions required before
   benchmark or archive updates.
2. Update `doc/running/active_training_campaign.yaml` to a completed closeout
   state with finish metadata and backlink to the results report.
3. Create the bidirectional mega-campaign closeout report under
   `doc/reports/campaign_results/track1/exact_paper/`.
4. Refresh the `RCIM Paper Reference Benchmark` tables and any related status
   text so the forward/backward colored cells reflect this campaign's accepted
   outcomes.
5. Refresh the `models/paper_reference/rcim_track1/forward/` archives and
   populate or refresh the corresponding `backward/` archives so both
   directions expose the canonical `10 x 19` accepted target packages.
6. Audit the existing closeout-governance wording for model-archive refresh
   and strengthen the repository docs if the current rule is incomplete for
   the bidirectional original-dataset workflow.
7. Run Markdown QA on the touched Markdown scope and regenerate the Sphinx
   portal if the touched documentation falls inside the canonical portal scope.
