# Track 1 SVM Remaining Yellow-Cell Campaign Launcher

This launcher runs the dedicated exact-paper `SVM` yellow-cell
repair wave for the canonical Track 1 family-row closure surface.

- included configs: `180`
- distinct target pairs: `3`
- closure attempts per target pair: `60`
- amplitude target count: `2`
- phase target count: `1`

Retry matrix:

- seeds: `0, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 27, 29, 31, 37, 42, 47, 53, 59, 61`
- test sizes: `0.20, 0.15, 0.25`

Scoped target pairs:

- amplitude harmonics: `40, 240`
- phase harmonics: `162`

Local command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_svm_remaining_yellow_cell_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_svm_remaining_yellow_cell_campaign.ps1 -Remote
```
