from __future__ import annotations

# Import Python Utilities
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class TrainingRunPlan:

    """Describe a single training run before execution.

    This structure captures the minimum set of values needed to stage a
    reproducible feedforward-network training run. The fields are intentionally
    concrete so the generated documentation can show a realistic API object
    rather than a toy example with abstract placeholders.

    Attributes:
        run_name: Human-readable logical name for the experiment.
        dataset_config_path: Absolute or repository-relative path to the dataset
            configuration YAML used by the datamodule.
        output_root: Root directory where training artifacts should be written.
        learning_rate: Optimizer learning rate used for the run.
        max_epochs: Upper training bound enforced by the trainer.
        fast_dev_run: When ``True``, the plan is intended for a short smoke test
            rather than a full optimization run.
    """

    run_name: str
    dataset_config_path: Path
    output_root: Path
    learning_rate: float
    max_epochs: int
    fast_dev_run: bool = False


def build_run_instance_id(run_name: str, timestamp_tag: str) -> str:

    """Create the immutable artifact identifier for a training execution.

    The repository distinguishes between a logical experiment name and the
    physical artifact folder used to store outputs. This helper encodes that
    convention by attaching a timestamp-like tag to the logical run name.

    Args:
        run_name: Logical experiment name chosen by the user or YAML
            configuration.
        timestamp_tag: Immutable time-based token such as
            ``2026-03-22_11-40-00``.

    Returns:
        The repository-style run instance identifier in the form
        ``<run_name>__<timestamp_tag>``.

    Raises:
        ValueError: If either input is blank after trimming whitespace.

    Examples:
        >>> build_run_instance_id("feedforward_baseline", "2026-03-22_11-40-00")
        'feedforward_baseline__2026-03-22_11-40-00'
    """

    # Normalize Raw Inputs
    normalized_run_name = run_name.strip()
    normalized_timestamp_tag = timestamp_tag.strip()

    # Validate Required Tokens
    if not normalized_run_name:
        raise ValueError("run_name must not be empty")

    if not normalized_timestamp_tag:
        raise ValueError("timestamp_tag must not be empty")

    # Compose Immutable Run Identifier
    return f"{normalized_run_name}__{normalized_timestamp_tag}"


def resolve_training_output_directory(model_family: str, run_instance_id: str, output_root: Path) -> Path:

    """Resolve the canonical output directory for a training run.

    The project stores training artifacts under family-specific roots so that
    experiment outputs, validation checks, and campaign-level registries remain
    inspectable. This helper documents the exact folder convention used for a
    single training run.

    Args:
        model_family: Canonical family name such as ``feedforward_network`` or
            ``harmonic_regression``.
        run_instance_id: Immutable artifact identifier for the current
            execution.
        output_root: Root output directory, typically the repository ``output``
            folder.

    Returns:
        Full path of the training-run directory inside
        ``output/training_runs/<model_family>/<run_instance_id>/``.

    Raises:
        ValueError: If ``model_family`` or ``run_instance_id`` is empty.

    Notes:
        This helper does not create directories on disk. It only computes the
        canonical destination so orchestration code can decide when filesystem
        side effects should happen.
    """

    # Normalize Family-Level Identifiers
    normalized_model_family = model_family.strip()
    normalized_run_instance_id = run_instance_id.strip()

    # Validate Canonical Path Tokens
    if not normalized_model_family:
        raise ValueError("model_family must not be empty")

    if not normalized_run_instance_id:
        raise ValueError("run_instance_id must not be empty")

    # Build Family-Oriented Output Path
    return output_root / "training_runs" / normalized_model_family / normalized_run_instance_id


def prepare_training_run_plan(
    run_name: str,
    dataset_config_path: Path,
    output_root: Path,
    learning_rate: float,
    max_epochs: int,
    fast_dev_run: bool = False,
) -> TrainingRunPlan:

    """Validate user-facing inputs and package them into a run plan.

    This function represents the boundary between loose CLI-style inputs and a
    strongly typed internal execution plan. In the real training script, this is
    where repository conventions should be enforced before Lightning objects,
    datamodules, or checkpoint callbacks are instantiated.

    Args:
        run_name: Logical experiment label shown in logs and registry files.
        dataset_config_path: Path to the dataset YAML consumed by the
            transmission-error datamodule.
        output_root: Base directory used to build the final artifact path.
        learning_rate: Positive optimizer step size.
        max_epochs: Positive upper bound for training epochs.
        fast_dev_run: Whether the plan targets a quick debugging pass.

    Returns:
        A validated :class:`TrainingRunPlan` instance ready for later
        orchestration.

    Raises:
        FileNotFoundError: If the dataset configuration file does not exist.
        ValueError: If numeric values are invalid or if ``run_name`` is blank.

    Examples:
        >>> config_path = Path("config/dataset/default.yaml")
        >>> prepare_training_run_plan("baseline", config_path, Path("output"), 1e-3, 100)
        TrainingRunPlan(...)
    """

    # Validate Basic Scalar Inputs
    if not run_name.strip():
        raise ValueError("run_name must not be empty")

    if learning_rate <= 0.0:
        raise ValueError("learning_rate must be strictly positive")

    if max_epochs <= 0:
        raise ValueError("max_epochs must be greater than zero")

    # Validate External Configuration Inputs
    if not dataset_config_path.is_file():
        raise FileNotFoundError(f"dataset configuration not found: {dataset_config_path}")

    # Package Validated Training Inputs
    return TrainingRunPlan(
        run_name=run_name.strip(),
        dataset_config_path=dataset_config_path,
        output_root=output_root,
        learning_rate=learning_rate,
        max_epochs=max_epochs,
        fast_dev_run=fast_dev_run,
    )


def summarize_training_run_plan(training_run_plan: TrainingRunPlan, timestamp_tag: str) -> dict[str, object]:

    """Build the high-level execution summary shown in documentation examples.

    The summary returned by this function is intentionally close to what a real
    orchestration layer would log before launching a trainer. It demonstrates
    how structured return values render in the generated API reference and makes
    the documentation page more informative than a collection of standalone
    helper signatures.

    Args:
        training_run_plan: Validated run plan prepared by
            :func:`prepare_training_run_plan`.
        timestamp_tag: Immutable timestamp-like token used to build the
            physical artifact identifier.

    Returns:
        Dictionary containing the logical run name, immutable artifact
        identifier, resolved output directory, and a small execution-mode flag.

    Raises:
        ValueError: If ``timestamp_tag`` is empty.

    Notes:
        The return shape is kept deliberately small for readability in the API
        docs. A production implementation would usually return a dedicated data
        structure rather than a free-form dictionary.
    """

    # Resolve Immutable Runtime Identifiers
    run_instance_id = build_run_instance_id(training_run_plan.run_name, timestamp_tag)
    output_directory = resolve_training_output_directory(
        model_family="feedforward_network",
        run_instance_id=run_instance_id,
        output_root=training_run_plan.output_root,
    )

    # Assemble Documentation-Friendly Summary
    return {
        "run_name": training_run_plan.run_name,
        "run_instance_id": run_instance_id,
        "output_directory": output_directory,
        "execution_mode": "fast_dev_run" if training_run_plan.fast_dev_run else "full_training",
    }
