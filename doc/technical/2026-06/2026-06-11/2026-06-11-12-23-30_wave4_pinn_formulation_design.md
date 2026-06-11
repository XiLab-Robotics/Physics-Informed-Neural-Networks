# Wave 4 PINN Formulation Design

## Overview

This technical document opens the non-invasive design step for `Wave 4` PINN
Formulation And First PINN while the separate `Track 2H` campaign is running
on another workstation. It does not change training code, campaign YAMLs,
launchers, active campaign state, or `Track 2H` artifacts.

`Wave 4` should test whether soft physics-informed constraints can improve TE
curve prediction after the dispersion-aware and hybrid structured branches.
The current reference material supports treating TE as a mechanically
structured quantity whose harmonics can be interpreted with respect to reducer
kinematics and error sources. The first PINN should therefore start with
constraints that are available from the repository data and reconstructed
curve representation, not with a full analytical RV reducer solver.

## Technical Approach

The design step will create a repository-owned Wave 4 explanatory report that:

- defines the first PINN as a soft-constraint model for TE curves;
- separates data-fit, periodicity, smoothness, harmonic-consistency,
  operating-condition consistency, and optional residual-structure losses;
- keeps the causal input boundary from `Track 2`;
- preserves direction-separated `global`, `Fw`, and `Bw` reporting;
- records what is reference-backed, what is an implementation inference, and
  what remains physically unproven;
- leaves implementation, campaign YAML generation, launcher generation, and
  training launch for a later approval gate.

No subagent use is planned for this design step.

## Involved Components

- `doc/reports/analysis/wave4/Wave 4 PINN Formulation And First PINN.md`
- `doc/README.md`
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`
- `doc/reports/analysis/track2/dispersion_aware_wave_roadmap/[2026-06-10]/track2_dispersion_aware_wave_roadmap.md`

## Implementation Steps

1. Create the Wave 4 PINN formulation design report.
2. Register the new technical document and analysis report in `doc/README.md`.
3. Keep this pass documentation-only and avoid active `Track 2H` campaign
   files.
4. Run repository Markdown QA on the touched Markdown files.
5. Wait for a later explicit approval before implementing Wave 4 code,
   campaign YAMLs, launchers, or training execution.
