# Spiegazione Serie Dati - Sintesi Di Progetto

## Fonte

- PDF di riferimento: `reference/SpiegazioneSerieDati.pdf`

## Obiettivo Del Documento

Questo documento chiarisce come sono costruite le serie dati del test rig e quali passaggi operativi determinano la validita' dei campioni usati per il calcolo del Transmission Error.

## Struttura Del Sistema Di Misura

- Encoder assoluti Renishaw sul lato veloce e sul lato lento.
- Servomotore Bosch position-controlled lato input.
- Servomotore Bosch torque-controlled lato output.
- Torquemeter Manner.
- Sensori di temperatura.
- Riduttore in prova e riduttore secondario.

## Significato Dei Dati

- Sono presenti valori encoder raw assoluti.
- Sono presenti valori cumulativi multi-turn ottenuti dopo zeroing comune.
- Il calcolo del TE usa solo una finestra specifica di campioni validi, identificata da `DataValid`.

## Procedura Operativa Del Test

1. Warm-up fino alla temperatura target.
2. Homing alla posizione zero assoluta del riduttore.
3. Unloading del lato lento.
4. Zeroing software comune dei due encoder.
5. Avvio del motore lato input alla velocita' target.
6. Rampa di coppia sul lato lento fino al valore target.
7. Inizio acquisizione dati in condizioni stazionarie.
8. Attivazione di `DataValid` solo nell'intervallo angolare utile al calcolo del TE.

## Messaggi Chiave

- Lo zeroing comune non coincide necessariamente con lo zero assoluto di ciascun encoder.
- La finestra `DataValid` e' fondamentale per evitare di usare campioni non coerenti con la definizione del TE.
- La procedura viene ripetuta per i due versi di rotazione.

## Implicazioni Per Questo Repository

- I loader dati devono preservare o ricostruire il significato di `DataValid`.
- Le feature angolari vanno interpretate sapendo che raw, zeroed e cumulative non sono la stessa grandezza.
- Ogni preprocessing futuro deve evitare di mescolare segmenti validi e segmenti di transizione.

## Requisiti Per La Pipeline

- Tracciare sempre il tipo di posizione usata.
- Mantenere la possibilita' di filtrare la finestra valida.
- Rendere esplicite nel codice le differenze tra zero assoluto, zeroing software e posizione cumulativa.
