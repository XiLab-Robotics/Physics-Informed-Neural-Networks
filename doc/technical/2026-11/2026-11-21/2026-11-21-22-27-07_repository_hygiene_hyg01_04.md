# Repository Hygiene HYG-01 to HYG-04: Sphinx, Documentation, Model Catalog and Submodules

**Created:** 2026-11-21 22:27:07 Europe/Rome (local system clock)
**Source baseline:** `XiLab-Robotics/Physics-Informed-Neural-Networks/main@c207c9aac5c802cdf56a3bbaa0dd22548a6471bb`
**Scope:** [HYG maintenance register, issue #2](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/issues/2)
**Owner direction:** Apply HYG-01/02/03/04 now, without a technical-plan approval pause; review branches only after these four fixes.
**Execution branch:** `maintenance/hyg01-04-sphinx-docs-models-submodules-20261121`

## Overview

Apply strictly conservative maintenance to the canonical scientific repository, preserving all historic reports, datasets, models, configs, output artifacts and the comprehensive documentation index. No training, model inference experiments, PLC/XAE build, TestRig source edit, TestRig runtime change, branch deletion, artifact cleanup, or simplified-pipeline implementation is authorized by this scope. The future minimal RCIM/DirectML branch is separate.

The user explicitly requested immediate execution of these four scoped items and waived the technical-document review pause for this work. Main is protected; prepare a reviewable feature branch and respect the existing pull-request checks and merge policy.

## Technical Approach

### HYG-01: Restore documentation CI and Pages build

The last inspected Pages run `32967999620` stopped in `python -m sphinx -W` with six Sphinx autodoc import warnings: `ModuleNotFoundError: No module named 'onnx'`. Both `.github/workflows/ci.yml` and `.github/workflows/publish-sphinx-pages.yml` already install `site/requirements-docs.txt`, which lacks ONNX. Introduce `onnx>=1.21,<2.0`, matching `requirements-twincat-onnx-conversion.txt`. Do not touch the base training requirements or workflow runtime behavior unless new evidence proves the first correction insufficient.

GitHub currently reports this parent repository as public and the two existing workflows use the standard GitHub-hosted `ubuntu-latest` runner. Public standard runner execution is free per the GitHub-hosted runner documentation. Verify actual CI results from the pull request; *do not* treat the dependency correction or a passing Sphinx build alone as proof of successful GitHub Pages publication. Publication requires a distinct successful main-branch deploy receipt.

### HYG-02: Correct current documentation inconsistencies without deletions

- Rename the stale root heading `StandardML - Codex` to `Physics-Informed Neural Networks`.
- Correct current, live-facing RCIM model archive links from `models/paper_reference/rcim_track1/` to `models/polished_dataset/paper_reference/rcim_track1/`.
- Distinguish existing sequence-model families (GRU, LSTM, TCN and variants) from future model development: these are implemented/archived, not all future work.
- Make the Sphinx Pages URL a configured publication target, not an unverified deployment claim.
- Preserve every historical document, report and root `doc/README.md` listing. Register this plan in the canonical index without rewriting or pruning its existing entries.
- Validate current local README Markdown links against GitHub paths before writing.

### HYG-03: Reconcile the model catalog against the authoritative YAML

`models/polished_dataset/setpoints/model_development_export_inventory.yaml` declares `entry_count: 114`, with `forward: 39`, `backward: 37` and `global: 38`; all 114 say `exported`. The leaf `integrated_specialist_a02/global/reference_inventory.yaml` is present but explicitly states `verified_offline_candidate_not_registry_replacement`. The stale summary in `models/README.md` says 113 (39/37/37). Fix that text only; never promote models, change YAML/archive hashes, or imply TwinCAT qualification.

### HYG-04: Advance only the two canonical PINNs submodule gitlinks

Current, linear, source-confirmed gitlink baselines:

- PINNs `reference/codes/TestRig`: `8e99c6ad9e5c4653c27be6cc29a9abe5f781f9c6` -> `XiLab-Robotics/TestRig/4026@6f7c4cec85f9a28563a9d4d7d8a27c43ce20eb2d` (175 commits ahead, zero behind).
- PINNs `reference/codes/TwinCAT_TF3820_StandaloneModelTest`: `a50aed6626333e44abf8968e64742b4c47aa1bd2` -> `XiLab-Robotics/TwinCAT-TF3820-StandaloneModelTest/main@9c07180b430cf6d156d441b31a091392c505477c` (263 commits ahead, zero behind).
- Preserve `.gitmodules` URLs/branches: they already name the correct `4026` and `main` upstreams.
- Preserve the other four imported reference/code-style submodule pins without unrequested upstream tracking changes.
- **Do not modify** TestRig `4026` or its nested standalone reusable gitlink `b95fb45d04c58a814ec4be0879a0e08f637a275f`; standalone reusable branch HEAD `09bc3606c8248cd7cdf4bf163fdd402e913edd4f` is not interchangeable with a tested Build or active runtime.
- Advancing the *parent* gitlinks is an up-to-date source-navigation change, **not** build/PLC/scientific acceptance.

## Involved Components

- `site/requirements-docs.txt`: ONNX docs dependency.
- `README.md`: current public-facing names, paths and status statements.
- `models/README.md`: authoritative 114-entry curated model inventory summary.
- `doc/README.md`: retained comprehensive index with one new technical-plan link.
- `reference/codes/TestRig` and `reference/codes/TwinCAT_TF3820_StandaloneModelTest`: two gitlinks only; no internal file changes.
- `.github/workflows/ci.yml` and `.github/workflows/publish-sphinx-pages.yml`: inspection and CI verification only.
- `AGENTS.md`, coordination Project Memory/Backlog/SRC-K-C: governance and status updates.

## Implementation Steps

1. Freeze and re-read exact main, TestRig/4026 and Standalone/main SHAs. Confirm the parent source tree and reusable nested pin.
2. Create this technical note first on the constrained maintenance branch; register it from `doc/README.md`.
3. Apply one ONNX documentation dependency; avoid ML and training changes.
4. Apply minimal root README and `models/README.md` corrections justified by source inventory.
5. Update exactly two PINNs gitlinks via Git-tree entries of mode `160000`; retain the other four entries and unchanged `.gitmodules`.
6. Check no files were removed or moved. Check for unwanted large added files (GitHub commit gate: no new blobs over 100 MB, no large aggregate staged payload).
7. Check touched Markdown for spacing, headings, a single final newline, and Markdownlint; check exact links and inventory provenance. Execute repository-owned QA and Sphinx where a full working tree and runtime dependencies are available, otherwise explicitly record the test limitation.
8. Open a reviewable PR for protected `main`, inspect actual Actions checks and review/merge requirements. Only a subsequent successful main-branch Pages deploy verifies HYG-01 publication.
9. Keep `PREPARED`, `APPLIED`, `SOURCE_VERIFIED`, `CI_VERIFIED`, `PAGES_VERIFIED` separate. Update coordinator evidence after changes are source-confirmed; never silently claim Build, training, live PLC or paper acceptance.

## Verification And Rollback

- Expected tracked diff: this new document, root/doc/model README, docs requirements, two exact gitlink SHA changes. Zero deletions, zero modified binary/model/source/training/config/TwinCAT files.
- The parent working tree does not contain the expanded contents of the two external repositories; gitlink changes only record commit IDs.
- Require branch head/source-tree re-read and parent diff after each GitHub write.
- Revert this branch through a normal reviewable Git commit/PR if any expected safety or compatibility check fails. Do not rewrite scientific history or force-push main.
- Until tests are observed, label the remediation `APPLIED_SOURCE_ONLY`; only evidence-backed workflow results may advance the CI or Pages statuses.

## HYG-01 CI runtime correction: source-backed finding

Historical [quality run 32862898056](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/actions/runs/32862898056) took more than five hours. Its Markdownlint step included 244 invocations for 25-file chunks. The repository-wide `.markdownlint-cli2.jsonc` file includes `globs`; markdownlint-cli2 appends these to every command-line invocation unless `--no-globs` is passed. Each chunk therefore rescanned the complete globbed documentation set repeatedly. The existing repository-owned `run_markdownlint.py` already uses `--no-globs` when explicit paths are supplied, confirming this is the intended behavior.

Correct the CI script so the explicit chunk list includes `config`, `models`, `doc` and `site` authored Markdown and each invocation passes `--no-globs`. This retains the configured canonical coverage and the existing 25-file memory-safe batching without repeated full-tree scans.

Previous full-hosted checkouts also materialized tens of thousands of files and the complete multi-gigabyte scientific archive even though this quality workflow checks only Markdown, Python syntax and the Sphinx portal. Use `actions/checkout@v5` **non-cone sparse-checkout** on both quality and Pages workflows, selecting root Markdown/lint configuration, all `site/` and `scripts/`, the lightweight `config/` tree, model Markdown and all `doc/**/*.md` plus site-embeddable PNG/SVG and small YAML/JSON assets. GitHub source trees and pinned submodules remain complete and unmodified; only the disposable runner working tree is sparse.

A local throwaway Git sparse-checkout fixture confirms that the anchored patterns include root `doc/README.md`, nested technical notes, root/nested model Markdown, portal, scripts, config and referenced PNG, while excluding output archives and PDF. This is a source/build optimization, not a deletion or archival operation. Continue to require a new observed `Repository Quality Checks` result and separate Pages deployment evidence. If Sphinx shows missing referenced assets, extend only the necessary sparse patterns; do not weaken `-W` or disable validation.

## HYG-01 CI iteration: run 44952932352

The optimized [PR quality run 44952932352](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/actions/runs/44952932352) completed in approximately five and a half minutes. Checkout, dependency install, structural Markdown QA, all Markdownlint chunks, and Python syntax compilation **PASS**. The strict Sphinx build found five remaining warnings:

- Three autodoc import failures due to missing `psutil`, imported from the existing `validate_wave52r_offline_leader_promotion.py` implementation.
- One autodoc import failure for `data.generate_polished_dataset`, whose lightweight Python source file was omitted by the sparse-checkout patterns.
- One MyST missing-target warning for the existing `reference/documentation_visual_references/ur_rtde_api_reference_example.pdf` link in `site/archives/ur_rtde_visual_reference.md`. The original PDF is present in the parent repository (17,645,730 bytes), not in the sparse runner.

The bounded correction is `psutil>=6.0,<9.0` in docs requirements and two additional sparse checkout patterns in both workflows: `/data/**/*.py` and the exact reference PDF path. Data files and model artifacts remain excluded from the ephemeral runner. Do not edit the source modules, rewrite the links, disable warnings or broaden to the complete `data/` and `reference/` trees. Await another observed full quality check outcome for this new commit.
## Required-Status Context Alignment

The [2026-11-21 quality run 44953488005](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/actions/runs/44953488005) completed `success`, including 269 Markdownlint chunks and strict Sphinx `build succeeded.` with zero warnings. Its GitHub Actions check-run was named `quality`. A separate source read of the active `Standard Protection` branch ruleset `14780874` confirms the configured required check context is `Repository Quality Checks`. To prevent a successful job from leaving the required context unmet, explicitly set the existing `quality` job display name to that exact string without changing its job identifier, triggers, validation commands or workflow title.

The post-change Actions check-run name and conclusion must both be independently verified on the new PR head before CI is declared fully ruleset-aligned. Main still also requires an independent human review and a separate Pages publish receipt.
