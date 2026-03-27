# Concept Video Package Command Archive And Reuse Template

## Overview

The user provided a temporary source file:

- `.temp/comandi_concept_video_package.txt`

This file contains the already-generated NotebookLM command texts used to ask
for video generation from each guide-local `concept_video_package`.

The same command family exists in two language variants for each topic:

- Italian version beginning with
  `Create a didactic video overview in Italian for beginners and junior engineers.`
- English version beginning with
  `Create a didactic video overview in English for beginners and junior engineers.`

The user requested that these commands be preserved as-is inside a repository-
owned technical document so they can serve as a stable template for future
models and future guide topics.

## Technical Approach

The repository should convert the temporary command collection into canonical
documentation rather than leave it inside `.temp/`.

The intended result should:

- preserve the commands without semantic rewriting;
- keep the command structure clearly reusable for future concept-video topics;
- make the bilingual pattern explicit;
- extract the common command skeleton so a new topic can receive the same
  treatment quickly in the future.

The repository-owned deliverable should likely include:

- the archived commands as historical examples;
- a generalized reusable template with clearly marked placeholders;
- guidance on how to derive a new topic command from the archived pattern.

This is documentation and workflow formalization work. It does not yet generate
new NotebookLM commands for future models automatically.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `.temp/comandi_concept_video_package.txt`
  Temporary source file containing the current concept-video commands.
- future repository-owned command archive document
  The canonical location that will preserve the commands and their reusable
  pattern after approval.
- guide-local `concept_video_package/` folders under `doc/guide/`
  The source-package roots from which these NotebookLM commands are derived.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Wait for explicit user approval before converting the temporary command list
   into a canonical repository-owned document.
3. After approval, read `.temp/comandi_concept_video_package.txt` as the source
   of truth and preserve the commands as-is in a stable document.
4. Record both language variants explicitly:
   - Italian
   - English
5. Extract a reusable future-topic template from the archived examples so a new
   model guide can receive an analogous `concept_video_package` command quickly.
6. Report completion and wait for explicit user approval before any commit.
