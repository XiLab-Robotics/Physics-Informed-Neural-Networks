# Wave 5.2R Stage 11 Uncertainty And Physics-Trust Calibration Campaign Plan

## Campaign Decision

Prepare and execute a bounded polished-setpoint forward campaign that asks one
question:

> Can causal uncertainty signals localize unreliable K01 predictions better
> than constant and shuffled controls?

The campaign does not optimize or promote a new mean predictor. K01 remains the
frozen prediction center, while PF-A, H04, the Stage 10 dense model, operating
support, and independent K01 seeds supply candidate trust signals.

## Fixed Scope

| Field | Value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | setpoints |
| Surface | `Fw` only |
| Curve length | `65` samples |
| Split source | frozen Stage 5 common split manifest |
| Training curves | `675` |
| Calibration curves | validation split, `194` |
| Final evaluation curves | held-out test split, `97` |
| Mean prediction center | frozen Stage 9 K01 |
| Primary seed | `314159` |
| Additional ensemble seeds | `271828`, `161803`, `141421`, `173205` |

No measured TE, residual target, or test error may enter a runtime uncertainty
feature. Validation errors may be used only to fit declared calibration maps
and conformal quantiles.

## Prediction Provenance

The driver must verify and record:

- the Stage 5 uniform-curve artifact hash;
- the common split signature;
- PF-A and H04 reconstruction agreement;
- the exact Stage 9 K01 checkpoint and configuration;
- the Stage 10 dense R00 prediction artifact;
- the accepted polished-setpoint forward periodic-GRU provenance used only as
  contextual evidence;
- zero target-derived runtime inputs.

If any frozen artifact cannot be aligned to the same curve identities, the
preflight fails before training.

## Candidate Matrix

| ID | Candidate | Runtime signal | Calibration |
| --- | --- | --- | --- |
| `C00` | Constant conformal control | none beyond K01 | global validation residual quantiles |
| `S01` | Condition distance | standardized nearest training-condition distance | isotonic error scale |
| `S02` | Support and boundary score | Stage 3 tier, normalized axis margin, density excess | isotonic error scale |
| `A01` | PF-A/H04 disagreement | curvewise and pointwise absolute disagreement | isotonic error scale |
| `A02` | H04/K01 disagreement | curvewise and pointwise absolute disagreement | isotonic error scale |
| `A03` | PF-A/K01 disagreement | curvewise and pointwise absolute disagreement | isotonic error scale |
| `D01` | Dense/K01 disagreement | Stage 10 R00 versus K01 disagreement | isotonic error scale |
| `E01` | K01 deep-ensemble spread | standard deviation over five deterministic K01 seeds | isotonic error scale |
| `M01` | Composite trust estimator | all causal scalar signals | validation-fitted nonnegative ridge plus isotonic map |
| `N01` | Shuffled negative control | deterministic permutation of `M01` | same marginal distribution |

Every entry produces a complete test score, interval payload, metric summary,
and inference-cost record. `C00` and `N01` cannot win.

## Ensemble Contract

The primary K01 checkpoint is reused. Four additional K01 members are trained
with the exact Stage 9:

- model class and layer dimensions;
- frozen H04 anchor;
- preprocessing statistics;
- causal sequence ordering;
- optimization objective;
- validation checkpoint rule;
- maximum epoch and early-stopping policy.

Only the random seed changes. The ensemble mean is diagnostic and must not
replace K01 as the official Stage 11 prediction center. The reported spread is
the sample standard deviation across the five mean predictions.

## Calibration Contract

### Curve-Level Error Localization

The target is per-curve K01 MAE. Each raw candidate score is monotonically
mapped to predicted curve error by validation-only isotonic regression with
out-of-domain clipping. Constant inputs receive a declared zero-correlation
result rather than an unhandled `NaN`.

The composite estimator uses standardized causal signals. A fixed ridge grid
is selected by deterministic five-fold cross-validation inside the validation
partition. Coefficients are constrained to remain nonnegative before the final
isotonic mapping so that larger physical-disagreement signals cannot silently
become higher trust.

### Prediction Intervals

Intervals remain centered on the primary K01 curve. Validation absolute
residuals calibrate:

- pointwise marginal 50, 80, 90, and 95 percent intervals;
- a 90-percent simultaneous complete-curve band;
- normalized conformal widths for nonconstant candidates.

The test split is evaluated once after all maps and quantiles are frozen.

## Required Metrics

### Primary Localization Metrics

- Spearman rank correlation between curve score and curve MAE;
- average precision for membership in the test top-error quintile;
- top-20-percent error capture by the top-20-percent uncertainty set;
- area under the risk-coverage curve;
- K01 MAE retained at 95, 90, 80, and 60 percent coverage.

### Calibration Metrics

- empirical pointwise coverage at nominal 50, 80, 90, and 95 percent;
- mean interval width at each nominal level;
- 90-percent simultaneous complete-curve coverage and width;
- coverage and width by torque, speed, and temperature tercile;
- coverage and localization by Stage 3 support tier.

### Operational Metrics

- uncertainty evaluation time per curve;
- total checkpoint size;
- multiplicative cost relative to one K01 checkpoint;
- target-derived runtime input count;
- finite-payload and curve-identity checks.

## Fixed Exit Gates

A non-control candidate becomes a qualified Stage 11 trust component only if
all applicable gates pass:

| Gate | Threshold |
| --- | ---: |
| Curve-MAE Spearman correlation | at least `0.30` |
| Top-quintile average precision | at least `0.35` |
| Top-20-percent error capture | at least `0.40` |
| Selective curve MAE at 80-percent coverage | at least `10%` below unfiltered K01 |
| Marginal 90-percent coverage | from `0.85` through `0.95` |
| Mean 90-percent width | no more than `1.05` times `C00` |
| Populated-band 90-percent coverage | no band below `0.75` when count is at least `10` |
| Runtime target-derived inputs | exactly `0` |
| Complete finite curve payload | required |

The ensemble candidate must additionally report the five-checkpoint cost.
Deployment promotion requires a single-pass or distilled mechanism no more than
`1.25` times the primary K01 evaluation cost. An informative but expensive
ensemble can be retained as an offline research component only.

## Decision Rules

- If one or more causal candidates pass every gate, retain the simplest passing
  trust mechanism as the Stage 11 qualified component.
- If only the full ensemble passes, retain it as offline evidence and require a
  future distilled trust-head parity test.
- If candidates localize error but interval calibration fails, retain only the
  diagnostic signal and do not call it calibrated uncertainty.
- If constant or shuffled controls match the best causal candidate, Stage 11
  closes without a qualified component.
- No outcome changes the K01 promotion decision or authorizes Wave 6.

## Campaign Package

The approved preparation must create:

- campaign YAML and ten queue entries;
- a Python campaign driver;
- a dedicated PowerShell launcher with local and `-Remote` support;
- a matching launcher note;
- persistent prepared and completed campaign state;
- immutable per-entry artifacts;
- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- a Markdown results report and validated styled PDF.

## Launch Commands

Local preflight:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 -PreflightOnly
```

Local run:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 -Run
```

Remote preflight:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 -Remote -PreflightOnly
```

Remote run:

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage11_uncertainty_trust_calibration.ps1 -Remote -Run
```

## Approval

The technical document and this campaign plan are covered by the user's
temporary blanket approval recorded at `2026-07-29T15:30:41+02:00`, expiring at
`2026-07-30T15:30:41+02:00`.
