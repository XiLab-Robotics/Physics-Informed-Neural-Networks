# Neural Network Foundations Video Guide Source Brief

## Audience

- beginners who do not yet know what a neural network is;
- technical students moving from intuitive understanding to first university-level formalism;
- readers who will later study TE-specific model reports in this repository.

## Video Goal

Explain what a neural network is, how it grows from linear regression to a multilayer perceptron, how learning happens through loss minimization and gradient-based updates, and why this matters for the TE regression problem.

## Target Depth

- start with plain-language intuition;
- introduce compact mathematical notation only after the intuition is established;
- stop before advanced optimization theory, Hessians, or statistical learning proofs.

## Required Chapter Order

1. Why supervised learning is the starting point.
2. Linear regression as the simplest predictive model.
3. A neuron as weighted sum plus bias plus activation.
4. From one neuron to one hidden layer to an MLP.
5. Forward propagation and prediction generation.
6. Loss functions and what the model is trying to minimize.
7. Gradient descent and backpropagation.
8. Batches, epochs, normalization, and overfitting.
9. TE-specific interpretation of inputs and outputs.

## Required Takeaways

- A neural network is not magic; it is a parameterized function adjusted from data.
- The jump from linear regression to a neuron comes from the activation function.
- The jump from one neuron to an MLP comes from layered feature transformations.
- Training means iteratively reducing a loss on training data.
- Good performance requires generalization, not only low training loss.
- In this repository, the neural network is learning TE-related mappings from operating conditions and engineered features.

## Concepts That Must Stay Brief

- biological-neuron analogies;
- matrix calculus details;
- optimizer variants beyond a short mention of gradient descent and Adam;
- historical timeline of neural networks.

## Concepts That Must Not Be Omitted

- weighted sum, bias, activation;
- hidden layers;
- loss;
- backpropagation as the gradient-computation mechanism;
- train versus generalize;
- TE context.
