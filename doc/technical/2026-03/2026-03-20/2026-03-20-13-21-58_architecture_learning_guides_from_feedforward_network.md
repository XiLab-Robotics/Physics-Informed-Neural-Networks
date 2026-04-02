# Architecture Learning Guides From FeedForward Network

## Overview

This document defines the next documentation series requested by the user: a set of `learning_guides` that explain the repository's model architectures one by one, starting from the implemented `FeedForward Network`.

The goal is to create a didactic progression that helps the reader understand:

- what each architecture is trying to model;
- how the architecture works at a conceptual level;
- how the architecture is structured computationally;
- why the architecture is useful in the TE compensation context of this repository;
- how the architecture relates to the existing model-explanatory reports and the broader TE curriculum guide.

The first guide in the series will focus on the `FeedForward Network`, then extend to the other currently documented architectures in a stable order.

## Technical Approach

The architecture-learning series should be built as report-local documentation under `doc/reports/analysis/learning_guides/`, with one dedicated folder per architecture.

Each learning guide should include:

- a plain-language introduction for beginners;
- a more formal explanation suitable for university-level readers;
- a conceptual diagram that explains the modeling idea;
- an architecture-style diagram that explains the network or algorithm flow;
- a repository-context section that maps the architecture to the implemented Python files and training workflow;
- a PDF companion exported from the Markdown source once the figures are approved;
- later, a `video_guide_package/` when the PDF and figures are complete and the user approves video-guide preparation.

The recommended first-series order is:

1. `FeedForward Network`;
2. `Harmonic Regression`;
3. `Periodic Feature Network`;
4. `Residual Harmonic Network`.

This order follows the current implementation maturity and mirrors the existing explanatory reports in `doc/reports/analysis/model_explanatory/`.

## Involved Components

- `doc/reports/analysis/model_explanatory/FeedForward Network/`
- `doc/reports/analysis/model_explanatory/Harmonic Regression/`
- `doc/reports/analysis/model_explanatory/Periodic Feature Network/`
- `doc/reports/analysis/model_explanatory/Residual Harmonic Network/`
- `doc/reports/analysis/learning_guides/`
- `doc/reports/analysis/learning_guides/<Architecture Name>/assets/`
- `doc/reports/analysis/learning_guides/<Architecture Name>/<Architecture Name>.md`
- `doc/reports/analysis/learning_guides/<Architecture Name>/<Architecture Name>.pdf`
- `README.md`
- `doc/README.md`
- `AGENTS.md`

## Implementation Steps

1. Create a dedicated learning guide for the `FeedForward Network` using the existing explanatory report as the technical reference.
2. Add the conceptual and architecture diagrams needed for that guide, storing them in the guide-local `assets/` folder.
3. Export and validate the PDF companion after the guide images are approved.
4. Repeat the same pattern for `Harmonic Regression`, `Periodic Feature Network`, and `Residual Harmonic Network`.
5. Keep each guide aligned with the same didactic depth, terminology discipline, and TE-specific framing so the series reads as one coherent curriculum.
6. Update the project documentation indexes so the new guides remain discoverable from `README.md` and `doc/README.md`.
