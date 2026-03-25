# NotebookLM Export Archives

The recovered `NotebookLM` assets are no longer stored as the primary canonical
content under the former isolated import root `doc/imports/notebooklm_exports/`.

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

## Historical Provenance Note

The former root:

- `doc/imports/notebooklm_exports/`

has now been retired from the live repository tree.

The old isolated-handoff archive that temporarily preserved a provenance
manifest has also been removed from the repository. The retained historical
decision trail now lives in the technical documents that described:

- the original isolated archive-ingestion plan;
- the later synchronized migration into `doc/guide/`;
- the final retirement of the old isolated handoff model.

## Decision Trail

The detailed archive-ingestion and reconciliation decisions are documented in:

- [NotebookLM Export Ingestion And Archive](../technical/notebooklm_export_ingestion.md)
- [Additional NotebookLM Guide Archives](../technical/additional_notebooklm_guide_archives.md)
- [Periodic And Residual NotebookLM Guide Archives](../technical/periodic_and_residual_notebooklm_guide_archives.md)
- [Isolated Integration Analysis](../technical/isolated_integration_analysis.md)

## Historical Cleanup Direction

The repository no longer keeps the old isolated handoff log as a physical
archive artifact. Future isolated work is tracked through the explicit
session-based workflow under `isolated/active/` and `isolated/completed/`.
