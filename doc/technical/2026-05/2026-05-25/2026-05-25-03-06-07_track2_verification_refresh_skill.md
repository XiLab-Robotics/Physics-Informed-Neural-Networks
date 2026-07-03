# TE Curve Verification Pipeline Verification Refresh Skill

## Overview

Create a repository-local Codex skill that captures the operational workflow
used after a completed campaign must be accepted into the official `TE Curve Verification Pipeline`
verification surface. The skill will guide future agents through the same
closeout-to-refresh path used for the `Wave 2.1` temporal-model campaign:
inspect campaign state, add candidates to the directional matrix, regenerate
visual companion reports, update the official report, validate PDFs, update
status documents, and prepare commit-safe artifacts.

The proposed skill name is `track2-verification-refresh`, stored under:

`C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\.codex\skills\track2-verification-refresh`

## Technical Approach

The skill will be concise and procedural. It will not duplicate full report
contents or campaign results. Instead it will preserve the reusable workflow,
canonical file paths, verification commands, decision rules, and common
failure points discovered during the Wave 2.1 refresh.

The skill will include:

- a required `SKILL.md` with trigger description and step-by-step workflow;
- a small `references/track2-refresh-checklist.md` file for the detailed
  artifact checklist and command sequence;
- optional `agents/openai.yaml` metadata if generated cleanly from the
  repository's skill tooling pattern.

The skill will intentionally avoid broad scripts unless a future refresh shows
that the workflow should be automated. For now, the fragile parts are mostly
coordination, evidence review, and report QA, so prose plus a checklist is the
right level of control.

## Involved Components

- `.codex/skills/track2-verification-refresh/SKILL.md`
- `.codex/skills/track2-verification-refresh/references/track2-refresh-checklist.md`
- `doc/README.md`
- existing related skills:
  - `campaign-architect`
  - `pytorch-training-workflows`
  - `styled-report-pdf-qa`
  - `markdown-report-qa`
  - `git-commit-preflight`
- canonical curve-verification artifacts:
  - `doc/running/active_training_campaign.yaml`
  - `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`
  - `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/`
  - `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/`
  - `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/`
  - `doc/running/te_model_live_backlog.md`
  - `doc/reports/analysis/project_status/current/Training Results Master Summary.md`

## Implementation Steps

1. Create `.codex/skills/track2-verification-refresh/`.
2. Write `SKILL.md` with:
   - trigger scope for post-campaign `TE Curve Verification Pipeline` verification refresh work;
   - required preflight checks;
   - candidate/matrix refresh expectations;
   - visual report regeneration expectations;
   - official report decision rules;
   - QA and commit-preflight requirements.
3. Add `references/track2-refresh-checklist.md` with the reusable checklist
   and known commands from the Wave 2.1 refresh.
4. Validate the skill folder with the system `quick_validate.py` helper if
   available; otherwise validate frontmatter and paths manually.
5. Run Markdown QA on the touched repository Markdown files.
6. Report completion and wait for separate commit approval if the user wants
   the skill committed.
