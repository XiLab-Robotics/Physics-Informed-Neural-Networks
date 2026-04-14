# Track 1 Paper Tables 2 6 Canonical Dashboard

## Overview

This technical document defines the requested documentation upgrade for the
paper-facing `Track 1` reporting surface.

The user requested one canonical document that:

- includes the paper tables `2`, `3`, `4`, `5`, and `6`;
- shows the original paper table content in repository-owned form;
- shows one analogous repository table for the current `Track 1` state;
- highlights each repository cell with a traffic-light status:
  - `green` -> paper target reached;
  - `yellow` -> nearly reached or still acceptable for follow-up;
  - `red` -> not reached;
- stays updated after every future `Track 1` progress step until full closure.

The most appropriate canonical home is
`doc/reports/analysis/RCIM Paper Reference Benchmark.md`, because that file is
already the repository-owned entry point for the paper baseline, the current
paper-vs-repository verdict, and the explicit `Track 1` / `Track 2` separation.

This task is documentation and reporting work only. It does not, by itself,
change the exact-paper training workflow or launch any new campaign.

Subagent usage is not planned for this task. No Codex subagent should be
launched unless a later runtime blocker appears and explicit user approval is
requested again at that time.

## Technical Approach

The repository already contains most of the required evidence, but it is split
across multiple surfaces:

- the paper benchmark entry point;
- the canonical exact-paper validation reports for Tables `3-6`;
- the latest campaign-results report;
- the per-run `validation_summary.yaml` files.

The requested improvement is therefore primarily a canonicalization and
presentation task rather than a new evaluation-method task.

The implementation should keep one source-of-truth flow:

1. treat `RCIM Paper Reference Benchmark.md` as the canonical dashboard for
   paper-side status tracking;
2. add one dedicated section for paper Tables `2-6`;
3. for each paper table:
   - restate the paper-side table in repository-owned Markdown form;
   - add one analogous repository table aligned to the same harmonics,
     families, and metrics where applicable;
   - add one explicit status row or status column that uses repository-owned
     color markers for `green`, `yellow`, and `red`;
4. define a stable meaning for each color so future updates remain
   comparable and do not drift semantically;
5. wire the surrounding wording so future `Track 1` progress updates are
   expected to refresh this dashboard after every material exact-paper
   improvement.

Recommended canonical scope by table:

- Table `2`: paper harmonic/model selection context and repository-side
  counterpart selection view;
- Table `3`: amplitude `RMSE` paper values vs repository best values;
- Table `4`: phase `MAE` paper values vs repository best values;
- Table `5`: phase `RMSE` paper values vs repository best values;
- Table `6`: paper selected family summary vs repository harmonic closure
  status.

Recommended status policy:

- `green`: the repository metric is at or better than the paper target for the
  corresponding cell;
- `yellow`: the cell is not closed yet, but the remaining gap is small enough
  to count as near-target or follow-up acceptable;
- `red`: the remaining gap is still materially open.

Because Markdown does not render native cell background colors reliably across
all repository surfaces, the first implementation should use explicit inline
status markers that remain readable everywhere, for example:

- `GREEN`
- `YELLOW`
- `RED`

If the current report renderer already supports safe inline HTML or styled
badge spans without introducing Markdown warnings, the implementation may
upgrade those markers into visually colored badges. If that path is chosen, it
must still remain readable in plain Markdown views and must not introduce a
warning regression.

The current exact thresholds for `yellow` should be defined explicitly during
implementation. They should be metric-aware and conservative rather than
cosmetic. If the evidence is not strong enough for a robust numeric rule, the
initial implementation should document a simple, inspectable fallback rule such
as `small positive gap only`, instead of inventing arbitrary optimism.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/validation_checks/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`
- `doc/reports/analysis/validation_checks/2026-04-13-22-09-00_paper_reimplementation_rcim_exact_model_bank_exact_open_cell_paper_family_reference_campaign_run_exact_paper_model_bank_report.md`
- `doc/reports/campaign_results/2026-04-13-22-55-28_track1_exact_paper_open_cell_repair_campaign_results_report.md`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-13-22-08-40__exact_open_cell_paper_family_reference_campaign_run/validation_summary.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `doc/README.md`

## Implementation Steps

1. Inspect the paper content for Tables `2-6` and confirm the repository-owned
   mapping needed to restate them accurately.
2. Add one dedicated `Tables 2-6` section to
   `doc/reports/analysis/RCIM Paper Reference Benchmark.md`.
3. For each table, add the paper-side Markdown reconstruction and the aligned
   repository-side comparison table.
4. Define and document the exact `green / yellow / red` rule so future updates
   remain deterministic.
5. Seed the new dashboard with the latest canonical `Track 1` state from the
   best current exact-paper run and the latest campaign closeout.
6. Update any adjacent canonical summary wording that points readers to the old
   split surfaces so the new dashboard becomes the first place to inspect.
7. Keep the per-run detailed validation reports as supporting evidence, but
   make the benchmark dashboard the maintained colleague-facing surface.
8. Run Markdown warning checks on the touched Markdown files and confirm clean
   trailing newline state before closing the task.

Implementation must not begin until the user explicitly approves this
technical document, per repository policy.
