# Track 2 Component Offset Identification Inputs

## Overview

This report prepares measured component-offset input tables for the
`Track 2` component-offset identification branch. It does not train
models, alter registries, or assert that `a_0` / `Component 0` is the
confirmed cause of the observed curve-offset symptom.

- Run Instance: `2026-06-09-18-39-13__track2_component_offset_identification_inputs`
- Output Directory: `output/validation_checks/track2_component_offset_identification/2026-06-09-18-39-13__track2_component_offset_identification_inputs`
- Source CSV Files: `969`
- Directional Curves: `1938`
- Directions: `backward`, `forward`
- Harmonic Orders: `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240`

## Output Tables

| Artifact | Purpose |
| --- | --- |
| `track2_component_offset_per_curve_components.csv` | Per-curve measured mean / `a_0` proxy and selected harmonic coefficients. |
| `track2_component_offset_condition_summary.csv` | Condition-level aggregates by direction, speed, torque, oil temperature, and harmonic order. |
| `track2_component_offset_identification_inputs_summary.yaml` | Machine-readable run summary. |

## Next Use

Use these tables to plot experimental `a_0` and curve-mean surfaces over
speed and torque, split by oil temperature and direction. The follow-up
diagnostic should compare high-offset cases against multiple harmonic
orders before deciding whether the issue is `a_0`-dominant,
multi-component, condition/regime-driven, or repeatability-limited.

## Table Counts

- Per-curve component rows: `19380`
- Condition summary rows: `19380`
