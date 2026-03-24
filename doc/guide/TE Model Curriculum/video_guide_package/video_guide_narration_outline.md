# TE Model Curriculum Video Guide Narration Outline

## Opening

Once the basics of neural networks and evaluation are clear, the next question is architectural choice. This guide explains why the TE problem is studied through a curriculum of model families, starting from interpretable baselines and moving toward models with stronger periodic, temporal, hybrid, and physics-informed structure.

## Chapter 1 - Why A Curriculum Exists

- Explain that one architecture rarely answers every modeling need.
- State the TE challenge: periodic structure, operating-condition dependence, and possible temporal effects.
- Introduce the idea of staged complexity.

## Chapter 2 - Baseline Families

- Present MLP as the general nonlinear baseline.
- Present harmonic regression as the structured periodic baseline.
- Explain why these two baselines anchor later comparisons.

## Chapter 3 - Periodic And Hybrid Families

- Explain periodic feature networks as a way to feed periodic structure into a neural model.
- Explain residual harmonic networks as a decomposition into structured part plus learned correction.
- Mention strengths and tradeoffs of explicit structure.

## Chapter 4 - Benchmark And Memory-Aware Families

- Place tree-based models as fast, non-neural baselines.
- Explain lagged-feature MLPs as the first step toward temporal context.
- Explain GRU, LSTM, and TCN as sequence-aware families with increasing temporal modeling intent.

## Chapter 5 - Advanced Structured Directions

- Briefly explain mixture-of-experts, Fourier-feature, harmonic-head, and smoothness-constrained ideas.
- Explain that these families explore stronger inductive bias without immediately jumping to the heaviest models.

## Chapter 6 - Frontier Directions

- Briefly introduce SIREN, lightweight transformer, state-space model, neural ODE, and PINN.
- Stress that these are roadmap directions and should be discussed with scope discipline.

## Chapter 7 - Study Order

- Recommend learning order from feedforward and harmonic models toward periodic, residual, temporal, and finally physics-informed models.
- Frame the curriculum as cumulative, not a list of disconnected options.

## Closing

End by reminding the viewer that architecture choice should follow problem structure, evaluation discipline, and deployment constraints rather than novelty alone.
