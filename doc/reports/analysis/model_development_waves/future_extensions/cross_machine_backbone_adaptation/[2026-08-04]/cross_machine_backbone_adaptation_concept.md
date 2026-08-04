# Cross-Machine Backbone Adaptation

## Status And Objective

`Cross-Machine Backbone Adaptation` is an inactive future extension of the TE
modeling program. It is not an active campaign and does not authorize data
collection, training, promotion, or deployment.

The objective is to reduce the measurement burden when adapting TE prediction
to a new physical machine or reducer. A checkpoint trained on the current
machine would provide a reusable source backbone. A smaller dataset measured
on the new machine would then support bounded fine-tuning instead of repeating
the complete source-machine measurement and training program from scratch.

The central hypothesis is:

> A source-machine TE backbone can preserve reusable angular, harmonic, and
> operating-condition representations, allowing a target machine to reach an
> acceptable curve-first result with fewer measured operating conditions.

This hypothesis is unverified. Archive quality, offline leadership, or
TwinCAT readiness on the source machine does not prove cross-machine transfer.

## Canonical Terminology

| Term | Meaning |
| --- | --- |
| Source machine | The currently characterized physical machine or reducer used to train the reusable checkpoint. |
| Source backbone | A provenance-complete checkpoint selected from the completed source-machine program. |
| Target machine | A different physical machine or reducer for which a new measured dataset is collected. |
| Target adaptation set | The limited target-machine training subset used for fine-tuning. |
| Target validation set | Held-out target-machine conditions used for tuning and checkpoint selection. |
| Target test set | Target-machine conditions opened once for the final curve-first decision. |
| Measurement budget | The number and coverage of target-machine operating conditions required by an adaptation arm. |

The word `backbone` has another valid repository meaning: K01 is the frozen
temporal base inside the A02 integrated-specialist composition. That is a
within-model architectural role and must not be confused with cross-machine
checkpoint adaptation.

## Distinction From Dirty-To-Clean Modeling

The historical `simplified_dataset` to `polished_dataset` proposal is a
within-machine paired-dataset hypothesis. Both datasets belong to the same
measurement lineage; the proposal tests noise-aware or dirty-to-clean
supervision.

Cross-machine backbone adaptation is different:

- the source and target datasets come from different physical machines;
- the target machine has its own train, validation, and test conditions;
- the target-machine measurement budget is the quantity to reduce;
- source-machine performance is not accepted as target-machine evidence;
- no polishing transform or measured TE target is added to runtime inputs.

The old dirty-to-clean branch remains historical evidence and is not the
canonical backbone fine-tuning roadmap.

## Proposed Future Workflow

```text
complete source-machine program
    -> select one provenance-complete source checkpoint
    -> freeze the source checkpoint and source evaluation record
    -> collect a limited target-machine adaptation dataset
    -> define target-machine train, validation, and test conditions
    -> fine-tune through bounded adaptation strategies
    -> compare against zero-shot and same-budget scratch controls
    -> apply direction-separated curve-first verification
    -> qualify export and runtime separately if adaptation succeeds
```

Backbone selection must occur only when the current source-machine program has
finished its active points. Candidate roles may include an accepted periodic
GRU, a later deployment-qualified temporal model, or another model with a
stable input and state contract. Current offline candidates such as K01 or A02
must not be treated as eligible solely because they lead an offline surface.

## Required Experimental Controls

Every future study must evaluate the same target-machine partitions through at
least these controls:

| Arm | Purpose |
| --- | --- |
| Source-only zero-shot | Measure how well the frozen source backbone transfers without target training. |
| Same-budget scratch | Train the same architecture from random initialization on the limited target adaptation set. |
| Backbone fine-tuning | Adapt the source checkpoint using the same target data budget. |
| Full-target reference | Estimate the performance available from the larger target dataset when that evidence is affordable. |

The scratch and fine-tuning arms must use matched target conditions, seeds,
optimization budgets, and selection rules. Otherwise an apparent transfer
gain could come from extra training, different data coverage, or checkpoint
selection leakage.

Candidate adaptation strategies may include:

- output-head-only adaptation;
- partial unfreezing of later backbone layers;
- full-network fine-tuning with a bounded learning rate;
- regularization toward the source checkpoint;
- explicit recalibration of target-machine normalization statistics.

These are future ablations, not approved implementation decisions.

## Measurement-Budget Evaluation

The future campaign must define a target-machine measurement ladder before
training. The ladder should cover progressively larger, condition-balanced
subsets rather than arbitrary row percentages.

Each budget must preserve planned coverage of:

- speed;
- applied torque;
- oil temperature;
- encoder zeroing and dataset provenance;
- `DataValid` TE extraction windows;
- `Fw` and `Bw` directions;
- operating extremes and interpolation conditions.

The result should be a measurement-efficiency curve, not one isolated
fine-tuning score. It must show the smallest target-machine condition budget
that reaches a predeclared curve-first acceptance level and how that budget
compares with training from scratch.

## Evaluation And Acceptance Boundary

Results must remain separate for `Fw`, `Bw`, and `global`. The canonical
multi-index curve-first policy applies to every target-machine comparison and
must keep visible:

- raw error;
- mean-centered shape fidelity;
- offset and continuity behavior;
- harmonic amplitude and phase fidelity;
- robustness and tail behavior;
- visual measured-versus-predicted curve evidence;
- deployment readiness.

A future adaptation result is useful only if it demonstrates a reproducible
target-machine data-efficiency gain over the same-budget scratch control. A
lower scalar MAE alone is insufficient. The study must also show that reduced
measurement coverage does not erase difficult directions, temperatures,
torques, speeds, offsets, or harmonic regimes.

Target-machine validation and test curves must never be used to construct
fine-tuning targets, normalization values, source-to-target correction curves,
or operating-condition sampling decisions.

## Deployment Boundary

The adapted model must retain causal, PLC-available inputs and explicit
intermediate quantities. Cross-machine fine-tuning changes model parameters;
it does not authorize target-derived preprocessing during inference.

Successful offline adaptation does not prove:

- ONNX or Beckhoff conversion parity;
- TwinCAT XAE compilation;
- target activation or TF3820 licensing;
- ADS communication;
- PLC latency or state-reset behavior;
- commissioned TestRig compensation.

Those remain separate per-machine qualification gates.

## Reopening Gate

This future extension may be promoted only after:

1. the current source-machine program points are closed;
2. the project explicitly selects cross-machine adaptation from the future
   extension portfolio;
3. a target machine and compatible measurement contract are available;
4. one source backbone has sufficient provenance and an appropriate causal
   inference contract;
5. a new technical document defines the target-machine split and measurement
   ladder;
6. a campaign planning report, YAML package, local and `-Remote` launcher,
   launcher note, persistent state, and exact commands are approved before
   training.

The project may instead select another future extension, such as reopening
MMT after its physical-input gate is satisfied. Listing an option in the
backlog does not prioritize or authorize it.
