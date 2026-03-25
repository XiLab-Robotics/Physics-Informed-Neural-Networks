# Integrate Concept NotebookLM Exports For Three Guides

## Overview

This document formalizes the integration of three newly provided `NotebookLM`
export bundles currently stored under `.temp/`:

- `.temp/Neural Network Foundations/`
- `.temp/TE Model Curriculum/`
- `.temp/Training, Validation and Testing/`

The user requested that these bundles be:

- renamed consistently;
- integrated into the canonical guide roots;
- stored in their proper final locations.

Repository inspection shows that the corresponding guide roots already contain
the repository-specific exported media named with the `Project` track, while the
new `.temp/` bundles contain educationally neutral filenames and should
therefore be treated as the missing `Concept` track exports.

## Technical Approach

### Classification

The new `.temp/` bundles should be classified as `Concept`-track outputs rather
than `Project`-track outputs because:

- the three guide roots already contain `... - Project ...` media;
- the new filenames are neutral and topic-teaching oriented rather than
  repository-role oriented;
- the user explicitly described these as the newly generated generalist videos.

### Integration Mapping

Each `.temp/` bundle should be mapped into the corresponding canonical guide
root:

- `.temp/Neural Network Foundations/`
  -> `doc/guide/Neural Network Foundations/`
- `.temp/TE Model Curriculum/`
  -> `doc/guide/TE Model Curriculum/`
- `.temp/Training, Validation and Testing/`
  -> `doc/guide/Training, Validation, And Testing/`

### Canonical Renaming Policy

The imported files should be renamed to the guide-local `Concept` export naming
pattern already established in the repository:

- `<Guide Name> - Concept Video Overview.mp4`
- `<Guide Name> - Concept Mind Map.png`
- `<Guide Name> - Concept Infographic.png`
- `<Guide Name> - Concept Slides.pdf`
- `<Guide Name> - Concept Slides.pptx`
- `<Guide Name> - Concept Supporting Brief.pdf`

The temporary original filenames should not remain as canonical artifacts in the
guide roots.

### Source-To-Target Filename Mapping

#### `Neural Network Foundations`

- `Fondamenti_Reti_Neurali.mp4`
  -> `Neural Network Foundations - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Neural Network Foundations - Concept Mind Map.png`
- `unnamed.png`
  -> `Neural Network Foundations - Concept Infographic.png`
- `TE_Neural_Network_Engineering.pdf`
  -> `Neural Network Foundations - Concept Slides.pdf`
- `TE_Neural_Network_Engineering.pptx`
  -> `Neural Network Foundations - Concept Slides.pptx`
- `Il Ciclo dell'Apprendimento_ Come le Macchine Imparano dai Dati.pdf`
  -> `Neural Network Foundations - Concept Supporting Brief.pdf`

#### `TE Model Curriculum`

- `Curriculum_dei_Modelli_TE.mp4`
  -> `TE Model Curriculum - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `TE Model Curriculum - Concept Mind Map.png`
- `unnamed.png`
  -> `TE Model Curriculum - Concept Infographic.png`
- `The_Torque_Error_Blueprint.pdf`
  -> `TE Model Curriculum - Concept Slides.pdf`
- `The_Torque_Error_Blueprint.pptx`
  -> `TE Model Curriculum - Concept Slides.pptx`
- `Guida Comparativa alle Architetture Neurali per l'Errore di Trasmissione (TE).pdf`
  -> `TE Model Curriculum - Concept Supporting Brief.pdf`

#### `Training, Validation, And Testing`

- `Training,_Validazione,_Test.mp4`
  -> `Training, Validation, And Testing - Concept Video Overview.mp4`
- `NotebookLM Mind Map.png`
  -> `Training, Validation, And Testing - Concept Mind Map.png`
- `unnamed.png`
  -> `Training, Validation, And Testing - Concept Infographic.png`
- `The_Filtered_Pipeline.pdf`
  -> `Training, Validation, And Testing - Concept Slides.pdf`
- `The_Filtered_Pipeline.pptx`
  -> `Training, Validation, And Testing - Concept Slides.pptx`
- `Guida Concettuale_ L'Arte di Dividere i Dati – Perché un Solo Dataset non Basta.pdf`
  -> `Training, Validation, And Testing - Concept Supporting Brief.pdf`

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
- `.temp/Neural Network Foundations/`
  Temporary source bundle for the concept exports of the Neural Network
  Foundations guide.
- `.temp/TE Model Curriculum/`
  Temporary source bundle for the concept exports of the TE Model Curriculum
  guide.
- `.temp/Training, Validation and Testing/`
  Temporary source bundle for the concept exports of the Training, Validation,
  And Testing guide.
- `doc/guide/Neural Network Foundations/`
  Canonical target root for the integrated concept exports.
- `doc/guide/TE Model Curriculum/`
  Canonical target root for the integrated concept exports.
- `doc/guide/Training, Validation, And Testing/`
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
