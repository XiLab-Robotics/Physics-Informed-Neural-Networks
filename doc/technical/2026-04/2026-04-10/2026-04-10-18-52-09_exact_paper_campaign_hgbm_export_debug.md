# Overview

This technical document defines the immediate debug pass for the failed strict
RCIM exact-paper campaign run.

The prepared campaign `exact_paper_model_bank_campaign_2026_04_10_17_04_41`
was started by the operator on `2026-04-10`, but it stopped during
`02_exact_full_bank_strict_reference.yaml` with a strict ONNX export failure:

- family: `HGBM`
- target: `fft_y_Fw_filtered_ampl_0`
- failing surface:
  `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

The campaign is therefore no longer blocked by the earlier `SVR` issue only.
The strict full-bank run now exposes at least one additional modern export
compatibility problem in the tree-boosting branch.

The goal of this pass is to reproduce the failure under controlled conditions,
identify the exact converter incompatibility, implement the narrowest safe fix,
and restore a runnable exact-paper campaign path.

## Technical Approach

The debug sequence should stay staged and inspectable.

1. Confirm the persisted active campaign state and inspect the failing log plus
   the partially generated strict-run artifact directory.
2. Reproduce the failure outside the full four-run launcher by running the
   exact failing strict config directly, so the converter stack can be debugged
   without campaign noise.
3. Inspect the `HGBM` fitted estimator and the export path used for
   `fft_y_Fw_filtered_ampl_0` to determine whether the issue is caused by:
   - unsupported estimator shape or metadata;
   - unsupported dtype or array layout;
   - a version-sensitive `sklearn` or `skl2onnx` converter assumption;
   - a repository-side serialization path that differs from what the converter
     expects.
4. Use Context7 to verify current library expectations for the affected ML
   export stack before changing any library-specific code.
5. Implement the narrowest safe fix in the exact-paper support layer:
   - either a family-specific export adaptation for `HGBM`;
   - or a stricter diagnostic/fallback branch if full faithful export is not
     currently possible under the repository dependency stack.
6. Re-run the isolated strict config locally to verify whether the failure is
   removed.
7. Re-run the canonical campaign launcher only after the isolated strict path
   is stable again.

Local reproduction should be attempted first because the failure happens during
converter logic, not during long numerical training. If the debug cycle turns
out to be too slow or memory-heavy on the local workstation, the same prepared
campaign can later be re-routed through the repository LAN-remote workflow on
the stronger machine.

No Codex subagent use is planned for this implementation. If subagent help
later becomes useful for isolated code review or verification, a separate
runtime approval request will be raised before launch.

## Involved Components

Active campaign state and operator-facing execution surface:

- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_model_bank_campaign.ps1`
- `output/training_campaigns/track1/exact_paper/exact_paper_model_bank_campaign_2026_04_10_17_04_41/logs/02_exact_full_bank_strict_reference.log`

Primary implementation surface expected to be inspected or modified:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-10_exact_paper_model_bank_campaign/02_exact_full_bank_strict_reference.yaml`

Reference and project context that should remain in scope:

- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`

Potential follow-up workflow surface if local debug proves insufficient:

- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- repository LAN-remote campaign tooling already used for stronger-machine
  execution

## Implementation Steps

1. Inspect the failing campaign log and strict-run artifacts to confirm the
   exact failing family-target export context.
2. Reproduce the strict failing config directly from the repository root.
3. Inspect the exact-paper support export path for `HGBM` and identify the
   incompatible converter call.
4. Check the relevant library behavior with Context7 before changing
   `scikit-learn` or `skl2onnx`-specific code.
5. Implement the narrowest safe repository-side fix.
6. Re-run the isolated strict validation config.
7. Re-run the canonical campaign launcher to confirm end-to-end recovery or to
   identify the next blocker with cleaner evidence.
8. Update campaign state, reports, and usage notes only after the debug result
   is confirmed.
