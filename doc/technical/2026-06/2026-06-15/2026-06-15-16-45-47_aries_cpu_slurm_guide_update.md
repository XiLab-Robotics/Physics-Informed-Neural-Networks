# 2026-06-15-16-45-47 Aries Cpu Slurm Guide Update

## Overview

Add CPU-oriented Aries Slurm examples to the existing cluster user guide. The
current guide documents the validated GPU/MIG `srun` and `sbatch` path, but it
does not show how to request CPU resources intentionally or how to interpret
the CPU limits exposed by the `gpus` QoS note.

## Technical Approach

Update `doc/guide/aries_cluster_user_guide.md` with a small, explicit CPU
section near the existing first interactive GPU session and first `sbatch`
template. Use the existing Aries defaults already recorded in the guide:
`aries.hpc.unimo.it`, account `xilab`, partition `ice4hpc`, QoS `gpus`, and
the call-note limit that the GPU QoS allows `cpu=8`, `gres/gpu=4`, and
`mem=100G` per job.

The user-provided batch note confirms the practical pattern used on Aries:
`#SBATCH -A xilab`, `#SBATCH -p ice4hpc`, `#SBATCH --qos=gpus`,
`#SBATCH --ntasks-per-node=8`, `#SBATCH --mem=20g`, and a MIG GPU request such
as `#SBATCH --gpus=1g.20gb:1`. The guide update should therefore distinguish
between:

- CPU-heavy work inside the validated `ice4hpc`/`gpus` QoS allocation pattern,
  where the documented CPU cap is eight CPUs per job unless `showqos` reports a
  different current limit.
- True CPU-only work, which should omit `--gpus` only if `sinfo` and `showqos`
  show a CPU-capable partition/QoS combination that accepts CPU-only jobs.

No subagent use is planned.

## Involved Components

- `doc/guide/aries_cluster_user_guide.md`
- `site/guide/aries_cluster_user_guide.md`
- `doc/README.md`

## Implementation Steps

1. Add an interactive CPU-oriented `srun` example that requests up to the known
   eight-CPU limit and sets common numerical-library thread variables from
   `SLURM_CPUS_PER_TASK`.
2. Add a CPU-oriented `sbatch` template adapted from the user's Aries notes,
   preserving the validated account, partition, QoS, memory, and MIG request.
3. Add a short CPU-only caveat explaining when to remove `--gpus` and replace
   partition/QoS values based on live `sinfo` and `showqos` output.
4. Mirror the same guide content into the Sphinx guide source under `site/`.
5. Run Markdown QA on the touched Markdown files and fix any warnings in the
   touched scope.
