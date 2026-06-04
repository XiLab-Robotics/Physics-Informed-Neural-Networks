# Track 2F-Bis Harmonic-Offset Probe Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the proposed `Track 2F-bis`
harmonic-offset probe without launching training.

The completed `Track 2F` `sequential_residual_offset_probe` campaign showed
that a clean causal non-harmonic residual-offset model is execution-valid, but
it does not force TE waveform shape through harmonic or periodic structure.
The next probe should therefore compare that clean baseline against an
explicit harmonic-offset model that separates shape and offset while preserving
the same causal runtime input boundary.

Training must not start until this planning report and the matching technical
document are explicitly approved.

## Baseline And Verification Rule

`Track 2` remains the official offline curve-first verification surface.
`Track 2F-bis` candidates must not be accepted from scalar training metrics
alone. Any promoted result must later refresh:

- the direction-aware `Track 2` matrix;
- the curve-first reranking report and PDF;
- the mean-offset diagnostics where relevant;
- the best-model collage report and PDF;
- the multi-model curve comparison report and PDF;
- the family and program registries;
- `Training Results Master Summary.md`.

The campaign keeps the repository direction rule:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

## Candidate Matrix

The first `Track 2F-bis` package should compare two intervention types across
the three required surfaces:

| Intervention | Direction Surfaces | Candidate Count | Initial Role |
| --- | --- | ---: | --- |
| `clean_sequential_residual_offset_control` | `global`, `Fw`, `Bw` | 3 | non-harmonic Track 2F-like control branch |
| `harmonic_residual_offset_probe` | `global`, `Fw`, `Bw` | 3 | explicit harmonic shape branch plus causal residual-offset branch |

The campaign therefore contains `6` runnable training entries. It is
deliberately smaller than a full wave because the goal is to isolate whether
explicit harmonic shape preservation fixes the curve-shape loss observed in
the clean Track 2F branch.

## Model Design

The clean control branch should reuse the existing
`sequential_residual_offset_probe` architecture and the same causal sequence
input structure. It provides the baseline without forced harmonics.

The new harmonic-offset branch should add one narrow model type, tentatively
named `harmonic_residual_offset_probe`, with this structure:

```text
final_te_prediction =
  structured_harmonic_shape_prediction
  + causal_residual_offset_prediction
```

The structured branch should reuse `HarmonicRegression`. The first campaign
should use the sparse `RCIM` harmonic list by default because Wave 2C showed
that sparse harmonic structure remained more credible than broad dense
expansion for curve-level behavior.

The residual-offset branch should reuse the unidirectional recurrent readout
pattern already validated by `SequentialResidualOffsetNetwork`. Any
bidirectional diagnostic run must remain out of this first deployable probe.

## Runtime Input Boundary

The campaign must preserve the practical deployment constraint:

- input features are current point-level operating state, supported short
  causal history, or causal derived features;
- direction, speed, torque, oil temperature, and angular position may be used
  when available at runtime;
- future TE values, full-curve means, complete-curve normalization, and
  future-looking smoothing are forbidden as model inputs;
- full curves are allowed only after inference for validation, diagnostics,
  and promotion decisions.

## Prepared Configuration Surface

The approved implementation should prepare a new campaign root:

```text
config/training/track2f_bis_harmonic_offset_probe/
```

Expected campaign profile:

- `campaign_profile=track2f_bis_harmonic_offset_probe`

Expected intervention selections:

- `intervention=clean_sequential_residual_offset_control`
- `intervention=harmonic_residual_offset_probe`

Expected direction selections:

- `direction=global`
- `direction=fw`
- `direction=bw`

The implementation should reuse existing sequence dataset profiles where
possible. Any new dataset wrapper must only expose causal inputs and must be
documented before training.

## Execution Gate

Before launch, the approved campaign package must contain:

- materialized queue YAML files for all `6` candidates;
- any required direction-specific dataset variant YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/track2/`;
- a launcher note under `doc/scripts/campaigns/track2/`;
- an updated `doc/running/active_training_campaign.yaml`;
- both local and `-Remote` launch commands.

The expected local launch command after approved preparation is:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1
```

The expected remote launch command after approved preparation is:

```powershell
.\scripts\campaigns\track2\run_track2f_bis_harmonic_offset_probe_campaign.ps1 -Remote
```

No training execution is approved by this report alone.

## Verification Plan

Before campaign execution:

- confirm the campaign state is `prepared`;
- validate all materialized YAML files;
- run Python compile checks for touched model and campaign scripts;
- run focused one-batch validation for the new model type;
- run a fast-dev smoke check for at least one harmonic-offset entry;
- run Markdown QA on touched authored documentation;
- provide the exact local and remote launcher commands.

After campaign execution:

- inspect `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- preserve separate `global`, `Fw`, and `Bw` branch candidates;
- refresh family-level and program-level registries only through the
  established workflow;
- refresh `Training Results Master Summary.md`;
- close out the campaign with Markdown and validated PDF deliverables;
- propose the optional heavy `Track 2` refresh as a separate
  operator-launched step.

## Decision Criteria

Carry forward the harmonic-offset branch if:

- it improves Track 2 curve shape versus the matching clean baseline on the
  same `global`, `Fw`, or `Bw` surface;
- raw error does not improve only by masking centered-shape, amplitude, or
  phase degradation;
- the structured branch remains interpretable and the residual branch remains
  causal.

Carry forward the clean branch if:

- a new objective, index, or training setup improves it without requiring
  harmonic forcing;
- it remains a stronger control for future composite-loss comparisons than the
  first Track 2F run.

Do not promote either branch if:

- the only gain is scalar `test_mae` without Track 2 curve-level support;
- the gain depends on future curve information unavailable at runtime;
- `global`, `Fw`, and `Bw` are collapsed into one scalar winner.
