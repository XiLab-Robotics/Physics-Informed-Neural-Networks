# Wave 1 Residual Harmonic Family Campaign Plan Report

## Overview

This report defines the first `Wave 1` follow-up family-specific
hyperparameter optimization campaign.

The target family is:

- `residual_harmonic_mlp`

This is the correct first family to optimize deeply because the completed Wave 1
recovery campaign established two important facts:

1. the best recovered residual configuration is the strongest recovered
   structured-neural candidate;
2. the global program leader is still a tree model, which means the residual
   family now deserves a serious best-training search rather than another broad
   baseline-only comparison.

The current residual reference winner is:

- `te_residual_h12_small_joint_recovery`

with:

- validation MAE: `0.003016 deg`
- validation RMSE: `0.003534 deg`
- test MAE: `0.003466 deg`
- test RMSE: `0.003967 deg`

This campaign is intentionally broader than the earlier feedforward
best-training pass. The user explicitly requested an aggressive search posture,
and the current family ranking justifies spending meaningful budget on the
residual harmonic branch before making the next cross-family decision.

## Why This Plan Makes Sense

The current residual baseline already shows the right qualitative behavior:

- the residual family is far stronger than the harmonic-only baselines;
- joint optimization is already slightly better than the frozen structured
  branch;
- the structured branch still exposes interpretable branch-level diagnostics,
  which keeps the family attractive in the project context.

At the same time, the current residual reference is still only one narrow local
configuration:

- harmonic order `12`;
- residual widths `64-64`;
- dropout `0.10`;
- layer norm enabled;
- learning rate `0.0010`;
- weight decay `0.0001`;
- point stride `5`;
- batch size `4`;
- epoch budget `20-250`;
- patience `35`.

That is a good anchor, but not yet a strong estimate of the family ceiling.

The next step should therefore test three kinds of questions separately:

1. does the family prefer a different structured backbone regime;
2. does the residual branch need more or less capacity and regularization;
3. does the family improve further when the optimization/data regime is pushed
   harder.

## Main Variables To Control

The campaign should focus on the residual-family levers that are already
supported by the current repository configuration schema.

### 1. Structured Backbone Mode

Controlled through:

- `freeze_structured_branch`
- `harmonic_order`

Reason:

- the Wave 1 recovery run showed a small but consistent advantage for the joint
  branch;
- that does not yet prove the frozen mode is globally inferior across broader
  settings;
- harmonic order directly changes how much periodic structure is delegated to
  the explicit branch before the residual MLP must compensate.

### 2. Residual Branch Capacity

Controlled through:

- `residual_hidden_size`

Reason:

- the current `64-64` branch may be underpowered;
- it may also already be near the sweet spot, in which case larger models would
  only add runtime and variance;
- this family needs explicit width/depth evidence rather than intuition.

### 3. Residual Regularization

Controlled through:

- `residual_dropout_probability`
- `residual_use_layer_norm`
- `weight_decay`

Reason:

- the residual branch is learning a correction term on top of an explicit
  structured backbone;
- too little regularization may overfit the residual;
- too much regularization may suppress exactly the nonlinear correction the
  family is supposed to learn.

### 4. Optimization Regime

Controlled through:

- `learning_rate`
- `max_epochs`
- `patience`

Reason:

- the current schedule is good, but still inherited from baseline decisions
  rather than optimized for this family;
- the residual branch may benefit from a slightly slower but longer schedule;
- the family may also respond differently to patience than a plain feedforward
  network because the structured branch already reduces the effective learning
  burden.

### 5. Data Density And Effective Batch

Controlled through:

- `point_stride`
- `curve_batch_size`

Reason:

- the residual family may benefit from denser curve sampling because the
  harmonic branch already captures large-scale periodic structure and the
  residual branch can then focus on smaller deviations;
- but denser sampling also increases runtime and may not be worth it if the
  structured branch already absorbs most of the periodic signal.

## What Should Stay Fixed

To keep this campaign interpretable, the following should remain fixed across
the matrix unless a concrete implementation blocker appears:

- same dataset root and split logic;
- same feature set (`input_size = 5`);
- same regression target definition;
- same output/logging workflow;
- same test-set evaluation logic;
- same runtime precision (`32`);
- same accelerator auto-resolution path;
- same random seed for the first pass (`42`).

The first `Wave 1` follow-up campaign should prioritize configuration-space
coverage over
multi-seed repetition. Multi-seed confirmation should be a second-step campaign
after the family champion is identified.

## Primary Campaign Matrix

The main plan is a `15`-run matrix split into three phases.

This is large enough to be informative without collapsing into an undisciplined
full Cartesian explosion.

## Phase Definitions

### Phase 1 - Structured Branch Regime

Goal:

- determine whether the best residual direction still centers on the joint mode;
- test whether harmonic order should stay at `12` or move lower/higher.

### Phase 2 - Residual Capacity And Regularization

Goal:

- test whether the family wants a larger residual branch, lower dropout, higher
  dropout, or different normalization behavior.

### Phase 3 - Optimization And Data Regime

Goal:

- test whether the strongest residual architecture improves further under denser
  data or a stronger optimization schedule.

## Proposed Run Table

| Run ID | Planned Name | Phase | Freeze Structured | Harmonic Order | Residual Hidden Size | Dropout | Layer Norm | Point Stride | Curve Batch | Learning Rate | Epoch Range | Patience | Main Question |
| --- | --- | --- | --- | ---: | --- | ---: | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | `residual_h08_small_frozen` | 1 | yes | 8 | 64-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does a lighter structured backbone help the frozen decomposition? |
| 2 | `residual_h08_small_joint` | 1 | no | 8 | 64-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does joint training still win when harmonic order is reduced? |
| 3 | `residual_h12_small_frozen` | 1 | yes | 12 | 64-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Is the current frozen baseline still competitive when rerun inside the new campaign? |
| 4 | `residual_h12_small_joint_anchor` | 1 | no | 12 | 64-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does the current recovery winner remain the anchor inside the new campaign state? |
| 5 | `residual_h16_small_joint` | 1 | no | 16 | 64-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does a richer harmonic backbone reduce the residual burden enough to improve held-out error? |
| 6 | `residual_h12_medium_joint` | 2 | no | 12 | 128-64 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Is a modest capacity increase enough to improve over the small joint anchor? |
| 7 | `residual_h12_wide_joint` | 2 | no | 12 | 128-128 | 0.10 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does a wider residual branch learn a better nonlinear correction? |
| 8 | `residual_h12_deep_joint` | 2 | no | 12 | 128-128-64 | 0.10 | yes | 5 | 4 | 0.0007 | 20-250 | 35 | Does extra depth become useful if the learning rate is softened slightly? |
| 9 | `residual_h12_small_joint_low_dropout` | 2 | no | 12 | 64-64 | 0.05 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Is the current branch slightly over-regularized? |
| 10 | `residual_h12_small_joint_high_dropout` | 2 | no | 12 | 64-64 | 0.20 | yes | 5 | 4 | 0.0010 | 20-250 | 35 | Does stronger residual regularization improve generalization? |
| 11 | `residual_h12_small_joint_no_layer_norm` | 2 | no | 12 | 64-64 | 0.10 | no | 5 | 4 | 0.0010 | 20-250 | 35 | Is layer norm helping, or only adding unnecessary constraints? |
| 12 | `residual_h12_small_joint_low_lr_long` | 3 | no | 12 | 64-64 | 0.10 | yes | 5 | 4 | 0.0007 | 20-320 | 45 | Does a slower, longer schedule improve the anchor configuration? |
| 13 | `residual_h12_wide_joint_low_lr_long` | 3 | no | 12 | 128-128 | 0.10 | yes | 5 | 4 | 0.0007 | 20-320 | 45 | Does the stronger schedule unlock the wide residual branch more effectively? |
| 14 | `residual_h12_small_joint_dense` | 3 | no | 12 | 64-64 | 0.10 | yes | 1 | 2 | 0.0010 | 20-250 | 35 | Does full-point training help the residual family when the batch is reduced conservatively? |
| 15 | `residual_h12_small_joint_medium_dense_large_batch` | 3 | no | 12 | 64-64 | 0.10 | yes | 5 | 8 | 0.0010 | 20-250 | 35 | Does a larger effective batch improve the current anchor without changing the architecture? |

## Why These Configurations

The matrix is not intended as a blind exhaustive search.

It is intended to answer the highest-value residual-family questions in a staged
and interpretable way.

### Why Phase 1 Is Small But Structural

Phase 1 isolates the backbone logic first:

- lower harmonic order;
- anchor order `12`;
- higher harmonic order;
- frozen versus joint comparison where still useful.

This is important because there is no point over-optimizing the residual branch
around the wrong structured regime.

### Why Phase 2 Focuses On Joint Mode

The recovery result already suggests joint mode is stronger.

Phase 2 therefore spends most of the search budget on joint variants instead of
duplicating every capacity test in both frozen and joint modes. That keeps the
matrix wide but still disciplined.

### Why Phase 3 Mixes Schedule And Density

The final phase tries to see whether the best residual architecture is currently
optimization-limited or data-regime-limited.

This is where the largest compute cost appears, so the matrix keeps only a few
carefully chosen schedule/density probes instead of exploding into another full
grid.

## Parameter Notes

### Harmonic Order

- `8` tests a lighter structured prior.
- `12` is the current best anchor.
- `16` tests whether extra periodic richness improves the decomposition.

Expected effect:

- lower order may leave too much work to the residual branch;
- higher order may reduce residual burden, but may also overconstrain the
  decomposition if the explicit branch becomes too dominant.

### Freeze Structured Branch

- `true` keeps the harmonic branch as a fixed interpretable backbone;
- `false` lets the whole decomposition adapt jointly.

Expected effect:

- frozen mode may preserve interpretability and stabilize training;
- joint mode may yield lower error by allowing the structured branch to adapt to
  the empirical TE behavior.

### Residual Hidden Size

- `64-64` is the proven small anchor;
- `128-64` tests a moderate width increase;
- `128-128` tests a clearly wider residual branch;
- `128-128-64` tests additional depth.

Expected effect:

- larger models may learn subtler correction structure;
- but they may also overfit or add runtime without proportional gain.

### Dropout And Layer Norm

- dropout `0.05`, `0.10`, and `0.20` tests under-regularized versus
  over-regularized behavior;
- layer norm on/off tests whether residual normalization is helping convergence
  or suppressing useful signal dynamics.

### Learning Rate And Schedule

- `0.0010` remains the practical default anchor;
- `0.0007` is the slower alternative for larger or longer runs;
- `20-320` plus patience `45` is the stronger schedule probe.

Expected effect:

- the longer schedule may matter if the family is still under-optimized;
- if not, longer runs will mainly add runtime without real test improvement.

### Data Density And Batch

- `point_stride = 1` is the full-density stress test;
- `curve_batch_size = 8` at stride `5` tests a smoother optimization regime
  without the full density cost.

Expected effect:

- denser data may help the residual branch model finer deviations from the
  harmonic prior;
- but it may also deliver weak gains if the explicit branch already absorbs the
  main periodic structure.

## Evaluation Rules

The campaign should rank configurations using the repository-standard policy:

- primary metric: `test_mae`
- first tie breaker: `test_rmse`
- second tie breaker: `val_mae`
- third tie breaker: `trainable_parameter_count`

The interpretation should also explicitly track:

- structured-versus-residual branch behavior through
  `test_structured_mae` and `val_structured_mae`;
- runtime cost versus accuracy gain;
- whether wider/deeper residual branches create meaningful improvement or only
  cost inflation;
- whether full-density training is practically justified for this family.

## Recommended Execution Order

The safest execution order is:

1. Phase 1
2. Phase 2
3. Phase 3

Within each phase:

1. smallest or closest-to-anchor variants first
2. wider/deeper or denser variants later

This preserves the option to stop intelligently if the evidence becomes
one-sided early, while still keeping the default plan intentionally ambitious.

## What We Expect To Learn

This campaign should answer the following concrete questions:

1. Is the residual family best in frozen or joint mode after a broader search?
2. Is harmonic order `12` actually the best residual backbone anchor?
3. Does the family want a larger residual branch, or is the current `64-64`
   branch already near-optimal?
4. Does lower or higher residual regularization improve held-out performance?
5. Is the family schedule-limited, density-limited, or already close to its
   practical ceiling?
6. Can the residual family close the remaining gap to the tree-family global
   leader strongly enough to justify becoming the main project candidate?

## Execution Gate

Before the campaign is launched:

1. the family YAML files must be generated from this approved plan;
2. the campaign state must be written to `doc/running/active_training_campaign.yaml`;
3. the exact launch command must be provided;
4. the protected-file workflow must be respected;
5. the user must explicitly approve the generated campaign preparation.

## Next Step

If this planning report is approved, generate the campaign YAML files for the
`15` residual-family runs, write the campaign state, and provide the exact
command needed to launch the first `Wave 1` follow-up familywise
hyperparameter campaign.
