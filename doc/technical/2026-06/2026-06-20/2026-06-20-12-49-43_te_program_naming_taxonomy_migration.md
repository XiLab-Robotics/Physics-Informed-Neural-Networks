# TE Program Naming Taxonomy Migration

## Overview

The repository currently uses `Track 1` and `Track 2` for several concepts
that no longer belong at the same semantic level. `Track 1` identifies the
paper-faithful RCIM harmonic model-bank reproduction, while `Track 2` is used
both for the official curve-verification pipeline and for diagnostic or
model-development branches such as `Track 2B` through `Track 2H-L`.

This project will replace that overloaded terminology with three explicit
program layers:

1. `RCIM Model-Bank Reproduction` for the former `Track 1`;
2. `Model Development Waves` for training and experimental model families;
3. `TE Curve Verification Pipeline` for model evaluation, curve diagnostics,
   selection, visualization, and report generation.

The migration will update repository-authored documentation comprehensively
while preserving historical machine identifiers wherever changing them would
break artifact traceability, registry lookup, reproducibility, or links to
completed campaign outputs.

No subagent is planned for this work. If later scope growth makes subagent use
useful, the delegated task boundary will be documented and explicit user
approval will be requested before launch.

## Technical Approach

### Canonical Terminology

The following names will become canonical:

| Legacy term | Canonical term | Canonical slug |
| --- | --- | --- |
| `Track 1` | `RCIM Model-Bank Reproduction` | `rcim_model_bank_reproduction` |
| `Track 2` evaluation workflow | `TE Curve Verification Pipeline` | `te_curve_verification` |
| `Track 2` official refresh | `TE Curve Verification refresh` | `te_curve_verification_refresh` |
| `Track 2` leader | `curve-verified leader` | not applicable |
| `Track 2` matrix | `curve-verification matrix` | not applicable |

The former evaluation-only branches will become named verification modules:

| Legacy term | Canonical module name |
| --- | --- |
| `Track 2B` | `Curve-First Reranking` |
| `Track 2C` | `Curve Payload Diagnostics` |
| mean-centered `Track 2` diagnostic | `Mean-Centered Error Decomposition` |
| `Track 2D` | `Offset and Shape Matrix Audit` |
| `Track 2E` | `Causal Offset Feasibility Analysis` |

Where ordered module numbers improve navigation, the documentation may use:

| Module | Name |
| --- | --- |
| `CVP 1.1` | `Curve-First Reranking` |
| `CVP 1.2` | `Curve Payload Diagnostics` |
| `CVP 1.3` | `Mean-Centered Error Decomposition` |
| `CVP 1.4` | `Offset and Shape Matrix Audit` |
| `CVP 1.5` | `Causal Offset Feasibility Analysis` |

### Model Development Wave Mapping

Training and model-development branches will use a wave hierarchy independent
from the verification pipeline:

| Canonical wave | Description | Legacy scope |
| --- | --- | --- |
| `Wave 1` | Baseline Models | existing Wave 1 |
| `Wave 2.1` | Temporal Sequence Baselines | existing Wave 2 |
| `Wave 2.2` | Periodic Temporal Hybrids | existing Wave 2B |
| `Wave 2.3` | Residual Harmonic Temporal Hybrids | existing Wave 2C |
| `Wave 3.1` | Residual Offset Models | former Track 2F |
| `Wave 3.2` | Harmonic Residual Offset Models | former Track 2F-bis |
| `Wave 3.3` | Curve-Aware Objective Models | former Track 2G |
| `Wave 4.1` | Robust-Loss Models | former Track 2H robust-loss package |
| `Wave 4.2` | Quantile and Probabilistic Models | former Track 2H quantile package |
| `Wave 4.3` | Mixture-Density Models | former Track 2H mixture-density package |
| `Wave 4.4` | Latent-State and Hysteresis Models | former Track 2H-L |
| `Wave 5.1` | Harmonic-Prior Residual Models | existing Wave 3 |
| `Wave 5.2` | MMT/PINN-Guided Models | existing Wave 4 |
| `Wave 6` | Integrated Multi-Task and Multi-Head Models | deferred integrated branch |

### Historical Identifier Policy

The migration will distinguish prose terminology from immutable or
compatibility-sensitive identifiers.

The following will be renamed in repository-authored documentation:

- headings, narrative text, tables, status summaries, roadmaps, and captions;
- documentation labels for pipelines, modules, waves, and leaders;
- future-facing example names where no implemented identifier is implied;
- canonical index descriptions and documentation portal text;
- repository instructions that define future workflow terminology.

The following will normally remain unchanged and be identified as legacy names
when needed:

- completed `run_name`, `run_instance_id`, campaign ID, and model-family keys;
- paths to existing reports, models, outputs, registries, and validation data;
- script and configuration filenames required by current runnable workflows;
- historical report titles when they are quoted as artifact names;
- embedded artifact metadata and checksums;
- external or recovered RCIM source material under `reference/`;
- binary PDF contents unless a canonical maintained PDF must be regenerated.

This policy prevents a documentation rename from silently invalidating
reproducible evidence. A legacy identifier may appear in backticks after the
new conceptual name when it is necessary to locate an existing artifact.

### Migration Scope

The initial scope will cover Git-tracked repository-authored textual sources,
including:

- root `README.md` and `AGENTS.md`;
- canonical documentation under `doc/`;
- Sphinx source files under `site/`;
- repository-owned Markdown associated with scripts and campaigns;
- YAML, JSON, TOML, Python, and PowerShell comments or user-facing strings when
  they define or display the old documentation terminology.

Generated portal output, binary files, training artifacts, and third-party or
recovered references will not be bulk-rewritten.

Historical technical plans and campaign reports will be updated carefully.
Their narrative terminology will migrate, but literal historical commands,
paths, IDs, and artifact names will remain stable.

### Compatibility And Discovery

Canonical overview documents will include a concise legacy-name mapping so
older report paths remain understandable. Search checks will classify every
remaining occurrence as one of:

1. migrated canonical prose;
2. required legacy machine identifier;
3. historical artifact path or title;
4. external reference content;
5. missed migration requiring correction.

The work will not claim zero old-token occurrences because valid identifiers
such as `te_track2g_*` must remain searchable. Completion instead requires zero
unclassified legacy terminology in the touched repository-authored scope.

## Involved Components

- `README.md`
- `AGENTS.md`
- `doc/README.md`
- `doc/reference_summaries/`
- `doc/reports/analysis/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`
- `doc/scripts/`
- `doc/technical/`
- `doc/running/`
- `site/`
- documentation-facing strings and comments under `scripts/`
- campaign and model configuration descriptions where terminology is
  user-facing
- Markdown QA tooling under `scripts/tooling/markdown/`
- Sphinx documentation build

The current active-campaign state is `none`, so no protected campaign file is
active at planning time.

## Implementation Steps

1. Build a repository-wide inventory of legacy terms, distinguishing prose
   references from machine identifiers and historical paths.
2. Add a canonical naming and legacy-alias section to the main TE program
   documentation entry points.
3. Replace `Track 1` prose with `RCIM Model-Bank Reproduction`, using the more
   precise model-bank wording rather than implying full online RCIM system
   reproduction.
4. Replace evaluation-workflow uses of `Track 2` with
   `TE Curve Verification Pipeline`.
5. Rename the former `Track 2B` through `Track 2E` concepts as `CVP 1.1`
   through `CVP 1.5` verification modules.
6. Reclassify model-development uses of former `Track 2F` through
   `Track 2H-L` as Waves `3.1` through `4.4`.
7. Renumber the existing Wave 3 and Wave 4 conceptual documentation as
   Waves `5.1` and `5.2`, and describe the integrated branch as Wave 6.
8. Update status ledgers, master summaries, policies, roadmaps, report
   descriptions, launcher notes, technical plans, and Sphinx pages.
9. Preserve literal historical identifiers and paths, adding legacy labels
   where readers could otherwise confuse them with current terminology.
10. Inspect residual old-name matches and document why every retained class is
    necessary.
11. Run the repository Markdown style checker and markdownlint over the full
    intended Git-tracked authored Markdown scope.
12. Confirm touched Markdown files end with one normal final newline.
13. Build the Sphinx portal with warnings treated as errors.
14. Report the completed migration, remaining intentional legacy identifiers,
    validation results, and changed-file scope.
15. Stop before creating a Git commit and wait for explicit user approval.
