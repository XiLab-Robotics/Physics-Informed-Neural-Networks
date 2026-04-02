# Additional NotebookLM Guide Archives

## Overview

This document extends the existing isolated import workflow for `NotebookLM` exported guide bundles.

Three additional guide folders were added under `.temp/` and the user requested that they be treated exactly like the previously archived guides.

The newly added bundles are:

- `FeedForward Network`
- `Harmonic Regression`
- `Training, Validation, and Testing Workflow for TE Models`

The goal is to analyze them, archive them under the same standalone import structure, and update the isolated handoff so the synchronized integration phase can later move them into the canonical guide folders under `doc/guide/`.

## Technical Approach

### Current File Inventory

Each of the three new bundles matches the expected imported-guide artifact family:

- one mind map image;
- one infographic image;
- one presentation deck in `.pptx`;
- one presentation export in `.pdf`;
- one supporting brief in `.pdf`;
- one video overview in `.mp4`.

#### FeedForward Network

- `FeedForward_Network_Baseline.pdf`
- `FeedForward_Network_Baseline.pptx`
- `Guida ai Concetti Fondamentali_ Il Neurone Artificiale nella Meccanica Industriale.pdf`
- `La_Rete_FeedForward.mp4`
- `NotebookLM Mind Map.png`
- `unnamed.png`

#### Harmonic Regression

- `Dall'Ingranaggio alla Funzione_ Guida alla Regressione Armonica per l'Errore di Trasmissione.pdf`
- `Harmonic_Regression_Blueprint.pdf`
- `Harmonic_Regression_Blueprint.pptx`
- `NotebookLM Mind Map.png`
- `Regressione_Armonica.mp4`
- `unnamed.png`

#### Training, Validation, and Testing Workflow for TE Models

- `Addestramento,_Validazione,_Test.mp4`
- `Manuale dei Fondamenti Dati_ L'Arte della Validazione nell'Errore di Trasmissione.pdf`
- `NotebookLM Mind Map.png`
- `TE_Dataset_Discipline.pdf`
- `TE_Dataset_Discipline.pptx`
- `unnamed.png`

### Standalone Archive Extension

The existing isolated archive root remains:

- `doc/imports/notebooklm_exports/`

The three new topic folders should be:

- `doc/imports/notebooklm_exports/feedforward_network/`
- `doc/imports/notebooklm_exports/harmonic_regression/`
- `doc/imports/notebooklm_exports/training_validation_and_testing/`

Each folder should use the same internal structure:

- `pdf/`
- `slides/`
- `video/`
- `images/`

### Recommended Archive Rename Map

#### FeedForward Network

- `FeedForward_Network_Baseline.pdf`
  -> `feedforward_network_notebooklm_slides.pdf`
- `FeedForward_Network_Baseline.pptx`
  -> `feedforward_network_notebooklm_slides.pptx`
- `Guida ai Concetti Fondamentali_ Il Neurone Artificiale nella Meccanica Industriale.pdf`
  -> `feedforward_network_notebooklm_supporting_brief.pdf`
- `La_Rete_FeedForward.mp4`
  -> `feedforward_network_notebooklm_video_overview.mp4`
- `NotebookLM Mind Map.png`
  -> `feedforward_network_notebooklm_mind_map.png`
- `unnamed.png`
  -> `feedforward_network_notebooklm_supporting_figure.png`

#### Harmonic Regression

- `Dall'Ingranaggio alla Funzione_ Guida alla Regressione Armonica per l'Errore di Trasmissione.pdf`
  -> `harmonic_regression_notebooklm_supporting_brief.pdf`
- `Harmonic_Regression_Blueprint.pdf`
  -> `harmonic_regression_notebooklm_slides.pdf`
- `Harmonic_Regression_Blueprint.pptx`
  -> `harmonic_regression_notebooklm_slides.pptx`
- `NotebookLM Mind Map.png`
  -> `harmonic_regression_notebooklm_mind_map.png`
- `Regressione_Armonica.mp4`
  -> `harmonic_regression_notebooklm_video_overview.mp4`
- `unnamed.png`
  -> `harmonic_regression_notebooklm_supporting_figure.png`

#### Training, Validation, and Testing Workflow for TE Models

- `Addestramento,_Validazione,_Test.mp4`
  -> `training_validation_and_testing_notebooklm_video_overview.mp4`
- `Manuale dei Fondamenti Dati_ L'Arte della Validazione nell'Errore di Trasmissione.pdf`
  -> `training_validation_and_testing_notebooklm_supporting_brief.pdf`
- `NotebookLM Mind Map.png`
  -> `training_validation_and_testing_notebooklm_mind_map.png`
- `TE_Dataset_Discipline.pdf`
  -> `training_validation_and_testing_notebooklm_slides.pdf`
- `TE_Dataset_Discipline.pptx`
  -> `training_validation_and_testing_notebooklm_slides.pptx`
- `unnamed.png`
  -> `training_validation_and_testing_notebooklm_supporting_figure.png`

### Future Canonical Guide Mapping

During the later synchronized integration phase, these archives should be mapped to:

- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Training, Validation, And Testing/`

For the third bundle, the imported folder name and the future canonical guide name are not identical.

The synchronized integration phase must normalize:

- imported source theme:
  `Training, Validation, and Testing Workflow for TE Models`
- canonical guide destination:
  `Training, Validation, And Testing`

## Involved Components

- `.temp/FeedForward Network/`
- `.temp/Harmonic Regression/`
- `.temp/Training, Validation, and Testing Workflow for TE Models/`
- `doc/imports/notebooklm_exports/`
- `readme.temp.md`
- `doc/technical/2026-03/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`

## Implementation Steps

1. Create this new standalone technical note for the additional imported guide bundles.
2. Create the three new archive topic folders under `doc/imports/notebooklm_exports/`.
3. Move the imported files out of `.temp/` into the archive folders using the normalized archive filenames listed above.
4. Update `readme.temp.md` with the new inventories and the future canonical mapping.
5. Keep shared repository index files untouched until the synchronized post-campaign integration phase.
