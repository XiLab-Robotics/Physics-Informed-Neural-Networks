# TE Curve Verification Pipeline Dataset-Surface Report Split Launcher

## Overview

This launcher prepares and runs the approved `TE Curve Verification Pipeline`
dataset/surface split workflow. It creates separate matrix and visual report
families for `polished_dataset` and `simplified_dataset` across `forward`,
`backward`, and `global` scopes, and it can build dataset-difference reports
from explicit simplified-trained versus polished-trained candidate pairs.

Status after the `2026-07-06` pruning decision: this broad split workflow is
paused / on-demand. The active default report workflow is the reduced
selected-model launcher:

- `scripts/campaigns/track_2/run_reduced_selected_track2_reports.ps1`

Do not run this broad launcher for routine closeout unless `global`, collage,
overlay, or simplified-vs-polished dataset-difference reports have been
explicitly requested.

The heavy run is gated. Do not use `-Run` until the full-wave polished
retraining closure commits and artifacts from the other workstation have been
merged into the local repository.

## Dry Run

Run from the repository root:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1
```

The default mode prints the planned dataset/surface matrix and exits without
running the heavy verification pipeline.

## Progress Smoke Test

Run the launcher-owned progress smoke test before a long operator run when
checking terminal rendering:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1 `
  -ProgressSmokeTest
```

This exercises the same `conda run` wrapper used by the heavy pipeline without
loading model candidates. The wrapper reads child-process output directly so
`tqdm` carriage-return updates can refresh a single terminal row while the
per-step log file still records the emitted progress lines. The smoke test also
asserts that the child process starts from the repository root.

## Local Run

After the full-wave polished retraining closure merge is present:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1 `
  -Run `
  -AcknowledgeFullWaveClosureMerged
```

If a long run stops after completing earlier steps, resume from the first
failed step instead of recomputing previous matrix or collage reports:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1 `
  -Run `
  -AcknowledgeFullWaveClosureMerged `
  -ResumeFromStep 03_overlay_polished_dataset_forward
```

Add candidate pairs for dataset-difference reports after the merged matrix
candidate IDs are known:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1 `
  -Run `
  -AcknowledgeFullWaveClosureMerged `
  -ForwardCandidatePair "feedforward_fw:feedforward_Fw:polished_feedforward_Fw" `
  -BackwardCandidatePair "feedforward_bw:feedforward_Bw:polished_feedforward_Bw" `
  -GlobalCandidatePair "feedforward_global:feedforward_global:polished_feedforward_global"
```

Each candidate-pair value must use:

```text
PAIR_ID:SIMPLIFIED_CANDIDATE_ID:POLISHED_CANDIDATE_ID
```

## Remote Run

After the full-wave closure merge is available in the remote checkout:

```powershell
.\scripts\campaigns\track_2\run_track2_dataset_surface_report_split.ps1 `
  -Remote `
  -AcknowledgeFullWaveClosureMerged `
  -RemoteHostAlias xilab-remote `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
```

Remote mode assumes the approved source and full-wave closure artifacts have
already been merged or synchronized into the remote checkout before launch.

## Expected Outputs

Matrix artifacts are written under:

- `output/validation_checks/track2_reference_comparison/`

The canonical directional matrix report is refreshed at:

- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`

Dataset/surface visual reports are written under:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/dataset_surface_report/<dataset>/<surface>/collage/[YYYY-MM-DD]/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/dataset_surface_report/<dataset>/<surface>/overlay/[YYYY-MM-DD]/`

Dataset-difference reports are written under:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/dataset_difference_report/[YYYY-MM-DD]/<dataset>/<surface>/`

Operator logs are written under:

- `output/validation_checks/track2_operator_launch_logs/`

The launcher streams child-process output to the terminal while also writing the
same text to the per-step log file. Cross-dataset model evaluation adapts each
candidate input matrix to the loaded model feature dimension before
normalization, so four-feature polished checkpoints and five-feature simplified
checkpoints can be evaluated in the same dataset-surface run.

## Notes

The existing overlay builder supports `forward` and `backward` scopes. Global
scope remains covered by the matrix and collage report paths. PDF export should
be performed after the generated Markdown and plot bundles have been inspected.
