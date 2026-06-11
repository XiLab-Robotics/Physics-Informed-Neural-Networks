# Wave 4 Sub-Branch Design Package

## Overview

This technical document records the documentation-only design package for all
planned `Wave 4` physics-informed sub-branches. The package expands the Wave 4
roadmap into separate designs for `Wave 4A` through `Wave 4G`, without
modifying training code, campaign YAMLs, launchers, active campaign state, or
the running `Track 2H` campaign.

## Technical Approach

The design package will create one report per Wave 4 sub-branch:

- `Wave 4A` MMT equation diagnostic;
- `Wave 4B` MMT feature generator;
- `Wave 4C` MMT soft-constraint PINN;
- `Wave 4D` mesh-stiffness and loaded-TE PINN;
- `Wave 4E` backlash, preload, and state-aware PINN;
- `Wave 4F` cycloid contact-force PINN;
- `Wave 4G` planetary mesh-force and loaded-static-TE PINN.

Each design separates the physical idea, required inputs, first implementation
candidate, leakage boundaries, expected artifacts, and decision gates. External
gear-dynamics sources are treated as exploratory formulation candidates, not
as directly validated RV-reducer equations.

No subagent use is planned.

## Involved Components

- `doc/reports/analysis/wave4/`
- `doc/reports/analysis/mmt_te_modeling/MMT TE Modeling Equation Extraction And Reimplementation Plan.md`
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`
- `doc/README.md`

## Implementation Steps

1. Create detailed design reports for `Wave 4A` through `Wave 4G`.
2. Update the main Wave 4 report with links to the detailed designs.
3. Register the new reports and this technical note in `doc/README.md`.
4. Run scoped Markdown QA on all touched Markdown files.
5. Wait for later explicit approval before implementing Wave 4 code,
   campaigns, YAMLs, launchers, or training execution.
