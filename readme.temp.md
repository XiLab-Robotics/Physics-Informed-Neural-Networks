# Temporary Handoff For Post-Campaign Integration

## Purpose

This file is a standalone handoff for the other Codex instance that will resume work on this repository after the active training campaign has finished on the other PC and the shared commits have been synchronized.

It describes:

- what was analyzed on this machine;
- what was intentionally changed;
- what was intentionally not changed;
- how the downloaded `NotebookLM` exports should be renamed and archived;
- which repository documents should be updated later on the other machine;
- which conflict-avoidance constraints were enforced here.

This file is intentionally standalone and should be treated as the authoritative transfer note for the delayed integration phase.

## Current Local Delta

At the time this handoff was written, the intended local delta on this machine is:

- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
- `doc/technical/2026-03-22/2026-03-22-09-50-07_additional_notebooklm_guide_archives.md`
- `doc/technical/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`
- `doc/technical/2026-03-22/2026-03-22-10-20-00_code_documentation_comparison_report_and_pdf.md`
- `doc/technical/2026-03-22/2026-03-22-10-50-00_code_documentation_report_table_header_fix.md`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.md`
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.pdf`
- `readme.temp.md`

No shared index file should remain modified here.

In particular, the following files were deliberately restored to avoid future merge conflicts with the other PC:

- `README.md`
- `doc/README.md`

## Context

The user reported that:

- an active training campaign is running on another PC on the same repository;
- there are files on that other machine that are not yet committed to Git;
- work on this machine must remain standalone until the campaign is finished and the other PC has pushed or finalized its changes;
- direct edits to shared files should be avoided to reduce conflict risk.

Because of that, the strategy on this machine was:

- do not touch protected campaign files;
- do not integrate imported materials into canonical guide folders yet;
- do not update shared documentation indexes yet;
- only create standalone artifacts that can be replayed later on the synchronized repository state.

## What Was Analyzed

Three `NotebookLM` export bundles were found under `.temp/`:

- `.temp/Neural Network Foundations/`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/`

Three additional `NotebookLM` export bundles were later added under `.temp/`:

- `.temp/FeedForward Network/`
- `.temp/Harmonic Regression/`
- `.temp/Training, Validation, and Testing Workflow for TE Models/`

### Bundle 1: Neural Network Foundations

Observed files:

- `Dalla Regressione Lineare ai Neuroni Artificiali_ Un Viaggio nella Predizione dell'Errore di Trasmissione.pdf`
- `Mind Map.png`
- `Neural_Network_Foundations.pdf`
- `Neural_Network_Foundations.pptx`
- `Reti_Neurali_e_Previsione_TE.mp4`
- `unnamed.png`

### Bundle 2: TE Model Curriculum

Observed files:

- `Il_Curriculum_dei_Modelli_TE.mp4`
- `Mind Map.png`
- `Panoramica delle Architetture Neurali_ Guida al Curriculum TE.pdf`
- `Transmission_Error_Model_Evolution.pdf`
- `Transmission_Error_Model_Evolution.pptx`
- `unnamed.png`

### Bundle 3: Multilayer Perceptrons

Observed files:

- `Evoluzione dell'Analisi Armonica.png`
- `Harmonic_Neural_Synthesis.pdf`
- `Harmonic_Neural_Synthesis.pptx`
- `Mind Map.png`
- `Modellare_Pattern_Periodici.mp4`
- `Oltre la Linea_ Come le Reti Neurali Risolvono l'Enigma dello XOR.pdf`

## Existing Canonical Repository Context

Two of the imported bundles correspond to existing canonical repository-authored learning guides:

- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`

The `Multilayer Perceptrons` bundle does not yet have an exact canonical peer folder, but it is closely related to the Wave 1 architecture-learning material and the existing family guides such as:

- `doc/reports/analysis/learning_guides/FeedForward Network/`
- `doc/reports/analysis/learning_guides/Harmonic Regression/`
- `doc/reports/analysis/learning_guides/Periodic Feature Network/`
- `doc/reports/analysis/learning_guides/Residual Harmonic Network/`

## Updated Structural Decision For Learning Guides

After reviewing the current repository layout, the user decided that the learning guides no longer belong semantically under:

- `doc/reports/analysis/learning_guides/`

The preferred canonical destination for the whole learning-guide family is now:

- `doc/guide/`

This is a better fit because the learning guides are persistent educational material rather than point-in-time analytical reports.

### Recommended Canonical Learning-Guide Layout

The future synchronized repository should likely move or recreate the guide family under:

- `doc/guide/Neural Network Foundations/`
- `doc/guide/Training, Validation, And Testing/`
- `doc/guide/TE Model Curriculum/`
- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`

The existing `doc/guide/project_usage_guide.md` should remain where it is.

### Recommended Internal Structure Per Learning Guide

Each canonical guide folder under `doc/guide/<Guide Name>/` should preserve the current internal structure where applicable:

- main Markdown guide
- PDF companion
- `assets/`
- `video_guide_package/`

This keeps the current guide-local organization intact while moving the family to a semantically better root.

### Proposed Canonical Migration Map

Current -> Future

- `doc/reports/analysis/learning_guides/Neural Network Foundations/`
  -> `doc/guide/Neural Network Foundations/`
- `doc/reports/analysis/learning_guides/Training, Validation, And Testing/`
  -> `doc/guide/Training, Validation, And Testing/`
- `doc/reports/analysis/learning_guides/TE Model Curriculum/`
  -> `doc/guide/TE Model Curriculum/`
- `doc/reports/analysis/learning_guides/FeedForward Network/`
  -> `doc/guide/FeedForward Network/`
- `doc/reports/analysis/learning_guides/Harmonic Regression/`
  -> `doc/guide/Harmonic Regression/`
- `doc/reports/analysis/learning_guides/Periodic Feature Network/`
  -> `doc/guide/Periodic Feature Network/`
- `doc/reports/analysis/learning_guides/Residual Harmonic Network/`
  -> `doc/guide/Residual Harmonic Network/`

### Proposed Imported Media Placement Inside Guide Folders

The current standalone archive under:

- `doc/imports/notebooklm_exports/`

should remain the provenance-preserving source archive during isolated work.

After synchronization and conflict re-validation, all imported bundles should be placed directly inside the corresponding canonical guide folders as requested by the user.

Recommended canonical pattern:

- `doc/guide/<Guide Name>/`

Recommended first mapping:

- `doc/imports/notebooklm_exports/neural_network_foundations/`
  -> canonical destination:
  `doc/guide/Neural Network Foundations/`
- `doc/imports/notebooklm_exports/te_model_curriculum/`
  -> canonical destination:
  `doc/guide/TE Model Curriculum/`
- `doc/imports/notebooklm_exports/multilayer_perceptrons/`
  -> canonical destination:
  `doc/guide/Multilayer Perceptrons/`

Because the user wants all imported files to live directly under the guide subtree, the synchronized integration pass should migrate them there after conflict checks rather than leaving them only under `doc/imports/notebooklm_exports/`.

### Expected Imported File Set Per Guide

For each imported `NotebookLM` guide bundle, the synchronized integration should expect this file family:

- one mind map image in `.png`
- one infographic image in `.png`
- one presentation in `.pptx`
- one presentation export in `.pdf`
- one supporting brief in `.pdf`
- one video overview in `.mp4`

Recommended guide-local imported-media layout:

- place the imported files directly in `doc/guide/<Guide Name>/`
- keep the naming readable and aligned with the current guide style

### Filename Normalization Rule For Imported Media

During the future synchronized integration, imported filenames should be normalized to readable guide-local names with no `notebooklm` marker in the filename.

Use human-readable names such as:

- `Mind Map.png`
- `Infographic.png`
- `<Guide Name>.pptx`
- `<Guide Name>.pdf`
- `Supporting Brief.pdf`
- `Video Overview.mp4`

This means that files currently archived as:

- `*_notebooklm_supporting_figure.png`

should be renamed during canonical integration to:

- `Infographic.png`

Recommended final filenames:

#### Neural Network Foundations

- `Mind Map.png`
- `Infographic.png`
- `Neural Network Foundations.pptx`
- `Neural Network Foundations.pdf`
- `Supporting Brief.pdf`
- `Video Overview.mp4`

#### TE Model Curriculum

- `Mind Map.png`
- `Infographic.png`
- `TE Model Curriculum.pptx`
- `TE Model Curriculum.pdf`
- `Supporting Brief.pdf`
- `Video Overview.mp4`

#### Multilayer Perceptrons

- `Mind Map.png`
- `Infographic.png`
- `Multilayer Perceptrons.pptx`
- `Multilayer Perceptrons.pdf`
- `Supporting Brief.pdf`
- `Video Overview.mp4`

### Recommendation For `Multilayer Perceptrons`

Recommended decision:

- treat `Multilayer Perceptrons` as a new canonical learning guide under:
  `doc/guide/Multilayer Perceptrons/`

Reason:

- the imported material is conceptually broader than one single Wave 1 implementation file;
- it sits naturally between `Neural Network Foundations` and the model-family-specific architecture guides;
- it provides a reusable conceptual bridge from basic neurons and feedforward logic to the implemented Wave 1 architectures;
- forcing it to be absorbed directly into the existing family guides would dilute its educational role and make the imported media harder to place cleanly.

Therefore, the synchronized integration pass should prefer:

- a dedicated canonical learning-guide folder for `Multilayer Perceptrons`;
- place the imported media directly inside:
  `doc/guide/Multilayer Perceptrons/`

If the synchronized repository state already contains a broader architecture-series layout by then, re-check this recommendation before finalizing the placement.

### Why `external_media/notebooklm/` Is Better Than Mixing Into `assets/`

`assets/` should ideally remain reserved for repository-authored figures, diagrams, and local guide visuals.

The imported `NotebookLM` materials are different in nature because they include:

- generated slide decks;
- generated videos;
- generated mind maps;
- imported support PDFs.

Keeping them under:

- `external_media/notebooklm/`

preserves:

- provenance clarity;
- easier later cleanup or replacement;
- less ambiguity about what is canonical versus imported.

### Current Migration-Sensitive References Already Identified

The future integration pass must review at least these reference families because they still point to the old learning-guide root:

- `README.md`
- `doc/README.md`
- `doc/technical/2026-03-20/2026-03-20-12-00-29_neural_network_foundations_and_te_model_learning_guide.md`
- `doc/technical/2026-03-20/2026-03-20-12-51-34_learning_guide_pdf_exports_and_post_image_approval_rule.md`
- `doc/technical/2026-03-20/2026-03-20-12-58-52_notebooklm_video_guide_source_package_and_workflow_rule.md`
- `doc/technical/2026-03-20/2026-03-20-13-21-58_architecture_learning_guides_from_feedforward_network.md`
- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`

These files do not necessarily need blind search-and-replace.

They must be reviewed in context during integration because some of them describe historical decisions made before the structural change and may need wording updates rather than only path updates.

## Main Decision

The imported `NotebookLM` outputs should not be dropped directly into the canonical learning-guide folders.

Reason:

- they are external generated artifacts, not repository-authored canonical guide sources;
- they include presentation decks, video exports, mind maps, and raw generated images;
- mixing them into the current guide folders would blur the distinction between canonical documentation and imported support media;
- the active campaign on the other PC makes it preferable to isolate all new material into standalone folders first.

At the same time, the future canonical home for learning-guide-related material is no longer the old `reports/analysis` subtree.

The long-term target should be the dedicated guide subtree under:

- `doc/guide/`

## Planned Standalone Destination

Create this archive root:

- `doc/imports/notebooklm_exports/`

Then create one normalized topic folder per bundle:

- `doc/imports/notebooklm_exports/neural_network_foundations/`
- `doc/imports/notebooklm_exports/te_model_curriculum/`
- `doc/imports/notebooklm_exports/multilayer_perceptrons/`

Inside each topic folder, create these subfolders:

- `pdf/`
- `slides/`
- `video/`
- `images/`

This keeps the imported materials:

- isolated from the canonical guides;
- easy to inspect later;
- ready for selective post-campaign integration.

## Proposed Rename Map

### Neural Network Foundations

Original -> Target

- `Neural_Network_Foundations.pdf`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/pdf/neural_network_foundations_notebooklm_slides.pdf`
- `Neural_Network_Foundations.pptx`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/slides/neural_network_foundations_notebooklm_slides.pptx`
- `Reti_Neurali_e_Previsione_TE.mp4`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/video/neural_network_foundations_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/images/neural_network_foundations_notebooklm_mind_map.png`
- `unnamed.png`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/images/neural_network_foundations_notebooklm_supporting_figure.png`
- `Dalla Regressione Lineare ai Neuroni Artificiali_ Un Viaggio nella Predizione dell'Errore di Trasmissione.pdf`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/pdf/neural_network_foundations_notebooklm_supporting_brief.pdf`

### TE Model Curriculum

Original -> Target

- `Transmission_Error_Model_Evolution.pdf`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/pdf/te_model_curriculum_notebooklm_slides.pdf`
- `Transmission_Error_Model_Evolution.pptx`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/slides/te_model_curriculum_notebooklm_slides.pptx`
- `Il_Curriculum_dei_Modelli_TE.mp4`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/video/te_model_curriculum_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/images/te_model_curriculum_notebooklm_mind_map.png`
- `unnamed.png`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/images/te_model_curriculum_notebooklm_supporting_figure.png`
- `Panoramica delle Architetture Neurali_ Guida al Curriculum TE.pdf`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/pdf/te_model_curriculum_notebooklm_supporting_brief.pdf`

### Multilayer Perceptrons

Original -> Target

- `Harmonic_Neural_Synthesis.pdf`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/pdf/multilayer_perceptrons_notebooklm_slides.pdf`
- `Harmonic_Neural_Synthesis.pptx`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/slides/multilayer_perceptrons_notebooklm_slides.pptx`
- `Modellare_Pattern_Periodici.mp4`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/video/multilayer_perceptrons_notebooklm_video_overview.mp4`
- `Mind Map.png`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/images/multilayer_perceptrons_notebooklm_mind_map.png`
- `Evoluzione dell'Analisi Armonica.png`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/images/multilayer_perceptrons_notebooklm_supporting_figure.png`
- `Oltre la Linea_ Come le Reti Neurali Risolvono l'Enigma dello XOR.pdf`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/pdf/multilayer_perceptrons_notebooklm_supporting_brief.pdf`

## Technical Document Created Here

The following technical document was created on this machine:

- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
- `doc/technical/2026-03-22/2026-03-22-09-50-07_additional_notebooklm_guide_archives.md`
- `doc/technical/2026-03-22/2026-03-22-10-05-00_code_documentation_platform_evaluation.md`
- `doc/technical/2026-03-22/2026-03-22-10-20-00_code_documentation_comparison_report_and_pdf.md`
- `doc/technical/2026-03-22/2026-03-22-10-50-00_code_documentation_report_table_header_fix.md`
- `scripts/reports/generate_styled_report_pdf.py`
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.md`
- `doc/reports/analysis/2026-03-22-10-28-00_code_documentation_platform_comparison_report.pdf`

Its purpose is to preserve the reasoning behind:

- why the imported files should remain standalone for now;
- how they should be renamed;
- where they should be moved;
- how they should later be integrated.

## Important Correction About Shared Indexes

During the first pass, there was an attempt to register the new technical document in:

- `README.md`
- `doc/README.md`

That was identified as a conflict risk because those files are likely to be updated on the other PC when the campaign work is committed.

Those two index edits were then explicitly removed.

Therefore, the other Codex instance should handle the README registration later, on top of the synchronized repository state.

## Proposed Repository Rule: Isolated Mode

The user requested a new persistent repository rule for an explicit `isolated mode`.

This rule was not written into shared repository files on this machine because the current work must remain conflict-safe during the active campaign.

Instead, the rule is defined here so the other Codex instance can later integrate it into the repository instructions and related documentation after synchronization.

### Activation

`Isolated mode` is activated when the user explicitly says one of the following, or an equivalent instruction with the same intent:

- "enter isolated mode"
- "work in isolated mode"
- "modalita isolata"
- "lavora in modo isolato"
- "do this in isolation"

The mode remains active until the user explicitly says that:

- isolated mode is over;
- the work should now be integrated into the repository;
- the work may now be applied to canonical repository files.

### Core Intent

When isolated mode is active, Codex must work as if it were preparing a delayed patch set for later replay on a synchronized repository state.

The goal is:

- avoid merge conflicts with concurrent work on another machine;
- avoid touching shared or conflict-prone repository files;
- still allow deep analysis, drafting, planning, asset organization, and standalone artifact preparation;
- preserve a complete implementation trail for later integration.

### Mandatory Operational Rules

When isolated mode is active, Codex must:

1. Avoid modifying shared repository files unless the user explicitly overrides the rule.
2. Prefer creating only new standalone files rather than editing existing ones.
3. Write new artifacts into isolated or temporary paths first.
4. Maintain a dedicated temporary handoff file that records all work in detail.
5. Clearly separate:
   - what was analyzed;
   - what was actually changed;
   - what was intentionally deferred;
   - what must later be integrated into the canonical repository.
6. Treat all implementation work as provisional until the user explicitly requests integration.
7. Preserve exact rename maps, move maps, target paths, and deferred repository edits so another Codex instance can replay the work reliably later.

### File Placement Rules

When isolated mode is active, Codex should prefer these patterns:

- temporary handoff file at repository root:
  - `readme.temp.md`
- standalone technical notes:
  - `doc/technical/<date>/...`
- isolated imported assets:
  - temporary staging or future archive paths that do not overwrite canonical guide folders
- temporary planning notes, inventories, migration maps, or patch instructions:
  - new standalone files only

Codex should avoid modifying, unless explicitly authorized:

- `README.md`
- `doc/README.md`
- campaign-tracked files
- current canonical guide indexes
- files likely to be changed concurrently on the other machine

### Required Handoff Content

While isolated mode is active, `readme.temp.md` must be kept updated and must contain enough detail for a later Codex instance to continue the work without losing context.

At minimum, the handoff file should contain:

1. purpose of the isolated work;
2. current local delta;
3. conflict-avoidance constraints;
4. analysis performed;
5. files discovered or inspected;
6. decisions taken and reasoning;
7. exact rename and move maps when relevant;
8. exact repository files intentionally not modified;
9. deferred implementation steps;
10. explicit instructions for later integration into the synchronized repository state.

### What Codex Needs From The User To Respect Isolated Mode

To follow isolated mode correctly, Codex needs these points to be either explicitly stated or reasonably inferable:

1. Confirmation that the work should remain isolated and not yet be merged into canonical repository files.
2. Any known shared files that are especially conflict-prone and should not be touched.
3. The preferred temporary or isolated destination root if the user wants one different from the default.
4. The condition that ends isolated mode, for example:
   - campaign finished;
   - other PC committed;
   - repository synchronized.
5. Whether Codex should only analyze and document, or also create standalone new files and assets in temporary paths.

If the user does not provide all details, Codex should default to the safest version:

- no shared-file edits;
- new standalone files only;
- full logging in `readme.temp.md`.

### Transition Out Of Isolated Mode

When the user later says to implement or integrate the isolated work, Codex must:

1. Re-open `readme.temp.md` and all standalone files created during isolated mode.
2. Re-validate the current repository state after synchronization.
3. Check whether any assumptions made during isolated mode are still valid.
4. Translate the isolated artifacts into canonical repository changes.
5. Update shared indexes, guides, and related documentation only at that later stage.
6. Remove ambiguity by producing a clear mapping from isolated artifacts to final repository modifications.

Integration should not assume that the repository state is unchanged from the time the isolated work was prepared.

### Mandatory Integration Workflow After Isolated Mode

When the user explicitly requests implementation of work prepared in isolated mode, Codex must not apply the isolated changes directly without a fresh repository-aware preparation step.

Instead, Codex must:

1. Create a new technical project document for the integration task, following the normal repository workflow.
2. Create an explicit integration checklist before applying repository changes.
3. Re-check each isolated artifact, planned rename, planned move, and planned repository edit against the current synchronized repository state.
4. Verify whether the target repository files changed while the work was isolated.
5. Re-evaluate each intended modification for conflict risk, overlap risk, and obsolete-assumption risk.
6. Adjust the integration plan if the repository evolved in the meantime.
7. Only then implement the canonical repository changes.

### Required Conflict Re-Validation During Integration

The other Codex instance must verify each planned implementation or modification individually.

That verification should include:

1. whether the target file already changed on the synchronized branch;
2. whether the isolated plan still matches the latest file structure and naming;
3. whether the target content now exists already in another form;
4. whether the isolated rename or move would overwrite, duplicate, or contradict newer repository content;
5. whether the target documentation indexes, guides, or reports now require a different update path;
6. whether any protected or recently changed files require user confirmation before editing.

If a conflict risk or ambiguity is found, Codex must surface it explicitly before proceeding with that part of the integration.

### Required Integration Checklist Content

The integration checklist should cover at minimum:

1. isolated artifacts to import;
2. standalone files to preserve;
3. canonical files to update;
4. index files to register;
5. rename and move operations to perform;
6. conflict checks completed for each target file;
7. documentation updates still required;
8. final verification that no isolated-only placeholder remains in the canonical repository by mistake.

### Recommended Repository-Level Rule Text For Later Integration

The other Codex instance can adapt the following wording into `AGENTS.md` or the repository workflow documentation:

`When the user explicitly requests isolated mode, work must proceed in a conflict-safe standalone manner. During isolated mode, avoid modifying shared repository files, prefer creating only new standalone files in temporary or isolated paths, and maintain a detailed handoff log in readme.temp.md describing all analysis, created artifacts, deferred edits, rename/move plans, and later integration steps. Do not apply isolated work to canonical repository files until the user explicitly requests integration. When the user later requests implementation of the isolated work, re-read the handoff artifacts, validate the synchronized repository state, and then translate the isolated outputs into the proper repository changes.`

## What The Other Codex Instance Should Do Later

After the campaign has finished on the other PC and the repository state is synchronized:

1. Verify that the active campaign is actually finished and that the shared repository state is stable.
2. Re-open this handoff file and the technical note:
   - `readme.temp.md`
   - `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
3. Re-check the contents of `.temp/` in case the user added or removed exports after this handoff was written.
4. Create the archive root:
   - `doc/imports/notebooklm_exports/`
5. Create the three topic folders and their `pdf/`, `slides/`, `video/`, and `images/` subfolders.
6. Rename and move the files according to the mapping in this document.
7. Produce a final inventory mapping original path -> archived path.
8. Prepare a migration plan for moving the canonical learning guides from:
   - `doc/reports/analysis/learning_guides/`
   to:
   - `doc/guide/learning/`
9. Re-check every guide-local asset path, PDF reference, `video_guide_package` reference, and internal document link that depends on the old location.
10. Decide how the archived imported assets should be attached to the new canonical guide folders while preserving provenance in the migration notes, but without keeping `notebooklm` in final filenames.
11. Update the documentation indexes on the synchronized branch:
    - `README.md`
    - `doc/README.md`
12. Update any guide-specific references that still point to the old `doc/reports/analysis/learning_guides/` paths.
13. Decide, with the user, whether any of the archived imported assets should also be selectively referenced from:
   - `doc/guide/Neural Network Foundations/`
   - `doc/guide/TE Model Curriculum/`
   - a new `doc/guide/Multilayer Perceptrons/` folder or a related Wave 1 guide location
14. Keep the archive provenance explicit so imported `NotebookLM` outputs remain distinguishable from canonical repository-authored guides.

## Recommended README Updates For Later

Once the other PC is synchronized and it is safe to touch shared indexes, add the new technical document to:

- `README.md`
- `doc/README.md`

Recommended path to register:

- `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`

The short description can state that the document defines the analysis, naming policy, and standalone archive workflow for imported `NotebookLM` export bundles.

## Constraints To Preserve

The other Codex instance should preserve these constraints unless the user explicitly changes them:

- do not silently mix imported `NotebookLM` outputs into canonical guide folders;
- keep imported materials under a provenance-preserving archive root first;
- avoid overwriting existing guide assets;
- avoid shared-file edits until the user confirms the campaign branch is safe to integrate;
- treat `doc/guide/` as the preferred future canonical home for the learning-guide family;
- use readable file names inside each guide folder and remove `notebooklm` from final filenames;
- treat this handoff as a replay plan, not as proof that the moves were already executed.

## Integration Checklist: Learning Guide Migration

This checklist is the required replay checklist for the other Codex instance once the repository is synchronized and isolated work may be integrated.

### Phase 1: Re-Validation

1. Confirm that the active campaign is finished and that integration work is now allowed.
2. Re-open:
   - `readme.temp.md`
   - `doc/technical/2026-03-20/2026-03-20-17-01-59_notebooklm_export_ingestion_and_archive.md`
3. Create a new technical project document for the integration task before modifying canonical repository files.
4. Verify whether `doc/reports/analysis/learning_guides/` still exists unchanged or whether the other PC already reorganized part of the guide tree.
5. Verify whether `doc/guide/learning/` already exists or whether it must be created.
6. Re-scan all references to `doc/reports/analysis/learning_guides/` before changing paths.

### Phase 2: Canonical Learning-Guide Migration

1. Move the current canonical guide folders from:
   - `doc/reports/analysis/learning_guides/`
   to:
   - `doc/guide/`
2. Preserve the per-guide structure:
   - main Markdown
   - main PDF
   - `assets/`
   - `video_guide_package/`
3. Confirm that no guide-local file is lost during the move.
4. Re-check internal links inside guide Markdown files after the move.

### Phase 3: Imported NotebookLM Media Placement

1. For each relevant guide, create:
   - the canonical guide folder under `doc/guide/<Guide Name>/`
2. Place all imported files directly under the corresponding guide folder.
3. Preserve provenance in the migration documentation, not in the final filenames.
4. Re-check that each guide has the expected full imported set:
   - mind map `.png`
   - infographic `.png`
   - slides `.pptx`
   - slides export `.pdf`
   - supporting brief `.pdf`
   - video overview `.mp4`

### Phase 4: Guide-by-Guide Imported Media Mapping

1. `Neural Network Foundations`
   - import from:
     `doc/imports/notebooklm_exports/neural_network_foundations/`
   - place under:
     `doc/guide/Neural Network Foundations/`
2. `TE Model Curriculum`
   - import from:
     `doc/imports/notebooklm_exports/te_model_curriculum/`
   - place under:
     `doc/guide/TE Model Curriculum/`
3. `Multilayer Perceptrons`
   - create canonical guide family folder:
     `doc/guide/Multilayer Perceptrons/`
   - place imported media under:
     `doc/guide/Multilayer Perceptrons/`
   - rename any archived `*_notebooklm_supporting_figure.png` file to `Infographic.png`
   - if a different synchronized canonical location exists by then, re-evaluate before moving files

### Phase 5: Conflict Checks

1. Check whether each target guide folder already contains imported files with overlapping names.
2. Check whether any guide already gained an `external_media/` subtree while isolated work was in progress.
3. Check whether any new guide was added on the other PC that changes where `Multilayer Perceptrons` should live.
4. Check whether README indexes or guide indexes were already updated by the other PC.
5. Check whether any of the recent technical documents were revised and therefore need contextual edits instead of path-only edits.
6. Check whether any imported filenames must be normalized from `supporting_figure` to `Infographic` during the final move into `doc/guide/`.

### Phase 6: Documentation Updates

1. Update `README.md` references from the old learning-guide root to `doc/guide/`.
2. Update `doc/README.md` references from the old learning-guide root to `doc/guide/`.
3. Review the recent technical documents that still mention the old learning-guide root and update them contextually where appropriate.
4. Update any guide-specific references that should mention the presence of imported NotebookLM external media.

### Phase 7: Final Verification

1. Confirm that the canonical learning-guide family now lives under `doc/guide/`.
2. Confirm that `doc/guide/project_usage_guide.md` still exists correctly as the operational usage guide.
3. Confirm that each imported `NotebookLM` bundle is now represented under the correct learning-guide folder.
4. Confirm that the imported files use readable guide-local names such as `Mind Map`, `Infographic`, `Supporting Brief`, and `Video Overview`.
5. Confirm that no stale reference to `doc/reports/analysis/learning_guides/` remains unless it is intentionally historical.
6. Confirm that no isolated-only placeholder or temporary note was accidentally treated as canonical content.

## Summary

What was actually done on this machine:

- inspected `.temp/` and the existing learning-guide structure;
- determined that the imports should remain standalone for now;
- created one technical planning note with the full archive strategy;
- created the standalone archive root `doc/imports/notebooklm_exports/`;
- renamed and moved the `NotebookLM` exported files into the standalone archive structure;
- extended the standalone archive with three additional guide bundles:
  - `feedforward_network`
  - `harmonic_regression`
  - `training_validation_and_testing`
- avoided permanent edits to shared README index files after conflict risk was recognized;
- created this handoff file so the other Codex instance can complete the work later without losing context.

What was not done on this machine:

- no canonical guide folder was modified;
- no shared README index update was left in place;
- no Git commit was created.

## Final Standalone Archive State

The imported files were moved into:

- `doc/imports/notebooklm_exports/neural_network_foundations/`
- `doc/imports/notebooklm_exports/te_model_curriculum/`
- `doc/imports/notebooklm_exports/multilayer_perceptrons/`
- `doc/imports/notebooklm_exports/feedforward_network/`
- `doc/imports/notebooklm_exports/harmonic_regression/`
- `doc/imports/notebooklm_exports/training_validation_and_testing/`

Each bundle now uses the subfolders:

- `pdf/`
- `slides/`
- `video/`
- `images/`

### Final Archive Inventory

#### Neural Network Foundations

- `.temp/Neural Network Foundations/Neural_Network_Foundations.pdf`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/pdf/neural_network_foundations_notebooklm_slides.pdf`
- `.temp/Neural Network Foundations/Neural_Network_Foundations.pptx`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/slides/neural_network_foundations_notebooklm_slides.pptx`
- `.temp/Neural Network Foundations/Reti_Neurali_e_Previsione_TE.mp4`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/video/neural_network_foundations_notebooklm_video_overview.mp4`
- `.temp/Neural Network Foundations/Mind Map.png`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/images/neural_network_foundations_notebooklm_mind_map.png`
- `.temp/Neural Network Foundations/unnamed.png`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/images/neural_network_foundations_notebooklm_supporting_figure.png`
- `.temp/Neural Network Foundations/Dalla Regressione Lineare ai Neuroni Artificiali_ Un Viaggio nella Predizione dell'Errore di Trasmissione.pdf`
  -> `doc/imports/notebooklm_exports/neural_network_foundations/pdf/neural_network_foundations_notebooklm_supporting_brief.pdf`

#### TE Model Curriculum

- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/Transmission_Error_Model_Evolution.pdf`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/pdf/te_model_curriculum_notebooklm_slides.pdf`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/Transmission_Error_Model_Evolution.pptx`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/slides/te_model_curriculum_notebooklm_slides.pptx`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/Il_Curriculum_dei_Modelli_TE.mp4`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/video/te_model_curriculum_notebooklm_video_overview.mp4`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/Mind Map.png`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/images/te_model_curriculum_notebooklm_mind_map.png`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/unnamed.png`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/images/te_model_curriculum_notebooklm_supporting_figure.png`
- `.temp/TE Model Curriculum - From Baselines to Physics-Informed Neural Networks/Panoramica delle Architetture Neurali_ Guida al Curriculum TE.pdf`
  -> `doc/imports/notebooklm_exports/te_model_curriculum/pdf/te_model_curriculum_notebooklm_supporting_brief.pdf`

#### Multilayer Perceptrons

- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Harmonic_Neural_Synthesis.pdf`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/pdf/multilayer_perceptrons_notebooklm_slides.pdf`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Harmonic_Neural_Synthesis.pptx`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/slides/multilayer_perceptrons_notebooklm_slides.pptx`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Modellare_Pattern_Periodici.mp4`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/video/multilayer_perceptrons_notebooklm_video_overview.mp4`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Mind Map.png`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/images/multilayer_perceptrons_notebooklm_mind_map.png`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Evoluzione dell'Analisi Armonica.png`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/images/multilayer_perceptrons_notebooklm_supporting_figure.png`
- `.temp/Multilayer Perceptrons - Foundations of Neural Network Architecture/Oltre la Linea_ Come le Reti Neurali Risolvono l'Enigma dello XOR.pdf`
  -> `doc/imports/notebooklm_exports/multilayer_perceptrons/pdf/multilayer_perceptrons_notebooklm_supporting_brief.pdf`

#### FeedForward Network

- `.temp/FeedForward Network/FeedForward_Network_Baseline.pdf`
  -> `doc/imports/notebooklm_exports/feedforward_network/pdf/feedforward_network_notebooklm_slides.pdf`
- `.temp/FeedForward Network/FeedForward_Network_Baseline.pptx`
  -> `doc/imports/notebooklm_exports/feedforward_network/slides/feedforward_network_notebooklm_slides.pptx`
- `.temp/FeedForward Network/Guida ai Concetti Fondamentali_ Il Neurone Artificiale nella Meccanica Industriale.pdf`
  -> `doc/imports/notebooklm_exports/feedforward_network/pdf/feedforward_network_notebooklm_supporting_brief.pdf`
- `.temp/FeedForward Network/La_Rete_FeedForward.mp4`
  -> `doc/imports/notebooklm_exports/feedforward_network/video/feedforward_network_notebooklm_video_overview.mp4`
- `.temp/FeedForward Network/NotebookLM Mind Map.png`
  -> `doc/imports/notebooklm_exports/feedforward_network/images/feedforward_network_notebooklm_mind_map.png`
- `.temp/FeedForward Network/unnamed.png`
  -> `doc/imports/notebooklm_exports/feedforward_network/images/feedforward_network_notebooklm_supporting_figure.png`

#### Harmonic Regression

- `.temp/Harmonic Regression/Dall'Ingranaggio alla Funzione_ Guida alla Regressione Armonica per l'Errore di Trasmissione.pdf`
  -> `doc/imports/notebooklm_exports/harmonic_regression/pdf/harmonic_regression_notebooklm_supporting_brief.pdf`
- `.temp/Harmonic Regression/Harmonic_Regression_Blueprint.pdf`
  -> `doc/imports/notebooklm_exports/harmonic_regression/pdf/harmonic_regression_notebooklm_slides.pdf`
- `.temp/Harmonic Regression/Harmonic_Regression_Blueprint.pptx`
  -> `doc/imports/notebooklm_exports/harmonic_regression/slides/harmonic_regression_notebooklm_slides.pptx`
- `.temp/Harmonic Regression/NotebookLM Mind Map.png`
  -> `doc/imports/notebooklm_exports/harmonic_regression/images/harmonic_regression_notebooklm_mind_map.png`
- `.temp/Harmonic Regression/Regressione_Armonica.mp4`
  -> `doc/imports/notebooklm_exports/harmonic_regression/video/harmonic_regression_notebooklm_video_overview.mp4`
- `.temp/Harmonic Regression/unnamed.png`
  -> `doc/imports/notebooklm_exports/harmonic_regression/images/harmonic_regression_notebooklm_supporting_figure.png`

#### Training, Validation, And Testing

- `.temp/Training, Validation, and Testing Workflow for TE Models/Addestramento,_Validazione,_Test.mp4`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/video/training_validation_and_testing_notebooklm_video_overview.mp4`
- `.temp/Training, Validation, and Testing Workflow for TE Models/Manuale dei Fondamenti Dati_ L'Arte della Suddivisione dei Dataset.pdf`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/pdf/training_validation_and_testing_notebooklm_supporting_brief.pdf`
- `.temp/Training, Validation, and Testing Workflow for TE Models/NotebookLM Mind Map.png`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/images/training_validation_and_testing_notebooklm_mind_map.png`
- `.temp/Training, Validation, and Testing Workflow for TE Models/TE_Dataset_Discipline.pdf`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/pdf/training_validation_and_testing_notebooklm_slides.pdf`
- `.temp/Training, Validation, and Testing Workflow for TE Models/TE_Dataset_Discipline.pptx`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/slides/training_validation_and_testing_notebooklm_slides.pptx`
- `.temp/Training, Validation, and Testing Workflow for TE Models/unnamed.png`
  -> `doc/imports/notebooklm_exports/training_validation_and_testing/images/training_validation_and_testing_notebooklm_supporting_figure.png`

## Remaining Temporary State

After the move operations, `.temp/` still contains the three original topic directories, but they are now empty.

The other Codex instance can decide later whether to:

- leave them in place temporarily;
- remove the empty directories during the post-campaign cleanup;
- confirm with the user before deleting them.
