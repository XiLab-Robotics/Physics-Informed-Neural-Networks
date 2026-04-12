# Exact Paper Faithful Reproduction Campaign Package

## Overview

This package prepares the first coordinated `Track 1` paper-faithful
reproduction campaign after the completed exact-paper model-bank stabilization
campaign.

The repository does not yet expose one single runner that unifies:

- the recovered exact-paper family-bank workflow; and
- the harmonic-wise shared offline evaluator anchored to `Target A`.

This package therefore uses a coordinated campaign structure with two existing
runner types:

- `run_exact_paper_model_bank_validation.py`
- `run_harmonic_wise_comparison_pipeline.py`

That keeps the campaign executable today while preserving the benchmark-facing
intent of the approved planning report.

## Included Runs

1. `01_exact_paper_recovered_reference.yaml`
2. `02_exact_paper_amplitude_phase_reference.yaml`
3. `03_exact_paper_dominant_harmonic_specialized.yaml`
4. `04_track1_current_best_shared_evaluator_reference.yaml`

## Scope Boundary

The first two runs validate the recovered exact-paper family-bank surface under
the exact `ampl_k` / `phase_k` target schema.

The last two runs use the repository-owned harmonic-wise offline evaluator with
the full RCIM harmonic set, so the campaign still measures progress against the
offline benchmark path that matters for `Target A`.

This is the closest honest executable approximation of a paper-faithful
reproduction campaign in the current repository state.
