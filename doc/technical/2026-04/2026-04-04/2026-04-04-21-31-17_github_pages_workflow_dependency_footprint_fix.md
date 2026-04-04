# GitHub Pages Workflow Dependency Footprint Fix

## Overview

This task fixes the GitHub Pages workflow failure currently happening in the
`build` job before Sphinx even starts. The latest run fails with
`OSError: [Errno 28] No space left on device` while `pip install -r requirements.txt`
downloads the full Linux training stack, including large CUDA-enabled PyTorch
packages and OCR/video dependencies that are not required to build the static
documentation portal.

## Technical Approach

The fix will decouple the Sphinx publication workflow from the full training
environment footprint. The Pages build only needs the documentation toolchain
plus the import-time dependencies required by the repository pages that Sphinx
parses.

The implementation will:

1. define a repository-owned documentation-specific dependency set for the
   GitHub Pages workflow;
2. update the Pages workflow so it installs the lighter documentation build
   environment instead of the full `requirements.txt`;
3. preserve local developer workflows and training environments by keeping the
   full runtime dependency set available for real training use;
4. rebuild the Sphinx portal locally with the adjusted documentation path and
   align the public documentation notes if the workflow instructions change.

No subagent is planned for this implementation. The change is small, local to
the repository CI/documentation pipeline, and does not benefit from delegated
work.

## Involved Components

- `.github/workflows/publish-sphinx-pages.yml`
- `requirements.txt`
- possible new documentation-specific dependency file under the repository root
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Introduce a documentation-specific dependency install path for the Pages
   workflow.
2. Update the GitHub Actions workflow to use that lighter dependency set.
3. Verify that the adjusted dependency set still supports a local
   `python -m sphinx -W -b html site site/_build/html` build.
4. Update the affected repository documentation if the documented build path
   changes.
5. Run Markdown checks on the touched Markdown scope before closing the task.
