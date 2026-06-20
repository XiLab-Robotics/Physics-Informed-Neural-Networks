# Wave 5.1 And Wave 5.2 Parallel Hardening Plan

## Purpose

This preliminary plan defines a non-campaign hardening pass for the committed
`Wave 5.1` and `Wave 5.2A` embryonic skeletons while the separate `Wave 4 series`
campaign runs elsewhere.

The plan has two outputs:

- a `Wave 5.1` training-smoke-ready validation path;
- a `Wave 5.2A` MMT equation diagnostic report generator.

This is not a training campaign. It must not create real campaign queues,
mutate `doc/running/active_training_campaign.yaml`, update registries, or run
official `TE Curve Verification Pipeline` verification.

## Scope

| Stream | Planned Output | Campaign Readiness |
| --- | --- | --- |
| `Wave 5.1` | One-batch training-stack validation for `wave3_harmonic_prior_residual`. | still not campaign-ready |
| `Wave 5.1` | Dry-run PowerShell wrapper and launcher note for the one-batch check. | still not campaign-ready |
| `Wave 5.2A` | MMT demonstration diagnostic report with harmonic summary. | diagnostic-only |
| `Wave 5.2A` | Companion validation tables under `output/validation_checks/`. | diagnostic-only |

## Boundaries

This pass may:

- compile and import new scripts;
- run one-batch validation for the Wave 5.1 skeleton;
- generate a Wave 5.2A diagnostic Markdown report and small companion tables;
- update documentation and Sphinx portal entries for new dry-run commands.

This pass must not:

- launch a multi-run or multi-epoch training campaign;
- create active queue YAMLs;
- edit `doc/running/active_training_campaign.yaml`;
- update model registries or campaign winner artifacts;
- use `Wave 4 series` results before that campaign is closed out;
- treat MMT equations as a hard physics loss.

## Planned Files

| Area | Candidate Files |
| --- | --- |
| Wave 5.1 validator | `scripts/campaigns/wave_3/validate_wave3_training_smoke_ready.py` |
| Wave 5.1 launcher | `scripts/campaigns/wave_3/run_wave3_training_smoke_ready_checks.ps1` |
| Wave 5.1 launcher note | `doc/scripts/campaigns/wave_3/wave3_training_smoke_ready_checks.md` |
| Wave 5.2A report script | `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py` |
| Wave 5.2A script note | `doc/scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.md` |
| Wave 5.2A report output | `doc/reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/` |
| Wave 5.2A validation output | `output/validation_checks/wave4_mmt_equation_diagnostic/` |

## Verification Plan

The pass is complete only after:

- Python compilation passes for new and touched scripts;
- the Wave 5.1 training-smoke-ready validator passes;
- the Wave 5.1 dry-run wrapper passes and does not launch training;
- the Wave 5.2A diagnostic report generator creates the Markdown report and
  companion validation data;
- Markdown QA passes for touched authored Markdown;
- Sphinx builds with `-W` if `site/` or included guide content changes;
- `git diff --check` passes.

## Materialized Hardening Outputs

| Stream | File Or Artifact | Status |
| --- | --- | --- |
| Wave 5.1 | `scripts/campaigns/wave_3/validate_wave3_training_smoke_ready.py` | implemented |
| Wave 5.1 | `scripts/campaigns/wave_3/run_wave3_training_smoke_ready_checks.ps1` | implemented and validated |
| Wave 5.1 | `doc/scripts/campaigns/wave_3/wave3_training_smoke_ready_checks.md` | implemented |
| Wave 5.1 | `output/validation_checks/wave3_harmonic_prior_residual/2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final/validation_summary.yaml` | finite checks passed |
| Wave 5.2A | `scripts/reports/analysis/build_wave4a_mmt_equation_diagnostic_report.py` | implemented |
| Wave 5.2A | `doc/reports/analysis/wave4/mmt_equation_diagnostic/[2026-06-11]/wave4a_mmt_equation_diagnostic.md` | generated |
| Wave 5.2A | `output/validation_checks/wave4_mmt_equation_diagnostic/2026-06-11-19-25-32__wave4a_mmt_equation_diagnostic/` | generated |

## Decision Gates

After this hardening pass:

- `Wave 5.1` may become eligible for a later real campaign package only after
  `Wave 4 series` selects or rejects robust-loss defaults;
- `Wave 5.2A` may feed `Wave 5.2B` or `Wave 5.2C` only if the diagnostic report
  shows useful, interpretable signals and the missing MMT parameter inventory
  is explicitly resolved;
- no campaign launch is approved by this plan.
