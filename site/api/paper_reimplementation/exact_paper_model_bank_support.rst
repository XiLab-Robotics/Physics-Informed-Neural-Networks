Exact Paper Model Bank Support
==============================

This page documents the helper utilities used by the strict paper-faithful
RCIM exact model-bank validation branch. The current RCIM Model-Bank Reproduction paper-faithful
surface preserves the recovered original pipeline protocol and feeds the
accepted forward/backward archives under ``models/paper_reference/rcim_track1``.

RCIM Model-Bank Reproduction is closed at the full-dataset faithful model-bank level; later
all-green or restricted-dataset studies are separate optimization/comparison
branches.

.. automodule:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support
   :no-members:

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.load_exact_model_bank_config

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.build_exact_paper_dataset_bundle

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.create_exact_paper_base_estimator

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.fit_exact_family_model_bank

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.evaluate_exact_family_model_bank

.. autofunction:: scripts.paper_reimplementation.rcim_ml_compensation.exact_paper_model_bank.exact_paper_model_bank_support.export_exact_family_python_and_onnx_bank
