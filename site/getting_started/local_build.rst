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

Keep the local warning-as-error build green before closing documentation-relevant
repository work.
