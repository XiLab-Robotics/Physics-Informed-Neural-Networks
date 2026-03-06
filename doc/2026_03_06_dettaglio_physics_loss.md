# 2026_03_06 - Dettaglio Physics Loss (Fase 2)

## 1) Obiettivo tecnico
Definire una `physics_loss` completamente differenziabile (solo operazioni `torch`) per il modello TE, implementando:

1. Eq. (29) e Eq. (30) del paper MMT nel grafo Autograd.
2. I termini elementari `f1`, `f2_i`, `f3`, `f4_i` (Eq. 31-34) senza uscire dal grafo.
3. La consistenza armonica `L_harm` sul set `H = {0,1,3,39,40,78,81,156,162,240}`.
4. La struttura della classe `TransmissionErrorLoss` (target: `physics_loss.py` nella fase successiva).

Nota di processo: questa fase produce solo specifica tecnica; nessuna implementazione Python finche non arriva conferma esplicita.

## 2) Formulazione matematica/fisica da implementare

### 2.1 Eq. (29) - forma generale (coefficienti di trasferimento)
Si definisce:

`Delta_theta_H = c1*f1 + c2*(1/3)*sum_{i=1..3}(f2_i) + c3*f3 + c4*(1/3)*sum_{i=1..3}(f4_i)`

con:

- `c1 = (g2*g3*g4) / (1 + g1*g2*g3*g4)`
- `c2 = (g3*g4) / (1 + g1*g2*g3*g4)`
- `c3 = g4 / (1 + g1*g2*g3*g4)`
- `c4 = 1 / (1 + g1*g2*g3*g4)`

Tutte le grandezze (`g1..g4`, `f*`) saranno tensori `torch.Tensor`.

### 2.2 Eq. (30) - caso RV one-tooth-difference
Con `z5 - z4 = 1`:

`Delta_theta_H = [ -(1/z4)*f1 - (1/(3*z4))*sum_{i=1..3}(f2_i) + f3 + (1/3)*sum_{i=1..3}(f4_i) ] / [ 1 + (z1+z2)/(z2*z4) ]`

Questa forma sara il default operativo (piu robusta lato integrazione, non richiede `g1..g4` espliciti).

### 2.3 Eq. (31)-(34) - termini elementari
Indice `i = 1,2,3`.

`f1 = (1/sin(theta_b2_n)) * ( -(Delta_l_b1/l_b2)*cos(theta_b1_n) + (l_b1/l_b2)*Delta_theta_b1*sin(theta_b1_n) - (Delta_l_n/l_b2) + (Delta_l_H1/l_b2)*cos(theta_H1_n) + (Delta_l_b2/l_b2)*cos(theta_b2_n) )`

`f2_i = (1/sin(theta_v_ci)) * ( -(Delta_l_Hi/l_v)*cos(theta_Hi_ci) - (Delta_l_ai/l_v)*cos(theta_ai_ci) + (Delta_l_v/l_v)*cos(theta_v_ci) + (Delta_l_ci/l_v) )`

`f3 = (1/sin(theta_k_rho)) * ( (Delta_l_v/l_k)*cos(theta_v_rho) + (Delta_l_k/l_k)*cos(theta_k_rho) + (Delta_l_rho/l_k) - (Delta_l_R/l_k)*cos(theta_p_rho) + (l_R/l_k)*Delta_theta_p*sin(theta_p_rho) )`

`f4_i = (1/sin(theta_Hi_ai)) * ( (Delta_l_Hi/l_Hi)*cos(theta_Hi_ai) + (Delta_l_ai/l_Hi) - (Delta_l_v/l_Hi)*cos(theta_v_ai) - (Delta_l_ci/l_Hi)*cos(theta_ci_ai) )`

Interpretazione fisica (MMT):
- `f1`, `f3`: contributi RTE dei sottosistemi di trasmissione involute/cicloidale.
- `f2_i`, `f4_i`: contributi RTE associati ai crankshaft nei loop ingresso/uscita.

## 3) Implementazione torch e Autograd

### 3.1 Vincolo critico
Nessuna operazione fuori grafo:
- vietati `numpy`, `.item()`, `.detach()`, cast Python durante il forward loss;
- solo `torch.add`, `torch.mul`, `torch.div`, `torch.sin`, `torch.cos`, `torch.sum`, `torch.mean`, `torch.clamp`, `torch.where`, ecc.

### 3.2 Stabilita numerica (denominatori)
Per i termini `1/sin(...)` e le divisioni geometriche:

- usare `eps > 0` configurabile (es. `1e-8`);
- definire helper differenziabile:
  - `safe_div(num, den) = num / clamp_abs(den, eps)`;
  - `clamp_abs(den, eps) = sign(den) * max(abs(den), eps)` (implementazione torch).

Questo evita `NaN/Inf` senza interrompere il backprop.

### 3.3 Shape e batching previsti
- scalari per campione: shape `[B]`
- termini indicizzati da `i`: shape `[B, 3]` (`f2_i`, `f4_i` e rispettivi input)
- somme sui crankshaft:
  - `sum_f2 = torch.sum(f2_i, dim=-1)`
  - `sum_f4 = torch.sum(f4_i, dim=-1)`

## 4) Integrazione della consistenza armonica `L_harm`

Set imposto:
`H = {0,1,3,39,40,78,81,156,162,240}`

Ricostruzione armonica per campione:

`TE_harm(theta) = A_0 + sum_{k in H, k>0} A_k * cos(k*theta + phi_k)`

con `A_k`, `phi_k` dal batch (`A_target_k`, `phi_target_k`) gia prodotti dal data loader di Fase 1.

Definizione loss:

`L_harm = mean( (TE_pred_raw - TE_harm)^2 )`

Note operative:
- `theta` in radianti (`batch["theta"]`).
- Se `TE_pred` e in scala standardizzata, prima inversione con `te_mean`, `te_std` del train set:
  - `TE_pred_raw = TE_pred*te_std + te_mean`.

## 5) Struttura prevista della classe `TransmissionErrorLoss`

### 5.1 Responsabilita
La classe combina:

- vincolo fisico Eq. (29)/(30): `L_eq`
- consistenza armonica: `L_harm`
- eventuali regolarizzazioni numeriche opzionali (fase successiva): `L_reg`

Loss totale:
`L_total = w_eq*L_eq + w_harm*L_harm + w_reg*L_reg`

### 5.2 API proposta
```python
class TransmissionErrorLoss(nn.Module):
    def __init__(
        self,
        mode: str = "eq30",            # "eq29" oppure "eq30"
        harmonic_orders: tuple[int, ...] = (0, 1, 3, 39, 40, 78, 81, 156, 162, 240),
        w_eq: float = 1.0,
        w_harm: float = 0.2,
        w_reg: float = 0.0,
        eps: float = 1e-8,
        te_mean: float = 0.0,
        te_std: float = 1.0,
    ): ...

    def forward(
        self,
        te_pred: torch.Tensor,         # [B] o [B,1]
        batch: dict,                   # theta + target armonici
        physics_inputs: dict,          # Delta_l_*, Delta_theta_*, theta_*, l_*, z_*
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]: ...
```

### 5.3 Metodi interni previsti
- `_safe_div(num, den)`
- `_compute_f_terms(physics_inputs) -> (f1, f2_i, f3, f4_i)`
- `_compute_delta_theta_h_eq29(f_terms, physics_inputs)`
- `_compute_delta_theta_h_eq30(f_terms, physics_inputs)`
- `_compute_te_harm(theta, batch)`
- `_to_raw_scale(te_pred)`

Output `forward`:
- `loss_tot` (tensor scalare)
- `metrics` dict (`L_eq`, `L_harm`, `L_reg`, `Delta_theta_H_mean`, ecc.) per logging.

## 6) Modifiche previste a moduli/interfacce

1. Nuovo modulo: `physics_loss.py`
2. Interfaccia training (fase successiva): passaggio di `physics_inputs` al criterio.
3. Allineamento con data loader:
   - uso diretto di `theta`, `A_target_k`, `phi_target_k`.
4. Configurazione:
   - scelta `mode` (`eq29`/`eq30`)
   - pesi `w_eq`, `w_harm`, `w_reg`
   - `eps`, `te_mean`, `te_std`.

## 7) Piano di validazione (test numerici/benchmark/metriche)

### 7.1 Unit test algebraici
- confronto tra formula manuale e output torch per Eq. (31)-(34).
- confronto Eq. (29) vs Eq. (30) in caso compatibile (`z5-z4=1`, mappatura coerente).

### 7.2 Test di differenziabilita
- `torch.autograd.gradcheck` su `f1..f4` e su `Delta_theta_H`.
- verifica assenza `NaN/Inf` in forward/backward su batch random fisicamente plausibili.

### 7.3 Smoke test in `pinns_env`
- un batch reale dal data loader Fase 1.
- calcolo `L_total`, `backward()`, controllo gradienti finiti.

### 7.4 Metriche di validazione
- `MSE(TE_pred_raw, Delta_theta_H)` = `L_eq`
- `MSE(TE_pred_raw, TE_harm)` = `L_harm`
- trend per condizione (`condition_id`) e per direzione (`dir_flag`).

## 8) Rischi tecnici e fallback

1. Singolarita numeriche (`sin(theta) ~ 0`):
   - fallback: `safe_div` con `eps`, clipping controllato.
2. Incoerenza unita di misura (TE standardizzato vs fisico):
   - fallback: loss solo in scala raw con inversione esplicita.
3. Mancanza di alcuni input fisici (`Delta_l_*`, angoli):
   - fallback A: modalita ridotta (solo termini disponibili, log warning).
   - fallback B: disattivare temporaneamente `L_eq` e usare solo `L_harm` (debug mode).
4. Sensibilita ai pesi di loss:
   - fallback: warm-up (`w_eq` crescente per epoche) e tuning separato per direzione FW/BW.

## 9) Trade-off principali
- Maggiore `w_eq`: piu coerenza fisica, ma rischio underfit su rumore sperimentale.
- Maggiore `w_harm`: migliore fedelta spettrale, ma possibile perdita di dettaglio locale nel dominio angolare.
- `eps` alto: piu stabilita numerica, ma maggiore bias sui casi vicini a singolarita.

---

Documento pronto per revisione utente.
Come richiesto da `AGENTS.md`, l'implementazione in codice di `physics_loss.py` parte solo dopo conferma esplicita.
