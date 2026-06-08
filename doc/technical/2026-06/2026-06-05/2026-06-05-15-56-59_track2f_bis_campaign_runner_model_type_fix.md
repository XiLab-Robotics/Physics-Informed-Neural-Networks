# Track 2F-Bis Campaign Runner Model-Type Fix

## Overview

The operator-launched `Track 2F-bis` campaign completed the three clean
non-harmonic control runs, but the three `harmonic_residual_offset_probe` runs
failed immediately.

The failed entries did not reach model training. The campaign execution report
shows the root cause:

```text
Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe
```

The model itself was already registered in `scripts/models/model_factory.py`
and passed one-batch validation plus fast-dev smoke testing before the
campaign was launched. The missing piece is the campaign runner model-type
whitelist in `scripts/training/run_training_campaign.py`.

## Technical Approach

Apply a narrow runner registration fix:

- add `harmonic_residual_offset_probe` to
  `SUPPORTED_MODEL_ENTRYPOINT_NAME_DICTIONARY`;
- add `harmonic_residual_offset_probe` to the supported handler dictionary in
  `resolve_training_handler`;
- keep the entrypoint as `scripts/training/train_feedforward_network.py`,
  matching the other neural PyTorch model families;
- validate the failed `Track 2F-bis` harmonic YAMLs after the fix;
- prepare rerun of only the three failed harmonic-offset entries, not the
  already-completed clean baseline runs.

The terminal-level `conda run ... failed` message is expected whenever
`run_training_campaign.py` exits nonzero because one or more campaign entries
failed. This fix addresses the real failure source for this campaign. The
previous wrapper-noise issue should still be treated separately from genuine
failed campaign entries.

## Involved Components

- `scripts/training/run_training_campaign.py`
- `config/training/queue/failed/2026-06-04-23-31-57_004_04_harmonic_residual_offset_probe_global.yaml`
- `config/training/queue/failed/2026-06-04-23-31-57_005_05_harmonic_residual_offset_probe_fw.yaml`
- `config/training/queue/failed/2026-06-04-23-31-57_006_06_harmonic_residual_offset_probe_bw.yaml`
- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/2026-06-04-23-31-57_track2f_bis_harmonic_offset_probe_campaign_2026_06_04/`
- later closeout report under `doc/reports/campaign_results/track2/`

## Implementation Steps

1. Update `scripts/training/run_training_campaign.py` to accept
   `harmonic_residual_offset_probe`.
2. Run Python compile checks for the runner and model registration path.
3. Revalidate the three failed harmonic-offset YAML files.
4. Run a focused one-batch validation for at least one failed harmonic YAML
   using its failed-queue copy.
5. Relaunch only the three failed harmonic-offset entries after approval.
6. Inspect the new campaign output and merge the result interpretation with
   the already-completed clean baseline runs.
7. Produce the normal campaign closeout Markdown and styled PDF only after the
   harmonic branch has actually run or after the campaign is explicitly closed
   as partial.
8. Clear or update `doc/running/active_training_campaign.yaml` according to the
   final closeout state.
