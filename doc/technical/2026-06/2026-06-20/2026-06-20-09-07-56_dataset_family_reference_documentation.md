# Dataset Family Reference Documentation

## Overview

Create canonical reference documentation for the three dataset surfaces under
`data/`: the raw `original_dataset`, the established `simplified_dataset`, and
the direction-separated `polished_dataset`.

The work will verify the requested provenance, directory structure, filename
convention, CSV schema, physical meaning, units, and generation procedure
against the repository contents rather than documenting assumptions. The
analysis will explicitly distinguish measured quantities from derived
quantities.

## Technical Approach

Inspect the raw source hierarchy, the polished export generator, representative
and full-population CSV metadata, and the existing dataset loader and reference
summaries. Use repository-owned validation scripts where applicable and
perform a deterministic dataset audit covering file counts, headers, numeric
parsing, row counts, operating-condition filename consistency, direction
separation, value ranges, and correspondence between raw source conditions and
polished outputs.

Record confirmed behavior and any discrepancies in a canonical dataset
reference document. Keep the existing polished-export README focused on the
generator while linking it to the broader reference. Register the new
documentation from `doc/README.md` and update user-facing dataset guidance only
where the verified findings affect normal repository use.

## Involved Components

- `data/original_dataset/`
- `data/simplified_dataset/`
- `data/polished_dataset/`
- `data/polished_dataset/generate_polished_dataset.py`
- `data/polished_dataset/README_POLISHED_CSV.md`
- `scripts/datasets/transmission_error_dataset.py`
- `doc/reference_summaries/01_Dataset_Operations_Guide.md`
- `doc/reference_summaries/05_Data_Series_Explanation_Project_Summary.md`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`

## Implementation Steps

1. Inventory all three dataset trees and quantify files, directions, operating
   conditions, CSV schemas, row counts, and parse failures.
2. Trace every polished column to the raw source columns and generator
   equations, including units, gear-ratio scaling, zeroing, validity masks, and
   numerical differentiation.
3. Verify that polished `forward` and `backward` files are independently
   exported from their corresponding validity windows and that naming and
   folder metadata agree with file contents.
4. Compare raw operating-condition coverage with polished output coverage and
   document duplicate, ignored, skipped, or otherwise exceptional sources.
5. Create the canonical dataset-family reference document with future-use
   guidance, limitations, and reproducible loading examples.
6. Align the polished README, dataset operations summary, project usage guide,
   and documentation index with the verified reference where necessary.
7. Run the repository Markdown warning checks, confirm final-newline hygiene,
   and rebuild the Sphinx portal warning-free if the approved documentation
   changes its user-facing scope.
