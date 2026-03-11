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

```graph
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

Additional working folders already used in the project lifecycle:

* `reference/` for PDFs, reports, and external code references, including Git submodules under `reference/codes/`
* `doc/` for internal synthesized project documents and coding style notes
* `agents/` for external agent and subagent repositories used as reusable workflow references

All comments in source files follow the internal style convention:

> Concise imperative descriptions with capitalized key words.

Example:

```text
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

The operational meaning of zeroing, cumulative positions, and `DataValid` windows is documented in `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`.

---

## Documentation

The project documentation derived from the reference material is stored in `doc/`.

Main entry point:

* `doc/README.md`

Available project documents:

Reference summaries:

* `doc/reference_summaries/01_Dataset_Operations_Guide.md`
* `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
* `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
* `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
* `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`
* `doc/reference_summaries/06_Programming_Style_Guide.md`

Reference code notes:

* `doc/reference_codes/README.md`
* `doc/reference_codes/blind_handover_controller_reference.md`
* `doc/reference_codes/mediapipe_gesture_recognition_reference.md`
* `doc/reference_codes/multimodal_fusion_reference.md`

Technical documents:

* `doc/technical/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
* `doc/technical/2026-03-10-02-49-17_dataset_processing_pipeline.md`
* `doc/technical/2026-03-10-03-04-57_script_config_documentation_structure.md`
* `doc/technical/2026-03-10-03-16-44_doc_folder_reorganization.md`
* `doc/technical/2026-03-10-03-21-23_script_document_naming_cleanup.md`
* `doc/technical/2026-03-10-03-23-28_script_docs_folder_mirroring.md`
* `doc/technical/2026-03-10-03-27-42_project_usage_guide.md`
* `doc/technical/2026-03-10-13-05-10_relative_config_paths.md`
* `doc/technical/2026-03-10-15-13-29_agent_submodule_reorganization.md`
* `doc/technical/2026-03-10-15-25-39_commit_workflow_rule_update.md`
* `doc/technical/2026-03-10-15-33-05_reference_code_submodule_migration.md`
* `doc/technical/2026-03-10-15-58-05_reference_code_style_reference_docs.md`
* `doc/technical/2026-03-10-16-05-50_feedforward_lightning_baseline.md`
* `doc/technical/2026-03-10-16-32-23_dataset_header_typo_clarification.md`
* `doc/technical/2026-03-10-16-41-20_project_usage_guide_update_rule.md`
* `doc/technical/2026-03-10-16-45-41_project_usage_guide_refresh.md`
* `doc/technical/2026-03-10-16-55-13_dataloader_worker_tuning.md`
* `doc/technical/2026-03-10-18-11-49_training_entry_point_import_fix.md`
* `doc/technical/2026-03-10-18-35-11_training_terminal_output_cleanup.md`
* `doc/technical/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md`
* `doc/technical/2026-03-11-13-06-15_lightning_training_noise_followup.md`
* `doc/technical/2026-03-11-13-28-06_contextmanager_return_type_fix.md`

Script documentation:

* `doc/scripts/datasets/transmission_error_dataset.md`
* `doc/scripts/datasets/visualize_transmission_error.md`
* `doc/scripts/training/train_feedforward_network.md`

Guides:

* `doc/guide/project_usage_guide.md`

These documents summarize:

* Dataset provenance and operational usage
* Analytical TE modeling theory
* ML-based online compensation strategy
* Test-rig workflow and TwinCAT implementation details
* Coding style conventions derived from prior repositories

All future feature-level technical documents must also be stored in `doc/technical/` and linked from this main project document.

---

## Critical Project Rules

The following rules are mandatory for all future project work:

* Use English as the primary project language for file names, identifiers, instructions, comments, and technical documentation.
* Adopt the coding style of `blind_handover_controller` rigorously.
* Always take into account the documents in `reference/` or their summaries in `doc/` before making design or implementation decisions.
* Before implementing any feature, create a technical project document in `doc/technical/` using the filename format `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
* Each technical project document must contain the sections:
  * `Overview`
  * `Technical Approach`
  * `Involved Components`
  * `Implementation Steps`
* Every newly created technical project document must be added as a reference in this main project document.
* No implementation code should be written before the user has explicitly approved the technical document for that feature.
* Every user-requested repository change must follow this sequence:
  * create the technical project document first;
  * wait for explicit user approval;
  * execute the approved modifications;
  * if the approved work adds or changes user-facing functionality, update `doc/guide/project_usage_guide.md` in detail before the final commit;
  * if the approved work introduces a new third-party library, update `requirements.txt` and every relevant setup or usage reference before the final commit;
  * create a Git commit immediately after the modifications are completed.
* Before the final commit, `doc/guide/project_usage_guide.md` must be updated whenever the approved work adds or changes runnable functionality such as training scripts, model architectures, inference/export flows, dataset-processing capabilities, or usage/configuration workflows.
* Before the final commit, every newly introduced third-party library must be added to `requirements.txt` and to any relevant installation or usage documentation so the project remains reproducible.
* Every required Git commit must use a title aligned with the repository's existing commit style and a body that accurately summarizes all relevant modifications.

---

## Coding Style

The coding style of this repository is intentionally aligned with previous XiLAB robotics and ML repositories, especially `blind_handover_controller`.

The main conventions are:

* Explicit domain-oriented variable names
* Uppercase module-level constants
* Frequent title-case comments before logical code blocks
* Short one-line docstrings
* Clear staged implementations instead of overly compact abstractions

The full style guide is documented in:

* `doc/reference_summaries/06_Programming_Style_Guide.md`

---

## PINN Formulation

The network predicts:

```math
RTE_{hat} = f_{theta}(x)
```

where `x` includes angular position and optional operating conditions.

### Loss Function

The total loss is defined as:

```math
L_{total} = L_{data} + lambda_{phys} * L_{physics} + lambda_{reg} * L_{reg}
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

```bash
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

* Python 3.10
* NVIDIA GPU with compatible drivers for CUDA execution
* PyTorch with CUDA support
* PyTorch Lightning
* NumPy
* SciPy
* TwinCAT 3 (for deployment phase)

## Initial Setup

The current project bootstrap also includes:

* Conda environment: `standard_ml_codex_env`
* Global Codex MCP connection to Context7 for up-to-date library documentation
* Git submodules in `agents/` for reusable external agent collections

Current agent submodules:

* `agents/claude-code-agents` -> `https://github.com/vizra-ai/claude-code-agents.git`
* `agents/claude-code-subagents` -> `https://github.com/0xfurai/claude-code-subagents.git`
* `agents/awesome-claude-code-subagents` -> `https://github.com/VoltAgent/awesome-claude-code-subagents.git`
* `agents/wshobson-agents` -> `https://github.com/wshobson/agents.git`

These setup choices are intended to support reproducible development, documentation lookup, and future agent-assisted workflows.

### Environment Installation For A New User

Create and activate the Conda environment:

```powershell
conda create -y -n standard_ml_codex_env python=3.10
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
```

Install the project dependencies.

Note: this workstation reports local CUDA Toolkit `13.1`, and the official PyTorch wheel index exposes `cu130` wheels for Windows + Python 3.10. The repository now tracks `torch` directly in `requirements.txt`, but for the current GPU setup it is still better to install the CUDA-enabled PyTorch wheel explicitly from the official index first:

```powershell
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

Optional verification:

```powershell
python -c "import torch, lightning; print(torch.__version__); print(lightning.__version__); print(torch.cuda.is_available())"
```

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
