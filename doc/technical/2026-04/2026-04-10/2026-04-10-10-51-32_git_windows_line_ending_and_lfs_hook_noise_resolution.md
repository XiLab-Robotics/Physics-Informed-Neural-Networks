# Git Windows Line Ending And LFS Hook Noise Resolution

## Overview

This document covers the recurring Git-on-Windows operational noise observed
during repository work:

1. repeated `LF will be replaced by CRLF` working-copy warnings during normal
   `git diff`, `git add`, and commit preparation;
2. the recurring post-commit `sh.exe` failure printed after an otherwise
   successful Git commit.

The current inspection shows two distinct root causes:

- the repository currently relies on the machine-wide Git setting
  `core.autocrlf=true` without a repository-owned text normalization policy in
  `.gitattributes`;
- the local repository uses Git LFS shell hook wrappers in `.git/hooks/` for
  `post-checkout`, `post-commit`, `post-merge`, and `pre-push`, and the shell
  wrapper path is the most likely source of the repeated `sh.exe` noise on this
  Windows setup.

The fix should therefore be split into a repository-owned part plus a
repository-local Git-environment part.

No subagent is planned for this task. The work is local repository and local
Git-environment maintenance, and any future delegated Git-environment diagnosis
would still require explicit user approval at runtime.

## Technical Approach

### 1. Normalize Repository Text Files Explicitly

Add a repository-owned `.gitattributes` text policy so canonical source and
documentation file types are checked out with stable line endings instead of
depending on the global Windows `core.autocrlf=true` behavior.

The policy should cover at least the file types that repeatedly triggered the
warnings:

- `*.md`
- `*.py`
- `*.rst`
- `*.txt`
- `*.yml`
- `*.yaml`
- `requirements*.txt`

The existing Git LFS `-text` entries for tracked binary artifacts must be kept
intact.

### 2. Align The Local Repository Git Config

Set repository-local Git config so this clone no longer inherits the global
`core.autocrlf=true` behavior for the working tree.

The likely local settings are:

- `core.autocrlf=false`
- optionally `core.eol=lf`

These changes are repository-local and not Git-tracked, but they are necessary
if the current clone should stop emitting the warning immediately instead of
waiting for future clean re-checkouts.

### 3. Remove The Noisy Local LFS Shell Hooks

The local `.git/hooks/post-checkout`, `.git/hooks/post-commit`, and
`.git/hooks/post-merge` wrappers currently call `git lfs ...` through `sh`.
Those wrappers are the most likely source of the recurring Windows-side
`signal pipe` noise.

For this repository, the critical LFS path is the push/upload path, so the
noise-producing local post-operation wrappers can be removed if:

- `pre-push` is kept intact for LFS upload handling;
- the repository does not depend on LFS lock-management side effects in the
  post-operation hooks.

### 4. Ignore Local Temporary Validation Environments

Add `.tmpdocenv/` to `.gitignore` so local Sphinx-validation environments do
not keep reappearing as untracked noise after documentation tasks.

### 5. Validate The Result

Validate the fix by checking that:

- `git diff` and `git add` stop emitting the repeated LF/CRLF warnings for the
  covered file types in this clone;
- a fresh local test commit no longer emits the post-commit `sh.exe` error;
- the repository still retains the intended LFS push path.

## Involved Components

- `.gitattributes`
- `.gitignore`
- `.git/hooks/post-checkout`
- `.git/hooks/post-commit`
- `.git/hooks/post-merge`
- `.git/hooks/pre-push`
- `doc/README.md`
- `doc/technical/2026-04/2026-04-10/2026-04-10-10-51-32_git_windows_line_ending_and_lfs_hook_noise_resolution.md`
- repository-local Git config in `.git/config`

## Implementation Steps

1. Add a repository-owned line-ending policy to `.gitattributes` while keeping
   the existing Git LFS binary rules intact.
2. Add `.tmpdocenv/` to `.gitignore`.
3. Set repository-local Git config to stop inheriting the global Windows
   `core.autocrlf=true` behavior in this clone.
4. Remove the noisy local LFS post-operation shell hooks while preserving the
   `pre-push` LFS hook.
5. Verify that normal Git inspection/staging commands stop printing the
   repeated line-ending warning for the touched file types.
6. Create one local no-op verification commit if needed to confirm that the
   recurring `sh.exe` error is gone, then immediately report the result.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   task.
8. Report the completed fix and wait for explicit approval before creating any
   Git commit.
