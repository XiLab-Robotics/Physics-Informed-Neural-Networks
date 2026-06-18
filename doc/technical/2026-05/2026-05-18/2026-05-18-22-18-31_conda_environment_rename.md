# Conda Environment Rename

## Overview

This document plans the repository-wide rename of the local Conda environment
from `standard_ml_codex_env` to `pinns_env` and the LAN/remote Conda
environment from `standard_ml_lan_node` to `pinns_lan_env`.

The current search surface contains references across root setup instructions,
Sphinx getting-started pages, project guides, campaign launchers, LAN launcher
helpers, campaign preparation scripts, running campaign state, technical notes,
and script-level documentation. The first scoped inventory found `188` files
outside the largest generated/output directories containing at least one of the
old environment names.

## Technical Approach

Perform a controlled text and configuration alignment after approval:

- Replace command examples and defaults for local execution with `pinns_env`.
- Replace remote/LAN execution defaults and documented prerequisites with
  `pinns_lan_env`.
- Preserve existing override behavior while renaming the public environment
  variables from the `STANDARDML_` prefix to the `PINNS_` prefix, for example
  `STANDARDML_REMOTE_TRAINING_CONDA_ENV` to
  `PINNS_REMOTE_TRAINING_CONDA_ENV`.
- Review path literals that include Conda environment directories, for example
  `miniconda3\envs\standard_ml_codex_env\python.exe`, and update them to the
  new environment directory when they are current operational guidance.
- Re-run the repository search after edits to confirm no unintended references
  remain in the active implementation and documentation surface.

Historical technical documents and closed campaign reports will be treated
carefully. If a file is purely historical, the old names may be left only when
they describe past state and are not executable guidance. Any retained
historical occurrence must be intentional and easy to distinguish from current
commands.

## Involved Components

- `README.md`
- `doc/guide/project_usage_guide.md`
- `doc/guide/aries_cluster_user_guide.md`
- `site/getting_started/`
- `doc/scripts/`
- `doc/running/`
- `scripts/campaigns/`
- `scripts/paper_reimplementation/`
- Campaign preparation scripts that serialize
  `remote_conda_environment_name`
- Current and historical technical/campaign-planning documents containing
  executable Conda commands

The active campaign state lists protected files. Several target files are
protected, including `doc/running/active_training_campaign.yaml`,
`scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`,
`scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1`,
`scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1`,
`scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`, and
`doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`.

## Implementation Steps

1. Re-run a repository search for both old names with generated/output
   directories excluded and save the touched-file scope.
2. Issue a `CRITICAL WARNING` and obtain explicit approval before editing any
   protected campaign file from `doc/running/active_training_campaign.yaml`.
3. Update local Conda names from `standard_ml_codex_env` to `pinns_env` in
   active commands, launcher defaults, setup instructions, and current script
   notes.
4. Update LAN/remote Conda names from `standard_ml_lan_node` to
   `pinns_lan_env` in active remote launcher defaults, environment variable
   examples, campaign state, and LAN documentation.
5. Rename public override variables from `STANDARDML_*` to `PINNS_*` while
   preserving their current lookup and fallback semantics.
6. Review historical documents and leave old names only where they represent
   past facts rather than current commands.
7. Re-run `rg` to confirm the active surface no longer points users or scripts
   to the old environment names.
8. Run Markdown checks for every touched Markdown scope with:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
9. If Sphinx-scope files are changed, regenerate the portal with
   `python -m sphinx -W -b html site site/_build/html`.
10. Report completion and wait for explicit user approval before any Git
    commit.

No subagent use is planned for this change.
