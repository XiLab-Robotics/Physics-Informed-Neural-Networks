# Track 2H Mixture Density Heads Campaign Package

This package materializes the approved Track 2H mixture-density
heads probe. It contains 6 runnable queue entries: `mdn_k2` and
`mdn_k3` across `global`, `Fw`, and `Bw` surfaces.

Deterministic Track 2 playback uses the mixture expectation. The
extra channels are component logits, component means, and component
scales for training and diagnostics, not future-looking inference
inputs.

## Queue Files

- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/01_mdn_k2_global.yaml`
- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/02_mdn_k2_fw.yaml`
- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/03_mdn_k2_bw.yaml`
- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/04_mdn_k3_global.yaml`
- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/05_mdn_k3_fw.yaml`
- `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign/queue/06_mdn_k3_bw.yaml`

## Launch Commands

```powershell
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -PreflightOnly
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1
.\scripts\campaigns\track2\run_track2h_mixture_density_heads_campaign.ps1 -Remote
```
