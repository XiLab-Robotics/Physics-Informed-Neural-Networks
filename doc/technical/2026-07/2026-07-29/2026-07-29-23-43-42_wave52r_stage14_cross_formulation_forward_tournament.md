# Wave 5.2R Stage 14 Cross-Formulation Forward Tournament

## Overview

Stage 14 audits every completed Wave 5.2R formulation against the six
predeclared tournament entry requirements, then compares the eligible roster on
raw error, centered shape, offset, harmonic fidelity, robustness,
interpretability, TwinCAT readiness, and balanced recommendation.

The scope remains exclusively `polished_dataset`, setpoint inputs, and `Fw`.
No training is planned. Existing held-out payloads and completed campaign
artifacts are read without changing checkpoints, thresholds, or registries.

The preliminary evidence indicates that H04, the bounded PF-A core-coefficient
correction from Stage 5, is the only formulation satisfying all six entry
requirements. K01 remains scientifically valuable but fails its complete
isolated gate and lacks the required three-seed continuation. The Stage 13 weak
residual is synthetic-only and cannot enter.

The technical document is covered by the user's active blanket approval. No
subagent is planned.

## Technical Approach

### Entry Audit

Each formulation receives explicit Boolean evidence for:

1. isolated gate passed;
2. three-seed evaluation completed;
3. matched control beaten;
4. leakage and causality checks passed;
5. complete full-curve payload available;
6. inference path inspectable.

An entrant must pass all six. Missing evidence is a failure, not an assumed
pass. Synthetic certification cannot substitute for real-data qualification.

The audit roster includes:

- Stage 4 residual-capacity candidates;
- Stage 5 H04 and H08;
- Stage 6 spectral, Sobolev, and weak-form candidates;
- Stage 7 mean and centered-shape candidates;
- Stage 8 weak-compliance candidates;
- Stage 9 K01 and other temporal residuals;
- Stage 10 sparse and symbolic candidates;
- Stage 11 uncertainty and trust candidates;
- Stage 12 advanced optimization candidates;
- Stage 13 synthetic-oracle diagnostics.

### Tournament Surface

Eligible entrants are compared with frozen non-entrant references:

- `PF_A_LOCAL_QUADRATIC`, the analytical anchor;
- accepted periodic harmonic MLP `Fw`, the harmonic-diagnostic reference;
- accepted periodic GRU `Fw`, the raw-error incumbent.

H04 and the references share compatible raw, centered-shape, and offset units.
Their currently stored harmonic metrics use different contracts, so direct
cross-formulation harmonic ranking is prohibited until Stage 15 places them on
the official common TE Curve Verification Pipeline surface.

For every category, the result distinguishes:

- entrant leader;
- incumbent or analytical reference leader;
- comparable evidence;
- unresolved evidence;
- readiness for official verification.

### Decision Contract

Because only one formulation is expected to enter, Stage 14 cannot claim broad
cross-formulation superiority. It may nominate H04 for Stage 15 official
forward verification if:

- every entry requirement is evidenced;
- H04 retains a genuine multi-index advantage over PF-A;
- its three-seed result is stable;
- no incompatible-unit metric is used to manufacture a win;
- the accepted GRU remains the incumbent until official verification.

This nomination is not registry promotion or official acceptance. If H04 fails
the audit, Stage 14 closes with no nomination and Stage 15 must not run a new
candidate.

## Involved Components

- Stage 0 frozen metrics and curve payloads provide the common references.
- Stage 4 through Stage 13 result reports and machine-readable campaign
  artifacts provide entry evidence.
- The Stage 5 H04 campaign and checkpoint provide the sole expected entrant.
- A repository-owned Stage 14 analysis script under
  `scripts/analysis/wave_5_2r/` will build the eligibility matrix, category
  matrix, evidence inventory, and decision artifact.
- A title-based Stage 14 analytical report bundle under
  `doc/reports/analysis/model_development_waves/wave_5_2/` will explain and
  preserve the result.
- A validated styled PDF, backlog update, ledger update, master-summary update,
  and Sphinx portal note will close the stage.

## Implementation Steps

1. Freeze the Stage 0, Stage 5, and completed Stage 4 through Stage 13 evidence
   paths and hashes.
2. Encode the six-entry-requirement matrix with one row per formulation family.
3. Validate that H04 is the only complete entrant and that synthetic or
   incomplete candidates remain excluded.
4. Build compatible raw, centered-shape, and offset comparisons against PF-A,
   the harmonic MLP, and the accepted GRU.
5. Record harmonic-contract incompatibility instead of ranking unlike units.
6. Audit three-seed robustness, interpretability, and TwinCAT readiness.
7. Produce the entrant, category, and balanced-decision artifacts.
8. Generate and visually validate the Markdown and styled PDF report.
9. Synchronize backlog, ledger, master summary, guide, and Sphinx portal.
10. Run repository QA and create the separately approved Stage 14 commit.
