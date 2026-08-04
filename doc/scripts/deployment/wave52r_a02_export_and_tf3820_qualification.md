# Wave 5.2R A02 Export And TF3820 Qualification

## Purpose

This note reproduces the export and static TwinCAT qualification package for
`wave52r_integrated_a02_seed_314159`. The selected A02 path is a fixed-grid
curve composer: it consumes complete global K01 and forward H08 prediction
curves, applies the learned forward-only centered residual, and returns the
final 2048-sample TE curve plus inspectable intermediate tensors.

The package is not a monolithic online predictor. K01 still owns its causal
32-sample recurrent execution, H08 produces its complete forward curve, and
the A02 composer operates only after both curves are available.

## Export And Parity

Run the full 194-condition reconstruction, ONNX Runtime, and independent
float32 PLC-reference check:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/export/wave_5_2r/export_wave52r_a02_composition_and_validate_parity.py
```

The recorded passed package is under
`output/deployment/wave52r_integrated_specialist_a02/` and contains the ONNX
composer, test vectors, gate parameters, Structured Text reference sources,
per-condition results, and the YAML summary. The `2026-08-04-13-39-00` run
passed on all 194 official test conditions:

- campaign reconstruction maximum absolute error: `1.4901161e-08 deg`;
- maximum ONNX output error: `5.9604645e-08 deg`;
- maximum float32 PLC-reference output error: `1.6391277e-07 deg`;
- backward residual and backward prediction-versus-K01 error: exactly zero.

## Curated Archive

After parity passes, reproduce the curated archive leaf and validate the full
polished-setpoint inventory:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/models/promote_wave52r_a02_export_archive.py --promote

conda run --no-capture-output -n pinns_env python -B `
  scripts/models/export_post_retraining_selected_model_archives.py --validate-existing
```

The A02 leaf is stored at
`models/polished_dataset/setpoints/integrated_specialist_a02/global/`. Its
inventory records the K01 and H08 dependencies, exact hashes, fixed input
shapes, test evidence, and the boundary that this is a verified offline
candidate rather than an accepted-registry replacement.

## Beckhoff TF3820 Preparation

Prepare the exported composer with the repository-owned Beckhoff toolbox:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/deployment/twincat_onnx_conversion/convert_onnx_for_twincat.py `
  --onnx models/polished_dataset/setpoints/integrated_specialist_a02/global/onnx/model.onnx `
  --output-root output/deployment/twincat_onnx_conversion `
  --run-name wave52r_integrated_specialist_a02_composer `
  --skip-tf38x0 --prepare-tf3820 --run-onnxruntime-smoke `
  --copy-source-onnx --fail-fast
```

Install the prepared package and dedicated curve-composer runner into the
maintained standalone project, then validate its catalog:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/deployment/twincat_onnx_conversion/install_wave52r_a02_standalone_package.py

conda run --no-capture-output -n pinns_env python -B `
  reference/codes/TwinCAT_TF3820_StandaloneModelTest/scripts/validate_model_catalog.py
```

The resulting catalog contains 40 packages and runners: 39 remain selectable
through the generic pointwise predictor, while A02 uses its dedicated
multi-input, multi-output fixed-grid runner. This distinction prevents the
composer from being misrepresented as a single-sample replacement model.

## Remaining Runtime Gates

The current evidence establishes Python reconstruction parity, ONNX Runtime
parity, float32 PLC-reference parity, Beckhoff TF3820 preparation, and static
standalone-project validation. It does not establish:

- TwinCAT XAE compilation;
- target activation or Machine Learning Server licensing;
- ADS availability or target file deployment;
- PLC inference latency and deterministic task timing;
- end-to-end K01/H08 curve production and A02 replay on the target;
- commissioned TestRig compensation performance.

Record those gates independently during operator-side PLC qualification.
