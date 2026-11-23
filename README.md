# Transmission Error Modeling — Paper Reproduction

A concise, publication-oriented reproduction branch of the XiLab RV reducer transmission-error research. The complete R&D code, experiments, Codex tooling and history remain in [main](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/tree/main). This branch deliberately contains **only two scientific pipelines**.

## Install

Use Python 3.12. Install a PyTorch build matching your platform, then run:

```powershell
python -m pip install -r requirements.txt
python run.py catalog
python run.py validate-data
```

The entire canonical polished dataset is included at `data/polished_dataset/` (969 forward and 969 backward CSV). The original directory name is intentionally preserved for exact configuration compatibility. CSV columns: `theta,theta_dot,tau_load,T,theta_TE`. Raw and simplified datasets, all global-trained models, A02 and unused research models are absent.

## The two methods

**Legacy RCIM:** repository-owned faithful reimplementation of the harmonic model-bank protocol. The promoted model banks preserve ten families (SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM and LGBM) with 19 amplitude/phase targets each, for both `forward` and `backward`, in both `setpoints` and `actual_values` modes. The source retains optional ELM support; no promoted ELM weights are claimed. The original imported paper-era scripts are intentionally excluded.

**DirectML:** twelve selected model families, 23 directional pretrained ONNX files; includes the TestRig-observed HR12, PMH7, RHMLP16 and PMLP6 models, standard feedforward/GRU/LSTM/TCN/tree baselines, periodic GRU, and the K01/H08 offline specialists. **K01 and H08 are preserved as trained offline references; their specialized retraining/evaluation flows are not yet qualified as Paper Reproduction commands.** H08 is forward-only.

## Usage

```powershell
# Show available pretrained models and directions
python run.py catalog

# Fast structural validation (not a full numeric checksum audit)
python run.py validate-data

# Preview a new training run without doing computation
python run.py train --pipeline direct_ml --model periodic_mlp_harmonic --direction forward --profile paired --dry-run

# Explicitly train a selected DirectML baseline
python run.py train --pipeline direct_ml --model feedforward --direction backward --profile paired

# Exact historical RCIM reimplementation
python run.py train --pipeline legacy --direction forward --input-mode setpoints --profile historical
python run.py train --pipeline legacy --direction backward --input-mode actual_values --profile historical

# Bounded pointwise ONNX evaluation of one polished CSV
python run.py evaluate --model periodic_mlp_harmonic --direction forward --csv data/polished_dataset/forward/25degree/100rpm/100.0rpm0.0Nm25.0deg.csv
```

Legacy reproduces the historical paper-style training search protocol. DirectML's `historical` profile uses the archived training setup; `paired` uses the **separate** condition-paired split manifest stored under `configs/splits/`. Results obtained with these two profiles are not interchangeable. For supported pointwise ONNX models, evaluation produces a compact `metrics.json`, `predictions.csv`, and two PNG overlays/errors under the ignored `results/` directory. A new dataset requires a compatible replacement manifest/config, not blindly reusing the archived assignments.

Each invocation prepares a non-overwriting `results/` run directory with resolved config and an execution receipt. Original backend code may still emit supplementary files under `results/` and `output/`; these are ignored by Git. Training is **never** started by `catalog` or `validate-data`.

## Files

- `configs/legacy/`, `configs/direct_ml/`: source-backed configurations for direction-specific training.
- `scripts/paper_reimplementation/rcim_ml_compensation/`: faithful RCIM algorithm core with unchanged mathematical routines.
- `scripts/training/`, `scripts/models/`: trimmed backend supporting baseline DirectML architectures.
- `models/legacy/` and `models/direct_ml/`: published Python/ONNX artifacts and original provenance inventories.
- `tests/`: bounded logic checks; no paper numerical or PLC guarantee.

Some Python checkpoints may be Git LFS pointer files until Git LFS objects are fetched. Always check the model input/output interface and preprocessing before inference; the generic evaluation command supports only **single-input pointwise ONNX tensors**. Sequence/stateful models require model-specific evaluation. Original archive inventory paths refer to **main** and are provenance, not absolute paths in this branch.

## Reproducibility and limits

Use consistent encoder angle, signed TE offset/A0, units, direction flag and torque/speed/temperature input source. The polished setpoint input order is **angle, speed, torque, temperature, direction**. The dataset's five measured columns are not the RCIM coefficient-bank input contract. Historical observations and training metrics are preserved on main; this branch does not automatically recreate them without rerunning the matching environment and protocol.

**A source/ONNX archive is not a TestRig or TwinCAT qualification.** Neither native XAE build, PLC RAM fingerprint, deterministic 500 Hz deadlines, nor physical encoder zero are established by this branch. No external machine experiment is automatically started. The publication should distinguish offline training, runtime feasibility and physical validation. Dataset and model rights should be checked before public redistribution.
