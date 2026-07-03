# Dataset-Aware Wave 5.2 And Wave 6 Documentation Rework

## Overview

This technical document plans a documentation-only rework of the TE modeling
roadmap after the decision to treat `simplified_dataset` and `polished_dataset`
as separate but related development surfaces.

The current `polished_dataset_full_wave_retraining_2026_06_22` campaign is
running on another workstation and must not be disturbed from this checkout.
The documentation rework will therefore avoid changing its manifest, launcher,
configuration, registries, closeout reports, or `TE Curve Verification
Pipeline` refresh artifacts. Those closeout and refresh tasks will be handled
on the other workstation after the campaign completes and artifacts are
synchronized.

The new roadmap should distinguish three branches:

- `polished_dataset` clean deployment branch for final comparability,
  curve-first promotion, and deployment-oriented model decisions;
- `simplified_dataset` noise-aware branch for stress-testing robust,
  structured, PINN-style, and multi-task mechanisms against the known dirty or
  disturbed surface;
- cross-dataset transfer branch for backbone pretraining, fine-tuning on
  `polished_dataset`, and reduced-point robustness studies.

No subagent is planned for this work. If a later review subagent is useful, its
name, task boundary, and approval requirement will be proposed before launch.

## Technical Approach

The approved documentation pass will update the canonical planning and status
surfaces so they no longer imply that `Wave 5.2` or `Wave 6` should continue
directly from the old `simplified_dataset`-centered `Wave 4` evidence without a
dataset-aware decision gate.

The rework will preserve existing historical evidence:

- `Wave 4.1` through `Wave 4.4` remain completed exploratory baselines on the
  prior development surface;
- `Wave 5.1` remains a completed harmonic-prior residual baseline;
- `polished_dataset` early-wave and `RCIM Model-Bank Reproduction` closeouts
  remain accepted normal campaign closeouts;
- the running full-wave polished campaign remains external and pending until
  the operator reports completion.

The revised roadmap will make `Wave 5.2` a dataset-aware MMT / PINN-guided
program rather than a single first-PINN campaign. The expected internal stages
are:

- `Wave 5.2A`: paired dataset diagnostics for `simplified_dataset` versus
  `polished_dataset`, including curve offsets, smoothness, harmonic content,
  removed or corrected points, and possible leakage boundaries;
- `Wave 5.2B`: clean `polished_dataset` MMT/PINN-guided feature or soft
  constraint path, only after polished retraining and curve verification expose
  remaining gaps;
- `Wave 5.2C`: dirty-to-clean or noise-aware multi-task path using lessons from
  the polishing workflow, without directly copying offline leakage into a
  deployable runtime model.

The revised `Wave 6` roadmap will become a later integrated multi-task /
multi-head and transfer-learning branch. It should wait for evidence from the
polished full-wave campaign, the dataset-pair diagnostics, and the
dataset-aware `Wave 5.2` stages.

## Involved Components

The documentation pass is expected to touch only repository-authored Markdown
status and planning surfaces:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`, only if the
  roadmap or active-family status summary needs wording alignment;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`,
  only if the dataset-role policy needs a short canonical pointer;
- `doc/README.md` or topic-local indices for any new canonical analysis note;
- this `doc/technical/2026-07/2026-07-01/` index.

Protected campaign files will not be edited:

- `config/training/polished_dataset_retraining/campaigns/2026-06-22_polished_full_wave_retraining/campaign.yaml`;
- `scripts/campaigns/cross_wave/run_polished_dataset_full_wave_retraining_campaign.ps1`;
- `doc/running/active_training_campaign.yaml`, unless the user explicitly asks
  to reconcile campaign state after the other workstation completes;
- campaign output registries, run artifacts, or closeout reports for the
  running full-wave polished campaign.

## Implementation Steps

1. Read the current dataset-family reference, live backlog, program closeout
   ledger, training master summary, and relevant polished campaign planning
   notes.
2. Reframe the backlog around three dataset-aware branches:
   `polished_dataset` clean deployment, `simplified_dataset` noise-aware
   research, and cross-dataset transfer / reduced-point robustness.
3. Update the program ledger so the next modeling decision no longer appears
   to be a simple choice between old `Wave 5.2` and `Wave 6`, but a staged
   dataset-aware planning gate.
4. Update the master summary only if needed to keep the executive snapshot and
   roadmap language aligned with the revised branch structure.
5. Add or update a concise canonical analysis note if the existing backlog and
   ledger cannot carry the new dataset-branch policy clearly.
6. Keep the active full-wave polished campaign untouched and explicitly
   document that its closeout and `TE Curve Verification Pipeline` refresh will
   be handled after completion on the other workstation.
7. Run repository Markdown QA on the touched Markdown scope:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py` with the
   touched file list.
8. Stop after the approved documentation rework and report the touched files,
   QA commands, and any deferred campaign-closeout or curve-verification work.
