# Guide Language Split For NotebookLM Exports

## Overview

The repository currently stores guide-local `NotebookLM` exports directly under
each topic root in `doc/guide/<Guide Name>/`, for example:

- `FeedForward Network - Concept Slides.pdf`
- `FeedForward Network - Concept Video Overview.mp4`
- `FeedForward Network - Project Slides.pdf`

The user added new `.temp/<Guide Name>/` folders containing English equivalents
of the concept-video deliverables generated from `concept_video_package/`,
excluding the mind map.

This creates a structural problem in the current guide layout:

- the current guide roots do not encode language explicitly;
- current exported filenames do not encode language explicitly;
- importing the English exports into the current root as-is would mix Italian
  and English deliverables under the same flat namespace.

The repository therefore needs a clean language-aware organization before the
English exports are integrated.

## Technical Approach

### Current Constraints

- The current guide roots already contain canonical authored documents such as
  `<Guide Name>.md` and `<Guide Name>.pdf`.
- The current guide roots also already contain established `concept` and
  `project` export artifacts, plus guide-local `concept_video_package/` and
  `project_video_package/`.
- Existing links and human expectations likely already depend on the current
  guide-root structure.
- The newly added English exports currently exist only in `.temp/`, with
  temporary filenames such as:
  - `FeedForward_Baseline.pdf`
  - `The_FeedForward_Network.mp4`
  - `unnamed.png`

### Option A: Per-Guide Language Subfolders For Exported Media

Keep the current guide root as the canonical topic root, and move generated
media exports into language-specific subfolders inside each guide:

- `doc/guide/<Guide Name>/localized/italian/concept/`
- `doc/guide/<Guide Name>/localized/italian/project/`
- `doc/guide/<Guide Name>/localized/english/concept/`
- `doc/guide/<Guide Name>/localized/english/project/`

Under this option:

- the authored guide Markdown/PDF and package folders remain in the topic root;
- generated media exports are removed from the topic root and placed under the
  localized subfolders;
- each imported file is renamed to an explicit repository-owned filename such as
  `<Guide Name> - Italian Concept Slides.pdf` or
  `<Guide Name> - English Concept Video Overview.mp4`.

Advantages:

- minimal disruption to the canonical guide root;
- explicit language split;
- future-ready for both concept and project exports;
- avoids top-level filename collisions.

Disadvantages:

- requires moving the current Italian exports out of the guide root;
- existing links to root-level media exports would need to be updated.

### Option B: Keep Current Italian Exports At Root, Add Only English Subfolders

Keep the current root-level exports as the implicit Italian/default set, and add
only an English export subfolder such as:

- `doc/guide/<Guide Name>/localized/english/concept/`

Advantages:

- smallest immediate change;
- preserves all current paths for the already integrated exports.

Disadvantages:

- leaves the repository asymmetrical;
- Italian remains implicit while English becomes explicit;
- future maintenance becomes harder because the root still mixes authored guide
  files with generated media.

### Option C: Split Languages At The Documentation Top Level

Create top-level trees such as:

- `doc/guide_italian/`
- `doc/guide_english/`

Advantages:

- very explicit language separation.

Disadvantages:

- duplicates the entire guide tree;
- forces large-scale link and documentation changes;
- mixes authored-guide language concerns with media-export organization;
- highest migration cost and highest risk.

### Recommended Direction

Recommend **Option A**.

It gives a clean long-term structure without redefining the guide roots
themselves. The guide root remains the canonical home of:

- authored guide Markdown/PDF;
- assets;
- `concept_video_package/`;
- `project_video_package/`.

Generated `NotebookLM` media exports then move into a dedicated language-aware
area under each guide root.

Recommended target structure per guide:

- `doc/guide/<Guide Name>/<Guide Name>.md`
- `doc/guide/<Guide Name>/<Guide Name>.pdf`
- `doc/guide/<Guide Name>/assets/`
- `doc/guide/<Guide Name>/concept_video_package/`
- `doc/guide/<Guide Name>/project_video_package/`
- `doc/guide/<Guide Name>/localized/italian/concept/`
- `doc/guide/<Guide Name>/localized/italian/project/`
- `doc/guide/<Guide Name>/localized/english/concept/`
- `doc/guide/<Guide Name>/localized/english/project/`

For the current approved integration scope, only these moves would be required:

1. create `localized/italian/concept/` under each guide and move the existing
   Italian concept exports there;
2. create `localized/english/concept/` under each guide and import the English
   concept exports from `.temp/`;
3. normalize filenames so they explicitly declare guide name, language, track,
   and artifact type;
4. leave project exports untouched for now unless the user explicitly extends
   the migration to them in the same pass.

This keeps the initial integration scope bounded while still establishing the
final language-aware pattern.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/guide/<Guide Name>/`
  Existing topic roots that need a language-aware export structure.
- `.temp/<Guide Name>/`
  Temporary source location of the new English concept exports.
- future guide-local targets after approval:
  - `doc/guide/<Guide Name>/localized/italian/concept/`
  - `doc/guide/<Guide Name>/localized/english/concept/`

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before reorganizing any guide-local export
   files.
3. After approval, create the guide-local localized export subfolders for the
   approved language/track scope.
4. Move and rename the existing root-level Italian concept exports into the new
   Italian concept subfolders.
5. Import and rename the English concept exports from `.temp/` into the new
   English concept subfolders.
6. Update the relevant guide documentation references so the reorganized export
   locations remain discoverable.
7. Run Markdown checks on the touched Markdown files before closing the task.
