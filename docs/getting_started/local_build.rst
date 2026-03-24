Local Build
===========

Use the main project environment and build the documentation site locally with:

.. code-block:: powershell

   conda activate standard_ml_codex_env
   python -m pip install -r requirements.txt
   python -m sphinx -W -b html docs docs/_build/html

Successful output will be generated under:

- ``docs/_build/html``

Batch 0 validation focuses on one clean local HTML build. Live hosting and CI publication are deferred to later batches.
