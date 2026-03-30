# Requirements Resolution Fix For Windows Clean Installs

## Overview

This technical note documents the next dependency-resolution fix required for
clean Windows installation of the repository environment.

After correcting the `colorama` lower bound, a new resolver conflict remained:

- `sphinx>=9.1,<10.0`
- `sphinx-rtd-theme>=3.1,<4.0`
- `myst-parser>=4.0,<5.0`

The clean-install resolver output shows that `myst-parser 4.x` requires
`sphinx<9`, while the repository now requires `sphinx>=9.1`.

The repository dependency set is therefore still internally inconsistent for a
fresh environment.

## Technical Approach

The planned fix is:

1. validate the current conflict in a temporary clean environment from the
   current workstation;
2. update the incompatible documentation dependency constraint so the full
   `requirements.txt` resolves again on Windows;
3. re-run the clean-install check in the temporary environment until the
   dependency set resolves successfully.

The likely minimal direction is to move `myst-parser` to a version range that
supports the tracked `Sphinx 9.x` line, rather than downgrading the repository
back to `Sphinx 8.x`, but that will be confirmed by the temporary-environment
test before finalizing the fix.

## Involved Components

- `requirements.txt`
  Canonical dependency list to repair.
- `README.md`
  Register this technical note as required by the repository workflow.

No subagent usage is planned for this scope.

## Implementation Steps

1. Register this technical note in `README.md`.
2. Create a temporary clean environment on the current workstation.
3. Reproduce the resolver failure against the current `requirements.txt`.
4. Adjust the conflicting dependency bound in `requirements.txt`.
5. Re-run the clean-install test in the temporary environment.
6. Keep the fix limited to the resolver conflict required to restore clean
   Windows installation.
