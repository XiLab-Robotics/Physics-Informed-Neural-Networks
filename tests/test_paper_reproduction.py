"""Small stdlib-only safety tests; no scientific training or PLC required."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run


class PaperReproductionTests(unittest.TestCase):
    def test_model_restrictions(self):
        with self.assertRaises(ValueError):
            run.onnx_path("integrated_specialist_a02", "forward")
        with self.assertRaises(ValueError):
            run.onnx_path("complex_harmonic_coefficient_h08", "backward")
        self.assertTrue(str(run.onnx_path("harmonic_regression", "forward")).endswith("model.onnx"))

    def test_paired_dataset_header_and_count(self):
        with TemporaryDirectory() as t:
            root = Path(t)
            for direction in run.DIRECTIONS:
                f = root / direction / "25degree" / "100rpm" / "100.0rpm50.0Nm25.0deg.csv"
                f.parent.mkdir(parents=True)
                f.write_text("theta,theta_dot,tau_load,T,theta_TE\n0,1,1,25,0.01\n")
            run.validate_data(root, allow_incomplete=True)
            with self.assertRaises(ValueError):
                run.validate_data(root, allow_incomplete=False)
            (root / "backward" / "25degree" / "100rpm" / "100.0rpm50.0Nm25.0deg.csv").unlink()
            with self.assertRaises(ValueError):
                run.validate_data(root, allow_incomplete=True)


if __name__ == "__main__":
    unittest.main()
