# Rich Training API Demo

## Overview

This page documents a standalone proof-of-concept Python module created only for
the documentation experiment.

The source module is:

- `poc_sources/rich_training_api_demo.py`

Its purpose is to show how the generated API pages change when the source code
contains structured Google-style docstrings with:

- detailed descriptions;
- explicit `Args`;
- explicit `Returns`;
- explicit `Raises`;
- `Notes`;
- `Examples`.

## Why This Page Matters

The current repository modules mostly use short title-style docstrings. Those
fit the local coding style, but they do not contain enough semantic structure to
produce API pages similar to the `ur_rtde` reference the user provided.

This demo page isolates the documentation question from the implementation
question:

- if this page renders clearly, the repository can keep `MkDocs` and improve
  source docstrings over time;
- if this page is still not good enough, the next comparison should be a direct
  `MkDocs` versus `Sphinx` API-layout test.

## Generated Reference

::: poc_sources.rich_training_api_demo
