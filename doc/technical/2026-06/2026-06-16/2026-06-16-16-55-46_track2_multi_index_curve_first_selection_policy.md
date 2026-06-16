# Track 2 Multi-Index Curve-First Selection Policy

## Overview

This technical document defines the repository change needed to shift `Track 2`
model evaluation from a primarily pointwise `MAE` / scalar-error ranking toward
a curve-first, multi-index selection policy. The change is documentation-first:
all `Track 2` reporting rules, official verification wording, closeout guidance,
and model-selection summaries must consistently state that curve reconstruction
quality is judged by several complementary indices, not by point-to-point error
alone.

The second phase will rerank all candidates included in the official `Track 2`
reports, spanning `Wave 1`, `Wave 2`, `Track 2B` through `Track 2H`, and
`Wave 3`. The reranking should produce readable tables that separate raw
operational error, mean-centered shape tracking, offset behavior, harmonic /
phase fidelity, robustness, and final recommendation status.

## Technical Approach

The policy update will preserve scalar `MAE`, `RMSE`, and percentage-error
metrics as required operational indicators, but it will demote them from the
single dominant selection rule. The official `Track 2` selection surface will
instead expose parallel winners:

- best raw-error candidate;
- best mean-centered shape candidate;
- best harmonic / phase fidelity candidate;
- best offset / continuity candidate;
- best robust worst-case candidate;
- recommended candidate per `global`, `Fw`, and `Bw` surface.

The documentation will define a normalized multi-index ranking policy. Metrics
with different physical units must not be combined directly without scaling.
The preferred implementation should normalize each metric across the evaluated
candidate set, use stable rank or percentile scores, and then compute a
transparent composite score. Any recommended best model must also pass veto
checks for extreme raw error, unstable worst-case behavior, invalid direction
scope, missing visual evidence, or deployment-incompatible inference paths.

The initial documentation pass will update the canonical policy locations
without executing training or rerunning the heavy `Track 2` matrix. The later
reranking pass will reuse existing `Track 2` matrix outputs, curve payload
diagnostics, mean-centered diagnostics, offset audits, and visual reports where
available, and will identify any missing payload exports needed to score all
registered candidates consistently.

No subagent is planned for this implementation. If later review would benefit
from a separate auditor for generated ranking tables or PDF validation, that
subagent scope must be proposed separately and explicitly approved before use.

## Involved Components

- `AGENTS.md`
  - Add the repository-level rule that official `Track 2` decisions must use
    multi-index curve-first selection rather than scalar `MAE` alone.
- `doc/README.md`
  - Register this technical document and any new canonical policy/report
    documents created by the implementation.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - Clarify that the directional matrix is a raw-error source table, not the
    complete promotion criterion.
- `doc/reports/analysis/track2/Track 2 Curve Reconstruction And Collage Pipeline.md`
  - Promote visual and mean-centered curve reconstruction checks to required
    evidence for official selection.
- `doc/reports/analysis/track2/curve_first_reranking_report/`
  - Treat the existing reranking report family as the bridge from scalar matrix
    metrics to multi-index selection.
- `doc/reports/analysis/track2/curve_payload_diagnostics_report/`
  - Treat payload diagnostics as the source for harmonic, phase, derivative,
    closure, and amplitude fidelity indices.
- `doc/reports/analysis/track2/mean_centered_collage_report/`
  - Treat mean-centered diagnostics as the source for offset-separated shape
    fidelity evidence.
- `doc/reports/analysis/TE Program Status And Closeout Ledger.md`
  - Record the policy shift and state that future closeouts must report
    multi-index Track 2 status when verification is refreshed.
- `doc/running/te_model_live_backlog.md`
  - Add the documentation-first and reranking follow-up tasks if they are not
    already represented.
- `scripts/reports/analysis/`
  - Later implementation may extend existing report builders or add a dedicated
    multi-index selection builder after the documentation policy is approved.

## Implementation Steps

1. Update canonical documentation rules so every future `Track 2` report and
   closeout distinguishes scalar accuracy from curve-shape fidelity.
2. Add a concise policy section defining the official multi-index selection
   axes, recommended weights or rank-normalized scoring, and veto conditions.
3. Update `Track 2` analysis-report references so prior MAE/MPE tables are
   framed as raw-error evidence rather than complete model-promotion decisions.
4. Register the new policy document and this technical document in `doc/README.md`.
5. Run Markdown QA on every touched Markdown file.
6. After approval of the policy update, inspect existing `Track 2B`, `Track 2C`,
   `Track 2D`, `Track 2E`, `Track 2G`, `Track 2H`, `Wave 1`, `Wave 2`, and
   `Wave 3` artifacts to build the candidate coverage map for complete
   reranking.
7. Prepare or update a multi-index reranking builder that outputs one table per
   surface and one table per selection axis.
8. Generate the complete reranking artifacts and report, then validate the
   resulting Markdown and PDF before proposing any model-promotion conclusion.
