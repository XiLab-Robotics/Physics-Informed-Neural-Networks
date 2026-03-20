# Residual Harmonic Network Video Guide Source Brief

## Audience

- readers who understand the harmonic and periodic-feature baselines;
- learners who want the clearest hybrid explanation in the architecture series;
- viewers interested in explicit structured-plus-residual decomposition.

## Video Goal

Explain how the residual harmonic network splits TE prediction into a structured harmonic branch and a learned residual branch, then adds the two together for the final output.

## Target Depth

- conceptual explanation first;
- decomposition mechanics second;
- implementation details last.

## Required Chapter Order

1. Why a hybrid model is needed.
2. What the structured harmonic branch does.
3. What the residual neural branch does.
4. How the two branches are combined.
5. What frozen versus joint training means.
6. Why the model is more interpretable than a plain MLP.
7. How the repository implements the architecture.
8. Why the model matters for the TE curriculum.

## Required Takeaways

- TE can be split into a periodic backbone plus residual correction;
- the model is explicitly additive;
- the harmonic branch preserves structure;
- the residual branch preserves flexibility;
- auxiliary outputs make the model more inspectable.

## Concepts That Must Stay Brief

- advanced multi-branch optimization theory;
- branch conflict theory;
- physics-informed loss details not present in this model.

## Concepts That Must Not Be Omitted

- structured branch;
- residual branch;
- additive merge;
- freeze option;
- auxiliary outputs;
- hybrid interpretation.
