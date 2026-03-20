# Harmonic Regression Video Guide Narration Outline

## Opening

Introduce the model as the first explicitly periodic TE architecture. The viewer should immediately understand that the model is not just another neural network with a different name.

## Chapter 1 - The Periodic Problem

- explain why TE is periodic in angular position;
- contrast this with the generic MLP baseline.

## Chapter 2 - The Harmonic Series Idea

- introduce sine and cosine basis terms;
- explain truncation and harmonic order;
- connect the math to the signal shape.

## Chapter 3 - Static And Conditioned Variants

- explain the shared coefficient version;
- explain the linear-conditioned version;
- note how operating variables shift the coefficients.

## Chapter 4 - Why It Is Interpretable

- discuss coefficient inspection;
- explain why the model is easier to reason about than a dense network.

## Chapter 5 - Repository Implementation

- identify the harmonic regression module;
- explain the factory registration;
- explain how the shared trainer passes raw angle and normalized conditions.

## Closing

Summarize the model as a compact, structured baseline that declares periodicity explicitly and serves as the reference point for later hybrid architectures.
