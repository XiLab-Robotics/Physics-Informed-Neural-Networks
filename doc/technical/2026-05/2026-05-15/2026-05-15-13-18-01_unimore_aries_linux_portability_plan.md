# Unimore Aries Linux Portability Plan

## Overview

This document plans the repository changes needed to run the current
campaign-oriented Python workflows on the Unimore Aries Red Hat Linux VM while
preserving the existing Windows behavior as the default operator path.

The immediate operational target is the RCIM Model-Bank Reproduction exact-paper launcher pair:

- `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- a new Linux-equivalent Bash launcher under the same campaign folder

The broader target is to make repository-owned Python entry points consume
repository-relative paths consistently and expose explicit platform selection
through `--windows` and `--linux`, with `--windows` remaining the default when
no flag is provided.

No subagent is planned for the first implementation pass. If the scope expands
to a full repository-wide launcher migration, subagent use must be proposed
separately and approved before launch.

## Technical Approach

The change should be implemented as a compatibility layer instead of scattered
per-script string replacements.

1. Add a small repository-owned platform/path utility for Python scripts.
   It should:
   - resolve the repository root from the script location or current working
     directory;
   - normalize input paths as repository-relative paths first;
   - accept absolute paths only when the path is an intentional external
     resource;
   - provide argparse helpers for `--windows` and `--linux`, with `windows` as
     the default platform;
   - serialize repository paths with POSIX separators for config and YAML
     artifacts unless a Windows-only external command requires backslashes.

2. Update the RCIM Model-Bank Reproduction exact-paper Python entry points first.
   The priority files are:
   - `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
   - `scripts/training/shared_training_infrastructure.py`
   - `scripts/campaigns/track_1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py`

3. Replace Windows-only launcher assumptions with Bash equivalents.
   The Linux launcher should be a sibling of the PowerShell launcher and keep
   the same operator semantics:
   - campaign slicing by direction and families;
   - stage selection;
   - local execution by default;
   - optional explicit environment name and Python executable;
   - terminal-visible progress markers;
   - log mirroring under the same repository-relative output root.

4. Keep PowerShell launchers intact.
   Existing `.ps1` files remain the Windows operator surface. The Linux work
   adds `.sh` equivalents and shared Python path handling rather than rewriting
   the Windows launch path.

5. Make path conversion explicit in YAML-producing scripts.
   Existing preparers still emit many protected campaign paths with `\`
   separators. The approved implementation should switch newly generated
   campaign state and queue metadata to repository-relative POSIX-style paths
   where the downstream Python path handling accepts both separators.

6. Document both launch surfaces.
   The existing launcher note should gain Linux examples, and the new Bash
   launcher should be listed beside the PowerShell launcher.

## Involved Components

- Protected campaign state:
  - `doc/running/active_training_campaign.yaml`

- Protected RCIM Model-Bank Reproduction launcher files:
  - `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
  - `scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.ps1`
  - `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.ps1`
  - `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.ps1`

- New Linux launcher targets:
  - `scripts/campaigns/track_1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh`
  - `scripts/campaigns/track_1/exact_paper/invoke_exact_paper_campaign_local.sh`
  - optional shared Bash helper under `scripts/campaigns/infrastructure/`

- Python path handling targets:
  - `scripts/training/shared_training_infrastructure.py`
  - RCIM Model-Bank Reproduction exact-paper campaign preparers under
    `scripts/campaigns/track_1/exact_paper/`
  - exact-paper validation runners under
    `scripts/paper_reimplementation/rcim_ml_compensation/`

- Documentation targets:
  - `doc/scripts/campaigns/run_track1_bidirectional_paper_faithful_grid_search_campaign.md`
  - `doc/README.md`
  - this technical document

## Implementation Steps

1. Run a focused Windows-specific audit.
   Use `rg` over `scripts/`, `config/`, and campaign documentation for:
   - `.ps1`, `PowerShell`, `cmd.exe`, `where.exe`, `conda.exe`;
   - hard-coded drive paths such as `C:\`;
   - explicit backslash-only path parsing;
   - `Resolve-Path`, `Join-Path`, and remote Windows bootstrap assumptions.

2. Add the Python platform/path helper.
   The helper should expose:
   - `add_platform_arguments(argument_parser)`;
   - `resolve_execution_platform(arguments)`;
   - `resolve_repository_path(path_value, allow_absolute=False)`;
   - `format_repository_path(path_value, platform_name)`.

3. Wire `--windows` and `--linux` into the exact-paper validation runner.
   The runner should pass the resolved platform into shared path formatting and
   artifact serialization without changing model behavior.

4. Update the RCIM Model-Bank Reproduction exact-paper campaign preparer.
   Newly generated campaign YAML, active campaign state, protected-file lists,
   and launcher commands should use repository-relative paths that work on
   Linux and Windows.

5. Add the Bash local launcher for the bidirectional paper-faithful campaign.
   It should mirror the PowerShell launcher arguments with idiomatic Bash
   flags:
   - `--direction Forward|Backward|Both`;
   - `--family All|...`;
   - `--families "SVR,MLP,..."`;
   - `--stage Search|Eval|Export|LoadBest`;
   - `--linux` passed through to Python by default from the Bash launcher;
   - `--windows` accepted only as an explicit compatibility override.

6. Add a Bash local invocation helper if duplication would otherwise grow.
   Keep the helper small and explicit, with no hidden argument rewriting.

7. Update launcher documentation.
   Add Linux examples using `bash` and keep the existing PowerShell examples.

8. Verify without starting a training campaign.
   Run syntax and dry-run checks only:
   - Python compile checks for touched Python files;
   - Bash syntax checks with `bash -n` if available;
   - PowerShell parse checks for touched `.ps1` files if changed;
   - a no-training queue-selection smoke or dry-run mode if implemented;
   - Markdown QA on touched Markdown files.

9. Stop before commit.
   Report the exact changed files and wait for explicit commit approval.

Protected-file approval is required before editing the current RCIM Model-Bank Reproduction launcher
files listed in `doc/running/active_training_campaign.yaml`, even though the
campaign state currently says `completed`.
