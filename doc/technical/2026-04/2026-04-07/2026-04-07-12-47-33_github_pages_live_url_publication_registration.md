# GitHub Pages Live URL Publication Registration

## Overview

The repository GitHub Pages deployment is now live at the public URL:

- `https://xilab-robotics.github.io/Physics-Informed-Neural-Networks/`

This task records the transition from workflow-ready Pages support to an
actually live public Sphinx portal, and updates the main repository entry
points so the published documentation URL is visible to new users.

## Technical Approach

The implementation will keep the published URL visible in the concise
GitHub-facing surfaces and in the Sphinx publication notes without turning the
landing pages into an internal registry.

The update will:

1. add the live documentation URL to `README.md`;
2. add the live documentation URL to the Sphinx portal landing surface under
   `site/`;
3. update the user-facing operational guidance in
   `doc/guide/project_usage_guide.md`;
4. refresh the GitHub Pages note so it records the actual public endpoint
   rather than only the workflow mechanics.

## Involved Components

- `README.md`
- `site/index.rst`
- `site/getting_started/github_pages.rst`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Update `README.md` with the live public Sphinx portal URL.
2. Update `site/index.rst` so the portal landing page references its live
   publication URL explicitly.
3. Update `site/getting_started/github_pages.rst` and
   `doc/guide/project_usage_guide.md` to record the live endpoint and keep the
   GitHub-side deploy notes aligned with the now-working public Pages setup.
4. Rebuild the Sphinx portal locally with warning-as-error enabled.
5. Run the touched-Markdown warning checks before closing the task.
