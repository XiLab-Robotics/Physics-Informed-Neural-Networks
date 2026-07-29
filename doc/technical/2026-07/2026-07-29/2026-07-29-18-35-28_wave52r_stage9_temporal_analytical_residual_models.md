# Wave 5.2R Stage 9 Temporal Analytical-Residual Models

## Overview

This project implements Stage 9 of the approved `Wave 5.2R` roadmap for the
`polished_dataset`, setpoint-only, forward (`Fw`) surface.

The stage tests whether causal angular context adds held-out predictive
information beyond static operating conditions and whether a structured
analytical anchor makes that temporal information easier to learn. The
accepted periodic GRU remains the required temporal benchmark, while Stage 5
H04 remains the qualified structured coefficient component.

The available files are steady-state angular curves. They do not provide
ordered load histories, reversal trajectories, or changing setpoints within a
curve. Therefore this stage can identify value in causal *angular context* but
cannot claim identification of mechanical memory across operating states.

This technical document is approved automatically under the user's blanket
approval recorded at `2026-07-29T15:30:41+02:00` and valid through
`2026-07-30T15:30:41+02:00`.

## Technical Approach

### Evidence And Split Contract

The campaign will reuse the frozen Stage 0 contract:

- `966` accepted forward curves;
- `675 / 194 / 97` train, validation, and test curves;
- common split signature
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- setpoint inputs only;
- no measured TE, future TE, centered target, offline coefficient, or target
  statistic at inference;
- exact `2048`-point uniform angular representation for curve-first
  evaluation.

### Causal Sequence Contract

New recurrent arms will use unidirectional GRUs with `batch_first=True`.
Hidden state will be an explicit zero tensor shaped
`(num_layers, batch_size, hidden_size)` at reset. The final hidden state may be
carried only across contiguous chunks of the same curve and must be reset at
every curve boundary.

The PyTorch GRU contract returns per-timestep outputs plus final hidden state;
omitting `h_0` also creates zeros, but Stage 9 will construct it explicitly so
deployment and reset behavior are inspectable. Bidirectional recurrence,
centered windows, future angular samples, and target-derived warm starts are
forbidden in new candidates.

### Benchmark And Candidate Ladder

The first screen will include:

| ID | Formulation | Purpose |
| --- | --- | --- |
| `D00` | frozen Stage 5 H04 | static structured baseline |
| `G00` | accepted periodic GRU replay | required external temporal benchmark |
| `C00` | causal periodic GRU | matched causal temporal control |
| `R00` | parameter-matched residual GRU without anchor | data-only residual control |
| `P01` | frozen PF-A plus causal residual GRU | analytical-residual candidate |
| `H01` | frozen H04 plus causal residual GRU | qualified-anchor candidate |
| `K01` | H04 coefficient-residual GRU | structured coefficient candidate |
| `M01` | static mean plus causal temporal shape | explicit component candidate |
| `L01` | H04 residual GRU with sequence-length curriculum | context curriculum |
| `N01` | shuffled angular-order residual GRU | temporal-specificity control |

The accepted periodic GRU uses its historical centered-window contract and is
therefore reported as an external benchmark, not as proof of causal
deployability. New candidates must beat it on the common Stage 0 test surface
without using its non-causal centered readout.

### Training And Diagnostics

The first screen will use seed `314159` and bounded epochs. Candidate
continuation to seeds `271828` and `161803` is conditional on complete
first-screen gate passage.

Every candidate will report:

- raw MAE and RMSE;
- curve-mean and centered-shape MAE;
- derivative and Sobolev agreement;
- periodic closure;
- retained harmonic amplitude and phase;
- per-curve P95 and worst-case MAE;
- residual-to-anchor magnitude;
- hidden-state norm and reset reproducibility;
- prefix-length sensitivity;
- prediction difference under shuffled angular order;
- runtime target-derived input count.

### Exit Gate

A promotable hybrid must:

1. beat frozen H04;
2. beat the accepted periodic GRU on the same Stage 0 test surface;
3. beat the parameter-matched data-only residual control;
4. beat the shuffled-order specificity control;
5. improve raw and curve-mean error;
6. preserve or improve centered shape, derivative, closure, harmonic
   amplitude, phase, and P95;
7. produce identical output after repeated explicit zero-state resets;
8. remain finite and bounded for every prefix length;
9. pass all gates for seeds `314159`, `271828`, and `161803`.

Scalar MAE or campaign rank alone cannot promote a candidate.

## Involved Components

- `reference/` and `doc/reference_summaries/` for analytical, harmonic, and
  deployment constraints;
- Stage 0 frozen split and evidence artifacts;
- Stage 1 technique register;
- Stage 5 H04 checkpoint and coefficient representation;
- accepted `periodic_gru_sequence_Fw` checkpoint and registry;
- existing temporal data and model utilities;
- a Stage 9 causal analytical-residual model module;
- a dedicated Stage 9 campaign runner and local/remote PowerShell launcher;
- campaign YAML, queue, state, results, closeout plots, Markdown, and PDF;
- roadmap, backlog, ledger, master summaries, usage guide, and Sphinx portal.

No subagent is planned or authorized for this stage.

## Implementation Steps

1. Create and approve the preliminary campaign plan.
2. Freeze exact H04 and accepted-GRU provenance.
3. Validate Stage 0 split coverage and the causal sequence construction.
4. Implement explicit GRU state initialization, reset, and chunk carry.
5. Implement the ten-candidate benchmark and ablation ladder.
6. Add reset reproducibility, prefix, shuffle, residual, and curve-first
   diagnostics.
7. Generate campaign YAML files, queue files, state, launcher, and launcher
   note.
8. Run compile, autograd, shape, leakage, and deterministic-reset preflight.
9. Execute the bounded first screen.
10. Continue only complete gate passers to the two additional seeds.
11. Generate the campaign-results Markdown and styled PDF.
12. Validate the real PDF and visually inspect every rendered page.
13. Synchronize roadmap, backlog, ledger, master summaries, usage guide, and
    Sphinx portal.
14. Run Markdown, Python, PowerShell, Sphinx, PDF, and Git preflight checks.
15. Commit the complete Stage 9 scope under the active blanket approval.
