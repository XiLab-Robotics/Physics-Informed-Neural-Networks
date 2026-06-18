# Track 1 Forward Remote Micro-Campaign And Mega Relaunch Gate Plan Report

## Overview

This planning report covers the reset path after the interrupted
`Track 1` bidirectional original-dataset mega-campaign.

The interrupted mega-campaign is treated as a discarded operational wave, not
as a resumable scientific campaign.

The next execution step is a deliberately small remote diagnostic campaign
whose only job is to verify that the current hardened pipeline behaves
correctly end to end on the remote workstation.

## Objective

Establish a low-risk remote relaunch gate before regenerating the full
bidirectional mega-campaign.

The gate must answer a simple question:

- can the current remote campaign stack complete one clean run for each exact
  paper family with the current launcher, current `MLP` stabilization, current
  ONNX preflight, and current output/report synchronization assumptions?

## Interrupted Wave Policy

The currently interrupted bidirectional mega-campaign must be closed with the
following policy:

| Surface | Policy |
| --- | --- |
| Campaign state | mark `interrupted` |
| Scientific reuse | discard |
| Benchmark promotion | forbidden |
| Registry promotion | forbidden |
| Archive refresh | forbidden |
| Operational traceability | keep logs and evidence |

## Micro-Campaign Surface

### Direction Policy

The micro-campaign stays `forward` only.

Reason:

- the user explicitly requested a small run with one training per algorithm;
- this keeps the diagnostic surface at `10` total runs instead of `20`;
- the goal is launcher and workflow validation, not bidirectional scientific
  coverage.

### Family Grid

| Direction | Families | Attempts Per Family | Total Runs |
| --- | ---: | ---: | ---: |
| `forward` | `10` | `1` | `10` |

## Family Policy

| Family | Search Policy |
| --- | --- |
| `SVR` | direct fit, grid search disabled |
| `MLP` | current stabilized exact-paper branch |
| `RF` | paper-reference grid search enabled |
| `DT` | paper-reference grid search enabled |
| `ET` | paper-reference grid search enabled |
| `ERT` | paper-reference grid search enabled |
| `GBM` | paper-reference grid search enabled |
| `HGBM` | paper-reference grid search enabled |
| `XGBM` | paper-reference grid search enabled |
| `LGBM` | paper-reference grid search enabled |

## Safety Constraints

| Setting | Value |
| --- | --- |
| Dataset Root | `data/datasets` |
| Direction | `forward` only |
| Split Policy | file-level `70 / 20 / 10` |
| Feature Schema | `rpm`, `deg`, `tor` |
| Target Scope | full exact-paper `19`-target family bank |
| Remote Mode | canonical remote operator launcher |
| Benchmark Impact | none during micro phase |

## Generated Artifacts

After implementation, the preparation step should generate:

- one interrupted closeout result report for the discarded mega-campaign;
- one fresh `10`-run micro-campaign config package;
- one dedicated remote launcher;
- one launcher note;
- one updated `doc/running/active_training_campaign.yaml` in `prepared` state
  for the micro-campaign;
- one exact launch command for the remote micro-campaign.

## Relaunch Gate

The full bidirectional mega-campaign may be regenerated only if the
micro-campaign satisfies all of the following:

1. all `10` runs complete;
2. no remote launcher/bootstrap crash occurs;
3. validation bundles are produced for all families;
4. ONNX export completes according to the configured policy;
5. no new class of remote logging or synchronization failure appears.

## Expected Follow-Up

If the gate passes, the next step is a fresh preparation of the full
bidirectional mega-campaign from zero, not a resume of the interrupted queue.
