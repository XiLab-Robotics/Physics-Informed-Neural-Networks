# Track 1 HGBM Remaining Yellow-Cell Campaign Launcher

This launcher runs the dedicated exact-paper `HGBM` yellow-cell
repair wave for the canonical Track 1 family-row closure surface.

- included configs: `60`
- distinct target pairs: `1`
- closure attempts per target pair: `60`
- amplitude target count: `1`
- phase target count: `0`

Retry matrix:

- seeds: `0, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 27, 29, 31, 37, 42, 47, 53, 59, 61`
- test sizes: `0.20, 0.15, 0.25`

Scoped target pairs:

- amplitude harmonics: `39`
- phase harmonics: `none`

Local command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_hgbm_remaining_yellow_cell_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_hgbm_remaining_yellow_cell_campaign.ps1 -Remote
```
