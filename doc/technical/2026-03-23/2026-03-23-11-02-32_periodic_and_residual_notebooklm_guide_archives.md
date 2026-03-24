# Periodic And Residual NotebookLM Guide Archives

## Overview

This document extends the existing isolated import workflow for `NotebookLM`
exported guide bundles.

Two additional guide folders were added under `.temp/`, and the user requested
that they be organized exactly like the previously archived guides.

The newly added bundles are:

- `Periodic Feature Network`
- `Residual Harmonic Network`

The goal is to analyze them, archive them under the same standalone import
structure already used for the other `NotebookLM` exports, and update the
isolated handoff so the synchronized integration phase can later place them in
the canonical guide tree.

## Technical Approach

### Current File Inventory

Each of the two new bundles matches the expected imported-guide artifact family:

- one mind map image;
- one infographic image;
- one presentation deck in `.pptx`;
- one presentation export in `.pdf`;
- one supporting brief in `.pdf`;
- one video overview in `.mp4`.

#### Periodic Feature Network

- `La Magia della Periodicità_ Guida alla Periodic Feature Network.pdf`
- `La_Rete_a_Caratteristiche_Periodiche.mp4`
- `NotebookLM Mind Map.png`
- `Periodic_Feature_Network.pdf`
- `Periodic_Feature_Network.pptx`
- `unnamed.png`

#### Residual Harmonic Network

- `La Residual Harmonic Network_ Un Ponte tra Fisica e Deep Learning attraverso la Decomposizione Additiva.pdf`
- `NotebookLM Mind Map.png`
- `Residual_Harmonic_Network.pdf`
- `Residual_Harmonic_Network.pptx`
- `Rete_Armonica_Residua.mp4`
- `unnamed.png`

### Standalone Archive Extension

The existing isolated archive root remains:

- `doc/imports/notebooklm_exports/`

The two new topic folders should be:

- `doc/imports/notebooklm_exports/periodic_feature_network/`
- `doc/imports/notebooklm_exports/residual_harmonic_network/`

Each folder should use the same internal structure:

- `pdf/`
- `slides/`
- `video/`
- `images/`

### Recommended Archive Rename Map

#### Periodic Feature Network

- `La Magia della Periodicità_ Guida alla Periodic Feature Network.pdf`
  -> `periodic_feature_network_notebooklm_supporting_brief.pdf`
- `La_Rete_a_Caratteristiche_Periodiche.mp4`
  -> `periodic_feature_network_notebooklm_video_overview.mp4`
- `NotebookLM Mind Map.png`
  -> `periodic_feature_network_notebooklm_mind_map.png`
- `Periodic_Feature_Network.pdf`
  -> `periodic_feature_network_notebooklm_slides.pdf`
- `Periodic_Feature_Network.pptx`
  -> `periodic_feature_network_notebooklm_slides.pptx`
- `unnamed.png`
  -> `periodic_feature_network_notebooklm_supporting_figure.png`

#### Residual Harmonic Network

- `La Residual Harmonic Network_ Un Ponte tra Fisica e Deep Learning attraverso la Decomposizione Additiva.pdf`
  -> `residual_harmonic_network_notebooklm_supporting_brief.pdf`
- `NotebookLM Mind Map.png`
  -> `residual_harmonic_network_notebooklm_mind_map.png`
- `Residual_Harmonic_Network.pdf`
  -> `residual_harmonic_network_notebooklm_slides.pdf`
- `Residual_Harmonic_Network.pptx`
  -> `residual_harmonic_network_notebooklm_slides.pptx`
- `Rete_Armonica_Residua.mp4`
  -> `residual_harmonic_network_notebooklm_video_overview.mp4`
- `unnamed.png`
  -> `residual_harmonic_network_notebooklm_supporting_figure.png`

### Future Canonical Guide Mapping

During the later synchronized integration phase, these archives should map to:

- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`

Until that later integration phase, the imported files should remain in the
standalone archive tree so their provenance stays explicit and conflict-safe.

## Involved Components

- `.temp/Periodic Feature Network/`
- `.temp/Residual Harmonic Network/`
- `doc/imports/notebooklm_exports/`
- `readme.temp.md`
- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
- `doc/technical/2026-03-22/2026-03-22-09-50-07_additional_notebooklm_guide_archives.md`

## Implementation Steps

1. Create this new standalone technical note for the two additional imported
   guide bundles.
2. Create the two new archive topic folders under
   `doc/imports/notebooklm_exports/`.
3. Move the imported files out of `.temp/` into the archive folders using the
   normalized archive filenames listed above.
4. Update `readme.temp.md` with the new inventories and the future canonical
   mapping.
5. Keep shared repository index files untouched until the synchronized
   post-campaign integration phase.
