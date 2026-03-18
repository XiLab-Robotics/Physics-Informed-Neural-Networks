# Model And Training Explanatory Report Rule

## Overview

This document formalizes a new mandatory documentation rule for future model implementations in this repository.

Whenever a new model family, model variant, or materially new training entry point is introduced, the implementation must be accompanied by a dedicated explanatory report that helps the reader understand the model quickly before reading the code.

The purpose of the report is twofold:

- provide a fast conceptual framing of the model, its nature, and its expected strengths and weaknesses;
- provide a technical walkthrough of the actual Python implementation so the code structure is immediately understandable.

## Technical Approach

The explanatory report should become a standard deliverable attached to every new model implementation task.

The report must always include a conceptual part and a code-level part.

For a newly introduced model, the report must contain:

1. a clear description of the model;
2. the operating principle and why the model belongs to its chosen family;
3. a conceptual map or schematic explanation of the network or algorithm structure;
4. the main advantages, limitations, and expected practical behavior in the TE context;
5. a technical Python section explaining the implemented files, classes, and functions.

If the new model also requires a new training file or a materially new training workflow, the same report must additionally contain:

1. a high-level explanation of how the training workflow operates;
2. a detailed section explaining the key Python functions and implementation choices in the training file.

The intent is not to produce a generic scientific summary, but a repository-oriented technical companion document that makes both the model design and the implementation legible at a glance.

## Involved Components

The new rule will affect:

- `AGENTS.md`
  Persistent repository workflow rules.

- `README.md`
  Main project rule and technical-document index.

- `doc/README.md`
  Internal documentation index.

- future model implementation tasks under `scripts/models/`
  Every newly added model should trigger an explanatory report deliverable.

- future training entry points under `scripts/training/`
  If a new model needs a new training script, the same report must also document the training workflow.

- future report locations under `doc/reports/analysis/` or another dedicated documentation location chosen consistently
  The repository should keep these explanatory reports in an explicit, discoverable location rather than leaving the explanation only inside code comments.

## Implementation Steps

1. Add the new rule to `AGENTS.md` so it becomes part of the persistent execution workflow.
2. Clarify in the rule that the explanatory report is mandatory whenever a new model is created.
3. Clarify that the report must include:
   - model description;
   - operating principle;
   - conceptual map or schematic structure;
   - pros and cons;
   - technical explanation of the Python implementation.
4. Clarify that, when a new training file is added, the same report must also include:
   - high-level training workflow explanation;
   - detailed explanation of the implemented training functions.
5. Reference this technical rule document from `README.md` and `doc/README.md`.
6. Apply the rule in future model-implementation tasks as a standard deliverable before final commit.
