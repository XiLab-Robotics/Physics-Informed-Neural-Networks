# RCIM Track1 Input-Mode Aries Script

## Purpose

Run one approved `RCIM Model-Bank Reproduction` input-mode campaign on Aries.
The script targets the polished `rcim_track1` campaign family and runs the
`global`, `fw`, and `bw` surfaces sequentially inside one Slurm allocation by
default. After the full manifest is validated, optional queue-config arguments
can restrict a Slurm allocation to one or more manifest-listed surfaces. This is
used to run `fw` and `bw` in parallel after `global` has completed.

This launcher is CPU/RAM oriented. The RCIM paper-bank workflow uses
scikit-learn model-bank training and ONNX export rather than PyTorch GPU
training, so the accepted Aries request prioritizes `32` CPU cores and `300g`
memory on the CPU-oriented `high` partition with `high` QoS. It does not
request `--gpus`, so Slurm should place the job on a CPU node rather than
`gnode01`.

## Actual-Values Campaign

```bash
sbatch scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.sbatch \
  config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_actual_values/campaign.yaml
```

Run only one validated surface:

```bash
sbatch scripts/campaigns/aries/run_rcim_track1_input_mode_campaign.sbatch \
  config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_actual_values/campaign.yaml \
  config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_actual_values/queue/002_rcim_track1_fw.yaml
```

## Preflight

Validate the campaign package before submission:

```bash
python -B scripts/campaigns/cross_wave/validate_rcim_track1_input_mode_campaign.py \
  --campaign-manifest-path config/paper_reimplementation/rcim_ml_compensation/rcim_track1_polished_input_mode_retraining/campaigns/dataset_input_mode_retraining__rcim_track1__polished_actual_values/campaign.yaml
```

## Terminal Cleanup

After the Slurm job reaches a terminal state and the stdout/stderr files have
been inspected, remove terminal `output/slurm/rcim_track1_<job_id>.out` and
`output/slurm/rcim_track1_<job_id>.err` files before committing closeout
artifacts.
