# Unimore Aries Cluster User Guide

## Scope

This guide explains how to start using the Unimore Aries cluster for this
repository from a clean workstation and a clean cluster shell. It covers SSH
login, GitHub SSH setup, repository cloning, Conda setup, basic Slurm
inspection, one interactive `srun` check, and one first `sbatch` submission.

The Aries-specific values below come from the local call notes in
`.temp/aries_call.txt`. Re-check them with `sinfo`, `showqos`, and the current
cluster welcome message before running large jobs.

Do not paste passwords into scripts, Markdown files, shell history notes, or
Git-tracked files. When a password is required, type it only into the SSH
prompt.

## Useful References

- Aries public page: <https://www.labcsai.unimore.it/aries/>
- GitHub SSH key generation for Linux:
  <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux>
- GitHub SSH key registration:
  <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>
- Slurm documentation: <https://slurm.schedmd.com/documentation.html>
- Slurm `srun`: <https://slurm.schedmd.com/srun.html>
- Slurm `sbatch`: <https://slurm.schedmd.com/sbatch.html>
- Harvard convenient Slurm commands:
  <https://docs.rc.fas.harvard.edu/kb/convenient-slurm-commands/>
- PyTorch install selector: <https://pytorch.org/get-started/locally/>

## Aries Values To Know

| Item | Value |
| --- | --- |
| SSH host | `aries.hpc.unimo.it` |
| Account | `xilab` |
| Main GPU partition for this work | `ice4hpc` |
| GPU QoS | `gpus` |
| GPU node mentioned in the call | `gnode01` |
| Recommended first GPU request | `--gpus=1g.20gb:1` |
| Recommended first mode | single GPU |
| Work directories | `/scratch1/<username>` or `/scratch2/<username>` |
| Persistent home | `/unimore_home/<username>` or `~` |

The call notes indicate that `gnode01` exposes H100 GPU resources through MIG
20 GB slices. Treat `nvidia-smi` inside an allocated GPU job as the real
runtime check.

## Mental Model

Aries has a login node and compute nodes.

- Use the login node for light setup: SSH, Git clone, editing files, Conda
  environment creation, and submitting jobs.
- Use compute nodes for Python tests, CUDA checks, training, and any expensive
  execution.
- Use `srun` for an interactive allocation. If the SSH session dies, the
  interactive work can die with it.
- Use `sbatch` for non-interactive jobs. The scheduler keeps running the job
  after you disconnect.

## Connect With SSH

From Windows PowerShell:

```powershell
ssh dferrari@aries.hpc.unimo.it
```

From Linux or macOS:

```bash
ssh dferrari@aries.hpc.unimo.it
```

Replace `dferrari` with your Aries username. After a successful login you
should land on the login node, for example with a prompt similar to:

```text
[dferrari@fe01 ~]$
```

## Choose A Working Directory

Use scratch for active repository work and job output:

```bash
cd /scratch1/$USER
pwd
```

If `/scratch1/$USER` is not available or is busy, try:

```bash
cd /scratch2/$USER
pwd
```

Use home for persistent shell configuration and small configuration files:

```bash
cd ~
pwd
```

## Load Cluster Modules

List available modules:

```bash
module av
```

Load Slurm if it is not already loaded:

```bash
module load slurm
```

Load CUDA and Anaconda:

```bash
module load cuda
module load Anaconda3
```

If `Anaconda3` is not the exact module name on the current module tree, inspect
the available names:

```bash
module av Anaconda
module av python
```

Run Conda initialization only if `conda activate` is not available:

```bash
conda init bash
```

Then disconnect and reconnect, or reload the shell:

```bash
exec bash -l
```

## Add A GitHub SSH Key On Aries

First check whether an SSH key already exists:

```bash
ls -al ~/.ssh
```

Generate a new key if needed. Use the email associated with your GitHub
account:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Accept the default path unless you intentionally manage multiple keys. Use a
passphrase if you want the private key protected on the cluster.

Start the SSH agent and add the key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Print the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Open GitHub in the browser on your local workstation and add the printed public
key under `Settings -> SSH and GPG keys -> New SSH key`. The official GitHub
guide is:

```text
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
```

Test the GitHub SSH connection from Aries:

```bash
ssh -T git@github.com
```

A successful test usually identifies your GitHub account and says GitHub does
not provide shell access. That is expected.

## Clone The Repository

Move to scratch:

```bash
cd /scratch1/$USER
```

Clone with SSH:

```bash
git clone git@github.com:XiLab-Robotics/Physics-Informed-Neural-Networks.git
cd Physics-Informed-Neural-Networks
```

Check the remote:

```bash
git remote -v
```

Optional but useful Git identity setup on Aries:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

## Create The Conda Environment

Load modules first:

```bash
module load cuda
module load Anaconda3
```

Create the project environment:

```bash
conda create -y -n pinns_env python=3.12
conda activate pinns_env
python -m pip install --upgrade pip
```

Install PyTorch using the official PyTorch selector for the CUDA build that
matches the loaded CUDA module and cluster driver:

```text
https://pytorch.org/get-started/locally/
```

For a CUDA `12.4` module, start by checking the current PyTorch selector and
then use the generated command. A typical pip pattern is:

```bash
python -m pip install torch --index-url https://download.pytorch.org/whl/cu124
```

If the selector recommends a newer CUDA wheel, use the selector output instead
of this example. Then install the repository dependencies:

```bash
python -m pip install -r requirements.txt
```

For the recovered original RCIM workflow only, there is also a nested historical
requirements file:

```bash
python -m pip install -r scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/requirements.txt
```

Use that nested file only when you are explicitly working in the recovered
original workflow.

## Verify Python And CUDA

On the login node, verify imports only:

```bash
python -c "import torch, lightning, numpy, pandas, sklearn; print(torch.__version__); print(lightning.__version__)"
```

Do not assume CUDA is available on the login node. Check CUDA inside an
allocated GPU job.

## Inspect Slurm State

Show partitions and node states:

```bash
sinfo
```

Show queue state:

```bash
squeue
```

Show only your jobs:

```bash
squeue -u "$USER"
```

The call notes also mention local aliases or helper commands:

```bash
sq
sq --me
sq -u dferrari
showqos
```

Common Slurm states:

| State | Meaning |
| --- | --- |
| `R` | Running |
| `PD` | Pending |
| `CD` | Cancelled or completed, depending on the command context |
| `idle` | Node has available resources |
| `mix` | Node is partially allocated |
| `alloc` | Node is fully allocated |

Cancel one of your jobs:

```bash
scancel <job_id>
```

Cancel all of your jobs only when you really intend to stop them:

```bash
scancel -u "$USER"
```

## First Interactive GPU Session With srun

Start with a modest request. This matches the Aries call notes and avoids
asking for more CPU or memory than the first check needs:

```bash
srun \
  --ntasks=4 \
  --nodes=1 \
  --mem=40g \
  --partition=ice4hpc \
  --account=xilab \
  --qos=gpus \
  --gpus=1g.20gb:1 \
  --pty \
  --mpi=pmix \
  /bin/bash
```

Once the shell opens on the allocated node, load modules and activate the
environment:

```bash
module load cuda
module load Anaconda3
conda activate pinns_env
```

Check the GPU:

```bash
nvidia-smi
```

Check PyTorch CUDA visibility:

```bash
python -c "import torch; print('cuda_available=', torch.cuda.is_available()); print('device_count=', torch.cuda.device_count()); print('device_name=', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu')"
```

Exit the interactive allocation when finished:

```bash
exit
```

## CPU-Oriented Interactive Session With srun

The Aries notes captured for this project describe the validated allocation
surface as account `xilab`, partition `ice4hpc`, and QoS `gpus`. That QoS was
reported with a per-job CPU limit of `cpu=8`, so use at most eight CPU tasks
unless `showqos` reports a newer limit.

For CPU-heavy debugging inside the validated Aries allocation pattern, keep the
MIG GPU request and spend the allocation mainly on CPU work:

```bash
srun \
  --ntasks=8 \
  --nodes=1 \
  --mem=20g \
  --partition=ice4hpc \
  --account=xilab \
  --qos=gpus \
  --gpus=1g.20gb:1 \
  --pty \
  --mpi=pmix \
  /bin/bash
```

Once the shell opens on the allocated node, bind common numerical-library thread
counts to the Slurm CPU request before running Python:

```bash
module load Anaconda3
conda activate pinns_env

export OMP_NUM_THREADS="${SLURM_NTASKS:-8}"
export MKL_NUM_THREADS="${SLURM_NTASKS:-8}"
export OPENBLAS_NUM_THREADS="${SLURM_NTASKS:-8}"
export NUMEXPR_NUM_THREADS="${SLURM_NTASKS:-8}"

python -c "import os; print('cpu_count=', os.cpu_count()); print('slurm_ntasks=', os.environ.get('SLURM_NTASKS'))"
```

For true CPU-only work, first verify that Aries exposes a CPU partition or CPU
QoS that accepts jobs without GPUs:

```bash
sinfo
showqos
```

Then remove the GPU request and replace the partition and QoS values with the
CPU-capable values shown by the live cluster commands:

```bash
srun \
  --ntasks=8 \
  --nodes=1 \
  --mem=20g \
  --partition=<cpu_partition> \
  --account=xilab \
  --qos=<cpu_qos> \
  --pty \
  --mpi=pmix \
  /bin/bash
```

If Slurm rejects the CPU-only request, return to the validated
`ice4hpc`/`gpus` pattern above or ask the cluster operator which CPU partition
is enabled for account `xilab`.

## First Repository Test Under srun

Use the repository's lightweight setup validation before launching training:

```bash
cd /scratch1/$USER/Physics-Informed-Neural-Networks
conda activate pinns_env
python -B scripts/training/validate_training_setup.py \
  --config-path config/training/feedforward/presets/baseline.yaml \
  --platform linux
```

Then run the minimal smoke test:

```bash
python -B scripts/training/run_training_smoke_test.py \
  --config-path config/training/feedforward/presets/baseline.yaml \
  --output-suffix aries_first_smoke_test \
  --fast-dev-run-batches 1 \
  --platform linux
```

These commands are still tests, not full campaigns. They create validation or
smoke-test artifacts under the repository output/report structure.

## First sbatch Script

Create a batch script in the repository root:

```bash
nano aries_first_smoke_test.sbatch
```

Use this template:

```bash
#!/bin/bash -l
#SBATCH -A xilab
#SBATCH -p ice4hpc
#SBATCH --qos=gpus
#SBATCH --time=01:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=40g
#SBATCH --gpus=1g.20gb:1
#SBATCH --job-name=aries_smoke
#SBATCH --output=aries_smoke_%j.out
#SBATCH --error=aries_smoke_%j.err

set -euo pipefail

module load cuda
module load Anaconda3

conda activate pinns_env

cd /scratch1/${USER}/Physics-Informed-Neural-Networks

echo "[INFO] Host: $(hostname)"
echo "[INFO] Workdir: $(pwd)"
echo "[INFO] Python: $(which python)"

nvidia-smi

python -c "import torch; print('cuda_available=', torch.cuda.is_available()); print('device_count=', torch.cuda.device_count()); print('device_name=', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu')"

python -B scripts/training/validate_training_setup.py \
  --config-path config/training/feedforward/presets/baseline.yaml \
  --platform linux

python -B scripts/training/run_training_smoke_test.py \
  --config-path config/training/feedforward/presets/baseline.yaml \
  --output-suffix aries_first_sbatch_smoke_test \
  --fast-dev-run-batches 1 \
  --platform linux
```

Submit it:

```bash
sbatch aries_first_smoke_test.sbatch
```

Watch the queue:

```bash
squeue -u "$USER"
```

Inspect output after the job starts or finishes:

```bash
tail -n 100 aries_smoke_<job_id>.out
tail -n 100 aries_smoke_<job_id>.err
```

Replace `<job_id>` with the numeric job id printed by `sbatch`.

## CPU-Oriented sbatch Script

Use this template when the job mainly needs CPU tasks but should follow the
validated Aries `ice4hpc`/`gpus` allocation pattern from the project notes:

```bash
#!/bin/bash -l
#SBATCH -A xilab
#SBATCH -p ice4hpc
#SBATCH --qos=gpus
#SBATCH --time=24:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=20g
#SBATCH --gpus=1g.20gb:1
#SBATCH --job-name=test_cpu
#SBATCH --output=cpu_%j.out
#SBATCH --error=cpu_%j.err

set -euo pipefail

module load Anaconda3

conda activate pinns_env

cd /scratch1/${USER}/Physics-Informed-Neural-Networks

export OMP_NUM_THREADS="${SLURM_NTASKS_PER_NODE:-8}"
export MKL_NUM_THREADS="${SLURM_NTASKS_PER_NODE:-8}"
export OPENBLAS_NUM_THREADS="${SLURM_NTASKS_PER_NODE:-8}"
export NUMEXPR_NUM_THREADS="${SLURM_NTASKS_PER_NODE:-8}"

echo "[INFO] Host: $(hostname)"
echo "[INFO] Workdir: $(pwd)"
echo "[INFO] Python: $(which python)"
echo "[INFO] SLURM job: ${SLURM_JOB_ID}"
echo "[INFO] SLURM tasks per node: ${SLURM_NTASKS_PER_NODE}"

python -c "import os; print('cpu_count=', os.cpu_count()); print('threads=', os.environ.get('OMP_NUM_THREADS'))"

python ./job01/miojob.py
```

Submit it with:

```bash
sbatch test_cpu.sbatch
```

For a true CPU-only `sbatch` script, remove `#SBATCH --gpus=1g.20gb:1` only
after `sinfo` and `showqos` confirm the CPU partition and QoS to use for
account `xilab`.

## Resource Request Rules Of Thumb

Start smaller than the maximum and scale only after a successful smoke test.

| Use Case | Starting Request |
| --- | --- |
| Shell and import checks | login node, no Slurm job |
| Interactive GPU check | `--ntasks=4 --mem=40g --gpus=1g.20gb:1` |
| Interactive CPU-heavy check | `--ntasks=8 --mem=20g --gpus=1g.20gb:1` |
| First smoke test | `--ntasks-per-node=4 --mem=40g --gpus=1g.20gb:1` |
| First CPU-heavy batch job | `--ntasks-per-node=8 --mem=20g --gpus=1g.20gb:1` |
| Heavier GPU training | Increase time first, then memory or CPU only if needed |
| True CPU-only job | Use live `sinfo` and `showqos` CPU partition/QoS values |

The call notes say the GPU QoS allows up to `cpu=8`, `gres/gpu=4`, and
`mem=100G` per job, with a per-user GPU limit visible through `showqos`.
Request less than the maximum unless the job actually needs it. Smaller jobs
usually queue faster.

## Troubleshooting

### `nvidia-smi` Is Missing

On the login node this can be normal. Inside a GPU allocation, load CUDA:

```bash
module load cuda
nvidia-smi
```

If it still fails, confirm that the job requested a GPU:

```bash
squeue -j <job_id> -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"
```

### Job Stays Pending

Check the pending reason:

```bash
squeue -u "$USER"
```

Common causes are resource pressure, priority, QoS limits, or asking for too
much CPU, memory, walltime, or GPU.

### Interactive Session Dies

Use `sbatch` for any job that should survive a dropped SSH connection. Keep
`srun --pty /bin/bash` for short debugging only.

### GitHub Clone Fails With `Permission denied (publickey)`

Check that the key exists and is loaded:

```bash
ls -al ~/.ssh
ssh-add -l
ssh -T git@github.com
```

Then verify that the public key in `~/.ssh/id_ed25519.pub` is registered in
GitHub.

### Conda Command Not Found

Reload the Anaconda module:

```bash
module load Anaconda3
which conda
```

If needed, initialize Bash and reconnect:

```bash
conda init bash
exit
```

### CUDA Is Not Available In PyTorch

Check all three layers:

```bash
module load cuda
nvidia-smi
python -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available())"
```

If `nvidia-smi` works but `torch.cuda.is_available()` is false, reinstall
PyTorch using the current command from the official PyTorch install selector.

## First Full Training Or Campaign

Do not turn the first `sbatch` smoke test into a full training campaign by
editing only the Python command. For a real training campaign, prepare the
campaign plan, YAML queue, launcher, active campaign state, and approval gate
required by the repository workflow.

For existing approved Linux launchers, prefer the repository-owned scripts
under `scripts/campaigns/` instead of hand-written cluster commands.
