# Video Guides Markdown Strict Cleanup And Lint Alignment

## Overview

The canonical video-guide reports and transcripts under
`doc/reference_codes/video_guides/` still contain Markdown patterns that are
flagged by stricter editor-integrated Markdown linting, even though the current
repository lint pass does not surface them all.

The user requirement for this task is stricter than the currently observed
repository baseline: the video-guide Markdown files should not emit residual
warnings such as:

- `MD060/table-column-style`
- `MD035/hr-style`
- `MD009/no-trailing-spaces`
- `MD033/no-inline-html`
- `MD032/blanks-around-lists`
- `MD004/ul-style`
- `MD034/no-bare-urls`

This task will clean the canonical video-guide Markdown set so it is compatible
with stricter editor linting and aligns better with the repository zero-warning
policy.

## Technical Approach

The cleanup will focus on the Git-tracked canonical video-guide Markdown files
under `doc/reference_codes/video_guides/`, including the directory README and
the per-video transcript/report pairs.

The fixes will be mechanical and minimal:

- remove trailing spaces from headings and prose lines;
- normalize horizontal rules to `---`;
- normalize list spacing and unordered-list style;
- normalize table formatting where stricter linters expect spacing around pipe
  separators;
- replace or reformulate any inline HTML or bare URL patterns if present;
- preserve the source-reference provenance blocks and the current document
  meaning.

If the root cause also involves a mismatch between repository lint policy and
the stricter editor behavior, the task may additionally update the local
documentation of the Markdown tooling so the stricter expectation is explicit.

## Involved Components

- `doc/reference_codes/video_guides/README.md`
- `doc/reference_codes/video_guides/*/*_report.md`
- `doc/reference_codes/video_guides/*/*_transcript.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/scripts/tooling/markdown/run_markdownlint.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Audit the canonical video-guide Markdown files for the stricter warning
   patterns reported by the editor.
2. Normalize the Markdown formatting of the per-video reports and transcripts
   without changing their technical meaning.
3. Update the canonical video-guide README if needed so its tables, lists, and
   provenance blocks follow the same stricter style.
4. Re-run repository Markdown checks on the touched scope and confirm that the
   cleaned files end with a normal single final newline.
5. If a tool-policy mismatch remains relevant, document the stricter lint
   expectation in the Markdown tooling notes or usage guide.
