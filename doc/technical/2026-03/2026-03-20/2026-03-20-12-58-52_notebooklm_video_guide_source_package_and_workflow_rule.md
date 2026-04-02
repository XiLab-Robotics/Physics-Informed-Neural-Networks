# NotebookLM Video Guide Source Package And Workflow Rule

## Overview

This document defines the requested extension of the repository documentation workflow from static learning guides to AI-assisted video guides generated with Google `NotebookLM`.

The user requested three connected outcomes:

- learn what source materials `NotebookLM` currently accepts and how its video-guide workflow is driven;
- define which repository-authored documents should be prepared so `NotebookLM` can generate stronger video guides from the approved learning guides;
- add a persistent repository rule stating that, after a learning-guide PDF is completed, the repository should prepare the video-guide source package and then proceed to video-guide generation only after explicit user approval.

This request does not yet ask for the actual video guides to be generated.

The immediate goal is to formalize the workflow and define the document package that should exist before `NotebookLM` is used as the video-guide generation layer.

## Technical Approach

### Verified NotebookLM Constraints And Capabilities

Based on the current official Google `NotebookLM` documentation and product updates, `NotebookLM` supports multiple source types relevant to this repository, including:

- `PDF`;
- `Google Docs`;
- `Google Slides`;
- `Google Sheets`;
- images;
- `Microsoft Word`, `Text`, `Markdown`, and `PDF` files;
- web URLs;
- public `YouTube` URLs;
- audio files;
- copied text.

The current official `NotebookLM` guidance also states that:

- a source is treated as a static imported copy used to ground the notebook outputs;
- `Video Overviews` are generated from selected notebook sources;
- the user can customize the resulting video by focusing it on selected aspects of the sources.

This means the repository should not rely on one monolithic document only.

Instead, it should prepare a small source package with complementary roles:

- one canonical detailed guide;
- one compressed teaching structure;
- one terminology and fact-consistency layer;
- one video-oriented framing layer.

### Why A Source Package Is Better Than A Single File

`NotebookLM` is source-grounded.

That makes source quality more important than prompt cleverness.

If the notebook receives only one long explanatory PDF, it may still generate a useful overview, but the result is less controllable.

A better approach is to upload multiple well-scoped sources that each provide one clean responsibility:

- authoritative content;
- structured sequencing;
- terminology control;
- visual and pedagogical framing;
- narration emphasis.

This improves:

- factual consistency;
- chapter ordering;
- vocabulary stability;
- controllability of the final video overview.

### Proposed Repository-Owned Source Package For Each Learning Guide

For every approved learning guide, the repository should prepare the following source set before `NotebookLM` video generation.

#### 1. Canonical Learning Guide PDF

Purpose:

- provide the full polished long-form source;
- preserve the approved diagrams and final typography;
- act as the primary authoritative document for the notebook.

Status in workflow:

- required.

#### 2. Canonical Learning Guide Markdown

Purpose:

- provide a text-native version that is easier for the notebook to segment;
- preserve heading structure more explicitly;
- act as a fallback textual source when PDF layout introduces noise.

Status in workflow:

- required.

#### 3. Video Guide Source Brief

Purpose:

- compress the full learning guide into a source specifically shaped for video generation;
- define target audience, desired depth, narration style, and chapter sequence;
- tell `NotebookLM` what the video should emphasize and what it should avoid.

Recommended contents:

- target audience;
- learning objectives;
- ordered chapter list;
- required takeaways per chapter;
- concepts that must not be omitted;
- concepts that should remain brief.

Status in workflow:

- required.

#### 4. Terminology And Definitions Sheet

Purpose:

- keep vocabulary stable across narration;
- avoid inconsistent naming between similar concepts;
- preserve TE-domain wording and repository conventions.

Recommended contents:

- term;
- short definition;
- allowed synonym if any;
- forbidden ambiguous wording if needed;
- TE-specific interpretation where relevant.

Status in workflow:

- required.

#### 5. Video Narration Outline

Purpose:

- provide a source that already resembles a spoken educational sequence;
- help `NotebookLM` create a more coherent explanation arc;
- reduce the risk of uneven pacing.

Recommended contents:

- opening framing;
- chapter-by-chapter narration bullets;
- transitions between chapters;
- closing recap.

Status in workflow:

- strongly recommended.

#### 6. Figure And Visual Reference Sheet

Purpose:

- explain what each approved diagram is supposed to communicate;
- give the notebook a cleaner mapping between visual assets and conceptual meaning;
- reduce the risk of shallow or generic commentary around diagrams.

Recommended contents:

- figure filename;
- figure title;
- one-sentence purpose;
- key message the narrator should extract from the figure.

Status in workflow:

- strongly recommended.

#### 7. Fact Check And Boundary Notes

Purpose:

- define what is implemented in the repository versus what is only planned;
- prevent the generated video from presenting roadmap items as completed implementations;
- capture high-risk distinctions that the narration must preserve.

Recommended contents:

- implemented families;
- planned families;
- exploratory families;
- explicit warnings about wording that would overstate repository status.

Status in workflow:

- required for roadmap-heavy guides such as the TE model curriculum.

### Recommended File Formats For The Package

The repository should prefer formats that are both:

- easy to version in Git;
- compatible with `NotebookLM`.

Recommended practical output set:

- `Markdown` for repository editing and traceability;
- `PDF` for polished long-form source delivery;
- optional `Google Docs` or `Google Slides` exports later, only if the user wants tighter direct integration with the Google ecosystem.

At the repository level, the first-class authored artifacts should remain:

- `Markdown`;
- `PDF`.

This keeps the workflow reproducible inside the repository while still staying compatible with `NotebookLM`.

### Proposed Workflow Rule

The new persistent workflow rule should be:

1. create or update the learning guide in Markdown;
2. generate the guide-local images;
3. wait for explicit user approval of the images;
4. export and validate the learning-guide PDF;
5. after the PDF is complete, prepare the `NotebookLM` video-guide source package;
6. wait for explicit user approval before actually generating or finalizing the video guide.

This preserves two distinct approval gates:

- image approval before PDF export;
- source-package and video-generation approval before `NotebookLM` video creation.

### Recommended Repository Output Layout For Future Video-Guide Packages

After approval, each learning guide should gain a discoverable sibling folder for video-guide preparation, for example:

- `doc/reports/analysis/learning_guides/<Guide Name>/video_guide_package/`

Inside that folder, the repository should write:

- `video_guide_source_brief.md`
- `video_guide_terminology_sheet.md`
- `video_guide_narration_outline.md`
- `video_guide_figure_reference.md`
- `video_guide_fact_boundary_notes.md`

If the user later wants export-ready source bundles, that folder can also contain:

- PDF companions for the package documents;
- a final upload checklist;
- a `NotebookLM` generation prompt note or usage instructions.

### Recommended Scope For The First Application Wave

Once this rule is approved and implemented, the first practical wave should target the already created learning guides:

- `Neural Network Foundations`
- `Training, Validation, And Testing`
- `TE Model Curriculum`

Those three guides are a natural pilot set because:

- they already exist;
- they already have approved figures;
- they form a coherent educational sequence;
- they are precisely the kind of source material that benefits from a video-overview workflow.

## Involved Components

- `README.md`
  Main project document that must reference this technical planning note.
- `doc/README.md`
  Internal documentation index that should also reference this technical planning note.
- `AGENTS.md`
  Repository workflow rules that should receive the new video-guide package rule after approval.
- `doc/reports/analysis/learning_guides/`
  Current and future learning guides that will become the primary source family for `NotebookLM` video-guide generation.
- `doc/technical/2026-03/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md`
  Earlier approved learning-guide PDF rule that this new video-guide workflow must extend rather than replace.
- Future target after approval:
  - `doc/reports/analysis/learning_guides/<Guide Name>/video_guide_package/`

## Implementation Steps

1. Create this technical planning document and register it in `README.md` and `doc/README.md`.
2. Wait for explicit user approval before changing permanent repository rules or generating any `NotebookLM` video-guide source packages.
3. After approval, add the new repository rule that learning-guide video-guide preparation starts only after the learning-guide PDF is complete.
4. Add the second approval rule that actual video-guide generation with `NotebookLM` requires explicit user approval even after the source package is ready.
5. Implement the repository-owned source package template for learning-guide video preparation.
6. Apply that template first to the existing three learning guides.
7. Update the documentation indexes so the video-guide preparation artifacts are discoverable when they are later created.
