# SharePoint TE Reference Library Ingestion And Synthesis

## Overview

This document proposes the controlled ingestion, deduplication, organization,
and scientific analysis of the material staged under:

- `.temp/sharepoint_documents/`.

The staging package currently contains 48 files in 9 directories, totaling
137,242,651 bytes:

| File type | Count |
| --- | ---: |
| PDF | 19 |
| ONNX | 16 |
| MATLAB | 7 |
| CSV | 6 |

The package covers:

- hysteresis and backlash;
- harmonic and Fourier-series transmission-error modeling;
- lookup-table and machine-learning compensation;
- the polynomial-Fourier method described in `Chris_Paper.pdf`;
- theoretical RV and cycloidal-reducer mechanics;
- the MMT paper and companion MATLAB linkage model;
- a MATLAB TE predictor that reconstructs curves from ONNX-predicted harmonic
  amplitudes and phases;
- five experimental TE curve files;
- a three-page OneNote export describing the Fourier Series plus Polynomial
  implementation.

The initial SHA-256 audit found no duplicates inside the staging package and 17
byte-identical files already present under `reference/`:

- `3-Theoretical/MMT_TEModeling.pdf` is identical to
  `reference/MMT_TEModeling.pdf`;
- all 16 ONNX files in `TE_Predictor_Matlab_PB/` are identical to canonical
  assets already stored under
  `reference/rcim_ml_compensation_recovered_assets/models/`.

These files will not be copied a second time. Their staging paths, hashes, and
canonical repository locations will be recorded in a provenance manifest.

This work is a source-library and documentation task. It does not authorize
model implementation, training, registry changes, or campaign execution. The
active campaign state is closed and its protected-file list is empty. No
subagent is planned.

## Technical Approach

### Immutable inventory and duplicate control

Before moving files, create a complete source manifest containing:

- original staging-relative path;
- byte size;
- SHA-256 hash;
- source category;
- duplicate status;
- canonical target or existing canonical path;
- final normalized filename;
- analysis status;
- notes about dependencies or provenance.

Deduplication will be content-based. Filename equality alone will not be used
as proof. Exact duplicates will retain one canonical repository copy and one
manifest record for every source occurrence.

The move will preserve all unique material. Staging duplicates will be removed
only after their byte-identical canonical targets and manifest records have
been reverified. The operation will use explicit resolved paths inside
`.temp/sharepoint_documents/` and `reference/`.

### Reference organization

Create a dedicated domain root:

- `reference/te_modeling/`.

The proposed organization is:

```text
reference/te_modeling/
|-- README.md
|-- source_inventory.yaml
|-- bibliography/
|   |-- hysteresis_and_backlash/
|   |-- harmonic_transmission_error/
|   |-- lookup_table_compensation/
|   |-- machine_learning_compensation/
|   `-- polynomial_fourier/
|-- theoretical_mechanics/
|   |-- kinematics_and_transmission_error/
|   |-- dynamics_hysteresis_and_efficiency/
|   `-- numerical_and_fea_models/
`-- implementations/
    |-- mmt_linkage_matlab/
    `-- polynomial_fourier_te_predictor_matlab/
```

PDF filenames will use descriptive, stable English names based on verified
title, author, year, and topic rather than publisher download identifiers such
as `1-s2.0-*`. Repository-relative paths and source filenames will remain in
the inventory for traceability.

The MMT MATLAB implementation will keep its scripts and experimental curve
together while linking to the existing canonical MMT PDF. The polynomial-
Fourier MATLAB implementation will keep its MATLAB scripts and five experiment
files together. Its duplicate ONNX dependencies will be referenced through a
dependency manifest instead of being copied.

### Scientific reading and extraction

Every PDF will be read in full. Text extraction will be combined with visual
inspection of equation, table, diagram, and result pages. Poppler is not
currently available in the shell PATH, so the implementation will use the
available PyMuPDF renderer and text extractor unless Poppler becomes available.
The three-page OneNote export requires visual inspection because its first page
does not expose useful extracted text.

Each source analysis will separate:

1. source-backed claims;
2. equations, symbols, units, assumptions, and boundary conditions;
3. experimental or numerical validation;
4. repository-implemented facts;
5. proposed PINN implications;
6. unavailable variables and identifiability risks;
7. open questions and falsification tests;
8. TwinCAT and PLC implications.

Particular attention will be assigned to:

- `Chris_Paper.pdf`, whose verified title is
  `Modeling Load-, Velocity-, and Temperature-Dependent Transmission Errors of
  Cycloidal Drives for Industrial Robots Using Fourier Series`;
- `Fourier Series + Polynomial.pdf`;
- `TE_Predictor_Matlab_PB/`;
- the theoretical RV and cycloidal-reducer mechanics papers;
- `3-Theoretical/MMT_Linkage_TEModel/`.

The Chris paper, OneNote export, MATLAB predictor, existing PLC Polynomial
Fourier Series code, and current repository summaries will be cross-checked as
one evidence family while preserving their distinct provenance. The analysis
must determine precisely:

- the Fourier reconstruction equation;
- the selected harmonic orders;
- how amplitudes and phases depend on speed, torque, and temperature;
- where polynomial regression is used and where ONNX regressors replace it;
- coefficient provenance and fit domain;
- interpolation or extrapolation behavior;
- direction handling;
- why the method predicts the current dataset well;
- which parts are empirical mathematics and which are physically defensible;
- how the formulation could become an analytical component, constraint, or
  baseline for a full PINN.

### Documentation outputs

Create a layered documentation package:

- `reference/te_modeling/README.md` for source-library navigation;
- `reference/te_modeling/source_inventory.yaml` for provenance and
  deduplication;
- a high-level library summary under `doc/reference_summaries/`;
- a dedicated polynomial-Fourier and MATLAB predictor summary;
- a dedicated MMT linkage MATLAB summary;
- thematic summaries for hysteresis and backlash, harmonic transmission error,
  ML compensation, and theoretical RV mechanics;
- detailed per-source evidence notes under the Wave 5.2 full-PINN analysis
  tree;
- a cross-reference formulation matrix connecting equations and observable
  variables to candidate PINN residuals or constraints;
- updates to the Wave 5.2 physics reference-intake register;
- updates to `reference/README.md` and `doc/README.md`.

Historical summaries for the existing MMT, RCIM compensation, and Machine
Learning Report sources will be preserved. New analysis will link to them and
extend them only where the imported material provides new evidence.

### PINN relevance classification

Each extracted formulation will receive one evidence-backed status:

- analytical residual candidate;
- compatibility or boundary constraint candidate;
- differentiable semi-analytical baseline;
- causal feature candidate;
- validation-only diagnostic;
- deployment reference;
- deferred for missing physical inputs;
- rejected for incompatibility or leakage risk.

Publication authority or predictive fit alone will not be sufficient for PINN
adoption. Equations must pass unit, observability, identifiability, causal
availability, and falsification gates.

## Involved Components

Source staging:

- `.temp/sharepoint_documents/0-Bibliography/`;
- `.temp/sharepoint_documents/3-Theoretical/`;
- `.temp/sharepoint_documents/3-Theoretical/MMT_Linkage_TEModel/`;
- `.temp/sharepoint_documents/TE_Predictor_Matlab_PB/`;
- `.temp/sharepoint_documents/Fourier Series + Polynomial.pdf`.

Existing canonical references and implementations:

- `reference/MMT_TEModeling.pdf`;
- `reference/RCIM_ML-compensation.pdf`;
- `reference/Report Machine Learning.pdf`;
- `reference/rcim_ml_compensation_recovered_assets/`;
- `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`;
- `doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`;
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`;
- `doc/reference_summaries/04_Machine_Learning_Report_Project_Summary.md`.

Planned canonical outputs:

- `reference/te_modeling/`;
- `doc/reference_summaries/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/full_pinn_program/[2026-07-25]/physics_reference_intake_register.md`;
- `reference/README.md`;
- `doc/README.md`;
- the canonical Sphinx source tree if the new reference summaries enter portal
  scope.

The working tree already contains the approved, uncommitted Wave 5.2 roadmap
reorganization. This task will preserve and extend those changes without
reverting or overwriting them.

## Implementation Steps

1. Register this technical document from `doc/README.md`.
2. Wait for explicit user approval before moving or documenting the staged
   source package.
3. Generate the complete SHA-256 inventory and final path map.
4. Verify all 17 known exact duplicates and search for semantic or renamed
   duplicates through title, DOI, author, year, and content checks.
5. Create `reference/te_modeling/` and its topic structure.
6. Move each unique source to its normalized canonical target.
7. Record duplicate source paths as canonical references without copying their
   payloads.
8. Reverify source and target hashes, file counts, dependency paths, and staging
   residue before removing verified duplicate staging copies.
9. Read all PDFs completely and visually inspect the equation, figure, table,
   and result pages.
10. Audit the MMT and polynomial-Fourier MATLAB code, experimental curves,
    ONNX dependency mapping, and existing PLC implementation.
11. Create the per-source notes, thematic syntheses, implementation summaries,
    and cross-formulation PINN matrix.
12. Update the Wave 5.2 reference-intake register, reference indexes, and
    documentation indexes.
13. Run Markdown warning checks, Markdownlint, final-newline checks, path and
    hash verification, `git diff --check`, and warning-free Sphinx validation
    if portal-backed documentation changes.
14. Check individual file sizes and aggregate Git payload risk before any later
    commit.
15. Stop without committing and report the completed ingestion and synthesis.
