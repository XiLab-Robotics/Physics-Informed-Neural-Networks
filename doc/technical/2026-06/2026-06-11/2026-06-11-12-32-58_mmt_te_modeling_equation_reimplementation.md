# MMT TE Modeling Equation Reimplementation

## Overview

This technical document plans the repository work requested for
`reference/MMT_TEModeling.pdf`, the Mechanism and Machine Theory paper
`A modelling approach for kinematic equivalent mechanism and rotational
transmission error of RV reducer`.

The requested deliverables are:

- a Markdown paper analysis and equation extraction document;
- a MATLAB reproduction script implementing the paper equations;
- an analogous Python reproduction script implementing the same equations;
- an implementation plan for evaluating whether the analytical model can
  predict transmission error on this repository's measured TE curves.

No subagent use is planned. If subagent use becomes useful later, the planned
subagent name, task boundary, and approval requirement must be recorded in an
updated technical document before requesting user approval.

## Technical Approach

The work will use `reference/MMT_TEModeling.pdf` as the primary source and
`doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md` as the existing
repository summary. The extraction will separate paper-stated facts from
implementation inferences.

The equation document will transcribe the numbered equations from the paper,
including the kinematic ratios, equivalent-linkage angle definitions,
closed-loop vector equations, velocity ratios, loop-incremental RTE model,
original-error mappings, prototype test equation, and validation-result
numbers. Ambiguous OCR extractions will be checked against rendered PDF pages
before being recorded.

The scripts will implement the equations in a transparent, traceable form
rather than as a fitted ML model. They will prioritize explicit intermediate
quantities such as `f1`, `f2i`, `f3`, `f4i`, the transfer coefficients
`g1`-`g4`, and original-error equivalent link errors.

The dataset-evaluation plan will map the paper's analytical inputs against
the repository's available operating variables and TE curve artifacts, then
identify which paper parameters are measured, configurable, assumed, or
unavailable.

## Involved Components

- `reference/MMT_TEModeling.pdf`
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
- planned equation report under `doc/reports/analysis/`
- planned MATLAB and Python reproduction scripts under a repository-owned
  scripts path
- repository TE dataset and TE Curve Verification Pipeline curve-evaluation documentation used for
  the later feasibility plan
- `doc/README.md` for registering the new technical document

## Implementation Steps

1. Complete a careful paper pass and record the paper's purpose, mechanism
   model, inputs, equations, validation setup, and reported results.
2. Create the Markdown equation extraction report with all numbered equations
   and a concise implementation note for each equation group.
3. Implement the MATLAB script with explicit parameter structures, equation
   functions, RV-80E prototype constants from the paper, and a reproducible
   simulation entry point.
4. Implement the Python script with the same structure and numerical behavior
   as the MATLAB script.
5. Add a dataset-evaluation plan explaining how to test the analytical model
   against repository TE curves, including required parameter mapping,
   calibration assumptions, metrics, and expected failure modes.
6. Run Markdown checks on touched Markdown files and basic syntax or smoke
   checks for the scripts where the local environment supports them.
