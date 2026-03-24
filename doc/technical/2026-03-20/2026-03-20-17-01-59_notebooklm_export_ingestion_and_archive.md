# NotebookLM Export Ingestion And Archive

## Overview

This document defines the intake workflow for three newly downloaded `NotebookLM` export bundles currently stored under `.temp/`.

The user requested a deep analysis of the downloaded files, plus a safe renaming and relocation plan that does not interfere with the active training campaign running on another machine.

The three current export bundles are:

- `Neural Network Foundations`
- `TE Model Curriculum - From Baselines to Physics-Informed Neural Networks`
- `Multilayer Perceptrons - Foundations of Neural Network Architecture`

Two of these themes already correspond to repository-owned learning guides:

- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`

The third bundle is conceptually adjacent to the existing Wave 1 architecture guide family, but it is not a one-to-one match for a current canonical folder.

Because the active campaign is ongoing and the user explicitly requested standalone work only, the imported `NotebookLM` artifacts should be archived as standalone external outputs rather than merged directly into the canonical guide folders at this stage.

## Technical Approach

### Current File Inventory

The downloaded bundles contain the following file classes:

#### Neural Network Foundations

- long-form presentation PDF: `Neural_Network_Foundations.pdf`
- presentation deck: `Neural_Network_Foundations.pptx`
- video overview: `Reti_Neurali_e_Previsione_TE.mp4`
- mind-map image: `Mind Map.png`
- additional generated image: `unnamed.png`
- short supporting PDF: `Dalla Regressione Lineare ai Neuroni Artificiali_ Un Viaggio nella Predizione dell'Errore di Trasmissione.pdf`

#### TE Model Curriculum

- long-form presentation PDF: `Transmission_Error_Model_Evolution.pdf`
- presentation deck: `Transmission_Error_Model_Evolution.pptx`
- video overview: `Il_Curriculum_dei_Modelli_TE.mp4`
- mind-map image: `Mind Map.png`
- additional generated image: `unnamed.png`
- short supporting PDF: `Panoramica delle Architetture Neurali_ Guida al Curriculum TE.pdf`

#### Multilayer Perceptrons

- long-form presentation PDF: `Harmonic_Neural_Synthesis.pdf`
- presentation deck: `Harmonic_Neural_Synthesis.pptx`
- video overview: `Modellare_Pattern_Periodici.mp4`
- mind-map image: `Mind Map.png`
- additional generated image: `Evoluzione dell'Analisi Armonica.png`
- short supporting PDF: `Oltre la Linea_ Come le Reti Neurali Risolvono l'Enigma dello XOR.pdf`

### Why These Files Should Not Be Merged Directly Into Canonical Guide Folders

The repository already distinguishes between:

- canonical repository-authored learning guides;
- report-local generated assets;
- `NotebookLM` video-guide source packages;
- temporary or imported artifacts.

The downloaded files are not repository-authored guide sources.

They are generated external outputs from `NotebookLM` and should remain identifiable as such.

If they are dropped directly into the existing learning-guide folders, the repository risks mixing:

- canonical Markdown and approved PDF deliverables;
- externally generated presentation decks;
- externally generated video exports;
- raw generated image artifacts with inconsistent names.

That would blur the boundary between authoritative repository documentation and imported supporting media.

### Recommended Standalone Archive Layout

The correct standalone location is a dedicated import archive:

- `doc/imports/notebooklm_exports/`

Each bundle should then be stored under a normalized topic folder:

- `doc/imports/notebooklm_exports/neural_network_foundations/`
- `doc/imports/notebooklm_exports/te_model_curriculum/`
- `doc/imports/notebooklm_exports/multilayer_perceptrons/`

Inside each topic folder, the artifacts should be split by type:

- `pdf/`
- `slides/`
- `video/`
- `images/`

This preserves:

- standalone isolation during the active campaign;
- clean provenance for imported assets;
- later selective integration into canonical guide folders after the campaign ends.

### Recommended File Renaming Policy

All imported files should receive:

- English-first normalized filenames;
- explicit topic prefixes;
- artifact-type clarity;
- no generic names such as `Mind Map.png` or `unnamed.png`.

Proposed rename map:

#### Neural Network Foundations

- `Neural_Network_Foundations.pdf`
  -> `neural_network_foundations_notebooklm_slides.pdf`
- `Neural_Network_Foundations.pptx`
  -> `neural_network_foundations_notebooklm_slides.pptx`
- `Reti_Neurali_e_Previsione_TE.mp4`
  -> `neural_network_foundations_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `neural_network_foundations_notebooklm_mind_map.png`
- `unnamed.png`
  -> `neural_network_foundations_notebooklm_supporting_figure.png`
- `Dalla Regressione Lineare ai Neuroni Artificiali_ Un Viaggio nella Predizione dell'Errore di Trasmissione.pdf`
  -> `neural_network_foundations_notebooklm_supporting_brief.pdf`

#### TE Model Curriculum

- `Transmission_Error_Model_Evolution.pdf`
  -> `te_model_curriculum_notebooklm_slides.pdf`
- `Transmission_Error_Model_Evolution.pptx`
  -> `te_model_curriculum_notebooklm_slides.pptx`
- `Il_Curriculum_dei_Modelli_TE.mp4`
  -> `te_model_curriculum_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `te_model_curriculum_notebooklm_mind_map.png`
- `unnamed.png`
  -> `te_model_curriculum_notebooklm_supporting_figure.png`
- `Panoramica delle Architetture Neurali_ Guida al Curriculum TE.pdf`
  -> `te_model_curriculum_notebooklm_supporting_brief.pdf`

#### Multilayer Perceptrons

- `Harmonic_Neural_Synthesis.pdf`
  -> `multilayer_perceptrons_notebooklm_slides.pdf`
- `Harmonic_Neural_Synthesis.pptx`
  -> `multilayer_perceptrons_notebooklm_slides.pptx`
- `Modellare_Pattern_Periodici.mp4`
  -> `multilayer_perceptrons_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `multilayer_perceptrons_notebooklm_mind_map.png`
- `Evoluzione dell'Analisi Armonica.png`
  -> `multilayer_perceptrons_notebooklm_supporting_figure.png`
- `Oltre la Linea_ Come le Reti Neurali Risolvono l'Enigma dello XOR.pdf`
  -> `multilayer_perceptrons_notebooklm_supporting_brief.pdf`

### Post-Campaign Integration Path

After the active campaign ends, the archive can be reviewed for selective integration.

The likely future mapping is:

- `neural_network_foundations` archive
  -> selectively referenced from `doc/reports/analysis/learning_guides/Neural Network Foundations/`
- `te_model_curriculum` archive
  -> selectively referenced from `doc/reports/analysis/learning_guides/TE Model Curriculum/`
- `multilayer_perceptrons` archive
  -> either promoted to a new learning-guide family or split into Wave 1 model-family supporting media

Until that later review, the archive should remain standalone and should not overwrite any existing canonical guide asset.

## Involved Components

- `.temp/`
  Current staging location of the downloaded `NotebookLM` export bundles.
- `doc/imports/notebooklm_exports/`
  Proposed standalone destination root for imported external `NotebookLM` outputs.
- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
  Existing canonical guide related to one imported bundle.
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`
  Existing canonical guide related to one imported bundle.
- `doc/reports/analysis/learning_guides/`
  Parent location for future post-campaign selective integration decisions.
- `README.md`
  Main project document that must reference this technical planning note.
- `doc/README.md`
  Internal documentation index that should also reference this technical planning note.

## Implementation Steps

1. Create this technical planning document and register it in `README.md` and `doc/README.md`.
2. Wait for explicit user approval before renaming or moving any downloaded file.
3. After approval, create `doc/imports/notebooklm_exports/` and the three normalized topic folders.
4. Move the downloaded artifacts out of `.temp/` into the archive folders and apply the normalized filenames listed in this document.
5. Produce a final inventory report that maps original paths to archived paths.
6. Leave canonical learning-guide folders unchanged until the active campaign ends and the user explicitly requests integration.
