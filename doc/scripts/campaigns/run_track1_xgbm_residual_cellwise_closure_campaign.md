# Track 1 XGBM Residual Cellwise Closure Campaign Launcher

This launcher runs the aggressive overnight residual-cell closure wave for the exact-paper `XGBM` family.

- included configs: `114`
- closure attempts per residual target pair: `6`

Attempt matrix:

| Attempt | `random_seed` | `test_size` |
| --- | ---: | ---: |
| `01` | `0` | `0.20` |
| `02` | `7` | `0.20` |
| `03` | `21` | `0.20` |
| `04` | `42` | `0.20` |
| `05` | `0` | `0.15` |
| `06` | `0` | `0.25` |

Local command:

```powershell
.\scripts\campaigns\run_track1_xgbm_residual_cellwise_closure_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\run_track1_xgbm_residual_cellwise_closure_campaign.ps1 -Remote
```
