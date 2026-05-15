# Repository-Wide Linux Script Portability Plan

## Overview

This document plans the full repository-wide Linux portability pass requested
after the first Unimore Aries Track 1 slice. The target is stronger than the
previous Track 1 exact-paper commit: every repository-owned runnable script
under `scripts/` must either be runnable on Linux directly, expose a documented
Linux equivalent, or be explicitly classified as intentionally Windows-only
with a clear replacement workflow.

The current audit baseline is:

- total scripts under `scripts/`: `208`;
- Python scripts: `109`;
- PowerShell scripts: `98`;
- Bash scripts: `1`;
- Python scripts with CLI/argparse-like surfaces: `44`;
- Python scripts currently exposing `--linux` / `--windows`: `3`;
- report/PDF Python scripts: `28`;
- report/PDF Python scripts currently exposing `--linux` / `--windows`: `0`.

Therefore, the repository is not yet Linux-portable as a whole. The previous
commit should be treated as a reusable first slice, not as completion of this
broader requirement.

No subagent is planned for the first repository-wide implementation pass. If
the work is split later across independent script domains, subagent use must be
declared separately, recorded in an updated technical note, and explicitly
approved before launch.

## Technical Approach

The implementation should proceed through a tracked inventory rather than
ad hoc script edits. The portability standard is:

- all repository paths accepted by Python entry points are repository-relative
  by default;
- `--windows` and `--linux` are available on all Python entry points that parse
  command-line arguments and need path, browser, shell, or platform-specific
  behavior;
- `--windows` remains the default for compatibility unless an existing Linux
  shell wrapper passes `--linux`;
- all newly emitted YAML, Markdown, JSON, and manifest path fields are
  repository-relative and can be formatted for the requested platform;
- every `.ps1` launcher that represents a runnable repository workflow has a
  `.sh` equivalent, unless the workflow is documented as Windows-only and has
  a Linux-safe replacement;
- report, PDF, and presentation pipelines resolve browser, validation, and
  shell tools through platform-aware logic rather than Windows hard-coded
  paths;
- verification is static or dry-run unless the user explicitly approves
  training, campaign execution, PDF generation, or presentation export.

The first implementation should promote the existing
`scripts/tooling/repository_path_support.py` helper into the common entry point
for repository path formatting and platform flag registration. It should be
extended only where needed, not duplicated in each script.

## Involved Components

- Shared path and CLI platform support:
  - `scripts/tooling/repository_path_support.py`
  - `scripts/datasets/transmission_error_dataset.py`
  - `scripts/training/shared_training_infrastructure.py`

- Python training and campaign runners:
  - `scripts/training/*.py`
  - `scripts/campaigns/**/*.py`
  - `scripts/paper_reimplementation/**/*.py`

- PowerShell launcher inventory and Linux equivalents:
  - `scripts/campaigns/**/*.ps1`
  - `scripts/tooling/**/*.ps1`
  - new `.sh` launchers beside the workflow-equivalent `.ps1` files

- Report, PDF, and presentation pipelines:
  - `scripts/reports/analysis/*.py`
  - `scripts/reports/closeout/**/*.py`
  - `scripts/reports/pdf/generate_styled_report_pdf.py`
  - `scripts/reports/pdf/run_report_pipeline.py`
  - `scripts/reports/pdf/validate_report_pdf.py`
  - `scripts/reports/presentation/generate_markdown_presentation.py`
  - `scripts/reports/presentation/run_presentation_pipeline.py`

- Documentation and indices:
  - `doc/scripts/`
  - `doc/scripts/campaigns/`
  - `doc/scripts/tooling/`
  - `doc/guide/project_usage_guide.md`
  - `site/`

- Protected campaign surfaces:
  - `doc/running/active_training_campaign.yaml`
  - any file listed in its `protected_file_list`

## Implementation Steps

1. Build a committed script portability inventory.
   Generate a repository-owned report or YAML inventory listing every script
   under `scripts/`, grouped by:
   - Python CLI entry point;
   - Python library/helper module;
   - PowerShell runnable launcher;
   - PowerShell helper;
   - Bash launcher;
   - report/PDF/presentation workflow;
   - intentionally Windows-only workflow.

2. Add a no-training dry-run surface where missing.
   Before broad launcher porting, ensure campaign and training launchers can
   validate queue selection, path resolution, and command construction without
   starting training.

3. Wire Python CLI entry points to platform flags.
   For each argparse-like Python script, add:
   - `repository_path_support.add_platform_arguments(...)`;
   - `repository_path_support.set_runtime_platform(...)`;
   - platform-aware output path formatting where the script emits paths.

4. Normalize repository-relative input paths globally.
   Replace direct `Path(path_value)` handling for repository paths with shared
   helper calls where Windows-style stored paths such as `config\...` could
   break on Linux.

5. Port campaign PowerShell launchers to Bash equivalents.
   For each runnable `.ps1` launcher, add an adjacent `.sh` equivalent or
   document why no Linux launch path is meaningful. Bash equivalents should:
   - run from the repository root;
   - pass `--linux` to Python entry points;
   - use `conda run --no-capture-output` when a Conda environment is needed;
   - mirror logs into the same repository-relative artifact roots;
   - expose a `--dry-run` mode where the launcher can otherwise start training.

6. Port report and PDF workflows explicitly.
   Replace Windows-only browser discovery in styled PDF export with
   platform-aware browser resolution. Linux candidates should include common
   Chrome/Chromium paths and an explicit override. Presentation export must
   not call `powershell` on Linux; it should either use a Linux-compatible
   LibreOffice command path or be classified as unsupported with a documented
   alternative.

7. Audit generated documentation commands.
   Update `doc/scripts/`, `doc/scripts/campaigns/`,
   `doc/scripts/tooling/`, and `doc/guide/project_usage_guide.md` so every
   documented Windows command has a Linux command when the workflow is meant to
   run on Aries.

8. Keep protected campaign edits gated.
   Before modifying files listed by `doc/running/active_training_campaign.yaml`,
   issue a `CRITICAL WARNING` and require explicit approval unless the user has
   already approved the exact protected-file scope for that implementation
   pass.

9. Verify in layers without launching training.
   Required checks for the implementation pass:
   - `py_compile` on touched Python files;
   - `bash -n` on new or touched Bash scripts;
   - PowerShell parser checks on touched `.ps1` files;
   - `--help` checks for touched CLI Python scripts;
   - `--dry-run` checks for touched campaign launchers;
   - Markdown style check and Markdownlint on touched Markdown;
   - Sphinx build when `doc/guide/` or portal-scoped docs change.

10. Verify on real Linux before declaring completion.
    The final claim that all scripts are Linux-runnable must be based on the
    Aries clone or an equivalent Linux environment, not only Windows or WSL
    static checks. At minimum, run the generated inventory checks, selected
    `--help` commands, Bash syntax checks, and non-training dry runs on Linux.

11. Stop before commit.
    Report the inventory results, changed files, verification matrix, and any
    intentionally unsupported scripts. Commit only after explicit user approval.

The completion criterion is strict: the final answer must not say "all scripts
are Linux-runnable" unless every runnable script has either passed Linux
verification or has a documented Linux replacement and is marked as such in the
inventory.
