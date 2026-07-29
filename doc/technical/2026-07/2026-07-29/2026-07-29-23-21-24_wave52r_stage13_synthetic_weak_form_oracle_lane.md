# Wave 5.2R Stage 13 Synthetic And Weak-Form Oracle Lane

## Overview

Stage 13 tests physics-guided formulations that are mathematically meaningful
but cannot be identified or falsified completely from the current real-data
contract. The scope remains exclusively the operating domain represented by
`polished_dataset`, setpoint inputs, and `Fw`.

The lane uses the frozen Stage 0 split and Stage 5 H04 Polynomial-Fourier
representation to define realistic condition grids, coefficient scales,
harmonic orders, and bounded perturbations. Known synthetic ground truth is
then used to measure recovery power, failure detection, noise sensitivity, and
sampling-density requirements.

Synthetic success validates an equation implementation or diagnostic. It does
not prove that the same equation is the true mechanism in the measured reducer.
No synthetic candidate can be promoted directly into the Stage 14 real-data
tournament.

The technical document and campaign plan are covered by the user's active
blanket approval. No subagent is planned.

## Technical Approach

### Frozen Oracle Contract

Every oracle case records:

- the frozen Stage 0 split and H04 provenance;
- the exact analytical generator and its parameters;
- the synthetic truth before corruption;
- deterministic noise and sampling seeds;
- the estimator or residual under test;
- recovery error, detection power, and negative-control behavior;
- a declared statement of what the result can and cannot establish.

The bounded matrix contains ten entries:

| ID | Oracle experiment | Purpose |
| --- | --- | --- |
| C00 | exact H04 reconstruction control | certify the unperturbed analytical path |
| H01 | controlled harmonic injection | recover a known added harmonic |
| H02 | controlled harmonic omission | detect an intentionally incomplete basis |
| C01 | coefficient-surface perturbation | recover condition-dependent coefficient changes |
| M01 | misspecified-anchor recovery | quantify correction from a biased H04 anchor |
| Q01 | synthetic compliance nonlinearity | identify a known torque-nonlinear response |
| P01 | pointwise oscillator residual | establish the derivative-sensitive baseline |
| W01 | weak-form oscillator residual | avoid differentiating corrupted observations |
| D01 | sampling-density stress | map the minimum useful angular density |
| N01 | wrong-law and shuffled-angle controls | prove residual specificity |

### Weak-Form Certification

For a known harmonic component satisfying
`u''(theta) + n^2 u(theta) = 0`, the pointwise lane estimates derivatives from
sampled curves. The weak lane transfers derivatives to smooth periodic test
functions through integration by parts. Both lanes are evaluated at identical
noise levels and angular densities.

The weak formulation qualifies only if it:

- remains near zero for the correct harmonic law;
- rejects a wrong harmonic order and shuffled-angle control;
- has lower normalized residual inflation than the pointwise formulation under
  non-zero noise;
- preserves the decision over the declared density range;
- reproduces exactly with the fixed seed.

### Recovery And Boundary Gates

Injection, omission, coefficient, anchor, and compliance cases must recover
their known parameters within predeclared normalized tolerances. Detection
results include false-positive behavior on C00. Noise and density thresholds
are fixed before the campaign is run.

The campaign can conclude:

- `certified_for_synthetic_use`;
- `implementation_valid_but_power_limited`;
- `rejected`;
- `blocked`.

No outcome changes the real-data Stage 9 leader or authorizes a physical claim.
Stage 14 may consume only already qualified real-data candidates; it may cite
Stage 13 as implementation or observability evidence.

## Involved Components

- The Stage 5 H04 dataset builder and Polynomial-Fourier utilities provide the
  frozen forward-domain representation.
- A Stage 13 analytical-oracle module under `scripts/models/` will implement
  deterministic generators, estimators, and pointwise and weak residuals.
- A Stage 13 campaign driver under `scripts/campaigns/wave_5_2/` will execute
  the ten-entry matrix and write immutable evidence.
- Campaign YAML and queue entries will live under
  `config/training/synthetic_weak_form_oracle_lane/`.
- A dedicated PowerShell launcher and launcher note will support local and
  `-Remote` execution.
- Campaign artifacts will use the immutable campaign and validation-check
  directory conventions.
- A model report, campaign result report, styled PDF, backlog update, ledger
  update, usage-guide update, and Sphinx API page will close the stage.

## Implementation Steps

1. Freeze Stage 0, H04, harmonic-order, perturbation, noise, and density
   provenance.
2. Create the campaign plan, ten-entry queue, launcher contract, and analytical
   formulation report.
3. Implement deterministic harmonic, coefficient, anchor, and compliance
   oracle generators.
4. Implement pointwise finite-difference and weak periodic-test residuals.
5. Add exact-reconstruction, parameter-recovery, repeatability, wrong-law,
   shuffled-angle, leakage, and boundary preflight checks.
6. Execute the bounded ten-entry campaign.
7. Generate per-case metrics, observability maps, certification decisions, and
   explicit synthetic-to-real limitations.
8. Produce and visually validate the Markdown and styled PDF closeout.
9. Synchronize backlog, ledger, guide, master summaries, and Sphinx portal.
10. Run repository QA and create the separately approved Stage 13 commit.
