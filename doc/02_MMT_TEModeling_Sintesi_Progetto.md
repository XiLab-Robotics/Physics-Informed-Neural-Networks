# MMT TE Modeling - Sintesi Di Progetto

## Fonte

- PDF di riferimento: `reference/MMT_TEModeling.pdf`

## Obiettivo Del Lavoro

Il paper sviluppa un modello analitico del Rotational Transmission Error di un riduttore RV. L'idea centrale e' trasformare la struttura cinematica sovravincolata del riduttore in un meccanismo equivalente multi-loop, cosi' da ottenere equazioni esplicite che collegano gli errori originali dei componenti al Transmission Error complessivo.

## Concetti Teorici Principali

- Il Rotational Transmission Error e' l'indicatore principale di accuratezza del riduttore.
- La struttura RV viene ricondotta a un meccanismo equivalente cinematico ottenuto sostituendo coppie superiori con coppie inferiori.
- Il modello viene sviluppato con approccio loop incremental.
- Gli errori di fabbricazione e assemblaggio vengono rappresentati come errori equivalenti sulle lunghezze dei collegamenti del meccanismo.
- Il modello rende esplicito il contributo di sottosistemi high-speed e low-speed al TE finale.

## Errori Considerati

- Eccentricita' degli alberi a manovella.
- Errori geometrici del gear train involuto.
- Errori del profilo cicloidale.
- Errori di raggio pin e pitch circle.
- Errori di accumulo passo.
- Errori di assemblaggio del disco di uscita e di altre parti accoppiate.

## Risultati Utili Per Il Progetto

- Gli errori dello stadio a bassa velocita' hanno impatto particolarmente forte sul TE.
- Le componenti in frequenza del TE sono direttamente interpretabili rispetto alle sorgenti di errore.
- Il modello analitico puo' essere usato come base fisica per vincoli, feature engineering o loss physics-informed.

## Implicazioni Per Questo Repository

- Il progetto deve trattare il TE come funzione strutturata dalla cinematica del riduttore, non come semplice regressione black-box.
- Una futura loss physics-informed dovrebbe incorporare relazioni tra variabili cinematiche, stage coupling e coerenza di rapporto di trasmissione.
- Le frequenze caratteristiche del TE non devono essere considerate soltanto come feature empiriche, ma come manifestazioni di errori meccanici specifici.

## Traduzione In Requisiti Software

- Separare chiaramente componenti data-driven e componenti fisiche del modello.
- Mantenere espliciti i parametri meccanici rilevanti nei config.
- Favorire funzioni che conservino tracciabilita' tra sorgente d'errore, armoniche attese e output del modello.

## Direzione Consigliata

- Usare il modello analitico come riferimento per:
  - validazione dei risultati ML;
  - definizione di feature fisiche;
  - costruzione di loss composite o physics-informed;
  - interpretazione delle armoniche compensate.
