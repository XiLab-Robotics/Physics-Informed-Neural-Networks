# Wave 3.1 Launcher Exit Flow Fix

## Overview

The local command:

```powershell
.\scripts\campaigns\track_2\run_track2f_offset_aware_probe_campaign.ps1
```

currently writes the Wave 3.1 prelaunch status YAML/CSV and then stops before
starting `scripts/training/run_training_campaign.py`.

The campaign package itself is valid: it contains three runnable
`sequential_residual_offset_probe` queue YAML files for `global`, `Fw`, and
`Bw`. The failure is in the PowerShell launcher control flow.

## Technical Approach

The launcher helper `Invoke-Track2FPython` currently lets Python stdout flow
through the PowerShell function output stream and also returns `$LASTEXITCODE`.
When the caller assigns the function output to `$pythonExitCode`, PowerShell
captures both printed text and the integer exit code. The later nonzero check
therefore sees textual output as a truthy mismatch and exits immediately after
validation.

The fix is to avoid returning mixed pipeline output from the helper. The
launcher should:

- invoke Python/Conda directly from the helper;
- store the real process exit code in a script-scoped variable;
- let stdout continue to the terminal for operator visibility;
- compare only the integer process exit code;
- continue from validation into the local `run_training_campaign.py` call when
  validation succeeds.

No model code or campaign YAML semantics need to change.

## Involved Components

Protected Wave 3.1 campaign files:

- `scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.ps1`;
- `scripts/campaigns/track_2/prepare_track2f_offset_aware_probe_campaign.py`;
- `doc/scripts/campaigns/track_2/run_track2f_offset_aware_probe_campaign.md`.

Supporting state and verification files:

- `doc/running/active_training_campaign.yaml`;
- `output/validation_checks/track2f_offset_aware_probe/2026-06-03_track2f_offset_aware_probe_prelaunch/track2f_probe_package_summary.yaml`;
- `output/validation_checks/track2f_offset_aware_probe/2026-06-03_track2f_offset_aware_probe_prelaunch/track2f_probe_entry_status.csv`.

## Implementation Steps

1. Update the Wave 3.1 launcher helper so it stores the external process exit
   code without returning stdout as a captured value.
2. Apply the same fix in the generator script so future launcher regeneration
   preserves the corrected behavior.
3. Keep the local and `-Remote` operator command text unchanged.
4. Run `-PreflightOnly` and confirm it exits after validation.
5. Run a non-training-safe direct command check if needed by using
   `run_training_campaign.py --enqueue-only` with the three queue YAML files.
6. Run PowerShell parser validation and Markdown QA on touched documentation.
7. Stop before launching the long training campaign unless the user explicitly
   asks to run it from Codex.

## Protected Campaign Warning

`doc/running/active_training_campaign.yaml` marks the Wave 3.1 launcher and
launcher note as protected. This fix intentionally edits that protected
launcher because it is the prepared campaign's operator entrypoint and it is
currently blocking execution before the training runner starts.
