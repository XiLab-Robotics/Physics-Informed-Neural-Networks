# HYG-06 Scientific Dependency Declaration Alignment

- **Prepared:** 2026-11-22 16:33:10 Europe/Rome from the local clock.
- **Source:** `XiLab-Robotics/Physics-Informed-Neural-Networks/main@0ec0349eacdf60f1d4e726fba4aec124e5b86e9e`.
- **Original requirements blob:** `32be1b18e8d3599c18692e02b2e1a0cf02626565`.
- **Tracking issue:** https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/issues/2
- **Owner authorization:** Explicit approval to apply the prepared three-file HYG-06 change and commit it was given on 2026-11-22; protected-main PR, review, and CI gates remain in force.

## Overview

Align the root scientific environment's declared direct dependencies with the
current source imports. Limit changes to `requirements.txt`, this technical
note, and its registration in `doc/README.md`. Keep all model, dataset,
training, PLC and historical-output content unchanged.

This declaration fix is separate from the Sphinx/Pages requirements and
Beckhoff TF3820 ONNX conversion requirements. It does not by itself establish
that a particular Python 3.12 environment installs or runs all packages.

## Technical Approach

- Add `onnx>=1.21,<2.0`, matching the existing range in the dedicated
  conversion and Sphinx requirements files. Direct current imports include
  `scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py`
  and `scripts/export/wave_5_2r/export_stage15_h04_onnx_and_validate_parity.py`.
- Add `psutil>=6.0,<9.0`, matching the existing Sphinx environment range,
  because `scripts/analysis/wave_5_2r/validate_wave52r_offline_leader_promotion.py`
  imports it directly.
- Add `scipy>=1.15,<2.0` to document direct use in
  `scripts/models/uncertainty_physics_trust_calibrator.py` and
  `scripts/campaigns/wave_5_2/run_wave52r_stage6_spectral_sobolev_guidance.py`.
  SciPy's published compatibility table supports Python 3.12 and NumPy 2.2
  for this lower bound. The exact solver outcome remains unverified.
- Consolidate `dask>=2026.3.0` plus `dask[distributed]` into
  `dask[distributed]>=2026.3.0`, preserving the version lower bound and
  the requested distributed extra.

No other requirement, Python script, version lock, model artifact, data file,
existing paper evidence, deployment workflow or training launcher is changed.

## Involved Components

| Path | Planned change |
| --- | --- |
| `requirements.txt` | Four narrowly scoped dependency declaration edits |
| `doc/README.md` | Register this technical note |
| `doc/technical/2026-11/2026-11-22/2026-11-22-16-33-10_hyg06_scientific_dependency_declaration_alignment.md` | Scope, evidence and release gate |
| `site/requirements-docs.txt` | Read-only: existing successful Sphinx/Pages profile |
| `requirements-twincat-onnx-conversion.txt` | Read-only: conversion profile remains independent |

## Implementation Steps

1. Verify the exact `main` SHA and existing requirements Git blob, then
   create one short-lived maintenance branch from that commit.
2. Record this technical note, register it from `doc/README.md`, and apply
   only the four approved edits to root `requirements.txt`.
3. Check requirement syntax, uniqueness, retention of all unrelated version
   bounds, Markdown whitespace, and final newlines. Confirm the Git compare
   exposes exactly these three files and no large staged content.
4. Open a protected-main PR, verify its standard GitHub-hosted
   `Repository Quality Checks` without launching scientific runners.
5. Require the repository's normal review and merge gates. After merge,
   separately check the new `main` SHA and Sphinx Pages workflow before
   deleting the temporary branch.
6. Record prepared, applied, and verified states separately in the maintenance
   issue and coordinator SRC/K/C registers.

## Verification And Release Gates

- **Source import audit:** previously SOURCE_STATIC_VERIFIED.
- **Exact original requirements blob and minimal declaration diff:** checked
  in the approved preparation.
- **Full Python 3.12 solver and installation:** NOT EXECUTED.
- **Actual training, benchmark, model conversion and numerical parity:**
  NOT EXECUTED.
- **PLC/TF3820/TestRig and live compensation:** NOT EXECUTED.
- **Scientific CI or large training runner:** CI_GATE_BLOCKED until an
  appropriate runner and budget are verified.
- **Main PR quality and Pages publishing:** verify separately after applying
  the change; do not infer success from previous workflow runs.
