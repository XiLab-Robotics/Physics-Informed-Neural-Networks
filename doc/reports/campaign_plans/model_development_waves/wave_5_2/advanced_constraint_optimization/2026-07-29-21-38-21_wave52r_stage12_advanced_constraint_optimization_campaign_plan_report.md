# Wave 5.2R Stage 12 Advanced Constraint Optimization Campaign Plan

## Campaign Scope

- Dataset: `polished_dataset`
- Inputs: setpoints only
- Surface: `Fw`
- First-screen seed: `314159`
- Conditional stability seeds: `271828`, `161803`
- Frozen analytical component: Stage 5 H04
- Frozen temporal reference: Stage 9 K01
- Planned first-screen entries: `10`

Stage 12 tests optimization methods, not new equations. Only the qualified H04
anchor and K01 causal coefficient-residual architecture are eligible.

## Scientific Question

Can an advanced optimizer improve the repeatability or curve-first accuracy of
K01 relative to the same architecture, data, split, budget, and standard AdamW
optimizer, while repairing periodic closure and preserving bounded analytical
corrections?

## Frozen Evidence Contract

The campaign must reproduce:

- the Stage 0 split signature and `97` test curves;
- the Stage 5 H04 coefficient and curve hashes;
- the Stage 9 K01 architecture and accepted checkpoint;
- the Stage 9 causal angular order and reset behavior;
- the same target normalization, harmonic order set, and curve length;
- the same deployment-facing chunk length.

Test labels cannot update weights, sampling probabilities, multipliers,
penalties, checkpoint choice, or candidate selection.

## Candidate Matrix

| ID | Optimization profile | Adaptive state |
| --- | --- | --- |
| C00 | frozen K01 replay | none |
| C01 | standard AdamW retrain | none |
| G01 | gradient-statistics balancing | training gradients |
| R01 | ReLoBRaLo-style balancing | training loss history |
| P01 | main-loss-preserving projection | per-component training gradients |
| S01 | self-adaptive curve weighting | bounded trainable curve logits |
| A01 | augmented Lagrangian | training closure and correction violations |
| U01 | curriculum regularization | deterministic epoch schedule |
| F01 | failure-informed resampling | prior-epoch training residuals |
| L01 | AdamW plus L-BFGS refinement | validation-selected deterministic refinement |

## Loss And Constraint Contract

The standard data objective retains K01's raw, mean, centered-shape, and
residual-magnitude terms. Advanced candidates may reweight or constrain only
declared components:

- raw point error;
- curve-mean error;
- centered-shape error;
- periodic closure;
- bounded coefficient-correction RMS.

Main-loss-preserving projection treats raw error as the protected gradient.
Augmented-Lagrangian multipliers update only from training violations.
Self-adaptive and failure-informed methods use bounded weights with a recorded
effective-sample-size floor.

## First-Screen Gates

A candidate must pass all applicable checks:

1. improve raw or centered-shape MAE by at least `1%` versus C01;
2. regress the complementary metric by no more than `0.5%`;
3. regress mean MAE and P95 absolute error by no more than `1%`;
4. reduce periodic closure error by at least `10%` versus C01;
5. meet reset reproducibility and the predeclared chunk-equivalence threshold;
6. remain inside the H04 coefficient-correction budget;
7. preserve finite gradients, losses, multipliers, and adaptive weights;
8. beat the frozen C00 reference on the complete curve-first comparison;
9. preserve inference cost and PLC state relative to K01;
10. pass method-specific disabled-adaptation or shuffled-weight controls.

If no candidate passes, stability is skipped and Stage 12 closes without
promotion.

## Conditional Stability

Only the strongest complete-gate candidate is repeated on seeds `271828` and
`161803`. It must pass the complete gate on all three seeds and improve either:

- median raw or centered-shape accuracy relative to the recorded standard-K01
  seed distribution; or
- repeatability, measured by a reduction of at least `10%` in the selected
  metric's inter-seed standard deviation.

## Required Artifacts

- campaign manifest and ten queue entries;
- local and `-Remote` PowerShell launcher;
- preflight validation summary;
- per-run metrics, predictions, history, gradient diagnostics, and optimizer
  state summary;
- campaign leaderboard, best-run YAML, best-run Markdown, and gate summary;
- Markdown result report and validated styled PDF;
- backlog, ledger, guide, master-summary, and Sphinx synchronization.

## Launch Commands

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -PreflightOnly

.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -Run

.\scripts\campaigns\wave_5_2\run_wave52r_stage12_advanced_constraint_optimization.ps1 `
  -Remote -Run
```

## Approval

The technical document and this campaign plan are approved under the user's
active blanket approval. Training may begin only after the code, configuration,
launcher, and preflight artifacts reproduce the frozen contract.
