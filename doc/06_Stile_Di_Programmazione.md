# Stile Di Programmazione Del Progetto

## Fonti Di Riferimento

- `reference/codes/blind_handover_controller-master.zip`
- `reference/codes/mediapipe_gesture_recognition-master.zip`
- `reference/codes/multimodal_fusion-master.zip`

La base principale dello stile e' `blind_handover_controller`, mentre gli altri due repository confermano gli stessi pattern di naming, commenti, struttura e tono implementativo.

## Naming

### Variabili

- Preferire nomi espliciti e di dominio.
- Esempi rappresentativi:
  - `trajectory_execution_received`
  - `train_dataloader`
  - `human_radius`
  - `admittance_weight`
  - `joint_states`
  - `process_dataset`

### Costanti

- Usare uppercase completo per costanti e flag di modulo.
- Esempi:
  - `PACKAGE_PATH`
  - `DEVICE`
  - `MODEL_TYPE`
  - `GRIPPER_OPEN`
  - `DYNAMIC_PLANNER`

### Classi

- Usare prevalentemente `PascalCase`.
- Mantenere naming robotico misto quando e' semanticamente utile.
- Esempi:
  - `TrainingNetwork`
  - `AdmittanceController`
  - `UR_RTDE_Move`
  - `UR_Toolbox`
  - `Handover_Controller`

### Funzioni E Metodi

- Usare `snake_case` per funzioni e utility generali.
- Per callback ROS o funzioni gia' allineate ai nodi, mantenere la convenzione mista presente nei repository di riferimento.
- Esempi:
  - `train_network`
  - `get_model_name`
  - `save_hyperparameters`
  - `jointStatesCallback`
  - `FTSensorCallback`

## Commenti

### Stile Dei Commenti

- Frequenti, brevi, operativi.
- Scritti in Title Case.
- Usati per scandire il flusso piu' che per spiegare ovvieta'.

### Pattern Preferiti

- `# Import ROS Messages`
- `# Initialize Admittance Controller`
- `# Compute Cartesian Velocity`
- `# Save Model`
- `# Move to Home | Error -> Return`

### Regole Pratiche

- Capitalizzare sempre le parole principali.
- Usare commenti prima di blocchi logici distinti.
- E' accettabile usare `->`, parentesi o sigle tecniche se aumentano chiarezza.

## Docstring

- Corte, una riga, in Title Case.
- Tipicamente descrivono classe o funzione senza prolissita'.

Esempi di forma corretta:

- `""" Handover Controller Class """`
- `""" Compute Loss """`
- `""" Cartesian Goal Callback """`

## Struttura Del Codice

- Preferire codice esplicito e progressivo.
- Spezzare il ragionamento in blocchi intermedi ben nominati.
- Evitare astrazioni troppo compatte quando rendono meno leggibile il flusso.
- Mantenere gruppi logici separati da commenti.

## Import

- Organizzare gli import per blocchi.
- Inserire commenti sintetici sopra gli import di gruppi importanti.

Pattern tipico:

```python
from termcolor import colored

# Import PyTorch Lightning Functions
from pytorch_lightning.callbacks import EarlyStopping

# Import Processed Dataset and DataLoader
from process_dataset import ProcessDataset
```

## Controlli E Validazioni

- Usare assert espliciti con messaggi dettagliati.
- Rendere visibili le assunzioni di tipo e forma dei dati.

Esempio di tono corretto:

```python
assert len(joint_positions) == 6, f"Joint Positions Length must be 6 | {len(joint_positions)} given"
```

## Type Hint

- Usare type hint quando servono davvero a chiarire tensori, array, messaggi ROS, tuple di ritorno e dataloader.
- Non serve forzarli ovunque, ma sono parte del tono tecnico del codice di riferimento.

## Logging E Debug

- Messaggi diretti, concreti, spesso con `print` o logger ROS.
- Se utile, usare output colorizzato per training, debug o stato del controller.
- Evitare testo generico o troppo narrativo.

## Regole Da Applicare In Questo Repository

- Ogni nuovo file deve usare naming esplicito e leggibile.
- Ogni funzione non banale deve essere spezzata in blocchi con commenti Title Case.
- I config e le costanti devono restare semanticamente trasparenti.
- Il codice di ML deve rimanere compatibile con una lettura ingegneristica e con una futura esportazione/deploy.
- In caso di dubbio, privilegiare il pattern osservato in `blind_handover_controller`.
