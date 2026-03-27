---
name: git-commit-preflight
description: Use when preparing a repository commit in StandardML - Codex. This skill is for approval-gated commit preflight, changed-file checks, and commit-message drafting, not for auto-committing.
---

# Git Commit Preflight

Prepare repository commits safely and completely before asking the user for
commit approval.

## Use This Skill For

- final changed-file review before requesting commit approval;
- checking whether required documentation or usage updates were missed;
- checking GitHub file-size constraints for commit-bound files;
- drafting repository-style commit titles and commit bodies;
- spotting unrelated dirty-worktree changes that should not be swept into the
  commit accidentally.

## Do Not Use This Skill For

- creating a commit before explicit user approval;
- rewriting history unless the user explicitly requests it;
- reverting unrelated user changes;
- broad Git workflow redesign with no immediate repository task.

## Required Checks

1. Read `AGENTS.md` for the current commit-gating rules.
2. Inspect `git status` and separate task-owned changes from unrelated
   worktree changes.
3. Check whether the approved work changed:
   `README.md`, `doc/guide/project_usage_guide.md`, or `requirements.txt`.
4. If repository-owned Markdown files were touched, run the scoped Markdown
   warning checks and confirm normal final-newline state.
5. Before any GitHub-bound commit, verify that no commit-included file exceeds
   `100 MB`.

## Repository Commit Rules

- Commits are always approval-gated.
- Do not auto-commit just because the work appears complete.
- Keep the commit scope aligned with the approved task.
- Prefer commit messages that reflect repository intent clearly rather than
  generic "update files" wording.
- If the worktree contains unrelated edits, surface that clearly before the
  commit request.

## Commit Preparation Output

Prefer this structure when reporting commit readiness:

1. What changed.
2. What was verified.
3. Whether any blockers remain.
4. Proposed commit title.
5. Proposed commit body.

## Commands To Prefer

```powershell
git status --short
git diff --stat
git diff -- <path>
git ls-files -s
```

## File Targets To Read First

- `AGENTS.md`
- `README.md`
- `doc/guide/project_usage_guide.md`
- `requirements.txt`
- touched files in the current task
