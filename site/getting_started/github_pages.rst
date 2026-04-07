GitHub Pages Publication
========================

The canonical publication path for the repository Sphinx portal is GitHub Pages
through the repository-owned GitHub Actions workflow:

- ``.github/workflows/publish-sphinx-pages.yml``

The workflow builds the documentation from the canonical ``site/`` tree and
publishes the generated HTML from:

- ``site/_build/html``
- ``site/requirements-docs.txt``

The local validation command remains:

.. code-block:: powershell

   conda activate standard_ml_codex_env
   python -m sphinx -W -b html site site/_build/html

The GitHub Pages workflow intentionally does **not** install the full
repository training stack. Instead, it installs a documentation-specific
dependency subset plus a CPU-only PyTorch wheel so the hosted runner does not
exhaust disk space on unnecessary CUDA, OCR, and video-tooling packages.

Repository rule:

- when approved work adds or materially changes a script, feature, runnable
  workflow, or documentation entry point, update the affected Sphinx source
  content under ``site/`` in the same task;
- rebuild the portal locally;
- keep the warning-as-error Sphinx build passing before closing the task.

If the repository Pages settings are not already configured, set the source to
``GitHub Actions`` after the workflow is available on the default branch.

If deployment still fails after a successful build with an error stating that
``standard-ml-codex`` is not allowed to deploy to ``github-pages``, the
remaining blocker is the GitHub environment configuration rather than the
Sphinx build itself. In that case:

- open ``Settings -> Environments -> github-pages``;
- inspect the deployment-branch protection rule;
- allow the ``standard-ml-codex`` branch to deploy, or remove the overly
  restrictive branch filter;
- rerun the Pages workflow after the environment rule is updated.

The workflow also opts into Node.js 24 for JavaScript-based GitHub Actions so
the repository stays aligned with GitHub's current Actions runtime transition.
