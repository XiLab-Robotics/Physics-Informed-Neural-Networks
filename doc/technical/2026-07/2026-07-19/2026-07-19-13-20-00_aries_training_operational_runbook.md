# Aries Training Operational Runbook

This note freezes the operational knowledge learned while running the
dataset/input-mode retraining program on the Unimore Aries cluster. It covers
the normal GPU training campaigns, the `rcim_track1` paper-bank pipeline, Slurm
resource choices, artifact promotion, cleanup, and Git/LFS handling.

## Scope

The active retraining plan remains:

- `doc/technical/2026-07/2026-07-07/2026-07-07-01-46-06_dataset_input_mode_retraining_campaigns.md`
- `doc/technical/2026-07/2026-07-13/2026-07-13-16-31-32_rcim_track1_polished_input_mode_retraining.md`

This runbook is not a replacement for those plans. It is the operational memory
for executing them without re-discovering the same cluster, pipeline, and
artifact-management details.

## Aries Baseline

Use the repository from the Aries scratch workspace, not from the Windows
machine:

```bash
cd /scratch1/dferrari/Physics-Informed-Neural-Networks
```

The standard environment used by the launchers is:

```bash
module load Anaconda3
conda activate "${PINNS_CONDA_ENVIRONMENT_NAME:-pinns_env}"
```

GPU jobs also load CUDA:

```bash
module load cuda
```

The current repository launchers create per-job temporary folders under
`output/tmp/slurm_<jobid>` and clean them through a shell `trap`. Keep this
pattern. It prevents large temporary files from accumulating in project output
folders after successful or failed jobs.

Useful Slurm commands:

```bash
squeue -u "$USER"
sacct -j <jobid>[,<jobid>...] --format=JobID,JobName%22,State,ExitCode,Elapsed,AllocCPUS -P
scancel <jobid>
```

Only cancel jobs after the decision is explicit. After cancellation or failure,
remove partial generated artifacts that cannot be accepted.

## Normal GPU Campaigns

Normal neural training campaigns are run through:

```bash
scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.sbatch
```

The documented launcher note is:

```bash
doc/scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.md
```

The launcher validates the manifest before training with:

```bash
scripts/campaigns/cross_wave/validate_dataset_input_mode_retraining_campaign.py
```

Then it calls:

```bash
python -B scripts/training/run_training_campaign.py ... --stop-on-error
```

Current Slurm resource baseline for normal GPU campaigns:

```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=02:00:00
#SBATCH --mem=40g
#SBATCH --partition=ice4hpc
#SBATCH --account=xilab
#SBATCH --qos=gpus
#SBATCH --gpus=1g.20gb:1
```

The launcher sets:

```bash
OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
NUMEXPR_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"
LD_LIBRARY_PATH="${CONDA_PREFIX}/lib:${LD_LIBRARY_PATH:-}"
```

Operational decisions learned during the GPU campaign work:

- Run one campaign at a time, then do closure, cleanup, and commit before the
  next campaign.
- Use an `srun` fast smoke before the first real `sbatch` on a new launcher,
  environment, or campaign shape.
- The accepted training policy after tuning is to use batch size `16` where the
  campaign/config supports it and validation passes.
- Monitor `nvidia-smi` and CPU use while tuning. If the GPU is underutilized,
  increase batch size and/or workers conservatively and record the exact config
  used.
- Do not mix resource tuning with unrecorded hyperparameter changes. Batch size
  and data-loader worker count are runtime throughput parameters; model/loss
  hyperparameter changes require a deliberate campaign decision.
- Do not run forward, backward, and global together on the same GPU allocation
  unless the allocation strategy explicitly assigns enough independent GPU
  resources. The accepted campaign rhythm is serial per campaign unless a
  specific parallel strategy is being tested.

Fast smoke pattern:

```bash
srun --nodes=1 --ntasks=1 --cpus-per-task=4 --time=00:20:00 --mem=20g \
  --partition=ice4hpc --account=xilab --qos=gpus --gpus=1g.20gb:1 --mpi=pmix \
  ./scripts/campaigns/aries/run_dataset_input_mode_retraining_smoke.sh \
  config/training/dataset_input_mode_retraining/campaigns/<campaign>/campaign.yaml
```

Batch pattern:

```bash
sbatch scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.sbatch \
  config/training/dataset_input_mode_retraining/campaigns/<campaign>/campaign.yaml
```

## Dataset Input Contracts

Every generated queue config, run manifest, export, report, and validation
artifact must preserve these labels:

- `dataset_name`
- `input_mode`
- `dataset_schema`
- `source_dataset_root`
- `expected_model_archive_root`
- `surface`

The three input modes are:

- `simplified_setpoints`: read from `data/simplified_dataset`; parse nominal
  speed, torque, and temperature from path/filename; keep `direction_flag`.
- `polished_setpoints`: read from `data/polished_dataset`; parse nominal speed,
  torque, and temperature from path/filename; use polished row-level `theta`
  and `theta_TE`; keep `direction_flag`.
- `polished_actual_values`: read from `data/polished_dataset`; use row-level
  `theta`, `theta_dot`, `tau_load`, and `T`; append `direction_flag`.

All three modes now use the same five-feature external input width. This is
intentional, because future validation/report scripts must be able to exercise
setpoint and actual-value archives through one shared input contract.

## RCIM Track 1 Pipeline

`rcim_track1` is a paper-bank reimplementation workflow, not a normal PyTorch
GPU training workflow. It trains and exports a scikit-learn style model bank
with ONNX conversion.

The Aries launcher is:

```bash
scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.sbatch
```

The launcher note is:

```bash
doc/scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.md
```

The runner is:

```bash
scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py
```

The manifest validator is:

```bash
scripts/campaigns/cross_wave/validate_rcim_track1_input_mode_campaign.py
```

Accepted resource baseline for RCIM on Aries:

```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --time=24:00:00
#SBATCH --mem=300g
#SBATCH --partition=high
#SBATCH --account=xilab
#SBATCH --qos=high
```

Do not request GPUs for the accepted RCIM paper-bank run path. The workflow is
CPU/RAM oriented, and the accepted setup uses CPU nodes (`cnode` through the
`high` partition), not `gnode01`.

The RCIM launcher intentionally pins numerical library thread pools to one
thread:

```bash
OMP_NUM_THREADS=1
MKL_NUM_THREADS=1
OPENBLAS_NUM_THREADS=1
BLIS_NUM_THREADS=1
NUMEXPR_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1
```

This avoids oversubscription when `GridSearchCV`/joblib is already parallelizing
candidate and fold evaluation.

## RCIM Surface Strategy

The RCIM surfaces are:

- `forward`
- `backward`
- `global`

For RCIM, surfaces can be launched as independent Slurm jobs when we want
parallel progress. This was necessary because the `global` surface is much
slower and can approach a 24-hour wall-time limit.

Do not assume that a single sequential manifest containing all three surfaces
will finish within one 24-hour job. Prefer one validated surface per Slurm job
when wall-time is uncertain.

Observed accepted polished actual-values timings on Aries:

- `136266 rcim_av_fw_opt`: `COMPLETED`, elapsed `13:04:30`
- `136267 rcim_av_bw_opt`: `COMPLETED`, elapsed `12:58:15`
- `136268 rcim_av_global_opt`: `COMPLETED`, elapsed `23:56:16`

An earlier high-partition global job timed out during LGBM and is not an
accepted result. Treat RCIM global as wall-time sensitive.

## RCIM LGBM Bottleneck

The main RCIM bottleneck is `LGBM` inside the exact paper model bank. Increasing
both outer joblib parallelism and inner LightGBM threading made the run slower
or less predictable because of oversubscription.

Accepted tuning direction:

- Keep model-bank outer parallelism in `GridSearchCV`.
- Keep LightGBM internal `n_jobs` at `1`.
- Keep numerical libraries pinned to one thread.
- Use enough Slurm CPUs for the outer joblib workers.
- Use enough memory headroom; `300g` was accepted and RAM was not the limiting
  issue in the successful campaign.

Accepted polished actual-values optimized setup:

- `grid_search_n_jobs: 16`
- `joblib_cpu_limit: 16`
- `grid_search_pre_dispatch: n_jobs`
- `threadpool_limit: 1`
- `estimator_runtime_parameters.LGBM.n_jobs: 1`
- Slurm allocation: `32` CPUs, `300g` memory

The repository contains a benchmark helper:

```bash
scripts/campaigns/aries/benchmark_rcim_track1_lgbm_scaling.py
```

It can test `grid_search_n_jobs`, `threadpool_limit`, `pre_dispatch`,
`lgbm_n_jobs`, and `device_type`. GPU LightGBM was considered during the Aries
investigation, but it is not the accepted default for the RCIM paper-bank
campaigns.

## RCIM Promotion

Promotion to the official archive is done with:

```bash
python -B scripts/campaigns/cross_wave/promote_rcim_track1_input_mode_exports.py \
  --input-mode <setpoints|actual_values> \
  --campaign-name <campaign-name> \
  --execution-environment "<where/how the accepted jobs ran>" \
  --replace
```

For the accepted polished actual-values closeout the command was:

```bash
python -B scripts/campaigns/cross_wave/promote_rcim_track1_input_mode_exports.py \
  --input-mode actual_values \
  --campaign-name dataset_input_mode_retraining__rcim_track1__polished_actual_values \
  --execution-environment "Aries cnode Slurm jobs 136266,136267,136268" \
  --replace
```

Official promoted RCIM polished archive roots:

```text
models/polished_dataset/paper_reference/rcim_track1/setpoints/
models/polished_dataset/paper_reference/rcim_track1/actual_values/
```

Each accepted RCIM surface contains the ten paper-bank model families:

```text
SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM, LGBM
```

Each surface has `19` targets per family, so a complete polished input-mode
archive contains:

- `570` ONNX files
- `570` Python pickle/model files
- `182` metadata files

The promotion script hard-checks dataset root, input mode, surface label,
five-feature input contract, and per-family export counts. Do not bypass these
checks.

## Slurm Log Lifecycle

Slurm stdout/stderr are terminal execution logs, not permanent model artifacts.
The accepted policy is:

1. Keep logs while the job is running and during verification.
2. Inspect them for failure signals such as `Traceback`, `OOM`, `TIMEOUT`,
   `FAILED`, `CANCELLED`, `Error`, and `Exception`.
3. Use `sacct` to confirm final state and exit code.
4. Record meaningful closeout information in a technical document.
5. Remove terminal Slurm logs and output noise before the closeout commit.
6. Keep `output/slurm/.gitkeep`.

Do not delete logs before extracting the evidence needed for closure. Do delete
them before committing once closure is complete.

## Git LFS Policy

Large RCIM validation bundles named `paper_family_model_bank.pkl` exceed normal
GitHub blob limits and must be tracked with Git LFS.

On Aries, `git-lfs` was installed in the conda environment:

```bash
conda install -y -n pinns_env -c conda-forge git-lfs
```

The binary path used during this work was:

```bash
/unimore_home/dferrari/.conda/envs/pinns_env/bin/git-lfs
```

Because this binary is not necessarily on the default non-interactive shell
`PATH`, the repository-local LFS filter was configured with absolute paths:

```bash
git config filter.lfs.clean '/unimore_home/dferrari/.conda/envs/pinns_env/bin/git-lfs clean -- %f'
git config filter.lfs.smudge '/unimore_home/dferrari/.conda/envs/pinns_env/bin/git-lfs smudge -- %f'
git config filter.lfs.process '/unimore_home/dferrari/.conda/envs/pinns_env/bin/git-lfs filter-process'
git config filter.lfs.required true
```

The local post-commit hook may still warn if it calls `git-lfs` by name and the
binary is not on `PATH`. The commit can still be valid when the clean/smudge
filters are configured with absolute paths and the staged files are verified as
LFS pointers.

Before committing large artifacts, verify that staged files are pointers:

```bash
git cat-file -s ":<path>"
git show ":<path>" | sed -n '1,3p'
```

Expected pointer size is small, around `134` bytes, and the content starts with:

```text
version https://git-lfs.github.com/spec/v1
```

Also check that no staged regular Git blob exceeds `100 MB`.

## Closeout Checklist

Before launching:

- Confirm the current repository, branch, and commit.
- Confirm the manifest path.
- Run the appropriate manifest validator.
- Confirm `dataset_name`, `input_mode`, `dataset_schema`,
  `source_dataset_root`, `expected_model_archive_root`, and `surface`.
- Confirm the launcher matches the workload: GPU launcher for normal neural
  campaigns, CPU/RAM launcher for RCIM paper-bank campaigns.

During execution:

- Monitor `squeue`.
- Use `sacct` for final state and elapsed time.
- For GPU campaigns, inspect `nvidia-smi` and CPU use when tuning throughput.
- For RCIM, watch LGBM progress and wall-time risk, especially on `global`.

After execution:

- Confirm all required surfaces completed with exit code `0:0`.
- Inspect logs for failure signals.
- Promote artifacts only through the campaign promotion scripts.
- Run package/count/schema validation after promotion.
- Record closeout evidence in `doc/technical/...`.
- Remove terminal Slurm logs and failed partial artifacts.
- Put large model bundles under Git LFS.
- Run `git status`, `git diff --check`, and a targeted artifact count check.
- Commit one campaign closure at a time.
