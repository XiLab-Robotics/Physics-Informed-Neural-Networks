# TE Model Family Roadmap

## Overview

This document defines the planning baseline for the next modeling phase of the repository.

The user requested a detailed implementation roadmap covering:

- standard data-driven algorithms and neural networks that could improve the current TE compensation case study;
- temporal models such as `LSTM` that can exploit short windows or sequences;
- intermediate solutions between pure black-box models and full PINNs, especially Fourier-based, Laplacian-regularized, and Hamiltonian-inspired approaches;
- full PINN directions and the technical prerequisites needed before deriving the final loss equations.

The planning target is the Rotational Transmission Error compensation problem for the RV reducer test rig, with the repository constraints already established by the project references:

- TE remains the main accuracy quantity;
- the input conditions must stay aligned with the real test rig (`speed`, `torque`, `temperature`, angular position, and valid operating windows);
- model choices must be judged not only by offline accuracy, but also by interpretability, robustness, and future TwinCAT / PLC deployment viability.

The purpose of this document is to define what should be implemented first, what should be treated as exploratory, and what technical groundwork is required before the project moves into a full physics-informed stage.

## Technical Approach

### Problem Framing

The current TE compensation problem is not a generic regression task.

It has four relevant structural properties:

1. the target is periodic or quasi-periodic with respect to angular position;
2. the target varies with operating conditions such as speed, torque, and oil temperature;
3. some error components are explainable through reducer kinematics and harmonic structure;
4. the final solution should remain simple enough for future PLC-side deployment or at least for conversion into a compact inference block.

Because of that, the model roadmap should not jump directly from a static feedforward baseline to a fully constrained PINN. A staged progression is more defensible:

1. strengthen static baselines;
2. test whether short temporal memory really helps;
3. inject structure through spectral or physics-inspired inductive biases;
4. move to full PINNs only after the mechanical residual terms and identifiability limits are clear.

### Evaluation Axes For Every Candidate

Every candidate family should be judged on the same axes:

- offline TE prediction accuracy on valid windows;
- generalization across operating conditions and unseen trajectories;
- ability to represent periodic or harmonic content cleanly;
- sensitivity to dataset size and noise;
- interpretability of intermediate quantities;
- exportability to lightweight runtime inference;
- implementation complexity and training stability.

For this repository, a model is not automatically a good candidate just because it can fit the data better. A heavier model is only justified if it improves one of these practical axes without making deployment unrealistic.

### Standard Approaches To Prioritize First

#### 1. Harmonic Regression Baseline

Principle:

- represent TE as a sum of sinusoidal components over angular position, with coefficients predicted globally or conditioned on operating variables.

Why it matters here:

- the reference material already states that TE frequency components have a direct physical meaning;
- this is the most interpretable bridge between analytical modeling and ML compensation;
- it is very compatible with PLC deployment.

Advantages:

- excellent interpretability;
- very low runtime cost;
- direct alignment with harmonic compensation logic;
- useful as a sanity baseline even if later models outperform it.

Disadvantages:

- limited ability to capture strongly nonlinear operating-condition effects;
- needs manual harmonic selection or coefficient parameterization;
- may underfit local irregularities and non-stationary behavior.

Recommendation:

- implement early, even before heavier neural architectures, because it sets a strong physics-aware baseline and clarifies which harmonics truly matter.

#### 2. Static MLP With Engineered Inputs

Principle:

- predict TE from angular position plus operating variables using a feedforward network;
- optionally augment inputs with harmonic features such as `sin(k*theta)` and `cos(k*theta)`.

Why it matters here:

- this is the natural continuation of the existing feedforward work;
- it is still compact enough to export later;
- it provides a clean baseline against which sequence models and PINNs can be compared.

Advantages:

- simple implementation and training;
- low inference latency;
- can capture moderate nonlinear couplings among angle, speed, torque, and temperature;
- easy to regularize and benchmark.

Disadvantages:

- no explicit memory;
- if fed only raw angle, it may learn periodic structure less efficiently than a spectral formulation;
- may need careful feature engineering to generalize well across operating regimes.

Recommendation:

- keep this as the primary standard baseline, but strengthen it with periodic features and explicit residual-style output design.

#### 3. Residual MLP On Top Of Harmonic Or Analytical Baseline

Principle:

- first compute a harmonic or analytical approximation;
- let a small MLP predict only the residual TE not explained by the structured baseline.

Advantages:

- more sample-efficient than a pure black-box MLP;
- preserves interpretability of the main TE structure;
- typically easier to deploy than a large end-to-end network.

Disadvantages:

- quality depends on the baseline quality;
- requires a clean separation between deterministic structure and residual terms.

Recommendation:

- this is one of the most promising near-term directions for the repository.

#### 4. Tree-Based Regressors As Non-Neural Standard ML Baselines

Candidate examples:

- gradient boosting;
- random forest;
- XGBoost-style methods if later approved.

Advantages:

- strong tabular baselines for operating-condition regression;
- easy feature-importance inspection;
- good benchmark for checking whether neural nets are actually necessary.

Disadvantages:

- weak native handling of periodic continuity over angle unless features are engineered carefully;
- less elegant for compact PLC deployment than a small linear or neural model;
- sequence handling is indirect.

Recommendation:

- useful as a benchmark layer, but not the main long-term architecture.

### Sequence-Aware Standard Networks

The temporal family is justified only if TE depends not just on the current angular and operating state, but also on recent history, transient evolution, hysteresis, thermal drift, or unmodeled lag.

#### 1. Lagged-Feature MLP / NARX-Style Regressor

Principle:

- feed the model a fixed window of past values, for example past TE samples, past angles, or past operating variables, while keeping the predictor itself feedforward.

Advantages:

- much simpler than recurrent models;
- preserves deterministic inference cost;
- often strong enough if the useful memory is short.

Disadvantages:

- manual window design;
- parameter count grows with window size;
- less elegant state handling than true sequence models.

Recommendation:

- implement before `LSTM`, because it tests whether temporal context helps at all without adding recurrent training complexity.

#### 2. LSTM / GRU

Principle:

- recurrent units maintain a latent state across the input sequence and can learn short- and medium-range dependencies.

Why it is relevant:

- it directly matches the user hypothesis that a temporal window may help;
- it can absorb hysteresis, transient thermal effects, and sequence-dependent operating behavior that a static model misses.

Advantages:

- explicit sequence modeling;
- flexible memory length;
- can improve robustness when operating points evolve gradually rather than staying strictly static.

Disadvantages:

- training is slower and more fragile than static MLPs;
- recurrent hidden state is harder to interpret and harder to port cleanly to PLC logic;
- may be unnecessary if TE is dominated by instantaneous angular plus operating-condition structure.

Recommendation:

- good candidate after lagged-MLP validation;
- prefer `GRU` first if a lighter recurrent baseline is desired, then `LSTM` if longer memory appears necessary.

#### 3. Temporal Convolutional Network (TCN) / 1D Causal CNN

Principle:

- learn temporal dependencies with dilated 1D convolutions over a fixed sequence window.

Advantages:

- often easier to train than recurrent networks;
- parallelizable;
- fixed receptive field gives predictable runtime;
- good compromise between memory modeling and deployment simplicity.

Disadvantages:

- still requires window design;
- can become less intuitive than lagged MLPs;
- does not provide the same compact hidden-state interpretation as some state-space formulations.

Recommendation:

- this is a serious alternative to `LSTM` and should likely be tested in the same phase.

#### 4. Lightweight Transformer Or State-Space Sequence Model

Principle:

- use attention or modern state-space operators for sequence modeling.

Advantages:

- high expressive power;
- good at longer context lengths.

Disadvantages:

- excessive complexity for the current dataset scale and deployment target;
- weak fit with PLC-oriented runtime constraints;
- lower immediate value than `LSTM`, `GRU`, or `TCN`.

Recommendation:

- keep in scope as an explicit low-priority exploratory family after `TCN`, `GRU`, and `LSTM`.

#### 5. Explicit State-Space Sequence Model

Principle:

- use a compact learned state-space operator to propagate sequence information with more structured dynamics than a plain recurrent model and less direct attention cost than a transformer.

Advantages:

- potentially good long-context efficiency;
- conceptually well positioned between `TCN` and attention-based sequence modeling;
- may offer a cleaner compact-dynamics bias than a generic transformer.

Disadvantages:

- still more complex than the main temporal baselines;
- currently weaker short-term justification than `TCN`, `GRU`, or `LSTM`.

Recommendation:

- keep in scope as a separate low-priority exploratory temporal family after the main temporal wave.

### Middle-Ground Models Between Standard ML And Full PINNs

This family is likely the most strategic for the repository. It introduces physical or structural bias without immediately requiring complete residual equations.

#### 0. Mixture-Of-Experts / Regime-Conditioned Model

Principle:

- use a lightweight gating mechanism or explicit regime conditioning so partially specialized experts model different operating regions such as speed, torque, temperature, or motion-direction regimes.

Why it fits this problem:

- TE behavior can vary meaningfully across operating conditions;
- a single global model may average across regimes that are better handled by specialized submodels;
- the idea can be applied to MLP, harmonic-head, or residual backbones.

Advantages:

- potentially better cross-regime generalization;
- interpretable regime specialization when the gating remains simple;
- can improve fit without requiring a fully different model family for each operating region.

Disadvantages:

- adds gating complexity and possible instability;
- can become unnecessarily complicated if the operating dependence is already smooth enough for one model.

Recommendation:

- add as a medium-priority structured or hybrid family after the main structured baselines.

#### 1. Fourier-Feature MLP

Principle:

- map angular inputs through a Fourier basis before the main network;
- optionally predict harmonic amplitudes and phases conditioned on operating variables.

Why it fits this problem:

- TE is strongly periodic;
- the analytical model points to physically meaningful frequencies;
- Fourier structure can improve sample efficiency and extrapolation over angle.

Advantages:

- strong inductive bias for periodic signals;
- better angular representation than raw-angle MLPs;
- still relatively easy to export if the basis is fixed.

Disadvantages:

- requires choosing frequency bandwidth and encoding strategy;
- may over-focus on periodic structure and under-represent slow non-periodic drift if not designed well.

Recommendation:

- one of the highest-priority hybrid approaches.

#### 2. Harmonic-Head Network

Principle:

- the network predicts coefficients of selected sinusoids instead of raw TE samples directly;
- the final TE is reconstructed analytically from those coefficients.

Advantages:

- highly interpretable;
- naturally aligns with the compensation logic already discussed in the reference material;
- simplifies later TwinCAT integration.

Disadvantages:

- requires fixing or learning a harmonic dictionary;
- may miss localized non-harmonic residuals.

Recommendation:

- should be tested alongside the Fourier-feature MLP. These two models are close relatives, but the harmonic-head variant is more explicit and deployment-friendly.

#### 3. Laplacian Or Smoothness-Regularized Networks

Principle:

- train a standard predictor while penalizing undesirable curvature or inconsistency over the angular manifold or neighborhood graph of samples;
- examples include angular smoothness penalties, graph Laplacian regularization over nearby operating points, or derivative penalties over predicted TE.

Why it fits this problem:

- TE curves are structured and smooth over valid windows, but not arbitrary;
- this can inject geometric discipline without requiring the full analytical residual equation.

Advantages:

- simple extension of current models;
- encourages physically plausible smoothness;
- may improve generalization under sparse operating-condition coverage.

Disadvantages:

- regularization strength is sensitive;
- too much smoothing can erase real harmonic content;
- less interpretable than explicit harmonic modeling.

Recommendation:

- strong intermediate option, especially as a low-risk step before full PINN residuals.

#### 4. SIREN Or Periodic-Activation Networks

Principle:

- use periodic activations so the network represents oscillatory signals natively.

Advantages:

- excellent expressivity for periodic signals and derivatives;
- potentially useful when later moving to derivative-based physics losses.

Disadvantages:

- training can be sensitive to initialization and scaling;
- deployment simplicity is worse than with standard activations;
- may be more research-heavy than necessary for the first hybrid wave.

Recommendation:

- exploratory, but relevant if Fourier-feature models still struggle with fine harmonic detail.

#### 5. Hamiltonian-Inspired Networks

Principle:

- enforce that latent dynamics or learned state evolution follow energy-like conservation or structured differential relations.

Why this is only a partial fit:

- Hamiltonian structure is powerful when the system state and conjugate variables are clearly defined;
- our current TE compensation task is closer to structured regression under operating conditions than to a fully observed conservative dynamical system.

Advantages:

- can improve interpretability when a physically meaningful latent state exists;
- useful if later the project evolves toward dynamic reducer-state modeling rather than static compensation only.

Disadvantages:

- the current measured variables do not yet define a clean Hamiltonian state space;
- strong risk of over-complicating the problem too early;
- unclear immediate deployment benefit for TwinCAT compensation.

Recommendation:

- low-to-medium priority research branch, not a first implementation target.

#### 6. Neural ODE / Latent State Hybrid

Principle:

- model the evolution of a latent state over angle or time, while keeping data loss and selected structural penalties.

Advantages:

- natural bridge toward continuous-time or continuous-angle physics constraints;
- useful if transient effects become central.

Disadvantages:

- heavier training cost;
- more moving parts than the repository currently needs.

Recommendation:

- keep in scope as an explicit low-priority exploratory family after the main hybrid models and before or alongside advanced physics-informed exploration, depending on the final formulation.

#### 7. Low-Priority Exploratory Status

`Lightweight Transformer`, `State-Space Sequence Model`, and `Neural ODE` families remain within the project scope.

They are not excluded. They are simply deferred until:

- the main structured, temporal, and hybrid families have been compared;
- the repository has evidence that longer-context or continuous-state modeling is still missing something important;
- or the user explicitly promotes one of these families into an earlier execution wave.

### Full PINN Directions

PINNs become justified when the project is ready to encode explicit mechanical constraints rather than only soft structural priors.

#### What A PINN Would Try To Learn

A full PINN for this repository would likely not be just "predict TE from inputs and add a generic physics penalty".

It should define a more structured learning target, for example:

- TE directly, with residuals built from analytical kinematic equations;
- harmonic coefficients constrained by reducer-stage relations;
- decomposed contributions from high-speed and low-speed stages;
- latent mechanical error terms that reconstruct the final TE through a differentiable analytical layer.

The last two options are often more meaningful than a single opaque output because they preserve traceability to physical causes.

#### What Must Be Specified Before PINN Implementation

1. Physics State Definition

- decide which variables are inputs, outputs, latent states, and fixed parameters;
- clarify whether angle is treated as the independent coordinate, whether time is explicit, and how speed enters the equations.

2. Governing Relations

- identify the kinematic constraints to enforce from the equivalent multi-loop model;
- define which relations are exact, which are approximate, and which are only regularization targets.

3. Error Decomposition

- decide whether the model learns aggregate TE only or separate physically interpretable error components;
- check whether the available data can identify those components without severe ambiguity.

4. Boundary And Periodicity Conditions

- enforce periodic consistency over angular cycles when appropriate;
- define continuity conditions across valid windows and direction changes.

5. Collocation Strategy

- determine where physics residuals are evaluated:
  - at data points only;
  - at additional collocation points over angle;
  - across multiple operating-condition grids.

6. Loss Weighting Strategy

- define how data loss, physics residual, smoothness, periodicity, and regularization are weighted;
- plan for curriculum or adaptive weighting to avoid one term dominating training.

7. Scaling And Non-Dimensionalization

- normalize angles, TE, torque, speed, and temperature consistently;
- non-dimensionalization is especially important so the different residual terms have comparable magnitudes.

8. Identifiability Analysis

- verify that the chosen physics parameters can actually be inferred from the measured signals;
- otherwise the PINN may satisfy equations numerically while remaining physically ambiguous.

9. Noise Model

- experimental TE contains noise, segmentation uncertainty, and operating variability;
- the PINN design must decide whether physics constraints should be strict or softened.

10. Deployment Path

- a pure training-time PINN may still export only the neural part at inference time;
- alternatively, the deployed model may need the analytical reconstruction layer too;
- this distinction must be decided early for TwinCAT compatibility.

#### Advantages Of PINNs For This Case Study

- better physical consistency under limited data;
- improved interpretability if outputs or latent terms are structured properly;
- better extrapolation across operating conditions when the encoded physics is correct;
- natural connection to the reducer analytical model already present in the project references.

#### Disadvantages And Risks

- substantial formulation effort before any coding;
- sensitive optimization due to multi-term losses;
- risk of encoding incomplete or weakly identifiable physics;
- higher implementation complexity and slower iteration than standard baselines.

#### Recommendation

- treat the PINN track as a second-stage effort after hybrid spectral and smoothness-constrained models.
- before implementing a full PINN, prepare a dedicated document only for:
  - chosen state variables;
  - residual equations;
  - boundary and periodic conditions;
  - loss-term normalization and weighting strategy.

### Recommended Implementation Priority

The most defensible roadmap for this repository is:

#### Phase 1. Strengthen Standard Static Baselines

- harmonic regression baseline;
- static MLP with periodic features;
- residual MLP on top of harmonic or analytical baseline;
- optional tree-based benchmark.

Reason:

- low cost, high interpretability, direct value for benchmarking.

#### Phase 2. Verify Whether Temporal Context Really Helps

- lagged-feature MLP;
- `GRU` or `LSTM`;
- `TCN`.

Reason:

- do not assume a sequence model is beneficial until the data proves that recent history contains useful information beyond current state and angle.

#### Phase 3. Add Structured Hybrid Bias

- Fourier-feature MLP;
- harmonic-head network;
- Laplacian or derivative regularization;
- optionally `SIREN`.

Reason:

- likely the best tradeoff between accuracy gain, physical plausibility, and implementation effort.

#### Phase 4. Prepare Full PINN Formulation

- define states, equations, residuals, collocation points, and weighting logic;
- only then implement the first PINN baseline.

Reason:

- a PINN implemented too early risks becoming a fragile black-box model with an arbitrary extra penalty, which is the opposite of the intended scientific contribution.

### Expected Winners For This Specific Case

At the planning level, the strongest candidates are:

1. residual MLP with periodic or harmonic features;
2. lagged-feature MLP or `TCN`;
3. Fourier-feature or harmonic-head hybrid network;
4. only after those, a carefully formulated PINN.

`LSTM` remains a valid candidate, especially if hysteresis and transient evolution are confirmed by the data, but it should not automatically be assumed to beat a good structured static model.

Hamiltonian-inspired networks are intellectually interesting, but they currently look less aligned with the available measurements than Fourier, harmonic, or Laplacian hybrids.

`Lightweight Transformer` and `Neural ODE` should remain visible as low-priority exploratory branches, but they should not displace the main roadmap unless later evidence clearly justifies them.

`Mixture-of-Experts / Regime-Conditioned Model` should remain visible as an added practical family because it is more likely than many other missing candidates to help under heterogeneous operating regimes.

## Involved Components

- `README.md`
  Main project document that must reference this planning note.
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
  Analytical basis for future physics residual construction.
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
  Main reference for ML compensation and TwinCAT deployment constraints.
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
  Practical project workflow, harmonic selection, and PLC-side notes.
- `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`
  Meaning of valid windows, zeroing, and angular signal interpretation.
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
  This technical planning document.
- Future implementation targets after approval:
  - `scripts/models/`
  - `scripts/training/`
  - `config/training/`
  - `doc/reports/campaign_plans/`
  - `doc/reports/campaign_results/`

## Implementation Steps

1. Create this technical planning document and register it in `README.md`.
2. Wait for explicit user approval before modifying any implementation code or training configuration.
3. Define a common evaluation protocol for all candidate families:
   - same train/validation/test splits;
   - same valid-window handling;
   - same primary TE metrics;
   - same operating-condition generalization checks.
4. Implement the static structured baselines first:
   - harmonic regression;
   - periodic-feature MLP;
   - residual MLP over structured baseline.
5. Evaluate whether temporal context is useful with the lowest-risk temporal approach first:
   - lagged-feature MLP;
   - then `GRU` / `LSTM`;
   - then `TCN`.
6. Implement the hybrid structured family:
   - Fourier-feature network;
   - harmonic-head network;
   - Laplacian or derivative regularization.
7. Compare the best standard and hybrid models on accuracy, interpretability, runtime cost, and PLC export viability.
8. Prepare a dedicated PINN formulation document that defines:
   - chosen states and inputs;
   - physical residual equations;
   - boundary and periodic constraints;
   - collocation strategy;
   - loss weighting and normalization.
9. After that formulation is approved, create the first PINN implementation and the related campaign-planning report before any training execution.
