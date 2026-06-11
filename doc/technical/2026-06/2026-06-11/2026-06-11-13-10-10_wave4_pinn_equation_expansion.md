# Wave 4 PINN Equation Expansion

## Overview

This technical document records the approved update to expand `Wave 4` from a
single first-PINN design into a staged physics-informed exploration branch.
The update incorporates the repository-owned `MMT_TEModeling` equation
reimplementation introduced by commit
`3d4b9b720471aa3aca461e94a9e14f353637b153` and adds additional gear-meshing
formulation families as exploratory Wave 4 sub-branches.

The work is documentation-only. It does not modify training code, campaign
YAMLs, launchers, active campaign state, or running `Track 2H` artifacts.

## Technical Approach

The documentation update will:

- promote the MMT equation-chain reproduction from generic Wave 4 background
  into the first explicit Wave 4 sub-branch;
- split Wave 4 into intermediate branches `4A`, `4B`, `4C`, and later
  candidates;
- define which equation families can be used immediately as diagnostics or
  soft regularizers and which require extra geometry, stiffness, contact, or
  calibration data;
- add external literature-derived candidates for transmission-error,
  time-varying mesh stiffness, loaded static TE, backlash/nonlinear dynamics,
  cycloid contact/modification, and planetary mesh-force behavior;
- preserve causal input discipline and direction-separated `global`, `Fw`,
  and `Bw` evaluation.

No subagent use is planned.

## Involved Components

- `doc/reports/analysis/wave4/Wave 4 PINN Formulation And First PINN.md`
- `doc/reports/analysis/mmt_te_modeling/MMT TE Modeling Equation Extraction And Reimplementation Plan.md`
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.m`
- `doc/README.md`

## Implementation Steps

1. Update the Wave 4 report with the MMT equation integration path.
2. Add staged Wave 4 sub-branches from `4A` through exploratory external
   formulation candidates.
3. Record source boundaries and repository readiness for each formulation
   family.
4. Register this technical document in `doc/README.md`.
5. Run scoped Markdown QA on touched Markdown files.
