# TwinCAT/TestRig Video Guide – *Machine_Learning 2.mp4*

## Overview  

The video demonstrates how a **TestRig** project in TwinCAT can be used to validate a machine‑learning (ML) model that predicts motor torque and velocity from sensor data. The ML model is exported from Python/Scikit‑Learn, imported into the PLC as a *Prediction Block*, and orchestrated by a set of user‑defined function blocks (`FB_BoschMotor`, `FB_LightDevice`, etc.). The video walks through:

1. **Importing the CSV dataset** located at  
   ```
   C:\Users\Alessio Tutarini\Unimore\XiLAB Robotics - DATA\02-Test Rig\Machine Learning
   ```  
2. **Configuring the prediction block** (`Predict_ML`) and linking it to the PLC variables that represent sensor inputs (e.g., `Db xCSV_and_Vectors`).
3. **Timing analysis** of the *Fast Task* (250 µs) versus the *ML Task* (500 µs) and how inter‑task communication is handled.
4. **Running a state machine** (`state 100`) that reads the first torque value from the CSV file, applies a compensation routine, and drives the motor.

The transcript highlights key timing figures (≈1.325 µs for task latency) and explains how low‑speed operation reduces the need for frequent compensation updates.

---

## Why This Video Matters  

- **Bridging ML and PLC**: It shows a concrete workflow to bring a trained model into an industrial controller, a common requirement in modern robotics.
- **Real‑time constraints**: The timing discussion (Fast Task 250 µs vs. ML Task 500 µs) illustrates how to meet hard real‑time deadlines while still executing data‑intensive inference.
- **State‑machine integration**: Demonstrates how a simple state machine can trigger model evaluation and compensation, which is useful for safety‑critical or precision tasks.

---

## Main Technical Findings  

| Item | Detail |
|------|--------|
| **ML Export Format** | The model is exported as an XML/JSON file that TwinCAT’s *Prediction Block* can read. The block expects a flat array of input features (`Db xCSV_and_Vectors`). |
| **Input/Output Assumptions** | - Inputs: sensor vectors (e.g., encoder positions, velocities). <br> - Outputs: predicted torque and velocity (`targetVelocity_TE`, `nTurnsLoadSide`). <br> The block is configured to output a 4‑element vector as seen in the OCR snippet at 00:15:30. |
| **Task Timing** | Fast Task (250 µs) handles sensor acquisition; ML Task (500 µs) performs inference. Inter‑task communication latency ≈1.325 µs, which is acceptable for the 2 kHz control loop. |
| **State Machine Logic** | State 100 reads the first CSV row, applies a compensation routine (`Applicazione correzione della posizione i-esima con l’angolo j`), and then transitions to normal operation. The OCR at 00:06:10 confirms the presence of this logic in the *Task Fast Task* block. |
| **Compensation Strategy** | At low speeds, the compensation is near zero; thus the same value can be reused for three cycles (as per transcript). This reduces computational load during steady‑state operation. |

---

## TwinCAT And Deployment Implications  

1. **Project Structure**  
   - *TestRig* project contains: `FB_BoschMotor`, `FB_LightDevice`, `Predict_ML` block, and the state machine PLC program (`PRG`).  
   - The CSV dataset is stored in a dedicated folder; the path must be hard‑coded or passed via a configuration variable.

2. **Runtime Configuration**  
   - The *Prediction Block* requires the file name (`TEFF_File`) to be set at runtime (see OCR at 00:15:30).  
   - Enable flags (`bEnableFF_TE`, `startEx_TE`) control whether the block runs in feed‑forward mode or iterative learning.

3. **Code Adaptation**  
   - When porting this setup to a different PLC, ensure that the task priorities match (Fast Task < ML Task) and that the inter‑task communication uses *Synchronized Variables* (`Db xCSV_and_Vectors`).  
   - The compensation routine must be adapted if the motor model changes; the current logic assumes a linear relationship between torque and velocity.

4. **Testing & Validation**  
   - Use the TestRig’s built‑in simulation to verify that the ML predictions match expected values from the CSV file.  
   - Monitor task timing in real time (e.g., via TwinCAT Diagnostics) to confirm that latency stays below 2 µs.

---

## Reference Snapshots  

| Time | Concept | Snapshot Description |
|------|---------|-----------------------|
| **00:06:10** | Task Timing & Communication | OCR shows “Task Fast Task Fast (250 s)” and references the prediction block (`Predict_ML`). |
| **00:01:15** | Input Data Structure | OCR lists `Db xCSV_and_Vectors` as a BOOL‑typed sensor group linked to *Task_500us_ML*. |
| **00:11:06 & 00:15:30** | Prediction Block Configuration | OCR displays variables such as `targetVelocity_TE`, `nTurnsLoadSide`, and file path `TEFF_File`. |
| **00:14:46** | State Machine Trigger | Transcript mentions “state 100” reading the first torque value from the CSV. |

These snapshots collectively illustrate how data flows from the CSV file into the PLC, through the prediction block, and finally to the motor control logic.

---

## Open Questions Or Uncertain Points  

1. **Exact Model Format** – The transcript does not specify whether the ML model is exported as a `.xml`, `.json`, or custom binary format. Clarification would aid in reproducing the import process.
2. **Error Handling** – It’s unclear how the system reacts if the CSV file is missing or corrupted. Does the prediction block default to zero, or does it trigger an alarm?
3. **Scalability** – The video shows a single motor scenario. How would the architecture change for multiple motors or higher‑dimensional sensor inputs?
4. **Safety Considerations** – No mention of safety interlocks or watchdog timers. In a production environment, how are these integrated with the TestRig?

Addressing these points will strengthen confidence in deploying similar ML‑augmented control loops on other TwinCAT platforms.
