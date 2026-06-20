# Harmonic-Wise Pipeline Project Video Terminology Sheet

## Required Terms

- `RCIM Model-Bank Reproduction`
- `paper-faithful`
- `harmonic-wise comparison pipeline`
- `TE Curve Verification Pipeline`
- `direct-TE`
- `Target A`
- `Target B`
- `offline-only`
- `Table 9`
- `paper vs repository`

## Preferred Definitions

- `RCIM Model-Bank Reproduction`
  the repository branch dedicated to paper-faithful harmonic-wise reproduction.
- `TE Curve Verification Pipeline`
  the separate branch that compares already trained direct-TE models under a
  common offline evaluator.
- `Target A`
  the offline paper-comparable threshold.
- `Target B`
  the future online compensation benchmark.

## Terms To Keep Distinct

- do not merge `paper-faithful` with `direct-TE comparable`
- do not describe `offline-only` as end-to-end replication
- do not describe `Target A` as the final paper benchmark
