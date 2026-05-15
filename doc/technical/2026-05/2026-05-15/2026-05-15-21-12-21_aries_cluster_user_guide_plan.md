# 2026-05-15-21-12-21 Aries Cluster User Guide Plan

## Overview

This document plans a repository-owned user guide for operating the Unimore
Aries cluster from a clean starting point. The guide will convert the local
call notes in `.temp/aries_call.txt` into an English, step-by-step operational
document for:

- connecting to Aries with SSH;
- adding a GitHub SSH key from the Aries Linux shell;
- cloning this repository;
- preparing a Conda environment suitable for repository tests and GPU work;
- inspecting Slurm partitions, QoS limits, jobs, and GPU availability;
- running a first interactive `srun` test;
- submitting a first non-interactive `sbatch` job.

The final guide must not publish private passwords or other secrets from the
call notes. Login examples may show usernames and hostnames, but password-based
authentication must be described as an interactive prompt or replaced by a
placeholder.

## Technical Approach

Create a canonical operational guide under `doc/guide/` with command-first
sections and compact explanations. The guide will be written for a user who has
never used Aries before but needs to run this repository on the cluster.

The guide will combine four source classes:

- Local Aries call notes from `.temp/aries_call.txt`, treated as the
  cluster-specific source of truth for Unimore-specific account, partition,
  QoS, scratch, and GPU-MIG conventions.
- The public Aries page at `https://www.labcsai.unimore.it/aries/`, used only
  as the public cluster reference.
- Official GitHub SSH documentation for Linux:
  `https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux`.
- Slurm documentation and command references:
  `https://slurm.schedmd.com/documentation.html`,
  `https://slurm.schedmd.com/sbatch.html`,
  `https://slurm.schedmd.com/srun.html`,
  `https://slurm.schedmd.com/squeue.html`, and the user-provided Harvard
  convenient command reference at
  `https://docs.rc.fas.harvard.edu/kb/convenient-slurm-commands/`.

The guide will keep Aries-specific commands separate from generic Slurm
concepts so that later cluster changes can be updated in one location. It will
prefer conservative resource requests based on the call notes: `ice4hpc`,
`xilab`, `gpus`, one `1g.20gb` GPU slice, limited CPU and memory requests, and
single-GPU execution until multi-GPU behavior is confirmed.

The first version will be documentation-only. It will not create or modify
training campaign YAML files, launchers, active campaign state, or model
registries. Any cluster execution examples will be inert examples in Markdown,
not locally executed training.

## Involved Components

- `.temp/aries_call.txt`
  Local call notes used as cluster-specific input material.
- `doc/guide/aries_cluster_user_guide.md`
  Proposed new canonical user guide.
- `doc/README.md`
  Proposed index update so the new guide is discoverable.
- `site/`
  Proposed Sphinx index update only if the existing portal includes guide
  pages in scope.
- `requirements.txt`
  Read-only unless the final guide proves that the documented install command
  needs a different repository dependency surface.
- Repository Markdown QA tooling:
  `scripts/tooling/markdown/markdown_style_check.py` and
  `scripts/tooling/markdown/run_markdownlint.py`.

## Implementation Steps

1. Read the current repository environment files that define the Conda and test
   workflow, including `requirements.txt`, available environment files, test
   entry points, and existing Linux portability notes.
2. Draft `doc/guide/aries_cluster_user_guide.md` with the following planned
   structure:
   - prerequisites and account assumptions;
   - SSH login from Windows and from Linux/macOS;
   - GitHub SSH key generation on Aries, public-key registration, and SSH
     clone test;
   - choosing `/scratch1/<username>` or `/scratch2/<username>` for active
     work versus home for persistent configuration;
   - loading modules such as Slurm, CUDA, and Anaconda;
   - cloning the repository and creating the Conda environment;
   - installing Python dependencies and validating PyTorch/CUDA visibility;
   - Slurm command cheat sheet for `sinfo`, `squeue`, `sq`, `showqos`,
     `scancel`, `srun`, and `sbatch`;
   - first interactive `srun` GPU session;
   - first repository smoke test under `srun`;
   - first `sbatch` script for a repository smoke test;
   - troubleshooting for missing `nvidia-smi`, missing modules, SSH key
     failures, pending jobs, and oversized resource requests.
3. Include a ready-to-edit `sbatch` template using the Aries-specific defaults:
   `#SBATCH -A xilab`, `#SBATCH -p ice4hpc`, `#SBATCH --qos=gpus`,
   `#SBATCH --gpus=1g.20gb:1`, one node, modest CPU and memory requests, and
   explicit output files.
4. Include a minimal interactive `srun` command that requests the same GPU
   slice and then runs shell-level checks before any Python test.
5. Add clear warnings that `srun` sessions can terminate when the SSH
   connection drops, while `sbatch` jobs continue through the scheduler.
6. Register the guide from `doc/README.md` and update Sphinx guide indices if
   the guide tree is included in the documentation portal.
7. Run scoped Markdown QA on the new and modified Markdown files:
   `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
   and `python -B scripts/tooling/markdown/run_markdownlint.py`.
8. If the Sphinx portal is touched, rebuild it with
   `python -m sphinx -W -b html site site/_build/html`, using the repository's
   documented environment fallback if the default interpreter lacks Sphinx.
9. Stop after implementation and verification. Do not create a Git commit
   without explicit user approval.
