# RCIM Retuned Paper Reference Models

This folder stores curated recovered-original RCIM models generated from the
retuned hyperparameter workflow.

Direction branches:

- `forward/`
- `backward/`

Each populated family archive follows the same structure used by
`models/paper_reference/rcim_original/`:

- `<direction>/<family>_reference_models/README.md`
- `<direction>/<family>_reference_models/reference_inventory.yaml`
- `<direction>/<family>_reference_models/onnx/amplitude/`
- `<direction>/<family>_reference_models/onnx/phase/`
- `<direction>/<family>_reference_models/python/amplitude/`
- `<direction>/<family>_reference_models/python/phase/`
- `<direction>/<family>_reference_models/data/`
- `<direction>/<family>_reference_models/dataset_snapshot_manifest.yaml`
- `<direction>/<family>_reference_models/source_runs/<run_instance_id>/`

Archive acceptance rule:

- every promoted family-direction archive has `20` ONNX files;
- every promoted family-direction archive has `20` Python pickle files;
- no promoted family-direction archive contains ONNX export-error sidecars.
