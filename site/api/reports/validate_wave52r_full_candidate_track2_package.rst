Wave 5.2R Full-Candidate Track 2 Package
========================================

This workflow inventories every Wave 5.2R trained artifact and prepares the
eligible real-data predictors for one polished-setpoint forward
``TE Curve Verification Pipeline`` comparison.

The package keeps temporal and non-temporal lanes separate. It includes the
accepted periodic GRU, accepted periodic harmonic MLP, PF-A, H04, K01, and
every other eligible Stage 4 through Stage 12 predictor. Calibration-only,
replay-only, and synthetic-oracle artifacts remain visible with explicit
exclusion reasons.

Validate the package without running the matrix:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
       -PreflightOnly

Run the matrix on the configured remote workstation:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_full_candidate_track2_analysis.ps1 `
       -Remote `
       -Run

.. automodule:: scripts.analysis.wave_5_2r.validate_wave52r_full_candidate_track2_package
   :members:
   :undoc-members:
   :show-inheritance:
