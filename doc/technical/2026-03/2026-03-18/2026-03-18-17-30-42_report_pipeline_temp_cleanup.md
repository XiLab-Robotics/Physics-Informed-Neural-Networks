# Report Pipeline Temp Cleanup

## Overview

This document defines the immediate cleanup pass for temporary report-generation artifacts that were created during the recent diagram, PDF-export, and PDF-validation work.

At the moment, the repository root still contains temporary directories produced by intermediate validation workflows:

- `.tmp_pdfenv/`
- `.tmp_pydeps/`
- `.temp/`

Now that the standardized report pipeline has been introduced, these temporary directories should be evaluated against the new intended policy:

- keep only the persistent tooling environment when explicitly needed;
- keep only the standardized temporary root when it still contains useful validation evidence;
- remove ad hoc or obsolete temporary environments that are no longer part of the preferred workflow.

## Technical Approach

The cleanup should preserve only what still has a clear operational role.

### 1. Remove Legacy Temporary Environments

The following directories are legacy temporary environments from ad hoc validation steps and should be removed:

- `.tmp_pdfenv/`
- `.tmp_pydeps/`

They are not part of the intended steady-state workflow anymore.

### 2. Evaluate The Current `.temp/` Root

The `.temp/` root now serves two different roles:

- standardized report-pipeline temporary artifacts under `.temp/report_pipeline/`;
- older ad hoc validation folders from before the standardized runner existed.

This cleanup pass should:

- keep the standardized root if it still contains recent validation evidence worth preserving temporarily;
- remove obsolete ad hoc validation leftovers that are no longer needed;
- avoid deleting current useful validation artifacts unless the user wants a fully clean rerun state.

### 3. Preserve Only The Intended Persistent Tooling Location

The long-term preferred persistent tooling location is:

- `.tools/report_pdf_env/`

If this environment does not exist yet, that is acceptable. It should not be created during cleanup.

The cleanup goal is simply to ensure that:

- legacy temp environments are gone;
- the repository no longer relies on those temp environments;
- future runs can use either the active project environment or the standardized `.tools/report_pdf_env/`.

## Involved Components

This cleanup will affect only local temporary directories in the repository root:

- `.tmp_pdfenv/`
- `.tmp_pydeps/`
- selected obsolete content under `.temp/`

No implementation code, report content, or committed output artifacts should be changed by this cleanup.

## Implementation Steps

1. Remove `.tmp_pdfenv/`.
2. Remove `.tmp_pydeps/`.
3. Inspect `.temp/` and keep only the standardized report-pipeline content that still has current validation value.
4. Remove obsolete ad hoc validation leftovers under `.temp/`.
5. Confirm the remaining local temporary layout after cleanup.
