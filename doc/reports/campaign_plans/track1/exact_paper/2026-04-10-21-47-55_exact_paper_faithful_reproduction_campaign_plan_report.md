# Exact Paper Faithful Reproduction Campaign Plan Report

## Overview

This report defines the preparation target for the next `Track 1` campaign
package after the completed exact-paper model-bank stabilization campaign.

The repository already proved two important things:

- the harmonic-wise paper-faithful branch has a real offline benchmark path,
  but the best completed result still stops at `8.877%` and therefore misses
  the paper offline threshold `4.7%`;
- the exact-paper family bank can now execute end to end and export a stable
  ONNX surface under the current repository stack.

What is still missing is a campaign that ties these layers together in a
paper-faithful way instead of treating them as unrelated branches.

## Why This Campaign Makes Sense

The current state is operationally useful but scientifically incomplete.

If the repository stops here, it can only claim:

- a stabilized recovered exact-paper family bank;
- strong but still insufficient harmonic-wise offline results;
- no true reproduction of the paper benchmark.

The next campaign therefore needs to answer the paper-facing question directly:

1. can the repository reproduce the recovered exact-paper training logic as
   faithfully as the available evidence permits;
2. can the resulting predictors improve the harmonic-wise benchmark path that
   is actually tied to `Target A`;
3. can the repository serialize the remaining gaps cleanly enough that the
   later online benchmark phase becomes a bounded engineering task rather than
   an open-ended research branch.

## Campaign Intent

This is not a generic sweep and not only a family-bank export check.

It is a paper-faithful reproduction campaign with three aligned objectives:

- reproduce the recovered exact-paper training setup rigorously;
- evaluate whether that reproduction improves the harmonic-wise offline
  benchmark path;
- generate artifacts that remain reusable for the later online compensation
  benchmark.

## Technical Context

The paper comparison report already states the missing pipeline clearly:

1. harmonic-wise prediction of `A_k` and `phi_k`;
2. TE reconstruction from those predicted harmonic components;
3. offline motion-profile playback for `Robot` and `Cycloidal` style profiles;
4. later online compensation and final Table 9 style reporting.

This campaign should prepare the part that can be executed now without
claiming the online benchmark prematurely.

That means the prepared package should focus on:

- recovered exact-paper training logic;
- harmonic-wise target parameterization choices;
- TE reconstruction-ready outputs;
- comparable offline metrics for `Target A`.

## Candidate Run Matrix

| Config ID | Role | Planned Name | Main Variation | Main Question |
| --- | --- | --- | --- | --- |
| 1 | Recovered exact baseline | `exact_paper_recovered_reference` | strict recovered family bank with paper-era parameters and recovered target schema | Can the repository reproduce the recovered exact-paper training surface faithfully and stably? |
| 2 | Amplitude/phase benchmark handoff | `exact_paper_amplitude_phase_reference` | exact-paper target parameterization passed through the harmonic-wise evaluation path | Does the recovered `ampl_k` / `phase_k` parameterization improve the offline benchmark path relative to the current mainline setup? |
| 3 | Dominant-harmonic specialization | `exact_paper_dominant_harmonic_specialized` | preserve full RCIM harmonic set while specializing the dominant error terms, especially `h0` | Can targeted specialization close the largest known offline error sources without abandoning the full harmonic set? |
| 4 | Repository baseline comparison | `track1_current_best_shared_evaluator_reference` | current best harmonic-wise branch evaluated through the same shared offline evaluator | Under one comparable evaluator, how much does the exact-paper-faithful path really improve or fail to improve over the current repository baseline? |

## Parameter Notes

### Recovered Training Parameters

The campaign should treat paper-era parameters with explicit provenance:

- exact recovered values when they are present in the recovered scripts or
  assets;
- explicit repository-side approximation only when the recovered evidence is
  incomplete or incompatible with the current stack;
- every approximation serialized in the campaign note so the final report can
  distinguish true reproduction from reasoned reconstruction.

### Harmonic Target Schema

The campaign should preserve the recovered harmonic set currently used in the
paper-faithful offline branch:

- `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`

The preparation should not regress to reduced subsets that already proved too
weak to reach the paper threshold even under their truncation-only oracle.

### Shared Offline Evaluator

Every candidate run should be judged under one comparable offline evaluator:

- harmonic-wise prediction output;
- TE reconstruction;
- final TE-curve mean percentage error on held-out data;
- explicit `Target A` verdict;
- component-side diagnostic metrics kept as supporting evidence only.

## Evaluation Rules

The campaign should inspect four layers:

1. recovered-training fidelity:
   - family inventory;
   - parameter provenance;
   - preprocessing and split assumptions;
2. component-level prediction quality:
   - family-level and target-level harmonic metrics;
3. TE-level offline benchmark quality:
   - reconstructed TE-curve percentage error;
   - explicit `Target A` status against `4.7%`;
4. export and artifact surface:
   - ONNX export completeness where required;
   - reconstruction-ready output artifacts;
   - reproducible campaign bookkeeping.

## Success Criteria

The preparation phase is successful when it produces a campaign package that:

- preserves the recovered exact-paper training assumptions as explicitly as the
  repository evidence allows;
- keeps the full RCIM harmonic set as the mainline target surface;
- measures every run through a shared offline evaluator anchored to `Target A`;
- serializes unresolved paper-reproduction assumptions instead of hiding them;
- is ready to generate canonical campaign YAML files, a dedicated launcher, and
  the standard operator-facing launch command after approval.

## Expected Implementation Outputs

After approval of this planning report, the implementation phase should
produce:

1. the campaign YAML package under
   `config/paper_reimplementation/rcim_ml_compensation/`;
2. a dedicated PowerShell launcher under `scripts/campaigns/`;
3. the matching launcher note under `doc/scripts/campaigns/`;
4. a prepared campaign state entry in `doc/running/active_training_campaign.yaml`;
5. the exact terminal command needed for operator-driven execution.

## Next Step

If this report is approved together with the technical document, generate the
campaign package and launcher for the first exact-paper faithful reproduction
campaign rather than another narrow export-stability batch.
