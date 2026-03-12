# Commit Requires Final User Approval Rule

## Overview

The user requested a new permanent workflow rule:

- complete the requested modifications first;
- report that the work is finished;
- explicitly ask for approval before creating the Git commit;
- do not create the commit until the user approves it.

This changes the current repository workflow because the current rules require creating a Git commit immediately after the modifications are completed.

The new rule should replace that final step with an approval gate just before the commit.

## Technical Approach

This is a repository-process update, not a feature implementation.

The rule should be made explicit in the permanent workflow instructions so future tasks follow the new sequence consistently.

The main places to update are:

- `AGENTS.md`
- `README.md`
- `doc/README.md`

The updated workflow should be:

1. create the technical document first;
2. create any required preliminary report if the task is training-related;
3. wait for user approval before implementation;
4. complete the approved modifications;
5. complete the required checks, exports, reports, and documentation updates;
6. tell the user the work is finished and ask for approval to commit;
7. create the Git commit only after explicit user approval.

## Involved Components

- `AGENTS.md`
  Persistent repository instructions that define the mandatory execution sequence.
- `README.md`
  Main project document that mirrors the critical workflow rules.
- `doc/README.md`
  Internal documentation index that should reference this technical document.

## Implementation Steps

1. Create this technical document and register it in the project indexes.
2. After user approval, update the permanent repository workflow rules so commits require a final explicit user approval.
3. Adjust the documented execution sequence in `AGENTS.md` and `README.md`.
4. Keep `doc/README.md` aligned with the new rule set.
5. Commit the approved rule update only after the new final-approval workflow itself has been followed.
