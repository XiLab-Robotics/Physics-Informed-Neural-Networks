# Track 1 Bidirectional Mega Launcher YAML Compatibility Fix

## Overview

The current launcher
`scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
fails at startup on the local workstation because it reads
`doc/running/active_training_campaign.yaml` through `ConvertFrom-Yaml`, and
that cmdlet is not available in the active PowerShell environment.

The immediate goal is to repair the launcher without changing the prepared
campaign package semantics, so the user can start the already prepared
bidirectional mega-campaign safely.

## Technical Approach

Replace the launcher-side YAML loading step with a repository-controlled,
environment-stable path that does not depend on optional PowerShell YAML
cmdlets.

The preferred repair is:

- keep the PowerShell launcher as the user-facing entry point;
- delegate YAML parsing to Python inside the already required Conda
  environment;
- read only `queue_config_path_list` from the active campaign state;
- preserve the existing sequential execution logic and failure behavior.

This keeps the launcher compatible across Windows PowerShell variants while
reusing the same Python environment already needed for the training runner.

## Involved Components

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- `doc/guide/project_usage_guide.md`
- `site/` documentation only if the user-facing launcher behavior description
  changes materially

## Implementation Steps

1. Patch the PowerShell launcher so it resolves the active campaign YAML
   through Python instead of `ConvertFrom-Yaml`.
2. Keep the returned config-path list identical to the prepared campaign state.
3. Update the launcher note if the implementation detail shown to the user has
   changed materially.
4. Run a narrow smoke launch check on the launcher startup path.
5. Run Markdown QA on touched documentation and rebuild Sphinx if portal-facing
   docs changed.
