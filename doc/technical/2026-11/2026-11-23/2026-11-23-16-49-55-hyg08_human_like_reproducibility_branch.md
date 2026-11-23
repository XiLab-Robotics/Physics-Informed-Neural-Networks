# HYG-08 — Human-Like Reproducibility Branch

Date: 2026-11-23. Status: OWNER-APPROVED SCOPE / IMPLEMENTATION IN PROGRESS.
Canonical R&D baseline: `main@0f4e7a31d4fefe95b169f882fd15ada8c35574a8`. Working branch: `human-like`.
Cross-repository design: [HYG-08 approved matrix](https://github.com/XiLab-Robotics/Transmission-Error-Modeling/blob/main/Documentation/PINNs_HYG08_HumanLike_Executable_Design_and_Model_Matrix_2026-11-23.md).

## Overview

Build a human-readable, publication-oriented branch inside the existing PINNs repository, preserving the full R&D `main` and immutable `track2-portable` ref. Keep only the complete polished dataset, the faithful modernized RCIM harmonic-bank workflow (both directions, setpoints and actual values), and 12 selected DirectML families (23 direction-specific ONNX leaves). Remove A02, all global exports/trainers, raw/simplified datasets, experimental Waves/Track2, AI/Codex skills, bulky reports and unneeded branches/tools **from the new branch tree only**. No Git history rewrite.

Owner confirmation: the current conversation explicitly approved the entire 12-KEEP/28-OMIT family list, the full RCIM modern reimplementation, Fw/Bw only, and the proposed simplified usage/structure, and requested implementation. This document precedes functional code changes in the working branch. It does not authorize new scientific training or PLC operations.

## Technical Approach

1. Inventory existing Git trees, ONNX and checkpoint metadata; reuse the exact existing Git object SHAs for polished data and accepted model artifacts without modifying their bytes. Exclude `global` from the final worktree, including archived RCIM global.
2. Preserve the RCIM exact-paper training algorithm and its 10 populated, 19-target promoted families per direction; retain ELM capability in source if required, but do not claim pre-trained ELM checkpoint existence. Both `setpoints` and `actual_values` feature modes remain distinguishable; do not reinterpret input tensors.
3. Retain only the selected DirectML baselines, four physically exercised families (HR12, PMH7, RHMLP16, PMLP6), K01 temporal offline specialist, H08 forward-only specialist, GRU temporal reference and standard GRU/LSTM/TCN. Eliminate A02 and other global-only/hybrid experimental exports from the new branch.
4. Provide a concise README and one CLI for dataset validation, model catalog, safe bounded inference, historical RCIM train delegation and explicit DirectML training. Separate exact-historical protocols from modern fresh-dataset split; never mix metrics. Use deterministic run IDs and simple `results/` outputs.
5. Exclude original raw data, copied legacy author code, Codex/agents/skills, technical/reports approval machinery, Sphinx/Pages and TestRig/Standalone submodules in the **final branch worktree**. This implementation document remains in Git history as the predecessor design.
6. Respect Git LFS pointer behavior. If a retained Python checkpoint depends on inaccessible LFS material or source-run extras, classify it as unverified; do not fabricate model parity or claim replay without actual execution.

## Involved Components

- Input: `data/polished_dataset/forward`, `backward` and immutable source split manifest.
- Legacy: `scripts/paper_reimplementation/rcim_ml_compensation/{exact_paper_model_bank,original_dataset_exact_model_bank,harmonic_wise_comparison}`, `scripts/datasets`, `scripts/training/shared_training_infrastructure.py`, 10 promoted RCIM families under `models/polished_dataset/paper_reference/rcim_track1/` per mode/direction.
- DirectML: selected model classes, training DataModule, model factory, serialised ONNX/torch checkpoints and archived metadata under `models/polished_dataset/setpoints/`.
- Read-only external boundaries: Standalone `main@9c07180b`, TestRig `4026@6f7c4cec`; no runtime build, reusable gitlink or commissioning.

## Implementation Steps

- [ ] HYG-08B: verify available Git tree names, source SHA, dataset Fw/Bw and 12-model direction matrix.
- [ ] HYG-08C: publish branch and this technical document; finalize compact source tree from preserved immutable Git objects.
- [ ] HYG-08D: wire legacy/DirectML entrypoints and remove unused imports/paths without modifying algorithmic numerical contracts.
- [ ] HYG-08E: complete simple config/catalog/CLI/README/requirements and gitignored output.
- [ ] HYG-08F: run bounded import, syntax, data integrity and inference/parity tests (only where full runtime and artifacts are genuinely accessible); no heavy train or runner without verified budget.
- [ ] HYG-08G: independent GitHub branch/commit inventory, exact SHA comparisons, project memory/backlog and issue update; report remaining gates separately.

## Acceptance and Risk Gates

No `global`, `AGENTS.md`, `.codex/`, experimental models, raw dataset or TestRig submodules in final branch tree. `main`/`track2-portable` must remain unchanged. All 12 selected families and each source artifact required for inference/training must have verified paths; 10 published RCIM families and Fw/Bw in two source input modes remain intact. If local runtime, ONNX parity, scientific resolver or heavy CPU task is unavailable, report `CI_GATE_BLOCKED` or `UNVERIFIED`, never PASS. No automatic trained-model export overwrite or deployment claim.
