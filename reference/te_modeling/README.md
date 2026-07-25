# Transmission-Error Modeling Reference Library

This directory contains the deduplicated source package imported from
`.temp/sharepoint_documents/` on `2026-07-25`.

## Library Structure

- `bibliography/hysteresis_and_backlash/`: joint hysteresis, nonlinear
  elasticity, friction, and sensorless compensation.
- `bibliography/harmonic_transmission_error/`: spatially periodic kinematic
  error and Fourier-based compensation.
- `bibliography/lookup_table_compensation/`: offline joint-error
  identification and correction.
- `bibliography/machine_learning_compensation/`: state-dependent TE regression
  and real-time compensation.
- `bibliography/polynomial_fourier/`: the Bauer polynomial-Fourier paper and
  the internal implementation note.
- `theoretical_mechanics/`: kinematic, dynamic, contact, tolerance, wear,
  efficiency, and FEA formulations for RV and cycloidal reducers.
- `implementations/mmt_linkage_matlab/`: simplified MMT linkage diagnostic.
- `implementations/polynomial_fourier_te_predictor_matlab/`: MATLAB ONNX
  harmonic-coefficient predictor and five experimental curves.
- `source_inventory.yaml`: content hashes, sizes, and duplicate dispositions.

## Deduplication

The imported package contained 48 files. Thirty-one unique files are stored in
this directory. Seventeen byte-identical files were not copied:

- the MMT paper already exists as `reference/MMT_TEModeling.pdf`;
- 16 ONNX models already exist in the recovered RCIM paper asset package.

The exact source-to-canonical mapping is recorded in
`source_inventory.yaml`.

## Interpretation Rule

This library contains several different evidence classes:

- empirical mathematical curve models;
- analytical and quasi-static physical models;
- dynamic and electromechanical models;
- numerical and finite-element models;
- data-driven surrogate and compensation methods;
- reference implementations.

Their presence here does not make every equation a valid PINN residual.
Candidate equations must still pass unit, observability, identifiability,
causality, and falsification checks.
