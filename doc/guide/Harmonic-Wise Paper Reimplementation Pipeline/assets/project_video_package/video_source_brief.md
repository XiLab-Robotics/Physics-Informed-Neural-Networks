# Harmonic-Wise Pipeline Project Video Source Brief

## Audience

- repository readers who want to understand why this branch was added
- colleagues who need a briefing on the paper-faithful reproduction path
- users who need the distinction between `Track 1` and `Track 2`

## Video Goal

Explain the harmonic-wise pipeline as the repository's paper-faithful offline
reimplementation branch created to reproduce the RCIM paper logic before the
future online compensation path.

## Target Depth

- repository motivation first
- implementation structure second
- benchmark meaning third

## Required Chapter Order

1. Why the repository needed a separate paper-faithful branch.
2. How the branch changes the learning problem compared with direct-TE models.
3. How the current repository implementation is structured in code and artifacts.
4. What the first offline baseline already proved.
5. What is still missing for the future online benchmark.

## Required Takeaways

- This branch exists to reproduce the paper's harmonic-wise logic, not to replace the direct-TE leaderboard.
- The repository now has an inspectable offline paper-comparable protocol.
- The current baseline is informative even though `Target A` is not yet met.
- The future online compensation branch remains a separate follow-up scope.

## Concepts That Must Stay Brief

- generic textbook harmonic analysis already covered by the concept track
- unrelated model-family history
- speculative deployment details beyond the current backlog

## Concepts That Must Not Be Omitted

- why `Track 1` exists
- how the supervised problem changes
- current artifact and reporting paths
- current benchmark status
- remaining gap to `Table 9`
