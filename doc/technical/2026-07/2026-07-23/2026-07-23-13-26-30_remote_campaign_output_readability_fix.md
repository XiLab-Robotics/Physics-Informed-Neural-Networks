# Remote Campaign Output Readability Fix

## Overview

The completed causal offset bounded `TE Curve Verification Pipeline` screen
finished successfully, but the local operator capture
`.temp/campaing_log.log` contains very long unwrapped lines. The screenshot in
`.temp/log.png` shows the same issue in the terminal.

The visible source is remote artifact synchronization output, especially
interactive `scp` progress records and PowerShell host records emitted as long
serialized strings. The same screen also finished with `report_plot_count: 0`,
so the operator-facing evidence package missed the expected bounded Track 2
measured-versus-predicted curve plots.

This fix should make future analogous campaign outputs readable and complete.

## Technical Approach

The implementation will inspect the current bounded Track 2 launcher and the
shared remote campaign infrastructure before changing code. The preferred fix
is to centralize the behavior in repository-owned campaign tooling rather than
patching only one launcher.

Planned changes:

- suppress or normalize interactive transfer progress from remote sync
  commands so terminal/log output is line-oriented and readable;
- preserve explicit high-level sync status messages, including source,
  destination, artifact count, and failure status;
- avoid committing or relying on large redundant remote artifact zip files when
  expanded canonical artifacts are already synchronized;
- trace why the bounded causal offset screen produced `report_plot_count: 0`
  and make bounded Track 2 screens generate the expected
  measured-versus-predicted plot package when plot generation is part of the
  report contract;
- update launcher notes and user-facing guide text if operator-visible commands
  or output behavior changes.

## Involved Components

- `scripts/campaigns/track_2/run_causal_offset_bounded_track2_screen.ps1`
- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`
- `scripts/campaigns/run_remote_training_campaign.ps1`
- `doc/scripts/campaigns/run_remote_training_campaign.md`
- `doc/scripts/campaigns/track_2/run_causal_offset_bounded_track2_screen.md`
- `doc/guide/project_usage_guide.md`
- `doc/running/active_training_campaign.yaml`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- bounded `TE Curve Verification Pipeline` report/plot output directories under
  `doc/reports/campaign_results/track_2/`

## Implementation Steps

1. Inspect the current local/remote launcher path and confirm no active
   protected campaign is open.
2. Identify each remote sync command that can emit progress bars or long
   serialized host records, starting from the causal offset bounded screen
   launcher.
3. Replace noisy transfer output with quiet transfer plus explicit
   repository-owned summary lines, or with a bounded line-normalizing wrapper
   if quiet mode is not sufficient.
4. Audit bounded Track 2 plot generation for this screen and determine whether
   missing plots came from launcher arguments, matrix configuration, sync
   selection, or plot-tool invocation.
5. Implement the smallest shared fix that applies to future analogous bounded
   screens.
6. Validate with PowerShell AST parsing, a local `-PreflightOnly` run, Markdown
   QA on touched docs, YAML parsing where applicable, and a controlled dry
   run/log sample that proves the output no longer emits long unwrapped
   transfer lines.

No subagent use is planned. If subagent review becomes useful, approval will be
requested before launching it.

## Implementation Record

Approved implementation applies the fix at two levels:

- shared remote campaign infrastructure now invokes `scp` in quiet mode for
  temporary script upload, source archive upload, source file upload, and
  artifact archive download;
- bounded Track 2 screen launchers now use quiet `scp`, summarize each synced
  source path, execute PowerShell remoting with text output, remove temporary
  artifact bundles after extraction, filter known remoting/progress noise from
  local step logs, and run the bounded candidate-curve plot builder explicitly.
- bounded Track 2 closeout PDFs are now treated as campaign-result reports by
  the styled-PDF layer, so `Execution Summary`, `Metric Ranking`, and
  `Pilot Graphs` page-break behavior remains consistent for future analogous
  closeouts.
- bounded Track 2 screen launchers now emit operator messages through plain
  console stdout instead of the PowerShell information stream, wrap long command
  and artifact path lines, suppress blank progress-renderer lines, and restrict
  post-run whitespace repair to screen-local report roots instead of broad
  historical validation-output trees.
- bounded Track 2 screen remote artifact sync now builds the remote bundle from
  the current screen's latest matrix output, latest matrix report, latest
  operator log, latest reranker output, screen-local reranker report, and
  screen-local plot root instead of copying full historical output roots.
- long remote artifact-sync logic is uploaded as a temporary PowerShell script
  and then invoked remotely, avoiding `ssh -EncodedCommand` command-line length
  limits while keeping terminal output text-only.
