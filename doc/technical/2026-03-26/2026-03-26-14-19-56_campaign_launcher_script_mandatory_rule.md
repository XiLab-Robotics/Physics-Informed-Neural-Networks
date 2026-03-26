# Campaign Launcher Script Mandatory Rule

## Overview

The current campaign-preparation workflow already requires:

- a technical document;
- a planning report;
- generated campaign YAML files;
- persistent campaign state in `doc/running/active_training_campaign.yaml`;
- the exact terminal command needed to launch the campaign.

The user requested one more mandatory deliverable for every prepared campaign:

- a dedicated PowerShell launcher script that can be run directly instead of
  manually pasting a very long `python scripts/training/run_training_campaign.py ...`
  command.

The user also requested that this launcher requirement become a permanent
repository rule rather than a one-off convenience for the current `Wave 2`
residual campaign.

## Technical Approach

The launcher requirement should become part of the standard campaign-preparation
bundle.

For every approved training campaign preparation, the repository should now
produce all of the following:

1. campaign YAML files;
2. persistent prepared-campaign state;
3. exact launch command;
4. dedicated launcher script under `scripts/campaigns/`;
5. launcher usage note under `doc/scripts/campaigns/`.

### Launcher Script Role

The PowerShell launcher should be a thin wrapper around the canonical campaign
runner.

Its role should be:

1. resolve the repository root;
2. optionally clear stale queue entries related to the same campaign when that
   cleanup is safe and intentional;
3. assemble the approved YAML path list in a stable order;
4. forward that list to `scripts/training/run_training_campaign.py`;
5. preserve the same live terminal behavior, per-run logs, and campaign
   artifacts as the underlying runner.

The launcher should not replace the canonical command. It should standardize it
and make campaign execution less error-prone.

### Documentation Requirement

Each launcher should have a matching repository-owned usage note in:

- `doc/scripts/campaigns/`

That note should describe:

- what the launcher is for;
- what campaign it wraps;
- the default command to run it;
- any optional arguments such as `-PythonExecutable`.

### Permanent Rule Update

The repository instructions should be tightened so future campaign preparation
is incomplete unless it includes:

- generated YAML files;
- campaign state tracking;
- exact raw launch command;
- a dedicated PowerShell launcher;
- launcher documentation.

This should be reflected in:

- `AGENTS.md`
- `doc/guide/project_usage_guide.md`

so future sessions follow the same workflow without relying on memory.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Documentation index that should reference this technical note.
- `AGENTS.md`
  Permanent repository instructions that should be updated after approval.
- `doc/guide/project_usage_guide.md`
  Usage guide that should document the launcher requirement after approval.
- `scripts/campaigns/`
  Home for repository-owned PowerShell launchers.
- `doc/scripts/campaigns/`
  Home for launcher usage notes.
- `scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.ps1`
  Existing launcher pattern to mirror for the new campaign-specific wrapper.
- `doc/scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md`
  Existing launcher documentation pattern to mirror for the new campaign note.
- `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave2_residual_harmonic_family_campaign/`
  Current approved campaign YAML set that should receive a matching launcher.
- `doc/running/active_training_campaign.yaml`
  Prepared campaign state that should remain aligned with the launcher output.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. Wait for explicit user approval before modifying repository rules or adding
   launcher files.
3. After approval, create
   `scripts/campaigns/run_wave2_residual_harmonic_family_campaign.ps1`.
4. Add the matching usage note under
   `doc/scripts/campaigns/run_wave2_residual_harmonic_family_campaign.md`.
5. Update `AGENTS.md` so every future approved campaign preparation must also
   include a dedicated launcher script and launcher documentation.
6. Update `doc/guide/project_usage_guide.md` so the launcher requirement is part
   of the documented training-campaign workflow.
7. Report completion and wait for explicit user approval before creating any
   Git commit.
