# Integrate Concept NotebookLM Exports For FeedForward, Harmonic, And Periodic Guides

## Overview

This document formalizes the integration of three newly provided `NotebookLM`
export bundles currently stored under `.temp/`:

- `.temp/FeedForward Network/`
- `.temp/Harmonic Regression/`
- `.temp/Periodic Feature Network/`

The user requested that these bundles be integrated into the canonical guide
roots using the same placement and naming convention already used in previous
guide-export integrations.

Repository inspection shows that the corresponding guide roots already contain
the repository-specific exported media named with the `Project` track, while
the new `.temp/` bundles contain educationally neutral filenames and should
therefore be treated as the missing `Concept` track exports.

## Technical Approach

### Classification

The new `.temp/` bundles should be classified as `Concept`-track outputs rather
than `Project`-track outputs because:

- the three guide roots already contain `... - Project ...` media;
- the new filenames are neutral and topic-teaching oriented rather than
  repository-role oriented;
- the user explicitly described them as generated from the respective
  `concept_video_package` folders.

### Integration Mapping

Each `.temp/` bundle should be mapped into the corresponding canonical guide
root:

- `.temp/FeedForward Network/`
  -> `doc/guide/FeedForward Network/`
- `.temp/Harmonic Regression/`
  -> `doc/guide/Harmonic Regression/`
- `.temp/Periodic Feature Network/`
  -> `doc/guide/Periodic Feature Network/`

### Canonical Renaming Policy

The imported files should be renamed to the guide-local `Concept` export naming
pattern already established in the repository:

- `<Guide Name> - Concept Video Overview.mp4`
- `<Guide Name> - Concept Mind Map.png`
- `<Guide Name> - Concept Infographic.png`
- `<Guide Name> - Concept Slides.pdf`
- `<Guide Name> - Concept Slides.pptx`
- `<Guide Name> - Concept Supporting Brief.pdf`

The temporary original filenames should not remain as canonical artifacts in
the guide roots.

### Source-To-Target Filename Mapping

#### `FeedForward Network`

- `Reti_FeedForward.mp4`
  -> `FeedForward Network - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `FeedForward Network - Concept Mind Map.png`
- `unnamed.png`
  -> `FeedForward Network - Concept Infographic.png`
- `FeedForward_Baseline.pdf`
  -> `FeedForward Network - Concept Slides.pdf`
- `FeedForward_Baseline.pptx`
  -> `FeedForward Network - Concept Slides.pptx`
- `Dalle Macchine ai Numeri_ Comprendere la Mappatura Non Lineare dell'Errore di Trasmissione.pdf`
  -> `FeedForward Network - Concept Supporting Brief.pdf`

#### `Harmonic Regression`

- `Regressione_Armonica.mp4`
  -> `Harmonic Regression - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Harmonic Regression - Concept Mind Map.png`
- `unnamed.png`
  -> `Harmonic Regression - Concept Infographic.png`
- `Harmonic_Regression_for_Transmission_Error.pdf`
  -> `Harmonic Regression - Concept Slides.pdf`
- `Harmonic_Regression_for_Transmission_Error.pptx`
  -> `Harmonic Regression - Concept Slides.pptx`
- `Guida Intuitiva alla Regressione Armonica_ Svelare la Periodicità nei Segnali.pdf`
  -> `Harmonic Regression - Concept Supporting Brief.pdf`

#### `Periodic Feature Network`

- `Rete_a_Feature_Periodiche.mp4`
  -> `Periodic Feature Network - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Periodic Feature Network - Concept Mind Map.png`
- `unnamed.png`
  -> `Periodic Feature Network - Concept Infographic.png`
- `Periodic_Feature_Network.pdf`
  -> `Periodic Feature Network - Concept Slides.pdf`
- `Periodic_Feature_Network.pptx`
  -> `Periodic Feature Network - Concept Slides.pptx`
- `Guida Introduttiva alla Rete a Caratteristiche Periodiche (Periodic Feature Network).pdf`
  -> `Periodic Feature Network - Concept Supporting Brief.pdf`

### Cleanup

After a successful move into the canonical guide roots:

- the imported `.temp/` files for these three bundles should be removed from
  `.temp/`;
- the canonical guide roots should contain both:
  - the existing `Project` exports;
  - the newly integrated `Concept` exports.

## Involved Components

- `README.md`
  Main project document that must reference this technical integration note.
- `.temp/FeedForward Network/`
  Temporary source bundle for the concept exports of the FeedForward Network
  guide.
- `.temp/Harmonic Regression/`
  Temporary source bundle for the concept exports of the Harmonic Regression
  guide.
- `.temp/Periodic Feature Network/`
  Temporary source bundle for the concept exports of the Periodic Feature
  Network guide.
- `doc/guide/FeedForward Network/`
  Canonical target root for the integrated concept exports.
- `doc/guide/Harmonic Regression/`
  Canonical target root for the integrated concept exports.
- `doc/guide/Periodic Feature Network/`
  Canonical target root for the integrated concept exports.

## Implementation Steps

1. Create this technical integration document and register it in `README.md`.
2. Wait for explicit user approval before moving or renaming any files.
3. Move the three `.temp/` bundles into their canonical guide roots.
4. Rename each imported file to the repository `Concept` naming pattern.
5. Remove the temporary source files from `.temp/` after successful
   integration.
6. Verify that each guide root now contains both the existing `Project` exports
   and the newly integrated `Concept` exports.
