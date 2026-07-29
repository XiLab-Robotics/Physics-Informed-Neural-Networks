# Wave 5.2R Stage 13 Synthetic And Weak-Form Oracle Lane Campaign Plan

## Campaign Scope

- Dataset domain: `polished_dataset`
- Inputs: setpoints only
- Surface: `Fw`
- Oracle seed: `314159`
- Frozen representation: Stage 5 H04 Polynomial-Fourier
- Planned entries: `10`
- Real-data model promotion: prohibited

Stage 13 is a bounded analytical certification campaign. It uses real-data
scales and operating conditions to construct deterministic synthetic truths,
but no measured test label selects a formulation or threshold.

## Scientific Questions

1. Can the implemented analytical paths recover known harmonic, coefficient,
   anchor, and compliance perturbations?
2. Does a weak harmonic residual retain specificity while reducing
   derivative-noise sensitivity?
3. What angular sampling density is required for a reliable decision?
4. Do wrong-law and shuffled-angle controls fail as required?

## Frozen Evidence Contract

The campaign must reproduce:

- the Stage 0 `Fw` split signature;
- the Stage 5 H04 core order list, anchor coefficients, and curve scale;
- `64` deterministically selected training-domain oracle conditions;
- angular densities `2048`, `1024`, `512`, `256`, and `128`;
- normalized noise levels `0`, `0.001`, `0.005`, and `0.01`;
- seed `314159`;
- all parameter and residual gates declared below.

Test curves are used only to verify provenance counts. Synthetic cases are
derived from training-domain H04 anchors and known analytical perturbations.

## Candidate Matrix

| ID | Experiment | Primary evidence |
| --- | --- | --- |
| C00 | exact H04 reconstruction | coefficient and curve round-trip |
| H01 | harmonic injection | injected-order amplitude recovery |
| H02 | harmonic omission | incomplete-basis error ratio |
| C01 | coefficient-surface perturbation | known correction recovery |
| M01 | misspecified anchor | residual correction recovery |
| Q01 | compliance nonlinearity | nonlinear torque coefficient recovery |
| P01 | pointwise oscillator residual | derivative-noise baseline |
| W01 | weak oscillator residual | integrated residual robustness |
| D01 | density stress | minimum passing sample count |
| N01 | wrong-law and shuffled controls | residual specificity |

## Predeclared Gates

- exact reconstruction maximum absolute error: `1e-10`;
- coefficient recovery normalized RMSE: at most `0.02`;
- harmonic omission error ratio: at least `5`;
- compliance coefficient relative error: at most `0.05`;
- weak residual noise inflation: below pointwise inflation at every non-zero
  noise level for densities at or above `256`;
- weak correct-law residual: below `0.02` at density `256` and noise `0.01`;
- wrong-order rejection ratio: at least `10`;
- shuffled-angle rejection ratio: at least `10`;
- deterministic replay difference: `0`;
- no test-label dependence and no synthetic-to-real promotion.

Each case receives one of `certified_for_synthetic_use`,
`implementation_valid_but_power_limited`, `rejected`, or `blocked`.

## Required Artifacts

- campaign manifest and ten queue entries;
- local and `-Remote` PowerShell launcher;
- preflight validation summary;
- per-case YAML/CSV metrics and oracle provenance;
- campaign leaderboard, best-run YAML, best-run Markdown, and certification
  summary;
- Markdown result report and validated styled PDF;
- backlog, ledger, guide, master-summary, and Sphinx synchronization.

## Launch Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -Run

.\scripts\campaigns\wave_5_2\run_wave52r_stage13_synthetic_weak_form_oracle_lane.ps1 `
  -Remote -Run
```

## Approval

The technical document and this campaign plan are approved under the user's
active twenty-four-hour blanket approval. Execution may begin after the code,
configuration, launcher, and preflight reproduce this contract.
