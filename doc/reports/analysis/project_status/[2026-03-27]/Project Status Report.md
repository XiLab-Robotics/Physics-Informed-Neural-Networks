# StandardML - Codex Project Status Report

## Executive Summary

`StandardML - Codex` is now past the initial proof-of-concept stage.

The repository has evolved from a single feedforward baseline into a structured
TE modeling program with:

- multiple implemented model families;
- reusable training, smoke-test, and validation infrastructure;
- campaign planning and campaign results workflows;
- family-level and program-level best-result registries;
- styled PDF reporting;
- explanatory guides with `NotebookLM` source packages;
- repository-specific Codex skills and subagents for future workflow support.

The current project identity is clear:

- the target remains rotational transmission error (`TE`) in RV reducers;
- the current program compares practical machine-learning baselines rather than
  jumping prematurely into full PINNs;
- interpretability, engineering discipline, and future TwinCAT / PLC
  deployability remain first-class constraints rather than afterthoughts.

The current best program-level result is still the tree-based
`hist_gradient_boosting` model with:

- validation MAE: `0.002719 deg`
- test MAE: `0.002885 deg`

The strongest current neural challenger is now the residual-harmonic family
winner:

- run: `te_residual_h12_deep_joint_wave1`
- validation MAE: `0.003024 deg`
- test MAE: `0.003152 deg`

This means the repository has already produced a technically meaningful result:
the best overall solution is currently a compact tabular model, while the best
neural direction is a structured-plus-residual architecture that preserves more
deployment relevance and interpretability than a purely opaque network.

The later LAN-remote validation campaign did, however, improve one important
family-local benchmark:

- `te_feedforward_high_compute_remote` is now the best `feedforward` family
  run with validation MAE `0.003059 deg` and test MAE `0.003274 deg`.

## Project Goal And Framing

The repository studies machine-learning workflows for transmission error
modeling in RV reducers used in industrial robotics.

The long-term goal is not only to fit TE data offline.

The intended direction is to build models that are:

- accurate on measured operating conditions;
- interpretable enough for engineering analysis;
- structured enough for future export or simplified PLC-side use;
- extensible toward hybrid and later physics-informed formulations.

The project is therefore organized as a staged modeling program rather than a
single-model benchmark.

## Current Repository State

The current implemented surface can be summarized as follows.

| Area | Current State | Why It Matters |
| --- | --- | --- |
| Dataset handling | Validated TE dataset processing and point-wise training workflow are in place. | Keeps experiments aligned with the real test-rig data structure. |
| Training infrastructure | Shared training, smoke-test, validation, and LAN-remote campaign execution paths exist under `scripts/training/` and `scripts/campaigns/`. | New families can be added without rebuilding the workflow from scratch, and heavier runs can be delegated to the stronger workstation. |
| Implemented model families | `feedforward`, `harmonic_regression`, `periodic_mlp`, `residual_harmonic_mlp`, and `tree`. | The repository now compares multiple practical baselines instead of one architecture. |
| Experiment tracking | Output roots, campaign folders, family registries, and a program-level best registry are active. | Best-result selection is explicit and inspectable. |
| Reporting | Styled analytical PDFs and campaign-results PDFs can be exported and validated. | Results can be reviewed and shared in a disciplined format. |
| Learning material | Canonical guides, PDFs, and `NotebookLM` source packages exist for the main model topics. | The repository already supports onboarding and reusable educational output. |
| Deployment planning | TwinCAT / PLC-oriented evaluation has been framed and partially analyzed. | The project keeps deployment realism in scope early. |
| Codex workflow | Repository-specific skills and subagents now exist for campaigns, Markdown QA, reports, commit preflight, ML workflows, and testing strategy. | Future repository work can be executed more consistently and with lower process drift. |

## What Has Been Done So Far

## 1. Foundation Phase

The earliest work established the repository as a reproducible TE modeling
workspace rather than an ad hoc experiment folder.

Key outcomes:

- environment and dependency baseline;
- validated dataset-processing path;
- organized `scripts/`, `config/`, `doc/`, and `reference/` structure;
- project usage documentation and style alignment with the repository
  reference-code baselines.

Why this work mattered:

- it made later model implementation and reporting repeatable;
- it reduced ambiguity around folder ownership and workflow entry points;
- it created a documented baseline for future extensions.

## 2. Baseline Training And Reporting Phase

The next phase established the first runnable TE baseline and the first serious
analysis/report workflow.

Key outcomes:

- PyTorch Lightning feedforward baseline;
- improved training terminal behavior and environment consistency;
- first analytical training reports;
- styled Markdown-to-PDF reporting path;
- PDF validation as a required closeout step.

Why this work mattered:

- it turned the repository from a code scaffold into a measurable ML program;
- it made result communication part of the engineering workflow instead of an
  optional afterthought.

## 3. Wave 0 Shared Infrastructure Phase

After the initial baseline, the repository moved to shared infrastructure.

Key outcomes:

- common artifact schema;
- separate roots for training runs, smoke tests, validation checks, campaigns,
  and registries;
- reusable one-batch validation entry point;
- reusable smoke-test entry point;
- explicit family-aware training flow.

Why this work mattered:

- future model families could now enter the program with the same validation
  and artifact contract;
- cross-family comparison became much more reliable.

## 4. Structured Baseline Expansion Phase

The repository then expanded beyond the original feedforward baseline.

Implemented families now include:

- feedforward MLP baseline;
- harmonic regression;
- periodic-feature MLP;
- residual-harmonic MLP;
- tree-based tabular baselines.

Why this work mattered:

- it tested not only accuracy, but also the tradeoff between structure,
  interpretability, and raw predictive strength;
- it created a realistic bridge from fully tabular baselines to
  structured-neural approaches.

## 5. Campaign And Registry Discipline Phase

The repository next formalized campaign preparation and results bookkeeping.

Key outcomes:

- campaign plan reports became mandatory;
- campaign YAML generation and launcher creation were standardized;
- active campaign state and protected-file boundaries were introduced;
- campaign-level best-run artifacts and family/program registries became part of
  the canonical workflow.

Why this work mattered:

- large experiment batches could be reproduced and audited;
- result promotion stopped depending on manual folder inspection.

## 6. Guide, Diagram, And Educational Layer Phase

The project later invested heavily in human-readable explanation layers.

Key outcomes:

- canonical guides for neural foundations, training/validation/testing, TE
  curriculum, and the main implemented model families;
- model-report diagrams and structured explanatory visuals;
- styled guide PDFs;
- guide-local `NotebookLM` source packages and prompts.

Why this work mattered:

- the repository is no longer only an experiment store;
- it now explains the implemented work in a way that is reusable for learning,
  communication, and future integration.

## 7. Deployment Planning And Documentation Strategy Phase

The most recent work widened the project from pure model comparison to broader
engineering readiness.

Key outcomes:

- TwinCAT deployment evaluation framing;
- operational backlog and wave planning;
- README redesign as a GitHub-facing landing page;
- Codex-native skills and subagent customization for repository workflows.

Why this work mattered:

- it moved the repository closer to a maintainable engineering program rather
  than a local experiment notebook;
- it made future execution more systematic.

## Why The Work Was Done In This Order

The repository's progression is intentional rather than accidental.

| Decision | Reason |
| --- | --- |
| Build static baselines before temporal or PINN models. | The project needed interpretable and cheap comparisons before heavier architectures. |
| Add reporting discipline early. | Without reliable reports and validated PDFs, campaign outcomes would remain hard to review. |
| Add shared infrastructure before broad family expansion. | A common validation and artifact contract was needed before comparing families seriously. |
| Keep structured models in scope. | TE is periodic and partly interpretable, so purely black-box work would hide useful engineering structure. |
| Keep TwinCAT deployability in scope now. | The final target is not only offline score; practical runtime form matters. |
| Treat guides and `NotebookLM` packages as repository-owned assets. | Knowledge transfer is part of the project output, not an external side effect. |

## Current Model And Results Snapshot

### Family-Level Best Runs

| Family | Best Run | Val MAE [deg] | Test MAE [deg] | Status Note |
| --- | --- | ---: | ---: | --- |
| `tree` | `te_hist_gbr_tabular` | 0.002719 | 0.002885 | Current program leader |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1` | 0.003024 | 0.003152 | Strongest neural challenger |
| `feedforward` | `te_feedforward_high_compute_remote` | 0.003059 | 0.003274 | Current feedforward family best from the validated LAN-remote campaign |
| `periodic_mlp` | `te_periodic_mlp_h04_standard` | 0.003097 | 0.003317 | Competitive hybrid baseline |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery` | 0.017004 | 0.020782 | Structured reference, not performance leader |

### Campaign-Level Status

| Campaign | Scope | Outcome |
| --- | --- | --- |
| Wave 1 recovery campaign | Recover failed harmonic, residual, and random-forest branches. | Completed successfully and restored missing comparisons. |
| Wave 1 residual-harmonic family campaign | Familywise search inside the residual-harmonic family. | Completed successfully and promoted a stronger residual family anchor. |
| Remote LAN validation campaign | Validate the SSH-backed remote campaign path while probing heavier tree and feedforward runs. | Completed successfully, validated the remote workflow, and promoted a stronger `feedforward` family best without displacing the global tree leader. |

### Most Important Numerical Conclusion

The most important current model-selection conclusion is:

- tree-based tabular learning is still the strongest overall empirical
  solution;
- residual-harmonic modeling is the strongest current neural direction;
- the validated LAN path improves the plain `feedforward` family enough to keep
  it useful as a stronger baseline anchor;
- harmonic regression remains valuable mainly as an interpretable structured
  reference rather than a metric leader.

## Documentation And Communication Status

The documentation layer is now substantial enough to support both engineering
work and communication work.

Current status:

- the main repository README is GitHub-facing and concise;
- `doc/README.md` acts as the main documentation index;
- canonical guides exist for the major implemented model topics;
- guide-local `English/` export areas and `NotebookLM` package structures are
  already part of the repository pattern;
- styled report export and PDF validation tooling are repository-owned;
- repository-specific Codex skills and subagents are now part of the working
  environment.

This is important because the project is no longer blocked on "explainability"
or "reporting infrastructure" before communicating results externally.

## Current Objectives

Based on the current evidence, the most defensible current objectives are the
following.

### 1. Keep The Program-Level Comparison Honest

The repository should keep using the explicit registries and campaign reports to
compare families rather than promoting a neural model prematurely because it is
architecturally more attractive.

### 2. Preserve The Residual-Harmonic Family As The Main Neural Branch

The residual-harmonic family has earned its role as the strongest current
structured-neural direction and should remain the main neural comparison anchor.

### 3. Use The LAN Workstation Selectively

The stronger LAN workstation is now worth using for targeted campaigns where
the heavier compute budget can plausibly change the family-level picture:

- larger or longer `feedforward` sweeps;
- residual-harmonic family extensions with deeper or denser variants;
- narrow `hist_gradient_boosting` follow-ups.

The remote evidence does not currently justify broad random-forest expansion.

### 4. Open The Deployment Evaluation Branch Carefully

TwinCAT and PLC-oriented export feasibility is now a natural next step because
the repository has:

- a meaningful set of candidate models;
- explicit structured-vs-black-box comparisons;
- project references that motivate PLC-side constraints.

### 4. Prepare The Transition To Wave 2 And Wave 3

The approved roadmap still points toward:

- `Wave 2` temporal models;
- `Wave 3` hybrid structured models;
- later PINN preparation only after the formulation is technically justified.

## Gaps, Risks, And Cleanup Notes

The project is in a strong state, but not in a finished state.

The main open issues are:

- the global best solution is still a tree model, so the main neural line has
  not yet won the accuracy race;
- the stronger remote workstation did not make random forest attractive enough
  to justify it as a leading family;
- temporal families are approved but not yet implemented;
- the TwinCAT deployment branch is framed but not yet executed as a real model
  export comparison;
- some running-state text appears slightly behind the actual deliverables.

One concrete example of the last point:

- `doc/running/te_model_live_backlog.md` still describes the residual-harmonic
  campaign results report as pending;
- however, the report and PDF already exist under `doc/reports/campaign_results/`.

This suggests that backlog synchronization is itself now an important cleanup
task so the operational view matches the actual repository state.

## Recommended Next Steps

The most reasonable near-term next steps are:

1. reconcile the live backlog and running-state documents with the now-completed
   Wave 1 reporting outputs;
2. formalize the next TwinCAT deployment-evaluation branch using the already
   approved reference-analysis material;
3. keep the residual-harmonic winner as the neural reference point for the next
   comparison phase;
4. prepare `Wave 2` temporal-model implementation only after the current
   reporting and backlog cleanup is fully coherent;
5. preserve the current documentation and `NotebookLM` discipline so future
   work remains easy to explain and reuse.

## High-Level Future Roadmap

| Horizon | Main Goal | Expected Value |
| --- | --- | --- |
| Immediate | Wave 1 closeout cleanup and deployment-branch setup | Keeps the repository state coherent and actionable |
| Near-term | TwinCAT deployment evaluation + Wave 2 temporal preparation | Tests whether the current winners remain practical beyond offline metrics |
| Mid-term | Temporal and hybrid family implementation | Expands the candidate set beyond static baselines |
| Longer-term | PINN formulation and first constrained models | Introduces physics-informed structure only when the prerequisites are ready |

## Conclusion

The repository already delivers more than a model sandbox.

It now contains:

- a reproducible TE modeling workflow;
- multiple implemented model families;
- meaningful campaign and ranking evidence;
- reporting and PDF validation infrastructure;
- educational guides and `NotebookLM` source packages;
- an explicit engineering path toward future deployment and richer model
  families.

The main strategic conclusion is straightforward:

- the project has successfully built the foundation and the first serious
  comparison layer;
- the next challenge is no longer "can the repository run structured TE
  experiments?";
- the next challenge is "which direction should be promoted next while keeping
  deployment realism, documentation quality, and comparison discipline intact?".

## Artifact References

- Program-level best registry:
  `output/registries/program/current_best_solution.yaml`
- Family-level best registries:
  `output/registries/families/`
- Live backlog:
  `doc/running/te_model_live_backlog.md`
- Current campaign state:
  `doc/running/active_training_campaign.yaml`
- Wave 1 recovery report:
  `doc/reports/campaign_results/wave1/2026-03-24-15-49-42_wave1_structured_baseline_recovery_campaign_results_report.md`
- Wave 1 residual family report:
  `doc/reports/campaign_results/wave1/2026-03-27-11-50-27_wave1_residual_harmonic_family_campaign_results_report.md`
- TE roadmap:
  `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- TE implementation backlog:
  `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
