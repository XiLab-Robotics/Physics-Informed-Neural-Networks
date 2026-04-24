# Track 1 Intermediate PKL LFS Demotion And Ignore Policy

## Overview

This document defines the repository change needed to stop tracking
intermediate validation-model `.pkl` artifacts for the active `Track 1` branch
under Git LFS while the track is still open.

The requested scope is limited to the intermediate model bundles inside:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/`

The intended policy is:

- remove the intermediate `.pkl` artifacts in those roots from Git LFS
  tracking;
- ignore future `.pkl` artifacts in those two validation roots through
  `.gitignore` until `Track 1` is formally closed;
- record a backlog reminder that, at `Track 1` closure, only the final selected
  models should be reconsidered for Git LFS promotion.

No subagent is planned or required for this implementation.

## Technical Approach

The change should be implemented in three coordinated parts.

First, `.gitattributes` must stop assigning Git LFS filters to the relevant
intermediate `.pkl` artifacts in the two validation roots. This includes the
current exact-paper family-bank pattern and the current harmonic-wise
`harmonic_model_bundle.pkl` pattern.

Second, `.gitignore` must gain explicit ignore rules for intermediate `.pkl`
files in those same validation roots so new local artifacts remain untracked
until the branch reaches closure.

Third, the canonical operational backlog under
`doc/running/te_model_live_backlog.md` must receive a reminder item stating
that, once `Track 1` is completed, the repository should selectively re-add
only the final chosen model artifacts to Git LFS instead of restoring blanket
tracking for intermediate bundles.

Because some of these files are already tracked through LFS, implementation
will also need the corresponding Git index cleanup so the repository no longer
keeps those paths under version control after the ignore policy lands.

## Involved Components

- `.gitattributes`
- `.gitignore`
- `doc/running/te_model_live_backlog.md`
- `doc/technical/2026-04/2026-04-13/README.md`

## Implementation Steps

1. Remove the Track 1 intermediate validation `.pkl` LFS rules from
   `.gitattributes`.
2. Add matching ignore rules for those intermediate `.pkl` outputs to
   `.gitignore`.
3. Remove the already tracked intermediate `.pkl` files from the Git index
   without deleting the local working copies.
4. Add a closure reminder to `doc/running/te_model_live_backlog.md` stating
   that final selected Track 1 models should be re-evaluated for Git LFS only
   after the track is closed.
5. Run Markdown QA on the touched documentation scope.
6. Stop before any commit and wait for explicit approval, as usual.
