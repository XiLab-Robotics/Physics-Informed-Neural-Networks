#!/bin/bash -l
set -euo pipefail

if [[ -n "${SLURM_SUBMIT_DIR:-}" && -d "${SLURM_SUBMIT_DIR}/scripts" ]]; then
  PROJECT_ROOT="${SLURM_SUBMIT_DIR}"
else
  PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
fi
cd "${PROJECT_ROOT}"

CAMPAIGN_MANIFEST_PATH="${1:-config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__tree__simplified_setpoints/campaign.yaml}"
CONDA_ENVIRONMENT_NAME="${PINNS_CONDA_ENVIRONMENT_NAME:-pinns_env}"

module load cuda
module load Anaconda3

CONDA_BASE="$(conda info --base)"
source "${CONDA_BASE}/etc/profile.d/conda.sh"
conda activate "${CONDA_ENVIRONMENT_NAME}"

export LD_LIBRARY_PATH="${CONDA_PREFIX}/lib:${LD_LIBRARY_PATH:-}"
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
export NUMEXPR_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

echo "[INFO] Host: $(hostname)"
echo "[INFO] SLURM job: ${SLURM_JOB_ID:-none}"
echo "[INFO] Manifest: ${CAMPAIGN_MANIFEST_PATH}"
echo "[INFO] Python: $(command -v python)"
python -V
nvidia-smi

python -B scripts/campaigns/cross_wave/validate_dataset_input_mode_retraining_campaign.py \
  --campaign-manifest-path "${CAMPAIGN_MANIFEST_PATH}"

FIRST_CONFIG_PATH="$(python - <<'PY' "${CAMPAIGN_MANIFEST_PATH}"
from pathlib import Path
import sys
import yaml
manifest = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
print(manifest["queue_config_path_list"][0])
PY
)"

python -B scripts/training/run_training_smoke_test.py \
  --config-path "${FIRST_CONFIG_PATH}" \
  --output-suffix "aries_fast_smoke" \
  --fast-dev-run-batches 1

echo "[DONE] Aries dataset/input-mode smoke completed"
