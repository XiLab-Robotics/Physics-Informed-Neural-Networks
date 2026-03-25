Transmission Error DataModule
=============================

This page documents the Lightning datamodule and batch-collation helpers used
by the TE regression training workflow.

.. automodule:: scripts.training.transmission_error_datamodule
   :no-members:

.. autoclass:: scripts.training.transmission_error_datamodule.NormalizationStatistics
   :members:

.. autoclass:: scripts.training.transmission_error_datamodule.DatasetSplitSummary
   :members:

.. autofunction:: scripts.training.transmission_error_datamodule.move_batch_tensor_collection_to_device

.. autofunction:: scripts.training.transmission_error_datamodule.extract_point_tensor_from_curve_sample

.. autofunction:: scripts.training.transmission_error_datamodule.collate_transmission_error_points

.. autoclass:: scripts.training.transmission_error_datamodule.TransmissionErrorDataModule
   :members:
