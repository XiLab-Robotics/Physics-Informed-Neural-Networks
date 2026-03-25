# Harmonic Regression Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Harmonic regression | Regression model that uses sine and cosine basis terms over angle. | Periodic regression | Generic neural network |
| Harmonic basis | Set of sine and cosine functions used to represent periodic signals. | Periodic basis | Feature noise |
| Coefficient vector | Learned weights that scale the harmonic basis terms. | Harmonic weights | Hidden layer |
| Static mode | One shared coefficient vector for all samples. | Global mode | Unconditioned guess |
| Linear-conditioned mode | Coefficients adjusted by a linear projection of operating features. | Conditioned mode | Temporal mode |
| Truncated series | Finite harmonic expansion with a chosen order. | Finite basis | Infinite model |
| Interpretability | Ability to inspect the model in terms of human-readable coefficients. | Readability | Simplicity only |
