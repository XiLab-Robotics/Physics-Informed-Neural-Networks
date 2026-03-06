import yaml
import torch
from pathlib import Path

from models.mlp_regressor import MLPRegressor

# Ensure The ONNX Export Matches The Inference Input Shape
def main() -> None:
    cfg = yaml.safe_load(Path("config/config.yaml").read_text())

    # Ensure The Best Checkpoint Is Used
    ckpt_path = Path("lightning_logs")
    candidates = list(ckpt_path.rglob("best.ckpt"))
    if not candidates:
        raise FileNotFoundError("No best.ckpt found. Train first.")
    best = candidates[-1]

    model = MLPRegressor.load_from_checkpoint(str(best))
    model.eval()

    dummy = torch.randn(1, 5, dtype=torch.float32)

    out_path = Path("artifacts/te_mlp.onnx")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    torch.onnx.export(
        model,
        dummy,
        str(out_path),
        input_names=["x"],
        output_names=["te_norm"],
        opset_version=17,
        dynamic_axes={"x": {0: "batch"}, "te_norm": {0: "batch"}},
    )

if __name__ == "__main__":
    main()