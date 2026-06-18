# Wave 2C Remote Repository Path Fallback

## Overview

The `Wave 2C` campaign launcher exposes `-Remote`, but a direct call without
`PINNS_REMOTE_TRAINING_REPO_PATH` currently fails before remote preflight:

```text
RemoteRepositoryPath is required. Set PINNS_REMOTE_TRAINING_REPO_PATH or pass -RemoteRepositoryPath.
```

The failure is caused by the dedicated `Wave 2C` wrapper forwarding an empty
`RemoteRepositoryPath` to the shared remote infrastructure launcher. Existing
repository-owned PowerShell remote launchers commonly fall back to the validated
LAN clone path:

```text
C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks
```

## Technical Approach

Update the `Wave 2C` launcher and its generator so `-Remote` behaves like the
other prepared campaign launchers:

- prefer `PINNS_REMOTE_TRAINING_REPO_PATH` when it is set;
- otherwise use the established LAN clone path fallback;
- keep explicit `-RemoteRepositoryPath` overrides supported;
- update the launcher note to document the fallback and override;
- avoid executing the launcher or starting training during validation.

## Involved Components

- `scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1`
- `scripts/campaigns/wave_2/prepare_wave2c_residual_harmonic_temporal_hybrid_campaign.py`
- `doc/scripts/campaigns/wave_2/run_wave2c_residual_harmonic_temporal_hybrid_campaign.md`
- `doc/running/active_training_campaign.yaml`
- `doc/README.md`

The `Wave 2C` launcher and launcher note are protected by the prepared campaign
state. This fix requires explicit approval before modifying them.

## Implementation Steps

1. Patch the dedicated `Wave 2C` launcher parameter default for
   `RemoteRepositoryPath`.
2. Patch the campaign preparer so regenerated launchers keep the same fallback.
3. Update the launcher note with the default remote repository path and the
   explicit override form.
4. Run static PowerShell parse checks and Python compile checks only.
5. Run scoped Markdown QA on touched Markdown files.
6. Do not launch the local or remote campaign script without separate operator
   authorization.
