# PROJECT MASTER

## Stato del Progetto

- Architettura tecnica iniziale definita a livello documentale (PINN + decomposizione armonica + training in due stadi).
- Analisi fisica completata sui riferimenti caricati in `/reference`, con focus su Eq. (29)-(30) del paper MMT.
- Pipeline dati definita a livello di piano, inclusa logica `DataValid` e normalizzazione delle variabili operative.
- Implementazione Python non ancora avviata (in attesa/procedura conforme ad `AGENTS.md`).

## Specifiche Tecniche PINN

### Riferimento fisico (MMT, Eq. 29)

Forma generale del contributo RTE:

`Delta_H = [g2*g3*g4 / (1 + g1*g2*g3*g4)]*f1 + [g3*g4 / (1 + g1*g2*g3*g4)]*(1/3)*sum_i(f2_i) + [g4 / (1 + g1*g2*g3*g4)]*f3 + [1 / (1 + g1*g2*g3*g4)]*(1/3)*sum_i(f4_i)`

dove `g1..g4` sono coefficienti di trasferimento errore dei sottosistemi cinematici e `f1,f2_i,f3,f4_i` sono i contributi elementari.

### Riferimento fisico (MMT, Eq. 30 - RV one-tooth-difference)

Con `z5 - z4 = 1`, la forma semplificata usata nel progetto:

`Delta_H = [-(1/z4)*f1 - (1/(3*z4))*sum_i(f2_i) + f3 + (1/3)*sum_i(f4_i)] / [1 + (z1 + z2)/(z2*z4)]`

Nota: la notazione verra mantenuta coerente con le definizioni implementative di `f1..f4` secondo Eq. (31)-(34) del paper MMT.

### Armoniche prioritarie

Set armoniche primarie da usare in training/validazione:

`H = {0, 1, 3, 39, 40, 78, 81, 156, 162, 240}`

Forma armonica operativa:

`TE(theta) = A0 + sum_{k in H+}(A_k * cos(k*theta + phi_k))`

con stima/predizione di `A_k` e `phi_k` condizionata da velocita, coppia, temperatura e direzione.

## Regole Operative

- Regola critica: prima di implementare una nuova funzionalita, creare prima un documento tecnico in `/doc` e attendere conferma esplicita utente (come da `AGENTS.md`).
- Nessuna implementazione codice per nuove feature senza conferma successiva alla consegna documentale.
- Nei log tecnici futuri citare sempre i file sorgente con formato:
  - `?F:<file_path>?L<linea>?`
- Mantenere esplicito il legame tra scelte implementative e vincoli fisici (accuratezza, stabilita, costo computazionale).

## Stack Tecnologico

- Framework: PyTorch + PyTorch Lightning
- Ottimizzazione: AdamW (fase esplorativa) + L-BFGS (fase rifinitura PINN)
- Target: pipeline riproducibile con configurazioni versionabili

## Obiettivo Immediato

Implementare `data_loader.py` con:

- uso esplicito di `DataValid` per isolamento del giro utile `0 deg -> 360 deg`;
- gestione forward/backward coerente;
- parsing metadati condizione (`rpm`, `Nm`, `degC`);
- normalizzazione feature operative in linea con il Report Machine Learning.

## Fonti Interne da Mantenere Allineate

- `doc/2026_03_06_analisi_fisica_pinn.md`
- `doc/2026_03_06_architettura_modello.md`
- `doc/2026_03_06_pipeline_dati.md`
- `reference/MMT_TEModeling.pdf`
- `reference/RCIM_ML-compensation.pdf`
- `reference/SpiegazioneSerieDati.pdf`
- `reference/Report Machine Learning.pdf`

