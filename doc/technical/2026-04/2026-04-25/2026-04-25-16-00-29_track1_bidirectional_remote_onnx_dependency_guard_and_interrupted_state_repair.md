# 2026-04-25-16-00-29 Track1 Bidirectional Remote Onnx Dependency Guard And Interrupted State Repair

## Overview

The active `Track 1` bidirectional original-dataset mega-campaign was manually
interrupted after the first remote launch exposed a real ONNX-export failure on
the remote workstation.

The persistent campaign state currently still says `running`, while the user
has explicitly stated that the campaign has been interrupted. That state must
be reconciled before the next launch.

The remote campaign log also shows that the current ONNX export path fails for
`SVR` and `MLP` with the misleading error `'NoneType' object is not callable`.
The failure happens during ONNX conversion and indicates that the export code is
using optional ONNX converter symbols before verifying that the corresponding
dependencies were imported correctly on the remote workstation.

## Technical Approach

The repair should address both the state mismatch and the ONNX export failure in
one coherent pass.

First, the active campaign state should be updated from `running` to
`interrupted` with an explicit interruption note, so the repository again
matches the real operator state.

Second, the ONNX export helper should be hardened so that every optional ONNX
dependency is asserted before first use. In particular, the scikit-learn ONNX
path must verify that both `convert_sklearn` and `FloatTensorType` are
available before constructing the shared `initial_types` signature. This
ensures that a missing or broken `skl2onnx` install produces an explicit
dependency error instead of the current misleading `NoneType` failure.

Third, the remote preflight should be extended to validate the complete ONNX
toolchain required by the families in this campaign:

- `skl2onnx`
- `onnxmltools`
- `onnxconverter-common`
- plus the already optional family-specific runtime dependencies such as
  `xgboost` and `lightgbm`

Fourth, the `MLP` configuration should be stabilized. The current remote log
shows repeated `overflow encountered in dot` warnings and
`Maximum iterations (200) reached` convergence warnings. The repair pass should
therefore revisit the effective `MLP` training defaults used by this branch and
raise or otherwise adjust the maximum-iteration budget so the family is not
systematically capped too early during the remote campaign.

Finally, before relaunching the full `400`-run bundle, a dedicated remote
micro-campaign should be prepared and executed with exactly one run per family,
for a total of `10` training runs. That small package should be used as the
controlled remote diagnostic surface to confirm:

- ONNX export succeeds for every family with the repaired dependency guards;
- `MLP` no longer emits the same early-cap maximum-iteration behavior by
  default;
- no new remote bootstrap, packaging, or artifact-sync regressions were
  introduced by the repair.

The bidirectional mega-campaign preparation pipeline should then be updated so
this ONNX/bootstrap contract and the validated family-level runtime assumptions
are preserved in the prepared campaign state and launcher documentation for
future re-preparations.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.ps1`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_original_dataset_mega_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_original_dataset_mega_campaign.py`
- `doc/scripts/campaigns/run_track1_bidirectional_original_dataset_mega_campaign.md`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/`

## Implementation Steps

1. Reconcile the active campaign state with the real interrupted operator state.
2. Add explicit optional-dependency guards to the ONNX export code before any
   ONNX converter symbol is called.
3. Extend the remote preflight to validate the ONNX converter stack needed by
   the campaign before training starts.
4. Adjust the effective `MLP` runtime configuration, including the maximum
   iteration budget, to reduce the repeated convergence-cap warnings seen in
   the interrupted remote run.
5. Prepare a remote micro-campaign with exactly one run per family, execute it
   on the remote workstation, and inspect the resulting warnings, ONNX export
   status, and artifact synchronization behavior.
6. Promote the ONNX preflight/export contract and the validated repair
   assumptions into the bidirectional campaign preparation pipeline and launcher
   note.
7. Run targeted script checks and provide the relaunch command without
   committing.
