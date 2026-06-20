# Obsolete Training Artifact Cleanup

## Overview

This document plans a conservative cleanup of obsolete repository-tracked model
artifacts, validation outputs, campaign outputs, smoke-test outputs, and
duplicated reference logs. The immediate goal is to reduce repository size and
Git LFS pressure while preserving the current best model surfaces, accepted
reference archives, campaign closeout evidence, and enough provenance to
reproduce the current project state.

The current repository state is clean before the planning document. The active
training campaign state is `status: none`, with an empty
`protected_file_list`, so no active protected campaign files are present.

The cleanup must not run until this technical document is explicitly approved.

## Technical Approach

The cleanup should use a retention-first policy:

- Preserve `output/registries/` and the current family and program best
  metadata.
- Preserve `models/exported/` because it is the canonical Wave 1 deployment and
  comparison surface.
- Preserve `models/paper_reference/` model payloads and inventories unless a
  separate approval allows removing duplicated source logs from reference
  archives.
- Preserve the best `2` or `3` training runs per model family and direction
  scope based on the existing family leaderboard order.
- Preserve campaign-level summary artifacts such as `campaign_leaderboard.yaml`,
  `campaign_best_run.yaml`, and `campaign_best_run.md` where they define closed
  campaign results.
- Remove obsolete full run directories, validation directories, ONNX export
  batches, large `.pkl` bundles, smoke-test payloads, and duplicated logs that
  are superseded by newer accepted runs or canonical model archives.
- Keep authored reports and technical documentation, but allow their artifact
  pointers to become historical references when the corresponding bulky output
  has been intentionally pruned.

Inventory from the current working tree:

| Area | Approximate size | File count | Cleanup interpretation |
| --- | ---: | ---: | --- |
| `output/validation_checks` | `11437.19 MB` | `30513` | Primary cleanup target. Mostly superseded validation bundles, `.pkl` banks, and ONNX exports. |
| `output/training_campaigns` | `2904.37 MB` | `6884` | Keep campaign result summaries; prune obsolete run/log payloads after registry and report cross-checks. |
| `output/training_runs` | `337.50 MB` | `3672` | Apply top `2` or `3` retention per family/scope from registries. |
| `output/transmission_error_png` | `210.27 MB` | `969` | Candidate for pruning generated previews if canonical reports retain selected figures elsewhere. |
| `output/smoke_tests` | `50.52 MB` | `18` | Candidate for removal; one obsolete tree smoke-test `.pkl` is about `49.47 MB`. |
| `models/` | `1921.15 MB` | `3303` | Treat as canonical archive; only duplicated source logs should be considered in this pass. |

The largest tracked output classes are:

| Extension | Count | Approximate tracked size |
| --- | ---: | ---: |
| `.pkl` | `3329` | `7116.73 MB` |
| `.onnx` | `15614` | `5800.86 MB` |
| `.log` | `3480` | `1082.94 MB` |
| `.ckpt` | `521` | `282.06 MB` |
| `.png` | `1068` | `224.93 MB` |

Git LFS currently tracks only two run-related `.pkl` files:

- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-00-03__track1_original_dataset_forward_rf_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-56-26__track1_original_dataset_backward_ert_attempt_08_campaign_validation/paper_family_model_bank.pkl`

Those two files are direct high-priority removal candidates if their accepted
content has already been promoted into `models/paper_reference/` or superseded
by the final `RCIM Model-Bank Reproduction` and `TE Curve Verification Pipeline` references.

## Involved Components

- `output/validation_checks/`
- `output/training_campaigns/`
- `output/training_runs/`
- `output/smoke_tests/`
- `output/transmission_error_png/`
- `output/registries/`
- `models/exported/`
- `models/paper_reference/`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_results/`
- `doc/reports/analysis/Training Results Master Summary.md`
- `.gitattributes`

## Implementation Steps

1. Re-check `git status --short` and
   `doc/running/active_training_campaign.yaml` immediately before cleanup.
2. Build a retention manifest from `output/registries/families/*/leaderboard.yaml`
   and `output/registries/program/current_best_solution.yaml`, keeping the top
   `2` or `3` entries per family and direction scope.
3. Add campaign winners and accepted reference artifacts to the keep manifest:
   campaign best files, family-best source runs referenced by `models/exported/`,
   and accepted `models/paper_reference/` archives.
4. Generate a deletion manifest for obsolete artifacts under `output/`, grouped
   by validation checks, training runs, campaign payloads, smoke tests, and
   generated previews.
5. Review the deletion manifest before applying it, with special attention to
   paths currently named in registries, closeout reports, and the active
   campaign state.
6. Remove approved obsolete files and directories using path-literal PowerShell
   operations or Git-aware deletion, preserving all paths in the keep manifest.
7. Update `.gitattributes` only if both run-related LFS `.pkl` pointers are
   removed and the explicit path entries become obsolete.
8. Run `git lfs ls-files --long`, `git status --short`, and size summaries to
   confirm that only intended artifacts were removed.
9. Run Markdown QA on touched Markdown files:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
10. Stop after reporting the cleanup result and wait for explicit approval
    before any Git commit.

## Cleanup Results

Approved cleanup was applied on `2026-05-19T15:18:05+02:00`.

Summary:

- Removed obsolete validation-check roots, old smoke-test outputs, generated
  transmission-error preview outputs, and non-retained training-run directories.
- Kept the top `3` training-run entries per family leaderboard.
- Trimmed family leaderboards to the retained top `3` entries.
- Removed generated campaign payload files with extensions `.log`, `.pkl`,
  `.onnx`, `.csv`, `.txt`, and `.sqlite3`, while preserving campaign YAML, MD,
  and JSON bookkeeping.
- Removed the two explicit Git LFS `.pkl` rules from `.gitattributes` because
  those obsolete validation model banks were deleted.

Measured `output/` footprint changed from approximately `14.6 GB` before
cleanup to approximately `75 MB` after cleanup, excluding unchanged canonical
archives under `models/` and unchanged reference videos under `reference/`.
