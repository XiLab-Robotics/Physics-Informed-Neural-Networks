# Documentation Proof Of Concept

## Overview

This isolated proof of concept tests whether `MkDocs + Material + mkdocstrings` is a good long-term documentation platform for this repository.

The scope is intentionally small but now includes an explicit quality comparison:

- one narrative guide page;
- current generated API pages from sparse-docstring repository modules;
- richer generated API pages from isolated mirrored modules with Google-style docstrings;
- one minimal navigation structure.

## Why This Stack

The repository is documentation-heavy and already contains a large Markdown knowledge base.

This stack is being tested because it can unify:

- guide-style documentation;
- generated Python API reference;
- future automation through one rebuild command.

## Current Proof-Of-Concept Pages

- `Usage Guide`
  A representative guide page derived from the current repository usage documentation.
- `FeedForward Network Module`
  A generated API reference page for `scripts/models/feedforward_network.py`.
- `FeedForward Training Script`
  A generated API reference page for `scripts/training/train_feedforward_network.py`.
- `Documented FeedForward Network Mirror`
  A generated API reference page for the isolated mirrored model module with rich docstrings.
- `Documented FeedForward Training Mirror`
  A generated API reference page for the isolated mirrored training workflow module with rich docstrings.
- `Rich Training API Demo`
  A smaller standalone module used to prove that structured docstrings materially improve API pages.

## What This POC Is Not Yet

This is not yet the canonical repository documentation system.

It is an isolated experiment intended to validate:

- output quality;
- navigation quality;
- Python API extraction quality;
- maintenance cost.

## Current Evaluation Goal

This POC is no longer just testing whether MkDocs can build.

It is now testing whether MkDocs can get close enough to the visual and structural clarity of the user's `ur_rtde` reference when the source modules are documented properly.
