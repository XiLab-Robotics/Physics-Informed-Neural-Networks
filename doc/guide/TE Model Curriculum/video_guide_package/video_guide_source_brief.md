# TE Model Curriculum Video Guide Source Brief

## Audience

- readers who already understand the basics of neural networks and dataset splits;
- learners who want to understand why the repository studies several TE model families instead of one universal architecture;
- students who need a roadmap from baseline models to advanced architectures.

## Video Goal

Explain the model-family progression for TE prediction, starting from MLP and harmonic regression, then moving through periodic, residual, temporal, hybrid, and physics-informed directions while clearly separating implemented baselines from planned research steps.

## Target Depth

- explain each family at a conceptual and practical level;
- remain accessible to an early university audience;
- avoid implementation details that belong in family-specific reports.

## Required Chapter Order

1. Why a curriculum of model families is needed.
2. MLP / feedforward network.
3. Harmonic regression.
4. Periodic feature network.
5. Residual harmonic network.
6. Tree-based benchmark.
7. Lagged-feature MLP / NARX-style regressor.
8. GRU, LSTM, and TCN.
9. Mixture, Fourier-feature, harmonic-head, and smoothness-constrained variants.
10. SIREN, transformer, state-space, neural ODE, and PINN directions.
11. Suggested study order and repository roadmap.

## Required Takeaways

- The repository starts from strong baselines before moving to heavier sequence or physics-informed models.
- Different model families capture different assumptions about periodicity, memory, and structure.
- Harmonic and feedforward baselines are not trivial; they are reference points for every later comparison.
- Planned families must be described as planned unless separately documented as implemented.

## Concepts That Must Stay Brief

- exhaustive tensor-shape walkthroughs;
- optimizer hyperparameter details;
- mathematical derivations for every temporal model.

## Concepts That Must Not Be Omitted

- reason each family exists;
- main strength and weakness in the TE context;
- study order;
- implemented-versus-planned boundary.
