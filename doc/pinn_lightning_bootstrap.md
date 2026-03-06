# Documento di Progetto: Bootstrap PINN con PyTorch Lightning

## 1) Obiettivo tecnico

Inizializzare una base progetto per una Physics-Informed Neural Network (PINN) in PyTorch con orchestrazione training tramite PyTorch Lightning, includendo:

- struttura moduli coerente con il README.md;
- requirements.txt riproducibile;
- ambiente sandbox locale (.venv) per isolamento dipendenze;
- script di verifica rapida eseguibile da terminale (Codex CLI) per confermare installazione e runtime.

Output atteso della fase di implementazione (dopo conferma):

- repository scaffold pronto a training baseline;
- comando unico di setup ambiente;
- comando unico di sanity check.

## 2) Formulazione matematica/fisica

Prima versione del problema (baseline estendibile):

- target: y_hat_theta = f_theta(x) con x contenente stato cinematico/operativo (es. angolo, coppia, temperatura);
- variabile osservata: errore di trasmissione rotazionale y = RTE.

Loss composita PINN:

L_tot = L_data + lambda_phys * L_phys + lambda_reg * ||theta||_2^2

con:

- L_data: MSE su dati misurati;
- L_phys: residuo dei vincoli fisici (inizialmente interfaccia/placeholder, poi esteso con vincoli specifici RV reducer);
- L_reg: regolarizzazione pesi.

Scelta numerica iniziale:

- normalizzazione input/output per condizionamento del gradiente;
- attivazioni tanh (o SiLU) per regolarita della funzione appresa;
- ottimizzatore AdamW;
- gradient clipping in Lightning per stabilita.

## 3) Modifiche previste a moduli e interfacce

Struttura proposta (fase implementativa):

- configs/
  - pinn_default.yaml (iperparametri training/model/loss)
- src/pinn_rv/
  - data/datamodule.py (LightningDataModule)
  - models/pinn_model.py (rete fully-connected baseline)
  - losses/data_loss.py
  - losses/physics_loss.py (interfaccia + placeholder fisico)
  - losses/composite_loss.py
  - training/lightning_module.py (LightningModule)
  - utils/seed.py, utils/metrics.py
- training/train.py (entrypoint training)
- training/validate_env.py (sanity check ambiente/dipendenze)
- requirements.txt
- .venv/ (non versionata, locale)

Interfacce minime:

- PhysicsLoss.forward(batch, preds) -> torch.Tensor
- CompositeLoss.forward(batch, preds, model) -> dict[str, torch.Tensor]
- PINNLightningModule.training_step(batch, batch_idx) -> torch.Tensor

## 4) Piano di validazione (test numerici, benchmark, metriche)

Validazione ambiente/tooling:

1. creazione .venv e install pip install -r requirements.txt;
2. python -c "import torch, lightning; print(...)";
3. python training/validate_env.py con check su:
   - versione Python;
   - import pacchetti core;
   - disponibilita CUDA (se presente);
   - forward pass dummy e backward pass dummy.

Validazione numerica baseline:

1. overfit controllato su mini-batch (sanity learning);
2. monitoraggio L_data, L_phys, L_tot;
3. metriche iniziali: MSE, RMSE, MAE;
4. verifica stabilita: assenza NaN/Inf, grad norm entro soglia.

## 5) Rischi tecnici e fallback

Rischi:

- mismatch versioni torch/lightning/python;
- instabilita iniziale della componente fisica;
- dataset reale con scaling eterogeneo e outlier.

Fallback:

- bloccare baseline su sola L_data (lambda_phys=0) per validare pipeline;
- pinning versioni conservative in requirements.txt;
- clipping gradiente + scheduler LR + normalizzazione robusta.

Trade-off dichiarati:

- maggiore lambda_phys migliora coerenza fisica ma puo rallentare convergenza;
- architetture piu profonde aumentano capacita ma riducono robustezza/tempo reale;
- tuning stabilita (clipping, regolarizzazione) puo ridurre picchi prestazionali ma aumenta affidabilita.

## 6) Procedura operativa prevista (dopo conferma)

1. creare scaffolding cartelle/file Python;
2. aggiungere requirements.txt;
3. generare .gitignore update per escludere .venv/;
4. creare script training/validate_env.py;
5. creare ambiente sandbox locale ed eseguire verifica da terminale;
6. riportare output sintetico della verifica eseguita in Codex CLI.
