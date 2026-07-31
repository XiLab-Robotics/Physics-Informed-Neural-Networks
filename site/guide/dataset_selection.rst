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

Shape-gate loss v2 checkpoint-selection pilot
---------------------------------------------

Validate the prepared one-run polished setpoint forward pilot without training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 -PreflightOnly

Run one-batch validation without launching training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
     -PreflightOnly `
     -RunOneBatchValidation

Launch locally only after confirming the prepared campaign state is intended:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1

Remote launch delegates to the repository-owned remote campaign runner:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 -Remote

Causal offset / mean calibration pilot
--------------------------------------

Validate the prepared two-arm ``polished_dataset`` setpoint ``Fw`` pilot
without training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
     -PreflightOnly `
     -RunOneBatchValidation

Launch the pilot on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_causal_offset_mean_calibration_pilot_campaign.ps1 `
     -Remote

Shape-gate loss v2 bounded TE Curve Verification screen
-------------------------------------------------------

After the checkpoint-selection pilot is closed out, validate the bounded
``polished_dataset`` setpoint ``Fw`` verification-screen package with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 `
     -PreflightOnly

Launch the bounded screen on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 `
     -Remote

Parallel shape-objective follow-up
----------------------------------

Validate the prepared three-arm ``polished_dataset`` setpoint ``Fw`` follow-up
without training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1 `
     -PreflightOnly `
     -RunOneBatchValidation

Launch the follow-up on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_parallel_shape_objective_followup_campaign.ps1 `
     -Remote

Shape-objective bounded TE Curve Verification screen
----------------------------------------------------

After the shape-objective follow-up is closed out, validate the bounded
``polished_dataset`` setpoint ``Fw`` verification-screen package with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
     -PreflightOnly

Launch the bounded screen on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_objective_bounded_track2_screen.ps1 `
     -Remote

Shape-first training-rule distillation pilot
--------------------------------------------

Validate the prepared two-arm ``polished_dataset`` setpoint ``Fw`` pilot
without training:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
     -PreflightOnly `
     -RunOneBatchValidation

Launch the pilot on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\cross_wave\run_shape_first_training_rule_distillation_pilot_campaign.ps1 `
     -Remote

Shape-first distillation bounded TE Curve Verification screen
-------------------------------------------------------------

After the shape-first distillation pilot is closed out, validate the bounded
``polished_dataset`` setpoint ``Fw`` verification-screen package with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1 `
     -PreflightOnly

Launch the bounded screen on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_shape_first_distillation_bounded_track2_screen.ps1 `
     -Remote

Causal offset bounded TE Curve Verification screen
--------------------------------------------------

After the causal offset / mean calibration pilot is closed out, validate the
bounded ``polished_dataset`` setpoint ``Fw`` verification-screen package with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_causal_offset_bounded_track2_screen.ps1 `
     -PreflightOnly

Launch the bounded screen on the remote workstation with:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_causal_offset_bounded_track2_screen.ps1 `
     -Remote

After normal campaign closeout, the separate operator-launched official TE
Curve Verification Pipeline refresh evaluates the selected harmonic-profile
registry candidates across ``global``, ``Fw``, and ``Bw``. Run it locally with:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1

Or delegate it to the remote campaign runner:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52b_te_curve_verification_refresh.ps1 -Remote

Reduced non-MMT cross-wave evaluation
-------------------------------------

The reduced cross-wave launcher keeps forward and backward surfaces separate
across polished setpoints, simplified setpoints, and polished actual values.
Print the six-cell plan without evaluating models:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1

Run the prepared evaluation locally or on the configured LAN workstation:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 -Run
   .\scripts\campaigns\track_2\run_reduced_selected_track2_reports.ps1 -Remote -Run

The launcher excludes MMT and ``global``. It synchronizes required code,
configuration, documentation, and selected model archives before remote
execution, then retrieves the generated reports, matrix artifacts, and logs.
Official promotion remains a separate curve-first review step.

Wave 5.2R full-candidate forward comparison
-------------------------------------------

The completed Wave 5.2R artifact inventory supports a forward-only comparison
between every eligible trained candidate, the accepted periodic GRU, the
accepted periodic harmonic MLP, and PF-A. Validate the package without running
the matrix:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
     -PreflightOnly

Run the matrix locally or on the configured LAN workstation:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 -Run
   .\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 -Remote -Run

The final decision keeps temporal and non-temporal rankings separate and uses
the multi-index curve-first policy rather than scalar campaign rank alone.

Wave 5.2R offline-leader cross-surface promotion
------------------------------------------------

K01 and H08 passed the local replay, causal/state, ONNX-parity, fallback, and
host-latency gates. The 27-run campaign completed with zero failures on
2026-07-31. Its reproducibility preflight command is:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 `
     -PreflightOnly

Run it locally or on the configured LAN workstation:

.. code-block:: powershell

   .\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 -Run
   .\scripts\campaigns\wave_5_2\run_wave52r_offline_leader_cross_surface_promotion.ps1 -Remote -Run

The completed campaign keeps ``Fw``, ``Bw``, and direction-aware ``global`` distinct.
Periodic GRU and periodic harmonic MLP remain accepted controls; campaign rank
alone cannot promote K01 or H08.

Run the prepared 24-candidate official review remotely:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_offline_leader_cross_surface_track2.ps1 -Remote -Run

The launcher evaluates ``forward``, ``backward``, and ``global`` separately.
The completed 2026-07-31 run evaluated all 24 candidates, followed by CVP 1.2
and visual review. K01 seed 271828 is the cross-surface temporal offline
leader. H08 remains a forward non-temporal specialist because its backward and
global raw and offset errors regressed. Periodic GRU and periodic harmonic MLP
remain accepted unchanged.
