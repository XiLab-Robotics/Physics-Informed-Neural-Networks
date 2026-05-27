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

Remote mode syncs the required local Track 2 launcher, config, script, registry,
and `Wave 2B` checkpoint paths to the remote checkout before execution. It then
syncs only the generated artifact paths listed by the run-local artifact sync
manifest back to the local repository. This keeps closed `Wave 1` report-plot
history out of normal `Wave 2B` refresh downloads.

Override connection details when needed:

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

By default, the matrix uses the configured baseline summary and only evaluates
new incremental candidates. The grouped report-plot sync is also scoped to the
new `wave2_temporal_entry_registry` source. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track 2/` visual refresh is required.

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

Remote source synchronization sends:

- `scripts/`
- `config/`
- `doc/scripts/campaigns/track2/`
- `output/registries/families/periodic_*`
- `output/training_runs/periodic_*`

Remote artifact synchronization retrieves:

- the current run's `output/validation_checks/track2_reference_comparison/...`
  directory;
- the current run's visual-report output directories when visual reports are
  enabled;
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- the dated visual-report bundles for the selected `-ReportDate`;
- the current run's operator log directory and `artifact_sync_manifest.txt`;
- `doc/reports/campaign_results/track 2/wave2_temporal_entry_registry/` when
  present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should then
inspect the matrix summary, regenerate or update the official model verification
decision report, validate the real PDFs, and synchronize the live backlog and
master summary.
