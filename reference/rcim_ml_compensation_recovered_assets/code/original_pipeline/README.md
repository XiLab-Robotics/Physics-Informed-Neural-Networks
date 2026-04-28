# Original Pipeline README

This file preserves the executable usage note shipped by the original authors.
The operational note below is author-provided source material and is kept as
part of the recovered evidence surface.

Repository interpretation of this root:

- the actual shipped filename is `1.1-main_prediction_v17.py`, even though the
  author README text refers to `1-main_prediction_v17.py`;
- the root also contains `instances_V3/` pickle caches and precomputed
  `output_prediction/` and `evaluation/` artifacts;
- both shipped dataframe CSVs already contain only `deg = 25, 30, 35`, so the
  older `deg <= 35` filter is redundant for this specific release.

## Author README Text

- **Dist - Training modelli**

Questo folder contiene gli script usati per preparare i dataset, allenare i
modelli e generare le tabelle di valutazione usate nel paper.

Requisiti

- Python 3.8+ (si consiglia un virtual environment)
- Installare le dipendenze del progetto (se presente `requirements.txt`):

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

Script principali

- `0-main_createDFforPrediction.py`
    - Legge tutto il contenuto della cartella di input (`inputPath`). Se trova file `.pickle` li carica; altrimenti processa i `.csv` disponibili per costruire il dataframe di input per le predizioni.
- `1-main_prediction_v17.py`
    - Struttura usata per l'export dei modelli finali (allenati su tutto il dataset) destinati al test sul robot.
- `1-main_prediction_v18.py`
    - Struttura usata per il training dei modelli con i parametri già ottimizzati (come usato nelle sperimentazioni riportate nel paper).
    - Note:
        - Se si vuole ripetere l'ottimizzazione degli iperparametri per un nuovo dataset, usare la funzione `predictorMLCrossValidationWithHyperparameter` contenuta nella classe `MLModelMultipleOutput`. In tal caso partire dalla struttura di `1-main_prediction_v17.py` sostituire la funzione `predictorML_allForExport` con `predictorMLCrossValidationWithHyperparameter` per abilitare la ricerca degli iperparametri.
        - Per riprodurre i risultati del paper: eseguire il training con i parametri trovati su 80% del dataset e validare su 20% (flusso previsto in `1-main_prediction_v18.py`).
- `2-main_evaluatePrediction_v4.py`
    - Genera le tabelle di valutazione (MAE, RMSE, MAPE, MSE) utilizzate nel paper.

Consigli pratici

- Verificare i percorsi di input/output e i nomi dei file nel relativo script prima di eseguirlo.
- Se si modifica il dataset è buona pratica rieseguire l'ottimizzazione degli iperparametri.
