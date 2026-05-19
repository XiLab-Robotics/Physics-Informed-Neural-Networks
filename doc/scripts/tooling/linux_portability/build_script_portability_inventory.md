# Script Portability Inventory Tool

## Overview

`scripts/tooling/linux_portability/build_script_portability_inventory.py`
builds the repository-wide script inventory used to track Linux portability
coverage.

The inventory scans every `.py`, `.ps1`, and `.sh` file under `scripts/` and
classifies each script by domain, script kind, platform-flag coverage, Bash
equivalent coverage, Windows-specific markers, and current portability status.

## Usage

Windows-formatted output paths:

```powershell
conda run -n pinns_env python scripts/tooling/linux_portability/build_script_portability_inventory.py --windows
```

Linux-formatted output paths:

```bash
conda run -n pinns_env python scripts/tooling/linux_portability/build_script_portability_inventory.py --linux
```

The default output bundle is written under:

- `doc/reports/analysis/utilities/linux_script_portability/[YYYY-MM-DD]/`

## Outputs

- `script_portability_inventory.yaml`
- `script_portability_inventory.md`

The Markdown report is the human-readable checklist. The YAML file is the
machine-readable source for follow-up audits.
