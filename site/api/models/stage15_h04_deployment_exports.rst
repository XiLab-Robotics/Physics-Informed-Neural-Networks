Stage 15 H04 Deployment Exports
================================

The Stage 15 export tools build the inspectable H04 ONNX graph and a
PLC-friendly Structured Text reference package. They validate Python/ONNX and
independent float32 PLC-reference parity on all 97 frozen forward conditions.

TwinCAT compilation, execution-time measurement, and runtime replay remain
separate acceptance gates. The completed official forward comparison did not
promote H04; the export package is retained as exploratory deployment evidence.

.. automodule:: scripts.export.wave_5_2r.export_stage15_h04_onnx_and_validate_parity
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: scripts.export.wave_5_2r.build_stage15_h04_plc_reference_package
   :members:
   :undoc-members:
   :show-inheritance:
