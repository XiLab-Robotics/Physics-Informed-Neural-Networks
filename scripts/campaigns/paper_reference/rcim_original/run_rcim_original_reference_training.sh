#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

# shellcheck source=../../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

BRANCH="Forward"
STAGE="LoadBest"
CONDA_ENVIRONMENT_NAME="standard_ml_codex_env"
PYTHON_EXECUTABLE="python"
FAMILIES=""
TEST_SIZE="0.20"
OUTPUT_SUFFIX=""
DATAFRAME_PATH=""
BEST_PARAMETER_SUMMARY_PATH=""
RETUNE_GRID_SEARCH_VERBOSE="10"
RETUNE_CROSS_VALIDATE_VERBOSE="10"
NO_EVAL="0"
NO_EXPORT="0"
DRY_RUN="0"

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.sh [options]

Options:
  --branch Forward|Backward|Both
  --stage Original|Retune|Eval|Export|LoadBest
  --conda-environment-name NAME
  --python-executable COMMAND
  --families TEXT
  --test-size FLOAT
  --output-suffix TEXT
  --dataframe-path PATH
  --best-parameter-summary-path PATH
  --retune-grid-search-verbose INT
  --retune-cross-validate-verbose INT
  --no-eval
  --no-export
  --dry-run
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --branch)
            BRANCH="$2"
            shift 2
            ;;
        --stage)
            STAGE="$2"
            shift 2
            ;;
        --conda-environment-name)
            CONDA_ENVIRONMENT_NAME="$2"
            shift 2
            ;;
        --python-executable)
            PYTHON_EXECUTABLE="$2"
            shift 2
            ;;
        --families)
            FAMILIES="$2"
            shift 2
            ;;
        --test-size)
            TEST_SIZE="$2"
            shift 2
            ;;
        --output-suffix)
            OUTPUT_SUFFIX="$2"
            shift 2
            ;;
        --dataframe-path)
            DATAFRAME_PATH="$2"
            shift 2
            ;;
        --best-parameter-summary-path)
            BEST_PARAMETER_SUMMARY_PATH="$2"
            shift 2
            ;;
        --retune-grid-search-verbose)
            RETUNE_GRID_SEARCH_VERBOSE="$2"
            shift 2
            ;;
        --retune-cross-validate-verbose)
            RETUNE_CROSS_VALIDATE_VERBOSE="$2"
            shift 2
            ;;
        --no-eval)
            NO_EVAL="1"
            shift
            ;;
        --no-export)
            NO_EXPORT="1"
            shift
            ;;
        --dry-run|--print-only)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            print_usage
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            print_usage >&2
            exit 2
            ;;
    esac
done

case "${BRANCH}" in
    Forward|Backward|Both) ;;
    *) echo "[ERROR] Unsupported branch | ${BRANCH}" >&2; exit 2 ;;
esac
case "${STAGE}" in
    Original|Retune|Eval|Export|LoadBest) ;;
    *) echo "[ERROR] Unsupported stage | ${STAGE}" >&2; exit 2 ;;
esac

cd "${PROJECT_ROOT}"

CONDA_COMMAND="$(campaign_launcher_resolve_conda_command)"
TRAINING_SCRIPT="scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py"
REGISTRY_SCRIPT="scripts/campaigns/paper_reference/rcim_original/rcim_original_best_parameter_registry.py"
REGISTRY_PATH="output/registries/program/rcim_original_best_hyperparameters.yaml"

build_run_root() {
    local direction_label="$1"
    local stage_label="$2"
    local direction_prefix="bw"
    [[ "${direction_label}" == "forward" ]] && direction_prefix="fw"
    local run_label="${direction_prefix}_${stage_label}_bundle"
    local timestamp
    timestamp="$(date +"%Y-%m-%d-%H-%M-%S")"
    local run_instance_id="${timestamp}__${run_label}"
    if [[ -n "${OUTPUT_SUFFIX}" ]]; then
        run_instance_id="${run_instance_id}_${OUTPUT_SUFFIX}"
    fi
    echo "output/training_campaigns/rcim_original/${direction_label}/${run_instance_id}"
}

run_registry_helper() {
    local command_list=(
        "${CONDA_COMMAND}"
        run
        -n
        "${CONDA_ENVIRONMENT_NAME}"
        "${PYTHON_EXECUTABLE}"
        -B
        "${REGISTRY_SCRIPT}"
        --registry-path
        "${REGISTRY_PATH}"
        "$@"
    )
    echo "[INFO] Registry Command | $(campaign_launcher_join_command "${command_list[@]}")" >&2
    if [[ "${DRY_RUN}" == "1" ]]; then
        return 2
    fi
    "${command_list[@]}"
}

run_python_stage() {
    local mode_name="$1"
    local direction_label="$2"
    local stage_root="$3"
    local log_path="$4"
    local best_summary_path="${5:-}"
    local command_list=(
        "${CONDA_COMMAND}"
        run
        --no-capture-output
        -n
        "${CONDA_ENVIRONMENT_NAME}"
        "${PYTHON_EXECUTABLE}"
        -u
        -B
        "${TRAINING_SCRIPT}"
        --mode
        "${mode_name}"
        --direction
        "${direction_label}"
        --test-size
        "${TEST_SIZE}"
        --output-root
        "${stage_root}"
    )
    [[ -n "${FAMILIES}" ]] && command_list+=(--families "${FAMILIES}")
    [[ -n "${DATAFRAME_PATH}" ]] && command_list+=(--dataframe-path "${DATAFRAME_PATH}")
    [[ -n "${best_summary_path}" ]] && command_list+=(--best-parameter-summary-path "${best_summary_path}")
    if [[ "${mode_name}" == "retune" ]]; then
        command_list+=(--retune-grid-search-verbose "${RETUNE_GRID_SEARCH_VERBOSE}")
        command_list+=(--retune-cross-validate-verbose "${RETUNE_CROSS_VALIDATE_VERBOSE}")
    fi

    echo "[INFO] Stage Command | $(campaign_launcher_join_command "${command_list[@]}")"
    echo "[INFO] Combined Log | ${log_path}"
    if [[ "${DRY_RUN}" == "1" ]]; then
        echo "DRY_RUN_STAGE::${mode_name}::${direction_label}::${stage_root}"
        return 0
    fi
    mkdir -p "$(dirname "${log_path}")" "${stage_root}"
    "${command_list[@]}" 2>&1 | tee "${log_path}"
    return "${PIPESTATUS[0]}"
}

materialize_best_summary() {
    local direction_label="$1"
    local output_summary_path="$2"
    local argument_list=(
        materialize-summary
        --branch
        "${direction_label}"
        --output-summary-path
        "${output_summary_path}"
    )
    [[ -n "${FAMILIES}" ]] && argument_list+=(--families "${FAMILIES}")
    run_registry_helper "${argument_list[@]}"
}

update_registry_from_retune() {
    local direction_label="$1"
    local best_summary_path="$2"
    local cross_validation_summary_path="$3"
    run_registry_helper \
        update-from-retune \
        --branch "${direction_label}" \
        --best-parameter-summary-path "${best_summary_path}" \
        --cross-validation-summary-path "${cross_validation_summary_path}"
}

run_eval_export_chain() {
    local direction_label="$1"
    local campaign_root="$2"
    local logs_root="$3"
    local best_summary_path="${4:-}"
    if [[ "${NO_EVAL}" != "1" ]]; then
        run_python_stage paper_eval "${direction_label}" "${campaign_root}/eval" "${logs_root}/eval.combined.log" "${best_summary_path}"
    fi
    if [[ "${NO_EXPORT}" != "1" ]]; then
        run_python_stage paper_export "${direction_label}" "${campaign_root}/export" "${logs_root}/export.combined.log" "${best_summary_path}"
    fi
}

run_branch() {
    local direction_label="$1"
    local stage_label
    stage_label="$(echo "${STAGE}" | tr '[:upper:]' '[:lower:]')"
    local campaign_root
    campaign_root="$(build_run_root "${direction_label}" "${stage_label}")"
    local logs_root="${campaign_root}/logs"
    mkdir -p "${logs_root}"

    echo "[INFO] RCIM Original Reference Training"
    echo "[INFO] Branch | ${direction_label}"
    echo "[INFO] Stage | ${STAGE}"
    echo "[INFO] Campaign Root | ${campaign_root}"
    echo "[INFO] Logs Root | ${logs_root}"

    local best_summary_path="${BEST_PARAMETER_SUMMARY_PATH}"
    if [[ "${STAGE}" == "Original" ]]; then
        if [[ "${direction_label}" == "backward" ]]; then
            echo "[WARNING] Backward Original has no recovered paper tuned map; use Retune or LoadBest." >&2
            return 0
        fi
        run_eval_export_chain "${direction_label}" "${campaign_root}" "${logs_root}" ""
        return 0
    fi

    if [[ "${STAGE}" == "LoadBest" || "${STAGE}" == "Eval" || "${STAGE}" == "Export" ]]; then
        if [[ -z "${best_summary_path}" ]]; then
            best_summary_path="${campaign_root}/resolved_best_parameter_summary.csv"
            if ! materialize_best_summary "${direction_label}" "${best_summary_path}"; then
                if [[ "${STAGE}" == "LoadBest" ]]; then
                    echo "[WARNING] Missing stored best parameters; falling back to Retune."
                    STAGE="Retune"
                elif [[ "${direction_label}" == "forward" ]]; then
                    echo "[WARNING] Missing stored best parameters; using forward built-in map."
                    best_summary_path=""
                else
                    echo "[ERROR] Missing stored best parameters for ${direction_label} ${STAGE}." >&2
                    return 2
                fi
            fi
        fi
    fi

    if [[ "${STAGE}" == "Retune" ]]; then
        local retune_root="${campaign_root}/retune"
        run_python_stage retune "${direction_label}" "${retune_root}" "${logs_root}/retune.combined.log" ""
        best_summary_path="${retune_root}/output_prediction/summaryBestParameter+_3.8_allFreq.csv"
        local cross_validation_summary_path="${retune_root}/output_prediction/summaryCrossValidation+_3.8_allFreq.csv"
        if [[ "${DRY_RUN}" != "1" ]]; then
            update_registry_from_retune "${direction_label}" "${best_summary_path}" "${cross_validation_summary_path}"
        fi
        run_eval_export_chain "${direction_label}" "${campaign_root}" "${logs_root}" "${best_summary_path}"
    elif [[ "${STAGE}" == "Eval" ]]; then
        run_python_stage paper_eval "${direction_label}" "${campaign_root}/eval" "${logs_root}/eval.combined.log" "${best_summary_path}"
    elif [[ "${STAGE}" == "Export" ]]; then
        run_python_stage paper_export "${direction_label}" "${campaign_root}/export" "${logs_root}/export.combined.log" "${best_summary_path}"
    else
        run_eval_export_chain "${direction_label}" "${campaign_root}" "${logs_root}" "${best_summary_path}"
    fi

    echo "[DONE] RCIM Original Reference Training Completed | ${campaign_root}"
}

case "${BRANCH}" in
    Forward)
        run_branch forward
        ;;
    Backward)
        run_branch backward
        ;;
    Both)
        run_branch forward
        run_branch backward
        ;;
esac
