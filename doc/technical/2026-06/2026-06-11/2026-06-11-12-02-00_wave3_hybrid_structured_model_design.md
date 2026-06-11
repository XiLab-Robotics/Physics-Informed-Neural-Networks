# Wave 3 Hybrid Structured Model Design

## Overview

This technical document opens the non-invasive design step for `Wave 3`
Hybrid Structured Models while the separate `Track 2H` dispersion-aware
campaign is running on another workstation. It does not change training code,
campaign YAMLs, launchers, active campaign state, or `Track 2H` artifacts.

`Wave 3` should test whether the TE curve problem benefits from combining the
paper-style harmonic representation with a learned residual or structured
decoder. The current `Track 2` evidence suggests that pure loss changes and
direct curve prediction are not enough to explain or remove the model-side
mean-surface errors. The design should therefore preserve harmonic
traceability while allowing a data-driven residual to correct the parts that
the harmonic stack does not capture robustly.

## Technical Approach

The design step will create a repository-owned Wave 3 explanatory report that:

- keeps the recovered paper harmonic set explicit:
  `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`;
- separates fragile harmonic groups from comparatively stable middle
  harmonics;
- proposes narrow hybrid structured candidates before any large integrated
  multi-head model;
- defines causal input boundaries and direction-separated `global`, `Fw`, and
  `Bw` reporting rules;
- records comparison targets against `Track 2G`, `Track 2H`, `Wave 2B`,
  `Wave 2C`, and accepted `Track 2` leaders;
- leaves implementation, campaign YAML generation, launcher generation, and
  training launch for a later approval gate.

No subagent use is planned for this design step.

## Involved Components

- `doc/reports/analysis/wave3/Wave 3 Hybrid Structured Models.md`
- `doc/README.md`
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/07_RCIM_Recovered_Assets_Project_Summary.md`
- `doc/reports/analysis/track2/dispersion_aware_wave_roadmap/[2026-06-10]/track2_dispersion_aware_wave_roadmap.md`

## Implementation Steps

1. Create the Wave 3 hybrid structured model design report.
2. Register the new technical document and analysis report in `doc/README.md`.
3. Keep this pass documentation-only and avoid active `Track 2H` campaign
   files.
4. Run repository Markdown QA on the touched Markdown files.
5. Wait for a later explicit approval before implementing Wave 3 code,
   campaign YAMLs, launchers, or training execution.
