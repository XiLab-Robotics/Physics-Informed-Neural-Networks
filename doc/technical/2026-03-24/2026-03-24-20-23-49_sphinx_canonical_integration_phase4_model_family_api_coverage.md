# Sphinx Canonical Integration Phase 4 Model Family API Coverage

## Overview

This document defines the next canonical Sphinx integration batch after the
completed training-infrastructure API phase.

The goal of this phase is to expose the current Wave 1 neural model families
through stable canonical API pages and better public docstrings, so the portal
documents both:

- the shared training backbone already integrated in Phase 3;
- the model families that those workflows can instantiate through the model
  factory.

## Technical Approach

This batch should remain focused on the current implemented model-family layer:

- `scripts/models/harmonic_regression.py`
- `scripts/models/periodic_feature_network.py`
- `scripts/models/residual_harmonic_network.py`
- `scripts/models/model_factory.py`

The implementation should:

- improve only the public docstrings needed for readable generated API pages;
- create canonical model-family API pages under `docs/api/models/`;
- explain constructor parameters, context-aware forward paths, and auxiliary
  branch outputs where relevant;
- expose the model-factory routing logic as the canonical entry point linking
  model type strings to concrete implementations.

This phase intentionally excludes:

- new conceptual learning-guide content;
- report-level explanatory model pages;
- tree-model coverage;
- campaign-orchestration coverage.

## Involved Components

- `docs/api/models/index.rst`
- `docs/api/models/`
- `scripts/models/harmonic_regression.py`
- `scripts/models/periodic_feature_network.py`
- `scripts/models/residual_harmonic_network.py`
- `scripts/models/model_factory.py`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Inspect the public constructors and forward-related methods of the three
   model-family modules and the model factory.
2. Rewrite the high-value public docstrings in canonical source files using the
   current repository style and Google-style API structure where useful.
3. Add canonical Sphinx API pages under `docs/api/models/` for the three model
   families and the factory entry point.
4. Update the model API index so the new pages become navigable from the
   portal.
5. Build the Sphinx site with warnings treated as errors and fix any import,
   signature, or rendering issues.
6. Reassess whether any follow-up cross-links to learning guides or explanatory
   reports should be handled in a later dedicated content batch rather than in
   this API-only phase.
