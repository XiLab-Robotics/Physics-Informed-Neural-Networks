# Track 2F Track 2 Verification Refresh Launcher

## Overview

This launcher runs the operator-approved `Track 2` offline verification refresh
for the completed `Track 2F` offset-aware probe campaign.

It evaluates the three registry-backed `Track 2F` branch candidates in
parallel:

| Surface | Candidate | Registry |
| --- | --- | --- |
| `global` | `sequential_residual_offset_probe_global` | `output/registries/families/sequential_residual_offset_probe/latest_family_best.yaml` |
| `Fw` | `sequential_residual_offset_probe_Fw` | `output/registries/families/sequential_residual_offset_probe_fw/latest_family_best.yaml` |
| `Bw` | `sequential_residual_offset_probe_Bw` | `output/registries/families/sequential_residual_offset_probe_bw/latest_family_best.yaml` |

The launcher is operator-facing. Codex prepares it and provides the command,
but does not run the heavy `Track 2` matrix internally.

## Local Command

Run from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_track2_verification_refresh.ps1
```

The default local environment is `pinns_env`.

## Remote Command

Run from the repository root:

```powershell
.\scripts\campaigns\track2\run_track2f_track2_verification_refresh.ps1 -Remote
```

Remote mode syncs the required local Track 2 launcher, config, scripts, Track
2F family registries, Track 2F training-run artifacts, and the completed
`Wave 2C` Track 2 baseline summary to the remote checkout before execution. It
then syncs only the generated artifact paths listed by the run-local artifact
sync manifest back to the local repository.

Override connection details when needed:

```powershell
.\scripts\campaigns\track2\run_track2f_track2_verification_refresh.ps1 `
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

By default, the matrix uses the completed `Wave 2B` refresh as the configured
baseline summary and only evaluates incremental current candidates. The new
candidate-source plot sync is scoped to
`track2f_offset_aware_probe_registry`. Use
`-SyncFullTrack2CampaignResultPlots` only when a deliberate full historical
`doc/reports/campaign_results/track 2/` visual refresh is required.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical matrix report is updated at:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Visual report bundles are written under:

- `doc/reports/analysis/track2/best_model_collage_report/[2026-06-04]/`
- `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-04]/`
- `doc/reports/analysis/track2/official_model_verification_report/[2026-06-04]/`

Operator launch logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

## Follow-Up

After the launcher completes, report completion back to Codex. Codex should
then inspect the matrix summary, review the launcher-generated official model
verification report, validate the real PDFs, and synchronize the live backlog
and master summary. The normal launcher path already generates the official
report and includes it in the PDF export.
