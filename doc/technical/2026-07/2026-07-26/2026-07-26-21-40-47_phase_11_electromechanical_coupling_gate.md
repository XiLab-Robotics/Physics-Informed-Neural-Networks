# Phase 11 Electromechanical Coupling Gate

## Overview

Phase 11 audits whether the current TE repository can support explicit
electromechanical PINN residuals derived from the PMSM, reducer dynamics, and
fault-sideband literature. The gate must distinguish measured mechanical
operating inputs from unavailable synchronized motor-current and drive-state
signals. The document is automatically approved under the user's active
sixteen-phase authorization.

## Technical Approach

Use the curated electromechanical reference, the mechanics synthesis, and the
verified dataset schema as the evidence boundary. Classify every required
quantity by measurement, offline reconstruction, synthetic-oracle, or
unavailable status. Evaluate `PINN-M1` through `PINN-M4` without treating
paper-reported current sidebands as local observations. Authorize training only
if a candidate has synchronized causal electrical inputs and an identifiable
physical residual.

## Involved Components

- Electromechanical coupling and fault-diagnosis reference PDF.
- RV-reducer mechanics and dataset-family reference summaries.
- Generic physics-portfolio feasibility builder and validator.
- Phase 11 configuration, CSV/YAML evidence artifacts, analytical report,
  roadmap, backlog, ledger, usage guide, and master summaries.

## Implementation Steps

1. Register and verify the electromechanical evidence sources.
2. Audit motor current, voltage, drive state, power, timing, mechanical
   channels, sideband targets, health labels, and runtime feasibility.
3. Classify `PINN-M1` through `PINN-M4` under the common feasibility taxonomy.
4. Generate and validate the Phase 11 evidence artifacts and report.
5. Synchronize canonical program documentation and advance to Phase 12 only if
   the audit is internally consistent.
6. Run touched-scope Markdown QA, final-newline checks, Sphinx, diff checks,
   staged-size checks, and create the dedicated Phase 11 commit.
