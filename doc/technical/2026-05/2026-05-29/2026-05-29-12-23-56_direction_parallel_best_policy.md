# Direction-Parallel Best Model Policy

## Overview

This document plans the documentation correction for the TE model selection
policy after the `Track 2B` and `Track 2C` curve-first work.

The project must carry three best-model surfaces in parallel:

- one best model for forward motion, `Fw`;
- one best model for backward motion, `Bw`;
- one best model for the combined global surface, `global`.

These surfaces must not be collapsed into a single winner. A strong `Fw`
candidate must not displace the `Bw` or `global` branch, and a strong `Bw`
candidate must not displace the `Fw` or `global` branch. The real deployment
program needs all three surfaces because the final application may need
direction-specific compensation and a deployable cross-direction fallback or
global model.

No subagent is planned for this documentation correction.

## Technical Approach

The implementation should update the repository documentation so future
training, reranking, validation, and closeout decisions use a
direction-parallel interpretation.

The correction should:

- replace ambiguous single-winner language with direction-parallel wording;
- keep `Fw`, `Bw`, and `global` as separate best-model tracks;
- clarify that `Track 2B` and `Track 2C` identify leaders per surface rather
  than one global replacement;
- keep `periodic_gru_sequence_Bw` as the strongest practical screened
  repository-owned backward candidate from `Track 2C`;
- keep `periodic_lstm_sequence_global` as the strongest screened neural global
  candidate from `Track 2C`;
- keep the forward branch open even when a paper-reference forward candidate
  currently leads the screened diagnostics;
- preserve the causal runtime input boundary.

This is a documentation and policy synchronization task. It must not launch
training, modify model code, or update registries.

## Involved Components

Primary documentation targets:

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/track2/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`
- `doc/reports/analysis/track2/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/README.md`

Secondary documentation targets, if wording is affected:

- `doc/guide/project_usage_guide.md`
- Sphinx sources under `site/`

Current evidence to preserve:

- `Track 2B` forward leader: `rcim_retuned_GBM19_Fw`;
- `Track 2B` backward leader: `rcim_retuned_GBM19_Bw`;
- `Track 2B` global-surface leader: `periodic_lstm_sequence_global`;
- `Track 2C` strongest practical repository-owned backward candidate:
  `periodic_gru_sequence_Bw`;
- `Track 2C` strongest screened neural global candidate:
  `periodic_lstm_sequence_global`;
- `tree` should not become the next sole branch despite scalar strength.

## Implementation Steps

1. Inspect the touched `Track 2B`, `Track 2C`, live backlog, master summary,
   and curve-first strategy documents for single-winner wording.
2. Update the language so `Fw`, `Bw`, and `global` best-model surfaces are
   explicitly parallel branches.
3. Add a short direction-parallel rule to the live backlog.
4. Update the master summary executive snapshot and takeaways so the next work
   is framed as parallel direction/surface advancement, not a single model
   competition.
5. Update the `Track 2B` and `Track 2C` reports so their decisions are read as
   surface-specific evidence.
6. Update `doc/README.md` if the new technical document or policy report needs
   indexing.
7. Run Markdown QA on touched authored Markdown.
8. Run Sphinx only if the portal-facing scope changes.
9. Stop after reporting completion; do not commit until the user explicitly
   requests it.
