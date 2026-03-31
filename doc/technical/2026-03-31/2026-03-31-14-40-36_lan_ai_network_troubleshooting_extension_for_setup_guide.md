# LAN AI Network Troubleshooting Extension For Setup Guide

## Overview

This document defines the approved scope for extending the LAN AI node setup
guide with the Windows-to-Windows network troubleshooting steps that were
validated during the first real remote connection attempt.

The goal is to capture the concrete recovery path for cases where:

- SSH is not reachable even though `sshd` is running;
- custom service ports such as `1234` and `8765` do not respond from the
  current workstation;
- the remote workstation services are listening locally but are still blocked
  by the Windows Firewall profile or by missing inbound rules.

## Technical Approach

The guide extension will document a structured troubleshooting sequence across
both machines:

- on the remote workstation:
  - `ipconfig`
  - `Get-Service sshd`
  - `netstat -ano | findstr :22`
  - `Test-NetConnection` on local and interface-bound ports
  - Windows Firewall profile inspection
  - inbound-rule creation for `22`, `1234`, and `8765`
- on the current workstation:
  - `Test-NetConnection`
  - `curl.exe` health checks
  - interpretation of SSH-ok but custom-port-fail cases

The guide should explicitly record the validated findings from this setup:

- the remote workstation was reachable by IP;
- SSH initially failed because the network profile and firewall scope were not
  aligned;
- custom ports `1234` and `8765` required explicit inbound firewall rules
  before the workstation-to-workstation LAN path became usable.

No subagent is planned for this task.

## Involved Components

- `doc/scripts/tooling/lan_ai_node_server.md`
- `doc/guide/project_usage_guide.md` if the LAN workflow section should mention
  the troubleshooting sequence
- `README.md` for technical-document registration only

## Implementation Steps

1. Extend the LAN AI node guide with a dedicated troubleshooting section for
   SSH, firewall profiles, and custom port exposure.
2. Add the validated diagnostic commands for both the current workstation and
   the remote workstation.
3. Add the explicit firewall-rule commands for `1234` and `8765`.
4. Update any LAN workflow note that benefits from referencing the new
   troubleshooting section.
5. Run scoped Markdown warning checks on all touched Markdown files and confirm
   normal final-newline state before closing the task.
