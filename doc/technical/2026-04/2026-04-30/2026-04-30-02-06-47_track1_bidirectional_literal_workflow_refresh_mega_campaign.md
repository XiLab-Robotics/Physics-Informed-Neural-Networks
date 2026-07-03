# 2026-04-30-02-06-47 Track1 Bidirectional Literal Workflow Refresh Mega Campaign

## Overview

This task prepares a full `RCIM Model-Bank Reproduction` refresh campaign after the exact-paper
family bank was realigned to the recovered original RCIM workflow.

The campaign must regenerate the canonical repository-owned `RCIM Model-Bank Reproduction`
bidirectional surface from the literalized implementation rather than from the
older approximate reimplementation. That means rerunning the complete
family-by-direction bank for both:

- `forward`
- `backward`

across the ten exact-paper families:

- `SVR`
- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The resulting campaign becomes the new scientific baseline for the
paper-reimplementation branch, while older campaign artifacts remain historical
evidence only.

## Technical Approach

The campaign will reuse the established `original_dataset_exact_model_bank`
bidirectional mega-campaign architecture, but it will be rebuilt as a fresh
package whose scientific meaning is explicitly tied to the newly literalized
workflow.

The preparation will keep the previous successful bidirectional mega-campaign
shape as the starting point:

- one full family bank per run;
- one playback direction per run;
- one immutable run instance per YAML config;
- one remote-capable launcher;
- one persistent active-campaign state entry.

The queue design remains a `20`-surface grid:

- `10` families for `forward`
- `10` families for `backward`

and each family-direction surface will again receive `20` split-seed attempts,
for a total target budget of `400` runs.

This is intentionally a full refresh rather than a narrow residual-cell repair
wave because the underlying implementation semantics changed at the shared
family-bank layer. A mixed benchmark that combines pre-alignment and
post-alignment family banks would no longer be canonically defensible.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `scripts/campaigns/track_1/exact_paper/`
- `doc/reports/campaign_plans/track_1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `models/paper_reference/rcim_track1/`

Subagents:

- none planned;
- any later delegation would require explicit user approval before launch.

## Implementation Steps

1. Freeze the literal-workflow bidirectional refresh scope in this technical
   document and in a dedicated planning report.
2. Reuse the established bidirectional mega-campaign structure and confirm the
   exact ten-family, two-direction, twenty-attempt queue design.
3. After approval, generate a fresh campaign package whose naming and docs
   explicitly mark it as the post-literal-alignment refresh baseline.
4. Update `doc/running/active_training_campaign.yaml` to the new prepared
   state only when the user explicitly approves the generated campaign package.
5. After campaign execution, close out the results as the new canonical RCIM Model-Bank Reproduction
   baseline and refresh the benchmark, master summary, and reference archives.
