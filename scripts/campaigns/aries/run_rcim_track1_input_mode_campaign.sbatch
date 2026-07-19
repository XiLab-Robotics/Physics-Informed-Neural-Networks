#!/bin/bash -l
#SBATCH --job-name=rcim_track1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --time=24:00:00
#SBATCH --mem=300g
#SBATCH --partition=high
#SBATCH --account=xilab
#SBATCH --qos=high
#SBATCH --output=output/slurm/%x_%j.out
#SBATCH --error=output/slurm/%x_%j.err

set -euo pipefail

if [[ -n "${SLURM_SUBMIT_DIR:-}" && -d "${SLURM_SUBMIT_DIR}/scripts" ]]; then
  PROJECT_ROOT="${SLURM_SUBMIT_DIR}"
else
  PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
fi
cd "${PROJECT_ROOT}"

CAMPAIGN_MANIFEST_PATH="${1:?Usage: sbatch scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.sbatch <campaign_manifest_path> [queue_config_path ...]}"
shift || true
CONDA_ENVIRONMENT_NAME="${PINNS_CONDA_ENVIRONMENT_NAME:-pinns_env}"
RUNNER_PATH="scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"
VALIDATOR_PATH="scripts/campaigns/cross_wave/validate_rcim_track1_input_mode_campaign.py"
OUTPUT_SUFFIX="${RCIM_TRACK1_OUTPUT_SUFFIX:-rcim_track1_polished_input_mode_campaign_validation}"

module load Anaconda3

CONDA_BASE="$(conda info --base)"
source "${CONDA_BASE}/etc/profile.d/conda.sh"
conda activate "${CONDA_ENVIRONMENT_NAME}"
PYTHON_EXECUTABLE="${CONDA_PREFIX}/bin/python"
if [[ ! -x "${PYTHON_EXECUTABLE}" ]]; then
  echo "[ERROR] Python executable not found in conda environment: ${PYTHON_EXECUTABLE}" >&2
  exit 1
fi

mkdir -p output/slurm
mkdir -p "${PROJECT_ROOT}/output/tmp/slurm_${SLURM_JOB_ID:-manual}"
export TMPDIR="${PROJECT_ROOT}/output/tmp/slurm_${SLURM_JOB_ID:-manual}"
export TMP="${TMPDIR}"
export TEMP="${TMPDIR}"
cleanup_job_temp_directory() {
  rm -rf "${TMPDIR}"
}
trap cleanup_job_temp_directory EXIT

export LD_LIBRARY_PATH="${CONDA_PREFIX}/lib:${LD_LIBRARY_PATH:-}"
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export BLIS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1

echo "[INFO] Host: $(hostname)"
echo "[INFO] SLURM job: ${SLURM_JOB_ID:-none}"
echo "[INFO] Manifest: ${CAMPAIGN_MANIFEST_PATH}"
echo "[INFO] Conda prefix: ${CONDA_PREFIX}"
echo "[INFO] Python: ${PYTHON_EXECUTABLE}"
echo "[INFO] TMPDIR: ${TMPDIR}"
echo "[INFO] CPUs: ${SLURM_CPUS_PER_TASK:-1}"
echo "[INFO] Memory request: ${SLURM_MEM_PER_NODE:-unknown}"
echo "[INFO] OMP_NUM_THREADS: ${OMP_NUM_THREADS}"
echo "[INFO] MKL_NUM_THREADS: ${MKL_NUM_THREADS}"
echo "[INFO] OPENBLAS_NUM_THREADS: ${OPENBLAS_NUM_THREADS}"
"${PYTHON_EXECUTABLE}" -V

"${PYTHON_EXECUTABLE}" -B "${VALIDATOR_PATH}" \
  --campaign-manifest-path "${CAMPAIGN_MANIFEST_PATH}"

readarray -t MANIFEST_QUEUE_CONFIG_PATH_LIST < <("${PYTHON_EXECUTABLE}" - <<'PY' "${CAMPAIGN_MANIFEST_PATH}"
from pathlib import Path
import sys
import yaml

manifest = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
for config_path in manifest["queue_config_path_list"]:
    print(config_path)
PY
)

if [[ "$#" -gt 0 ]]; then
  QUEUE_CONFIG_PATH_LIST=("$@")
else
  QUEUE_CONFIG_PATH_LIST=("${MANIFEST_QUEUE_CONFIG_PATH_LIST[@]}")
fi

for QUEUE_CONFIG_PATH in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
  QUEUE_CONFIG_ALLOWED=0
  for MANIFEST_QUEUE_CONFIG_PATH in "${MANIFEST_QUEUE_CONFIG_PATH_LIST[@]}"; do
    if [[ "${QUEUE_CONFIG_PATH}" == "${MANIFEST_QUEUE_CONFIG_PATH}" ]]; then
      QUEUE_CONFIG_ALLOWED=1
      break
    fi
  done
  if [[ "${QUEUE_CONFIG_ALLOWED}" -ne 1 ]]; then
    echo "[ERROR] Queue config is not listed in the validated campaign manifest: ${QUEUE_CONFIG_PATH}" >&2
    exit 1
  fi
done

for QUEUE_CONFIG_PATH in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
  echo "[STEP] RCIM Track1 input-mode surface run | ${QUEUE_CONFIG_PATH}"
  "${PYTHON_EXECUTABLE}" -B "${RUNNER_PATH}" \
    --config-path "${QUEUE_CONFIG_PATH}" \
    --output-suffix "${OUTPUT_SUFFIX}"
done

echo "[DONE] RCIM Track1 input-mode campaign completed | ${CAMPAIGN_MANIFEST_PATH}"
