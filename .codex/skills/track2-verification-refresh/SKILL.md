---
name: track2-verification-refresh
description: Use after a completed StandardML training campaign must be accepted into the official Track 2 offline verification package. Covers campaign-state inspection, candidate addition to the directional matrix, registry-backed model evaluation, collage and overlay report regeneration, official Track 2 decision reporting, PDF validation, backlog/master-summary synchronization, and commit preflight for Track 2 refresh work.
---

# Track 2 Verification Refresh

## Purpose

Prepare and review the post-campaign `Track 2` verification workflow without
losing the decision discipline established during the Wave 2 temporal refresh.
This skill does not replace campaign planning, training execution, or normal
campaign closeout; use it after the campaign is complete and the user asks to
refresh official `Track 2` verification.

Do not run the heavy `Track 2` matrix inside Codex by default. The default
workflow is to prepare an operator-facing PowerShell launcher with local and
`-Remote` modes, provide the exact command, and wait for the user to run it and
report completion before inspecting the resulting artifacts.

## Coordinate Skills

Use these skills as needed during the workflow:

- `campaign-architect`: inspect completed campaign state and protected files.
- `pytorch-training-workflows`: adapt model loading or inference paths for new
  PyTorch candidate families.
- `styled-report-pdf-qa`: export and validate real PDFs.
- `markdown-report-qa`: run repository Markdown checks.
- `git-commit-preflight`: prepare the final commit after user approval.

Do not launch subagents silently. If subagent review would help, declare the
scope and wait for explicit user approval.

## Required Preflight

1. Read `doc/running/active_training_campaign.yaml`.
2. Confirm the campaign is completed or explicitly cleared before touching
   protected files.
3. Read the approved technical document or refresh plan for the campaign.
4. Confirm normal campaign closeout has already completed, or that the user has
   explicitly approved preparing `Track 2` before closeout.
5. Confirm the user approved an operator-launched `Track 2` run.
6. Identify the new candidate surfaces: `global`, `Fw`, `Bw`, or an explicitly
   approved exception.
7. Confirm the registry files exist under `output/registries/families/`.
8. Inspect current `Track 2` report-builder code before patching.

For the detailed command checklist, read
`references/track2-refresh-checklist.md`.

## Matrix Refresh

Add new candidates through the compact matrix config when possible:

`config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`

Keep direction semantics stable:

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

If the candidate model family needs a new inference shape, patch the shared
support code in:

`scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`

## Operator Launcher Gate

When `Track 2` is approved, create or update a dedicated launcher under
`scripts/campaigns/` or the existing campaign-specific tooling root. The
launcher must:

- run the matrix locally by default;
- expose a `-Remote` option when the repository remote-campaign conventions are
  available;
- write logs and output suffixes that make reruns distinguishable;
- avoid starting the matrix during preparation;
- be accompanied by a short launcher note under `doc/scripts/campaigns/` or the
  relevant `doc/scripts/` topic.

After providing the command, stop and wait until the user confirms that the
launcher completed.

Verify the canonical matrix report updates:

`doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Check that the candidate count changes as expected and that new source-group
sections are visible in the Markdown, not only in the YAML summary.

## Visual Reports

Regenerate both visual companion reports for a real `Track 2` acceptance
refresh:

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`

Expected deliverables are dated report bundles under:

- `doc/reports/analysis/track2/best_model_collage_report/[YYYY-MM-DD]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[YYYY-MM-DD]/`

Keep companion output artifacts under:

- `output/validation_checks/track2_best_model_collage_report/`
- `output/validation_checks/track2_multi_model_curve_comparison_report/`

When a full matrix run creates broad preview churn under
`doc/reports/campaign_results/track 2`, keep only the new candidate-source
folder that is part of the refresh. Restore unrelated regenerated legacy PNGs.

## Official Decision

Update or create the dated official report bundle:

`doc/reports/analysis/track2/official_model_verification_report/[YYYY-MM-DD]/`

The official report must state:

- which candidates were added;
- which candidate is strongest for `global`, `Fw`, and `Bw`;
- whether the new family is promoted, rejected, or kept as a verified
  exploratory baseline;
- whether the accepted `tree` or paper-derived baseline changes;
- where the matrix, collage, overlay, and validation artifacts live.

Do not infer promotion from campaign leaderboard metrics alone. Use the
direction-aware Track 2 matrix and the visual companion PDFs.

## Status Synchronization

After the report decision, update:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- any narrower topic index or report pointer that still references the prior
  dated official report.

Keep the wording concrete: include the decision, strongest candidates, and
whether the accepted baseline changed.

## Validation

Run the repository checks before calling the refresh complete:

```powershell
python -m py_compile <modified-python-files>
conda run -n pinns_env python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning
conda run -n pinns_env python -B scripts/tooling/markdown/run_markdownlint.py
conda run -n pinns_env python -m sphinx -W -b html site site/_build/html
```

Export and raster-validate the real PDFs with:

```powershell
conda run -n pinns_env python -B scripts/reports/pdf/run_report_pipeline.py `
  --input-markdown-path "<collage-report.md>" `
  --input-markdown-path "<overlay-report.md>" `
  --input-markdown-path "<official-report.md>" `
  --clean-temp --windows
```

Open representative validation images for the official report and visual PDFs.
Fix visible table overflow, raw Markdown image syntax, clipped content, or bad
page starts before finalizing.

## Commit Discipline

Do not commit until the user explicitly asks. Before the commit:

- inspect `git status --short` and `git diff --cached --stat`;
- stage only task-owned files;
- check staged files over `100 MB`;
- check aggregate staged size;
- run `git diff --cached --check`;
- use a commit title that states the verification refresh, not a generic report
  update.
