# Cross-Machine Backbone Adaptation Documentation Correction

## Overview

The repository currently conflates two different future model-development
ideas under the broad terms `transfer`, `backbone pretraining`, and
`fine-tuning`:

1. a historical within-machine dirty-to-clean hypothesis that would pretrain
   on `simplified_dataset` and fine-tune on `polished_dataset`; and
2. the intended cross-machine adaptation workflow, where a model trained on
   the current reducer or machine becomes a reusable backbone and is
   fine-tuned with a smaller measured dataset from a different machine.

This documentation-only task will establish the second meaning as the
canonical future extension. The objective is to reduce the measurement burden
for a new machine by transferring reusable TE representations from a
source-machine checkpoint, then adapting and validating the model on a
target-machine dataset that may be substantially smaller than the original
training dataset.

The historical `simplified_dataset` to `polished_dataset` dirty-to-clean
hypothesis will remain documented as a separate, non-priority intra-machine
experiment. It must not be presented as the intended backbone adaptation
roadmap. This task does not authorize model implementation, data collection,
fine-tuning, training, campaign preparation, or deployment claims.

No subagent is planned. If later work would benefit from a subagent, its name,
task boundary, and approval requirement must be recorded and approved before
launch.

## Technical Approach

Introduce the canonical term `Cross-Machine Backbone Adaptation` and define
the roles explicitly:

- the current measured machine is the `source machine`;
- a selected checkpoint trained on the source-machine dataset is the
  `source backbone`;
- a different physical machine or reducer is the `target machine`;
- a smaller, newly measured target-machine dataset supports bounded
  fine-tuning;
- target-machine validation and test partitions remain held out from
  fine-tuning and model selection;
- success is measured against both a source-only zero-shot control and a model
  trained from scratch using the same limited target-machine data budget.

The future workflow must preserve direction-separated `Fw`, `Bw`, and
`global` reporting, curve-first evaluation, causal inference inputs, explicit
checkpoint provenance, and TwinCAT-facing inspectability. It must also define
measurement-budget curves so the project can quantify how many target-machine
conditions are needed to reach a declared fraction of full-data performance.

The repository will distinguish three unrelated uses of similar terminology:

| Concept | Meaning | Current status |
| --- | --- | --- |
| Cross-machine backbone adaptation | Source-machine checkpoint fine-tuned on a smaller dataset from a new machine | Future extension |
| Dirty-to-clean modeling | `simplified_dataset` to `polished_dataset` supervision within the existing machine and dataset lineage | Historical separate hypothesis; not the intended backbone roadmap |
| Integrated-specialist backbone | K01 used as the frozen temporal base inside A02 | Current model-composition role; not cross-machine fine-tuning |

Historical technical documents and completed campaign reports will retain
their original decisions. Where they conflate dirty-to-clean work with the
intended backbone idea, a concise supersession note will clarify the new
terminology rather than rewriting historical outcomes.

## Involved Components

The implementation pass is expected to update these canonical surfaces:

- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- both maintained copies of `Training Results Master Summary.md`;
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`;
- the Wave 5.2 paired-dataset and model-design-gate reports that currently
  associate backbone transfer with `simplified_dataset` to
  `polished_dataset` training;
- the corresponding July technical documents and historical campaign
  plan/result documents where an explicit supersession note is required;
- a new canonical concept note under the analysis-report tree for future
  cross-machine backbone adaptation;
- `doc/README.md` and any narrower topic index required to register the new
  concept note and this technical document.

The search scope will include authored Markdown and YAML references to
`dirty-to-clean`, `transfer-learning backbone`, `backbone pretraining`,
`fine-tuning`, and legacy `Wave 5.2C` descriptions. References to unrelated
fine-tuning controls, synthetic-to-real studies, generic transfer tests, or
the K01/A02 frozen-backbone composition will not be relabeled.

The completed campaign state has an empty protected-file list. No campaign
configuration, launcher, training code, model artifact, registry, or active
campaign execution state needs to change for this documentation correction.

## Implementation Steps

1. Create a canonical future-extension concept note defining the
   source-machine backbone, target-machine limited-data fine-tuning workflow,
   measurement-budget objective, evaluation controls, and reopening gates.
2. Add `Cross-Machine Backbone Adaptation` to the live backlog as an inactive
   future option to be considered after the current program points are
   completed, alongside other explicitly deferred options such as MMT.
3. Synchronize the program ledger and both master-summary copies with the same
   future-extension status without presenting it as an active campaign.
4. Clarify the dataset-family reference so dirty-to-clean modeling remains an
   intra-machine dataset experiment and is not described as the intended
   cross-machine backbone workflow.
5. Add supersession notes to the specific Wave 5.2 design and paired-dataset
   documents that conflate the two concepts, while preserving their historical
   experimental conclusions and legacy identifiers.
6. Register the new concept note and technical document from canonical
   documentation entry points.
7. Re-run a focused repository search and classify every remaining transfer
   reference as cross-machine adaptation, historical dirty-to-clean work, or
   an unrelated use of transfer or fine-tuning.
8. Run the repository Markdown style checker, Markdownlint, final-newline
   checks, master-summary mirror verification, `git diff --check`, and the
   warning-free Sphinx build if the changed documentation lies within portal
   scope.
9. Report the completed documentation correction and wait for explicit user
   approval before any Git commit.

## Approval Gate

Implementation was explicitly approved by the user on `2026-08-04` after this
technical document was created and registered. Any later training or
limited-data adaptation experiment still requires a separate technical
document and campaign planning report before execution.
