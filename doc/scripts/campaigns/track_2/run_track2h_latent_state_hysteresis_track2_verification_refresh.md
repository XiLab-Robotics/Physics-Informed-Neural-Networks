# Track 2H-L Track 2 Verification Refresh Launcher

## Overview

This launcher runs the operator-approved official `Track 2` offline
verification refresh for the completed `Track 2H-L` latent-state /
hysteresis-aware campaign.

It adds six registry-backed candidates to the direction-aware matrix: two
latent-state profiles over the three required deployment surfaces.

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `gru_offset_residual` | `track2h_l_gru_offset_residual_global` | `track2h_l_gru_offset_residual_Fw` | `track2h_l_gru_offset_residual_Bw` |
| `causal_tcn_offset_residual` | `track2h_l_causal_tcn_offset_residual_global` | `track2h_l_causal_tcn_offset_residual_Fw` | `track2h_l_causal_tcn_offset_residual_Bw` |

The launcher is operator-facing. Codex prepares it and provides the command,
but does not run the heavy `Track 2` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local `Track 2` launcher, config, scripts,
`Track 2H-L` family registries, `Track 2H-L` training-run artifacts, and the
completed `Wave 2C` `Track 2` baseline summary to the remote checkout before
execution. It then syncs only the generated artifact paths listed by the
run-local artifact sync manifest back to the local repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\track_2\run_track2h_latent_state_hysteresis_track2_verification_refresh.ps1 `
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
4. the visual source-coverage validation against the matrix candidate list;
5. the official model-verification report generation;
6. the PDF export for the collage, overlay, and official verification reports.

Use `-SkipVisualReports` to run only the matrix, or `-SkipPdfExport` to leave
the generated visual and official reports as Markdown plus image artifacts.
When visual reports are enabled, the launcher fails before PDF export if a
registry-backed matrix source is not visible in the collage and overlay
Markdown reports.

By default, the matrix uses the completed `Wave 2C` refresh as the configured
baseline summary and evaluates the current matrix candidates. The new
candidate-source plot sync is scoped to
`track2h_latent_state_hysteresis_registry`. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track_2/verification_plots/` visual refresh is
required.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-06-18]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-18]/`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-18]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

Remote source synchronization sends:

- `scripts/`
- `config/`
- `doc/scripts/campaigns/track_2/`
- `output/registries/families/track2h_latent_state_hysteresis_*`
- `output/training_runs/track2h_latent_state_hysteresis_*`
- the completed `Wave 2C` `Track 2` baseline summary and per-condition metrics

Remote artifact synchronization retrieves:

- the current run's `output/validation_checks/track2_reference_comparison/...`
  directory;
- the current run's visual-report output directories when visual reports are
  enabled;
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- the dated visual-report and official-report bundles for the selected
  `-ReportDate`;
- the current run's operator log directory and `artifact_sync_manifest.txt`;
- `doc/reports/campaign_results/track_2/verification_plots/track2h_latent_state_hysteresis_registry/`
  when present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog,
training master summary, and TE program ledger if the official decision
changes modeling status.
