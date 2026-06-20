# TE Curve Verification Pipeline Curve Reconstruction And Collage Pipeline

## Purpose

This document describes how `TE Curve Verification Pipeline` constructs the curves plotted in the
best-model collage reports. It is intentionally implementation-facing: every
major statement is tied to the current repository code so that future
investigations into `CVP 1.1` through `Wave 3.1` can separate real model
behavior from plotting, reconstruction, offset, or convention artifacts.

The main focus is the visual report family under:

```text
doc/reports/analysis/track2/best_model_collage_report/
```

The document also explains how the mean-centered diagnostic introduced by commit
`940a16b934e29ca83fef36da010fdf671bdd52c4` relates to the standard collage
path. That commit does not replace the standard `TE Curve Verification Pipeline` reconstruction path;
it adds a post-prediction diagnostic view that subtracts the measured and
predicted per-curve means separately.

As of the `2026-06-16` policy update, collage and overlay evidence are required
inputs to the official multi-index curve-first selection process. The visual
reports do not override raw metrics by themselves, but they must be considered
when scalar error, centered-shape metrics, offset diagnostics, and harmonic /
phase diagnostics disagree.

## Key Takeaways

- The standard collage report does not read curve data back from the report
  images. It regenerates predictions from the same candidate loading and
  evaluation support used by the `TE Curve Verification Pipeline` matrix.
- Repository-backed models such as `harmonic_regression` predict a full TE curve
  directly at each angular position.
- Paper/reference-bank candidates such as `paper_original_best_Fw` predict
  harmonic amplitude and phase targets from operating conditions, then
  reconstruct a full TE curve from harmonic coefficients.
- `paper_original_best_Fw` uses 19 effective predicted targets for
  reconstruction: 10 amplitudes, including `h0`, and 9 phases for the positive
  harmonics. A phase target for `h0` may exist in inventories, but the
  reconstruction path does not use it because `h0` is the constant term.
- A large improvement in the mean-centered diagnostic is evidence of an offset
  or DC-component problem, not by itself evidence that the curve shape is wrong.
- A phase/sign-convention problem would usually remain visible after
  mean-centering because subtracting the mean cannot repair harmonic phase.
- Official `TE Curve Verification Pipeline` promotion decisions must not be made from `MAE`, `RMSE`,
  or mean percentage error alone. They must preserve separate raw-error,
  shape-fidelity, offset / continuity, harmonic / phase, robustness, visual,
  and deployment-readiness evidence per `global`, `Fw`, and `Bw` surface.

## Source Map

| Concern | Canonical Source | Key Lines |
| --- | --- | --- |
| curve-verification matrix configuration | `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml` | `2`, `11`, `13`, `16-213`, `265-275` |
| Test curve record construction | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `370-432` |
| Reference-bank feature matrix | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `435-449` |
| Reference-bank target prediction | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `471-496` |
| Amplitude/phase to coefficients | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `544-576` |
| Source-specific `h0` sign rule | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `579-585` |
| Registry-model input tensor | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `658-672` |
| Registry-model curve prediction | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `815-848` |
| Candidate loading | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `1158-1292` |
| Candidate evaluation | `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | `1295-1397` |
| Harmonic decomposition convention | `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py` | `224-269` |
| Harmonic curve reconstruction | `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py` | `537-557` |
| Collage report runner | `scripts/reports/analysis/build_track2_best_model_collage_report.py` | `866-1024` |
| Collage curve selection | `scripts/reports/analysis/build_track2_best_model_collage_report.py` | `576-633` |
| Collage plotting | `scripts/reports/analysis/build_track2_best_model_collage_report.py` | `644-688` |
| Mean-centered diagnostic | `scripts/reports/analysis/build_track2_mean_centered_collage_report.py` | `156-190`, `243-291`, `585-716` |
| `harmonic_regression` model | `scripts/models/harmonic_regression.py` | `12-186` |

## Configuration Surface

The standard `TE Curve Verification Pipeline` matrix and visual reports use the same matrix template:

```yaml
# Source: config/.../full_track2_matrix_template.yaml:1-13
paths:
  dataset_config_path: config/datasets/transmission_error_dataset.yaml

comparison:
  run_name: track2_full_directional_family_matrix
  model_family: track2_reference_comparison
  output_root: output/validation_checks/track2_reference_comparison
  comparison_mode: full_directional_candidate_matrix
  canonical_report_path: doc/reports/analysis/track2/TE Curve Verification Pipeline Directional Model Comparison.md
  baseline_summary_path: output/validation_checks/track2_reference_comparison/...
  lightweight_test_curve_records: true
  report_plot_generation_scope: incremental_current_candidates
  percentage_error_denominator: peak_to_peak_truth
```

The key flags for the collage path are:

- `dataset_config_path`: points to the canonical dataset configuration.
- `lightweight_test_curve_records: true`: builds records directly from the
  test CSV files without requiring harmonic decomposition targets on each
  record.
- `percentage_error_denominator: peak_to_peak_truth`: normalizes percentage
  error by each truth curve's peak-to-peak amplitude.
- `evaluation.selected_harmonics`: fixes the harmonics used by paper/reference
  reconstruction.

The selected harmonics are:

```yaml
# Source: config/.../full_track2_matrix_template.yaml:265-275
evaluation:
  selected_harmonics:
    - 0
    - 1
    - 3
    - 39
    - 40
    - 78
    - 81
    - 156
    - 162
    - 240
```

The dataset configuration behind `dataset_config_path` resolves to
`data/simplified_dataset` and enables both directions. The current split policy uses a
20 percent validation split, a 10 percent test split, and seed `42`. The
collage report therefore works on held-out test curves, not training curves.

## Candidate Families And Direction Surfaces

`TE Curve Verification Pipeline` evaluates candidate surfaces directionally:

| Surface | Valid Curves | Typical Candidate ID |
| --- | --- | --- |
| `global` | forward and backward | `harmonic_regression_global` |
| `Fw` | forward only | `harmonic_regression_fw` |
| `Bw` | backward only | `harmonic_regression_bw` |

Direction filtering is enforced in the shared evaluation code:

```python
# Source: reference_family_vs_feedforward_support.py:1295-1308
def filter_curve_records_for_candidate(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    candidate: Track2Candidate,
) -> list[harmonic_wise_support.HarmonicCurveRecord]:

    """Filter held-out curves to the directions valid for one candidate."""

    filtered_curve_record_list = [
        curve_record
        for curve_record in curve_record_list
        if str(curve_record.direction_label).strip().lower() in candidate.allowed_direction_list
    ]
    assert filtered_curve_record_list, f"No curves available for TE Curve Verification Pipeline candidate | {candidate.candidate_id}"
    return filtered_curve_record_list
```

This matters for debugging: a forward-only reference candidate should not be
judged on backward curves, and a backward-only candidate should not be judged on
forward curves. If a future `CVP 1.1` through `Wave 3.1` wrapper bypasses this
filter, its visual artifacts are not comparable with the canonical matrix.

## Standard Best-Model Collage Flow

The standard collage entry point is
`scripts/reports/analysis/build_track2_best_model_collage_report.py`.

The runner performs these steps:

1. Resolve a timestamped output directory and dated report directory.
2. Load the `TE Curve Verification Pipeline` matrix template.
3. Read `evaluation.selected_harmonics`.
4. Build test curve records.
5. Resolve report candidate configurations.
6. Load each candidate.
7. Evaluate every candidate over its valid held-out curves without storing full
   curve payloads.
8. Summarize metrics by candidate and direction.
9. Select four representative curves for each candidate.
10. Re-evaluate only the selected curves with full curve payloads.
11. Save one PNG collage per candidate.
12. Copy the PNG into the report bundle's `assets/` tree.
13. Save candidate metrics and a YAML summary.
14. Write the Markdown report.

The core runner sequence is:

```python
# Source: build_track2_best_model_collage_report.py:884-914
training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
    training_config,
    selected_harmonic_list,
)
percentage_error_denominator = str(training_config["comparison"]["percentage_error_denominator"])

candidate_configuration_list = resolve_report_candidate_configuration_list(
    training_config,
    arguments.family_registry_root,
    arguments.periodic_mlp_harmonic_campaign_leaderboard_path,
    output_directory,
)
candidate_list = [
    reference_family_vs_feedforward_support.load_track2_candidate(candidate_configuration)
    for candidate_configuration in candidate_configuration_list
]
```

After that initial candidate load, each candidate is evaluated once across all
valid curves without the full TE arrays:

```python
# Source: build_track2_best_model_collage_report.py:907-915
per_candidate_entry_list: list[dict[str, Any]] = []
for candidate in candidate_list:
    candidate_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
        candidate,
        curve_record_list,
        percentage_error_denominator,
        include_curve_payload=False,
    )
    per_candidate_entry_list.extend(candidate_entry_list)
```

The initial no-payload pass is used for metrics and representative-curve
selection. The selected four curves are then re-evaluated with payload enabled:

```python
# Source: build_track2_best_model_collage_report.py:953-970
selected_curve_record_list = [
    curve_record_lookup[build_curve_key(selected_entry)]
    for selected_entry in selected_entry_list
]
selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
    candidate,
    selected_curve_record_list,
    percentage_error_denominator,
    include_curve_payload=True,
)
selected_payload_lookup = {
    build_curve_key(selected_payload_entry): selected_payload_entry
    for selected_payload_entry in selected_payload_entry_list
}
selected_entry_list = [
    selected_payload_lookup[build_curve_key(selected_entry)]
    for selected_entry in selected_entry_list
]
```

The important point is that the plotted curves are regenerated through
`evaluate_track2_candidate()`. They are not loaded from a previous PNG or from a
hand-authored report table.

## Test Curve Record Construction

When `lightweight_test_curve_records` is true, curve records are built directly
from the dataset test split:

```python
# Source: reference_family_vs_feedforward_support.py:377-427
if bool(training_config.get("comparison", {}).get("lightweight_test_curve_records", False)):
    dataset_configuration = transmission_error_dataset.load_dataset_processing_config(
        training_config["paths"]["dataset_config_path"]
    )
    dataset_root = transmission_error_dataset.resolve_project_relative_path(
        dataset_configuration["paths"]["dataset_root"]
    )
    direction_configuration = dataset_configuration["directions"]
    split_configuration = dataset_configuration["split"]
    directional_file_manifest = transmission_error_dataset.build_directional_file_manifest(
        dataset_root=dataset_root,
        use_forward_direction=bool(direction_configuration["use_forward_direction"]),
        use_backward_direction=bool(direction_configuration["use_backward_direction"]),
    )
    train_manifest, validation_manifest, test_manifest = transmission_error_dataset.split_directional_file_manifest(
        directional_file_manifest,
        validation_split=float(split_configuration["validation_split"]),
        test_split=float(split_configuration["test_split"]),
        random_seed=int(split_configuration["random_seed"]),
    )
```

For each test CSV, the code stores:

- source file path;
- direction label;
- direction flag;
- speed in rpm;
- torque in Nm;
- oil temperature in degrees Celsius;
- angular positions in degrees;
- measured transmission error in degrees.

The lightweight path deliberately leaves `coefficient_dictionary` and
`amplitude_phase_dictionary` empty:

```python
# Source: reference_family_vs_feedforward_support.py:397-415
for csv_file_path, direction_label in test_manifest:
    curve_sample = transmission_error_dataset.build_validated_directional_sample(
        csv_file_path.resolve(),
        direction_label,
    )
    curve_record_list.append(
        harmonic_wise_support.HarmonicCurveRecord(
            source_file_path=curve_sample.source_file_path,
            direction_label=curve_sample.direction_label,
            direction_flag=float(curve_sample.direction_flag),
            speed_rpm=float(curve_sample.speed_rpm),
            torque_nm=float(curve_sample.torque_nm),
            oil_temperature_deg=float(curve_sample.oil_temperature_deg),
            angular_position_deg=curve_sample.angular_position_deg.astype(np.float32),
            transmission_error_deg=curve_sample.transmission_error_deg.astype(np.float32),
            coefficient_dictionary={},
            amplitude_phase_dictionary={},
        )
    )
```

This is why `TE Curve Verification Pipeline` collage reconstruction for paper/reference candidates is
based on model-predicted harmonic targets, not on harmonic targets precomputed
for each repository curve.

## Representative Curve Selection

Each collage contains exactly four curves. The report builder enforces this:

```python
# Source: build_track2_best_model_collage_report.py:607-622
def select_candidate_collage_entries(
    candidate_entry_list: list[dict[str, Any]],
    selection_mode: str,
    curves_per_collage: int,
) -> list[dict[str, Any]]:

    """Select the representative entries for one candidate collage."""

    assert curves_per_collage == 4, "The current report layout expects four curves per collage."
    if selection_mode != "mixed":
        direction_entry_list = [
            entry
            for entry in candidate_entry_list
            if str(entry["direction_label"]).strip().lower() == selection_mode
        ]
        return select_spread_entries(direction_entry_list, curves_per_collage)
```

For `global` candidates, `selection_mode` is `mixed`; the builder selects two
forward and two backward curves from the sorted available list. For `Fw` and
`Bw` candidates, all four selected curves come from the matching direction.

The sorting order is deterministic:

```python
# Source: build_track2_best_model_collage_report.py:576-589
return sorted(
    entry_list,
    key=lambda entry: (
        str(entry["direction_label"]),
        float(entry["oil_temperature_deg"]),
        float(entry["torque_nm"]),
        float(entry["speed_rpm"]),
        str(entry["source_file_path"]),
    ),
)
```

The selected entries are spread across that sorted list using evenly spaced
positions. This makes the visual report deterministic and inspectable.

## Plotting Mechanics

The standard collage plotting function receives entries that already contain:

- `angular_position_deg`;
- `truth_curve_deg`;
- `predicted_curve_deg`;
- condition metadata;
- per-curve metrics.

The plotting code is intentionally simple:

```python
# Source: build_track2_best_model_collage_report.py:661-688
for axis, per_candidate_entry in zip(flattened_axis_list, selected_entry_list):
    angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float32)
    truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float32)
    predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float32)
    axis.plot(angular_position_deg, truth_curve_deg, label="Measured TE", linewidth=1.2, color="#4a4a4a")
    axis.plot(angular_position_deg, predicted_curve_deg, label=candidate_id, linewidth=1.2, color="#1f77b4")
    axis.set_title(
        (
            f"{per_candidate_entry['direction_label']} | "
            f"{float(per_candidate_entry['speed_rpm']):.0f} rpm | "
            f"{float(per_candidate_entry['torque_nm']):.0f} Nm | "
            f"{float(per_candidate_entry['oil_temperature_deg']):.0f} C"
        ),
        fontsize=9,
    )
```

There is no smoothing, re-centering, resampling, or post-hoc correction in the
standard collage. The line labeled `Measured TE` is the test CSV curve. The line
labeled with the candidate ID is the candidate prediction returned by
`evaluate_track2_candidate()`.

## Shared Candidate Evaluation Function

The single most important function for understanding the plotted curves is:

```text
reference_family_vs_feedforward_support.evaluate_track2_candidate()
```

Its behavior branches on the candidate kind:

- reference candidates predict harmonic targets and reconstruct a curve;
- registry candidates directly predict a full TE curve.

The branch is visible here:

```python
# Source: reference_family_vs_feedforward_support.py:1323-1365
if candidate.candidate_kind in REFERENCE_CANDIDATE_KIND_SET:
    assert candidate.model_entry_list is not None
    predicted_target_dictionary = predict_reference_bank_target_dictionary(
        candidate_curve_record_list,
        candidate.model_entry_list,
        candidate.model_dictionary,
    )
    ...
    prediction_lookup = build_reference_prediction_lookup(
        candidate.model_entry_list,
        predicted_target_dictionary,
    )
else:
    predicted_target_dictionary = {}
    prediction_lookup = {}

per_candidate_entry_list: list[dict[str, Any]] = []
for sample_index, curve_record in enumerate(candidate_curve_record_list):
    if candidate.candidate_kind in REFERENCE_CANDIDATE_KIND_SET:
        coefficient_dictionary, _ = build_reference_coefficient_dictionary_from_entries(
            prediction_lookup,
            sample_index,
            candidate.selected_harmonic_list,
            resolve_reference_h0_sign_multiplier(candidate),
        )
        predicted_curve_deg = harmonic_wise_support.reconstruct_curve_from_coefficients(
            curve_record.angular_position_deg,
            candidate.selected_harmonic_list,
            coefficient_dictionary,
        )
    else:
        assert candidate.training_config is not None
        predicted_curve_deg = predict_wave1_registry_curve(
            candidate.model_object,
            candidate.training_config,
            curve_record,
        )
```

Every later metric, CSV row, summary entry, or plotted line depends on this
`predicted_curve_deg`.

## Repository Model Path: Harmonic Regression

### Candidate Identity

In the standard collage report, `harmonic_regression` appears as three
registry-backed candidates:

| Candidate ID | Registry | Valid Directions |
| --- | --- | --- |
| `harmonic_regression_global` | `output/registries/families/harmonic_regression/latest_family_best.yaml` | forward and backward |
| `harmonic_regression_fw` | `output/registries/families/harmonic_regression_fw/latest_family_best.yaml` | forward |
| `harmonic_regression_bw` | `output/registries/families/harmonic_regression_bw/latest_family_best.yaml` | backward |

The candidate configurations are generated by the collage builder:

```python
# Source: build_track2_best_model_collage_report.py:244-273
for base_family_name in WAVE1_BASE_FAMILY_LIST:
    candidate_configuration_list.extend(
        [
            {
                "candidate_id": f"{base_family_name}_global",
                "candidate_family": base_family_name,
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": "wave1_current_registry",
                "candidate_surface": "global",
                "family_registry_path": f"{registry_root_text}/{base_family_name}/latest_family_best.yaml",
                "allowed_direction_list": ["forward", "backward"],
            },
            {
                "candidate_id": f"{base_family_name}_fw",
                "candidate_family": base_family_name,
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": "wave1_current_registry",
                "candidate_surface": "Fw",
                "family_registry_path": f"{registry_root_text}/{base_family_name}_fw/latest_family_best.yaml",
                "allowed_direction_list": ["forward"],
            },
            {
                "candidate_id": f"{base_family_name}_bw",
                "candidate_family": base_family_name,
                "candidate_kind": "wave1_registry_model",
                "candidate_source_label": "wave1_current_registry",
                "candidate_surface": "Bw",
                "family_registry_path": f"{registry_root_text}/{base_family_name}_bw/latest_family_best.yaml",
                "allowed_direction_list": ["backward"],
            },
        ]
    )
```

`harmonic_regression` is in `WAVE1_BASE_FAMILY_LIST`, so these three candidates
are included automatically.

### Registry Loading

For a repository model, `load_track2_candidate()` takes the
`wave1_registry_model` branch:

```python
# Source: reference_family_vs_feedforward_support.py:1249-1267
if candidate_kind == "wave1_registry_model":
    family_registry_path = candidate_configuration["family_registry_path"]
    registry_entry = resolve_family_best_entry(family_registry_path)
    model_object, training_config = load_wave1_registry_model(registry_entry)
    return Track2Candidate(
        candidate_id=candidate_id,
        candidate_family=candidate_family,
        candidate_kind=candidate_kind,
        candidate_source_label=candidate_source_label,
        candidate_surface=candidate_surface,
        allowed_direction_list=allowed_direction_list,
        source_path=shared_training_infrastructure.resolve_runtime_project_relative_path(family_registry_path),
        selected_harmonic_list=[],
        model_entry_list=None,
        model_dictionary=None,
        registry_entry=registry_entry,
        training_config=training_config,
        model_object=model_object,
    )
```

The registry entry points to the selected run directory and checkpoint. The
loader opens that run's `training_config.yaml`, reads the model type, and loads
the matching artifact:

```python
# Source: reference_family_vs_feedforward_support.py:316-341
def load_wave1_registry_model(registry_entry: dict[str, Any]) -> tuple[Any, dict[str, Any]]:

    """Load one Wave 1 registry-backed model artifact."""

    output_directory = shared_training_infrastructure.resolve_runtime_project_relative_path(
        registry_entry["output_directory"]
    )
    training_config_path = output_directory / shared_training_infrastructure.COMMON_TRAINING_CONFIG_FILENAME
    training_config = shared_training_infrastructure.load_training_config(training_config_path)
    model_type = str(registry_entry["model_type"]).strip().lower()
    if model_type in {"hist_gradient_boosting", "random_forest"}:
        model_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
            registry_entry["best_checkpoint_path"]
        )
        return tree_regression_support.load_tree_model(model_path), training_config

    best_checkpoint_path = shared_training_infrastructure.resolve_runtime_project_relative_path(
        registry_entry["best_checkpoint_path"]
    )
    return (
        load_lightning_regression_module_for_inference(
            best_checkpoint_path,
            training_config,
        ),
        training_config,
    )
```

For `harmonic_regression`, this means the candidate is a loaded Lightning
`TransmissionErrorRegressionModule` whose internal model is
`scripts/models/harmonic_regression.py`.

### Input Tensor

Every repository candidate receives pointwise physical inputs:

```python
# Source: reference_family_vs_feedforward_support.py:658-672
def build_feedforward_input_tensor(curve_record: harmonic_wise_support.HarmonicCurveRecord) -> torch.Tensor:

    """Build the pointwise feedforward input tensor for one curve record."""

    sequence_length = int(curve_record.angular_position_deg.shape[0])
    input_feature_matrix = np.column_stack(
        [
            curve_record.angular_position_deg.astype(np.float32),
            np.full(sequence_length, curve_record.speed_rpm, dtype=np.float32),
            np.full(sequence_length, curve_record.torque_nm, dtype=np.float32),
            np.full(sequence_length, curve_record.oil_temperature_deg, dtype=np.float32),
            np.full(sequence_length, curve_record.direction_flag, dtype=np.float32),
        ]
    ).astype(np.float32)
    return torch.from_numpy(input_feature_matrix)
```

The columns are:

1. angular position in degrees;
2. speed in rpm;
3. torque in Nm;
4. oil temperature in degrees Celsius;
5. direction flag.

### Direct TE Prediction

Repository candidates do not predict amplitude and phase targets in the
`TE Curve Verification Pipeline` collage path. They return a full TE curve directly:

```python
# Source: reference_family_vs_feedforward_support.py:815-848
def predict_wave1_registry_curve(
    model_object: Any,
    training_config: dict[str, Any],
    curve_record: harmonic_wise_support.HarmonicCurveRecord,
) -> np.ndarray:

    """Predict one TE curve with a loaded registry-backed model."""

    model_type = str(training_config["experiment"]["model_type"]).strip().lower()
    if model_type in {"hist_gradient_boosting", "random_forest"}:
        input_tensor = build_feedforward_input_tensor(curve_record).float()
        input_feature_matrix = input_tensor.detach().cpu().numpy().astype(np.float32)
        return np.asarray(model_object.predict(input_feature_matrix), dtype=np.float32).reshape(-1)

    assert isinstance(model_object, TransmissionErrorRegressionModule), (
        f"Expected TransmissionErrorRegressionModule | {model_type}"
    )
    ...
    with torch.no_grad():
        normalized_input_tensor = model_object.normalize_input_tensor(input_tensor)
        normalized_prediction_tensor, _ = model_object.forward_regression_model(
            input_tensor,
            normalized_input_tensor,
        )
        predicted_curve_tensor = model_object.denormalize_target_tensor(normalized_prediction_tensor)
    return predicted_curve_tensor.detach().cpu().numpy().reshape(-1).astype(np.float32)
```

For `harmonic_regression`, the final plotted curve is therefore:

```text
predicted_curve_deg =
    harmonic_regression(
        angular_position_deg,
        speed_rpm,
        torque_nm,
        oil_temperature_deg,
        direction_flag,
    )
```

The collage does not perform an external harmonic reconstruction for this
candidate.

### Internal Harmonic Regression Shape

The model itself is harmonic, but the output is still scalar TE per point. Its
basis is:

```python
# Source: scripts/models/harmonic_regression.py:127-137
angular_position_rad = angular_position_deg * (torch.pi / 180.0)
harmonic_feature_tensor_list = [torch.ones_like(angular_position_rad)]

# Append Sine And Cosine Features For Each Harmonic Order
for harmonic_multiplier in self.positive_harmonic_index_tensor:
    harmonic_feature_tensor_list.append(torch.sin(harmonic_multiplier * angular_position_rad))
    harmonic_feature_tensor_list.append(torch.cos(harmonic_multiplier * angular_position_rad))

# Concatenate Harmonic Features
return torch.cat(harmonic_feature_tensor_list, dim=-1)
```

The coefficients can be static or linearly conditioned on normalized operating
conditions:

```python
# Source: scripts/models/harmonic_regression.py:139-157
def resolve_coefficient_tensor(self, normalized_condition_tensor: torch.Tensor) -> torch.Tensor:
    ...
    if self.conditioning_projection is None:
        return self.base_coefficient_tensor.unsqueeze(0).expand(normalized_condition_tensor.shape[0], -1)

    # Add Linear Condition-Dependent Coefficient Adjustment
    return self.base_coefficient_tensor.unsqueeze(0) + self.conditioning_projection(normalized_condition_tensor)
```

The forward pass multiplies the harmonic basis by those coefficients and sums
the result:

```python
# Source: scripts/models/harmonic_regression.py:174-185
angular_position_deg = input_tensor[:, 0:1]
normalized_condition_tensor = normalized_input_tensor[:, 1:]

# Build Harmonic Feature Tensor
harmonic_feature_tensor = self.build_harmonic_feature_tensor(angular_position_deg)

# Resolve Harmonic Coefficients
coefficient_tensor = self.resolve_coefficient_tensor(normalized_condition_tensor)

# Compute Harmonic Regression
return torch.sum(harmonic_feature_tensor * coefficient_tensor, dim=-1, keepdim=True)
```

This is an internal model parameterization, not the same as the
paper/reference-bank target protocol. The external `TE Curve Verification Pipeline` evaluation still
sees only a direct TE curve prediction.

## Paper-Original Forward Path: `paper_original_best_Fw`

### Candidate Definition

`paper_original_best_Fw` is defined as a composite reference-bank candidate. It
uses different archived paper model families for different amplitude and phase
targets:

```yaml
# Source: full_track2_matrix_template.yaml:73-100
- candidate_id: paper_original_best_Fw
  candidate_family: best_composite
  candidate_source_label: rcim_original
  candidate_surface: Fw
  archive_root: models/paper_reference/rcim_original/forward
  allowed_direction_list:
    - forward
  amplitude_family_by_harmonic:
    "0": SVM
    "1": RF
    "3": HGBM
    "39": HGBM
    "40": ERT
    "78": HGBM
    "81": RF
    "156": ERT
    "162": ERT
    "240": ERT
  phase_family_by_harmonic:
    "1": LGBM
    "3": HGBM
    "39": HGBM
    "40": GBM
    "78": RF
    "81": RF
    "156": RF
    "162": ERT
    "240": ERT
```

This gives 19 effective reconstruction targets:

| Target Type | Harmonics | Count |
| --- | --- | --- |
| Amplitude | `0`, `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240` | 10 |
| Phase | `1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, `240` | 9 |

The constant harmonic `h0` has an amplitude-like value but no phase in the
reconstruction formula.

### Composite Candidate Loading

For `composite_reference_bank`, `load_track2_candidate()` loops through the
amplitude and phase family maps, opens the relevant family inventory, and
collects one `ReferenceModelEntry` per selected target:

```python
# Source: reference_family_vs_feedforward_support.py:1190-1218
if candidate_kind == "composite_reference_bank":
    archive_root = str(candidate_configuration["archive_root"]).rstrip("/")
    family_folder_lookup = candidate_configuration["family_folder_lookup"]
    model_entry_list: list[ReferenceModelEntry] = []
    inventory_entry_cache: dict[str, list[ReferenceModelEntry]] = {}
    inventory_path_cache: dict[str, Path] = {}

    for target_kind, selection_dictionary in [
        ("amplitude", candidate_configuration["amplitude_family_by_harmonic"]),
        ("phase", candidate_configuration["phase_family_by_harmonic"]),
    ]:
        for harmonic_order_text, family_id in selection_dictionary.items():
            archive_folder = family_folder_lookup[str(family_id)]
            reference_inventory_path = f"{archive_root}/{archive_folder}/reference_inventory.yaml"
            if family_id not in inventory_entry_cache:
                reference_inventory = load_reference_inventory(reference_inventory_path)
                inventory_entry_cache[family_id] = load_reference_model_entries(reference_inventory)
                ...
            model_entry_list.append(
                find_reference_model_entry(
                    inventory_entry_cache[family_id],
                    target_kind,
                    int(harmonic_order_text),
                )
            )
```

The candidate's `selected_harmonic_list` is then derived from the collected
entries:

```python
# Source: reference_family_vs_feedforward_support.py:1218-1233
selected_harmonic_list = sorted(
    {
        reference_entry.harmonic_order
        for reference_entry in model_entry_list
    }
)
return Track2Candidate(
    candidate_id=candidate_id,
    candidate_family=candidate_family,
    candidate_kind=candidate_kind,
    candidate_source_label=candidate_source_label,
    candidate_surface=candidate_surface,
    allowed_direction_list=allowed_direction_list,
    source_path=shared_training_infrastructure.resolve_runtime_project_relative_path(archive_root),
    selected_harmonic_list=selected_harmonic_list,
    model_entry_list=model_entry_list,
```

Because the amplitude map contains `h0` and the phase map contains positive
harmonics, the final list is the expected 10 harmonic indices.

### Paper-Compatible Feature Matrix

Reference-bank models do not receive the angular position. They predict
curve-level harmonic targets from the operating condition:

```python
# Source: reference_family_vs_feedforward_support.py:435-449
def build_reference_feature_matrix(curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord]) -> pd.DataFrame:

    """Build the reference-bank feature matrix aligned with the archived models."""

    return pd.DataFrame(
        data=[
            {
                "rpm": float(curve_record.speed_rpm),
                "deg": float(curve_record.oil_temperature_deg),
                "tor": float(curve_record.torque_nm),
            }
            for curve_record in curve_record_list
        ],
        columns=["rpm", "deg", "tor"],
    )
```

The schema is exactly:

| Column | Repository Meaning |
| --- | --- |
| `rpm` | input speed |
| `deg` | oil temperature |
| `tor` | torque |

This naming mirrors the recovered paper assets. It is a common point to audit
because `deg` can be misread as angular position; in this path it is oil
temperature.

### Target Prediction

Each target-specific archived model is called with the same feature matrix:

```python
# Source: reference_family_vs_feedforward_support.py:471-496
def predict_reference_bank_target_dictionary(
    curve_record_list: list[harmonic_wise_support.HarmonicCurveRecord],
    reference_model_entry_list: list[ReferenceModelEntry],
    reference_model_dictionary: dict[str, Any] | None,
) -> dict[str, np.ndarray]:

    """Predict all archived amplitude and phase targets for the held-out curves."""

    reference_feature_matrix = build_reference_feature_matrix(curve_record_list)
    predicted_target_dictionary: dict[str, np.ndarray] = {}
    for reference_entry in reference_model_entry_list:
        assert reference_entry.feature_name_list == ["rpm", "deg", "tor"], (
            "Unexpected reference feature schema | "
            f"{reference_entry.feature_name_list}"
        )
        if reference_model_dictionary is None:
            with reference_entry.python_model_path.open("rb") as model_file:
                reference_model_object = pickle.load(model_file)
        else:
            reference_model_object = reference_model_dictionary[reference_entry.target_name]
        predicted_target_dictionary[reference_entry.target_name] = predict_reference_model_in_batches(
            reference_model_object,
            reference_feature_matrix,
        )
        del reference_model_object
    return predicted_target_dictionary
```

For `paper_original_best_Fw`, these target names follow the recovered paper
schema, for example:

```text
fft_y_Fw_filtered_ampl_0
fft_y_Fw_filtered_ampl_1
fft_y_Fw_filtered_phase_1
```

The inventory files under `models/paper_reference/rcim_original/forward/*`
provide the mapping from target names to archived `.pkl` models.

### Amplitude/Phase To Coefficients

After all targets are predicted, the code converts the target vectors for each
curve into harmonic coefficients:

```python
# Source: reference_family_vs_feedforward_support.py:544-576
def build_reference_coefficient_dictionary_from_entries(
    prediction_lookup: dict[tuple[str, int], np.ndarray],
    sample_index: int,
    selected_harmonic_list: list[int],
    h0_sign_multiplier: float = 1.0,
) -> tuple[dict[str, float], dict[str, float]]:

    """Convert one generic RCIM Model-Bank Reproduction bank prediction into harmonic coefficients."""

    coefficient_dictionary: dict[str, float] = {}
    amplitude_phase_dictionary: dict[str, float] = {}

    for harmonic_order in selected_harmonic_list:
        predicted_amplitude = float(prediction_lookup[("amplitude", harmonic_order)][sample_index])

        if harmonic_order == 0:
            signed_amplitude = float(h0_sign_multiplier * predicted_amplitude)
            coefficient_dictionary["coefficient_cos_h0"] = signed_amplitude
            amplitude_phase_dictionary["amplitude_h0"] = abs(signed_amplitude)
            amplitude_phase_dictionary["phase_rad_h0"] = 0.0
            continue

        predicted_phase = float(prediction_lookup[("phase", harmonic_order)][sample_index])
        coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = float(
            predicted_amplitude * np.cos(predicted_phase)
        )
        coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = float(
            -predicted_amplitude * np.sin(predicted_phase)
        )
```

The effective equations are:

```text
coefficient_cos_h0 = h0_sign_multiplier * amplitude_h0

coefficient_cos_h = amplitude_h * cos(phase_h)
coefficient_sin_h = -amplitude_h * sin(phase_h)
```

The negative sign in the sine coefficient is deliberate. It matches the
repository decomposition convention described later.

### Source-Specific `h0` Sign Rule

The only source-specific `h0` sign rule in the current code is for
`rcim_track1` forward:

```python
# Source: reference_family_vs_feedforward_support.py:579-585
def resolve_reference_h0_sign_multiplier(candidate: Track2Candidate) -> float:

    """Resolve source-specific `h0` sign compatibility for reference banks."""

    if candidate.candidate_source_label == "rcim_track1" and candidate.candidate_surface == "Fw":
        return -1.0
    return 1.0
```

For `paper_original_best_Fw`, the candidate source label is `rcim_original`, so
the multiplier is `+1.0`. If a mean-offset problem is isolated specifically in
`paper_original_best_Fw`, this function is one of the key places to inspect,
because the current implementation intentionally does not apply an original
paper forward sign correction.

### Final Harmonic Reconstruction

The final curve is reconstructed by:

```python
# Source: harmonic_wise_support.py:537-557
def reconstruct_curve_from_coefficients(
    angular_position_deg: np.ndarray,
    selected_harmonic_list: list[int],
    coefficient_dictionary: dict[str, float],
) -> np.ndarray:

    """Reconstruct one TE curve from harmonic coefficients."""

    angle_radians = np.deg2rad(angular_position_deg.astype(np.float64))
    reconstructed_curve = np.zeros_like(angle_radians, dtype=np.float64)

    for harmonic_order in selected_harmonic_list:
        if harmonic_order == 0:
            reconstructed_curve += float(coefficient_dictionary["coefficient_cos_h0"])
            continue

        reconstructed_curve += (
            float(coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"]) * np.cos(float(harmonic_order) * angle_radians)
            + float(coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"]) * np.sin(float(harmonic_order) * angle_radians)
        )
```

The mathematical form is:

```text
TE(theta) =
    coefficient_cos_h0
    + sum_h(
        coefficient_cos_h * cos(h * theta)
        + coefficient_sin_h * sin(h * theta)
      )
```

Because `coefficient_sin_h = -amplitude_h * sin(phase_h)`, this is equivalent
to:

```text
TE(theta) =
    amplitude_h0
    + sum_h(
        amplitude_h * cos(phase_h) * cos(h * theta)
        - amplitude_h * sin(phase_h) * sin(h * theta)
      )
```

Using the identity `cos(a + b) = cos(a)cos(b) - sin(a)sin(b)`, the positive
harmonic contribution is:

```text
amplitude_h * cos(h * theta + phase_h)
```

This convention is important: changing the sine sign changes the phase
direction of every reconstructed positive harmonic.

## Repository Harmonic Convention

The same convention appears in the decomposition support. During least-squares
decomposition, the repository solves for cosine and sine coefficients:

```python
# Source: harmonic_wise_support.py:238-266
design_matrix = build_harmonic_design_matrix(reduced_angular_position_deg, selected_harmonic_list)
coefficient_vector, *_ = np.linalg.lstsq(
    design_matrix,
    reduced_transmission_error_deg,
    rcond=None,
)
...
coefficient_cos = float(coefficient_vector[vector_index])
coefficient_sin = float(coefficient_vector[vector_index + 1])
amplitude_value = float(np.sqrt((coefficient_cos ** 2) + (coefficient_sin ** 2)))
phase_value = float(np.arctan2(-coefficient_sin, coefficient_cos))

coefficient_dictionary[f"coefficient_cos_h{harmonic_order}"] = coefficient_cos
coefficient_dictionary[f"coefficient_sin_h{harmonic_order}"] = coefficient_sin
amplitude_phase_dictionary[f"amplitude_h{harmonic_order}"] = amplitude_value
amplitude_phase_dictionary[f"phase_rad_h{harmonic_order}"] = phase_value
```

The phase is computed as:

```text
phase_h = atan2(-coefficient_sin_h, coefficient_cos_h)
```

Therefore the inverse conversion must use:

```text
coefficient_sin_h = -amplitude_h * sin(phase_h)
```

The reference-bank reconstruction path follows that inverse exactly.

## Metrics Attached To The Plotted Curves

After `predicted_curve_deg` is produced, the shared evaluator computes metrics
against the measured test curve:

```python
# Source: reference_family_vs_feedforward_support.py:1367-1371
metric_dictionary = harmonic_wise_support.compute_curve_metric_dictionary(
    curve_record.transmission_error_deg,
    predicted_curve_deg,
    percentage_error_denominator,
)
```

The report stores those metrics in each selected curve entry:

```python
# Source: reference_family_vs_feedforward_support.py:1372-1393
per_candidate_entry = {
    "candidate_id": candidate.candidate_id,
    "candidate_family": candidate.candidate_family,
    "candidate_kind": candidate.candidate_kind,
    "candidate_source_label": candidate.candidate_source_label,
    "candidate_surface": candidate.candidate_surface,
    "allowed_direction_list": list(candidate.allowed_direction_list),
    "source_path": shared_training_infrastructure.format_project_relative_path(candidate.source_path),
    "source_file_path": shared_training_infrastructure.format_project_relative_path(curve_record.source_file_path),
    "direction_label": curve_record.direction_label,
    "speed_rpm": float(curve_record.speed_rpm),
    "torque_nm": float(curve_record.torque_nm),
    "oil_temperature_deg": float(curve_record.oil_temperature_deg),
    "metrics": metric_dictionary,
}
if include_curve_payload:
    per_candidate_entry.update(
        {
            "angular_position_deg": curve_record.angular_position_deg.astype(float).tolist(),
            "truth_curve_deg": curve_record.transmission_error_deg.astype(float).tolist(),
            "predicted_curve_deg": predicted_curve_deg.astype(float).tolist(),
        }
    )
```

Those payload fields are the values used by the PNG plotter.

## Mean-Centered Diagnostic From Commit 940a16b9

Commit `940a16b934e29ca83fef36da010fdf671bdd52c4` added:

```text
scripts/reports/analysis/build_track2_mean_centered_collage_report.py
doc/scripts/reports/analysis/build_track2_mean_centered_collage_report.md
```

The diagnostic reuses the standard candidate list and standard selected curves.
It does not change model loading or prediction. It calls
`evaluate_track2_candidate()` again, gets the same raw predicted payload, and
then computes mean-centered metrics.

The per-curve transformation is:

```python
# Source: build_track2_mean_centered_collage_report.py:160-174
truth_curve_deg = np.asarray(entry_dictionary["truth_curve_deg"], dtype=np.float64)
predicted_curve_deg = np.asarray(entry_dictionary["predicted_curve_deg"], dtype=np.float64)
raw_residual_deg = predicted_curve_deg - truth_curve_deg

truth_mean_deg = float(np.mean(truth_curve_deg))
predicted_mean_deg = float(np.mean(predicted_curve_deg))
centered_truth_curve_deg = truth_curve_deg - truth_mean_deg
centered_predicted_curve_deg = predicted_curve_deg - predicted_mean_deg
centered_residual_deg = centered_predicted_curve_deg - centered_truth_curve_deg

raw_mae_deg = float(np.mean(np.abs(raw_residual_deg)))
raw_rmse_deg = float(np.sqrt(np.mean(raw_residual_deg ** 2)))
centered_mae_deg = float(np.mean(np.abs(centered_residual_deg)))
centered_rmse_deg = float(np.sqrt(np.mean(centered_residual_deg ** 2)))
offset_error_deg = predicted_mean_deg - truth_mean_deg
```

The plotted diagnostic curves are:

```python
# Source: build_track2_mean_centered_collage_report.py:260-269
for axis, per_candidate_entry in zip(flattened_axis_list, selected_entry_list):
    angular_position_deg = np.asarray(per_candidate_entry["angular_position_deg"], dtype=np.float64)
    truth_curve_deg = np.asarray(per_candidate_entry["truth_curve_deg"], dtype=np.float64)
    predicted_curve_deg = np.asarray(per_candidate_entry["predicted_curve_deg"], dtype=np.float64)
    truth_centered_deg = truth_curve_deg - np.mean(truth_curve_deg)
    predicted_centered_deg = predicted_curve_deg - np.mean(predicted_curve_deg)
    metric_dictionary = per_candidate_entry["mean_centering_metrics"]

    axis.plot(angular_position_deg, truth_centered_deg, label="Measured TE centered", linewidth=1.2, color="#4a4a4a")
    axis.plot(angular_position_deg, predicted_centered_deg, label=f"{candidate_id} centered", linewidth=1.2, color="#1f77b4")
```

The diagnostic runner makes the reuse of the standard selected curves explicit:

```python
# Source: build_track2_mean_centered_collage_report.py:604-657
training_config = shared_training_infrastructure.load_training_config(arguments.config_path)
source_collage_summary = load_source_collage_summary(arguments.source_collage_summary_path)
selected_harmonic_list = [int(value) for value in training_config["evaluation"]["selected_harmonics"]]
curve_record_list, _, _, dataset_root = reference_family_vs_feedforward_support.build_curve_record_list(
    training_config,
    selected_harmonic_list,
)
...
source_candidate_summary = source_candidate_summary_lookup[candidate_id]
selected_curve_record_list = [
    curve_record_lookup[build_curve_key(source_curve_entry)]
    for source_curve_entry in source_candidate_summary["selected_curve_list"]
]
selected_payload_entry_list, _ = reference_family_vs_feedforward_support.evaluate_track2_candidate(
    candidate,
    selected_curve_record_list,
    percentage_error_denominator,
    include_curve_payload=True,
)
```

Interpretation:

- If mean-centering greatly improves a candidate, the candidate shape may be
  close while its per-curve mean is offset.
- This is especially relevant for reference-bank candidates because their
  constant term is predicted through `h0`.
- Mean-centering is not a deployable runtime correction in this report. It is a
  diagnostic lens.
- Mean-centering cannot repair wrong phase direction, wrong harmonic family
  selection, or wrong angular basis. Those errors affect curve shape after the
  mean is removed.

## Error Sources To Audit In CVP 1.1 Through Wave 3.1

### Offset Or DC-Term Problems

Most relevant when:

- raw MAE is high;
- mean-centered MAE drops strongly;
- curve peaks and troughs align visually after centering;
- residuals are dominated by a near-constant vertical shift.

Primary code points:

- `build_reference_coefficient_dictionary_from_entries()`;
- `resolve_reference_h0_sign_multiplier()`;
- reference inventories for `ampl_0`;
- dataset zeroing and `DataValid` extraction upstream of the test CSV.

For `paper_original_best_Fw`, the present code uses `h0_sign_multiplier = +1.0`
because the special `-1.0` rule applies only to `rcim_track1` forward.

### Phase Or Sine-Sign Problems

Most relevant when:

- mean-centered curves still show phase inversion or shifted peaks;
- harmonic amplitude predictions look plausible but the reconstructed curve
  shape is wrong;
- errors are periodic rather than mostly vertical.

Primary code points:

- `phase_value = atan2(-coefficient_sin, coefficient_cos)`;
- `coefficient_sin_h = -amplitude_h * sin(phase_h)`;
- `reconstruct_curve_from_coefficients()`.

The current code is internally consistent. Any change here must be justified
against the recovered paper convention, not only against one visual plot.

### Feature-Schema Problems

Most relevant when:

- all amplitude and phase targets for a paper bank look degraded;
- errors are condition-dependent;
- a model family works in its original paper validation but fails in `TE Curve Verification Pipeline`.

Primary code point:

```python
# Source: reference_family_vs_feedforward_support.py:439-449
return pd.DataFrame(
    data=[
        {
            "rpm": float(curve_record.speed_rpm),
            "deg": float(curve_record.oil_temperature_deg),
            "tor": float(curve_record.torque_nm),
        }
        for curve_record in curve_record_list
    ],
    columns=["rpm", "deg", "tor"],
)
```

The `deg` field is oil temperature here. It is not angular position.

### Direction-Scope Problems

Most relevant when:

- a forward-only candidate appears in a backward report section;
- a global candidate is compared as though it were forward-only;
- selected collage curves differ between standard and mean-centered reports.

Primary code points:

- `allowed_direction_list` in candidate configuration;
- `filter_curve_records_for_candidate()`;
- `build_report_group_list()`;
- `select_candidate_collage_entries()`.

### Direct-Curve Versus Reference-Reconstruction Confusion

Most relevant when:

- a repository model is debugged as though it predicted amplitudes and phases;
- a paper-reference model is debugged as though it emitted per-point TE.

The two paths are different:

| Candidate Kind | Example | Prediction Output Before Plotting |
| --- | --- | --- |
| `wave1_registry_model` | `harmonic_regression_fw` | Direct per-point TE curve |
| `composite_reference_bank` | `paper_original_best_Fw` | Amplitudes and phases, then reconstructed TE curve |

Debugging must begin by identifying the candidate kind. The same visual report
contains both kinds.

## End-To-End Path Comparison

### `harmonic_regression_fw`

```text
latest_family_best.yaml
  -> best checkpoint and training_config.yaml
  -> load Lightning TransmissionErrorRegressionModule
  -> build pointwise input tensor:
       [angle, rpm, torque, oil_temperature, direction_flag]
  -> normalize input
  -> run harmonic_regression model
  -> denormalize scalar TE output
  -> predicted_curve_deg
  -> metric calculation
  -> standard collage plot
```

No external amplitude/phase prediction happens in this path.

### `paper_original_best_Fw`

```text
full_track2_matrix_template.yaml
  -> composite candidate maps each harmonic target to a paper family
  -> load reference_inventory.yaml for each required family
  -> load target-specific Python pickle models
  -> build paper feature matrix:
       [rpm, deg=oil_temperature, tor]
  -> predict 10 amplitude targets and 9 phase targets
  -> convert amplitude/phase to harmonic coefficients:
       h0: coefficient_cos_h0 = amplitude_h0
       h>0: coefficient_cos_h = amplitude_h * cos(phase_h)
       h>0: coefficient_sin_h = -amplitude_h * sin(phase_h)
  -> reconstruct TE over each repository angular-position vector
  -> predicted_curve_deg
  -> metric calculation
  -> standard collage plot
```

This path is sensitive to `h0`, phase convention, feature schema, and archive
target selection.

## Practical Debug Checklist

When investigating a suspicious `TE Curve Verification Pipeline` collage or a `CVP 1.1` through
`Wave 3.1` branch, use this order:

1. Identify `candidate_id`, `candidate_kind`, `candidate_source_label`, and
   `candidate_surface` from the validation summary.
2. Confirm `allowed_direction_list` matches the report section.
3. Confirm whether the candidate is direct-curve or reference-reconstruction.
4. For direct-curve candidates, inspect the registry entry, training config,
   checkpoint, input tensor shape, and denormalization.
5. For reference candidates, inspect the amplitude/phase family maps, inventory
   entries, feature schema, `h0` handling, and phase-to-coefficient convention.
6. Compare standard raw metrics with mean-centered metrics.
7. If mean-centered metrics improve strongly, inspect offset/DC behavior before
   changing harmonic phase code.
8. If mean-centered metrics remain poor, inspect phase convention, selected
   harmonics, direction filtering, and condition feature mapping.
9. Keep standard and diagnostic plots separate: the mean-centered plot is not a
   replacement for the official raw-curve evaluation.
10. For official selection, summarize raw error, mean-centered shape, offset /
    continuity, harmonic / phase, robustness, visual evidence, and deployment
    readiness before recommending promotion or rejection.

## Current Interpretation Of The 940a16b9 Diagnostic

The diagnostic introduced by `940a16b9` is useful because it isolates vertical
offset from shape-following error. In the standard pipeline, both repository
models and reference candidates are judged on raw measured TE. In the diagnostic
pipeline, each measured curve and predicted curve is centered by its own mean
before recomputing metrics.

Therefore:

- a large raw-to-centered improvement points toward offset, zeroing, or `h0`
  behavior;
- a small raw-to-centered improvement points toward shape, phase, harmonic, or
  feature errors;
- a correction to `h0` should be validated against the raw official `TE Curve Verification Pipeline`
  matrix and not only against the mean-centered visual report;
- any correction to phase sign must be checked against the repository
  decomposition convention and the recovered paper convention.

For `paper_original_best_Fw`, the most important observation is that the
reference path reconstructs the full curve from predicted targets. It is not
equivalent to a repository model that learns TE directly point-by-point. This
distinction should remain explicit in future `CVP 1.1` through `Wave 3.1`
investigations.
