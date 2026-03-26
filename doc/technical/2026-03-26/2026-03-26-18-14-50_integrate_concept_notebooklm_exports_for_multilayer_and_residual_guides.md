# Integrate Concept NotebookLM Exports For Multilayer And Residual Guides

## Overview

This document formalizes the integration of two newly provided `NotebookLM`
export bundles currently stored under `.temp/`:

- `.temp/Multilayer Perceptrons/`
- `.temp/Residual Harmonic Network/`

The user requested that these bundles be integrated into the canonical guide
roots using the same placement and naming convention already used in previous
guide-export integrations.

Repository inspection shows two different target states:

- `Residual Harmonic Network` currently has only the `Project` media exports and
  therefore needs the missing `Concept` track to be added.
- `Multilayer Perceptrons` is a known exception root that already contains
  `Concept`-track media files, so the new `.temp/` bundle should refresh those
  canonical concept exports in place rather than creating a second parallel set.

## Technical Approach

### Classification

Both new `.temp/` bundles should be classified as `Concept`-track outputs
because:

- their filenames are neutral and topic-teaching oriented rather than
  repository-role oriented;
- the user explicitly described them as generated from the respective
  `concept_video_package` folders;
- `Residual Harmonic Network` already has `Project` exports;
- `Multilayer Perceptrons` already uses the canonical `Concept` naming pattern.

### Integration Mapping

Each `.temp/` bundle should be mapped into the corresponding canonical guide
root:

- `.temp/Multilayer Perceptrons/`
  -> `doc/guide/Multilayer Perceptrons/`
- `.temp/Residual Harmonic Network/`
  -> `doc/guide/Residual Harmonic Network/`

### Canonical Renaming Policy

The imported files should use the guide-local `Concept` export naming pattern:

- `<Guide Name> - Concept Video Overview.mp4`
- `<Guide Name> - Concept Mind Map.png`
- `<Guide Name> - Concept Infographic.png`
- `<Guide Name> - Concept Slides.pdf`
- `<Guide Name> - Concept Slides.pptx`
- `<Guide Name> - Concept Supporting Brief.pdf`

For `Residual Harmonic Network`, these files will be new canonical additions.

For `Multilayer Perceptrons`, these filenames already exist canonically, so the
incoming files should replace the current concept-track assets in place.

### Source-To-Target Filename Mapping

#### `Multilayer Perceptrons`

- `Capire_i_Multilayer_Perceptron.mp4`
  -> `Multilayer Perceptrons - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Multilayer Perceptrons - Concept Mind Map.png`
- `unnamed.png`
  -> `Multilayer Perceptrons - Concept Infographic.png`
- `Multilayer_Perceptron_Fundamentals.pdf`
  -> `Multilayer Perceptrons - Concept Slides.pdf`
- `Multilayer_Perceptron_Fundamentals.pptx`
  -> `Multilayer Perceptrons - Concept Slides.pptx`
- `Il Cuore dei Modelli Densi_ Una Guida Introduttiva ai Multilayer Perceptrons.pdf`
  -> `Multilayer Perceptrons - Concept Supporting Brief.pdf`

#### `Residual Harmonic Network`

- `Residual_Harmonic_Network.mp4`
  -> `Residual Harmonic Network - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Residual Harmonic Network - Concept Mind Map.png`
- `unnamed.png`
  -> `Residual Harmonic Network - Concept Infographic.png`
- `Residual_Harmonic_Network.pdf`
  -> `Residual Harmonic Network - Concept Slides.pdf`
- `Residual_Harmonic_Network.pptx`
  -> `Residual Harmonic Network - Concept Slides.pptx`
- `La Residual Harmonic Network_ L'Unione tra Ordine e Flessibilità.pdf`
  -> `Residual Harmonic Network - Concept Supporting Brief.pdf`

### Replacement And Cleanup Policy

After successful integration:

- the imported `.temp/` files for both bundles should be removed from `.temp/`;
- `Residual Harmonic Network` should contain both:
  - the existing `Project` exports;
  - the newly integrated `Concept` exports.
- `Multilayer Perceptrons` should continue to expose one canonical `Concept`
  export set, refreshed with the new incoming files rather than duplicated.

## Involved Components

- `README.md`
  Main project document that must reference this technical integration note.
- `.temp/Multilayer Perceptrons/`
  Temporary source bundle for the concept exports of the Multilayer
  Perceptrons guide root.
- `.temp/Residual Harmonic Network/`
  Temporary source bundle for the concept exports of the Residual Harmonic
  Network guide.
- `doc/guide/Multilayer Perceptrons/`
  Canonical target root for refreshing the concept exports.
- `doc/guide/Residual Harmonic Network/`
  Canonical target root for adding the concept exports.

## Implementation Steps

1. Create this technical integration document and register it in `README.md`.
2. Wait for explicit user approval before moving, renaming, or replacing any
   files.
3. Replace the existing canonical `Concept` exports in
   `doc/guide/Multilayer Perceptrons/` with the new `.temp/` bundle.
4. Move the `Residual Harmonic Network` bundle into its canonical guide root.
5. Rename each imported file to the repository `Concept` naming pattern.
6. Remove the temporary source files from `.temp/` after successful
   integration.
7. Verify that:
   - `Multilayer Perceptrons` contains one refreshed canonical `Concept` set;
   - `Residual Harmonic Network` contains both `Project` and `Concept` exports.
