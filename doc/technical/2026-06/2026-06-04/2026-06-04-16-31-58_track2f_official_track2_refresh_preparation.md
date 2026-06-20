# Wave 3.1 Official TE Curve Verification Pipeline Refresh Preparation

## Overview

This technical document plans the operator-launched `TE Curve Verification Pipeline` verification
refresh for the completed `Wave 3.1` offset-aware probe campaign.

The completed campaign is already closed out. `doc/running/active_training_campaign.yaml`
records `status: none` and exposes three completed branch candidates in
`last_completed_campaign.branch_best_list`:

| Surface | Candidate Family | Run |
| --- | --- | --- |
| `global` | `sequential_residual_offset_probe` | `te_sequential_residual_offset_probe_remote_global` |
| `Fw` | `sequential_residual_offset_probe_fw` | `te_sequential_residual_offset_probe_remote_fw` |
| `Bw` | `sequential_residual_offset_probe_bw` | `te_sequential_residual_offset_probe_remote_bw` |

The refresh must preserve these as three parallel candidates. It must not
collapse the refresh to the scalar-first `Fw` campaign entry.

## Technical Approach

The implementation will prepare a repository-owned `Wave 3.1` verification
launcher and its documentation. The launcher will add or activate the three
registry-backed `Wave 3.1` candidates in the official `TE Curve Verification Pipeline` matrix path,
then run the matrix only when the user launches it.

Codex will not run the heavy matrix during preparation. The prepared launcher
will support local execution and `-Remote` execution using the repository's
remote campaign workflow where available.

After the user runs the launcher and reports completion, a separate inspection
step will accept or reject the produced artifacts, regenerate the official
visual reports and PDFs, and update the official decision report.

No subagent use is planned for this preparation.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `output/registries/families/sequential_residual_offset_probe/latest_family_best.yaml`
- `output/registries/families/sequential_residual_offset_probe_fw/latest_family_best.yaml`
- `output/registries/families/sequential_residual_offset_probe_bw/latest_family_best.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/campaigns/track_2/`
- `doc/scripts/campaigns/track_2/`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

## Implementation Steps

1. Inspect the current `TE Curve Verification Pipeline` matrix template and support code to confirm
   how registry-backed neural candidates are declared and loaded.
2. Add the three `Wave 3.1` branch candidates to the matrix configuration, or
   create a narrow Wave 3.1 overlay configuration if that is safer than
   editing the canonical template directly during preparation.
3. Patch inference support only if `sequential_residual_offset_probe` is not
   already loadable by the shared registry-backed `TE Curve Verification Pipeline` path.
4. Create a dedicated PowerShell launcher under `scripts/campaigns/track_2/`
   with local and `-Remote` modes.
5. Create the matching launcher note under `doc/scripts/campaigns/track_2/`
   with exact local and remote commands.
6. Ensure the launcher writes a distinct output suffix for the `Wave 3.1`
   refresh and does not start automatically during preparation.
7. Run focused validation checks on the launcher/configuration without running
   the heavy matrix.
8. Run Markdown QA on touched authored Markdown files and compile touched
   Python files.
9. Report the exact command for the user to run, then wait for completion
   before inspecting or accepting `TE Curve Verification Pipeline` artifacts.
