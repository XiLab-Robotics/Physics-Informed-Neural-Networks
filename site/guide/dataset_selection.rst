Dataset Selection
=================

The repository defaults to ``polished_dataset`` and retains
``simplified_dataset`` as a compatibility option.

Polished schema
---------------

Each polished row provides four model inputs:

* ``theta``
* ``theta_dot``
* ``tau_load``
* ``T``

The target is ``theta_TE``. Direction is resolved from the first-level
``forward`` or ``backward`` folder and is not added to the input tensor.

Command-line selection
----------------------

Training, validation, smoke-test, visualization, split-export, and campaign
entry points expose a ``--dataset`` selector:

.. code-block:: powershell

   python -B scripts/training/validate_training_setup.py `
     --config-path config/training/feedforward/presets/trial.yaml `
     --dataset polished_dataset

Use ``--dataset simplified_dataset`` to preserve the legacy five-feature
contract.

Stage 1 campaign
----------------

Validate the prepared polished-dataset smoke campaign without training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_polished_dataset_stage1_smoke_campaign.ps1 -PreflightOnly
