# Report Machine Learning - Sintesi Di Progetto

## Fonte

- PDF di riferimento: `reference/Report Machine Learning.pdf`

## Obiettivo Del Documento

Il report descrive il lavoro pratico svolto sul test rig, la costruzione del dataset, la scelta delle frequenze significative del TE, l'importazione dei modelli in TwinCAT e le criticita' incontrate durante l'implementazione.

## Contenuti Principali

- Raccolta automatizzata del dataset sperimentale.
- Definizione delle fasi dell'esperimento su PLC.
- Uso della variabile `DataValid` per isolare il tratto utile al calcolo del TE.
- Analisi delle frequenze adimensionali piu' rilevanti.
- Importazione dei modelli in TwinCAT tramite blocchi funzionali dedicati.
- Test pratici di riproduzione e compensazione.

## Workflow Sperimentale Ricostruito

- Impostazione parametri di velocita', coppia e temperatura.
- Monitoraggio dei limiti e delle condizioni di sicurezza.
- Warm-up fino alla temperatura richiesta.
- Homing e zeroing degli encoder.
- Esecuzione del test forward e backward.
- Registrazione dei dati con segmentazione tramite `DataValid`.

## TwinCAT E Blocchi Funzionali

- `FB_Predict` viene usato per interrogare il modello ML.
- `ML_Transmission_Error` usa la predizione del modello per ricostruire e applicare la compensazione.
- L'importazione modelli in TwinCAT richiede attenzione al formato, ai file XML e ai limiti del runtime.

## Indicazioni Tecniche Importanti

- La procedura sperimentale e' organizzata come macchina a stati.
- La temperatura puo' essere trattata come valore iniziale costante oppure come segnale aggiornato, ma la scelta deve essere esplicita.
- Le frequenze usate per la compensazione nascono da analisi sperimentale, non da selezione arbitraria.
- La robustezza lato PLC richiede gestione di NaN, limiti di tempo ciclo e strutture semplici.

## Implicazioni Per Questo Repository

- La pipeline dati deve essere coerente con l'esperimento reale, non solo con file CSV statici.
- I config futuri dovrebbero permettere di tracciare:
  - condizioni operative;
  - frequenze selezionate;
  - strategia di uso della temperatura;
  - modalita' di compensazione.
- Il progetto dovrebbe mantenere una netta separazione tra:
  - raccolta dati;
  - analisi armonica;
  - training del modello;
  - esportazione e deploy.

## Requisiti Software Derivati

- Esporre in modo chiaro il legame tra input sperimentali e input modello.
- Rendere ripetibili le fasi principali della pipeline.
- Progettare l'output del modello in una forma immediatamente utilizzabile per ricostruzione del TE e compensazione.
