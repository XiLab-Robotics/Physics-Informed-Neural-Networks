# Track 1 SVR Reference Grid Smoke Campaign Plan

## Purpose

Validate the corrected exact-paper launchers on a real repository-owned run
before reattempting the heavier `Track 1` `SVR` reference-grid repair campaign.

## Scope

- family: `SVR` only
- target scope: amplitude harmonic `40` only
- search mode: `paper_reference_grid_search`
- grid-search `n_jobs`: `1`

## Success Criteria

- the run starts and emits live exact-paper logs;
- the run completes without remote wrapper hangs;
- validation artifacts and Markdown report are produced;
- the launcher exits with the true child exit code.
