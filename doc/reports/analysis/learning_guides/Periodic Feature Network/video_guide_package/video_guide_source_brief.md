# Periodic Feature Network Video Guide Source Brief

## Audience

- readers who already know the baseline MLP and harmonic regression;
- learners who want a middle-ground architecture with explicit periodic features and neural flexibility;
- viewers comparing structured input engineering with structured output decomposition.

## Video Goal

Explain how the periodic feature network converts angular position into periodic basis features, concatenates them with operating variables, and uses a standard MLP as the final regressor.

## Target Depth

- conceptual explanation first;
- architectural explanation second;
- implementation mapping last.

## Required Chapter Order

1. Why a middle-ground model is useful.
2. How periodic features are built.
3. How those features are fed into the MLP.
4. Why this is different from harmonic regression.
5. Why this is different from the baseline MLP.
6. How the repository implements the architecture.
7. Why the model is useful in the TE context.

## Required Takeaways

- periodicity is made explicit in the input map;
- the final regressor is still a feedforward network;
- the model can learn nonlinear interactions more flexibly than harmonic regression;
- the model is more structured than the baseline MLP;
- it is the middle option between generic and fully structured approaches.

## Concepts That Must Stay Brief

- deep learning regularization theory;
- periodic basis derivations beyond the required sine and cosine expansion;
- optimizer details.

## Concepts That Must Not Be Omitted

- periodic feature expansion;
- concatenation with operating-condition channels;
- MLP backend;
- repository-specific contextual forward path;
- middle-ground interpretation.
