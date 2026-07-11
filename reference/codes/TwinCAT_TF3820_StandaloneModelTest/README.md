# TwinCAT TF3820 Standalone Model Test

This folder is generated from the StandardML TF3820 compatibility matrix. It is
intended for a blank Beckhoff PLC target with TwinCAT and TF3820 installed.

The harness is independent from the full TestRig project. It provides one
generated runner per prepared model and a top-level PLC program:

```text
P_TF3820StandaloneModelTest
```

Model artifacts are copied under:

```text
ML_models/<family_id>/
```

Before runtime testing, copy that folder to the target path expected by the PLC:

```text
C:\TwinCAT\3.1\Boot\ML\tf3820\standalone
```

Supported shape groups:

- `[1, 3]` -> `[1, 1]`: 1 model(s)
- `[1, 5]` -> `[1, 1]`: 6 model(s)
- `[1, 33, 4]` -> `[1, 1]`: 13 model(s)
- `[1, 33, 4]` -> `[1, 2]`: 1 model(s)
- `[1, 33, 4]` -> `[1, 3]`: 1 model(s)
- `[1, 33, 4]` -> `[1, 6]`: 1 model(s)
- `[1, 33, 4]` -> `[1, 9]`: 1 model(s)
- `[1, 33, 5]` -> `[1, 1]`: 13 model(s)

Runtime validation flow:

1. Open `TwinCAT_TF3820_StandaloneModelTest.sln`.
2. Resolve the `Tc3_MlServer` library.
3. Build the PLC project.
4. Copy `ML_models` to `C:\TwinCAT\3.1\Boot\ML\tf3820\standalone` on the target.
5. Start `TcMlServer`.
6. Select a value of `SelectedModel`.
7. Pulse `bLoadSelectedModel`.
8. Enable `bEnablePrediction`.
9. Watch `bPredictionReady`, `bError`, `nErrorCode`,
   `nMaxInferenceDuration`, and `aPredictionOutput`.

The synthetic input contract is common across models:

```text
theta, theta_dot, tau_load, T, direction_flag
```

Sequence models receive the same operating point repeated over 33 samples with
`fThetaStep` added to `theta` at each sequence index.
