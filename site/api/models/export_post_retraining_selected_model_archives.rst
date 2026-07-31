Post-Retraining Model Archive Promotion
=======================================

The dedicated exporter rebuilds and validates the five approved Wave 5.2R
archive leaves outside ``models/``. Its default mode is non-promoting. The
``--promote`` option installs the validated K01, H08, and H04 family roots only
when those destinations do not already exist, then regenerates the polished
setpoint aggregate inventory. The ``--validate-existing`` mode checks the
installed aggregate counts, all recorded Python and ONNX paths, and every
available artifact hash without rebuilding staging.

Archive preservation records an offline or exploratory role; it does not
claim TwinCAT runtime qualification or change the accepted deployment leaders.

.. automodule:: scripts.models.export_post_retraining_selected_model_archives
   :members:
   :undoc-members:
   :show-inheritance:
