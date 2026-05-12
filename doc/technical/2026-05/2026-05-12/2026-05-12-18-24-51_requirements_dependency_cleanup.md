# Requirements Dependency Cleanup

## Overview

Plan the cleanup of the repository Python dependency declarations after a full
local scan of Python scripts and requirement surfaces. The work will separate
active runtime, documentation, LAN-node, and recovered-original workflow needs
so obsolete or misplaced packages can be removed without breaking training,
reporting, campaign, or remote operator workflows.

## Technical Approach

The cleanup will audit all repository-owned Python scripts with static import
inspection, then compare those imports against every active requirement file.
The active requirement surfaces are:

- `requirements.txt`
- `site/requirements-docs.txt`
- `scripts/tooling/lan_ai/requirements-lan-ai-node.txt`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/requirements.txt`

Requirement files under `reference/` will be treated as preserved historical
reference inputs unless a later check proves they are used as an install target
by repository-owned tooling. Dependency removals will be conservative and based
on direct imports, documented runtime plugin needs, or explicit command-line
workflow dependencies.

Context7 will be used before finalizing version-sensitive recommendations for
ML and adjacent tooling dependencies when API or packaging behavior matters.
No subagent use is planned for this task.

## Involved Components

- Root Python runtime and training dependencies in `requirements.txt`.
- Documentation portal dependency surface in `site/requirements-docs.txt`.
- LAN AI node dependency surface in
  `scripts/tooling/lan_ai/requirements-lan-ai-node.txt`.
- Recovered original RCIM workflow dependency surface in
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/requirements.txt`.
- Repository Python scripts under `scripts/` and `site/`.
- Reference summaries under `doc/reference_summaries/`.
- Active campaign state in `doc/running/active_training_campaign.yaml`, checked
  to avoid touching protected campaign files.

## Implementation Steps

1. Build a complete list of Python imports from repository-owned Python files,
   excluding preserved reference snapshots unless they are active install
   targets.
2. Map imports to PyPI requirement names, accounting for package/import-name
   differences such as `sklearn` to `scikit-learn`, `yaml` to `PyYAML`, and
   `fitz` to `pymupdf`.
3. Identify dependencies that are directly required, indirectly required only by
   optional workflows, duplicated across narrower requirement files, or not
   referenced by active code.
4. Check version-sensitive ML/tooling packages with Context7 or official
   documentation where local evidence is not enough.
5. Update the smallest appropriate requirement files after approval, preserving
   separate LAN-node and documentation install surfaces.
6. Run focused validation on touched requirement files and Markdown QA on this
   technical document plus `doc/README.md`.
