# Wave 5.2 Sub-Branch Design Package

## Overview

This technical document records the documentation-only design package for all
planned `Wave 5.2` physics-informed sub-branches. The package expands the Wave 5.2
roadmap into separate designs for `Wave 5.2A` through `Wave 5.2G`, without
modifying training code, campaign YAMLs, launchers, active campaign state, or
the running `Wave 4 series` campaign.

## Technical Approach

The design package will create one report per Wave 5.2 sub-branch:

- `Wave 5.2A` MMT equation diagnostic;
- `Wave 5.2B` MMT feature generator;
- `Wave 5.2C` MMT soft-constraint PINN;
- `Wave 5.2D` mesh-stiffness and loaded-TE PINN;
- `Wave 5.2E` backlash, preload, and state-aware PINN;
- `Wave 5.2F` cycloid contact-force PINN;
- `Wave 5.2G` planetary mesh-force and loaded-static-TE PINN.

Each design separates the physical idea, required inputs, first implementation
candidate, leakage boundaries, expected artifacts, and decision gates. External
gear-dynamics sources are treated as exploratory formulation candidates, not
as directly validated RV-reducer equations.

No subagent use is planned.

## Involved Components

- `doc/reports/analysis/model_development_waves/wave_4/`
- `doc/reports/analysis/te_modeling/analytical_mmt/MMT TE Modeling Equation Extraction And Reimplementation Plan.md`
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`
- `doc/README.md`

## Implementation Steps

1. Create detailed design reports for `Wave 5.2A` through `Wave 5.2G`.
2. Update the main Wave 5.2 report with links to the detailed designs.
3. Register the new reports and this technical note in `doc/README.md`.
4. Run scoped Markdown QA on all touched Markdown files.
5. Wait for later explicit approval before implementing Wave 5.2 code,
   campaigns, YAMLs, launchers, or training execution.
