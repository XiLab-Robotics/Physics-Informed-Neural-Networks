# NotebookLM Export Archives

The recovered `NotebookLM` assets are no longer stored as the primary canonical
content under `doc/imports/notebooklm_exports/`.

They have now been migrated into the corresponding guide folders under:

- `doc/guide/`

## Migrated Guide Targets

- `doc/guide/Neural Network Foundations/`
- `doc/guide/Training, Validation, And Testing/`
- `doc/guide/TE Model Curriculum/`
- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`
- `doc/guide/Multilayer Perceptrons/`

Each migrated guide-local media set now uses readable collision-safe names:

- `Mind Map.png`
- `Infographic.png`
- `Slides.pdf`
- `Slides.pptx`
- `Supporting Brief.pdf`
- `Video Overview.mp4`

## Residual Provenance Root

The root:

- `doc/imports/notebooklm_exports/`

is now retained only as a lightweight provenance manifest location. It is no
longer the canonical storage root for the imported media files themselves.

## Decision Trail

The detailed archive-ingestion and reconciliation decisions are documented in:

- [NotebookLM Export Ingestion And Archive](../technical/notebooklm_export_ingestion.md)
- [Additional NotebookLM Guide Archives](../technical/additional_notebooklm_guide_archives.md)
- [Periodic And Residual NotebookLM Guide Archives](../technical/periodic_and_residual_notebooklm_guide_archives.md)
- [Isolated Integration Analysis](../technical/isolated_integration_analysis.md)

## Source Of Truth

The main isolated handoff remains:

- `readme.temp.md`

That file is still the most complete recovery log for the original isolated
archive moves, rename policies, and later synchronized migration obligations.
