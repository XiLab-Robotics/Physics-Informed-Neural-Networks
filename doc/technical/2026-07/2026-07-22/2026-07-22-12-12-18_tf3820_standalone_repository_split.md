# TF3820 Standalone Repository Split

## Overview

The standalone TwinCAT `TF3820` model-test harness currently lives inside this
repository under `reference/codes/TwinCAT_TF3820_StandaloneModelTest/`.

The goal is to move that harness into a dedicated GitHub repository so it can
be cloned, tested, and versioned as an independent PLC validation project, then
bring it back into this repository as a Git submodule. This keeps the main
machine-learning repository focused on training, conversion, and documentation
while the PLC smoke-test project becomes a reusable TwinCAT artifact.

The external repository is:

```text
XiLab-Robotics/TwinCAT-TF3820-StandaloneModelTest
```

```text
https://github.com/XiLab-Robotics/TwinCAT-TF3820-StandaloneModelTest
```

## Technical Approach

The split should preserve the existing generated harness exactly before any
follow-up TwinCAT refactor. The new repository should contain the standalone
project root contents, not the parent `reference/codes/` folder:

```text
TwinCAT_TF3820_StandaloneModelTest.sln
TwinCAT_TF3820_StandaloneModelTest.tsproj
PLC_project/
ML_models/
model_catalog.json
README.md
```

The GitHub CLI is installed on this workstation and is used to create and push
the standalone repository over HTTPS.

After the external repository exists, the local implementation should:

1. initialize a temporary local Git repository from the current standalone
   harness contents;
2. commit those contents as the standalone repository initial state;
3. push that commit to the new GitHub remote;
4. replace the tracked in-tree harness directory in the main repository with a
   submodule at the same path;
5. configure the submodule URL and, if useful, branch tracking;
6. verify that a fresh submodule checkout restores the standalone project and
   its `ML_models` artifacts.

## Involved Components

- `reference/codes/TwinCAT_TF3820_StandaloneModelTest/`
  Current tracked standalone TwinCAT project to externalize.
- `.gitmodules`
  Main-repository submodule registry that will receive the new standalone
  project entry.
- `doc/README.md`
  Documentation index updated to register this technical plan.
- `doc/scripts/deployment/twincat_onnx_conversion/README.md`
  Existing usage note that may need a small path/source clarification after the
  submodule replacement.
- `doc/guide/project_usage_guide.md`
  User-facing guide that may need a small note explaining that the standalone
  project is a submodule.

## Implementation Steps

1. Create this technical document and register it in `doc/README.md`.
2. Wait for explicit user approval before changing Git structure or creating
   the external repository.
3. Confirm the target GitHub organization/name and whether the repository
   should be public or private.
4. Create or use the external GitHub repository.
5. Move the current standalone project contents into the new repository and
   push the initial commit.
6. Replace the main-repository tracked directory with a submodule at
   `reference/codes/TwinCAT_TF3820_StandaloneModelTest`.
7. Update affected usage documentation to state that the standalone project is
   now retrieved through a submodule.
8. Validate with `git submodule status`, a clean submodule checkout, file-size
   checks, Markdown QA, and a final main-repository status review.
