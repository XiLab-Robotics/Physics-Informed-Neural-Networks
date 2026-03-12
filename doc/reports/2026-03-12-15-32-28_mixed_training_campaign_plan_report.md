# Mixed Training Campaign Plan Report

## Overview

This report defines the next planned feedforward training campaign after the first comparative study on:

- `trial`
- `baseline`
- `high_density`
- `high_epoch`
- `high_compute`

The previous campaign already established one important result:

- increasing optimization time helped more than increasing point density alone.

The new campaign is therefore designed to test **mixed combinations**, not isolated one-factor changes.

The specific objective is to understand whether the next meaningful gain comes from:

1. combining the long schedule with denser point sampling;
2. increasing the effective batch size for the denser variants;
3. increasing model capacity only after the data and schedule become stronger.

This document is intentionally written as a planning report, not as an execution report. No new runs are assumed completed yet.

## Why This Plan Makes Sense

The previous results suggest the following interpretation:

- `high_epoch` was the strongest configuration;
- `high_density` improved validation slightly but not test;
- `high_compute` was good but did not beat `high_epoch`.

That pattern suggests the current bottleneck is not simply:

- "use more points";

and not simply:

- "make the network bigger".

The more plausible hypothesis is:

- the model benefits from longer optimization,
- but the value of denser point sampling depends on how the schedule, batch regime, and model capacity interact.

That is why the next campaign should be structured around combinations.

## Main Variables To Control

The new campaign focuses on four levers.

### 1. Point Density

Controlled through `point_stride`.

The density levels worth testing are:

- `10`
- `5`
- `1`

Reason:

- `10` is the mild dense regime already partially explored;
- `5` is a stronger dense regime;
- `1` means full-point usage and answers the obvious question: what happens if no point is skipped?

### 2. Optimization Depth

The campaign should inherit the stronger schedule logic from `high_epoch`:

- `min_epochs: 20`
- `max_epochs: 250`
- `patience: 35`

Reason:

- this is the best reference discovered so far;
- it isolates density/batch/model effects on top of the currently best schedule backbone.

### 3. Effective Batch Regime

The campaign should test both:

- conservative batch sizes;
- larger batch sizes.

Important constraint:

- the larger batch should be larger **relative to the same density case**,
- not necessarily identical across all densities.

For example:

- a large batch at `stride=10` can be much larger than a large batch at `stride=1`,
- because `stride=1` is much more memory-expensive.

This is important to keep the plan realistic rather than artificially uniform.

### 4. Model Capacity

The campaign should compare:

- standard MLP: `128-128-64`
- larger MLP: `256-256-128-64`

Reason:

- the previous `high_compute` run already suggests that larger capacity is not automatically the winner;
- but it may become more useful once the data density and batch regime are also strengthened.

## What Should Stay Fixed

To keep the campaign interpretable, these items should remain fixed across the matrix unless a concrete blocker appears:

- same dataset split logic;
- same train/validation/test proportions;
- same feature set (`input_size = 5`);
- same target definition;
- same optimizer family (`AdamW`);
- same output/logging workflow;
- same held-out test evaluation logic.

This keeps the campaign focused on the intended questions.

## Primary Campaign Matrix

The most defensible primary matrix is a `3 x 3` grid:

- 3 density levels
- 3 execution phases

That gives `9` runs total.

## Phase Definitions

### Phase 1

Goal:

- test density on top of the best current schedule,
- without changing the model size,
- with conservative batch choices.

### Phase 2

Goal:

- test whether the denser variants benefit from a larger batch regime,
- still keeping the model at standard size.

### Phase 3

Goal:

- test whether the denser variants benefit from larger model capacity **after** density and batch have already been strengthened.

## Proposed Run Table

| Run ID | Planned Name | Phase | Point Stride | Curve Batch Size | Hidden Layers | Learning Rate | Epoch Range | Patience | Main Question |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | ---: | --- |
| 1 | `stride10_long` | 1 | 10 | 4 | 128-128-64 | 0.0010 | 20-250 | 35 | Does mild dense sampling beat the current high-epoch winner when schedule is held strong? |
| 2 | `stride5_long` | 1 | 5 | 2 | 128-128-64 | 0.0010 | 20-250 | 35 | Does a denser regime help if we still keep batch conservative? |
| 3 | `stride1_long` | 1 | 1 | 1 | 128-128-64 | 0.0010 | 20-250 | 35 | What happens if we use all points with the safest batch size? |
| 4 | `stride10_long_large_batch` | 2 | 10 | 8 | 128-128-64 | 0.0010 | 20-250 | 35 | Does smoother optimization help the stride-10 regime? |
| 5 | `stride5_long_large_batch` | 2 | 5 | 4 | 128-128-64 | 0.0010 | 20-250 | 35 | Does larger batch unlock the denser stride-5 regime? |
| 6 | `stride1_long_large_batch` | 2 | 1 | 2 | 128-128-64 | 0.0010 | 20-250 | 35 | Is full-density training still stable with a higher effective batch? |
| 7 | `stride10_long_large_batch_big_model` | 3 | 10 | 8 | 256-256-128-64 | 0.0007 | 20-250 | 35 | Does extra capacity help when stride-10 already has long schedule and larger batch? |
| 8 | `stride5_long_large_batch_big_model` | 3 | 5 | 4 | 256-256-128-64 | 0.0007 | 20-250 | 35 | Does extra capacity become useful at stronger density? |
| 9 | `stride1_long_large_batch_big_model` | 3 | 1 | 2 | 256-256-128-64 | 0.0007 | 20-250 | 35 | Is the most data-rich and capacity-rich feedforward setup actually worth the cost? |

## Why These Batch Sizes

The batch sizes above are not arbitrary.

They are chosen so that:

- `stride10` explores the most aggressive batch among the three density levels;
- `stride5` remains clearly heavier than the old baseline but still realistic;
- `stride1` does not become reckless from the beginning.

The plan intentionally does **not** force one identical batch size across all densities.

That would be less meaningful because:

- the memory cost of `stride=1` is fundamentally different from `stride=10`;
- a fake uniform rule would mainly test memory limits rather than model behavior.

## Why The Learning Rate Changes For The Big Model

The larger model variants use:

- `learning_rate = 0.0007`

instead of:

- `0.0010`

Reason:

- the previous heavier run selected an early best checkpoint;
- a slightly smaller learning rate is a reasonable way to stabilize the larger-capacity model without changing the optimizer family.

This is not guaranteed to be optimal, but it is a technically defensible starting point.

## Alternative Roads Worth Considering

The 9-run grid is the main plan. Still, a few alternative strategies are worth documenting before execution.

### Alternative A - Stop After Phase 1 If Full-Density Is Clearly Unfavorable

If `stride1_long` is:

- much slower,
- not more accurate,
- or unstable,

then it may not be worth continuing all the way to the full `stride1` phase-2 and phase-3 variants.

This would reduce wasted compute.

### Alternative B - Use Gradient Accumulation Instead Of Larger Batch

Instead of increasing `curve_batch_size` directly, another path is:

- keep the conservative batch;
- increase effective batch through gradient accumulation.

Why this may help:

- lower memory risk;
- easier to scale the `stride1` case.

Why it is not the default first choice:

- it adds one more training knob;
- it complicates the interpretation of the first mixed campaign.

### Alternative C - Curriculum Density

Another scientifically meaningful path is:

1. train first with `stride10`,
2. then resume from checkpoint with `stride5`,
3. then optionally resume with `stride1`.

Why this may help:

- cheaper early training;
- denser data only in the later refinement stage.

Why it is not the default first choice:

- it changes the experiment type from direct comparison to staged optimization;
- it is better tested after the direct matrix is understood.

### Alternative D - Multi-Seed On Only The Best Two Configs

If compute budget is limited, another pragmatic alternative is:

- run fewer configurations,
- but repeat the strongest two with multiple seeds.

This gives stronger statistical confidence at lower grid size.

## Recommended Execution Order

The most sensible order is:

1. Phase 1 first
2. Phase 2 second
3. Phase 3 third

Within each phase:

1. `stride10`
2. `stride5`
3. `stride1`

Why:

- lower-risk runs first;
- earlier warning if denser regimes are not paying off;
- easier to stop intelligently before spending full compute on the most extreme variants.

## What We Expect To Learn

This campaign should answer these concrete questions:

1. Does `high_epoch` remain the winner once density is increased under the same long schedule?
2. Is `point_stride=1` actually useful, or mostly expensive?
3. Is the best next gain coming from:
   - full-density data,
   - larger batch,
   - larger model,
   - or only from longer schedules?
4. At what point does added compute stop paying for itself?

## Practical Recommendation Before Execution

The current plan is strong enough to execute, but there is one reasonable decision point before launching all `9` runs:

- decide whether the campaign should be run fully,
- or whether it should be run with a stop-rule after Phase 1.

My recommendation is:

- prepare all `9` configs,
- but keep the right to stop after Phase 1 if `stride1_long` is clearly dominated.

That keeps the plan ambitious while still technically disciplined.
