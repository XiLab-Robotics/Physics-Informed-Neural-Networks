# Video-Guide Script Docstring And Comment Retrofit

## Overview

This document defines a targeted documentation-quality retrofit for the most
recent TwinCAT/TestRig video-guide tooling scripts.

The immediate trigger is the current mismatch between:

- the repository-owned Sphinx configuration under `site/conf.py`, which enables
  `sphinx.ext.napoleon` with `napoleon_google_docstring = True`;
- the previously approved documentation direction recorded in
  `doc/technical/2026-03/2026-03-22/2026-03-22-12-05-00_documentation_direction_docstring_standard_and_dual_poc.md`,
  which established Google-style docstrings as the official API-documentation
  direction;
- the current implementation state of the recent `scripts/tooling/video_guides/`
  Python modules, which still rely on very short placeholder docstrings and
  insufficient internal section comments for the complexity of their workflow.

This task is intentionally limited to documentation quality and code-readability
retrofit. It does not change the functional runtime contract of the
video-guide pipeline.

## Technical Approach

The implementation should retrofit the following modules:

- `scripts/tooling/video_guides/analyze_video_guides.py`
- `scripts/tooling/video_guides/extract_video_guide_knowledge.py`
- `scripts/tooling/video_guides/generate_video_guide_reports.py`

The retrofit should apply these rules:

1. keep module behavior unchanged unless a tiny clarity-only correction is
   required to support the documentation rewrite safely;
2. replace placeholder one-line docstrings on public helpers, dataclasses, and
   workflow functions with Google-style docstrings that Sphinx `napoleon` can
   render cleanly;
3. add `Args`, `Returns`, `Raises`, `Attributes`, and `Notes` sections only
   where they materially improve API clarity instead of mechanically expanding
   every trivial helper;
4. increase internal section-comment coverage inside non-trivial functions so
   the stage flow remains visually scannable while reading the implementation;
5. keep comments short, operational, and aligned with the repository coding
   style instead of replacing internal readability with long prose comments;
6. preserve the existing domain vocabulary around TwinCAT, TestRig, OCR,
   transcript cleanup, snapshot selection, and report synthesis;
7. verify that the retrofitted modules remain compatible with the current
   Sphinx autodoc plus napoleon configuration.

The documentation baseline for this work is the combination of:

- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`
- `site/conf.py`

No subagent is planned for this task. The scope is narrow, local to three
Python files, and does not justify delegated execution. If a later extension
requests broader repository-wide API-documentation migration, any future
subagent proposal must still be declared separately and approved at runtime.

## Involved Components

- `scripts/tooling/video_guides/analyze_video_guides.py`
- `scripts/tooling/video_guides/extract_video_guide_knowledge.py`
- `scripts/tooling/video_guides/generate_video_guide_reports.py`
- `site/conf.py`
- `doc/reference_summaries/06_Programming_Style_Guide.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`
- `doc/README.md`

## Implementation Steps

1. Re-read the current video-guide tooling modules and identify the public
   entry points, data containers, and non-trivial helpers that need richer API
   documentation.
2. Rewrite the relevant module, class, dataclass, and function docstrings in
   Google style so they render cleanly through the current Sphinx `napoleon`
   setup.
3. Add missing internal section comments in the longer workflow functions,
   especially where transcript extraction, cleanup, OCR, snapshot selection,
   and report synthesis move through multiple distinct stages.
4. Keep the code behavior stable and avoid unrelated refactors during the
   documentation retrofit.
5. Run a focused verification pass on the touched Python modules, including at
   least syntax validation and a Sphinx-oriented sanity check if the local
   documentation path can be exercised cheaply.
6. Run Markdown warning checks on the touched Markdown scope created or updated
   by this task, including this technical document and the updated `doc/README.md`
   entry.
7. Stop after implementation and verification, report the outcome, and wait for
   explicit approval before any Git commit.
