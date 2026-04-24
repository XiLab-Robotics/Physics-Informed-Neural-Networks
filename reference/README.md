# Reference Root

This folder contains the repository reference surface used to guide design,
implementation, deployment constraints, and coding style decisions.

## Main Reference PDFs

- [RCIM_ML-compensation.pdf](./RCIM_ML-compensation.pdf)
  Main paper reference for ML-based TE harmonic prediction and online
  compensation.
- [MMT_TEModeling.pdf](./MMT_TEModeling.pdf)
  Main analytical reference for equivalent-mechanism TE modeling.
- [Report Machine Learning.pdf](./Report%20Machine%20Learning.pdf)
  Practical ML and workflow reference recovered with the project material.
- [SpiegazioneSerieDati.pdf](./SpiegazioneSerieDati.pdf)
  Data-series explanation reference for the measured variables and acquisition
  interpretation.
- [Guida.pdf](./Guida.pdf)
  Additional project reference guide recovered with the source material.

## Reference Codebases

- [codes/](./codes/)
  Imported external reference codebases used for coding-style and
  implementation-pattern study.

## Recovered RCIM Paper Assets

- [rcim_ml_compensation_recovered_assets/README.md](./rcim_ml_compensation_recovered_assets/README.md)
  Organized repository-owned copy of the recovered RCIM paper assets currently
  available in the repository. This recovered root remains generic because it
  contains generic recovered code snapshots plus forward-only benchmark
  artifacts such as the shipped `Fw` dataframe and exact ONNX paper release.

## Usage

- Treat this folder as read-mostly reference material.
- Use the canonical summaries under `doc/reference_summaries/` when you need
  repository-facing conclusions rather than raw source artifacts.
- Use the recovered RCIM asset package when you need exact paper-era models,
  recovered paper code, or deployment-facing backup exports.
- Treat the currently stored recovered RCIM exact ONNX release and shipped
  `Fw` dataframe as `forward-only` unless a future repository update
  explicitly adds the missing backward-side recovered assets.
