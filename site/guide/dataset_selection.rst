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

Early-wave polished retraining
------------------------------

Validate the prepared 36-run early-wave polished-dataset campaign without
training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1 -PreflightOnly

Launch the local early-wave batch only after confirming the active campaign
state intentionally records the RCIM run as parallel on another workstation:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_polished_dataset_early_wave_parallel_training_campaign.ps1

Wave 5.2B polished offset and harmonic guided campaign
------------------------------------------------------

Validate the prepared 12-run Wave 5.2B polished-dataset campaign without
training:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -PreflightOnly

Launch locally only after confirming the prepared campaign state is intended:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1

Remote launch delegates to the repository-owned remote campaign runner:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_offset_harmonic_guided_campaign.ps1 -Remote

After normal campaign closeout, the separate operator-launched official TE
Curve Verification Pipeline refresh evaluates the selected harmonic-profile
registry candidates across ``global``, ``Fw``, and ``Bw``. Run it locally with:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1

Or delegate it to the remote campaign runner:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1 -Remote
