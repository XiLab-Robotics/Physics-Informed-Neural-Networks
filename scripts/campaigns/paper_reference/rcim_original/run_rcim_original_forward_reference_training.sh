#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ARGUMENT_LIST=(--branch Forward --stage Original)
while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip-paper-eval)
            ARGUMENT_LIST+=(--no-eval)
            shift
            ;;
        --skip-paper-export)
            ARGUMENT_LIST+=(--no-export)
            shift
            ;;
        --print-only)
            ARGUMENT_LIST+=(--dry-run)
            shift
            ;;
        *)
            ARGUMENT_LIST+=("$1")
            shift
            ;;
    esac
done

bash "${SCRIPT_DIRECTORY}/run_rcim_original_reference_training.sh" "${ARGUMENT_LIST[@]}"
