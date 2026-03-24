# FeedForward Network Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Feedforward network | A neural network with one-way information flow from input to output. | MLP, dense network | Sequence model |
| Point-wise sample | One TE measurement represented as one input-output pair. | Single point | Whole curve |
| Dense layer | A layer where every output unit connects to every input unit. | Linear layer | Convolution |
| Activation function | Nonlinear transform applied after a linear layer. | Nonlinearity | Loss function |
| Normalization | Rescaling inputs or targets using train-set statistics. | Scaling | Data leakage |
| Baseline | Reference model used for comparison with later architectures. | Reference model | Weak model |
| Scalar regression output | Single numeric prediction returned by the model. | Single output | Classification label |
| Inductive bias | The structural preference built into the model design. | Structural prior | Shortcut |

