# Full Report Pipeline Temp Reset

## Overview

This document defines a full reset of the remaining report-pipeline runtime temporary artifacts.

After the previous cleanup pass, the repository no longer contains the old ad hoc temporary environments. The only remaining temporary content is the standardized report runtime root:

- `.temp/report_pipeline/`

This root currently contains:

- empty or reusable runtime subfolders such as browser-profile and HTML-preview roots;
- one recent PDF-validation image set from the report-pipeline smoke test.

The user now requested a fully clean repository state with no remaining report-pipeline runtime temporary artifacts.

## Technical Approach

The cleanup goal is now stricter than the previous pass.

### 1. Remove The Entire Runtime Temp Root

The entire standardized runtime root should be removed:

- `.temp/report_pipeline/`

This is safe because:

- the validation images are only temporary evidence, not canonical project artifacts;
- the pipeline can recreate the directory structure deterministically on the next run;
- no committed outputs depend on the continued presence of these folders.

### 2. Remove The Parent `.temp/` Directory If It Becomes Empty

After removing `.temp/report_pipeline/`, the parent directory should also be removed if it no longer contains any remaining content.

The expected final local state is:

- no `.tmp_*` legacy directories;
- no `.temp/` runtime leftovers.

### 3. Preserve Only Real Project Artifacts

This cleanup must not touch:

- report Markdown files;
- generated PDF deliverables under `doc/reports/analysis/`;
- SVG assets under `doc/reports/analysis/assets/`;
- documentation;
- source code;
- future persistent tooling locations such as `.tools/report_pdf_env/` if they are created later.

## Involved Components

This cleanup affects only:

- `.temp/report_pipeline/`
- the parent `.temp/` directory if it becomes empty

No repository-authored content should be modified.

## Implementation Steps

1. Remove `.temp/report_pipeline/`.
2. Remove `.temp/` if it becomes empty.
3. Confirm that no temporary runtime directories remain in the repository root.
