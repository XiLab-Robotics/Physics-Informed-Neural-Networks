# RCIM Paper Reference Benchmark

## Purpose

This report turns the paper
`reference/RCIM_ML-compensation.pdf` into a repository-owned benchmark package.
Its role is to keep the paper findings easy to inspect during planning,
training review, and colleague-facing status updates.

At the current repository state, the comparison is explicitly `offline-only`.
The repository does not yet have the online compensation pipeline needed for a
real Table 9 style comparison.

## Guided Reading

Read the paper in this order:

1. `Sections 2-3`: problem setup, dataset structure, selected harmonics, and
   model evaluation logic.
2. `Section 3.7` plus `Tables 2-6`: harmonic-level model ranking and the
   deployed model choices.
3. `Sections 4-5` plus `Table 9`: TwinCAT/PLC integration and the final online
   compensation benchmark.

The most important paper message is not only that ML can fit the reducer TE,
but that a deployable harmonic-wise prediction stack can be integrated into a
PLC and produce large online reductions in TE during real motion profiles.

## What The Paper Actually Says

### Problem Setup

- The paper models rotational Transmission Error of an RV reducer as a function
  of `input speed`, `applied torque`, and `oil temperature`.
- The TE is reconstructed from selected harmonic components rather than from
  one monolithic end-to-end neural predictor.
- The paper explicitly separates:
  - offline harmonic prediction;
  - PLC integration;
  - online compensation validation.

### Experimental Domain

- Total experimental samples: `1026`
- Speed levels: `100` to `1800 rpm`
- Torque levels: `0` to `1800 Nm`
- Temperature levels: `25`, `30`, `35 C`

### Harmonic Structure

The paper emphasizes these harmonics as the practical basis for TE modeling and
compensation:

- `0`
- `1`
- `3`
- `39`
- `40`
- `78`
- `81`
- `156`
- `162`
- `240`

The deployed compensation baseline then centers primarily on:

- `0`
- `1`
- `39`

Additional validation variants also include:

- `40`
- `78`

## Model Selection Summary

### Paper-Level Conclusion

The paper does not end with a single universal winner across every harmonic.
Instead, it converges toward a deployable stack dominated by tree and boosting
 models.

### Harmonic-Level Selected Models

| Harmonic | Selected Paper Model(s) |
| --- | --- |
| `0` | `SVM` |
| `1` | `RF / LGBM` |
| `3` | `HGBM` |
| `39` | `HGBM` |
| `40` | `ERT / GBM` |
| `78` | `HGBM / RF` |
| `81` | `RF` |
| `156` | `ERT / RF` |
| `162` | `ERT` |
| `240` | `ERT` |

### Why This Matters Here

- The paper is not arguing for a plain MLP-first deployment path.
- It favors models that are compact, interpretable enough for deployment work,
  and supported by the Beckhoff/TwinCAT stack.
- This is already directionally consistent with the current repository state,
  where the global offline winner is also tree-based.

## Extracted Reference Metrics

### Offline Prediction Validation

For unseen validation scenarios executed in TwinCAT-side prediction tests, the
paper reports mean percentage errors along the TE function of:

- `2.6%`
- `3.1%`
- `4.7%`

This is the most practical offline reference target that the repository can
aim to reproduce before the online compensation loop exists.

### Motion-Profile Test Conditions

| Motion Profile | Max Speed [rpm] | Max Torque [Nm] | Temperature [C] |
| --- | ---: | ---: | ---: |
| `Robot` | 303 | 759 | 31.6 |
| `Cycloidal` | 500 | 370 | 26.7 |

### Online Compensation Benchmark

| Profile | Case | TE RMS [deg] | TE Max [deg] | Reduction [%] |
| --- | --- | ---: | ---: | --- |
| `Robot` | No compensation | 0.0478 | 0.0681 | `-` |
| `Robot` | Comp `(0,1,39)` | 0.0080 | 0.0325 | `83.3 / 52.4` |
| `Robot` | Comp `(0,1,39,40)` | 0.0078 | 0.0309 | `83.6 / 54.7` |
| `Robot` | Comp `(0,1,39,78)` | 0.0079 | 0.0319 | `83.5 / 53.2` |
| `Cycloidal` | No compensation | 0.0282 | 0.0534 | `-` |
| `Cycloidal` | Comp `(0,1,39)` | 0.0017 | 0.0044 | `94.0 / 91.7` |
| `Cycloidal` | Comp `(0,1,39,40)` | 0.0017 | 0.0062 | `94.0 / 88.3` |
| `Cycloidal` | Comp `(0,1,39,78)` | 0.0027 | 0.0020 | `90.5 / 96.3` |

## Minimum Practical Targets For This Repository

### Target A

Match or beat the paper on a comparable offline prediction benchmark.

Minimum repository target:

- reproduce a paper-comparable TE-curve validation protocol;
- reach `<= 4.7%` mean percentage error on unseen comparable scenarios.

### Target B

Replicate the paper online compensation benchmark.

Minimum repository target:

- at least `83%` robot-profile TE RMS reduction;
- at least `90%` cycloidal-profile TE RMS reduction;
- and a cycloidal-profile TE max reduction in the same practical range as the
  paper benchmark.

## Repository Comparison At The Current State

### What Is Already Aligned

- The repository global offline winner is tree-based:
  - family: `tree`
  - model type: `hist_gradient_boosting`
  - run: `te_hist_gbr_tabular`
- The strongest current neural branch is still behind the tree winner:
  - family: `residual_harmonic_mlp`
- This is directionally consistent with the paper, where the deployable
  harmonic stack is dominated by tree and boosting models.

### Comparison Structure To Preserve

The repository should now keep two explicit offline comparison tracks:

- `Track 1`: paper-faithful harmonic-wise benchmark
- `Track 2`: repository direct-TE comparable benchmark

The first track answers whether the repository can reproduce the paper's own
harmonic-wise logic. The second track answers whether the repository's already
trained direct-TE families can match or beat the paper at the level of final
offline TE-curve prediction quality.

These two tracks must not be merged in reporting. Future paper-comparison
tables should explicitly label each entry as either:

- `paper-faithful harmonic-wise`
- `result-level comparable direct-TE`

### What Is Not Yet Comparable

- The repository now has a repository-owned harmonic-wise offline validation
  protocol, but the first baseline does not yet match the paper threshold.
- The repository does not yet have a harmonic-wise online compensation loop.
- The repository does not yet have TwinCAT-side or equivalent motion-profile
  compensation tests matching the paper's `Robot` and `Cycloidal` profile
  benchmark.
- Therefore, the repository cannot yet claim a real comparison against the
  paper's `Table 9`.

### Latest Harmonic-Wise Offline Result

The latest completed repository-owned harmonic-wise campaign is:

- `track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03`

Winning validation summary:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/2026-04-09-20-45-48__te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run/validation_summary.yaml`

Winning companion report:

- `doc/reports/analysis/validation_checks/2026-04-09-20-46-45_paper_reimplementation_rcim_harmonic_wise_te_harmonic_wise_full_rcim_no_engineering_reference_campaign_run_harmonic_wise_comparison_report.md`

Campaign results report:

- `doc/reports/campaign_results/2026-04-09-21-19-05_track1_second_iteration_harmonic_wise_campaign_results_report.md`

Current best paper-faithful offline result:

- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- feature set: `base_only`
- validation mean percentage error: `9.229%`
- test mean percentage error: `8.877%`
- oracle test mean percentage error: `2.749%`
- current `Target A` status: `not_yet_met`

The repository now also includes a stricter exact-paper validation branch:

- script: `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- config: `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- scope: recovered `rpm`, `deg`, `tor` inputs; exact `ampl_k` / `phase_k`
  targets; exact family bank; per-target ONNX export
- prepared campaign plan:
  `doc/reports/campaign_plans/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md`
- prepared launcher:
  `scripts/campaigns/run_exact_paper_model_bank_campaign.ps1`

This exact branch is implemented and campaign-prepared, but not yet executed,
so the current offline paper-faithful status is still anchored to the
completed harmonic-wise campaign above.

What the second iteration established:

- the full RCIM set still outperforms all reduced harmonic subsets;
- the engineered operating-condition features did not improve the full-RCIM
  branch in this campaign;
- the reduced subsets `0,1,39` and `0,1,39,40` are weak final targets because
  even their truncation-only oracle stays above `4.7%`;
- the main remaining gap is now better localized to predictor design,
  especially the dominant `h0` term and a smaller late-harmonic cluster.

Immediate next repository step:

- keep the full RCIM harmonic set as the mainline `Track 1` target;
- start a third harmonic-wise iteration focused on target parameterization,
  especially:
  - explicit handling of `h0`;
  - targeted comparison between `cos/sin` and `amplitude/phase` on dominant
    harmonics;
  - per-harmonic estimator specialization for the dominant error terms.

Important interpretation:

- the repository now has a completed second `Track 1` campaign rather than only
  a first baseline proof of concept;
- the best harmonic-wise result improved from `9.403%` to `8.877%`, so the
  branch is moving in the right direction;
- the paper threshold of `4.7%` remains substantially unmet, so the repository
  is still only partially aligned with the paper offline.

### Current Comparison Verdict

| Comparison Axis | Current Repository Status | Verdict |
| --- | --- | --- |
| Offline winner family direction | Tree winner (`hist_gradient_boosting`) | aligned |
| Offline metric protocol | Harmonic-wise held-out mean percentage error now available: `9.403%` | comparable_but_not_yet_matching |
| Online compensation benchmark | missing | not yet comparable |
| End-to-end paper replication | missing | not yet comparable |

## Online Compensation Tracking

This section is intentionally prepared now and must be updated as soon as the
repository implements online compensation tests.

### Repository Online Results

- Status: `not yet available`
- Required future fields:
  - robot profile uncompensated TE RMS and TE max;
  - robot profile compensated TE RMS and TE max;
  - robot profile reduction percentages;
  - cycloidal profile uncompensated TE RMS and TE max;
  - cycloidal profile compensated TE RMS and TE max;
  - cycloidal profile reduction percentages;
  - exact harmonic set used in each online test;
  - execution path used for the test.

### Online Comparison Rule

Once repository-owned online compensation tests exist, update both:

- this report;
- `doc/reports/analysis/Training Results Master Summary.md`

At that point the project can present a real `paper vs repository` end-to-end
comparison instead of the current offline-only comparison.

## Missing Pipeline For A Real Table 9 Comparison

The exact missing pipeline is:

1. a repository-owned harmonic-wise prediction workflow that outputs the same
   practical quantities used in the paper, namely amplitude and phase terms for
   selected harmonics across operating conditions;
2. a TE reconstruction workflow from those predicted harmonic components;
3. a motion-profile playback workflow for the `Robot` and `Cycloidal` style
   profiles used as the final benchmark;
4. an online compensation loop that applies the reconstructed TE correction
   during motion execution rather than only offline evaluation;
5. a measurement and reporting path that records uncompensated versus
   compensated TE RMS and TE max in a Table 9 style format;
6. a repository-owned final comparison report that states whether `Target A`
   and `Target B` were met.

Until those six pieces exist, the repository results remain strong offline
training results, but not yet a true reproduction of the paper benchmark.

## Implementation Priority

### Implement Now

- harmonic-wise prediction of `A_k` and `phi_k`
- TE reconstruction from the predicted harmonic terms
- offline motion-profile playback for `Robot` and `Cycloidal` style profiles
- paper-comparable offline validation protocol to close `Target A`
- repository-owned shared offline evaluator for direct-TE model families under
  the same final TE-curve percentage-error protocol
- evaluation of current best direct-TE families under that shared evaluator
- dual-track reporting that keeps paper-faithful and direct-TE result-level
  comparisons separate

These four items belong to the immediate repository branch because they create
the stable offline baseline that the online branch will later depend on.

This immediate branch should now be read as an explicit intermediate stage
between completed `Wave 1` and the later `Wave 2` temporal-model work.

### Implement Later

- online compensation loop execution in the future TestRig / online branch
- uncompensated vs compensated `TE RMS` and `TE max` measurement
- final `Table 9` style benchmark report to close `Target B`

These items should be treated as the follow-up online branch, not as the first
implementation step, because they only become trustworthy once the offline
harmonic prediction and reconstruction stack is already stable.

The future `Wave 2` temporal-model branch also stays in the roadmap, but it is
no longer the immediate next branch. It should open only after the
harmonic-wise comparison framework is implemented and reviewed.

## Sources

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `output/registries/program/current_best_solution.yaml`
