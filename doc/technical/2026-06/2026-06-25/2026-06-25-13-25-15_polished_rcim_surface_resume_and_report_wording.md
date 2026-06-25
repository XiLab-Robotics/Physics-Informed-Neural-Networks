# Polished RCIM Surface Resume And Report Wording

## Overview

The polished `RCIM Model-Bank Reproduction` campaign was interrupted after the
forward surface completed and after the backward run directory was created.
The campaign launcher needs a safe way to run only one surface, so the operator
can resume `bw` without rerunning `fw`.

The validation report generator also still uses wording inherited from the
legacy original-dataset workflow. That wording is misleading for
`polished_dataset` runs even when the actual dataset root recorded in the
summary is correct.

## Technical Approach

Add an explicit surface selector to the polished RCIM campaign launcher with
accepted values `all`, `fw`, and `bw`. Keep `all` as the default to preserve
existing behavior.

Add persistent local log capture per selected surface so future interruptions
leave inspectable campaign logs under the campaign output directory.

Make the report title, overview wording, and report filename suffix derive from
the resolved dataset root where possible. Preserve the legacy wording for
non-polished runs so historical original-dataset semantics remain explicit.

## Involved Components

- `scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.ps1`
- `doc/scripts/campaigns/cross_wave/run_polished_dataset_rcim_model_bank_reproduction_campaign.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `doc/README.md`

## Implementation Steps

1. Add the technical plan and register it in `doc/README.md`.
2. Add a `-Surface` parameter to the polished RCIM launcher.
3. Filter the local and remote RCIM config/run-name lists from the selected
   surface.
4. Capture local launcher output into surface-specific log files while
   preserving console output.
5. Derive report wording and suffix from `dataset_root` for polished runs.
6. Update launcher documentation with all, forward-only, and backward-only
   commands.
7. Run preflight and Markdown checks before committing the maintenance change.
