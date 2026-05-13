# Track 1 Paper-Faithful ELM Queue Addendum Plan Report

## Overview

This addendum extends the approved Track 1 paper-faithful search campaign
package so the prepared queue matches the current operational exact-paper
family surface.

The original replacement plan fixed the campaign at the `10` paper families
available at preparation time. The exact-paper implementation now also supports
`ELM` as an operational family, with the same recovered-original-style search,
export, and ONNX support used by the shared family bank.

## Objective

Add one `ELM` search run per direction to the already prepared paper-faithful
queue without changing the recovered-original search protocol.

## Queue Delta

| Direction | Existing Families | Added Families | New Runs |
| --- | ---: | ---: | ---: |
| `forward` | `10` | `1` | `11` |
| `backward` | `10` | `1` | `11` |

Total family-direction surfaces after this addendum: `22`.

## ELM Policy

| Family | Search Policy | Literal-Workflow Status |
| --- | --- | --- |
| `ELM` | paper-reference grid search enabled once | literalized from recovered-original `ELMRegressor` support |

## Safety Constraints

- No seed sweep is introduced.
- No retry ladder is introduced.
- The campaign remains one config and one search pass per family-direction
  surface.
- The existing exact-paper runner continues to perform `GridSearchCV` plus the
  historical `cross_validate(...)` replay.
- The launch command can be sliced to `forward` or `backward` through the
  existing launcher arguments.

## Generated Artifacts

This addendum prepares:

- one forward `ELM` YAML;
- one backward `ELM` YAML;
- matching queue-local README files;
- an updated persistent campaign state that includes `ELM` in the queue and
  protected-file bookkeeping;
- updated launcher documentation for the `11`-family forward command.

## Launch Command

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM" `
  -Stage Search `
  -GridSearchVerboseOverride 3 `
  -HistoricalCrossValidateVerboseOverride 10 `
  -Remote
```

## Post-Campaign Obligations

The post-campaign closeout remains the same as the parent paper-faithful
replacement plan: update the paper-reference benchmark, master summary,
family/program registries, and Track 1 archives after completed runs are
available.
