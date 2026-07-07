# Dataset Input-Mode Retraining Aries Scripts

## Purpose

Run one approved dataset/input-mode retraining campaign on Aries.

## Prepare One Campaign

```bash
python -B scripts/campaigns/cross_wave/prepare_dataset_input_mode_retraining_campaign.py \
  --family tree \
  --version simplified_setpoints
```

## GPU Smoke With `srun`

```bash
srun \
  --nodes=1 \
  --ntasks=1 \
  --cpus-per-task=4 \
  --time=00:20:00 \
  --mem=20g \
  --partition=ice4hpc \
  --account=xilab \
  --qos=gpus \
  --gpus=1g.20gb:1 \
  --mpi=pmix \
  ./scripts/campaigns/aries/run_dataset_input_mode_retraining_smoke.sh \
  config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__tree__simplified_setpoints/campaign.yaml
```

## Batch Launch With `sbatch`

```bash
sbatch scripts/campaigns/aries/run_dataset_input_mode_retraining_campaign.sbatch \
  config/training/dataset_input_mode_retraining/campaigns/dataset_input_mode_retraining__tree__simplified_setpoints/campaign.yaml
```
