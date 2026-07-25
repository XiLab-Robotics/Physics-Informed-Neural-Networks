# Phase 0 PINN Program Foundations

## Overview

This technical project closes Phase 0 of the sixteen-phase Wave 5.2 PINN
implementation roadmap. It extends the already implemented paired `Fw` / `Bw`
common split into a complete, versioned foundation contract covering dataset
provenance, coordinates, units, direction conventions, causal availability,
operating-domain coverage, temporal evidence, and harmonic evidence.

This document is automatically approved under the user's standing instruction
for the sixteen-phase roadmap. It authorizes Phase 0 implementation and its
phase-closing Git commit. It does not authorize a training campaign.

## Technical Approach

The existing content-addressed paired manifest remains the canonical
condition-level split. A repository-owned foundation-audit script will read
every paired curve and produce:

- per-direction angular-grid and revolution statistics;
- nominal-versus-measured operating-condition ranges;
- sign and direction evidence;
- interpolation and extrapolation support maps;
- time, acceleration, inertia, reversal-cycle, and `DataValid` availability;
- a signal-causality and PLC-availability matrix;
- measured harmonic-order prevalence on a normalized one-revolution grid;
- explicit input-side and output-side angle conventions;
- duplicate-condition, source-hash, and split-leakage evidence.

The audit will use NumPy 2.x array loading and real-valued FFT operations
according to the current official API semantics reviewed through Context7.
Frequency bins will be interpreted in cycles per output revolution.

## Involved Components

- `config/analysis/pinn_program_foundations/`
- `scripts/analysis/pinn_program_foundations/`
- `output/analysis/pinn_program_foundations/`
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/`
- `doc/scripts/analysis/pinn_program_foundations/`
- `doc/running/te_model_live_backlog.md`
- the current ledger and Training Results Master Summary mirrors

Canonical inputs:

- `data/polished_dataset/`
- `output/analysis/polynomial_fourier_benchmark/common_split_manifest.yaml`
- `doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md`
- `doc/reference_summaries/10_Polynomial_Fourier_TE_Model_Project_Summary.md`
- `doc/reference_summaries/13_RV_Reducer_Theoretical_Mechanics_Reference_Synthesis.md`
- the full-PINN theory-validation roadmap

No model registry, accepted program leader, or campaign state will change.

## Implementation Steps

1. Define the complete Phase 0 audit configuration and output schema.
2. Validate the paired split and load all 1,938 polished directional curves.
3. Audit angular grids, revolutions, units, direction signs, nominal and
   measured conditions, and missing or non-finite values.
4. Build interpolation-domain, temporal-evidence, causal-signal, and
   PLC-availability contracts.
5. Compute direction-specific measured harmonic prevalence on normalized
   one-revolution grids.
6. Generate machine-readable YAML and CSV artifacts plus the canonical Phase 0
   Markdown report.
7. Update the roadmap, backlog, ledger, master summaries, usage guide, and
   documentation indices.
8. Run Python, manifest, Markdown, Sphinx, and Git-diff validation.
9. Run commit preflight and create the Phase 0 commit.

## Completion Criteria

Phase 0 is complete only when every test listed in its roadmap section is
represented by direct machine-readable evidence or an explicit unavailable
signal classification, and every later formulation can determine whether its
required inputs are measured, causally reconstructable, offline-only, or
absent.
