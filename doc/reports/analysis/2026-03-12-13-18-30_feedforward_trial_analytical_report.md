# Feedforward Trial Analytical Report

## Overview

This document analyzes the proof training run executed for the current feedforward Transmission Error regression baseline.

The goal of this report is not only to restate the final metrics, but to explain what was actually trained, why the run can be considered successful as a first baseline verification, what the current result does not prove yet, and how it compares with the expectations extracted from the project reference material.

The analyzed run is:

- Run Name: `te_feedforward_trial`
- Model Type: `feedforward`
- Training Config: `config/feedforward_network_training_trial.yaml`
- Dataset Config: `config/dataset_processing.yaml`
- Metrics Artifact: `output/feedforward_network/te_feedforward_trial/training_test_metrics.yaml`
- Auto-Generated Summary: `output/feedforward_network/te_feedforward_trial/training_test_report.md`
- Best Checkpoint: `output/feedforward_network/te_feedforward_trial/checkpoints/feedforward-epoch=003-val_mae=0.00375716.ckpt`

## Executed Workflow

The executed workflow is an offline regression experiment on validated Transmission Error curves already stored in the repository dataset.

The current point-wise input features were:

1. output angular position in degrees
2. input speed in rpm
3. input torque in Nm
4. oil temperature in degrees
5. direction flag (`+1` forward, `-1` backward)

The target was the measured Transmission Error in degrees.

The run used the lightweight proof configuration rather than the full default baseline configuration. This was a deliberate engineering choice to verify the end-to-end pipeline quickly while still preserving the same model family, feature set, normalization logic, best-checkpoint selection, and held-out test evaluation.

Key proof-run settings were:

- `curve_batch_size: 8`
- `point_stride: 200`
- `maximum_points_per_curve: 200`
- `min_epochs: 3`
- `max_epochs: 12`
- `patience: 3`

The dataset split was performed at file level with reproducible randomization:

- training split: `70%`
- validation split: `20%`
- test split: `10%`
- random seed: `42`

At directional-curve level, the resulting split sizes were:

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

The training entry point used:

- training-only normalization statistics;
- validation-based checkpoint selection through `val_mae`;
- best-checkpoint reload before final evaluation;
- a final held-out `test` pass separate from validation.

This means the reported test metrics are methodologically stronger than the earlier workflow, where only training plus validation were available.

## Quantitative Results

Final recorded metrics for the selected best checkpoint were:

| Split | Loss | MAE [deg] | RMSE [deg] |
| --- | ---: | ---: | ---: |
| Validation | 0.011193 | 0.003757 | 0.004555 |
| Test | 0.009341 | 0.003583 | 0.004295 |

The target normalization statistics stored for the run were:

- target mean: `-0.017496 deg`
- target standard deviation: `0.045597 deg`

This gives a useful scale reference:

- validation MAE is about `8.24%` of the target standard deviation;
- test MAE is about `7.86%` of the target standard deviation;
- validation RMSE is about `9.99%` of the target standard deviation;
- test RMSE is about `9.42%` of the target standard deviation.

These percentages should not be interpreted as compensation percentages. They only contextualize the regression error relative to the variability of the current processed target distribution.

## Assessment Of The Training Run

### Short Answer

For a proof run, the training should be considered successful.

### Why It Looks Good

The main positive signs are:

- all final metrics are finite and small in absolute TE units;
- test metrics are very close to validation metrics;
- the test metrics are slightly better than the validation metrics, which does not indicate obvious overfitting on this split;
- the best checkpoint was found early and the run remained numerically stable;
- the complete workflow now reaches training, checkpoint selection, held-out evaluation, and report generation without manual intervention.

From an engineering standpoint, this is exactly what a first baseline run should demonstrate:

- the dataset path is valid;
- the point-wise feature representation is trainable;
- the current MLP can fit the processed TE signal structure to a meaningful degree;
- the training stack is reproducible enough to produce a checkpoint and a held-out test result.

### What "Went Well" Does Not Mean

This result does **not** prove that the repository already reproduces the industrial impact reported in the reference papers.

It proves a narrower claim:

- the current offline feedforward baseline can learn the mapping from processed features to processed TE values with stable generalization on one held-out split.

That is useful and necessary, but it is still only the first layer of validation.

## Interpretation Of Validation Versus Test Behavior

The fact that the test MAE (`0.003583 deg`) is slightly lower than the validation MAE (`0.003757 deg`) is a positive sign, but it should be interpreted conservatively.

The most reasonable reading is:

- there is no immediate generalization alarm on this split;
- the model did not memorize the validation set in a way that collapses on the held-out test set;
- the difference is small enough that it is more likely due to ordinary split variability than to any deeper conclusion.

This is especially important because:

- only one random split was evaluated;
- the proof-run configuration is lighter than the default baseline;
- the dataset consists of already processed TE curves rather than a broader raw-data reconstruction workflow.

So the correct conclusion is not "the model is solved," but rather:

- the current baseline behaves credibly enough to justify deeper experiments.

## Comparison With The Reference Material

### Where The Current Result Is Aligned

The current run is already aligned with several important project principles extracted from the reference summaries:

1. **Operating variables are physically meaningful.**
   The reference material emphasizes speed, torque, and oil temperature as key operating variables. The current baseline uses all three explicitly, together with angular position and direction.

2. **The model remains simple and inspectable.**
   The reference notes stress TwinCAT/PLC practicality and stable lightweight models. A feedforward MLP is consistent with that direction better than a more opaque or overly heavy architecture.

3. **The workflow is reproducible.**
   The papers and the internal summaries emphasize a clear separation between data, model training, and deployment. The repository now has an explicit train/validation/test split plus per-run report artifacts, which is a meaningful step toward disciplined experimentation.

4. **The result is reported in TE units.**
   The current evaluation reports MAE and RMSE directly in degrees of Transmission Error, which keeps the output interpretable for the application domain.

### Where The Current Result Is Still Behind The Papers

The gap with the reference material is still significant, and it should be stated clearly.

1. **Offline regression is not the same as online compensation.**
   The `RCIM` summary highlights compensation effectiveness during real operation and reports TE reductions above `80-90%` in some scenarios. Those are closed-loop or application-level compensation outcomes. The current run measures offline regression error on held-out processed data. These are not directly comparable quantities.

2. **There is no harmonic-selection study yet.**
   The machine-learning report summary stresses the selection of relevant TE frequencies and PLC-friendly representations. The current baseline predicts TE directly point by point; it does not yet analyze or optimize harmonic content for deployment.

3. **There is no TwinCAT deployment validation yet.**
   The reference material treats TwinCAT integration as a central requirement. The present run does not test export, PLC execution constraints, XML import flow, cycle-time impact, or runtime robustness.

4. **The current dataset path starts from validated TE curves.**
   The data-series explanation stresses encoder zeroing, `DataValid`, and the distinction between raw and processed signals. In the present run, those semantics are inherited indirectly from the curated dataset rather than being revalidated end to end during the experiment.

5. **The proof run is intentionally lighter than the default baseline.**
   Because `point_stride` was increased and `maximum_points_per_curve` was capped, this run is best understood as a workflow verification and preliminary performance estimate, not as the final baseline benchmark.

## Comparison Summary

The fairest comparison with the papers is therefore:

- **Good news:** the repository now demonstrates a credible offline ML baseline that respects the main physical operating variables and produces stable held-out errors.
- **Not proven yet:** no claim can be made that this baseline already matches the compensation effectiveness, deployment maturity, or experimental completeness described in the references.

This is still a useful result, because a stable offline baseline is a prerequisite for the later steps emphasized in the papers.

## Main Limitations Of The Current Run

The most important limitations are:

1. only one proof split was evaluated;
2. the run used a lighter verification config, not the full default baseline;
3. no ablation was performed on speed, torque, temperature, direction, or point subsampling;
4. no analysis was performed on specific operating regimes such as speed bands, torque bands, or temperature bands;
5. no harmonic-domain evaluation was performed;
6. no compensation simulation or online reproduction test was performed;
7. no TwinCAT-oriented export and runtime validation was performed.

These limitations do not invalidate the run. They define its scope.

## Final Conclusion

The training run should be judged as **successful for a first proof-of-work baseline**.

More precisely:

- the pipeline executed correctly end to end;
- the model learned a nontrivial mapping with stable held-out behavior;
- the resulting errors are small in TE units and consistent between validation and test;
- the repository is now in a better position to support more serious experimental comparisons.

However, this result should be described as:

- an **offline feedforward regression baseline validation**,

not as:

- a demonstrated industrial compensation result.

That distinction is essential to stay aligned with the reference papers.

## Recommended Next Steps

The next technically meaningful steps are:

1. run the full default baseline configuration and compare it against the proof run;
2. repeat the evaluation across multiple random seeds or split definitions;
3. produce regime-wise error analysis by speed, torque, and temperature;
4. add plots comparing predicted versus measured TE curves on representative conditions;
5. study harmonic content and evaluate whether a PLC-friendlier representation should be preferred;
6. prepare an export-and-runtime validation path compatible with future TwinCAT integration;
7. only after those steps, attempt a fair comparison with the compensation-level claims reported in the reference material.
