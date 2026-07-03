# Analysis Report Directory Reorganization

## Overview

This technical document defines the approved structure and migration approach
for reorganizing `doc/reports/analysis/` into a smaller set of human-readable
containers. The current analysis tree mixes project status reports, analytical
TE modeling notes, model-development wave reports, validation setup reports,
and TE Curve Verification Pipeline artifacts at the same directory level.

The migration must preserve historical report provenance while making the
current repository documentation easier to browse. It must also update all
automatic path references in scripts, configuration files, repository-local
Codex skills, operational notes, and generated-report documentation that point
to the directories being renamed or moved.

No subagent is planned for this implementation. If a subagent becomes useful,
the proposed subagent name, reason, and bounded scope must be declared and
approved before launch.

## Technical Approach

The migration will be performed as a manifest-driven documentation
reorganization rather than a manual folder shuffle.

The target top-level structure under `doc/reports/analysis/` is:

- `project_status/`
- `te_modeling/`
- `model_development_waves/`
- `training_configuration/`
- `validation_checks/`
- `te_curve_verification_pipeline/`

The planned high-level moves are:

- Move `Repository Status Wave Track Synthesis.*`,
  `TE Program Status And Closeout Ledger.md`, and
  `Training Results Master Summary.md` into `project_status/current/`.
- Merge `mmt_te_modeling/` into `te_modeling/analytical_mmt/`.
- Keep the existing TE strategy and family material under clearer
  `te_modeling/strategy/`, `te_modeling/family_studies/`, and
  `te_modeling/analytical_studies/` subfolders.
- Move `training_analysis/` into `training_configuration/`.
- Move `wave1/`, `wave2/`, `wave3/`, `wave4/`, and `wave5_2/` into
  `model_development_waves/wave_1/`, `wave_2/`, `wave_3/`, `wave_4/`, and
  `wave_5_2/`.
- Rename the human-facing `track2/` report root to
  `te_curve_verification_pipeline/` and regroup its children by purpose:
  overview, official decisions, visual reports, CVP diagnostics, offset
  investigations, and reference or legacy material.
- Reorganize `validation_checks/` without deleting historical validation
  reports, separating infrastructure checks, RCIM Model-Bank Reproduction
  reports, TE Curve Verification Pipeline validation reports, model-development
  wave setup reports, and generated setup reports.

The path-reference audit must cover at least:

- `.codex/agents/`
- `.codex/skills/`
- `config/`
- `doc/`
- `doc/running/`
- `doc/scripts/`
- `scripts/`
- `site/`, excluding built Sphinx output

The initial read-only audit found path references in repository-local Codex
skill material, campaign launchers, report builders, training configuration
YAML files, persistent running-state notes, generated report documentation,
and canonical analysis reports. The implementation must update these references
after the file moves so future tools write to the new locations.

## Involved Components

Primary documentation roots:

- `doc/reports/analysis/`
- `doc/README.md`
- `doc/running/te_model_live_backlog.md`
- `doc/running/active_training_campaign.yaml`

Automation and workflow roots that require path-reference updates:

- `.codex/agents/`
- `.codex/skills/track2-verification-refresh/`
- `config/paper_reimplementation/`
- `config/training/`
- `scripts/campaigns/`
- `scripts/paper_reimplementation/`
- `scripts/reports/analysis/`
- `scripts/training/`
- `doc/scripts/`

The active campaign state currently reports `status: none` and has an empty
`protected_file_list`, so no active local campaign file is blocked by the
protected-file gate. The `next_prepared_campaign` entry remains historical
state and must not be altered except for documentation-path reference updates
that are part of this approved migration.

## Implementation Steps

1. Confirm approval of this technical document before moving any report,
   script, configuration, or workflow path.
2. Generate a complete move manifest for every affected path under
   `doc/reports/analysis/`.
3. Generate a complete reference manifest for every file containing old
   analysis-report paths.
4. Use `git mv` or equivalent Git-aware moves for tracked files and folders.
5. Update all references in Markdown, YAML, Python, PowerShell, Bash, TOML, and
   repository-local skill files that point to moved locations.
6. Add or update lightweight `README.md` index files where they materially
   improve human navigation of the reorganized roots.
7. Update `doc/README.md` to register the new technical document and the new
   canonical analysis-report locations.
8. Run targeted path-audit checks to confirm no stale old-root references remain
   outside deliberate historical notes.
9. Run repository-owned Markdown checks on the touched Markdown scope:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
10. Report the completed migration and wait for explicit approval before any
    Git commit.
