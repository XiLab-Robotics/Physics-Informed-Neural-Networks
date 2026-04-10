# RCIM Paper Asset Recovery And Reference Integration

## Overview

This document defines how the newly recovered paper assets from the RCIM
ML-compensation work should be analyzed and integrated into the repository
reference surface.

The recovered material currently staged under `.temp/` includes:

- exact paper ONNX model exports under `.temp/paper_models/0-onnxFiles_paper/`;
- original paper pipeline code under `.temp/paper_models/0_code/`;
- likely newer code snapshots under `.temp/ML-model-training 1/`;
- backup code, ONNX variants, and TwinCAT XML exports under
  `.temp/paper_models/backup/`;
- a large `instance_v1` pickle archive under `.temp/paper_models/instance_v1/`.

The repository already has the paper PDF and summary, but it does not yet have
a dedicated, organized reference area for the recovered exact assets used in
the paper workflow.

## Technical Approach

The integration should create a paper-specific reference root instead of
spreading models, scripts, and deployment artifacts across unrelated existing
folders.

The intended structure is:

- `reference/rcim_ml_compensation_recovered_assets/`
- `reference/rcim_ml_compensation_recovered_assets/README.md`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release/`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/`
- `reference/rcim_ml_compensation_recovered_assets/code/backup_legacy/`
- `reference/rcim_ml_compensation_recovered_assets/deployment/twincat_xml/`
- `reference/rcim_ml_compensation_recovered_assets/backup/`
- `reference/rcim_ml_compensation_recovered_assets/data/instance_archives/`

The integration pass should not treat every recovered file as equally
important. It should classify the material into:

- primary reference artifacts;
- secondary backup artifacts;
- heavy archival artifacts that need explicit storage policy notes.

The expected classification is:

- `0-onnxFiles_paper`: primary reference models;
- `0_code`: primary reference code for the paper pipeline;
- `ML-model-training 1`: primary candidate for the latest recovered code
  snapshot;
- `backup/Code` and `backup/XML Files_TwinCAT`: secondary but important
  reference material;
- `backup/onnxFiles`: secondary backup ONNX bundles;
- `instance_v1`: heavy archive that must be documented carefully because it
  contains about `913` pickle files for about `4.68 GB`.

The analysis already indicates that `instance_v1` is likely an instance or
signal archive rather than a model archive, because the filenames follow the
pattern `rpm / torque / deg`, for example
`100.0rpm500.0Torque30.0deg.pickle`.

The ONNX area also contains at least one evident duplicate artifact:

- `RF/ampl/RandomForestRegressor_ampl240.onnx`
- `RF/ampl/RandomForestRegressor_ampl240 (1).onnx`

That duplicate should be preserved as recovered evidence, but explicitly
documented in the reference README and inventory instead of being silently
collapsed.

Because the `instance_v1` archive is large, the integration plan should record
that one of the following repository-safe approaches must be used during the
approved implementation:

- Git LFS tracking for the archived pickle subtree;
- or a manifest-based integration if full Git tracking is judged too heavy
  during the implementation pass.

The implementation should also create a dedicated reference README that:

- explains the provenance of each recovered subtree;
- distinguishes exact paper assets from later code snapshots and from backup
  material;
- explains which code snapshot appears to be the closest to the paper release;
- documents the archive policy for the heavy pickle subtree;
- explains how these artifacts relate to the repository Track 1 paper-faithful
  reimplementation.

## Involved Components

- `.temp/paper_models/0-onnxFiles_paper/`
- `.temp/paper_models/0_code/`
- `.temp/ML-model-training 1/`
- `.temp/paper_models/backup/`
- `.temp/paper_models/instance_v1/`
- `reference/`
- `doc/README.md`

Repository documents already relevant to the interpretation:

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Implementation Steps

1. Create the new paper-specific reference root under `reference/`.
2. Promote the exact ONNX models into a clearly named model subtree.
3. Promote the original recovered paper code into a dedicated original-pipeline
   subtree.
4. Promote `ML-model-training 1` into a latest-snapshot subtree, clearly
   labeled as a recovered later code version rather than the exact paper
   release.
5. Promote useful backup code, ONNX variants, and TwinCAT XML files into
   clearly separated backup and deployment subtrees.
6. Inspect the heavy `instance_v1` archive and integrate it with an explicit
   storage policy and inventory notes.
7. Create the new reference README describing provenance, organization, and
   usage guidance for the recovered assets.
8. Add a short canonical index reference so the new recovered-paper asset root
   is discoverable from the repository documentation surface.
