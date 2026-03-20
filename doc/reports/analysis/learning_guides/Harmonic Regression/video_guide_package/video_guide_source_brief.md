# Harmonic Regression Video Guide Source Brief

## Audience

- readers who already understand the basic feedforward baseline;
- learners who want to see why TE is a periodic modeling problem;
- viewers who need an interpretable structured alternative to the MLP baseline.

## Video Goal

Explain how harmonic regression represents TE as a truncated periodic series, how the coefficients are learned, why conditioning matters, and why the model is more interpretable than a generic neural network.

## Target Depth

- clear conceptual explanation first;
- mathematical form second;
- implementation details last.

## Required Chapter Order

1. Why periodicity matters for TE.
2. What harmonic regression is.
3. How sine and cosine basis terms are built.
4. How the coefficients are learned.
5. Static versus conditioned modes.
6. Why the model is more interpretable than an MLP.
7. How the repository implements the model.
8. Why the model is a structured baseline.

## Required Takeaways

- the model encodes periodicity explicitly;
- coefficients determine the TE shape;
- the conditioned mode adjusts coefficients from operating variables;
- the model is compact and readable;
- the model is the first explicitly TE-structured architecture in the series.

## Concepts That Must Stay Brief

- trigonometric derivations beyond the core series form;
- optimization details;
- Fourier theory history.

## Concepts That Must Not Be Omitted

- harmonic basis;
- coefficient vector;
- static and linear-conditioned modes;
- angular position in radians;
- interpretability advantage.
