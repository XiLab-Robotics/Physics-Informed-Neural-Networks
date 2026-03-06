import yaml
from pathlib import Path

import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint

from utils.seed import seed_everything
from datasets.te_dataset import TEDataset, build_loaders
from models.mlp_regressor import MLPRegressor

# Ensure The Training Entry-Point Is Deterministic And Simple
def main() -> None:

    cfg_path = Path("config/config.yaml")
    cfg = yaml.safe_load(cfg_path.read_text())

    seed_everything(cfg["split"]["seed"])

    # Ensure Dataset Is Built From The Paper CSV Structure
    ds = TEDataset(
        csv_dir=cfg["data"]["csv_dir"],
        index_csv=cfg["data"]["index_csv"],
        theta_unit=cfg["data"]["theta_unit"],
        normalize_x=cfg["data"]["normalize"]["x"],
        normalize_y=cfg["data"]["normalize"]["y"],
    )

    loaders = build_loaders(
        dataset=ds,
        train_ratio=cfg["split"]["train"],
        val_ratio=cfg["split"]["val"],
        test_ratio=cfg["split"]["test"],
        seed=cfg["split"]["seed"],
        batch_size=cfg["train"]["batch_size"],
        num_workers=cfg["train"]["num_workers"],
    )

    model = MLPRegressor(
        input_dim=5,
        hidden=cfg["model"]["hidden"],
        dropout=cfg["model"]["dropout"],
        lr=cfg["train"]["lr"],
    )

    ckpt = ModelCheckpoint(monitor="val_mse", mode="min", save_top_k=1, filename="best")
    es = EarlyStopping(monitor="val_mse", mode="min", patience=cfg["train"]["patience"])

    trainer = pl.Trainer(
        max_epochs=cfg["train"]["max_epochs"],
        callbacks=[ckpt, es],
        accelerator="auto",
        devices="auto",
        log_every_n_steps=50,
    )

    trainer.fit(model, loaders["train"], loaders["val"])
    trainer.test(model, dataloaders=loaders["test"], ckpt_path="best")


if __name__ == "__main__":
    main()