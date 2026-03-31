# SSH Key-Based Access Extension For LAN AI Node Guide

## Overview

This document defines the approved scope for extending the LAN AI node setup
guide with the Windows-to-Windows SSH key-based access procedure that was
actually validated between the current workstation and the remote workstation.

The goal is to make `doc/scripts/tooling/lan_ai_node_server.md` reflect the
real working SSH setup instead of only the password-based baseline.

## Technical Approach

The guide extension will add the repository-owned, validated SSH path for:

- generating or selecting a local SSH key on the current workstation;
- installing the public key on the remote Windows workstation;
- handling the Windows OpenSSH administrator-account case through
  `C:\ProgramData\ssh\administrators_authorized_keys`;
- setting the required ACLs;
- restarting `sshd` from an elevated PowerShell prompt;
- creating a local SSH host alias in `C:\Users\<user>\.ssh\config`;
- validating interactive and command-based remote access through the alias.

The documentation should explicitly record the Windows-specific caveat that an
administrator account may not use the profile-local `authorized_keys` path in
practice and instead may require the shared
`administrators_authorized_keys` file.

No subagent is planned for this task.

## Involved Components

- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md` if the LAN workflow section should mention
  the new SSH alias path
- `README.md` for the required technical-document registration only

## Implementation Steps

1. Extend the LAN AI node setup guide with the validated SSH key-based login
   flow.
2. Document the administrator-account caveat and the
   `administrators_authorized_keys` fix.
3. Add the local `~/.ssh/config` alias example used to simplify the workflow.
4. Update any LAN workflow usage note that benefits from referencing the SSH
   alias.
5. Run scoped Markdown warning checks on all touched Markdown files and confirm
   normal final-newline state before closing the task.
