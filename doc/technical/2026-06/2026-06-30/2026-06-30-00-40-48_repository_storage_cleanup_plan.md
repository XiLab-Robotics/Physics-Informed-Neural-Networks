# Repository Storage Cleanup Plan

## Overview

The local repository checkout has grown to roughly `216 GiB`, with the largest
contributors concentrated in generated artifacts, local ignored model bundles,
Git object storage, datasets, and temporary folders. This cleanup plan defines
an evidence-first review workflow before removing files.

No subagent is planned. No active training campaign is currently protected by
`doc/running/active_training_campaign.yaml`.

The first cleanup pass is limited to ignored or non-tracked local artifacts so
that disk space can be recovered without changing Git history or removing
canonical tracked evidence. Later passes may consider tracked Git or Git LFS
removal, but those require separate review because they affect GitHub and
historical reproducibility.

## Technical Approach

- Separate local disk cleanup from repository-history cleanup.
- Do not delete active campaign state, registries, closeout reports, promoted
  model archives, or accepted reference datasets.
- Treat `original pipeline`, `RCIM Model-Bank Reproduction`, `Wave 1`, `Wave 2`,
  and later wave artifacts as in-scope reference material unless specific
  evidence shows that a file is obsolete, duplicated, failed, or superseded.
- Treat pre-original-pipeline and pre-Track-1 experiments as cleanup candidates,
  but validate them against reports, registries, and current model references
  before deletion.
- Prefer exact path manifests for destructive cleanup rather than broad
  wildcard deletion.
- Keep Git LFS cleanup separate from local ignored-file deletion because
  deleting an LFS-tracked file from the current branch does not remove the
  historical LFS object from GitHub storage.

## Involved Components

- `output/training_runs/`
- `output/validation_checks/`
- `output/training_campaigns/`
- `output/registries/`
- `.git/lfs/objects/`
- `.temp/`
- `.tmpdocenv/`
- `doc/running/active_training_campaign.yaml`
- `doc/README.md`

## Implementation Steps

1. Inventory repository size by top-level directory, `output/` root, tracked
   files, ignored files, untracked files, and Git LFS objects.
2. Build a first local-cleanup manifest containing only ignored or non-tracked
   files that can be removed without changing Git history.
3. Review each first-pass candidate with the user before deletion.
4. After approval, remove only approved local paths and re-run `git status`,
   size inventory, and protected-campaign checks.
5. Build a second tracked-artifact review matrix for Git and Git LFS files,
   separating `keep`, `candidate removal`, and `needs historical review`.
6. For any Git or Git LFS deletion, create a separate approval-gated commit
   plan and document whether GitHub storage is actually reduced or whether
   history rewrite/LFS object retention remains.

## Initial Local Cleanup Manifest

These files and folders are ignored or non-tracked in the current checkout.
They are candidates for local deletion only after explicit approval.

### High-Confidence Local Deletion Candidates

| Size | Path | Evidence |
| ---: | --- | --- |
| `87.446 GiB` | `output/training_runs/tree/2026-04-03-20-38-08__te_random_forest_remote_medium/tree_model.pkl` | Ignored by `.gitignore`; documented as an oversized RandomForest exportability constraint; later Wave 1 tree exports and registries point to smaller promoted `tree_model.pkl` artifacts. |
| `7.265 GiB` | `output/training_runs/tree/2026-03-20-17-15-25__te_random_forest_tabular_recovery/tree_model.pkl` | Ignored by `.gitignore`; older recovery artifact; not the current promoted tree reference. |
| `25.740 GiB` | `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/family_exploration/rf/*/harmonic_model_bundle.pkl` | Fourteen exact ignored paths; audited as non-competitive legacy RandomForest harmonic-wise bundles; small metadata and reports retain the outcome evidence. |
| `1.788 GiB` | `.temp/npm-cache/` | Temporary cache under ignored `.temp/`; not repository evidence. |
| `0.972 GiB` | `.tmpdocenv/` | Ignored temporary documentation environment. |

### Needs Review Before Local Deletion

| Size | Path | Review reason |
| ---: | --- | --- |
| `6.740 GiB` | `.temp/remote_training_campaigns/` | Temporary remote-campaign transfer/cache material; verify that no unique run output exists only here before deletion. |
| `0.448 GiB` | `.temp/maxi_recovery/` | Temporary recovery material; inspect contents before deletion. |
| `0.079 GiB` | `.temp/stream_probe/` | Temporary probe material; inspect contents before deletion. |

### Not In This First Pass

- Git-tracked `output/validation_checks/` artifacts.
- Git LFS objects under `.git/lfs/objects/`.
- Canonical datasets under `data/`.
- Promoted model archives under `models/`.
- Campaign closeout artifacts under `doc/` and `output/training_campaigns/`.

## First Local Cleanup Result

The approved high-confidence local cleanup pass removed all `18` manifest
entries:

- Two ignored oversized `tree_model.pkl` files under `output/training_runs/`.
- Fourteen ignored legacy RandomForest harmonic-wise validation bundles under
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`.
- The ignored `.temp/npm-cache/` folder.
- The ignored `.tmpdocenv/` temporary documentation environment.

The post-cleanup inventory reported:

| Path | Files | Size |
| --- | ---: | ---: |
| `.git` | `6046` | `31.455 GiB` |
| `data` | `4912` | `25.045 GiB` |
| `output` | `10193` | `15.283 GiB` |
| `reference` | `4494` | `11.440 GiB` |
| `.temp` | `194` | `7.338 GiB` |
| `doc` | `7549` | `3.475 GiB` |
| `models` | `3303` | `1.881 GiB` |
| `.tmpdocenv` | `0` | `0 GiB` |

`git status` remained clean for tracked artifact deletions because the removed
paths were ignored or local-only. The only tracked repository change after this
cleanup pass is the documentation update for this plan and its `doc/README.md`
registration.

## Second Local Cleanup Result

The approved `.temp/` residual cleanup removed the three reviewed temporary
roots:

- `.temp/remote_training_campaigns/`
- `.temp/maxi_recovery/`
- `.temp/stream_probe/`

The post-cleanup inventory reported:

| Path | Files | Size |
| --- | ---: | ---: |
| `.git` | `6046` | `31.455 GiB` |
| `data` | `4912` | `25.045 GiB` |
| `output` | `10193` | `15.283 GiB` |
| `reference` | `4494` | `11.440 GiB` |
| `doc` | `7549` | `3.475 GiB` |
| `models` | `3303` | `1.881 GiB` |
| `.temp` | `113` | `0.052 GiB` |
| `.tmpdocenv` | `0` | `0 GiB` |

The remaining `.temp/` footprint is small and consists of repository-local
working, validation, and debug folders plus `aries_call.txt`. No tracked
artifact deletion was introduced by this second local cleanup pass.

## Tracked Artifact Review

The tracked working tree inventory after local cleanup identified these largest
roots:

| Root | Files | Size | Initial decision |
| --- | ---: | ---: | --- |
| `data/` | `4912` | `25.045 GiB` | Keep for now. Contains canonical `original_dataset`, `polished_dataset`, `original_pipeline_instances`, and `simplified_dataset` material. |
| `output/validation_checks/` | `6385` | `14.327 GiB` | Review. This is the main current-branch cleanup target. |
| `reference/` | `2342` | `10.909 GiB` | Keep for now. Contains recovered original-pipeline assets and canonical video source references. |
| `doc/` | `7548` | `3.475 GiB` | Keep. Authored reports and promoted documentation evidence. |
| `models/` | `3303` | `1.881 GiB` | Keep for now. Promoted model archives. |

The largest tracked `output/validation_checks/` roots are:

| Root | Files | Size | Evidence and recommendation |
| --- | ---: | ---: | --- |
| `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/` | `2687` | `7.269 GiB` | Candidate removal from current branch. The root contains only `.pkl` model-bank intermediates. Repository notes state intermediate validation-model `.pkl` bundles under this root should stay out of Git tracking, with curated accepted archives retained under `models/`. |
| `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/` | `326` | `4.798 GiB` | Candidate partial removal from current branch. Keep the `256` small YAML summaries, but remove the `70` tracked `.pkl` harmonic bundles. The latest harmonic-wise summary documents a `not_yet_met` status, and the current accepted RCIM reproduction is elsewhere. |
| `output/validation_checks/rcim_model_bank_reproduction/` | `770` | `0.737 GiB` | Keep. This root contains the accepted June polished-dataset RCIM Model-Bank Reproduction forward and backward surfaces referenced by active registries and closeout reports. |
| Wave and `TE Curve Verification Pipeline` report roots | mixed | about `1.523 GiB` | Keep for now. These are in the user's in-scope wave and verification history. |

The Git LFS inventory found `41` tracked LFS files. The first cleanup target
would remove LFS pointers for `31` old validation `.pkl` files under the two
`paper_reimplementation_*` roots while keeping:

- the two accepted polished `rcim_model_bank_reproduction` LFS bundles;
- the canonical `reference/video_guides/source_bundle/` LFS source media.

This current-branch deletion would reduce checkout size and future normal pulls
on the branch. It would not by itself erase historical Git blobs or historical
Git LFS storage on GitHub; true remote storage reduction would require a
separate history-rewrite or GitHub LFS retention cleanup decision.

The exact proposed tracked-removal manifest for the next approval gate is:

| Candidate | Files | Working-tree size | Action |
| --- | ---: | ---: | --- |
| `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/**/*.pkl` | `2687` | `7.269 GiB` | Remove from Git current branch. |
| `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/**/*.pkl` | `70` | `4.796 GiB` | Remove from Git current branch, keep YAML evidence. |
| Matching `.gitattributes` path-specific LFS entries for removed files | `31` | metadata only | Remove together with the tracked file deletion. |

Estimated current-branch checkout reduction from this tracked artifact pass is
`12.065 GiB`.

## Tracked Artifact Cleanup Result

The approved tracked-artifact cleanup removed `2757` `.pkl` files from the
current Git branch with `git rm`:

- `2687` intermediate `paper_family_model_bank.pkl` files from
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`;
- `70` intermediate `harmonic_model_bundle.pkl` files from
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`.

The cleanup also removed `31` obsolete path-specific LFS rules from
`.gitattributes`. The remaining LFS rules cover only the canonical
`reference/video_guides/source_bundle/` media files and the two accepted
polished-dataset `rcim_model_bank_reproduction` bundles.

The post-cleanup inventory reported:

| Path | Files | Size |
| --- | ---: | ---: |
| `.git` | `6046` | `31.454 GiB` |
| `data` | `4912` | `25.045 GiB` |
| `reference` | `4494` | `11.440 GiB` |
| `doc` | `7549` | `3.475 GiB` |
| `output` | `7436` | `3.218 GiB` |
| `output/validation_checks` | `3628` | `2.262 GiB` |
| `models` | `3303` | `1.881 GiB` |
| `.temp` | `64` | `0.036 GiB` |

The reviewed roots now contain:

| Root | Files | Size | `.pkl` files | YAML files |
| --- | ---: | ---: | ---: | ---: |
| `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/` | `0` | `0 GiB` | `0` | `0` |
| `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/` | `256` | `0.001 GiB` | `0` | `256` |
| `output/validation_checks/rcim_model_bank_reproduction/` | `770` | `0.737 GiB` | `382` | `770` |

This pass reduces the current checkout size and the future current-branch
pull footprint. Historical Git blobs and already uploaded historical Git LFS
objects remain a separate remote-storage cleanup question.
