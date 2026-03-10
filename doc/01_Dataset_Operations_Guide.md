# Dataset Operations Guide

## Source

- Reference PDF: `reference/Guida.pdf`

## Document Purpose

This document collects the operational guidance extracted from the quick project guide. It does not add new TE theory, but clarifies where the data comes from and which practical materials must be treated as primary references during development.

## Key Points

- The main dataset to use for the ML and TE project is the Transmission Error dataset that has already been extracted and validated.
- There is also a more complete raw dataset, useful when extended series, extra temperature conditions, or lower-level signal checks are required.
- The guide explicitly points to support material explaining the meaning of the data series and to practical documentation for TwinCAT and Machine Learning.
- The `reference/codes` subfolder must be treated as a structural reference for software organization, deployment choices, and implementation style.

## Implications For The Repository

- The correct workflow starts from already filtered and segmented data when the goal is model training or evaluation.
- Raw data should be used only when preprocessing, validation, or additional analysis must be reconstructed.
- The technical documentation of the project must stay connected to TwinCAT and to the reference codebases, not only to the offline ML model.

## Decisions To Preserve

- Prefer validated datasets for training and evaluation.
- Treat raw files as the source for audit, debugging, and preprocessing reconstruction.
- Keep theoretical documents separate from operational documents.

## Practical Use

- For training: start from already cleaned data series.
- For deployment: always keep dataset assumptions aligned with TwinCAT constraints.
- For documentation: always connect datasets, experimental procedure, and compensation code.
