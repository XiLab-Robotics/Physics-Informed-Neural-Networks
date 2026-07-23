# Track 2 Closeout Report Path Cleanup

## Overview

The causal offset bounded `TE Curve Verification Pipeline` closeout report is
currently stored directly under `doc/reports/campaign_results/track_2/`. That
root is too flat for concrete closeout deliverables and makes the report look
like a generic Track 2 result instead of a bounded-screen closeout.

The report should move under:

`doc/reports/campaign_results/track_2/campaign_closeouts/`

The move should keep the Markdown, PDF, plot references, active-state pointers,
and styled-PDF behavior consistent.

## Technical Approach

Move the causal offset bounded closeout Markdown and PDF into the
`campaign_closeouts` subtree and update every repository-owned reference that
points to the old location. Because the Markdown image paths are relative to
the report location, the `Pilot Graphs` image links must be adjusted after the
move so the regenerated PDF still embeds the existing
measured-versus-predicted Track 2 plot package under
`doc/reports/campaign_results/track_2/verification_plots/`.

The styled-PDF generator already uses the report stem for the report-specific
`Metric Ranking` page break, so the path move should not require a new report
identifier.

No subagent use is planned. If subagent review becomes useful, approval will be
requested before launching it.

## Involved Components

- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-07-23-13-18-49_causal_offset_bounded_track2_screen_closeout_report.md`
- `doc/reports/campaign_results/track_2/campaign_closeouts/2026-07-23-13-18-49_causal_offset_bounded_track2_screen_closeout_report.pdf`
- `doc/reports/campaign_results/track_2/campaign_closeouts/`
- `doc/reports/campaign_results/track_2/verification_plots/`
- `doc/running/active_training_campaign.yaml`
- `doc/technical/2026-07/2026-07-23/2026-07-23-13-26-30_remote_campaign_output_readability_fix.md`
- `doc/README.md`

## Implementation Steps

1. Re-check the worktree and active campaign state before moving the closeout.
2. Create `doc/reports/campaign_results/track_2/campaign_closeouts/` if needed.
3. Move the closeout Markdown and PDF into the new closeout subtree.
4. Update repository references from the old closeout path to the new path.
5. Adjust relative image links in the moved Markdown from
   `verification_plots/...` to `../verification_plots/...`.
6. Regenerate the styled PDF from the moved Markdown.
7. Raster-validate the real PDF, confirming table page starts and
   `Pilot Graphs` image embedding still work.
8. Run Markdown QA on touched Markdown, Python compile checks if report tooling
   changes, and `git diff --check`.
