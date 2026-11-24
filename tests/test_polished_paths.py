"""Regression tests for canonical and explicitly selected polished paths."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.tooling.polished_path_support import resolve_polished_direction


class PolishedPathTests(unittest.TestCase):
    def test_canonical_and_alternate_root(self):
        with TemporaryDirectory() as temp:
            base = Path(temp)
            canonical = base / "data" / "polished_dataset"
            alternate = base / "results" / "qualification" / "subset" / "polished_dataset"
            for root in (canonical, alternate):
                for direction in ("forward", "backward"):
                    path = root / direction / "30degree" / "100rpm" / "100.0rpm100.0Nm30.0deg.csv"
                    path.parent.mkdir(parents=True)
                    path.touch()
                    self.assertEqual(resolve_polished_direction(path, root), direction)
                    self.assertEqual(resolve_polished_direction(path), direction)
            with self.assertRaises(ValueError):
                resolve_polished_direction(path, canonical)

    def test_reject_wrong_direction_and_root(self):
        with TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "polished_dataset"
            for path in (root / "other" / "file.csv",
                         root / "file.csv",
                         base / "other" / "forward" / "file.csv",
                         root / "polished_dataset" / "forward" / "file.csv"):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    resolve_polished_direction(path)


if __name__ == "__main__":
    unittest.main()
