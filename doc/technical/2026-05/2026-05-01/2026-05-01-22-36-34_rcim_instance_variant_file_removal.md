# Overview

Plan the final recovered-workflow instance-helper cleanup so
`instance_v4.py` and `instance_v5.py` are physically removed from the
repository-owned active workflow subtree, leaving `instance.py` as the only
runtime instance-helper file under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/`.

## Technical Approach

The previous cleanup established that:

- the active runtime already flows through `statistics.py`;
- `statistics.py` now imports `Instance` from `instance.py`;
- `instance_v4.py` is not used by the current repository-owned runtime;
- `instance_v5.py` is now only a compatibility shim.

This follow-up should finish the cleanup by removing both variant-named files.
The repository should keep the historical trace in documentation, not in the
active utility folder.

The implementation should:

1. delete `instance_v4.py`;
2. delete the temporary compatibility shim `instance_v5.py`;
3. keep `instance.py` as the sole runtime helper;
4. update the recovered-workflow README so it explicitly states that the old
   variant-named files were removed from the repository-owned workflow copy;
5. keep a placeholder in the README so the final cleanup commit hash can be
   written there afterward.

The numerical behavior of the active runtime must remain unchanged.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/technical/2026-05/2026-05-01/README.md`
- `doc/README.md`

## Implementation Steps

1. Delete `instance_v4.py` from the repository-owned workflow subtree.
2. Delete the `instance_v5.py` compatibility shim.
3. Verify that `statistics.py` and the active entrypoints still resolve
   `instance.py` correctly.
4. Update the recovered-workflow README to reflect the final single-file
   runtime surface and to keep the migration-commit placeholder.
5. Run `py_compile` on the touched utility files and a smoke dataframe-creation
   run that exercises `statistics.py -> instance.py`.
