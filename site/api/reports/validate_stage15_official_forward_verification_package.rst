Stage 15 Official Forward Verification Package
================================================

This validator checks the hash-locked H04 checkpoint, PF-A anchor, accepted
reference inventories, and exact replay of the 97 frozen Stage 5 forward test
curves before the operator launches the official curve-verification matrix.

The corresponding PowerShell launcher supports local and remote execution:

.. code-block:: powershell

   .\scripts\campaigns\track_2\run_wave52r_stage15_official_forward_verification.ps1 `
       -Remote `
       -Run

The completed matrix was reviewed under the multi-index curve-first policy.
H04 improved PF-A and selected shape metrics but did not displace the accepted
periodic GRU. No registry promotion was made.

The frozen evidence can be rebuilt into the canonical visual closeout with:

.. code-block:: powershell

   conda run --no-capture-output -n pinns_env python -B `
       scripts/reports/closeout/wave_5_2/build_stage15_official_forward_verification_closeout.py

.. automodule:: scripts.analysis.wave_5_2r.validate_stage15_official_forward_verification_package
   :members:
   :undoc-members:
   :show-inheritance:
