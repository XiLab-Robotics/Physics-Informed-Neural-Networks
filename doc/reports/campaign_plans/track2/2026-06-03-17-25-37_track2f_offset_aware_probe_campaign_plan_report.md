# Track 2F Offset-Aware Probe Campaign Plan Report

## Executive Summary

This preliminary campaign plan prepares the proposed `Track 2F`
offset-aware probe without launching training.

`Track 2D` decomposed full-matrix curve error into raw error, curve offset,
centered-shape error, amplitude error, and harmonic phase error. `Track 2E`
then showed that the offset is partly predictable from conservative causal
condition groupings, with `direction_torque` as the strongest aggregate signal
after excluding exact full-condition memorization.

The planned campaign is intentionally small. It should test whether
offset-aware compensation is worth turning into a larger model-family branch
before opening a full wave.

Training must not start until this planning report and the matching technical
document are explicitly approved.

## Baseline And Verification Rule

`Track 2` remains the official offline verification surface. `Track 2F`
candidates must not be accepted from training metrics alone. Any promoted
result must later refresh:

- the direction-aware `Track 2` matrix;
- the curve-first reranking report and PDF;
- the mean-offset / offset-predictability diagnostic reports where relevant;
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

The first probe should compare three intervention types across the three
parallel surfaces:

| Intervention | Direction Surfaces | Candidate Count | Initial Role |
| --- | --- | ---: | --- |
| `posthoc_direction_torque_offset_baseline` | `global`, `Fw`, `Bw` | 3 | non-learned causal aggregate offset benchmark |
| `sequential_residual_offset_probe` | `global`, `Fw`, `Bw` | 3 | second-stage causal offset / low-frequency residual predictor |
| `multi_head_shape_offset_probe` | `global`, `Fw`, `Bw` | 3 | shared causal trunk with separate centered-shape and offset heads |

The planned first package therefore contains `9` candidate runs or runnable
validation entries. If the post-hoc baseline is implemented as a validation
entry rather than a trainable run, it must still be represented in the
campaign output and leaderboard so the learned probes are compared against a
simple causal baseline.

## Starting Candidates

The probe should use the completed `Track 2E` recommendations as starting
evidence, not as automatic best-model promotions:

| Surface | Track 2E Probe Reference | Reason |
| --- | --- | --- |
| `global` | `harmonic_regression_global` | largest conservative offset-correction gain, but still amplitude/phase limited |
| `Fw` | `LGBM19_Fw` | strongest forward sequential-offset feasibility probe |
| `Bw` | `rcim_retuned_XGBM19_Bw` | strongest backward sequential-offset feasibility probe |

The implementation may choose repository-owned neural starting candidates
where model export or training integration makes the exact Track 2E reference
unavailable. If that happens, the deviation must be documented in the prepared
campaign package and the report must keep the Track 2E reference as the
diagnostic comparator.

## Runtime Input Boundary

The campaign must preserve the practical deployment constraint:

- input features are current point-level operating state, supported short
  causal history, or causal derived features;
- `direction`, speed, torque, and oil temperature may be used when available
  at runtime;
- future TE values, full-curve means, complete-curve normalization, and
  future-looking smoothing are forbidden as model inputs;
- full curves are allowed only after inference for validation, diagnostics,
  and promotion decisions.

## Prepared Configuration Surface

The approved implementation should prepare a new campaign root:

`config/training/track2f_offset_aware_probe/`

Expected campaign profile:

- `campaign_profile=track2f_offset_aware_probe`

Expected intervention selections:

- `intervention=posthoc_direction_torque_offset_baseline`
- `intervention=sequential_residual_offset_probe`
- `intervention=multi_head_shape_offset_probe`

Expected direction selections:

- `direction=global`
- `direction=fw`
- `direction=bw`

The implementation should reuse existing dataset and sequence profiles where
possible. Any new dataset wrapper must only expose causal inputs and must be
documented before training.

## Execution Gate

Before launch, the approved campaign package must contain:

- materialized queue YAML files or validation entries for all `9` candidates;
- any required direction-specific dataset variant YAML files;
- a dedicated PowerShell launcher under `scripts/campaigns/track2/`;
- a launcher note under `doc/scripts/campaigns/track2/`;
- an updated `doc/running/active_training_campaign.yaml`;
- both local and `-Remote` launch commands.

The expected local launch command after approved preparation is:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1
```

The expected remote launch command after approved preparation is:

```powershell
.\scripts\campaigns\track2\run_track2f_offset_aware_probe_campaign.ps1 -Remote
```

No training execution is approved by this report alone.

## Verification Plan

Before campaign execution:

- confirm the campaign state is `prepared`;
- validate all materialized YAML files or validation entries;
- run focused smoke checks for any new offset-aware model or loss components;
- run Markdown QA on touched authored documentation;
- provide the exact local and remote launcher commands.

After campaign execution:

- inspect `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and
  `campaign_best_run.md`;
- update family-level and program-level best-result registries only when the
  result is promoted through the established workflow;
- refresh `Training Results Master Summary.md`;
- close out the campaign with Markdown and validated PDF deliverables;
- propose the optional heavy `Track 2` refresh as a separate
  operator-launched step.

## Decision Criteria

The probe is successful only if it clarifies the next branch.

Carry forward a sequential residual-offset branch if:

- the sequential probe beats the post-hoc `direction_torque` baseline on raw
  curve error;
- centered-shape error does not regress materially;
- the gain appears on the matching `Fw`, `Bw`, or `global` surface rather than
  only in a pooled scalar metric.

Carry forward a multi-head shape/offset branch if:

- the multi-head probe improves raw error while also reducing centered-shape,
  amplitude, or phase limitations;
- the offset head remains interpretable and does not require non-causal curve
  inputs.

Do not carry forward an offset-first branch if:

- the post-hoc baseline is stronger than the learned probes;
- offset correction improves raw error but worsens shape, amplitude, or phase;
- the only strong signal depends on exact full-condition memorization.
