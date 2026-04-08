Local Build
===========

Use the main project environment and build the documentation site locally with:

.. code-block:: powershell

   conda activate standard_ml_codex_env
   python -m sphinx -W -b html site site/_build/html

Successful output will be generated under:

- ``site/_build/html``

GitHub Pages publication is handled through the repository-owned GitHub Actions
workflow:

- ``.github/workflows/publish-sphinx-pages.yml``
- ``site/requirements-docs.txt``

If the Pages build succeeds but deploy fails, inspect the GitHub-side
``github-pages`` environment separately. A rejected deploy from
``main`` is an environment-permission issue, not a local Sphinx build issue.

The canonical active GitHub branch is now ``main``. Historical branches such as
``base``, ``standard-ml``, and ``codex-agent-pinns`` are retained only as
legacy branches and are not part of the active documentation publication path.

Keep the local warning-as-error build green before closing documentation-relevant
repository work.
