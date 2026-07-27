Physics-Guided Optimization Instrumentation
===========================================

This page documents the reusable Wave 5.2R loss-interaction diagnostics,
weight adapters, conflict-aware gradient composition, schedules, and
deterministic dataloader helpers.

.. automodule:: scripts.training.physics_guided_optimization_instrumentation
   :no-members:

.. autoclass:: scripts.training.physics_guided_optimization_instrumentation.LossActivationSchedule
   :members:

.. autoclass:: scripts.training.physics_guided_optimization_instrumentation.LossComponentConfiguration
   :members:

.. autoclass:: scripts.training.physics_guided_optimization_instrumentation.ParameterFreezeSchedule
   :members:

.. autoclass:: scripts.training.physics_guided_optimization_instrumentation.PhysicsGuidedOptimizationInstrumentation
   :members:

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.capture_trainable_parameter_vector

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.assign_flat_gradient_to_parameters

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.compute_update_to_parameter_ratio

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.configure_deterministic_execution

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.build_deterministic_dataloader

.. autofunction:: scripts.training.physics_guided_optimization_instrumentation.compute_dataloader_fingerprint
