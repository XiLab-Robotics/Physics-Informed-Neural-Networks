# Track 2H Quantile Probabilistic Track 2 Verification Refresh Launcher

## Overview

This launcher runs the operator-approved official `Track 2` offline
verification refresh for the completed second `Track 2H`
quantile/probabilistic campaign.

It adds six registry-backed candidates to the direction-aware matrix: two
probabilistic profiles over the three required deployment surfaces.

| Profile | `global` | `Fw` | `Bw` |
| --- | --- | --- | --- |
| `quantile_p10_p50_p90` | `track2h_quantile_p10_p50_p90_global` | `track2h_quantile_p10_p50_p90_Fw` | `track2h_quantile_p10_p50_p90_Bw` |
| `gaussian_nll` | `track2h_gaussian_nll_global` | `track2h_gaussian_nll_Fw` | `track2h_gaussian_nll_Bw` |

The launcher is operator-facing. Codex prepares it and provides the command,
but does not run the heavy `Track 2` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local Track 2 launcher, config, scripts,
Track 2H quantile/probabilistic family registries, matching training-run
artifacts, and the completed `Wave 2C` Track 2 baseline summary to the remote
checkout before execution. It then syncs only the generated artifact paths
listed by the run-local artifact sync manifest back to the local repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\track_2\run_track2h_quantile_probabilistic_track2_verification_refresh.ps1 `
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

The matrix compares the deterministic scalar curve exposed by each
probabilistic checkpoint: `p50` for quantile candidates and `mu` for Gaussian
NLL candidates.

By default, the matrix uses the completed `Wave 2C` refresh as the configured
baseline summary and only evaluates incremental current candidates. The new
candidate-source plot sync is scoped to
`track2h_quantile_probabilistic_registry`. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track_2/verification_plots/` visual refresh is required.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-06-12]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-12]/`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-12]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

The visual coverage step writes the `04_track2_visual_source_coverage.log`
file in the same operator log directory. A successful run confirms that every
registry-backed source resolved from the matrix configuration is exposed by
the visual Markdown reports before PDF export.

The official report step writes the
`05_track2_official_verification_report.log` file and builds the official
decision Markdown from the same matrix, collage, and overlay summaries used by
the operator run. The PDF export step includes all three dated reports.

Remote source synchronization sends:

- `scripts/`
- `config/`
- `doc/scripts/campaigns/track_2/`
- `output/registries/families/track2h_quantile_probabilistic_*`
- `output/training_runs/track2h_quantile_probabilistic_*`
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
- `doc/reports/campaign_results/track_2/verification_plots/track2h_quantile_probabilistic_registry/`
  when present.

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog
and master summary. The normal launcher path already generates the official
report and includes it in the PDF export.
