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
The repository currently keeps project-authored Python code under `scripts/`, external references under `reference/`, and reserves root `models/` for trained or exported model artifacts.

The conceptual architecture sketch below is legacy. For current repository navigation, treat `scripts/`, `reference/agents/`, and root `models/` as the authoritative structure.

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

* `reference/` for PDFs, reports, and external references, including Git submodules under `reference/codes/` and `reference/agents/`
* `doc/` for internal synthesized project documents and coding style notes
* `models/` for trained checkpoints and exported model artifacts

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

* `2026-03-10`
  * `doc/technical/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
  * `doc/technical/2026-03-10/2026-03-10-02-49-17_dataset_processing_pipeline.md`
  * `doc/technical/2026-03-10/2026-03-10-03-04-57_script_config_documentation_structure.md`
  * `doc/technical/2026-03-10/2026-03-10-03-16-44_doc_folder_reorganization.md`
  * `doc/technical/2026-03-10/2026-03-10-03-21-23_script_document_naming_cleanup.md`
  * `doc/technical/2026-03-10/2026-03-10-03-23-28_script_docs_folder_mirroring.md`
  * `doc/technical/2026-03-10/2026-03-10-03-27-42_project_usage_guide.md`
  * `doc/technical/2026-03-10/2026-03-10-13-05-10_relative_config_paths.md`
  * `doc/technical/2026-03-10/2026-03-10-15-13-29_agent_submodule_reorganization.md`
  * `doc/technical/2026-03-10/2026-03-10-15-25-39_commit_workflow_rule_update.md`
  * `doc/technical/2026-03-10/2026-03-10-15-33-05_reference_code_submodule_migration.md`
  * `doc/technical/2026-03-10/2026-03-10-15-58-05_reference_code_style_reference_docs.md`
  * `doc/technical/2026-03-10/2026-03-10-16-05-50_feedforward_lightning_baseline.md`
  * `doc/technical/2026-03-10/2026-03-10-16-32-23_dataset_header_typo_clarification.md`
  * `doc/technical/2026-03-10/2026-03-10-16-41-20_project_usage_guide_update_rule.md`
  * `doc/technical/2026-03-10/2026-03-10-16-45-41_project_usage_guide_refresh.md`
  * `doc/technical/2026-03-10/2026-03-10-16-55-13_dataloader_worker_tuning.md`
  * `doc/technical/2026-03-10/2026-03-10-18-11-49_training_entry_point_import_fix.md`
  * `doc/technical/2026-03-10/2026-03-10-18-35-11_training_terminal_output_cleanup.md`
  * `doc/technical/2026-03-10/2026-03-10-18-56-13_dependency_tracking_rule_and_requirements_audit.md`
* `2026-03-11`
  * `doc/technical/2026-03-11/2026-03-11-13-06-15_lightning_training_noise_followup.md`
  * `doc/technical/2026-03-11/2026-03-11-13-28-06_contextmanager_return_type_fix.md`
  * `doc/technical/2026-03-11/2026-03-11-13-36-18_function_definition_spacing_normalization.md`
  * `doc/technical/2026-03-11/2026-03-11-15-18-56_repository_wide_function_spacing_normalization.md`
  * `doc/technical/2026-03-11/2026-03-11-15-53-46_class_and_dataclass_spacing_normalization.md`
  * `doc/technical/2026-03-11/2026-03-11-15-57-47_manual_refactoring_style_propagation.md`
  * `doc/technical/2026-03-11/2026-03-11-16-00-33_programming_style_guide_update_for_spacing_and_manual_refactor_rules.md`
  * `doc/technical/2026-03-11/2026-03-11-16-53-35_programming_style_guide_alignment_with_latest_manual_refactor.md`
  * `doc/technical/2026-03-11/2026-03-11-16-59-54_feedforward_training_trial_and_testing_report.md`
* `2026-03-12`
  * `doc/technical/2026-03-12/2026-03-12-13-13-27_feedforward_trial_analytical_report.md`
  * `doc/technical/2026-03-12/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md`
  * `doc/technical/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md`
  * `doc/technical/2026-03-12/2026-03-12-15-27-38_mixed_density_batch_model_training_campaign.md`
  * `doc/technical/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md`
  * `doc/technical/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md`
  * `doc/technical/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md`
  * `doc/technical/2026-03-12/2026-03-12-16-03-09_report_pdf_visual_redesign.md`
  * `doc/technical/2026-03-12/2026-03-12-16-25-26_professional_blue_pdf_report_redesign.md`
  * `doc/technical/2026-03-12/2026-03-12-16-35-28_pdf_margin_and_table_layout_corrections.md`
  * `doc/technical/2026-03-12/2026-03-12-16-54-22_pdf_table_fit_and_post_export_validation.md`
  * `doc/technical/2026-03-12/2026-03-12-17-01-59_pdf_configuration_table_consistency_refinement.md`
  * `doc/technical/2026-03-12/2026-03-12-17-07-18_pdf_golden_standard_and_report_style_rules.md`
  * `doc/technical/2026-03-12/2026-03-12-17-11-25_report_exporter_style_alignment_and_rule_update.md`
  * `doc/technical/2026-03-12/2026-03-12-17-49-03_commit_requires_final_user_approval_rule.md`
  * `doc/technical/2026-03-12/2026-03-12-17-54-59_report_exporter_comment_cleanup_and_style_rule_alignment.md`
  * `doc/technical/2026-03-12/2026-03-12-18-06-27_batch_training_queue_and_config_reorganization.md`
  * `doc/technical/2026-03-12/2026-03-12-18-41-55_active_training_campaign_lock_and_auto_generation_workflow.md`
* `2026-03-13`
  * `doc/technical/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md`
  * `doc/technical/2026-03-13/2026-03-13-20-50-37_campaign_results_pdf_requirement.md`
  * `doc/technical/2026-03-13/2026-03-13-23-09-48_campaign_results_pdf_table_layout_repair.md`
* `2026-03-14`
  * `doc/technical/2026-03-14/2026-03-14-00-07-38_pdf_table_header_and_semantic_wrap_refinement.md`
  * `doc/technical/2026-03-14/2026-03-14-00-25-04_pdf_vertical_alignment_and_section_page_break_control.md`
  * `doc/technical/2026-03-14/2026-03-14-00-37-25_campaign_training_terminal_logging_alignment.md`
  * `doc/technical/2026-03-14/2026-03-14-00-56-05_best_training_logging_validation_campaign.md`
  * `doc/technical/2026-03-14/2026-03-14-02-07-47_best_training_logging_validation_campaign_results_report.md`
  * `doc/technical/2026-03-14/2026-03-14-02-19-57_campaign_runner_colorama_shutdown_fix.md`
  * `doc/technical/2026-03-14/2026-03-14-02-43-38_best_training_logging_validation_report_addendum.md`
  * `doc/technical/2026-03-14/2026-03-14-02-56-20_permanent_pdf_validation_tooling.md`
  * `doc/technical/2026-03-14/2026-03-14-03-07-08_pdf_tooling_style_and_cleanup_fixes.md`
  * `doc/technical/2026-03-14/2026-03-14-03-14-39_validate_report_pdf_style_refactor.md`
  * `doc/technical/2026-03-14/2026-03-14-03-18-45_validate_report_pdf_manual_style_rule_update.md`
  * `doc/technical/2026-03-14/2026-03-14-12-15-36_repository_code_layout_reorganization_and_agent_reference_migration.md`
  * `doc/technical/2026-03-14/2026-03-14-12-23-10_scripts_root_code_reorganization_and_reference_agents_move.md`
  * `doc/technical/2026-03-14/2026-03-14-12-46-27_gpu_training_path_and_transfer_optimization.md`
* `2026-03-16`
  * `doc/technical/2026-03-16/2026-03-16-16-55-15_python_3_12_environment_migration_feasibility.md`
* `2026-03-17`
  * `doc/technical/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  * `doc/technical/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  * `doc/technical/2026-03-17/2026-03-17-16-11-13_low_priority_neural_ode_and_transformer_models.md`
  * `doc/technical/2026-03-17/2026-03-17-16-22-47_additional_te_model_family_candidates.md`
  * `doc/technical/2026-03-17/2026-03-17-16-30-08_wave0_shared_training_and_validation_infrastructure.md`

Script documentation:

* `doc/scripts/datasets/transmission_error_dataset.md`
* `doc/scripts/datasets/visualize_transmission_error.md`
* `doc/scripts/training/train_feedforward_network.md`
* `doc/scripts/training/run_training_campaign.md`
* `doc/scripts/training/validate_training_setup.md`
* `doc/scripts/training/run_training_smoke_test.md`

Reports:

* `Analysis`
  * `doc/reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md`
  * `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  * `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` -> golden standard visual reference for future styled analytical PDFs
  * `doc/reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md`
* `Campaign Plans`
  * `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
* `Campaign Results`
  * `doc/reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md`
  * `doc/reports/campaign_results/2026-03-13-20-54-54_mixed_training_campaign_results_report.md`

Guides:

* `doc/guide/project_usage_guide.md`

These documents summarize:

* Dataset provenance and operational usage
* Analytical TE modeling theory
* ML-based online compensation strategy
* Test-rig workflow and TwinCAT implementation details
* Coding style conventions derived from prior repositories

All future feature-level technical documents must also be stored in the appropriate day folder under `doc/technical/YYYY-MM-DD/` and linked from this main project document.

---

## Critical Project Rules

The following rules are mandatory for all future project work:

* Use English as the primary project language for file names, identifiers, instructions, comments, and technical documentation.
* Adopt the coding style of `blind_handover_controller` rigorously.
* Apply the same coding-style discipline to utility scripts and report exporters, not only to training or model code.
* Keep section comments short and operational. Prefer compact labels over sentence-length explanations when the code is already explicit.
* Always take into account the documents in `reference/` or their summaries in `doc/` before making design or implementation decisions.
* Before implementing any feature, create a technical project document in `doc/technical/YYYY-MM-DD/` using the filename format `YYYY-MM-DD-HH-mm-SS-feature_name.md`.
* Each technical project document must contain the sections:
  * `Overview`
  * `Technical Approach`
  * `Involved Components`
  * `Implementation Steps`
* Every newly created technical project document must be added as a reference in this main project document.
* Before executing any training campaign, a preliminary planning report must be created in `doc/reports/campaign_plans/` describing the relevant parameters, their effects, and the candidate configuration table to be tested.
* For every approved training campaign preparation, the campaign YAML files and the exact launch command must also be generated automatically.
* The current prepared or active training campaign must be tracked persistently in `doc/running/active_training_campaign.yaml`.
* While a campaign is prepared or active, any modification to a protected campaign file must trigger a `CRITICAL WARNING` and wait for explicit user approval.
* Every final campaign-results report must be produced both as Markdown and as a validated PDF export.
* Use `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf` as the golden standard for future styled analytical PDF reports.
* Future styled PDFs must preserve the same professional report direction: white background, restrained blue accents, rounded cards, safe A4 margins, split comparison tables when needed, repeated `Config` anchors across split tables, and a final post-export PDF inspection.
* Styled PDF validation must catch not only clipping but also poor table balance such as crushed `Config` columns, oversized numeric columns, wrapped metric headers caused by bad width allocation, and right-edge pressure.
* If the validation evidence for the real exported PDF is inconclusive, the PDF-report task must stay open until the layout is proved acceptable or explicitly escalated to the user.
* Long table headers must remain visually contained inside their own cells. If needed, they should wrap within the cell instead of spilling across column boundaries.
* Identifier-style table values should wrap at meaningful token boundaries whenever possible. Avoid arbitrary one-letter or two-letter fragments at the end of a wrapped line.
* Table width balancing should start from roughly even columns, then shift space moderately toward genuinely longer content while keeping short columns tighter without over-compressing them.
* Table content should be centered vertically inside cells by default; mixed multi-line and single-line rows must not look top-aligned.
* Major sections in styled PDFs should not begin at the bottom of one page and continue immediately on the next when the section could cleanly start on the next page instead.
* No implementation code should be written before the user has explicitly approved the technical document for that feature.
* No training campaign should be executed before the user has explicitly approved both the technical document and the preliminary training-planning report for that campaign.
* Every user-requested repository change must follow this sequence:
  * create the technical project document first;
  * if the request includes training execution, create the preliminary planning report in `doc/reports/campaign_plans/` before requesting approval;
  * wait for explicit user approval;
  * if the approved work is a training campaign, generate the campaign YAML files, store the campaign state, and provide the exact launch command;
  * execute the approved modifications;
  * if the approved work includes training execution, create a detailed post-training results report in `doc/reports/campaign_results/` with metrics tables, interpretation, best-configuration summary, future improvement proposals, and a validated PDF export;
  * if the approved work adds or changes user-facing functionality, update `doc/guide/project_usage_guide.md` in detail before the final commit;
  * if the approved work introduces a new third-party library, update `requirements.txt` and every relevant setup or usage reference before the final commit;
  * tell the user the work is complete and ask for explicit approval to commit;
  * create the Git commit only after the user explicitly approves it.
* Do not create a Git commit immediately after finishing the work. Always stop and wait for explicit user approval before committing.
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
* Short operational comments instead of long explanatory prose
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
python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/baseline.yaml
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

* Python 3.12
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
* Git submodules in `reference/agents/` for reusable external agent collections

Current agent submodules:

* `reference/agents/claude-code-agents` -> `https://github.com/vizra-ai/claude-code-agents.git`
* `reference/agents/claude-code-subagents` -> `https://github.com/0xfurai/claude-code-subagents.git`
* `reference/agents/awesome-claude-code-subagents` -> `https://github.com/VoltAgent/awesome-claude-code-subagents.git`
* `reference/agents/wshobson-agents` -> `https://github.com/wshobson/agents.git`

These setup choices are intended to support reproducible development, documentation lookup, and future agent-assisted workflows.

### Environment Installation For A New User

Create and activate the Conda environment:

```powershell
conda create -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
```

Install the project dependencies.

Note: this workstation reports local CUDA Toolkit `13.1`, and the official PyTorch wheel index exposes `cu130` wheels for Windows + Python 3.12. The repository now tracks `torch` directly in `requirements.txt`, but for the current GPU setup it is still better to install the CUDA-enabled PyTorch wheel explicitly from the official index first:

```powershell
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

If you are upgrading an existing `standard_ml_codex_env` created with Python 3.10, update the interpreter first and then rebuild the binary wheels inside the environment:

```powershell
conda install -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --force-reinstall --no-cache-dir -r requirements.txt
python -m pip install --force-reinstall --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu130
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
