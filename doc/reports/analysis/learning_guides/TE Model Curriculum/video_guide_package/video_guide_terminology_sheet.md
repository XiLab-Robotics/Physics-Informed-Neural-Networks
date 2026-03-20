# TE Model Curriculum Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Model family | Group of architectures sharing the same main modeling idea. | Architecture family | Single model run |
| Baseline | Simple or reference model used for comparison. | Reference model | Weak model by default |
| MLP | Feedforward dense network with layered nonlinear transformations. | Feedforward network | Sequence model |
| Harmonic regression | Structured model that fits sinusoidal basis components to periodic behavior. | Harmonic baseline | Generic Fourier network |
| Periodic feature network | Neural model that first expands inputs with periodic features. | Periodic-feature model | Harmonic regression itself |
| Residual harmonic network | Hybrid model that combines structured harmonic content with a learned residual branch. | Residual hybrid | Two unrelated models |
| Tree-based benchmark | Non-neural decision-tree ensemble used as a comparison baseline. | Tree regressor baseline | Temporal neural model |
| Lagged-feature regressor | Model that uses previous values or lagged features as extra inputs. | NARX-style regressor | Recurrent network |
| GRU | Gated recurrent unit sequence model. | GRU sequence model | Generic memory cell |
| LSTM | Long short-term memory recurrent sequence model. | LSTM sequence model | Same as GRU |
| TCN | Temporal convolutional network using convolutions over sequence windows. | Temporal CNN | Dense MLP |
| PINN | Physics-informed neural network that includes physical constraints in the learning objective. | Physics-informed model | Guaranteed physical simulator |
| Planned family | Architecture direction identified for future implementation or study. | Roadmap family | Already implemented model |
| Implemented family | Architecture with repository code and supporting documentation already present. | Available family | Future idea |
