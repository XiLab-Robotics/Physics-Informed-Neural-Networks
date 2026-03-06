from typing import List
import torch
import pytorch_lightning as pl

# Ensure A Simple MLP Regressor Is Used
class MLPRegressor(pl.LightningModule):

    def __init__(
        self,
        input_dim: int,
        hidden: List[int],
        dropout: float,
        lr: float,
    ) -> None:
        super().__init__()
        self.save_hyperparameters()

        layers = []
        d_in = input_dim
        for d_out in hidden:
            layers.append(torch.nn.Linear(d_in, d_out))
            layers.append(torch.nn.ReLU())
            if dropout > 0.0:
                layers.append(torch.nn.Dropout(dropout))
            d_in = d_out

        layers.append(torch.nn.Linear(d_in, 1))
        self.net = torch.nn.Sequential(*layers)

        # Ensure A Stable Regression Loss Is Used
        self.loss_fn = torch.nn.MSELoss()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        self.log("train_mse", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        self.log("val_mse", loss, prog_bar=True)

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        self.log("test_mse", loss, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.lr)