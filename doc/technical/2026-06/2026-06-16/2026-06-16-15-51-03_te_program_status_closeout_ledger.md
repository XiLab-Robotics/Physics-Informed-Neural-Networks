# TE Program Status And Closeout Ledger

## Overview

This technical note prepares an official, maintainable replacement for the
informal Transmission Error modeling status summary that has been copied across
past chats and manually extended after later campaign and `Track 2` closeouts.

The requested repository change has two durable outcomes:

- create a canonical program-status ledger that summarizes the current
  branch-parallel `Track 2` and wave history from `Wave 1` through the latest
  `Wave 3` and `Track 2H` evidence;
- update campaign closeout rules so every future closeout refreshes that
  ledger when the campaign changes modeling status, accepted leaders, Track 2
  verification state, roadmap position, or next-step decisions.

The ledger must replace stale narrative fragments rather than preserve them as
historical truth. It should reflect current repository state, not the older
pre-`Track 2G` plan.

## Technical Approach

The official ledger will be an authored Markdown analysis document under
`doc/reports/analysis/`, with a title-based filename so it can be kept current
across many future closeouts without creating a new dated report for every
small update.

The document will use the repository's current evidence hierarchy:

- accepted reference and direction-parallel leaders from
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- official `Track 2` verification reports through the current `Wave 3`
  refresh dated `2026-06-15`;
- campaign-results reports for `Track 2G`, the three completed `Track 2H`
  packages, and the first real `Wave 3` campaign;
- roadmap documents that explain the transition from curve-aware losses to
  dispersion-aware probes, structured harmonic priors, and later `Wave 4` /
  multi-head integration.

The ledger will keep the central modeling boundary explicit:

- runtime inference remains pointwise or causal-short-history only;
- full TE curves remain valid for offline training grouping, evaluation,
  diagnostics, checkpoint selection, and promotion decisions;
- `Fw`, `Bw`, and `global` remain parallel decision surfaces rather than one
  destructive scalar competition.

## Involved Components

The implementation will touch documentation and governance files only:

- `doc/reports/analysis/TE Program Status And Closeout Ledger.md` as the new
  canonical maintained ledger;
- `doc/README.md` to register the new official analysis document and this
  technical note;
- the repository closeout governance surface, expected to include `AGENTS.md`,
  so campaign closeouts explicitly require checking and updating the ledger
  when applicable;
- possibly `doc/running/te_model_live_backlog.md` or related running-state
  notes if the existing closeout checklist is more specific there than in
  `AGENTS.md`.

The content will be grounded in these already-present evidence sources:

- `Track 2B` curve-first reranking;
- `Track 2C` curve-payload diagnostics;
- mean-centered and `Track 2D` offset audits;
- `Track 2E` offset-predictability feasibility;
- `Track 2F` and `Track 2F-bis` offset-aware probes;
- `Track 2G` curve-aware training and official verification;
- `Track 2H` robust-loss, quantile/probabilistic, and mixture-density packages;
- first real `Wave 3` harmonic-prior residual training and official `Track 2`
  verification;
- earlier `Wave 1`, `Wave 2`, `Wave 2B`, and `Wave 2C` campaign and report
  milestones needed to make the ledger complete.

No subagent is planned for this work. If a later implementation pass needs a
subagent for broad report reconciliation, it must be proposed with an explicit
scope and wait for user approval before launch.

## Implementation Steps

1. Read the current repository evidence listed above, including the most recent
   official `Track 2` report and active campaign state.
2. Draft the official ledger with a current-state narrative, a chronological
   wave / track table, current direction-parallel leaders, and update rules for
   future closeouts.
3. Add the ledger to `doc/README.md` under the analysis-report index.
4. Update the campaign closeout governance rule so each closeout checks whether
   the ledger must be updated and records the result.
5. Run Markdown QA on the touched authored Markdown scope:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
6. Stop after completion and wait for explicit commit approval, preserving the
   repository's final approval gate.
