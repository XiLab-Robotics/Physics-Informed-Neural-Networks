# Local Machine Timestamp Rule For Technical Docs

## Overview

This document introduces a stricter timestamp-source rule for new technical project documents.

The repository already requires every implementation task to begin with a timestamped technical note. This update makes the timestamp source explicit:

- the timestamp must be read from the real current local machine date and time;
- the timestamp must be used exactly in the filename;
- the timestamp must not be inferred or estimated from conversation context.

## Technical Approach

The rule should be added to the two repository surfaces that govern execution discipline:

- `AGENTS.md`
- `README.md`

The wording should stay short and operational so future work starts by querying the local machine clock before naming a new technical document.

## Involved Components

- `AGENTS.md`
  Repository execution rules consumed during implementation work.
- `README.md`
  Main project document that mirrors the workflow rules.
- `doc/technical/2026-03/2026-03-24/2026-03-24-16-00-12_local_machine_timestamp_rule_for_technical_docs.md`
  This technical note.

## Implementation Steps

1. Create this technical note using a timestamp read from the real local machine clock.
2. Add the timestamp-source rule to `AGENTS.md`.
3. Add the same rule to `README.md`.
4. Register this technical note in `README.md`.
