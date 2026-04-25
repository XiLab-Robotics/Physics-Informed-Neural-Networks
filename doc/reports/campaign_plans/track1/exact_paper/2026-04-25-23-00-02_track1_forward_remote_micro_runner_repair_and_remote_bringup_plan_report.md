# Track 1 Forward Remote Micro Runner Repair And Remote Bringup Plan Report

## Overview

This planning report covers the repair and rerun of the prepared `Track 1`
forward-only original-dataset remote micro-campaign after the first launch
failed before the initial `SVR` run could build its dataset bundle.

The current failure is not a scientific-model issue.

It is a campaign-stack routing issue:

- the micro-campaign YAML payload is original-dataset based;
- the launcher still calls the legacy exact-paper recovered-CSV runner.

## Confirmed Failure

| Surface | Current Value |
| --- | --- |
| Campaign | `track1_forward_original_dataset_remote_micro_campaign_2026-04-25_22_53_15` |
| Failure Family | `SVR` |
| Failure Stage | dataset bundle build |
| Trigger | legacy runner expects `paths.source_dataframe_path` |
| Current YAML Surface | `paths.dataset_config_path` |

## Repair Objective

Produce one fully working remote micro-campaign execution over the `10`
prepared family runs, using the original-dataset validation workflow that
reads from `data/datasets`.

## Execution Policy

| Policy | Value |
| --- | --- |
| Launch Mode | remote only |
| Diagnostic Scope | current forward-only micro-campaign |
| Total Runs | `10` |
| Attempts Per Family | `1` |
| Dataset Root | `data/datasets` |
| Direction | `forward` |
| Scientific Promotion During Bringup | forbidden |

## Repair Steps

1. fix the runner mismatch in the local/remote launch path;
2. re-prepare the micro-campaign if the launcher contract changes;
3. rerun the remote micro-campaign;
4. fix any newly exposed remote failure until the `10` runs complete;
5. only after clean completion, hand the exact launch command back to the
   user for independent operator validation.

## Success Gate

The repaired micro-campaign is accepted only if all of the following become
true in one remote execution:

1. all `10` family runs start;
2. all `10` family runs complete;
3. validation bundles materialize locally after sync;
4. no runner-schema mismatch remains;
5. no unresolved remote launcher crash remains.
