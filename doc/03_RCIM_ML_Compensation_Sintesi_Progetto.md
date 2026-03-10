# RCIM ML Compensation - Sintesi Di Progetto

## Fonte

- PDF di riferimento: `reference/RCIM_ML-compensation.pdf`

## Obiettivo Del Lavoro

Il paper propone una strategia di modellazione e compensazione online del Transmission Error nei servomeccanismi industriali usando Machine Learning, con successiva integrazione del modello in PLC Beckhoff TwinCAT per la compensazione in tempo reale.

## Variabili Operative Fondamentali

- Velocita' di ingresso.
- Coppia applicata.
- Temperatura dell'olio.

Queste tre variabili descrivono gran parte della dipendenza operativa del TE osservato sul test rig.

## Architettura Del Processo

- Raccolta dati su test rig dedicato.
- Addestramento di modelli ML per predire il TE o sue componenti rilevanti.
- Esportazione del modello in un formato utilizzabile lato PLC.
- Compensazione online durante profili di moto reali.

## Messaggi Chiave Del Paper

- I modelli ML sono adatti al problema perche' offrono predizione rapida.
- L'integrazione TwinCAT e' un requisito pratico centrale, non un dettaglio accessorio.
- La compensazione viene costruita in modo compatibile con task PLC a tempo ciclo limitato.
- I risultati sperimentali mostrano riduzioni del TE superiori all'80-90% in diversi scenari.

## Elementi Di Implementazione Rilevanti

- Il deploy industriale richiede modelli leggeri, interpretabili e con inferenza stabile.
- Le armoniche selezionate del TE sono una rappresentazione pratica molto utile lato PLC.
- Il sistema distingue task piu' veloci per la compensazione e task piu' lenti per la predizione ML.

## Implicazioni Per Questo Repository

- I modelli devono essere progettati con vincoli di esportazione e deploy, non solo per massimizzare accuracy offline.
- Ogni pipeline di training deve considerare come output finale una forma compatibile con TwinCAT o con una sua trascrizione strutturata.
- Le feature di ingresso devono rimanere allineate al test rig reale: velocita', coppia, temperatura e posizione angolare.

## Decisioni Progettuali Da Conservare

- Favorire architetture semplici e stabili.
- Rendere esplicite le grandezze fisiche usate come input e output.
- Tenere separati il modello di predizione e il modulo di compensazione.
- Prevedere fin da subito valutazioni su latenze, frequenze aggiornabili e requisiti di task PLC.

## Uso Nel Progetto Corrente

- Questo documento costituisce il riferimento principale per la parte ML-driven compensation.
- Ogni nuova implementazione deve poter essere valutata sia offline sia in ottica deploy TwinCAT.
