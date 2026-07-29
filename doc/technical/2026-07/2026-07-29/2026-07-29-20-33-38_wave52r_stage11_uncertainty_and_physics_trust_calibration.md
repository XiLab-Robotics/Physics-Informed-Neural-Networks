# Wave 5.2R Stage 11 Uncertainty And Physics-Trust Calibration

## Overview

Wave 5.2R Stage 11 determines whether observable, causal signals can identify
unreliable polished-setpoint forward predictions. It does not change the
official mean prediction and does not promote a new TE model. The stage
calibrates uncertainty around the retained analytical and residual branches,
then tests whether that uncertainty localizes high-error curves, operating
boundaries, and weakly supported conditions on the frozen Stage 2 split.

The stage retains four evidence sources:

- the PF-A analytical anchor from Stage 3;
- the H04 harmonic residual model from Stage 5;
- the K01 causal coefficient-residual GRU from Stage 9;
- the dense Stage 10 condition library as diagnostic disagreement evidence.

The campaign will compare simple support-aware scores, analytical-versus-learned
disagreement, seed-ensemble spread, calibrated combinations, and shuffled or
constant controls. Any uncertainty signal used at inference must depend only
on operating conditions, frozen model outputs, or ensemble outputs. Measured TE
and held-out prediction error are evaluation targets only.

## Technical Approach

### Frozen Data And Prediction Contract

The implementation will reuse the Stage 5 uniform curve representation and
common split manifest:

- dataset: `polished_dataset`;
- input mode: setpoints;
- surface: forward only;
- training, validation, and test identities remain unchanged;
- complete `65`-sample curves remain the evaluation unit;
- the held-out test partition is never used to fit an uncertainty mapping.

PF-A, H04, K01, and the Stage 10 dense formulation remain frozen comparison
branches. If additional K01 seeds are required for ensemble spread, they will
be trained with the same Stage 9 architecture, preprocessing, objective,
checkpoint rule, and causal sequence contract. Only the random seed changes.

### Uncertainty Signals

The bounded candidate set will include:

1. a constant validation-quantile interval as the non-localizing control;
2. standardized operating-condition nearest-neighbor distance;
3. the Stage 3 support tier and axis-boundary proximity;
4. PF-A-to-H04 and H04-to-K01 curve disagreement;
5. PF-A-to-K01 aggregate disagreement;
6. a K01 deep-ensemble spread from deterministic independent seeds;
7. a validation-calibrated composite trust score built from the causal signals;
8. a shuffled-score negative control with the same marginal distribution.

The first implementation will favor explicit NumPy/SciPy or scikit-learn
calibration over an opaque uncertainty network. A heteroscedastic neural head
or Bayesian last layer will be added only if the simpler signals fail to
localize error and the campaign plan can define a leakage-safe training target.
That deferral avoids training a larger uncertainty mechanism before proving
that error localization is observable.

### Calibration Protocol

Raw uncertainty scores will be fitted or monotonically calibrated on the
validation partition only. The test partition remains untouched until final
evaluation. Where interval coverage is required, split-conformal residual
quantiles will be estimated from validation residuals and applied once to the
test predictions.

Calibration will be measured at curve level and, where meaningful, at sample
level. The required evidence includes:

- Spearman uncertainty-error rank correlation;
- top-20-percent high-error capture rate;
- precision-recall area for high-error localization;
- risk-coverage area and selective MAE at fixed coverage;
- empirical coverage and mean width for nominal 50, 80, 90, and 95 percent
  intervals;
- calibration by torque, speed, and temperature band;
- separate supported-core, sparse-or-corner, and extrapolation evidence;
- boundary-holdout behavior;
- inference-time and storage cost relative to one K01 model.

### Exit Gate

A Stage 11 trust mechanism qualifies only if it is more informative than the
constant and shuffled controls and satisfies all of the following on the
held-out test partition:

- positive uncertainty-error rank correlation with a declared minimum before
  execution;
- high-error capture materially above the random 20-percent expectation;
- lower selective risk than unfiltered K01 predictions;
- non-vacuous interval coverage with reported width;
- no material collapse in any populated torque, speed, or temperature band;
- causal runtime inputs and complete prediction payloads;
- explicit inference and storage cost.

A uniformly wide interval, an uncalibrated ensemble spread, or a score that
works only after observing measured TE fails the stage. A qualified trust
mechanism remains an auxiliary research component; it does not retroactively
promote K01 or authorize physics-integrated Wave 6.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/running/te_model_live_backlog.md`
- Stage 3 analytical-anchor reproduction and support-envelope artifacts
- Stage 5 uniform curve representation and frozen split manifest
- Stage 9 K01 implementation, checkpoint, and prediction artifacts
- Stage 10 dense-library prediction and disagreement artifacts
- `config/training/uncertainty_physics_trust_calibration/`
- `scripts/models/` for any reusable trust-calibration component
- `scripts/campaigns/wave_5_2/` for the Python campaign driver and dedicated
  PowerShell launcher
- `doc/scripts/campaigns/wave_5_2/` for the launcher note
- `output/training_runs/uncertainty_physics_trust_calibration/`
- `output/training_campaigns/<run_instance_id>/`
- `output/analysis/wave_5_2r/stage11_uncertainty_physics_trust_calibration/`
- Stage 11 campaign-results Markdown, styled PDF, and companion figures
- the program ledger, backlog, master summaries, usage guide, and Sphinx portal

No subagent is planned. Repository instructions require separate explicit
approval before any subagent launch.

## Implementation Steps

1. Freeze the Stage 5 split and verify PF-A, H04, K01, and Stage 10 prediction
   provenance.
2. Create the Stage 11 campaign planning report with candidate identifiers,
   fixed thresholds, calibration partitions, negative controls, and artifact
   contracts.
3. Query current library documentation through Context7 before implementing
   version-sensitive NumPy, SciPy, scikit-learn, or PyTorch behavior.
4. Implement reusable causal uncertainty scores, monotonic calibration,
   conformal intervals, localization metrics, and cost measurement.
5. Reuse the Stage 9 K01 workflow to train only the additional deterministic
   seeds required for ensemble spread.
6. Create campaign YAML files, the local and `-Remote` PowerShell launcher,
   launcher documentation, and prepared campaign state.
7. Run syntax checks, campaign validation, and local and remote preflight
   contracts.
8. Execute the approved campaign and preserve immutable per-run artifacts,
   leaderboard files, and explicit best-run evidence.
9. Build the Stage 11 closeout report with calibration, localization,
   operating-band, boundary, and deployment-cost figures.
10. Export and validate the real styled PDF, inspect every rendered page, and
    repair any layout defect.
11. Synchronize the backlog, ledger, master summaries, usage guide, technical
    indices, and Sphinx portal.
12. Run Markdown warning checks, MarkdownLint, Python and PowerShell checks,
    Sphinx `-W`, workflow preflight, PDF validation, and Git size checks.
13. Commit the complete validated Stage 11 scope under the active temporary
    user approval, then advance to Stage 12.
