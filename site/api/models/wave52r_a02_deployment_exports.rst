Wave 5.2R A02 Deployment Exports
================================

The A02 export tools reconstruct the verified routed K01/H08 curve
composition, export its fixed-shape ONNX graph, and validate campaign, ONNX
Runtime, and independent float32 PLC-reference parity over all 194 official
test conditions.

The deployment package is a full-curve composer. It requires complete K01 and
H08 2048-sample prediction curves and does not replace their upstream
inference contracts. TwinCAT compilation, activated-target execution, timing,
and commissioned TestRig compensation remain separate gates.

.. automodule:: scripts.export.wave_5_2r.export_wave52r_a02_composition_and_validate_parity
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: scripts.models.promote_wave52r_a02_export_archive
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: scripts.deployment.twincat_onnx_conversion.install_wave52r_a02_standalone_package
   :members:
   :undoc-members:
   :show-inheritance:
