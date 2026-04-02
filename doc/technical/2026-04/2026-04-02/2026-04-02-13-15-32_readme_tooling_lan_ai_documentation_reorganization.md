# README Tooling LAN AI Documentation Reorganization

## Overview

This scope addresses four related repository-organization concerns that have
become visible after the recent TwinCAT/TestRig LAN-AI pipeline work.

First, the root `README.md` is accumulating too many implementation artifacts,
technical-note registrations, and workflow-specific details. That weakens its
role as a concise GitHub-facing landing page.

Second, `scripts/tooling/` is becoming crowded with mixed-purpose utilities:
video analysis, LAN-AI runtime helpers, Markdown utilities, and isolated-mode
support all currently live in one flat folder.

Third, `requirements-lan-ai-node.txt` works from the repository root, but its
placement should be evaluated against repository clarity and long-term
maintainability.

Fourth, the LAN-AI workflow is documented across multiple files and is probably
complete enough operationally, but it should be reviewed for consolidation and
clearer entry points.

## Technical Approach

The reorganization should optimize for three things:

1. a clean public repository entry point;
2. a more discoverable tooling layout;
3. a single, explicit documentation path for the LAN-AI workflow.

The proposed direction is:

- trim the root `README.md` back to GitHub-facing essentials and move artifact
  registry-style details into more appropriate documentation entry points;
- reorganize `scripts/tooling/` into topic-based subfolders, with the strongest
  candidate split being:
  - `scripts/tooling/video_guides/`
  - `scripts/tooling/lan_ai/`
  - `scripts/tooling/markdown/`
  - `scripts/tooling/session/`
- move `requirements-lan-ai-node.txt` closer to the LAN-AI tooling, likely
  under `scripts/tooling/lan_ai/` or a nearby LAN-AI-focused location, unless
  a root-level environment-file policy clearly outweighs the locality benefit;
- consolidate the LAN-AI documentation so that setup, runtime topology,
  launcher usage, troubleshooting, and artifact provenance are linked from one
  clear entry flow instead of relying on the reader to discover the chain
  indirectly.

This task is documentation and repository-structure work only. No subagent is
planned or needed.

## Involved Components

- `README.md`
  Must be restored to a concise landing-page role.
- `doc/README.md`
  May become a stronger index for internal technical navigation.
- `doc/guide/project_usage_guide.md`
  User-facing workflow reference that should remain detailed.
- `doc/scripts/tooling/lan_ai_node_server.md`
  Setup and troubleshooting guide for the remote LAN node.
- `doc/scripts/tooling/remote_high_quality_video_pipeline.md`
  Canonical runtime/process note for the strong remote path.
- `scripts/tooling/`
  Flat tooling directory that should be reviewed for topic-based subdivision.
- `requirements-lan-ai-node.txt`
  Candidate for relocation closer to the LAN-AI scripts.

## Implementation Steps

1. Define a concise target role for the root `README.md` and move excess
   technical-registry detail out of it.
2. Propose and implement a topic-based `scripts/tooling/` subfolder layout.
3. Relocate `requirements-lan-ai-node.txt` if the final structure benefits from
   moving it closer to the LAN-AI tooling.
4. Update all script references, documentation links, and usage examples to the
   new tooling paths.
5. Review the LAN-AI documentation chain and tighten the entry points so setup,
   runtime use, troubleshooting, and rerun process are easy to discover.
6. Run scoped Markdown checks on the touched Markdown files before closing the
   task.
