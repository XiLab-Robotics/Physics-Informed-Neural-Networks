# TE Curve Verification Pipeline Refresh Checklist

Use this checklist after a completed campaign is ready for official `TE Curve Verification Pipeline`
acceptance review.

## 1. Campaign And Registry State

Run:

```powershell
Get-Content -Path doc/running/active_training_campaign.yaml
git status --short
```

Confirm:

- active campaign status is `none` or the user has explicitly approved edits to
  protected files;
- completed campaign exposes `campaign_leaderboard.yaml`,
  `campaign_best_run.yaml`, and `campaign_best_run.md`;
- family registry files exist for every candidate surface under
  `output/registries/families/<family>/latest_family_best.yaml`.

## 2. Matrix Candidate Integration

Patch:

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`;
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  only if candidate generation or inference support must change.

For registry-backed candidates, preserve direction policy:

- `<family>_global`: `allowed_direction_list: ["forward", "backward"]`;
- `<family>_Fw`: `allowed_direction_list: ["forward"]`;
- `<family>_Bw`: `allowed_direction_list: ["backward"]`.

If a model expects sequence windows, build full-curve windows so the predicted
curve length matches the measured angular grid. Do not compare truncated
center-only outputs against full curves.

Prepare an operator-facing launcher for the matrix. The launcher must support a
local run and, when available for the repository workflow, a `-Remote` run. Do
not run the heavy matrix from Codex during preparation.

The local launcher command should wrap this matrix command:

```powershell
conda run -n pinns_env python -B scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml `
  --output-suffix <campaign_refresh_suffix> `
  --windows
```

Provide the exact local command and the exact `-Remote` command to the user,
then wait for the user to run the launcher and report completion. If the user
reports that the wrapper timed out but the child `pinns_env` Python process is
still using CPU, tell them to wait for that process instead of launching a
second matrix run.

## 3. Matrix Report Sanity Checks

Check:

```powershell
Select-String -LiteralPath "doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md" `
  -Pattern "candidate count|<new_family>|<expected_candidate>"
```

Confirm:

- candidate count increased by the expected number;
- candidate inventory includes new registry paths;
- direction tables show new candidate-source sections;
- global candidates appear in the global direction breakdown;
- strongest candidates can be read from the matrix, not inferred from run
  names.

## 4. Visual Companion Reports

Run:

```powershell
conda run -n pinns_env python -B scripts/reports/analysis/build_track2_best_model_collage_report.py `
  --report-date YYYY-MM-DD --windows

conda run -n pinns_env python -B scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py `
  --report-date YYYY-MM-DD --windows
```

Check the generated Markdown for the new candidate names and groups:

```powershell
Select-String -LiteralPath "<report.md>" -Pattern "<new_family>|Wave 2.1|Temporal"
```

If broad legacy plot PNGs were regenerated, restore unrelated churn:

```powershell
git restore -- "doc/reports/campaign_results/track 2"
```

Then add back only the new source-specific folder if it is a deliberate
deliverable.

## 5. Official Report Decision

Create or update:

`doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[YYYY-MM-DD]/track2_official_model_verification_report.md`

Record:

- matrix candidate count before and after refresh;
- strongest new candidate per direction/surface for raw error, shape fidelity,
  offset / continuity, harmonic / phase fidelity, robustness, and final
  recommendation when the required diagnostics exist;
- comparison to accepted `tree` and paper-derived baselines;
- final decision: promoted, rejected, or verified exploratory baseline;
- current matrix, collage, overlay, PDF, and validation paths.

Apply the canonical policy in:

`doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`

Do not promote or reject a candidate from scalar `MAE`, matrix MPE, or campaign
leaderboard rank alone.

Do not embed raw Markdown images in the official report unless the PDF exporter
is known to render them correctly. Prefer text pointers when the visual
evidence already lives in the companion PDFs.

## 6. PDF Export And Visual QA

Run:

```powershell
conda run -n pinns_env python -B scripts/reports/pdf/run_report_pipeline.py `
  --input-markdown-path "<collage-report.md>" `
  --input-markdown-path "<overlay-report.md>" `
  --input-markdown-path "<official-report.md>" `
  --clean-temp --windows
```

Review representative validation images with `view_image`:

- first page of the official report;
- page containing the update ledger;
- page containing final decision;
- one collage page with new candidates;
- one overlay page with new candidates.

Fix:

- clipped columns;
- raw Markdown image syntax;
- table overflow;
- unreadable identifiers;
- awkward section starts.

## 7. Status Documents

Update:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Use direct wording:

- campaign completed;
- TE Curve Verification refresh completed;
- strongest new candidates;
- baseline changed or unchanged;
- next operational branch.

## 8. Verification Commands

Run:

```powershell
python -m py_compile <modified-python-files>
conda run -n pinns_env python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning
conda run -n pinns_env python -B scripts/tooling/markdown/run_markdownlint.py
conda run -n pinns_env python -m sphinx -W -b html site site/_build/html
git diff --check
```

Before commit:

```powershell
git status --short
git diff --stat
git diff --cached --stat
git diff --cached --check
```

Check staged size:

```powershell
$total = 0
git diff --cached --name-only | ForEach-Object {
  if (Test-Path -LiteralPath $_ -PathType Leaf) {
    $total += (Get-Item -LiteralPath $_).Length
  }
}
[PSCustomObject]@{
  StagedSizeBytes = $total
  StagedSizeMB = [Math]::Round($total / 1MB, 2)
}
```
