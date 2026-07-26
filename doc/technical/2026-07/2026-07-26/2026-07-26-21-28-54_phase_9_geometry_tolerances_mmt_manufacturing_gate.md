# Phase 9 Geometry, Tolerances, MMT, And Manufacturing Gate

## Overview

Phase 9 evaluates geometry-, tolerance-, MMT-, and manufacturing-prior PINNs.
It preserves the paper and simulation knowledge as synthetic-oracle evidence
while enforcing the completed MMT parameter-availability blocker.

This document is automatically approved under the standing document approval
through 2026-07-27 12:50 Europe/Rome. The general approval for the Phase 9
commit remains valid through 2026-07-26 22:37:56 Europe/Rome.

## Technical Approach

1. Verify MMT, tolerance, wear/contact, and FEA-surrogate sources.
2. Audit nominal geometry, unit-specific tolerances, component errors,
   reducer-instance identity, synthetic populations, and transfer evidence.
3. Keep condition-invariant constants distinct from condition-varying causal
   physical inputs.
4. Classify `PINN-G1` through `PINN-G5` without fitting unobserved geometry
   from TE targets.
5. Preserve paper-faithful MMT as deferred and allow synthetic oracle work to
   proceed independently.

## Involved Components

- Phase 9 portfolio configuration and generic portfolio audit tooling
- MMT paper and MATLAB demonstrator
- Jin, Chen, and Wang numerical/FEA sources
- MMT diagnostic and reference summaries
- Phase 9 report, roadmap, backlog, ledger, master summaries, guide, and site

No subagent is planned.

## Implementation Steps

1. Create, run, and validate the Phase 9 portfolio audit.
2. Record source, quantity, formulation, and exit-gate artifacts.
3. Synchronize canonical status documents.
4. Run Python, YAML, Markdown, Git, and Sphinx QA.
5. Check staged sizes and create the Phase 9 commit.
