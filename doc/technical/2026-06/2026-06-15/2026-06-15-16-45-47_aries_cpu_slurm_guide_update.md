# 2026-06-15-16-45-47 Aries Cpu Slurm Guide Update

## Overview

Add corrected Aries Slurm examples to the existing cluster user guide. The
current guide documents the validated GPU/MIG `srun` and `sbatch` path, but it
does not clearly separate interactive compute-node shells, `srun` script
execution, CPU-only allocations, GPU allocations, and queue inspection
commands.

## Technical Approach

Update `doc/guide/aries_cluster_user_guide.md` with explicit, separate Slurm
operator sections. Use the existing Aries defaults already recorded in the
guide: `aries.hpc.unimo.it`, account `xilab`, GPU partition `ice4hpc`, GPU QoS
`gpus`, CPU QoS values `normal`/`high`/`low`, and the call-note limit that the
GPU QoS allows `cpu=8`, `gres/gpu=4`, and `mem=100G` per job.

The user-provided batch note confirms the practical pattern used on Aries:
`#SBATCH -A xilab`, `#SBATCH -p ice4hpc`, `#SBATCH --qos=gpus`,
`#SBATCH --ntasks-per-node=8`, `#SBATCH --mem=20g`, and a MIG GPU request such
as `#SBATCH --gpus=1g.20gb:1` for GPU-partition work. The live terminal
evidence also confirms that `sq` is not available, `squeue --me` is available,
`squeue -me` is invalid, and `showqos` can be unavailable inside a compute-node
shell while available on the login node.

The guide update should therefore distinguish between:

- Interactive `srun --pty /bin/bash` sessions for manual terminal work on a
  compute node.
- `srun` script execution, where resources are passed on the `srun` command
  line and `#SBATCH` directives are only comments.
- CPU-only allocations on CPU partitions such as `user-debug`, `low`, `high`,
  or `ulow` with CPU QoS values such as `normal`.
- GPU allocations on `ice4hpc` with QoS `gpus` and an explicit MIG GPU request.
- Queue inspection and cancellation commands using full Slurm commands instead
  of unavailable aliases.

No subagent use is planned.

## Involved Components

- `doc/guide/aries_cluster_user_guide.md`
- `site/guide/aries_cluster_user_guide.md`, which includes the guide from
  `doc/guide/`
- `doc/README.md`

## Implementation Steps

1. Replace alias-style queue examples with full `squeue`, `squeue --me`,
   `squeue -u "$USER"`, `scontrol show job`, and `scancel` examples.
2. Add interactive GPU and CPU compute-node sections that show when
   `srun --pty /bin/bash` opens a manual shell on a node.
3. Add a dedicated `srun` script section with CPU and GPU hello-world checks,
   making clear that `#SBATCH` directives are not consumed by `srun`.
4. Add a CPU-only `sbatch` template that uses CPU partitions and QoS values
   without a GPU request.
5. Keep the existing GPU `sbatch` path for `ice4hpc`/`gpus` work and update
   the resource rule-of-thumb table.
6. Run Markdown QA on the touched Markdown files and fix any warnings in the
   touched scope.
