# Harmonic-Wise Pipeline Project Video Fact Boundary Notes

## Facts That Must Stay Explicit

- The current repository branch is an offline paper-faithful reproduction path.
- The current baseline uses `HistGradientBoosting` regressors on harmonic
  target terms.
- The current baseline reports about `9.403%` mean percentage error on the
  held-out test split.
- The current paper-aligned offline threshold is `4.7%`.
- The current branch does not yet implement online compensation or the final
  `Table 9` benchmark.

## Facts That Must Not Be Overstated

- Do not claim that the repository already beats the paper offline.
- Do not claim that `Track 1` replaces the direct-TE branch.
- Do not claim that TwinCAT-side compensation is already integrated.

## Safe Framing

- It is correct to say that this branch gives the repository a proper
  paper-faithful offline comparison path.
- It is correct to say that the current result is informative but still below
  the paper target.
