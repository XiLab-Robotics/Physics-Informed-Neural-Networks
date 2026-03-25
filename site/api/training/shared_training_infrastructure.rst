Shared Training Infrastructure
==============================

This page documents the reusable infrastructure that resolves TE experiment
identity, prepares immutable artifact folders, initializes shared Lightning
components, and maintains family/program registries.

.. automodule:: scripts.training.shared_training_infrastructure
   :no-members:

.. autoclass:: scripts.training.shared_training_infrastructure.ExperimentIdentity
   :members:

.. autoclass:: scripts.training.shared_training_infrastructure.ModelParameterSummary
   :members:

.. autoclass:: scripts.training.shared_training_infrastructure.RunArtifactIdentity
   :members:

.. autofunction:: scripts.training.shared_training_infrastructure.load_training_config

.. autofunction:: scripts.training.shared_training_infrastructure.resolve_experiment_identity

.. autofunction:: scripts.training.shared_training_infrastructure.prepare_output_artifact_training_config

.. autofunction:: scripts.training.shared_training_infrastructure.resolve_run_artifact_identity

.. autofunction:: scripts.training.shared_training_infrastructure.create_datamodule_from_training_config

.. autofunction:: scripts.training.shared_training_infrastructure.create_regression_backbone_from_training_config

.. autofunction:: scripts.training.shared_training_infrastructure.create_regression_module_from_training_config

.. autofunction:: scripts.training.shared_training_infrastructure.initialize_training_components

.. autofunction:: scripts.training.shared_training_infrastructure.fetch_first_batch

.. autofunction:: scripts.training.shared_training_infrastructure.validate_batch_dictionary

.. autofunction:: scripts.training.shared_training_infrastructure.build_common_metrics_snapshot

.. autofunction:: scripts.training.shared_training_infrastructure.save_yaml_snapshot

.. autofunction:: scripts.training.shared_training_infrastructure.save_training_config_snapshot

.. autofunction:: scripts.training.shared_training_infrastructure.save_common_metrics_snapshot

.. autofunction:: scripts.training.shared_training_infrastructure.update_family_registry

.. autofunction:: scripts.training.shared_training_infrastructure.update_program_registry

.. autofunction:: scripts.training.shared_training_infrastructure.save_run_metadata_snapshot
