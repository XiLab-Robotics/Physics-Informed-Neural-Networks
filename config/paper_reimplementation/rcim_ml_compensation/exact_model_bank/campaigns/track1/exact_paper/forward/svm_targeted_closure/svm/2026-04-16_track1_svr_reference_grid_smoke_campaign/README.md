# Track 1 SVR Reference Grid Smoke Campaign Package

This package contains a minimal exact-paper `SVR` smoke campaign used to
validate the corrected local and remote exact-paper launchers before retrying
the heavier `Track 1` reference-grid repair campaign.

Package rules:

- only `SVR` is enabled;
- only amplitude harmonic `40` is included;
- `paper_reference_grid_search` remains enabled to exercise the real
  paper-faithful search path;
- `grid_search_n_jobs` is forced to `1` so the run stays small enough to
  validate orchestration without long silent phases.
