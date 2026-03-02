# Physics-Informed Neural Networks for Rotational Transmission Error Compensation in RV Reducers

## Overview

This project implements a **Physics-Informed Neural Network (PINN)** for modeling and compensating the **Rotational Transmission Error (RTE)** in RV reducers used in industrial robotics.

The objective is to combine:

* Analytical kinematic error models of RV reducers
* Experimental datasets from a dedicated Test Rig
* Deep learning (PyTorch / PyTorch Lightning)
* Real-time deployment in **TwinCAT 3 PLC environments**

The project follows the software architecture and coding style of previous PyTorch-based repositories (notably `blind_handover_controller`) and is structured for industrial-grade reproducibility and deployment.

---

## Scientific Motivation

Rotational Transmission Error (RTE) is a key performance indicator in precision gear systems and directly affects robot joint positioning accuracy.

Traditional approaches include:

1. Purely analytical multi-loop kinematic error models
2. Data-driven machine learning compensation models

This project introduces a **Physics-Informed approach**, where:

* The neural network is trained on experimental RTE data
* Physical constraints derived from the RV reducer kinematics are embedded directly into the loss function

The PINN enforces consistency with:

* Gear ratio constraints
* Multi-loop kinematic relations
* Error transfer coefficients
* Structural coupling between high-speed and low-speed stages

This ensures improved generalization, physical interpretability, and robustness under varying operating conditions.

---

## Project Objectives

* Implement a PINN-based RTE predictor
* Compare against:

  * Analytical equivalent multi-loop model
  * Classical ML compensation approaches
* Validate on experimental datasets
* Deploy the trained model on TwinCAT 3 for real-time compensation

---

## Repository Structure

The repository follows a modular PyTorch Lightning architecture.

```
.
├── configs/                # YAML configuration files
├── data/                   # Dataset loaders and preprocessing
│   ├── datasets/
│   ├── transforms/
│   └── datamodules/
├── models/                 # Neural network architectures
│   ├── pinn_model.py
│   ├── ml_baseline.py
│   └── blocks/
├── losses/                 # Physics-informed loss functions
│   ├── data_loss.py
│   ├── physics_loss.py
│   └── composite_loss.py
├── training/               # Lightning training scripts
│   ├── train.py
│   ├── evaluate.py
│   └── callbacks/
├── inference/              # Export and runtime inference utilities
│   ├── export_onnx.py
│   ├── export_st.py
│   └── runtime_validation.py
├── twincat/                # Structured Text implementation templates
├── utils/                  # Logging, metrics, normalization
└── README.md
```

All comments in source files follow the internal style convention:

> Concise imperative descriptions with capitalized key words.

Example:

```
# Ensure Inputs are Properly Normalized Before Forward Pass
```

---

## Dataset

The training and validation datasets are derived from a dedicated RV reducer Test Rig.

Data includes:

* Input shaft angle
* Output shaft angle
* Measured RTE
* Torque
* Temperature
* Operational conditions

Two dataset categories are used:

1. Transmission Error Dataset (preprocessed and validated)
2. Complete Raw Dataset (full experimental recordings)

Preprocessing steps:

* Synchronization of encoder signals
* Noise filtering
* Outlier rejection
* Feature normalization
* Cycle segmentation

---

## PINN Formulation

The network predicts:

```
RTE_hat = f_theta(x)
```

where `x` includes angular position and optional operating conditions.

### Loss Function

The total loss is defined as:

```
L_total = L_data + lambda_phys * L_physics + lambda_reg * L_reg
```

Where:

* `L_data`: Mean Squared Error between measured and predicted RTE
* `L_physics`: Constraint residuals derived from analytical RTE equations
* `L_reg`: Weight regularization term

### Physics Constraints Include

* Multi-loop kinematic closure relations
* Speed ratio consistency
* Error transfer coefficient relations
* Stage coupling constraints

This ensures that the learned function respects the mechanical structure of the RV reducer.

---

## Model Architecture

Default architecture:

* Fully Connected Network
* 3–6 Hidden Layers
* 64–256 Neurons per layer
* Tanh or SiLU activation
* Optional residual connections

The architecture is selected to ensure:

* Smooth function approximation
* Stable real-time execution
* Straightforward translation to PLC Structured Text

---

## Training

Training is performed using PyTorch Lightning.

### Features

* Automatic check-pointing
* TensorBoard logging
* Early stopping
* Learning rate scheduling
* Reproducible seeds

### Example Command

```
python training/train.py --config configs/pinn_default.yaml
```

---

## Evaluation Metrics

* Peak-to-peak RTE error
* RMS error
* Frequency-domain consistency
* Generalization across operating conditions
* Comparison with analytical model

---

## TwinCAT 3 Deployment

The trained model can be exported in two ways:

### 1. ONNX Export

* Used for C++ or runtime integration

### 2. Structured Text Export

* Automatic generation of fully connected forward pass
* Deterministic execution
* Fixed-point or floating-point compatible

TwinCAT integration features:

* Real-time execution inside PLC task
* Online RTE compensation
* Integration with encoder inputs
* Compatibility with ATI F/T sensor system

---

## Real-Time Considerations

* Deterministic inference time
* Limited network depth for PLC compatibility
* No dynamic memory allocation
* Precomputed normalization constants

---

## Validation Strategy

1. Offline validation against test bench measurements
2. Frequency-domain comparison
3. Stress testing under varying torque and temperature
4. Online compensation validation in PLC

---

## Research Contribution

* Hybrid analytical–data-driven modeling approach
* Industrial PLC deployment of PINNs
* Comparative analysis with classical RTE models
* Practical application in high-precision robotics

---

## Requirements

* Python 3.10+
* PyTorch
* PyTorch Lightning
* NumPy
* SciPy
* TwinCAT 3 (for deployment phase)

---

## Future Work

* Extension to dynamic torque-dependent RTE
* Adaptive online learning
* Integration with digital twin models
* Multi-axis robot joint compensation

---

## Author

Davide Ferrari

---

## License

Specify appropriate license (e.g., MIT, BSD-3, or proprietary industrial use).
