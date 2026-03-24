# NotebookLM Export Archives

The repository contains eight recovered `NotebookLM` export bundles under:

- `doc/imports/notebooklm_exports/`

These bundles are preserved as provenance material from the isolated
documentation workflow. They are not yet canonical guide pages and they should
not be confused with repository-authored learning-guide sources.

## Current Archive Topics

- `neural_network_foundations`
- `te_model_curriculum`
- `multilayer_perceptrons`
- `feedforward_network`
- `harmonic_regression`
- `training_validation_and_testing`
- `periodic_feature_network`
- `residual_harmonic_network`

## Archive Layout

Each topic folder follows the same structure:

- `images/`
- `pdf/`
- `slides/`
- `video/`

This keeps imported visual material, slide decks, supporting PDFs, and video
exports separated by artifact type while preserving their original topic
grouping.

## Canonical Integration Status

The current canonical rule remains:

- keep these bundles archived under `doc/imports/notebooklm_exports/` as
  provenance-preserving imported material;
- integrate them into the public documentation portal through summary and
  reference pages first;
- decide any later migration into canonical guide folders only after an
  explicit repository-wide learning-guide restructuring step.

The detailed archive-ingestion and extension decisions are documented in the
technical notes below:

- [NotebookLM Export Ingestion And Archive](../technical/notebooklm_export_ingestion.md)
- [Additional NotebookLM Guide Archives](../technical/additional_notebooklm_guide_archives.md)
- [Periodic And Residual NotebookLM Guide Archives](../technical/periodic_and_residual_notebooklm_guide_archives.md)
- [Isolated Integration Analysis](../technical/isolated_integration_analysis.md)

## Source Of Truth

The main isolated handoff remains:

- `readme.temp.md`

That file should still be treated as the most complete recovery log for the
original archive moves, rename policies, and deferred migration decisions.
