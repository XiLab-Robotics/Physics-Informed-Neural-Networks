# Guida Operativa Dataset

## Fonte

- PDF di riferimento: `reference/Guida.pdf`

## Scopo Del Documento

Questo documento raccoglie le indicazioni operative emerse dalla guida rapida del progetto. Non introduce nuova teoria sul Transmission Error, ma definisce dove reperire i dati e quali materiali pratici devono essere considerati come riferimento durante lo sviluppo.

## Punti Chiave

- Il dataset principale da usare per il progetto ML e TE e' il dataset di Transmission Error gia' estratto e validato.
- Esiste anche un dataset raw piu' completo, utile quando servono serie estese, temperature aggiuntive o controlli piu' fini sui segnali originali.
- La guida rimanda esplicitamente a materiale di supporto sul significato delle serie dati e a documentazione pratica su TwinCAT e Machine Learning.
- La sottocartella `reference/codes` va trattata come base di ispirazione per struttura software, deploy e stile implementativo.

## Implicazioni Per Il Repository

- Il flusso corretto parte da dati gia' filtrati e segmentati quando l'obiettivo e' il training del modello di compensazione.
- I dati raw vanno usati solo quando serve ricostruire preprocessing, validazione o analisi aggiuntive.
- La documentazione tecnica del progetto deve rimanere connessa a TwinCAT e ai codici di riferimento, non solo al modello ML offline.

## Decisioni Da Mantenere

- Privilegiare dataset gia' validati per training ed evaluation.
- Trattare i file raw come sorgente di audit, debugging e ricostruzione pipeline.
- Mantenere separati i documenti teorici dai documenti operativi.

## Uso Pratico

- Per il training: partire da serie dati gia' pulite.
- Per il deploy: mantenere sempre allineate le assunzioni sui dati con i vincoli TwinCAT.
- Per la documentazione: collegare sempre dataset, procedura sperimentale e codice di compensazione.
