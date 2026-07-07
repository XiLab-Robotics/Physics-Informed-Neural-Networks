#!/bin/bash -l
#SBATCH --job-name=pinns_input_mode
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=02:00:00
#SBATCH --mem=40g
#SBATCH --partition=ice4hpc
#SBATCH --account=xilab
#SBATCH --qos=gpus
#SBATCH --gpus=1g.20gb:1
#SBATCH --output=output/slurm/%x_%j.out
#SBATCH --error=output/slurm/%x_%j.err

set -euo pipefail

if [[ -n "${SLURM_SUBMIT_DIR:-}" && -d "${SLURM_SUBMIT_DIR}/scripts" ]]; then
  PROJECT_ROOT="${SLURM_SUBMIT_DIR}"
else
  PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
fi
cd "${PROJECT_ROOT}"

CAMPAIGN_MANIFEST_PATH="${1:?Usage: sbatch scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.sbatch <campaign_manifest_path>}"
CONDA_ENVIRONMENT_NAME="${PINNS_CONDA_ENVIRONMENT_NAME:-pinns_env}"

module load cuda
module load Anaconda3

CONDA_BASE="$(conda info --base)"
source "${CONDA_BASE}/etc/profile.d/conda.sh"
conda activate "${CONDA_ENVIRONMENT_NAME}"

mkdir -p output/slurm
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

readarray -t CAMPAIGN_ARGUMENTS < <(python - <<'PY' "${CAMPAIGN_MANIFEST_PATH}"
from pathlib import Path
import sys
import yaml
manifest = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
for path in manifest["queue_config_path_list"]:
    print(path)
print("--queue-root")
print(manifest["queue_root"])
print("--campaign-name")
print(manifest["campaign_name"])
print("--planning-report-path")
print(manifest["planning_report_path"])
print("--dataset")
print(manifest["dataset_name"])
print("--input-mode")
print(manifest["input_mode"])
print("--stop-on-error")
PY
)

python -B scripts/training/run_training_campaign.py "${CAMPAIGN_ARGUMENTS[@]}"
