# Track 1 MLP Family Full-Matrix Repair Campaign Launcher

This launcher runs the dedicated exact-paper `MLP` family repair wave for
the canonical `Track 1` full-matrix replication surface.

- included configs: `324`
- distinct target pairs: `12`
- closure attempts per target pair: `27`
- amplitude target count: `8`
- phase target count: `4`

Attempt matrix:

| Attempt | `random_seed` | `test_size` |
| --- | ---: | ---: |
| `01` | `0` | `0.20` |
| `02` | `7` | `0.20` |
| `03` | `11` | `0.20` |
| `04` | `13` | `0.20` |
| `05` | `17` | `0.20` |
| `06` | `21` | `0.20` |
| `07` | `23` | `0.20` |
| `08` | `29` | `0.20` |
| `09` | `42` | `0.20` |
| `10` | `0` | `0.15` |
| `11` | `7` | `0.15` |
| `12` | `11` | `0.15` |
| `13` | `13` | `0.15` |
| `14` | `17` | `0.15` |
| `15` | `21` | `0.15` |
| `16` | `23` | `0.15` |
| `17` | `29` | `0.15` |
| `18` | `42` | `0.15` |
| `19` | `0` | `0.25` |
| `20` | `7` | `0.25` |
| `21` | `11` | `0.25` |
| `22` | `13` | `0.25` |
| `23` | `17` | `0.25` |
| `24` | `21` | `0.25` |
| `25` | `23` | `0.25` |
| `26` | `29` | `0.25` |
| `27` | `42` | `0.25` |

Scoped target pairs:

- amplitude harmonics: `0, 1, 3, 39, 40, 81, 156, 240`
- phase harmonics: `1, 3, 39, 162`

Local command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_family_full_matrix_repair_campaign.ps1
```

Remote command:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_mlp_family_full_matrix_repair_campaign.ps1 -Remote
```
