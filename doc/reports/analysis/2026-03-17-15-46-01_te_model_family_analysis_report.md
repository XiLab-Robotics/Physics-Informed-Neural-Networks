# TE Model Family Analysis Report

## Overview

This report translates the approved technical roadmap into a more operational analysis for the current RV reducer Transmission Error case study.

The goal is to identify which algorithm families are worth implementing, why they may improve over the current feedforward baseline, and what technical tradeoffs they introduce with respect to:

- TE prediction quality;
- operating-condition generalization;
- harmonic fidelity;
- interpretability;
- TwinCAT / PLC deployment viability;
- implementation and training complexity.

This report should be read together with:

- `doc/technical/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`
- `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`

## Problem Restatement For This Repository

The current repository does not solve a generic scalar regression problem.

The target is the Rotational Transmission Error of an RV reducer measured on a controlled test rig, and the reference material already imposes a specific structure on the problem:

1. TE is the main accuracy indicator.
2. TE depends on angular position and on operating variables such as speed, torque, and oil temperature.
3. The measured TE should be interpreted only inside the valid windows defined by the experiment and by `DataValid`.
4. The physical system contains identifiable harmonic content and stage-coupling behavior.
5. The final model family should remain compatible with compact and inspectable deployment logic.

These points matter because they rule out two simplistic mistakes:

- treating the problem as pure static tabular regression without respecting periodic structure;
- jumping directly into a full PINN without first checking whether simpler structured models already capture most of the useful behavior.

## What A Better Model Must Improve

Relative to the current point-wise feedforward baseline, an improved model should ideally address at least one of the following weaknesses:

### Better Periodic Representation

The target depends strongly on angular position and contains meaningful harmonic components. A stronger model should represent periodic structure more naturally than a generic MLP fed with raw angle alone.

### Better Cross-Condition Generalization

The model should remain reliable when speed, torque, and temperature vary, especially in combinations that are less frequent in the dataset.

### Better Handling Of History-Dependent Effects

If hysteresis, warm-up drift, or sequence-dependent transients exist, a static point-wise model may be structurally incomplete.

### Better Physical Plausibility

The prediction should not only fit the data, but also remain consistent with the known reducer behavior, angular smoothness, and physically meaningful harmonic composition.

### Better Deployment Readiness

A model family that achieves slightly better offline error at the price of poor runtime transparency may still be a worse engineering choice for this project.

## Evaluation Criteria For All Candidate Families

Every candidate should be compared with the same evaluation frame.

### Accuracy Metrics

- MAE and RMSE on valid TE windows;
- per-operating-regime error slices across speed, torque, temperature, and direction;
- error on unseen files and not only on unseen points.

### Harmonic Metrics

- error on dominant TE harmonics;
- phase consistency over angle;
- ability to preserve physically meaningful periodic content instead of only smoothing it away.

### Robustness Metrics

- stability across random seeds;
- sensitivity to sparse operating-condition regions;
- degradation under noisier or partially shifted valid windows.

### Deployment Metrics

- inference complexity;
- parameter count;
- requirement for past context or recurrent state;
- ease of exporting the model or translating it into a compact PLC-side surrogate.

### Scientific Value

- interpretability of the learned representation;
- usefulness for later physics-informed extensions;
- ability to explain which part of the TE is captured structurally and which part remains residual.

## Standard Model Families

## Harmonic Regression

### Principle

Harmonic regression models TE as a sum of sinusoidal components over angular position. The amplitudes, phases, or combined coefficients can be constant or conditioned on the operating variables.

Typical form:

`TE(theta, u) = sum_k a_k(u) * sin(k * theta) + b_k(u) * cos(k * theta)`

where `u` collects speed, torque, temperature, and optionally motion direction.

### Why It Is Strong In This Case Study

This is the cleanest first model because the project references already say that TE frequencies can be linked to physical error sources. That means the harmonic basis is not arbitrary feature engineering. It is already supported by the reducer physics interpretation.

### Main Advantages

- very interpretable;
- directly aligned with frequency-domain compensation logic;
- low inference cost;
- naturally compatible with PLC-oriented deployment;
- useful to expose whether the problem is dominated by a small set of harmonics.

### Main Disadvantages

- limited flexibility when the residual is strongly nonlinear;
- depends on selecting a suitable harmonic set;
- may struggle with local anomalies or cross-condition effects not well expressed through coefficient modulation.

### Recommendation

This should be implemented early and treated as more than a toy baseline. In this project, harmonic regression is a serious candidate because it sits exactly between analytical understanding and practical deployment.

## Feedforward MLP With Explicit Periodic Features

### Principle

A feedforward network predicts TE from the current operating point and angular position, but the input is strengthened with features such as:

- `sin(theta)`, `cos(theta)`;
- higher-order harmonic pairs;
- optionally normalized condition interactions.

### Why It Is Relevant

The repository already has a feedforward path. This family offers the cheapest upgrade path because it preserves the same training logic while giving the network a better representation of angular periodicity.

### Main Advantages

- minimal implementation disruption;
- low training risk;
- low inference latency;
- straightforward comparison with the current baseline.

### Main Disadvantages

- still no explicit temporal memory;
- still mostly black-box in how it combines features;
- may only partially exploit the underlying harmonic structure.

### Recommendation

This is the first neural architecture that should be strengthened. If this model improves significantly over the raw-angle baseline, it will confirm that representation quality matters as much as depth.

## Residual MLP Over Harmonic Or Analytical Baseline

### Principle

A structured baseline first explains the main TE component. A small MLP then learns only the residual:

`TE_pred = TE_structured + TE_residual_network`

### Why It Is Strong

This family is highly suitable for the repository because it keeps the main signal interpretable and delegates only the hard nonlinear residue to the network.

### Main Advantages

- often more sample-efficient than end-to-end black-box regression;
- clean separation between explained structure and unexplained residue;
- easier to justify scientifically;
- easier to deploy than a large unconstrained network.

### Main Disadvantages

- depends on a good structured baseline;
- requires careful data bookkeeping so the residual has the intended meaning.

### Recommendation

This is one of the best near-term candidates in the entire roadmap.

## Tree-Based Standard ML

### Principle

Use models such as random forest or gradient boosting on engineered features.

### Main Advantages

- strong tabular benchmark;
- fast iteration for feature-importance checks;
- useful to test whether neural networks are actually necessary.

### Main Disadvantages

- awkward periodic continuity handling;
- weak alignment with harmonic reconstruction logic;
- less attractive deployment path than compact linear or neural surrogates.

### Recommendation

Keep these models as reference baselines, not as the main target family.

## Sequence-Aware Families

The temporal branch is justified only if the TE depends on recent history and not only on the current state.

That can happen through:

- hysteresis between forward and backward motion;
- thermal drift;
- transient loading behavior;
- unmodeled actuator or reducer-state lag.

## Lagged-Feature MLP / NARX-Style Regressor

### Principle

Construct a fixed window of past samples and feed it into an otherwise static network.

Example:

- current angle and operating variables;
- previous `N` TE values or previous `N` angles;
- optional previous torque or temperature values.

### Why It Matters

This is the lowest-risk way to test whether memory helps. If a lagged-feature model does not outperform the static baseline, a more complex recurrent network becomes harder to justify.

### Main Advantages

- simpler than recurrent models;
- deterministic runtime;
- good short-memory benchmark.

### Main Disadvantages

- manual window design;
- larger input dimension;
- less elegant state handling than recurrent or convolutional temporal models.

### Recommendation

This should come before `LSTM`.

## GRU / LSTM

### Principle

A recurrent network carries a hidden state through the sequence and learns how much past information should be retained.

### Why It Could Help

If the current TE depends on recent system evolution and not just on the instantaneous condition, `LSTM` or `GRU` can capture that dependence directly.

### Main Advantages

- true sequence modeling;
- can capture short and medium-range dependencies;
- relevant when the dataset is organized as ordered curves rather than isolated points.

### Main Disadvantages

- harder training and tuning;
- less interpretable hidden state;
- less convenient PLC-side deployment story;
- risk of adding complexity without real gain if the target is mostly instantaneous.

### Recommendation

`GRU` should be tried before `LSTM` if a lighter recurrent baseline is preferred. `LSTM` becomes more defensible only if longer-memory effects are visible in the data.

## Temporal Convolutional Network

### Principle

Use dilated 1D convolutions over a finite window to model temporal or angular context.

### Why It Is A Serious Alternative

This family often captures local and mid-range dependencies with less training fragility than recurrent networks.

### Main Advantages

- parallelizable training;
- fixed receptive field;
- predictable runtime;
- often a better engineering compromise than recurrent models.

### Main Disadvantages

- still requires window design;
- less intuitive than the simplest lagged-feature approach.

### Recommendation

This is the strongest non-recurrent competitor to `LSTM` for the repository.

## Lightweight Transformer

### Principle

Use a compact attention-based sequence model over short or medium TE windows.

### Why It Remains Low Priority

This family stays in scope, but not in the main execution path, because:

- the useful context length is not yet proven to be large enough to justify attention;
- the repository still has stronger lower-cost temporal candidates such as lagged-feature MLP, `GRU`, `LSTM`, and especially `TCN`;
- deployment and runtime transparency are currently better served by the simpler temporal families.

### Main Advantages

- potentially better modeling of broader context interactions;
- flexible sequence representation if the dataset later expands to richer windows.

### Main Disadvantages

- higher tuning and implementation cost than the main temporal baselines;
- weaker immediate fit with compact deployment goals;
- lower short-term value than the other temporal families already prioritized.

### Recommendation

Keep it as an explicit low-priority exploratory branch after the main temporal wave.

## Structured Hybrid Families Between Standard ML And PINNs

This branch is likely the most valuable scientific middle ground for the project.

It preserves the practical strengths of standard models while injecting problem-specific structure.

## Fourier-Feature Network

### Principle

Map the angular input through a fixed or learned Fourier basis before the main regression block.

### Why It Fits The TE Problem

The target is periodic, and the reference material already indicates that selected frequencies carry physical meaning. Fourier features give the model a representation aligned with that geometry from the start.

### Main Advantages

- excellent inductive bias for periodic signals;
- better angular extrapolation than raw-angle inputs;
- moderate implementation complexity;
- still reasonably exportable.

### Main Disadvantages

- requires frequency-band design;
- may not capture non-periodic drift unless the rest of the model is well designed.

### Recommendation

This is one of the highest-priority hybrid models.

## Harmonic-Head Network

### Principle

The network predicts harmonic coefficients, and TE is reconstructed analytically from them.

### Why It Is Important

This is very close to the actual compensation logic and creates a direct bridge between offline learning and runtime harmonic reconstruction.

### Main Advantages

- interpretable outputs;
- direct harmonic control;
- natural deployment path;
- easier scientific explanation than arbitrary point-wise regression.

### Main Disadvantages

- requires a reliable harmonic dictionary;
- may under-represent highly local residual effects.

### Recommendation

This should be tested together with Fourier-feature models, not treated as a niche variant.

## Laplacian-Regularized Or Smoothness-Constrained Network

### Principle

Train a standard predictor with extra penalties that enforce smoothness or neighborhood consistency over angle or operating-condition space.

The regularization can be applied to:

- first derivatives over angle;
- second derivatives over angle;
- graph-Laplacian consistency among nearby operating conditions.

### Why It Matters

This adds physics-like discipline without requiring the full analytical model. It is especially useful when the data coverage is incomplete and the model would otherwise learn noisy or implausible local oscillations.

### Main Advantages

- low implementation barrier;
- can improve generalization;
- useful bridge toward future derivative-based PINN losses.

### Main Disadvantages

- sensitive regularization tuning;
- too much smoothness can erase real harmonic content.

### Recommendation

This is a strong intermediate step before full PINNs.

## SIREN / Periodic-Activation Network

### Principle

Use sinusoidal activations so the network naturally represents oscillatory functions and their derivatives.

### Main Advantages

- expressive for periodic signals;
- helpful when later derivative computations become central.

### Main Disadvantages

- training sensitivity;
- weaker deployment simplicity than conventional activations.

### Recommendation

Exploratory, but relevant if Fourier-feature models still leave fine harmonic detail unresolved.

## Hamiltonian-Inspired Network

### Principle

Impose energy-structured dynamics or conservative latent evolution.

### Why It Is Not The First Choice

Hamiltonian methods shine when the system state, conjugate variables, and energy structure are explicit. In the current TE compensation setting, the problem is not yet formulated as a fully observed dynamical system with a clear Hamiltonian state.

### Main Advantages

- potentially elegant physical interpretability in the right formulation;
- possible future value if the project expands toward dynamic reducer-state modeling.

### Main Disadvantages

- weak current fit with available measurements;
- high modeling overhead;
- unclear short-term benefit for compensation performance.

### Recommendation

Keep this as a research branch, not as a first implementation target.

## Neural ODE / Continuous-State Hybrid

### Principle

Model the evolution of a latent state continuously over angle or time, then decode that state into TE predictions.

### Why It Remains Low Priority

This family stays in scope, but not in the primary backlog, because the repository still lacks a sufficiently fixed continuous-state formulation:

- the independent variable is not yet fixed cleanly as angle, time, or a mixed formulation;
- the latent state does not yet have a well-defined physical interpretation;
- the expected advantage over simpler temporal or hybrid models is not yet demonstrated.

### Main Advantages

- interesting bridge between sequence learning and future differential or physics-informed formulations;
- potentially useful if later evidence supports continuous-state modeling.

### Main Disadvantages

- heavier training and solver complexity;
- harder validation and deployment path;
- easier to overcomplicate the problem before the main structured baselines are exhausted.

### Recommendation

Keep it as an explicit low-priority exploratory branch after the main hybrid wave and before advanced physics-informed exploration, only if a defensible formulation emerges.

## Full PINNs

## What PINNs Can Add

PINNs are attractive here because the analytical reducer model already suggests explicit constraints:

- transmission-ratio consistency;
- coupling between high-speed and low-speed stage contributions;
- physically meaningful harmonic relations;
- smooth periodic behavior across angular cycles.

If encoded correctly, these constraints can improve generalization and help prevent purely empirical overfitting.

## What Makes PINNs Difficult In This Repository

The hard part is not writing a custom loss function. The hard part is defining the right physical variables and residual equations so that the loss actually has scientific meaning.

There are at least six unresolved design points that must be fixed first:

1. Which variables are direct inputs, which are latent physical quantities, and which are fixed mechanical parameters?
2. Is angle the independent coordinate, or do we need time and speed jointly?
3. Should the network predict total TE directly or decomposed stage contributions?
4. Which equations are strict constraints and which are soft regularizers?
5. How should collocation points be placed across angle and operating conditions?
6. How should the data term and physics term be normalized so one does not dominate the other?

## Advantages Of PINNs

- strongest physical consistency potential;
- natural link to the analytical RV reducer model;
- improved scientific interpretability when the formulation is right;
- better chance of robust extrapolation under limited data.

## Disadvantages Of PINNs

- highest formulation cost;
- most fragile optimization;
- identifiability risk if the measured variables do not support the chosen decomposition;
- easiest family to implement incorrectly while appearing principled.

## Recommendation

Do not start with a PINN implementation immediately.

The correct approach is:

1. identify the best structured non-PINN baselines;
2. determine what residual behavior remains unexplained;
3. only then define the first PINN around that residual structure.

## Comparative Assessment Matrix

| Family | Core Idea | Expected Benefit | Main Risk | Deployment Fit | Priority |
| --- | --- | --- | --- | --- | --- |
| Harmonic regression | Explicit sinusoidal TE model | Maximum interpretability and PLC alignment | Underfitting nonlinear residuals | High | Very high |
| Periodic-feature MLP | Feedforward regression with harmonic inputs | Better angular representation with low complexity | Still no memory | High | Very high |
| Residual MLP | Learn only the unexplained residual | Strong accuracy/interpretability tradeoff | Needs good baseline decomposition | High | Very high |
| Tree-based regression | Tabular non-neural benchmark | Fast baseline and feature inspection | Poor periodic continuity handling | Medium | Medium |
| Lagged-feature MLP | Fixed temporal window without recurrence | Cheap memory test | Manual window design | Medium to high | High |
| GRU / LSTM | Recurrent sequence modeling | Captures history-dependent behavior | Harder training and export | Medium | Medium to high |
| TCN | Convolutional sequence modeling | Better engineering compromise than RNN in many cases | Window tuning still needed | Medium | High |
| Lightweight Transformer | Compact attention-based sequence modeling | Potential broader-context modeling | Higher complexity than other temporal baselines | Medium to low | Low |
| Fourier-feature network | Spectral encoding before regression | Strong periodic inductive bias | Frequency design sensitivity | High | Very high |
| Harmonic-head network | Predict harmonic coefficients directly | Strong interpretability and deployment bridge | Harmonic dictionary limitations | High | Very high |
| Laplacian-regularized network | Smoothness or graph consistency constraints | Better physical plausibility | Over-smoothing risk | High | High |
| SIREN | Periodic activations | Strong fine harmonic expressivity | Sensitive optimization | Medium | Medium |
| Hamiltonian-inspired network | Structured energy-based latent dynamics | Potential long-term physics elegance | Weak fit to current formulation | Low to medium | Low |
| Neural ODE | Continuous-state latent dynamics | Bridge toward continuous and differential modeling | Formulation and solver complexity | Low to medium | Low |
| Full PINN | Data + explicit physics residuals | Maximum physics integration | Highest formulation and training complexity | Medium if designed carefully | Deferred until prerequisites are fixed |

## Recommended Execution Order

## Phase 1. Strong Structured Baselines

Implement first:

1. harmonic regression;
2. periodic-feature MLP;
3. residual MLP over structured baseline.

Why first:

- low implementation cost;
- high scientific value;
- direct relevance to PLC-compatible compensation logic.

## Phase 2. Temporal Validation

Implement next:

1. lagged-feature MLP;
2. `TCN`;
3. `GRU` and then `LSTM` only if sequence dependence is confirmed.

Why second:

- temporal complexity should be earned by evidence, not assumed.

## Phase 3. Hybrid Structured Models

Implement after temporal baselines:

1. Fourier-feature network;
2. harmonic-head network;
3. Laplacian-regularized network;
4. optional `SIREN`.

Why third:

- these models are likely to offer the best middle ground between physics structure and engineering practicality.

## Phase 4. PINN Preparation

Before implementation, prepare a dedicated document that specifies:

- chosen physical states;
- target decomposition;
- residual equations;
- periodic and boundary conditions;
- collocation strategy;
- scaling and weighting rules.

Only after that should the first PINN be implemented.

## Most Likely High-Value Winners

For the current repository stage, the strongest high-value candidates are:

1. harmonic regression;
2. residual MLP over a harmonic or analytical baseline;
3. periodic-feature or Fourier-feature MLP;
4. harmonic-head network;
5. `TCN` if history dependence proves real.

The most likely mistake would be to prioritize a full PINN or a Hamiltonian network before these structured baselines are tested.

## Practical Conclusions

The model search should not be framed as "standard networks versus PINNs."

For this TE case study, the more useful framing is:

- first capture periodic structure explicitly;
- then verify whether memory adds real value;
- then inject smoothness or physics-inspired bias;
- only then write the full physics residuals.

This staged approach is more likely to improve performance, preserve interpretability, and avoid unnecessary complexity.

At the current state of the repository, the best engineering direction is therefore:

- structured baselines first;
- sequence models second;
- hybrid spectral and smoothness-constrained models third;
- full PINNs only after a separate formulation phase for the loss equations and physical residual terms.
