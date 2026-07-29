# Wave 5.2R Stage 8 Weak Forward Compliance Priors Campaign Plan

## Overview

This plan authorizes a bounded forward-only screen of progressively stronger
compliance priors above the qualified Stage 5 H04 component. It is designed to
falsify whether the Phase 3 positive compliance signal carries incremental
predictive information when the prior is weaker, support-aware, and explicitly
compared with shuffled and hard-equation controls.

The campaign is approved under the user's twenty-four-hour blanket approval
recorded at `2026-07-29T15:30:41+02:00`.

## Fixed Contract

- dataset: `polished_dataset`;
- inputs: causal setpoints only;
- surface: `Fw`;
- train, validation, test split: `675 / 194 / 97`;
- angular samples: `2048`, uniform and endpoint-excluded;
- first-screen seed: `314159`;
- conditional stability seeds: `271828`, `161803`;
- qualified incoming component: Stage 5 H04;
- official TE Curve Verification Pipeline: excluded from normal closeout.

## Scientific Hypotheses

1. The sign of forward torque-to-mean response is more robust than a single
   exact stiffness value.
2. A broad training-supported derivative interval is less misspecified than
   the Phase 3 fixed compliance equation.
3. Confidence weighting can avoid forcing the prior in sparse operating
   regions.
4. Delayed or adaptive activation can preserve data-fit convergence while
   adding a useful mechanism bias.
5. A shuffled-torque prior should fail if the true ordering carries
   incremental information.
6. A hard elastic equation should reproduce the earlier underfit and serves as
   a negative control.

## Candidate Matrix

| ID | Candidate | Physics weight | Control role |
| --- | --- | ---: | --- |
| `D00` | frozen H04 diagnostic | `0` | immutable baseline |
| `C00` | H04 data-only fine-tune | `0` | matched trainable control |
| `S01` | sign-only prior | bounded | weakest physics-guided arm |
| `B01` | broad derivative interval | bounded | interval arm |
| `W01` | confidence-weighted interval | bounded | support-aware arm |
| `T01` | temperature-stratified interval | bounded | conditional arm |
| `A01` | delayed interval activation | bounded schedule | curriculum arm |
| `R01` | adaptive weak-prior weighting | bounded adaptive | optimization arm |
| `N01` | shuffled-torque sign prior | matched to `S01` | specificity control |
| `H01` | hard compliance equation | architectural | misspecification control |

The planned first screen contains ten candidates, including the immutable D00
evaluation. Stability adds two seeds per qualifying trainable candidate only.

## Training-Only Bootstrap

The preflight must:

- use training curves only;
- establish torque-mean sign support under speed and temperature controls;
- compute conservative derivative quantiles and effective-stiffness summaries;
- quantify bootstrap sign frequency;
- compute temperature-band intervals only where support is sufficient;
- build confidence weights from train-condition density;
- compare with a deterministically shuffled-torque distribution;
- persist all random seeds and hashes.

No validation or test mean may set a loss sign, bound, weight, or schedule.

## Optimization Contract

- initialize from the qualified H04 checkpoint or reproduce its exact output;
- preserve the H04 coefficient orders and bounded correction path;
- use the Stage 2 named-loss and gradient-interaction instrumentation;
- cap compliance weights and adaptive multipliers;
- record early stopping and best-checkpoint selection on validation data;
- prevent full held-out curves from becoming runtime features;
- write immutable timestamped `run_instance_id` directories.

## First-Screen Gate

A candidate qualifies for stability only if it:

- beats frozen H04 and C00 on raw MAE;
- improves absolute curve-mean error;
- preserves or improves centered-shape MAE;
- preserves derivative, amplitude, phase, closure, and P95 gates;
- beats N01 when the formulation has a matched shuffled control;
- remains finite and causal;
- does not merely reduce its own compliance loss;
- does not saturate its derivative interval or correction bounds.

## Stability And Promotion Gate

Every qualifying formulation must pass the same gate for all three seeds.
Parameter stability is reported separately from predictive stability.

No Stage 8 model replaces the accepted periodic GRU or becomes a production
candidate through this campaign alone. A passing formulation becomes an
isolated structured ingredient eligible for later stages and the Stage 14
tournament.

## Required Artifacts

- technical document and this planning report;
- training-only bootstrap report and machine-readable summary;
- model explanatory report;
- campaign and queue YAML;
- local and `-Remote` PowerShell launcher;
- launcher note with exact commands;
- protected campaign state;
- per-run checkpoints, histories, metrics, and full-curve payloads;
- campaign leaderboard and explicit best-run artifacts;
- closeout gate summary;
- campaign-results Markdown and validated PDF;
- synchronized roadmap, backlog, ledger, master summaries, usage guide, and
  Sphinx API.

## Launch Commands

The dedicated launcher must expose:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Run
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Remote -PreflightOnly
.\scripts\campaigns\wave_5_2\run_wave52r_stage8_weak_forward_compliance_priors.ps1 -Remote -Run
```

The `-Remote` path must use the repository-owned remote campaign
infrastructure and synchronize source, configuration, documentation, outputs,
registries, campaign state, and status artifacts.

## Stop Rules

Stop a branch when:

- train-only bootstrap sign support is insufficient;
- the prior performs no better than shuffled torque;
- the physical loss improves while predictive gates regress;
- compliance gradients consistently oppose raw, mean, or shape objectives;
- one of three seeds fails;
- bounds or hard equations produce saturation or cancellation;
- the formulation requires unavailable history, contact, clearance, force, or
  stiffness inputs.

The campaign may close as a valid negative result.
