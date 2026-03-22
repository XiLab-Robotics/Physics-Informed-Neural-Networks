# Project Usage Guide

## Overview

This page is a proof-of-concept mirror of the repository usage documentation.

The canonical source currently remains:

- `doc/guide/project_usage_guide.md`

This POC page intentionally keeps only a compact subset so the documentation site can be evaluated without migrating the full guide tree yet.

## Current Runnable Areas

The repository currently exposes workflows for:

- dataset processing and visualization;
- feedforward neural-network training;
- structured Wave 1 baselines;
- tree-based baselines;
- smoke-test and validation utilities;
- report PDF export and PDF validation.

## Relevant Repository Paths

Representative paths for the current project workflow are:

- `scripts/datasets/`
- `scripts/models/`
- `scripts/training/`
- `scripts/reports/`
- `config/`
- `doc/guide/`
- `doc/reports/`

## Why This Page Exists In The POC

This mirrored page validates that a future documentation portal can host narrative documentation next to generated API reference pages in a coherent navigation tree.

## Future Migration Direction

If the POC is approved later, the synchronized integration phase can decide whether:

- the canonical guide files should be served directly through MkDocs;
- mirrored pages should be generated automatically;
- only selected guide families should enter the portal first.
