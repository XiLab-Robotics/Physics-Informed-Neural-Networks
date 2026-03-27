<!-- markdownlint-disable MD025 -->

# StandardML - Codex

## Project Status Overview

- TE modeling workflow for RV reducer transmission error
- current focus: reproducible comparison of practical ML baselines
- long-term direction: hybrid and later physics-informed models

---

## Why This Project Exists

- transmission error is a key reducer accuracy signal
- the repository targets both predictive accuracy and engineering usability
- deployment realism matters, especially for future TwinCAT / PLC paths

---

## Current Repository Identity

- no longer a single-model prototype
- now a structured TE modeling program
- includes training, validation, smoke-test, campaign, report, and guide layers

---

## What Has Already Been Built

- validated TE dataset workflow
- shared training and verification infrastructure
- styled PDF reporting pipeline
- campaign planning and campaign-results discipline
- educational guides and `NotebookLM` source packages

---

## Implemented Model Families

- `feedforward`
- `harmonic_regression`
- `periodic_mlp`
- `residual_harmonic_mlp`
- `tree`

Each family now lives inside the same artifact and evaluation structure.

---

## Best Current Results

| Family | Best Test MAE [deg] |
| --- | ---: |
| `tree` | 0.002885 |
| `residual_harmonic_mlp` | 0.003152 |
| `feedforward` | 0.003301 |
| `periodic_mlp` | 0.003317 |
| `harmonic_regression` | 0.020782 |

---

## Main Technical Conclusion

- the current global leader is still `hist_gradient_boosting`
- the strongest neural direction is now `residual_harmonic_mlp`
- harmonic regression remains valuable mainly as a structured reference

---

## Why The Work Was Done This Way

- structured baselines before heavier models
- shared infrastructure before broad family expansion
- reporting discipline before large campaign growth
- documentation and explainability treated as core project assets

---

## Documentation And Communication Layer

- GitHub-facing `README`
- `doc/README.md` documentation index
- canonical guides with PDFs
- `NotebookLM` source packages for video-oriented reuse
- repository-owned Codex skills and subagents

---

## Current Objectives

- keep model comparison honest through registries and campaign reports
- preserve residual harmonic as the main neural branch
- open the TwinCAT deployment evaluation track carefully
- prepare the transition to Wave 2 temporal models

---

## Important Open Gaps

- neural models have not yet overtaken the tree leader
- temporal families are still pending
- deployment evaluation is planned but not yet executed
- the live backlog needs synchronization with the latest delivered reports

---

## Recommended Next Steps

1. update the live backlog and running-state view
2. formalize the TwinCAT deployment evaluation branch
3. keep the residual winner as the neural reference anchor
4. prepare Wave 2 temporal implementation
5. preserve the current documentation and reporting discipline

---

## Strategic Takeaway

The repository has already built the foundation and the first serious
comparison layer.

The next question is no longer whether the project can run structured TE
experiments.

The next question is which direction should be promoted next without losing
deployment realism, documentation quality, and comparison discipline.
