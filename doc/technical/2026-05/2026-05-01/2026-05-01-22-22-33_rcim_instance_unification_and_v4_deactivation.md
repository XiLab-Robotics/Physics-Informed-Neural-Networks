# Overview

Plan a structural cleanup of the recovered original RCIM workflow so the active
runtime surface uses a single `instance.py` helper derived from the current
`instance_v5.py`, while `instance_v4.py` is removed from the active execution
path and retained only as a historical reference if still needed. The README
for the recovered workflow must explicitly record that this migration happened
and later capture the Git commit that introduced it, so the pre-cleanup state
remains recoverable.

## Technical Approach

The current repository-owned runtime already routes through
`utilities/statistics.py`, which imports `instance_v5.Instance`. The cleanup
therefore should not merge two equally active variants; instead it should
formalize the de facto runtime truth:

1. promote the currently active `instance_v5.py` surface to `instance.py`;
2. update `statistics.py` to import from `instance.py`;
3. decide how to retain `instance_v4.py` as a historical artifact without
   leaving it ambiguous as an active dependency;
4. update the recovered-workflow README so it documents:
   - that the active runtime moved from `instance_v5.py` to `instance.py`;
   - that `instance_v4.py` is historical and not used by the active scripts;
   - that the cleanup commit hash must be recorded there after the final commit.

The implementation should stay conservative:

- do not alter the numerical logic of the active `Instance` implementation;
- do not silently fuse `v4` and `v5` semantics into one polymorphic branch;
- keep the historical distinction visible in documentation.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v5.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance_v4.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/instance.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/technical/2026-05/2026-05-01/README.md`
- `doc/README.md`

## Implementation Steps

1. Create `utilities/instance.py` from the active `instance_v5.py` runtime
   surface.
2. Repoint `utilities/statistics.py` to import `Instance` from `instance.py`.
3. Keep `instance_v4.py` out of the active runtime path and clarify its
   historical role.
4. Decide whether to keep or retire `instance_v5.py` after the import switch,
   based on the cleanest repository-owned surface.
5. Update `recovered_original_workflow/README.md` with the migration note and a
   placeholder section that will later store the final commit hash.
6. Run `py_compile` and one smoke command that exercises `statistics.py` and the
   active instance helper.
