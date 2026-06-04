# Track 2F-Bis Harmonic-Offset Probe Campaign Package

This package materializes the approved Track 2F-bis harmonic-offset probe.

It contains six runnable queue YAML files:

- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/01_clean_sequential_residual_offset_control_global.yaml`
- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/02_clean_sequential_residual_offset_control_fw.yaml`
- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/03_clean_sequential_residual_offset_control_bw.yaml`
- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/04_harmonic_residual_offset_probe_global.yaml`
- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/05_harmonic_residual_offset_probe_fw.yaml`
- `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/06_harmonic_residual_offset_probe_bw.yaml`

## Launch Commands

Preflight validation:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -PreflightOnly
```

Local training:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1
```

Remote training:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote
```
