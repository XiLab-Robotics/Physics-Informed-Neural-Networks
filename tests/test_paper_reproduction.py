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

    def test_pretrained_checkpoints_are_binary(self):
        """The selected Lightning checkpoints must not be text links or LFS pointers."""
        directory = run.ROOT / "models" / "direct_ml"
        checkpoints = list(directory.rglob("*.ckpt"))
        self.assertEqual(18, len(checkpoints), "Expected 18 promoted Lightning checkpoints")
        for file in checkpoints:
            with self.subTest(file=str(file.relative_to(run.ROOT))):
                self.assertGreater(file.stat().st_size, 4096, "Checkpoint is not a binary artifact")
                with file.open("rb") as stream:
                    prefix = stream.read(128)
                self.assertFalse(prefix.startswith(b"../"), "Broken historical relative link")
                self.assertFalse(prefix.startswith(b"version https://git-lfs.github.com/spec/v1"),
                                 "Unmaterialized Git LFS pointer")

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
