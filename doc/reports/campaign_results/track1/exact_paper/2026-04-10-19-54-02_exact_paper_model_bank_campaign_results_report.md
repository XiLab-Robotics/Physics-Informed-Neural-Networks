# Exact Paper Model Bank Campaign Results Report

## Overview

This report closes the exact-paper model-bank campaign prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-10-17-04-41_exact_paper_model_bank_campaign_plan_report.md`

The campaign executed `4` repository-owned validation runs through the
dedicated exact-paper launcher:

- completed runs: `4`
- failed runs: `0`
- execution window: `2026-04-10T18:44:39.0700428+02:00` to `2026-04-10T19:14:18.3733939+02:00`
- campaign artifact root:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/`

Unlike the harmonic-wise `Track 1` campaign, this package does not optimize the
full TE-curve offline benchmark directly. Its purpose is to validate the
stricter recovered-paper branch that uses:

- recovered `rpm`, `deg`, `tor` inputs;
- exact `ampl_k` and `phase_k` targets for harmonics
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- the full recovered family bank;
- one ONNX export artifact per family and target.

## Objective And Outcome

The campaign had four concrete questions:

1. can the full bank finish in diagnostic mode without ONNX export crashes?
2. can the same bank finish in strict mode after the `HGBM` converter fix?
3. does the isolated `SVR` branch still need surrogate safeguards, and does it
   now serialize cleanly?
4. can the non-`SVR` branch export cleanly as a reference bank?

Outcome:

- the full exact-paper bank now completes in both diagnostic `continue` mode
  and strict `reference` mode;
- the `HGBM` ONNX export blocker is resolved under the current local stack;
- the isolated `SVR` branch exports all `20` targets successfully, with `5`
  constant-surrogate replacements still required for degenerate targets;
- the non-`SVR` branch exports its full `180`-file surface cleanly;
- the canonical winner is the strict full-bank reference run
  `exact_full_bank_strict_reference`.

## Ranking Policy

This campaign is a stabilization campaign, not a generic hyperparameter sweep.
The ranking therefore follows this explicit serialized policy:

- primary metric: `winning_mean_component_mape_percent`
- first tie breaker: `winning_mean_component_mae`
- second tie breaker: prefer `strict` export mode over `continue`
- third tie breaker: prefer broader enabled-family coverage
- fourth tie breaker: `winning_mean_component_rmse`
- fifth tie breaker: lexical `run_name`

That policy intentionally promotes the cleanest faithful reference when the
diagnostic and strict runs produce equivalent validation metrics.

## Campaign Ranking

### Ranked Completed Runs

| Rank | Config | Family Scope | Export Mode | Winner | Mean Component MAPE [%] |
| --- | --- | --- | --- | --- | ---: |
| `1` | `exact_full_bank_strict_reference` | `all 10` recovered families | `strict` | `RF` | `18.369` |
| `2` | `exact_full_bank_diagnostic_continue` | `all 10` recovered families | `continue` | `RF` | `18.369` |
| `3` | `exact_non_svr_export_reference` | `9` non-`SVR` families | `strict` | `RF` | `18.369` |
| `4` | `exact_svr_export_diagnostic` | `SVR` only | `continue` | `SVR` | `103.265` |

| Config | Mean Component MAE | ONNX Exported | Surrogates | Failed Exports |
| --- | ---: | ---: | ---: | ---: |
| `exact_full_bank_strict_reference` | `0.056284` | `200` | `5` | `0` |
| `exact_full_bank_diagnostic_continue` | `0.056284` | `200` | `5` | `0` |
| `exact_non_svr_export_reference` | `0.056284` | `180` | `0` | `0` |
| `exact_svr_export_diagnostic` | `0.138346` | `20` | `5` | `0` |

## Campaign Winner

The explicit campaign winner is:

- `exact_full_bank_strict_reference`

Its result was:

- winner family: `RF`
- winner family estimator: `RandomForestRegressor`
- enabled families: `SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM`
- winner mean component MAPE: `18.369%`
- winner mean component MAE: `0.056284`
- winner mean component RMSE: `0.144839`
- ONNX exported files: `200`
- failed exports: `0`
- surrogate exports: `5`

This run won because it matched the best achieved component metric while also
proving that the full exact-paper bank now survives strict export mode without
fallback continuation behavior.

### Top Family Ranking Inside The Winning Run

| Rank | Family | Mean Component MAPE [%] | Mean Component MAE | Mean Component RMSE |
| --- | --- | ---: | ---: | ---: |
| `1` | `RF` | `18.369` | `0.056284` | `0.144839` |
| `2` | `HGBM` | `20.586` | `0.079797` | `0.155340` |
| `3` | `ERT` | `21.017` | `0.054424` | `0.139747` |
| `4` | `GBM` | `24.343` | `0.062593` | `0.152818` |
| `5` | `DT` | `27.419` | `0.063643` | `0.170755` |

## Interpretation By Experiment Block

### 1. The Full Strict Reference Is Now Operational

The most important campaign result is operational rather than purely numerical.
The full strict exact-paper bank now completes end to end:

- all `10` recovered families fitted;
- all `20` harmonic targets evaluated per family;
- all `200` per-target ONNX artifacts exported;
- zero export failures under `strict` mode.

Interpretation:

- the exact-paper branch is no longer only prepared;
- the `HGBM` ONNX export blocker has been removed in the repository-owned
  support layer;
- the campaign now provides a stable exact-paper reference surface for future
  comparison and deployment-facing inspection.

### 2. The Diagnostic Continue Run Is Now A Safety Net, Not The Mainline

The full-bank diagnostic run now reaches the same winner metric as the strict
reference:

- full diagnostic winner: `RF` at `18.369%`
- full strict winner: `RF` at `18.369%`

Interpretation:

- diagnostic mode remains useful for future isolation work;
- however, the branch no longer depends on diagnostic continuation to finish;
- promotion should therefore move to the strict full-bank run, not stay on the
  continue-mode path.

### 3. The `SVR` Branch Is Stable, But It Still Requires Surrogate Handling

The isolated `SVR` export diagnostic completed successfully:

- exported targets: `20`
- failed exports: `0`
- constant-surrogate exports: `5`

Interpretation:

- the earlier degenerate-`SVR` converter crash is resolved operationally;
- the branch is still not a pure raw-`SVR` export path, because `5` targets
  remain constant predictors under the modern stack;
- the surrogate behavior is now a documented compatibility layer rather than a
  hidden failure.

### 4. The Non-`SVR` Branch Confirms The Remaining Bank Is Clean

The non-`SVR` reference run exported the remaining family bank independently:

- enabled families: `9`
- exported files: `180`
- failed exports: `0`

Interpretation:

- the rest of the recovered family bank no longer depends on the `SVR`
  safeguard to remain operational;
- the branch can now be discussed as two stable pieces:
  - the special-case `SVR` branch with documented surrogate handling;
  - the non-`SVR` branch with clean strict export behavior.

## Error And Family Findings

The winning strict full-bank run keeps the same best family ordering as the
diagnostic full-bank run. The best exact-paper family in this repository branch
is still:

- `RF`

The highest-contributing winning-family target errors remain concentrated in
the phase branch:

- `fft_y_Fw_filtered_phase_156` MAE `0.425070`
- `fft_y_Fw_filtered_phase_240` MAE `0.277042`
- `fft_y_Fw_filtered_phase_162` MAE `0.230457`
- `fft_y_Fw_filtered_phase_78` MAE `0.051585`
- `fft_y_Fw_filtered_phase_81` MAE `0.047979`

Interpretation:

- the exact-paper branch remains dominated by phase-target difficulty rather
  than amplitude-target difficulty;
- the exact family-bank workflow is now stable enough that future work can
  focus on interpretation and parity analysis instead of export rescue.

## ONNX Export Alignment Findings

The campaign succeeded operationally, but the path-level recovered-reference
comparison remains intentionally unresolved:

- full-bank exported files: `200`
- recovered reference files: `201`
- matched relative paths: `0`
- missing relative paths against reference: `201`
- extra exported relative paths: `200`

This does **not** mean the export failed. The mismatch is structural:

- the recovered paper bundle uses nested family-plus-kind paths such as
  `DT/ampl/DecisionTreeRegressor_ampl0.onnx`;
- the repository export currently writes flat family folders such as
  `DT/DecisionTreeRegressor_ampl0.onnx`;
- the recovered bundle also contains at least one duplicate-style filename
  variant such as `RF/ampl/RandomForestRegressor_ampl240 (1).onnx`.

Interpretation:

- exportability is now stable;
- semantic path parity with the recovered release is still open;
- the next exact-paper refinement should normalize repository export layout if
  strict recovered-path mirroring is required.

## Paper Alignment Impact

This campaign materially changes the exact-paper branch in three ways.

### What Improved

- the exact-paper model-bank launcher is no longer only campaign-prepared;
- the full strict recovered family bank now executes end to end;
- the `SVR` and `HGBM` export blockers are both operationally contained.

### What Remains Open

- the exact branch still uses component-level family metrics, not the harmonic
  reconstruction TE-curve benchmark used for `Target A`;
- recovered-path ONNX parity is still not normalized;
- no online compensation benchmark exists yet.

### What The Campaign Established

- the exact-paper branch is now a stable structural reference bank;
- the harmonic-wise branch remains the current `Target A` offline benchmark;
- future paper-comparison reporting can now distinguish clearly between:
  - harmonic-wise TE-curve benchmark status;
  - exact family-bank export and parity status.

## Main Conclusions

The campaign supports five conclusions.

### 1. The Exact-Paper Branch Is Now Campaign-Executable

The repository can now run the full exact-paper family bank through the
canonical batch launcher without manual intervention.

### 2. The Correct Promoted Winner Is The Strict Full-Bank Reference

The diagnostic full-bank run and the strict reference reached the same winning
metric, so promotion should prefer the strict exact-paper reference because it
proves the branch no longer needs diagnostic continuation behavior.

### 3. The `HGBM` Export Issue Was Real And Is Now Resolved

The campaign would not have finished without the repository-side `HGBM`
converter sanitation fix. That fix is now validated by the real four-run batch.

### 4. `SVR` Is Operationally Stable But Still Special-Case

The branch is exportable again, but only because the repository now documents
and applies constant-surrogate handling for degenerate `SVR` targets.

### 5. Exact-Bank Success Does Not Yet Close `Target A`

This campaign stabilizes the exact-paper branch, but it does not replace the
harmonic-wise offline TE-curve benchmark that still sits at `8.877%` and
remains above the paper's `4.7%` threshold.

## Recommended Next Actions

The next technically justified steps are:

1. keep `exact_full_bank_strict_reference` as the canonical exact-paper run
   when discussing recovered-family-bank status;
2. preserve the `SVR` diagnostic branch for future surrogate-audit work rather
   than as the promoted reference;
3. decide whether the next exact-paper task should target recovered ONNX path
   mirroring, because the current export surface is operationally valid but not
   path-identical to the recovered release;
4. keep `Target A` tracking anchored to the harmonic-wise offline branch until
   the exact bank is connected to a TE-curve reconstruction benchmark;
5. defer any LAN-remote rerun unless future exact-bank iterations become
   materially heavier than the current local stabilization pass.

## Artifact References

- Campaign root:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/`
- Campaign leaderboard:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/campaign_leaderboard.yaml`
- Campaign best run YAML:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/campaign_best_run.yaml`
- Campaign best run note:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/campaign_best_run.md`
- Winning strict validation summary:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run/validation_summary.yaml`
- Winning strict model bundle:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-12-14__exact_full_bank_strict_reference_campaign_run/paper_family_model_bank.pkl`
- Diagnostic `SVR` validation summary:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-12-57__exact_svr_export_diagnostic_campaign_run/validation_summary.yaml`
- Per-run launcher logs:
  `output/training_campaigns/exact_paper_model_bank_campaign_2026_04_10_17_04_41/logs/`
