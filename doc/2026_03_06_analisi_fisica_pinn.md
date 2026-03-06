# 20260306 Analisi Fisica PINN

## Obiettivo
Tradurre le Eq. (29)-(30) di MMT in una `physics_loss` differenziabile, integrata con la rappresentazione armonica del TE.

## 1) Traduzione operativa di Eq. (29)-(30)

### Forma fisica di riferimento
Useremo Eq. (29) come forma generale con coefficienti di trasferimento errore `g1..g4`:

`Delta_H_phys = C1(g)*f1 + C2(g)*sum_i(f2_i) + C3(g)*f3 + C4(g)*sum_i(f4_i)`

Dove `C1..C4` sono i prefattori derivati da Eq. (29).

Per la configurazione RV one-tooth-difference useremo Eq. (30):

`Delta_H_phys = N(f1,f2_i,f3,f4_i,z1,z2,z4) / D(z1,z2,z4)`

con `N` e `D` implementati in modo coerente al paper.

### Collegamento alla rete
La rete produrra:
- `TE_hat(theta, v, tau, T, dir)` (predizione principale)
- opzionalmente campi ausiliari per errori elementari (es. `Delta_l_*`, `Delta_alpha_*`) necessari per costruire `f1,f2,f3,f4`.

In prima versione, i termini geometrici nominali (`z1,z2,z4`, rapporti) sono parametri noti da configurazione.

## 2) Definizione della physics_loss

`L_phys = w_eq * L_eq + w_loop * L_loop + w_harm * L_harm + w_smooth * L_smooth`

Componenti:

1. `L_eq` (consistenza Eq. 29/30)
- `L_eq = MSE(TE_hat - Delta_H_phys)`
- impone che la predizione segua la decomposizione fisica dei contributi `f1..f4`.

2. `L_loop` (vincoli dei loop cinematici)
- residui su Eq. (23)-(26) in forma differenziabile.
- riduce soluzioni numericamente corrette ma fisicamente non compatibili.

3. `L_harm` (consistenza armonica)
- `TE_harm(theta) = A0 + sum_{k in H+} A_k * cos(k*theta + phi_k)`
- `H = {0,1,3,39,40,78,81,156,162,240}` (estendibile da config)
- `L_harm = MSE(TE_hat - TE_harm)` + regularization su periodicita di `A_k,phi_k` vs condizioni operative.

4. `L_smooth` (stabilita fisico-numerica)
- penalita su derivate angolari per evitare forme non fisiche:
- `L_smooth = MSE(dTE_hat/dtheta, dTE_harm/dtheta) + beta*MSE(d2TE_hat/dtheta2, d2TE_harm/dtheta2)`.

## 3) Uso della differenziazione automatica per f1,f2,f3,f4

I termini `f1,f2,f3,f4` verranno implementati con sole operazioni `torch` (somma, prodotto, cos, sin, divisione), quindi autograd propaghera i gradienti verso i parametri della rete.

Passaggi previsti:

1. Definire `theta` con `requires_grad=True`.
2. Calcolare i termini elementari (`Delta_l_*`, `Delta_alpha_*`, angoli ausiliari) in modo differenziabile.
3. Comporre `f1,f2_i,f3,f4_i` secondo Eq. (31)-(34).
4. Calcolare `Delta_H_phys` tramite Eq. (29) o Eq. (30).
5. Ottenere derivate con `torch.autograd.grad(..., create_graph=True)`:
   - `dTE_hat/dtheta`, `d2TE_hat/dtheta2`
   - `df1/dtheta`, `df2_i/dtheta`, `df3/dtheta`, `df4_i/dtheta` (se attiviamo regularizer su smoothness dei singoli contributi)
6. Usare tali quantita in `L_smooth` e in eventuali vincoli addizionali (periodicita, simmetria fw/bw).

Nota: in Eq. (31)-(34) non compaiono derivate esplicite, ma autograd e necessario per l ottimizzazione end-to-end e per i vincoli su derivate dei contributi.

## 4) Integrazione di ampiezze A_k e fasi phi_k

Strategia prevista:

- Head armonica dedicata che predice `A_k` e `phi_k` condizionati da `(v,tau,T,dir)`.
- Ricostruzione `TE_harm(theta)` durante il training.
- Doppio accoppiamento:
  1) `TE_hat <-> TE_harm` tramite `L_harm`
  2) `TE_hat <-> Delta_H_phys` tramite `L_eq`

Questo crea un vincolo triangolare tra:
- modello PINN (uscita diretta),
- struttura meccanica (Eq. 29/30),
- descrizione spettrale (armoniche misurate).

## 5) Assunzioni, limiti, trade-off

Assunzioni:
- parametri geometrici nominali disponibili e stabili per il riduttore testato;
- armoniche principali ben descritte da `H` scelto.

Limiti:
- identificabilita parziale dei contributi `f1..f4` senza misure geometriche dirette;
- possibile confondimento tra contributi fisici e artefatti di misura ad alcune velocita.

Trade-off:
- aumentare `w_eq` migliora coerenza fisica ma puo ridurre fit locale sui dati rumorosi;
- aumentare cardinalita di `H` migliora accuratezza spettrale ma aumenta costo computazionale e rischio overfit.
