# Track 2 Backward Retuned Baseline Rule

## Overview

This technical document plans the documentation-only formalization of the
`Track 2` backward comparison baseline.

The RCIM paper does not provide a paper-original backward benchmark equivalent
to the forward Tables `2`-`5` reference surface. The repository therefore needs
an explicit rule for `Target A` and `Track 2` closeout wording: the backward
offline comparison should use the repository-owned recovered-original retuned
backward archive as the canonical paper-derived backward baseline.

## Technical Approach

The implementation will update the canonical operational and analytical
documentation without changing training code, model archives, or campaign
artifacts.

The rule to formalize is:

- forward `Target A` comparison remains anchored to the paper-original and
  paper-retuned forward references, with the current best practical reference
  selected from the available forward comparison matrix;
- backward `Target A` comparison uses `paper_retuned_best_Bw` as the canonical
  paper-derived baseline because no paper-original backward reference exists;
- `Track 1` remains closed as a faithful full-dataset reproduction surface, not
  as the numeric winner for every offline comparison cell;
- `Track 2` closeout should state the forward and backward baselines separately
  so future waves do not conflate paper-original availability with retuned
  backward evidence.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/README.md`

No subagent is planned. If subagent use becomes useful later, it must be
declared and approved before launch.

## Implementation Steps

1. Update the live backlog `Target A` and `Track 2` closeout wording with the
   backward retuned-baseline rule.
2. Update the canonical `Track 2` comparison report so the rule is visible next
   to the best composite references and closeout interpretation.
3. Update the master summary only if its current `Target A` or roadmap wording
   would otherwise remain ambiguous.
4. Run Markdown QA on the touched Markdown files with the repository-owned
   tooling.
5. Report the completed documentation changes and wait for explicit commit
   approval.
