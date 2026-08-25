# Consolidate TestRig And TF3820 Submodules

## Overview

The parent Physics-Informed-Neural-Networks repository currently tracks two
separate submodules sourced from `XiLab-Robotics/TestRig`: the canonical
`reference/codes/TestRig` checkout and the historical
`reference/codes/TestRig_TF3820_MachineLearningServer` migration checkout.
The migration branch has been superseded by the reusable standalone TF3820
function-block integration on TestRig branch `4026`, and its remote branch has
been retired.

This change will consolidate the parent repository onto one canonical TestRig
submodule and one canonical standalone TF3820 development submodule:

```text
reference/codes/TestRig
  XiLab-Robotics/TestRig branch 4026

reference/codes/TwinCAT_TF3820_StandaloneModelTest
  XiLab-Robotics/TwinCAT-TF3820-StandaloneModelTest branch main
```

The verified remote targets at planning time are:

- TestRig `4026`: `8e99c6ad9e5c4653c27be6cc29a9abe5f781f9c6`;
- standalone `main`: `e878ee5d54f43c9d996834896197ac25203c7baa`;
- reusable predictor pinned inside TestRig: `93cbf44675a3ac3b0ab0eb5e247d0392ddb965c7`.

## Technical Approach

The parent repository will remove the obsolete
`TestRig_TF3820_MachineLearningServer` gitlink and its `.gitmodules` entry.
The historical technical documents that describe the original migration
prototype will remain unchanged because they are part of the project record.

The retained `TestRig` submodule configuration will explicitly record branch
`4026` and its gitlink will be advanced from `a7ce8fc` to the verified current
commit `8e99c6a`. This commit contains the reusable TF3820 predictor integration,
experiment hardening, live-compensation guards, and setpoint-domain angle
correction. The nested reusable-package gitlink inside TestRig will remain at
its repository-owned pinned commit `93cbf44`; this parent cleanup will not
silently change TestRig internals.

The retained `TwinCAT_TF3820_StandaloneModelTest` submodule will continue to
track branch `main`, and its parent gitlink will be advanced to verified remote
commit `e878ee5`. That baseline includes the standalone predictor/function-block
work, the feedforward latency and same-invocation-submit development, reusable
package synchronization tooling, and current catalog validation support.

After changing the tracked structure, Git submodule configuration will be
synchronized and the retained submodules will be checked against their exact
remote refs. Removal of the obsolete path is recoverable from parent Git
history and from commit `95d73f0`; no external repository history will be
rewritten.

## Involved Components

- `.gitmodules`
  Remove the retired TestRig migration entry and declare branch `4026` for the
  retained TestRig submodule.
- `reference/codes/TestRig`
  Advance the parent gitlink to `TestRig/4026@8e99c6a`.
- `reference/codes/TestRig_TF3820_MachineLearningServer`
  Remove the obsolete parent gitlink and working-tree path.
- `reference/codes/TwinCAT_TF3820_StandaloneModelTest`
  Advance the parent gitlink to standalone `main@e878ee5`.
- `doc/README.md`
  Register this technical change plan.
- Historical migration documents under `doc/technical/2026-07/`
  Preserve them as historical evidence; do not retarget their original paths.

## Implementation Steps

1. Obtain explicit approval for this technical plan.
2. Recheck the parent and all three current submodule worktrees for unrelated
   or untracked content before removing or advancing anything.
3. Confirm the remote SHAs for TestRig `4026` and standalone `main` have not
   moved since this plan was written; record any newer verified tip before use.
4. Remove `reference/codes/TestRig_TF3820_MachineLearningServer` as a parent
   submodule and remove only its corresponding `.gitmodules` section.
5. Add `branch = 4026` to the retained TestRig submodule configuration and pin
   its gitlink to the verified `origin/4026` tip.
6. Keep `branch = main` for the standalone submodule and pin its gitlink to the
   verified `origin/main` tip.
7. Synchronize submodule configuration and verify recursive status without
   changing the TestRig-owned nested reusable-package pin.
8. Search the active repository surface for stale operational references to
   the removed submodule; preserve clearly historical technical records.
9. Run Markdown style and Markdownlint checks on the touched documentation.
10. Inspect the complete parent diff, submodule SHAs, removed-path scope, and
    file-size risk.
11. Report the prepared change and wait for separate explicit approval before
    creating a Git commit or pushing it to GitHub.

## Approval Gate

Repository implementation must not begin until the user explicitly approves
this document. Commit and push remain a later, separate approval boundary.
