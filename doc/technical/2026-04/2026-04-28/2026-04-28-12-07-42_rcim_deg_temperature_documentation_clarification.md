# Overview

This technical document plans a documentation clarification for the recovered
RCIM exact-paper analysis notes.

The user clarified an important domain detail about the recovered prediction
CSV files under
`reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/` and,
by extension, the original pipeline code under
`reference/rcim_ml_compensation_recovered_assets/code/`:

- the dataframe column `deg` represents oil temperature;
- the filter `deg <= 35` therefore keeps only operating points whose oil
  temperature is at or below `35` degrees.

The current analysis notes already mention the existence of the `deg <= 35`
filter, but they may not state explicitly enough that this is a thermal filter
rather than an abstract operating-variable cut.

## Technical Approach

The change is documentation-only and should stay tightly scoped.

The main task is to inspect the current analysis documents that explain the
recovered original pipeline and the reimplementation, then make the thermal
meaning of `deg` explicit wherever the existing wording is ambiguous.

The intended update should:

1. clarify that `deg` in the recovered forward and backward prediction CSVs is
   oil temperature;
2. clarify that `deg <= 35` means the original runner keeps only rows from oil
   temperatures below or equal to `35` degrees;
3. avoid over-editing unrelated explanations or changing the previously agreed
   original-versus-reimplementation analysis scope;
4. keep the companion report and any closely related analysis notes aligned.

## Involved Components

Primary reference inputs:

- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Bw_v14_newFreq.csv`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/main_prediction_v17.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-main_prediction_v18.py`

Primary documentation targets to inspect:

- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`

Index target:

- `doc/README.md`

No subagent use is planned. If that changes, explicit user approval will be
requested before any launch.

## Implementation Steps

1. Inspect the current analysis reports for mentions of `deg`, `deg <= 35`,
   and operating-condition wording.
2. Identify whether the companion document alone needs clarification or
   whether the audit/workflow reports also need aligned wording.
3. Update the necessary Markdown files to state explicitly that `deg` is oil
   temperature and that `deg <= 35` is a thermal cutoff.
4. Keep the change narrow and preserve the rest of the established analysis.
5. Run scoped Markdown QA on the touched Markdown files.
6. Report completion and wait for explicit commit approval if the user wants
   the clarification committed.
