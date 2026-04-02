# TE Model Implementation Backlog

## Overview

This document converts the approved TE model roadmap into an executable backlog for the repository.

The requested scope is broader than a simple model list. The work must cover, for every selected model family:

- implementation;
- validation;
- smoke-test;
- one or more training campaigns;
- hyperparameter search;
- comparative reporting;
- promotion or rejection against the previously implemented architectures.

After the model-family campaigns are completed, the repository must also support:

- selection of the best overall solution;
- a dedicated best-solution training run;
- a final detailed analytical report describing the winning architecture, its strengths and weaknesses, what should be expected from it, and how it compares with all previously implemented alternatives.

This document is intentionally execution-oriented. It defines the work packages, expected artifacts, quality gates, and campaign sequence that should govern the next implementation phase.

## Technical Approach

### Guiding Principles

The backlog should preserve the project-specific constraints already established in the approved planning and analysis documents:

- TE remains the main accuracy target;
- all models must stay aligned with the real test-rig variables and with `DataValid` semantics;
- deployment viability matters together with offline accuracy;
- structured baselines must be implemented before the more ambitious physics-informed families;
- full PINNs must not be implemented before a dedicated formulation step for residual equations and loss terms.

The implementation program should therefore proceed in waves rather than as an unstructured sequence of experiments.

### Global Execution Structure

The recommended execution structure is:

1. common infrastructure and evaluation alignment;
2. structured static baselines;
3. temporal models;
4. hybrid structured models;
5. PINN preparation;
6. first PINN implementations;
7. cross-family comparison and best-solution promotion;
8. best-solution rerun and final analytical closeout.

Each wave should end with a comparison checkpoint so weak model families can be stopped early instead of consuming unnecessary training time.

### Common Deliverables Required For Every Model

Every model that enters the backlog must produce the same minimum artifact set.

#### 1. Implementation Deliverables

- model implementation under `scripts/models/`;
- any supporting training or loss utilities under `scripts/training/`;
- configuration family under `config/training/`;
- registration in `scripts/models/model_factory.py` or equivalent family-selection path;
- script-level documentation updates if the user-facing workflow changes.

#### 2. Smoke-Test Deliverables

Each model must have a lightweight smoke-test path proving that:

- imports succeed;
- the model can be instantiated from config;
- one batch can pass through forward propagation;
- the training module can compute loss and metrics for one batch;
- checkpoint save and reload logic still works when relevant.

The smoke-test does not need to be a long training run. It should be a short deterministic verification, such as:

- one forward pass over a sampled batch;
- one optimizer step;
- one `fast_dev_run`-style trainer execution if supported by the existing training stack.

#### 3. Validation Deliverables

Before large campaigns, each model must pass a validation checklist:

- correct input and output tensor shapes;
- correct treatment of angle, direction, and operating-condition features;
- correct normalization path;
- correct compatibility with valid-window dataset semantics;
- finite losses and metrics;
- deterministic inference for fixed weights and inputs.

#### 4. Campaign Deliverables

Each promoted model must have:

- an exploratory campaign;
- a refined hyperparameter campaign if the exploratory results justify it;
- a campaign plan report in `doc/reports/campaign_plans/`;
- generated campaign YAML files;
- a stored campaign state in `doc/running/active_training_campaign.yaml` while prepared or active;
- a final campaign results report in `doc/reports/campaign_results/`;
- PDF export and PDF validation for the final campaign results report.

#### 5. Comparison Deliverables

Each model family must contribute to a rolling comparison matrix covering:

- best validation metrics;
- best test metrics;
- harmonic quality indicators;
- runtime and complexity indicators;
- interpretability notes;
- deployment viability notes.

### Common Infrastructure Backlog

Before implementing all individual families, the repository should absorb a small amount of shared infrastructure work.

#### Wave 0. Shared Evaluation And Training Infrastructure

Backlog items:

- formalize a model-family-agnostic training config layout;
- formalize a common metrics schema shared by all models;
- add family-aware artifact naming so different architectures remain comparable;
- define a reusable smoke-test entry point for new models;
- define a reusable validation checklist or script for one-batch verification;
- define the common comparative report table structure that future campaign reports will reuse.

Reason:

- without this wave, each new family will create slightly different artifacts and later comparison will become noisy and expensive.

Expected output:

- one technical implementation branch for infrastructure;
- one small validation run showing the shared path works for the current feedforward baseline too.

### Structured Static Baseline Backlog

These families should be implemented first because they are the most interpretable and cheapest to compare.

#### 1. Harmonic Regression Baseline

Implementation backlog:

- implement a harmonic basis generator over angular position;
- implement a regression head for fixed or condition-dependent harmonic coefficients;
- support selectable harmonic orders from config;
- support direct TE reconstruction from predicted coefficients.

Smoke-test backlog:

- instantiate with a small harmonic dictionary;
- run one forward pass on a sampled batch;
- verify TE reconstruction shape and finite values.

Validation backlog:

- verify that the predicted harmonic coefficients reconstruct the batch TE tensor correctly;
- verify that coefficient ordering remains stable across save/load;
- verify that removing all but a few harmonics behaves as expected.

Campaign backlog:

- exploratory campaign on harmonic-order depth and coefficient parameterization strategy;
- refined campaign on regularization and selected harmonic set;
- report focusing on interpretability, harmonic fidelity, and PLC deployment suitability.

Promotion criterion:

- keep this family if it becomes a competitive structured baseline or if it gives the most interpretable harmonic decomposition even when not the best overall metric winner.

#### 2. Periodic-Feature Feedforward MLP

Implementation backlog:

- extend the current feature path with configurable `sin/cos` harmonic encodings;
- support different harmonic-depth presets;
- keep the rest of the feedforward training path reusable.

Smoke-test backlog:

- verify feature expansion shape;
- verify forward pass and loss computation with one batch.

Validation backlog:

- verify that periodic features use the intended angle unit and scaling;
- verify that feature generation is identical between train, validation, and inference paths.

Campaign backlog:

- exploratory campaign on harmonic-feature depth, hidden width, depth, dropout, and sampling density;
- refined campaign around the best feature-encoding depth and network size;
- comparison report versus the raw-angle feedforward baseline.

Promotion criterion:

- promote if it materially improves over the current feedforward baseline with similar runtime complexity.

#### 3. Residual MLP Over Harmonic Or Analytical Baseline

Implementation backlog:

- implement a structured baseline submodule;
- implement a residual predictor branch;
- support training the residual branch with frozen or jointly trainable structured components;
- log both structured prediction and residual prediction separately.

Smoke-test backlog:

- verify that `structured + residual` reconstructs the final TE output;
- verify that a zero residual branch reduces to the structured baseline.

Validation backlog:

- verify residual target construction;
- verify that residual magnitude stays numerically consistent with expectations;
- verify that metric logging separates structured-only and final prediction quality.

Campaign backlog:

- exploratory campaign comparing:
  - harmonic baseline only;
  - residual branch over harmonic baseline;
  - residual branch over analytical approximation if later available;
- refined campaign on residual width, depth, and regularization.

Promotion criterion:

- high priority promotion if it outperforms the pure MLP while preserving interpretability.

#### 4. Tree-Based Standard ML Benchmarks

Implementation backlog:

- implement a tabular benchmark path for tree-based models on the same features;
- ensure feature engineering is aligned with the neural baselines.

Smoke-test backlog:

- fit on a small subset and confirm finite predictions.

Validation backlog:

- verify train/inference feature parity;
- verify serialization and reload path if model persistence is added.

Campaign backlog:

- limited benchmark campaign rather than a large family sweep;
- report should focus on whether neural models are justified by the performance gap.

Promotion criterion:

- use mainly as a benchmark family, not as the final deployment target unless results are unexpectedly strong.

### Temporal Model Backlog

These families should be implemented only after the static structured baselines establish a strong non-sequential reference.

#### 5. Lagged-Feature MLP / NARX-Style Regressor

Implementation backlog:

- add sequence-window dataset support for lagged features;
- support configurable lag length and feature selection for lagged inputs;
- keep the predictor feedforward for deployment simplicity.

Smoke-test backlog:

- verify window extraction shape and alignment;
- verify one forward pass with lagged inputs.

Validation backlog:

- verify that no future leakage is introduced by the windowing logic;
- verify that the first valid sample after windowing is correct;
- verify that lagged features remain aligned with motion direction and operating conditions.

Campaign backlog:

- exploratory campaign on lag length, window feature set, and network size;
- refined campaign if short-memory gains appear consistently.

Promotion criterion:

- promote only if the performance gain clearly exceeds the added input complexity.

#### 6. GRU Baseline

Implementation backlog:

- add sequence-batch support in the dataset and datamodule path;
- implement a compact `GRU` model with configurable hidden size, layers, and sequence reduction logic.

Smoke-test backlog:

- verify sequence tensor layout;
- verify recurrent forward pass and hidden-state reset behavior.

Validation backlog:

- verify no sequence leakage across files or curves;
- verify deterministic evaluation behavior with fixed sequence ordering;
- verify that direction changes are handled explicitly.

Campaign backlog:

- exploratory campaign on sequence length, hidden size, number of layers, and learning rate;
- refined campaign only if `GRU` beats the lagged-feature baseline.

Promotion criterion:

- keep if it proves that learned recurrent state captures real TE history dependence.

#### 7. LSTM Baseline

Implementation backlog:

- implement `LSTM` using the same sequence interface introduced for `GRU`;
- keep configuration comparable to the `GRU` family.

Smoke-test backlog:

- same smoke-test coverage as `GRU`, with explicit hidden/cell state verification.

Validation backlog:

- verify state reset, checkpoint reload, and sequence-length handling.

Campaign backlog:

- run only after `GRU` or in parallel with a tightly controlled comparison;
- focus on whether the extra memory capacity gives a measurable benefit.

Promotion criterion:

- keep only if it improves enough over `GRU` or `TCN` to justify the added recurrent complexity.

#### 8. Temporal Convolutional Network

Implementation backlog:

- implement causal 1D temporal convolution blocks with configurable dilation and kernel size;
- support fixed receptive-field design from config.

Smoke-test backlog:

- verify tensor layout and output length;
- verify one forward and loss pass.

Validation backlog:

- verify receptive-field coverage against the configured sequence length;
- verify no future-context leakage.

Campaign backlog:

- exploratory campaign on window size, dilation schedule, channel width, and depth;
- refined campaign if temporal gains are confirmed.

Promotion criterion:

- strong candidate if it matches or beats recurrent models with easier training and runtime behavior.

#### 9. Lightweight Transformer Exploratory Baseline

Implementation backlog:

- implement a compact attention-based temporal model only after the main temporal families are already comparable;
- keep the sequence interface aligned with the `GRU`, `LSTM`, and `TCN` families;
- constrain parameter count and context length so the family remains a genuine lightweight baseline.

Smoke-test backlog:

- verify sequence tensor layout, masking or padding path if used, and one forward-loss pass.

Validation backlog:

- verify no future-context leakage;
- verify consistent handling of sequence length and ordering;
- verify that the architecture remains numerically stable on short and medium windows.

Campaign backlog:

- limited exploratory campaign after the main temporal wave;
- refined campaign only if it shows value beyond `TCN`, `GRU`, or `LSTM`.

Promotion criterion:

- promote only if broader-context modeling yields a clear gain that simpler temporal families do not achieve.

#### 10. State-Space Sequence Exploratory Baseline

Implementation backlog:

- implement a compact state-space sequence model only after the main temporal families are benchmarked;
- keep the sequence interface aligned with the rest of the temporal stack.

Smoke-test backlog:

- verify sequence input layout and one forward-loss pass with finite outputs.

Validation backlog:

- verify no future leakage;
- verify stable handling of short and medium sequence windows;
- verify deterministic evaluation behavior for fixed weights and ordered inputs.

Campaign backlog:

- limited exploratory campaign after the main temporal wave;
- refined campaign only if it shows a better cost/performance tradeoff than the other advanced temporal options.

Promotion criterion:

- promote only if compact state-space modeling adds value beyond `TCN`, `GRU`, `LSTM`, and the lightweight transformer branch.

### Hybrid Structured Model Backlog

These families are the main bridge between standard ML and full PINNs.

#### 11. Mixture-Of-Experts / Regime-Conditioned Model

Implementation backlog:

- implement a lightweight gating path or explicit regime-conditioned expert selection;
- keep the first version small and interpretable;
- support one or more backbones such as MLP, residual MLP, or harmonic-head variants.

Smoke-test backlog:

- verify expert routing shape and final TE prediction shape;
- verify that a single-active-expert fallback behaves correctly.

Validation backlog:

- verify that the gating logic does not introduce train/inference mismatch;
- verify that experts remain numerically active and do not collapse immediately to a degenerate solution;
- verify consistency across operating-regime partitions.

Campaign backlog:

- exploratory campaign on number of experts, gating strategy, and backbone choice;
- refined campaign only if regime specialization improves generalization over the best single-backbone model.

Promotion criterion:

- promote if it improves cross-regime performance while remaining interpretable and compact enough for the project goals.

#### 12. Fourier-Feature Network

Implementation backlog:

- implement configurable Fourier encodings for angular inputs;
- support either fixed frequencies or a controlled learned-frequency variant if justified.

Smoke-test backlog:

- verify Fourier feature generation and forward pass.

Validation backlog:

- verify angular scaling and frequency ordering;
- verify parity between train and inference encoding paths.

Campaign backlog:

- exploratory campaign on encoding bandwidth, network width, depth, and regularization;
- refined campaign around the best spectral encoding range.

Promotion criterion:

- high-priority promotion if it improves harmonic fidelity and generalization simultaneously.

#### 13. Harmonic-Head Network

Implementation backlog:

- implement a network whose outputs are harmonic coefficients rather than direct TE points;
- reconstruct TE analytically from the predicted coefficients;
- optionally support condition-dependent coefficient heads.

Smoke-test backlog:

- verify coefficient output shape and TE reconstruction path.

Validation backlog:

- verify coefficient-to-TE reconstruction numerically;
- verify interpretability logging of dominant coefficients.

Campaign backlog:

- exploratory campaign on harmonic dictionary size and head architecture;
- refined campaign on coefficient regularization and output parameterization.

Promotion criterion:

- promote if it offers strong accuracy with superior interpretability and deployment readiness.

#### 14. Laplacian-Regularized Or Smoothness-Constrained Network

Implementation backlog:

- implement derivative or graph-based smoothness penalties;
- support regularization-weight scheduling from config;
- keep the base predictor selectable so the regularizer can be reused across model families.

Smoke-test backlog:

- verify that the regularization term can be computed on a batch without NaN or shape errors.

Validation backlog:

- verify that the regularizer responds correctly to smoother versus noisier predictions;
- verify that the loss remains finite under mixed data and regularization terms.

Campaign backlog:

- exploratory campaign on regularization type and weight;
- refined campaign around the best regularization regime.

Promotion criterion:

- keep if it improves robustness and harmonic realism without oversmoothing the TE curves.

#### 15. SIREN / Periodic-Activation Network

Implementation backlog:

- implement periodic-activation blocks with proper initialization control;
- expose initialization and frequency-scale controls in config.

Smoke-test backlog:

- verify stable forward propagation and finite gradients for one batch.

Validation backlog:

- verify initialization sensitivity and derivative stability.

Campaign backlog:

- limited exploratory campaign first;
- refined campaign only if clear harmonic-detail gains appear.

Promotion criterion:

- keep as a specialist family if it captures fine periodic detail better than Fourier-feature MLPs.

#### 16. Hamiltonian-Inspired Exploratory Model

Implementation backlog:

- create a separate exploratory branch only after the stronger hybrid families are in place;
- first define the latent-state interpretation before writing the model code.

Smoke-test backlog:

- verify only after the state formulation exists.

Validation backlog:

- require a conceptual validation note explaining why the chosen state has mechanical meaning.

Campaign backlog:

- only a limited research campaign unless early evidence is unexpectedly strong.

Promotion criterion:

- low priority; keep only if it reveals a physically meaningful advantage not captured by the more direct hybrid models.

#### 17. Neural ODE / Continuous-State Exploratory Model

Implementation backlog:

- define whether the independent variable is angle, time, or a mixed formulation before implementation;
- define the latent continuous state and the solver strategy;
- keep the first variant intentionally narrow and exploratory.

Smoke-test backlog:

- verify one forward pass through the ODE block and one backward pass with finite gradients.

Validation backlog:

- verify consistency of the chosen continuous variable definition;
- verify solver stability on representative batches;
- verify that the formulation is not leaking future information through the sequence or integration setup.

Campaign backlog:

- only a limited exploratory campaign after the stronger hybrid families are already benchmarked;
- refined campaign only if the formulation proves scientifically meaningful and empirically promising.

Promotion criterion:

- promote only if continuous-state modeling captures behavior that the main temporal and hybrid families still miss.

### PINN Preparation And PINN Backlog

The PINN track should be separated into preparation and implementation.

#### 18. Kernel Ridge / Gaussian Process Optional Benchmark

Implementation backlog:

- add a smooth-regression benchmark path for kernel ridge and, if practical, a Gaussian-process-style baseline on a controlled subset.

Smoke-test backlog:

- fit a small subset and verify finite predictions.

Validation backlog:

- verify feature preprocessing parity with the neural baselines;
- verify that the benchmark remains computationally tractable on the selected subset sizes.

Campaign backlog:

- optional benchmark campaign only;
- use primarily for sample-efficiency and smooth-regression comparison rather than as a final candidate.

Promotion criterion:

- keep only as a benchmark unless it becomes unexpectedly competitive.

#### 19. PINN Formulation Package

Implementation backlog:

- create a dedicated formulation document for:
  - inputs, outputs, and latent states;
  - independent variable definition;
  - residual equations;
  - periodic and boundary conditions;
  - collocation strategy;
  - term normalization and weighting.

Validation backlog:

- verify that the proposed residual terms are identifiable from the available measurements;
- verify that residual magnitudes are numerically balanced after normalization.

Promotion criterion:

- the first PINN implementation must not start before this package is approved.

#### 20. First PINN Baseline

Implementation backlog:

- implement a data term plus a minimal physically meaningful residual term;
- keep the first PINN intentionally narrow rather than maximally ambitious;
- log data and physics losses separately.

Smoke-test backlog:

- verify forward pass, residual computation, and backward propagation on one batch and one collocation batch.

Validation backlog:

- verify that the physics term decreases under training without destabilizing the data term;
- verify that collocation sampling and data sampling remain consistent.

Campaign backlog:

- exploratory campaign on loss weights, collocation density, and normalization strategy;
- refined campaign only if the first PINN shows credible gains.

Promotion criterion:

- promote only if it improves generalization or physical plausibility enough to offset the added complexity.

### Campaign Program Backlog

The campaign program should be wave-based rather than model-by-model in isolation.

#### Campaign Wave A. Structured Baseline Campaign

Included families:

- harmonic regression;
- periodic-feature MLP;
- residual MLP;
- tree-based benchmark.

Expected outcome:

- identify the best structured static family;
- establish a stronger non-sequential baseline than the current feedforward model.

#### Campaign Wave B. Temporal Model Campaign

Included families:

- lagged-feature MLP;
- `GRU`;
- `LSTM`;
- `TCN`.

Expected outcome:

- determine whether history dependence is real and valuable enough to justify sequence models.

Deferred exploratory extension:

- `Lightweight Transformer` may enter only after the main temporal wave if the earlier temporal families leave credible evidence that broader-context modeling is still underexploited.
- `State-Space Sequence Model` may enter only after the main temporal wave if compact longer-context dynamics still look under-modeled.

#### Campaign Wave C. Hybrid Structured Campaign

Included families:

- Mixture-of-Experts / regime-conditioned model;
- Fourier-feature network;
- harmonic-head network;
- Laplacian-regularized network;
- optional `SIREN`.

Expected outcome:

- identify the best bridge architecture between standard ML and PINNs.

Deferred exploratory extension:

- `Neural ODE` may enter after the main hybrid wave if a defensible continuous-state formulation becomes clear.
- optional `Kernel Ridge / Gaussian Process` benchmark may enter as a side benchmark if a stronger non-neural smooth-regression reference is useful.

#### Campaign Wave D. PINN Preparation And First PINN Campaign

Included families:

- first approved PINN baseline;
- optionally one second PINN variant only if the first is credible.

Expected outcome:

- verify whether explicit physics residuals improve on the best hybrid or structured baseline.

#### Campaign Wave E. Best-Solution Confirmation Campaign

Included content:

- rerun the best candidate architecture with the selected best hyperparameters;
- run multiple seeds if feasible;
- run the strongest previous baselines for direct comparison if a clean rerun is needed.

Expected outcome:

- confirm that the chosen best solution is not a one-run accident;
- prepare the final comparison report and deployment-oriented expectation analysis.

### Hyperparameter Search Backlog

The hyperparameter search should use a two-stage strategy for every promoted family.

#### Stage 1. Coarse Search

Goal:

- identify the right region of the search space quickly.

Typical dimensions:

- learning rate;
- weight decay;
- hidden width and depth;
- harmonic count or spectral bandwidth;
- sequence length;
- regularization weights;
- collocation density for PINNs.

#### Stage 2. Local Refinement

Goal:

- tighten around the best-performing region discovered by the coarse search.

Reason:

- this avoids wasting compute on wide exhaustive sweeps for weak families.

### Report Backlog

The documentation program should be part of the implementation backlog, not an afterthought.

#### Required Reports During The Program

- one campaign plan report per approved campaign wave;
- one campaign results report per completed campaign wave;
- one cross-wave comparison analysis once structured, temporal, hybrid, and PINN families have all been evaluated enough to compare fairly;
- one final best-solution report after the confirmation campaign.

#### Required Final Best-Solution Report Content

The final report must include:

- the selected best architecture and best training configuration;
- detailed architecture description;
- training and evaluation summary;
- comparison with previously implemented architectures;
- advantages and disadvantages of the winning family;
- what should reasonably be expected from the model in future use;
- limitations and residual risks;
- suggested next steps for future improvement.

As required by the repository rules, the final campaign-results reports must be delivered as Markdown and PDF, and the exported PDF must be validated against the repository golden standard.

### Decision Rules For Best-Solution Selection

The best solution should not be selected by test MAE alone.

The decision should balance:

- TE accuracy;
- stability across validation and test;
- harmonic fidelity;
- complexity and inference cost;
- interpretability;
- deployment viability;
- consistency across seeds or reruns.

A simpler structured or hybrid model should win over a heavier family if the metric gain of the heavier family is marginal.

## Involved Components

- `README.md`
  Main project document that must reference this backlog document.
- `doc/README.md`
  Internal documentation index that should also list this technical document.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
  This technical backlog document.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  Approved roadmap document for the model families.
- `doc/reports/analysis/2026-03-17-15-46-01_te_model_family_analysis_report.md`
  Approved analytical comparison report that motivates the backlog priorities.
- `scripts/models/`
  Future architecture implementations for the approved model families.
- `scripts/training/`
  Future training, loss, datamodule, and validation updates needed by the new families.
- `config/training/`
  Future family-specific training configs, queue configs, and campaign folders.
- `doc/reports/campaign_plans/`
  Required planning reports for each approved campaign wave.
- `doc/reports/campaign_results/`
  Required results reports for completed campaigns, with validated PDF exports.
- `doc/running/active_training_campaign.yaml`
  Persistent prepared or active campaign state tracking for future training waves.
- `doc/guide/project_usage_guide.md`
  Must be updated later if the approved implementation changes runnable training workflows.

## Implementation Steps

1. Create this technical backlog document and register it in the documentation indexes.
2. Wait for explicit user approval before modifying implementation code, training configs, or campaign artifacts.
3. Implement the shared infrastructure wave so all future model families use a comparable training and reporting path.
4. Prepare the first campaign plan report for the structured baseline wave.
5. After approval, implement and validate harmonic regression, periodic-feature MLP, residual MLP, and the tree-based benchmark.
6. Add smoke-tests for each structured baseline family.
7. Generate the structured-baseline campaign YAML files, store the campaign state, and run the approved campaign.
8. Produce the structured-baseline results report and validated PDF export.
9. Prepare the temporal-model campaign plan report.
10. After approval, implement and validate lagged-feature MLP, `GRU`, `LSTM`, and `TCN`.
11. Add smoke-tests for each temporal family and run the approved temporal campaign.
12. Produce the temporal-model results report and validated PDF export.
13. Prepare the hybrid-structured campaign plan report.
14. After approval, implement and validate Fourier-feature, harmonic-head, Laplacian-regularized, and optional `SIREN` models.
15. Add smoke-tests for each hybrid family and run the approved hybrid campaign.
16. Produce the hybrid-model results report and validated PDF export.
17. If justified after the temporal wave, implement, validate, smoke-test, and benchmark the low-priority `Lightweight Transformer` exploratory family.
18. If justified after the temporal wave, implement, validate, smoke-test, and benchmark the low-priority `State-Space Sequence Model` exploratory family.
19. If justified after the hybrid wave, implement, validate, smoke-test, and benchmark the low-priority `Neural ODE` exploratory family.
20. If useful as a benchmark, implement, validate, smoke-test, and benchmark the optional `Kernel Ridge / Gaussian Process` family.
21. Prepare the dedicated PINN formulation document and obtain explicit approval for it.
22. Prepare the PINN campaign plan report only after the formulation is approved.
23. Implement, validate, and smoke-test the first PINN baseline, then run the approved PINN campaign.
24. Produce the PINN results report and validated PDF export.
25. Create a cross-wave comparison analysis that ranks all sufficiently evaluated families.
26. Select the candidate best solution based on accuracy, stability, interpretability, complexity, and deployment viability.
27. Prepare the best-solution confirmation campaign plan report.
28. After approval, rerun the best solution with the selected best hyperparameters and any required comparison reruns.
29. Produce the final best-solution report and validated PDF export, including architecture analysis, expected behavior, comparison against earlier architectures, and future recommendations.
30. Update `doc/guide/project_usage_guide.md` before any final commit if the approved implementation changes the runnable workflows.
31. Stop after reporting completion and explicitly ask the user for approval before creating any Git commit.
