# RCIM Retuned Backward HGBM Reference Models

This archive stores the retuned recovered-original RCIM target-level models for
the `backward` branch.

Archive contents:

- `reference_inventory.yaml`
- `onnx/amplitude/`
- `onnx/phase/`
- `python/amplitude/`
- `python/phase/`
- `data/`
- `dataset_snapshot_manifest.yaml`
- `source_runs/<run_instance_id>/`

Selection rule:

- retuned hyperparameters come from the accepted `Retune` stage;
- `Eval` and `Export` stages are the accepted downstream recovery surfaces;
- every target must expose both ONNX and Python pickle artifacts;
- any source export with ONNX errors is rejected for this curated archive.

Provenance summary:

- direction label: `backward`
- paper family: `HGBM`
- implementation family: `HGBM`
- retune source bundle: `2026-05-12-11-08-07__bw_retune_bundle`
- eval source bundle: `2026-05-12-18-22-07__bw_eval_bundle`
- export source bundle: `2026-05-12-18-22-27__bw_export_bundle`
- archived target count: `20`
- ONNX exported target count: `20`
- Python pickle target count: `20`
- ONNX export error count: `0`
