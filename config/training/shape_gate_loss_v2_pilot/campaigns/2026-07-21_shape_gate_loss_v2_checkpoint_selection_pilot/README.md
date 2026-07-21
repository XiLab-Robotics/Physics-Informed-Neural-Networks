# Shape-Gate Loss V2 Checkpoint Selection Pilot Package

## Contents

This package prepares one non-promotional pilot run:

- `campaign.yaml`
- `queue/001_shape_gate_loss_v2_periodic_gru_sequence_fw.yaml`

## Scope

- dataset: `polished_dataset`
- input mode: `setpoints`
- surface: `Fw`
- model: `periodic_gru_sequence`
- run count: `1`

The package tests light shape-aware pressure plus post-run shape-gated
checkpoint acceptance. It does not open the full three-dataset, three-surface
campaign.

## Launcher

Use:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1
```

Remote execution:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
  -Remote
```
