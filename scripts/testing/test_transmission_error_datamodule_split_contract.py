"""Lightweight source-contract regressions for the TE DataModule test split.

These tests use Python's AST to isolate the fail-fast guard without importing
heavy Lightning/PyTorch dependencies or loading large scientific datasets.
They do not replace a native DataModule integration or training smoke test.
"""

from __future__ import annotations

# Standard Library Imports
import ast
from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DATAMODULE_SOURCE_PATH = (
    REPOSITORY_ROOT / "scripts" / "training" / "transmission_error_datamodule.py"
)
DATASET_CONFIG_PATH = (
    REPOSITORY_ROOT / "config" / "datasets" / "transmission_error_dataset.yaml"
)


def extract_training_test_split_guard() -> tuple[object, int, int]:
    """Compile the production DataModule's nonempty-test guard in isolation."""
    syntax_tree = ast.parse(DATAMODULE_SOURCE_PATH.read_text(encoding="utf-8"))
    datamodule_class = next(
        node for node in syntax_tree.body
        if isinstance(node, ast.ClassDef) and node.name == "TransmissionErrorDataModule"
    )
    setup_method = next(
        node for node in datamodule_class.body
        if isinstance(node, ast.FunctionDef) and node.name == "setup"
    )
    guard_list = [
        node for node in setup_method.body
        if isinstance(node, ast.If)
        and isinstance(node.test, ast.UnaryOp)
        and isinstance(node.test.op, ast.Not)
        and isinstance(node.test.operand, ast.Name)
        and node.test.operand.id == "test_directional_file_manifest"
    ]
    if len(guard_list) != 1:
        raise AssertionError(
            "DataModule.setup must contain exactly one nonempty-test precondition"
        )
    guard = guard_list[0]
    test_dataset_construction = [
        node for node in ast.walk(setup_method)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Attribute)
            and target.attr == "test_dataset"
            for target in node.targets
        )
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "TransmissionErrorCurveDataset"
    ]
    if len(test_dataset_construction) != 1:
        raise AssertionError("DataModule test dataset construction could not be isolated")
    construction_line = test_dataset_construction[0].lineno
    isolated_module = ast.fix_missing_locations(
        ast.Module(body=[guard], type_ignores=[])
    )
    return compile(isolated_module, str(DATAMODULE_SOURCE_PATH), "exec"), guard.lineno, construction_line


class TransmissionErrorDataModuleSplitContractTests(unittest.TestCase):
    """Check fail-fast behavior and unchanged default dataset split."""

    def test_zero_test_split_is_rejected_before_dataset_construction(self) -> None:
        """A zero-test manifest must yield an explanatory ValueError."""
        guard_code, guard_line, construction_line = extract_training_test_split_guard()
        self.assertLess(guard_line, construction_line)
        with self.assertRaisesRegex(ValueError, "nonempty test split"):
            exec(guard_code, {"test_directional_file_manifest": []})

    def test_nonempty_test_manifest_passes_guard(self) -> None:
        """A normal test manifest must reach subsequent dataset setup."""
        guard_code, _, _ = extract_training_test_split_guard()
        synthetic_test_manifest = [(Path("synthetic_test.csv"), "forward")]
        exec(
            guard_code,
            {"test_directional_file_manifest": synthetic_test_manifest},
        )

    def test_default_dataset_split_remains_ten_percent(self) -> None:
        """The public training default remains 0.1 (not a zero-test setup)."""
        config_text = DATASET_CONFIG_PATH.read_text(encoding="utf-8")
        self.assertRegex(config_text, r"(?m)^  test_split: 0\\.1\\s*$")


if __name__ == "__main__":
    unittest.main()
