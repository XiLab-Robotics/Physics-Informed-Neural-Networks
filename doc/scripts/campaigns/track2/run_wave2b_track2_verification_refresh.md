# Wave 2B Track 2 Verification Refresh Launcher

## Overview

This launcher runs the operator-approved `Track 2` offline verification refresh
for the completed `Wave 2B` harmonic-temporal hybrid campaign.

It adds the current registry-backed `Wave 2B` candidate surfaces to the official
direction-aware matrix through:

- `periodic_temporal_convolution_global`, `periodic_temporal_convolution_Fw`,
  and `periodic_temporal_convolution_Bw`;
- `periodic_gru_sequence_global`, `periodic_gru_sequence_Fw`, and
  `periodic_gru_sequence_Bw`;
- `periodic_lstm_sequence_global`, `periodic_lstm_sequence_Fw`, and
  `periodic_lstm_sequence_Bw`.

The launcher is intentionally operator-facing. Codex prepares it and provides
the command, but does not run the heavy `Track 2` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track2\run_wave2b_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track2\run_wave2b_track2_verification_refresh.ps1 -Remote
```

Remote mode assumes the remote repository checkout already contains the same
committed state as the local repository. Override connection details when
needed:

```powershell
.\scripts\campaigns\track2\run_wave2b_track2_verification_refresh.ps1 `
  -Remote `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName pinns_env
```

## Workflow

The launcher runs:

1. the official full direction-aware `Track 2` matrix;
2. the best-model collage report generation;
3. the multi-model curve-comparison report generation;
4. the PDF export for the two visual reports.

Use `-SkipVisualReports` to run only the matrix, or `-SkipPdfExport` to leave
the generated visual reports as Markdown plus image artifacts.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-26]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-05-26]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should then
inspect the matrix summary, regenerate or update the official model verification
decision report, validate the real PDFs, and synchronize the live backlog and
master summary.
