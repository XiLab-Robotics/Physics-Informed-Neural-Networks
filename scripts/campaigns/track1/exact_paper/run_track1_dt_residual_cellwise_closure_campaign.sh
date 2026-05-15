#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${SCRIPT_DIRECTORY}/run_exact_paper_campaign_from_powershell_metadata.sh" \
    --source-powershell-script "${SCRIPT_DIRECTORY}/run_track1_dt_residual_cellwise_closure_campaign.ps1" \
    "$@"
