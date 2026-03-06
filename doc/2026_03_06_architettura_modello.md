# 20260306 Architettura Modello

## Obiettivo
Definire una architettura MLP compatibile con PINN per RTE e una strategia di training in due fasi: Adam + L-BFGS.

## 1) Input, output e heads

Input base per campione:
- `theta` (angolo uscita, in radianti)
- `sin(theta)`, `cos(theta)` (embedding periodico)
- `v_norm` (velocita normalizzata)
- `tau_norm` (coppia normalizzata)
- `T_norm` (temperatura normalizzata)
- `dir_flag` (`+1` forward, `-1` backward)

Output previsti:
- Head 1: `TE_hat(theta,v,tau,T,dir)`
- Head 2 (armonica): vettori `A_k`, `phi_k` per `k in H`
- Head 3 opzionale (fisica): quantita ausiliarie per `f1..f4`

## 2) Proposta MLP

Backbone consigliato (default):
- 6 hidden layers
- 128 neuroni per layer
- residual skip ogni 2 layer (stabilita)
- layer norm opzionale solo se necessario (default off)

Attivazioni:
- opzione A (default PINN): `tanh`
- opzione B (ablation): `swish/SiLU`

Motivazione:
- `tanh` favorisce regolarita delle derivate angolari e stabilita dei vincoli fisici;
- `swish` puo accelerare convergenza dati-driven ma puo rendere meno pulita la parte di vincoli differenziali.

## 3) Loss totale e pesi

`L_tot = w_data*L_data + w_phys*L_phys + w_harm*L_harm + w_reg*L_reg`

Schema iniziale pesi:
- `w_data = 1.0`
- `w_phys = 0.5` (warm-up) -> fino a `1.0` dopo stabilizzazione
- `w_harm = 0.3`
- `w_reg = 1e-6`

I pesi saranno in config YAML per tuning riproducibile.

## 4) Strategia di addestramento

### Fase A - Adam (esplorazione)
- Ottimizzatore: `AdamW`
- LR iniziale: `2e-3`
- Weight decay: `1e-6`
- Batch size: 1024 (adattabile a memoria)
- Epoch: 200-500 (o stop su plateau)
- Scheduler: cosine decay o ReduceLROnPlateau
- Gradient clipping: 1.0

Obiettivo Fase A:
- entrare in regione stabile del minimo;
- bilanciare `L_data` e `L_phys` senza instabilita.

### Fase B - L-BFGS (rifinitura PINN)
- Ottimizzatore: `torch.optim.LBFGS`
- `lr=1.0`, `max_iter=500`, `history_size=50`, `line_search_fn='strong_wolfe'`
- full-batch o large-batch deterministico
- closure con calcolo completo di `L_tot`

Obiettivo Fase B:
- migliorare accuratezza fine sui vincoli fisici;
- ridurre residui Eq. 29/30 e mismatch armonico.

## 5) Metriche e criteri stop

Metriche train/val:
- MSE, RMSE, MAE sul TE
- residual norm Eq. 29/30
- errore armonico per ordine `k` (su `A_k`, `phi_k`)

Early stopping:
- monitor su metrica composita val
- patience separata per Fase A e Fase B

## 6) Trade-off e rischi

- modello piu profondo: migliore capacita, ma maggiore costo e rischio instabilita LBFGS
- troppa enfasi fisica: underfit locale su porzioni rumorose
- troppa enfasi dati: perdita interpretabilita meccanica

Mitigazione:
- curriculum su `w_phys`
- controllo gradienti e fallback a sola `L_data` per debug.
