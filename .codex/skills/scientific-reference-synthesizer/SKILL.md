---
name: scientific-reference-synthesizer
description: Use when synthesizing scientific or engineering references from reference/ and repository summaries into implementation-facing conclusions, technical notes, or model understanding documents for StandardML - Codex.
---

# Scientific Reference Synthesizer

Turn repository reference material into implementation-facing analysis without
losing source boundaries.

## Use This Skill For

- reading papers and engineering references from `reference/`;
- comparing repository summaries against source material;
- extracting implementation implications for TE modeling;
- drafting concise evidence-grounded technical conclusions.

## Do Not Use This Skill For

- generic internet literature reviews when repository references are enough;
- writing final model code directly;
- broad product or market research.

## Workflow

1. Read the relevant files in `reference/`.
2. Read matching summaries in `doc/reference_summaries/` when they exist.
3. Separate:
   implemented facts, reference-backed claims, and open questions.
4. Translate the source material into repository consequences:
   model choice, training implications, deployability, or documentation needs.

## Repository Priorities

- Keep rotational transmission error as the central modeling target.
- Preserve the distinction between analytical modeling and ML-based
  compensation.
- Keep operating variables explicit when the reference material depends on
  them.
- When a source does not prove a claim, label the result as inference rather
  than fact.

## Output Pattern

Prefer this structure:

1. What the reference actually says.
2. Why it matters for this repository.
3. What is already implemented here.
4. What remains missing, risky, or uncertain.

## File Targets To Read First

- `reference/`
- `doc/reference_summaries/`
- `doc/reference_codes/`
- relevant `doc/technical/` notes
