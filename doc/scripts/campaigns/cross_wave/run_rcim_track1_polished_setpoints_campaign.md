# Run RCIM Track1 Polished Setpoints Campaign

## Purpose

Operator-facing launcher for the prepared
`dataset_input_mode_retraining__rcim_track1__polished_setpoints` campaign.

## Preflight

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1 -PreflightOnly
```

## Local Launch

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1
```

The default local launch runs `global`, `fw`, and `bw` in parallel on the
Windows workstation. This campaign is intentionally not submitted to Aries, so
the cluster can keep running the separate cross-wave retraining queue.

When the shell is not already inside `pinns_env`, the launcher resolves and
uses that environment's `python.exe` directly instead of wrapping long surface
runs with `conda run`.

## Promotion

After the three surfaces finish and the campaign package validator still
passes, promote the exported ONNX and Python artifacts into the official
paper-reference archive:

```powershell
conda run --no-capture-output -n pinns_env python -B scripts\campaigns\cross_wave\promote_rcim_track1_input_mode_exports.py --input-mode setpoints --replace
```

The promotion step hard-checks the polished dataset, `setpoints` input mode,
surface labels, five-feature input contract, and per-family ONNX/Python export
counts before writing:

```text
models/polished_dataset/paper_reference/rcim_track1/setpoints/
```

## Local Sequential Launch

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1 -Sequential
```

## Local Surface Launch

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1 -Surface global
```

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1 -Surface fw
```

```powershell
.\scripts\campaigns\cross_wave\run_rcim_track1_polished_setpoints_campaign.ps1 -Surface bw
```

## Campaign Manifest

`config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_setpoints/campaign.yaml`
