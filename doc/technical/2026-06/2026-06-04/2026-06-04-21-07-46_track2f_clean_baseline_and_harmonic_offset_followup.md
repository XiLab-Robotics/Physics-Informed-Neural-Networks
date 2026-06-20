# Wave 3.1 Clean Baseline And Harmonic-Offset Follow-Up

## Overview

This technical note records the modeling decision made after reviewing the
completed `Wave 3.1` `sequential_residual_offset_probe` results.

The completed `Wave 3.1` model was intentionally a clean non-harmonic baseline:
it combined a pointwise feedforward branch with a causal sequential residual
offset branch, but it did not force periodic or harmonic TE curve structure.
The observed TE Curve Verification Pipeline behavior is therefore diagnostically useful even though it
is not a shape-leading candidate.

Future offset-aware model work must keep this clean branch available as a
baseline when testing new curve indices, multi-head structures, or composite
losses. It should not be confused with the next family of harmonic or periodic
shape-preserving models.

## Technical Approach

The follow-up plan should preserve two parallel comparison tracks:

- a clean causal non-harmonic baseline derived from
  `sequential_residual_offset_probe`;
- a shape-preserving harmonic or periodic family with explicit offset, bias, or
  amplitude heads.

The clean baseline remains important because it measures whether improvements
come from the new objective or multi-head training itself, rather than only from
forcing harmonic features into the model. It should be evaluated with the same
curve-first TE Curve Verification Pipeline metrics as the harmonic candidates.

The harmonic-offset follow-up should combine:

- an explicit harmonic or periodic shape branch;
- a causal offset or low-frequency residual branch;
- a composite selection target that includes pointwise error, centered-shape
  error, mean-offset error, and, where feasible, spectral or amplitude/phase
  diagnostics;
- separate `global`, `Fw`, and `Bw` branches carried forward in parallel.

## Involved Components

- `scripts/models/sequential_residual_offset_network.py`
- `scripts/models/periodic_feature_network.py`
- `scripts/models/residual_harmonic_temporal_sequence_network.py`
- `config/training/track2f_offset_aware_probe/`
- `doc/reports/campaign_results/track_2/campaign_closeouts/`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Implementation Steps

1. Update the Wave 3.1 campaign closeout narrative to state explicitly that
   `sequential_residual_offset_probe` is the clean non-harmonic baseline.
2. Update the curve-first TE strategy to keep this clean baseline in the future
   comparison matrix when introducing new curve indices, multi-head training, or
   composite losses.
3. Ensure future campaign plans keep `global`, `Fw`, and `Bw` branches separate
   for both clean and harmonic-offset candidates.
4. Do not promote Wave 3.1 as the shape-leading model family; use it as the
   control branch for the next harmonic-offset intervention.
5. Run Markdown QA on every touched authored Markdown file before closing the
   documentation update.
