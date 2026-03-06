# 20260306 Pipeline Dati

## Obiettivo
Pianificare `data_loader.py` per:
- isolare i tratti validi con `DataValid`;
- costruire campioni forward/backward coerenti su 0-360 gradi;
- normalizzare velocita, coppia e temperatura come da range del Report Machine Learning.

## 1) Formati supportati

### A) Dataset raw (acquisizione PLC)
Campi attesi (nomenclatura variabile):
- angolo encoder output (assoluto single-turn)
- segnali necessari al calcolo TE
- `DataValid` (0/1)
- eventuali segnali ausiliari

### B) Dataset gia preprocessato (4 colonne)
- `Position_Output_Reducer_Fw`
- `Transmission_Error_Fw`
- `Position_Output_Reducer_Bw`
- `Transmission_Error_Bw`

Nel formato B il filtro `DataValid` e gia implicitamente applicato.

## 2) Logica di estrazione con DataValid

Flusso proposto per formato raw:

1. Caricare file e uniformare nomi colonne (mapping robusto).
2. Isolare righe con `DataValid == 1`.
3. Segmentare forward/backward usando monotonia angolo o flag direzione.
4. Conservare solo tratto geometrico di un giro utile:
   - forward: angolo crescente nel dominio 0-360
   - backward: angolo decrescente nel dominio 360-0
5. Correggere eventuali salti di wrap-around con unwrapping controllato.
6. Scartare segmenti con campioni insufficienti o incoerenze.

Fallback se `DataValid` assente:
- usare maschera su intervallo angolare + controllo di coerenza dinamica.

## 3) Parsing metadata esperimento

Dal nome file (es. `1000.0rpm1000.0Nm25.0deg.csv`) estrarre:
- `v_rpm`
- `tau_Nm`
- `temp_degC`

Questi valori diventano feature statiche del campione.

## 4) Normalizzazione segnali

Range da Report Machine Learning:
- velocita: `v in [100,1800] rpm` (notare eventuale assenza di 1200 in alcune campagne)
- coppia: `tau in [0,1800] Nm`
- temperatura: `T in [25,35] degC`

Scelta consigliata (feature): min-max su `[-1,1]`
- `v_norm = 2*(v-100)/1700 - 1`
- `tau_norm = 2*(tau-0)/1800 - 1`
- `T_norm = 2*(T-25)/10 - 1`

Angolo:
- `theta_deg -> theta_rad`
- usare anche `sin(theta)`, `cos(theta)` per periodicita.

Target TE:
- default: standardizzazione z-score sui soli dati train
- salvare `mean/std` per inferenza coerente.

## 5) Costruzione armoniche per training

Per ogni segnale TE (fw e bw):
1. resampling opzionale su griglia uniforme in `theta`;
2. stima `A_k,phi_k` su `H={0,1,3,39,40,78,81,156,162,240}`
   - via FFT o fit least-squares trigonometrico;
3. salvataggio target armonici per `L_harm`.

## 6) Output del data_loader

Ogni item dataset (dict):
- `theta`, `sin_theta`, `cos_theta`
- `v_norm`, `tau_norm`, `T_norm`, `dir_flag`
- `te_target`
- `A_target[k]`, `phi_target[k]` (opzionale)
- metadati (`file_id`, `split`, `condition_id`)

## 7) Split e validazione

Split consigliato:
- stratificato per griglia `(v,tau,T)` per evitare leakage tra condizioni molto simili.

Controlli qualita:
- assenza NaN/Inf
- copertura uniforme del giro
- verifica periodicita (coerenza vicino a 0/360)
- report campioni scartati con motivazione.

## 8) Rischi e fallback

Rischi:
- incoerenze naming colonne tra campagne diverse
- aliasing armonico se campionamento non uniforme
- outlier da risonanza sistema misura

Fallback:
- layer di mapping colonne configurabile
- resampling uniforme prima di FFT
- flag quality per escludere condizioni non affidabili.
