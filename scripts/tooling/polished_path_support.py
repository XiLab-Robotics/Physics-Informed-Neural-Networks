"""Resolve direction without assuming the canonical polished data root."""
from pathlib import Path


def resolve_polished_direction(csv_file_path: str | Path,
                               dataset_root: str | Path | None = None) -> str:
    """Require a forward/backward child of a canonical or alternate polished root.

    When the caller knows the selected dataset root, use it explicitly. A
    standalone curve reader can instead resolve the unique named ancestor.
    Never silently fall back to the full canonical dataset.
    """
    path = Path(csv_file_path).resolve()
    if dataset_root is None:
        roots = [parent for parent in path.parents if parent.name == "polished_dataset"]
        if len(roots) != 1:
            raise ValueError(f"Expected one polished_dataset ancestor | {path}")
        root = roots[0]
    else:
        root = Path(dataset_root).resolve()
    if root.name != "polished_dataset" or not path.is_relative_to(root):
        raise ValueError(f"CSV outside selected polished_dataset root | {path} | {root}")
    parts = path.relative_to(root).parts
    if len(parts) < 2 or parts[0].lower() not in ("forward", "backward"):
        raise ValueError(f"Polished direction folder must be forward or backward | {path}")
    return parts[0].lower()
