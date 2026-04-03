GitHub Pages Publication
========================

The canonical publication path for the repository Sphinx portal is GitHub Pages
through the repository-owned GitHub Actions workflow:

- ``.github/workflows/publish-sphinx-pages.yml``

The workflow builds the documentation from the canonical ``site/`` tree and
publishes the generated HTML from:

- ``site/_build/html``

The local validation command remains:

.. code-block:: powershell

   conda activate standard_ml_codex_env
   python -m pip install -r requirements.txt
   python -m sphinx -W -b html site site/_build/html

Repository rule:

- when approved work adds or materially changes a script, feature, runnable
  workflow, or documentation entry point, update the affected Sphinx source
  content under ``site/`` in the same task;
- rebuild the portal locally;
- keep the warning-as-error Sphinx build passing before closing the task.

If the repository Pages settings are not already configured, set the source to
``GitHub Actions`` after the workflow is available on the default branch.
