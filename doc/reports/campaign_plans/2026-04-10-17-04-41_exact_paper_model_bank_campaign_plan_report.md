# Exact Paper Model Bank Campaign Plan Report

## Overview

This report defines the first repository-owned batch campaign for the strict
RCIM exact-paper branch.

The branch now exists in code, but the first real baseline attempt exposed two
practical issues:

- the ONNX export surface can fail on degenerate `SVR` targets under the
  current modern dependency stack;
- a single ad-hoc runner is not enough for reproducible operator-facing work in
  this repository.

This campaign is therefore not a generic hyperparameter sweep. It is a
stabilization and baseline-establishment campaign for the exact paper family
bank.

The campaign must answer three questions:

1. can the repository run the recovered full exact family bank end-to-end;
2. can it export an ONNX surface that remains operationally comparable to the
   recovered exact paper bank;
3. where exactly are the remaining export mismatches or family-specific
   failures, if any remain.

## Why This Campaign Makes Sense

The exact-paper branch is now the stricter `Track 1` reference branch.

That means the repository needs more than a successful script invocation. It
needs:

- repeatable batch execution;
- logged run boundaries;
- per-run validation summaries;
- explicit diagnostic/reference separation;
- a launcher path that matches the rest of the training program.

Because this branch is still stabilizing, the first campaign should remain
narrow and inspectable. It should not explode into a large sweep before the
baseline export surface is proven stable.

## Technical Context

This campaign is built around:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

Each run:

1. loads the recovered paper dataframe;
2. fits one exact-paper family bank or family subset;
3. evaluates family-level and target-level metrics;
4. exports one ONNX model per target when enabled;
5. compares the generated export surface against the recovered ONNX release;
6. writes a validation summary and Markdown report.

This is not a standard neural training campaign and should not be routed
through `scripts/training/run_training_campaign.py`.

## Technical Approach

The campaign should contain four runs.

### Run 1 - Full Exact Bank Diagnostic

Purpose:

- run the full recovered family set;
- keep ONNX export enabled;
- allow export failures to be captured and serialized rather than crashing the
  batch.

This run is the safest first global baseline because it gives full visibility
without losing the rest of the run to one converter failure.

### Run 2 - Full Exact Bank Strict Reference

Purpose:

- run the full recovered family set again;
- keep export strict;
- verify whether the new export safeguards are sufficient for a clean
  end-to-end exact-paper reference run.

This is the intended stable baseline if the diagnostic run shows no remaining
unexpected failures.

### Run 3 - SVR Export Diagnostic

Purpose:

- isolate the `SVR` branch that already produced the first observed ONNX crash;
- confirm the constant-surrogate export path behaves correctly;
- serialize a clean family-local diagnostic summary.

This run is targeted debugging, not the final paper benchmark.

### Run 4 - Non-SVR Export Reference

Purpose:

- run the exact bank without `SVR`;
- validate the rest of the export surface independently of the special-case
  `SVR` path;
- provide a clean comparison point if the `SVR` branch still needs more work.

This gives a stable fallback export reference for all other families.

## Candidate Run Matrix

| Config ID | Role | Planned Name | Enabled Families | Export Mode | Main Question |
| --- | --- | --- | --- | --- | --- |
| 1 | Full-bank diagnostic | `exact_full_bank_diagnostic_continue` | all `10` recovered families | `continue` | Does the full exact bank complete and serialize every remaining export problem clearly? |
| 2 | Full-bank strict reference | `exact_full_bank_strict_reference` | all `10` recovered families | `strict` | Is the repository now able to execute the strict paper-faithful baseline cleanly end-to-end? |
| 3 | SVR isolation | `exact_svr_export_diagnostic` | `SVR` only | `continue` | Does the degenerate-`SVR` export safeguard produce a stable target-wise export surface? |
| 4 | Non-SVR reference | `exact_non_svr_export_reference` | `MLP,RF,DT,ET,ERT,GBM,HGBM,XGBM,LGBM` | `strict` | Are the non-`SVR` families clean independently of the special `SVR` path? |

## Parameter Notes

### Export Failure Mode

The campaign uses two explicit export behaviors:

- `continue`
  diagnostic mode; export failures are recorded in the validation summary and
  report so the batch can still finish;
- `strict`
  reference mode; any remaining export failure still stops the run.

This split is necessary because the branch is still stabilizing.

### Empty-SVR Constant Surrogate

The campaign keeps the constant-surrogate safeguard enabled.

Its purpose is to handle recovered `SVR` targets that degenerate to constant
predictors with zero support vectors under the modern library stack. The
surrogate must remain functionally equivalent at inference time while restoring
exportability.

### Family Subsets

The exact-paper baseline is still the full recovered family bank. Family
subsets in this campaign are diagnostic tools only.

Promotion logic remains:

1. prove the full bank in diagnostic mode;
2. prove the full bank in strict mode;
3. use family-subset diagnostics only to isolate remaining faults, not to
   replace the exact baseline.

## Evaluation Rules

The campaign should inspect three output layers:

1. family-level component metrics;
2. target-wise winner registry;
3. export-surface status:
   - exported file count;
   - failed target count;
   - surrogate export count;
   - matched/missing/extra relative paths versus the recovered ONNX bank.

The winner of the campaign should not be interpreted as a new `Target A`
offline prediction winner. The first purpose here is exact-paper workflow
stability, not cross-family repository performance promotion.

## Operator Guide To Prepare

The implementation phase should provide:

1. the exact-paper campaign config package;
2. a dedicated PowerShell launcher;
3. a launcher note under `doc/scripts/campaigns/`;
4. logging to campaign-local `.log` files under the campaign output root;
5. the exact terminal command for operator-driven launch.

## Execution Gate

Before this campaign is launched:

1. the technical document must be approved;
2. this planning report must exist;
3. the campaign config package must exist;
4. the PowerShell launcher and launcher note must exist;
5. `doc/running/active_training_campaign.yaml` must be updated to `prepared`;
6. the user must explicitly start the prepared campaign.

## Next Step

After this planning report is written, generate the exact-paper campaign
package, launcher, launcher note, and prepared campaign state so the user can
launch the batch from PowerShell in the standard repository workflow.
