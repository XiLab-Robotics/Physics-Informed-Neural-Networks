# Wave 5.2R Integrated Specialist Model Campaign Plan

## Campaign Status

- Campaign: `wave52r_integrated_specialist_model_2026_08_02`
- Technical document: approved
- Campaign plan: approved on `2026-08-03T17:15:01+02:00`
- Training: authorized through the dedicated operator launcher; not started
- Dataset and inputs: `polished_dataset + setpoints`
- Surfaces: separate `Fw`, `Bw`, and direction-aware `global`
- Seeds: `314159`, `271828`, and `161803`
- Maximum run count: `24`

This is an empirical Wave 5.2R ablation campaign. It is not a PINN campaign,
does not reopen Wave 6, and cannot change accepted registries or deployment
status automatically.

## Objective

The campaign tests whether bounded, inspectable specialist residuals add
balanced incremental value above frozen K01 without importing the known H08,
H04, Stage 12, or Stage 10 defects. K01 remains the causal temporal baseline.
H08 is available only as a mean-centered forward specialist and is exactly
zero on backward records.

The primary decision is whether to retain K01 alone or qualify one or more
empirical specialist branches for a later, separate TE Curve Verification
Pipeline review. Campaign scalar rank is never sufficient for promotion.

## Frozen Evidence And Inputs

The campaign replays the selected K01 seed `271828` on `Fw`, `Bw`, and
`global`, the matched H04 anchors, and the selected forward H08 seed `161803`.
Their paths are frozen in `campaign.yaml`, hashed during every preflight, and
synchronized to the remote workstation by the dedicated launcher.

The global dataset retains the official grouped split signature
`c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`.
It contains explicit direction and preserves independent `Fw`, `Bw`, and
`global` reporting. All normalization, gates, and learned coefficients use
training data only. The test split is evaluated once after checkpoint and
branch selection are frozen.

## Architecture Contract

The implementation starts from exact K01 replay:

```text
prediction = frozen_k01
           + bounded_forward_h08_centered_residual
           + bounded_h04_or_learned_shape_residual
           + bounded_condition_interaction_residual
```

Each contribution is exposed separately. The H08 curve is mean-centered
before use, its `a0` channel is absent, and a deterministic direction gate
forces its contribution to zero on `Bw`. Learned shape and condition branches
use fixed sine/cosine bases and fixed-size tensor operations suitable for a
later PLC-oriented export path.

The campaign predeclares the global direction-aware K01 checkpoint as the
specialist attachment topology because it has official cross-surface evidence,
one explicit direction input, one checkpoint/state path, and lower initial PLC
routing complexity. Deterministically routed directional K01 checkpoints are
replayed as `A00D` before specialist training and remain visible as the
topology control. Validation scalar rank cannot silently switch the topology;
any later replacement requires direction-separated multi-index, state, export,
and PLC-cost review.

## Ablation Matrix

| ID | Role | Trained runs | Advancement rule |
| --- | --- | ---: | --- |
| `A00` | Frozen global K01 replay | 0 | Baseline control |
| `A00D` | Routed `Fw`/`Bw` K01 replay | 0 | Topology control |
| `A01` | Decomposed K01 identity replay | 0 | Exact numerical identity |
| `A02` | Forward-only centered H08 branch | 3 | Phase specialty plus non-regression |
| `A03` | H04 centered analytical control | 3 | Shape specialty plus non-regression |
| `A04` | F01-derived centered-shape objective | 3 | Shape specialty plus non-regression |
| `A05` | Stage 12 S01-derived harmonic/closure objective | 3 | Closure specialty plus non-regression |
| `A06` | Stage 10 R00 dense condition library | 3 | Raw-error specialty plus non-regression |
| `A07` | Stage 10 S01 thresholded control | 3 | Raw-error specialty plus non-regression |
| `A08` | Passed branches only | 0 or 3 | Runs only when at least one branch passes two seeds |

The single-branch screen always contains `18` trained runs. `A08` adds three
conditional runs, giving a maximum campaign size of `24` entries including
the three replay controls.

## Training And Selection Contract

Each trainable arm uses AdamW for at most `40` epochs with learning rate
`0.001`, weight decay `0.00001`, curve batches of `32`, gradient clipping at
`1.0`, and validation-only checkpoint selection. All branch heads start at
zero so training begins from exact K01 replay.

The branch-specific objectives are:

- `A02`, `A03`, `A06`, and `A07`: raw error, centered shape, and bounded
  correction;
- `A04`: stronger centered-shape weighting derived from the Stage 12 F01
  hypothesis;
- `A05`: centered shape, retained harmonic error, and periodic closure terms
  derived from the Stage 12 S01 hypothesis.

No failed Stage 12 checkpoint is imported as a qualified expert. Stage 10
S01 remains a thresholded negative control and is never described as an
identified sparse law.

## Predeclared Acceptance Gates

A branch must improve its declared validation specialty by at least `1%`
relative to `A01`. It must also remain within `1%` of `A01` on all of:

- raw MAE;
- absolute mean-offset error;
- centered-shape MAE;
- peak-to-peak absolute error;
- per-curve MAE P95.

At least two of three seeds must pass before a branch enters `A08`. The final
report must additionally separate raw, shape, offset, robustness, harmonic,
phase, closure, correction-bound, routing, and deployment evidence across
`Fw`, `Bw`, and `global`. Any scalar leaderboard remains provisional.

## Mandatory Runtime And Negative Controls

Preflight requires exact `A01` versus K01 identity and an exactly zero H08
contribution on a backward record. Campaign artifacts must retain the global
and routed K01 controls, H04 control, dense and thresholded Stage 10 arms, and
the simpler passing parent beside any integrated result.

Later acceptance must also cover deterministic replay, reset, causal prefix,
state carry, non-overlapping 32-sample chunk behavior, direction transition,
invalid-input fallback, saturation, export parity, latency, and package size.
The present campaign can produce offline evidence only; it cannot establish a
TwinCAT build, TF3820 activation, ADS operation, or commissioned runtime.

## Expected Artifacts

The runner writes immutable outputs under:

- `output/training_runs/integrated_specialist_models/<run_instance_id>/`;
- `output/training_campaigns/<campaign_run_instance_id>/`;
- `output/validation_checks/wave52r_integrated_specialist_model/`.

The campaign root must contain `campaign_results.csv`,
`branch_gate_summary.yaml`, `campaign_leaderboard.yaml`,
`campaign_best_run.yaml`, `campaign_best_run.md`,
`campaign_artifact_path_list.txt`, and `campaign_state.yaml`. The winner is
explicit but remains a provisional validation winner.

## Resource Estimate

The frozen expert replay loads three K01 checkpoints, three H04 checkpoints,
and one forward H08 checkpoint. The learned heads are small, but every run
evaluates `2048`-sample curves. The expected workload is `18` mandatory and
up to `3` conditional trained runs. A CUDA workstation is preferred; local
CPU execution remains supported but is expected to be materially slower.

## Launcher Contract

Preflight without training:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -PreflightOnly
```

Remote preflight without training:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Remote -PreflightOnly
```

Local training, only after explicit approval of this report:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Run
```

Remote training, only after explicit approval of this report:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_integrated_specialist_model.ps1 `
  -Remote -Run
```

The remote path synchronizes source, configuration, documentation, split
evidence, and frozen checkpoints before execution. It returns preflight
evidence and, after a run, campaign outputs, per-run artifacts, queue outcome,
and persistent campaign state.

## Closeout Boundary

After the user runs the campaign and reports completion, normal closeout must
inspect every required artifact, create the campaign-results Markdown and
validated styled PDF, synchronize registries and status where evidence
requires it, and preserve incumbents unless separately accepted.

The heavy TE Curve Verification Pipeline is not part of this campaign. It may
be proposed only after normal closeout as a separate operator-run local or
remote step.

## Approval Record

The user explicitly approved this planning report on
`2026-08-03T17:15:01+02:00`. The manifest and persistent state therefore use
`campaign_plan_status: approved`. Local and remote `-Run` paths are enabled,
but campaign execution remains an operator action and has not started.
