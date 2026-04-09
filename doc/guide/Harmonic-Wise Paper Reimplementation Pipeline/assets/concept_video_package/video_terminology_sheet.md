# Harmonic-Wise Pipeline Terminology Sheet

## Required Terms

- `Transmission Error (TE)`
- `harmonic-wise pipeline`
- `selected harmonics`
- `cosine coefficient`
- `sine coefficient`
- `amplitude`
- `phase`
- `TE reconstruction`
- `mean percentage error`
- `offline benchmark`

## Preferred Definitions

- `harmonic-wise pipeline`
  a workflow that predicts harmonic descriptors of a full TE curve rather than
  point-wise TE samples directly.
- `selected harmonics`
  the specific harmonic orders kept as the compact representation of the curve.
- `cosine coefficient` / `sine coefficient`
  the coefficient pair used to encode one harmonic contribution.
- `amplitude`
  the magnitude of one harmonic contribution.
- `phase`
  the angular shift associated with one harmonic contribution.
- `TE reconstruction`
  rebuilding the full TE curve from the predicted harmonic terms.
- `mean percentage error`
  the curve-level percentage error used as the main paper-comparable offline
  metric.

## Terms To Avoid Replacing Casually

- do not replace `harmonic-wise` with vague phrases like `frequency thing`
- do not collapse `reconstruction` into generic `prediction`
- do not describe `Target A` as an online benchmark
