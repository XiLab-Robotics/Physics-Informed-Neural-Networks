# Overview

This technical document plans a structural reorganization of the RCIM
paper-reimplementation script surface, with special focus on the recovered
original workflow copies under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`.

The user clarified two important scope decisions:

1. the newly restored `instance_v4.py` and `instance_v5.py` files under
   `reference/rcim_ml_compensation_recovered_assets/code/` should now allow
   reconstruction of the full original workflow surface;
2. `main_prediction_v18.py` and its `ELMRegressor` branch should not be used
   as the canonical paper workflow, because that script represents a later
   attempt rather than the original paper path.

The repository-owned recovered-original workflow should therefore be rebuilt
around the `latest_snapshot/main_prediction_v17.py` generation while still
including the now-restored dataframe-creation and evaluation code in a clean
three-stage layout.

The target result is:

- one recovered-original workflow surface, not two competing top-level trees;
- three stage folders only:
  - `dataframe_creation/`
  - `training/`
  - `evaluation/`
- one high-detail README beside that workflow explaining:
  - stage order;
  - runnable entry points;
  - required inputs;
  - produced outputs;
  - how each stage maps to the copied original code.

The user also requested a broader cleanup of
`scripts/paper_reimplementation/rcim_ml_compensation/` so the whole subtree is
grouped into dedicated subfolders instead of leaving unrelated workflows flat
at one level.

## Technical Approach

The reorganization should separate two concerns cleanly.

First, the recovered-original workflow copy should become a single explicit
pipeline rooted in one canonical copied surface. That means:

- retire the current top-level split between `latest_snapshot/` and
  `original_pipeline/` inside the copied script tree;
- rebuild the copied workflow under stage-oriented folders:
  - `dataframe_creation/`
  - `training/`
  - `evaluation/`
- treat the `latest_snapshot` training branch as the canonical recovered paper
  training path because the user explicitly does not want the `v18` ELM branch
  to define the paper workflow;
- still reuse the restored original dataframe-creation and evaluation code as
  stage-specific copied assets where appropriate.

Second, the broader `rcim_ml_compensation` script subtree should be grouped by
workflow family so that each repository-owned branch has its own dedicated
folder instead of sharing one flat namespace. The likely target grouping is:

- `exact_paper_model_bank/`
- `original_dataset_exact_model_bank/`
- `harmonic_wise_comparison/`
- `reference_family_vs_feedforward/`
- `recovered_original_workflow/`

Each dedicated folder should own:

- its runnable entry script(s);
- its support modules;
- its README or usage note when the branch is substantial enough to justify
  one.

The recovered-original workflow root itself should then contain:

- the three stage folders;
- one repository-owned runner/wrapper layer if still needed;
- one detailed README;
- no stale generated artifacts or duplicate copied branches unless a specific
  stage needs them as intentional fixtures.

## Involved Components

Primary reference-code inputs:

- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/main_prediction_v17.py`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/predictorML_v7.py`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Bw_v14_newFreq.csv`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/0-dfCreation/0-main_createDFforPrediction.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/0-dfCreation/0-statistic.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/0-dfCreation/instance_v5.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/2-evaluation/2-main_evaluatePrediction_v4.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/2-evaluation/2-main_evaluateSignals.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/2-evaluation/instance_v4.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/2-evaluation/instance_v5.py`

Current repository-owned workflow surface to reorganize:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_reference_family_vs_feedforward_comparison.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward_support.py`

Documentation surfaces likely to update:

- `doc/README.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`

No subagent use is planned. If that changes, explicit user approval will be
requested before any launch.

## Implementation Steps

1. Inspect the restored reference-code surface and confirm which copied files
   should populate the three recovered-original stage folders.
2. Rebuild
   `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
   into exactly:
   - `dataframe_creation/`
   - `training/`
   - `evaluation/`
   plus one root README and any minimal repository-owned wrapper files still
   required.
3. Base the recovered-original training stage on the `latest_snapshot`
   `main_prediction_v17.py` branch, not on `1-main_prediction_v18.py`.
4. Remove stale duplicate copied trees, generated artifacts, and cache files
   from the reorganized recovered-original workflow root unless they are
   intentionally preserved inputs.
5. Reorganize the broader
   `scripts/paper_reimplementation/rcim_ml_compensation/` subtree into
   dedicated workflow subfolders and update imports/entry points accordingly.
6. Write a high-detail README for the recovered-original workflow that explains
   the code structure, stage order, runnable commands, inputs, outputs, and
   code-level role of each main file.
7. Update companion documentation and script notes so the new structure is
   discoverable from canonical documentation entry points.
8. Run scoped validation:
   - import/entry-point checks for moved scripts;
   - smoke execution where feasible;
   - Markdown QA for touched repository-owned Markdown files.
9. Report completion and wait for explicit commit approval before creating any
   Git commit.
