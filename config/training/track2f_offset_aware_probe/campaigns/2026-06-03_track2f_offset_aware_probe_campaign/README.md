# Wave 3.1 Offset-Aware Probe Campaign Package

This package materializes the approved Wave 3.1 offset-aware probe plan.

It contains descriptor entries for the full Wave 3.1 matrix plus three
runnable `sequential_residual_offset_probe` queue YAML files. The post-hoc
`direction_torque` offset baseline remains a validation-only benchmark, while
`multi_head_shape_offset_probe` remains guarded until its own model type is
introduced through a later technical gate.

## Descriptor Matrix

- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/01_global_posthoc_direction_torque_offset_baseline.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/02_fw_posthoc_direction_torque_offset_baseline.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/03_bw_posthoc_direction_torque_offset_baseline.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/04_global_sequential_residual_offset_probe.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/05_fw_sequential_residual_offset_probe.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/06_bw_sequential_residual_offset_probe.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/07_global_multi_head_shape_offset_probe.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/08_fw_multi_head_shape_offset_probe.yaml`
- `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/probe_descriptors/09_bw_multi_head_shape_offset_probe.yaml`

## Launch Commands

Preflight validation:

```powershell
.\scripts\campaigns\track_2\run_track2f_offset_aware_probe_campaign.ps1 -PreflightOnly
```

Sequential probe training:

```powershell
.\scripts\campaigns\track_2\run_track2f_offset_aware_probe_campaign.ps1
```

Remote sequential probe training:

```powershell
.\scripts\campaigns\track_2\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```
