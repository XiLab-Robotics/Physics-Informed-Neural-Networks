# Track 1 Bidirectional Original-Dataset Interrupted Discard Closeout Campaign Results Report

## Overview

This report closes the interrupted remote campaign that had been prepared in:

- `doc/reports/campaign_plans/track1/exact_paper/2026-04-25-12-02-54_track1_bidirectional_original_dataset_mega_campaign_plan_report.md`

Campaign identity:

- campaign name:
  `track1_bidirectional_original_dataset_mega_campaign_2026-04-25_17_07_07`
- prepared state source:
  `doc/running/active_training_campaign.yaml`
- intended queue size: `400`
- intended surface: `10` families x `20` attempts x `2` directions

The operator process on the local workstation crashed while the remote run was
active, and the queue was later found inactive on the remote workstation with
no remaining Python process.

This report therefore performs an interrupted closeout with explicit scientific
discard policy.

## Objective And Outcome

The intended objective of the interrupted campaign was:

1. rebuild the full bidirectional original-dataset exact-paper family bank from
   zero;
2. explore `20` attempts per family-direction surface;
3. promote only accepted post-campaign winners into the canonical Track `1`
   benchmark and family archives.

Actual outcome:

- the campaign did not complete;
- the remote process is no longer active;
- only a prefix of the queue produced validation bundles;
- the campaign is closed as `interrupted`;
- the partial scientific results are discarded and will not be promoted into
  benchmark, registry, or archive surfaces.

## Closeout Policy

| Surface | Policy |
| --- | --- |
| Campaign execution state | `interrupted` |
| Scientific reuse | discarded |
| Resume policy | forbidden |
| Benchmark promotion | forbidden |
| Registry promotion | forbidden |
| Family archive refresh | forbidden |
| Operational traceability | preserved |

## Verified Execution Evidence

The following facts were verified during closeout:

- the canonical campaign state file still showed `status: running`, but that
  state was stale;
- no Python training process remained active on the remote workstation;
- the latest remote validation bundle timestamp was
  `2026-04-25T19:30:56`;
- the latest completed run discovered on the remote workstation was:
  `track1_original_dataset_forward_dt_attempt_11`;
- the local wrapper log stopped on the next intended queue item:
  `track1_original_dataset_forward_dt_attempt_11.yaml` as the active validation
  line.

## Completed Campaign Prefix

The interrupted run completed the following contiguous prefix of the queue:

- `forward/SVR`: attempts `01-20`
- `forward/MLP`: attempts `01-20`
- `forward/RF`: attempts `01-20`
- `forward/DT`: attempts `01-11`

No evidence was found for completed runs beyond `forward/DT attempt 11`.

## Queue Accounting

| Quantity | Count |
| --- | ---: |
| Intended total queue size | `400` |
| Verified completed runs in interrupted wave | `71` |
| Remaining runs never completed | `329` |
| Completed directions | `forward` prefix only |
| Completed backward runs | `0` |

## Why The Results Are Discarded

The interrupted wave is not treated as a resumable or promotable scientific
campaign for three reasons.

1. The remote run crossed multiple tooling-fix generations:
   ONNX dependency hardening, path/bootstrap repairs, progress-surface cleanup,
   and `MLP` stabilization were not all present at the same time.
2. The local operator process crashed, so wrapper-level bookkeeping and final
   artifact synchronization are incomplete.
3. The user explicitly requested a fresh restart after the current known fixes,
   preceded by a smaller remote gate campaign.

Because of that, the interrupted prefix is useful only as operational evidence,
not as accepted Track `1` scientific output.

## Preserved Evidence Roots

Operational evidence remains preserved under:

- local wrapper-tracking root:
  `.temp/remote_training_campaigns/2026-04-25-17-07-23_track1_bidirectional_original_dataset_mega_campaign_2026_04_25_17_07_07/`
- remote validation artifact root:
  `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/`
- remote training-campaign root:
  `output/training_campaigns/track1/exact_paper/bidirectional_original_dataset/`

These paths remain useful for troubleshooting and provenance only.

## Canonical Impact

This closeout intentionally does **not** update:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- family or program best-run registries
- `models/paper_reference/rcim_track1/`

The next canonical step is a fresh forward-only remote micro-campaign that
tests one run per family with the current hardened launcher stack before a
brand-new bidirectional mega-campaign is generated from zero.

## Final Conclusion

The interrupted `400`-run bidirectional original-dataset mega-campaign is
closed as an operationally traceable but scientifically discarded wave.

Its verified completion depth is `71 / 400`, ending at
`track1_original_dataset_forward_dt_attempt_11`.

No resume should be attempted. The correct continuation path is:

1. prepare and run the fresh forward-only remote micro-campaign;
2. verify the repaired remote stack on `10` total runs;
3. regenerate the full bidirectional mega-campaign from zero.
