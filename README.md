# Transmission Error Modeling — Paper Reproduction

A concise, publication-oriented reproduction branch of the XiLab RV reducer transmission-error research. The complete R&D code, experiments, Codex tooling and history remain in [main](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/tree/main). This branch deliberately contains **only two scientific pipelines**.

## Clone — Paper Reproduction only

Clone only this branch with a shallow history. A default clone of the full repository would download unnecessary research history and objects from other branches.

```powershell
git clone --branch paper-reproduction --single-branch --depth 1 --no-tags https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks.git PINNs-Paper-Reproduction
cd PINNs-Paper-Reproduction

# Verify the selected branch and shallow history.
git branch --show-current
git rev-parse --is-shallow-repository
```

The expected outputs are `paper-reproduction` and `true`. The command downloads the current Paper Reproduction snapshot, including its complete polished dataset and selected pretrained models, without fetching the full development history or other branch snapshots. The dataset itself still requires substantial disk space. Do not use `--recurse-submodules` or `--unshallow` for this workflow.

To update an existing clone, run `git pull --ff-only` from the Paper Reproduction directory. No separate clone of `main` is required.

## Choose an environment

Use a dedicated Conda environment, not system Python. Choose the workflow that
matches your goal; there is no need to install both environments.

| Goal | Environment file | Environment name |
| --- | --- | --- |
| Test pretrained ONNX models, validate data and generate pointwise evaluation plots | `environment.yml` | `pinns-paper-repro` |
| Retrain supported models, replay Python checkpoints or use the full scientific backend | `environment-full.yml` | `pinns-paper-train` |

Run commands from the repository root in a Conda-enabled terminal (for example,
Anaconda PowerShell Prompt). Activate the selected environment once per terminal
session, then use ordinary `python` commands. If Conda is not initialized in
PowerShell, run `conda init powershell` and reopen the terminal.

### A. Lightweight — pretrained ONNX inference

```powershell
conda env create -f environment.yml
conda activate pinns-paper-repro

python --version
python -m pip check
```

This installs Python 3.12, NumPy, pandas, ONNX Runtime (CPU), matplotlib and
PyYAML. PyTorch, Lightning and training/export libraries are not required.
A fresh environment is lightweight; an existing `pinns-paper-repro` environment
from earlier qualification may already contain additional scientific packages.
It can be reused without deleting packages or recreating it. For an existing
environment, skip creation and activate it directly.

### B. Full — training and Python checkpoint replay

```powershell
conda env create -f environment-full.yml
conda activate pinns-paper-train

python --version
python -m pip check
```

The full environment installs the scientific dependencies from
[`requirements.txt`](requirements.txt), including PyTorch, Lightning,
scikit-learn, XGBoost, LightGBM and ONNX conversion tools. It can also execute
the lightweight workflow. The default installation resolves a platform-compatible
PyTorch package from the configured Python package index; hardware acceleration
is not guaranteed by installation alone.

If you need a specific CPU or CUDA build, use this alternative setup **instead**
of creating the environment from the full YAML. For CPU-only Windows/Linux x86-64:

```powershell
conda create -n pinns-paper-train python=3.12 pip
conda activate pinns-paper-train
python -m pip install "torch>=2.10,<3.0" --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r requirements.txt
python -m pip check
```

For GPU training, select the appropriate wheel using the official
[PyTorch installation instructions](https://pytorch.org/get-started/locally/)
before installing the remaining requirements. The optional ELM implementation
is not one of the ten retained Legacy families; install `scikit-elm` separately
only if intentionally exploring it.

Creating either environment does **not** start training. The previously
qualified Windows CPU environment and bounded model tests are documented in
the project closeout; fresh resolution of the new environment files and
full retraining are not yet qualified.

The entire canonical polished dataset is included at `data/polished_dataset/` (969 forward and 969 backward CSV). The original directory name is intentionally preserved for exact configuration compatibility. CSV columns: `theta,theta_dot,tau_load,T,theta_TE`. Raw and simplified datasets, all global-trained models, A02 and unused research models are absent.

## The two methods

**Legacy RCIM:** repository-owned faithful reimplementation of the harmonic model-bank protocol. The promoted model banks preserve ten families (SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, XGBM and LGBM) with 19 amplitude/phase targets each, for both `forward` and `backward`, in both `setpoints` and `actual_values` modes. The source retains optional ELM support; no promoted ELM weights are claimed. The original imported paper-era scripts are intentionally excluded.

**DirectML:** twelve selected model families, 23 directional pretrained ONNX files; includes the TestRig-observed HR12, PMH7, RHMLP16 and PMLP6 models, standard feedforward/GRU/LSTM/TCN/tree baselines, periodic GRU, and the K01/H08 offline specialists. **K01 and H08 are preserved as trained offline references; their specialized retraining/evaluation flows are not yet qualified as Paper Reproduction commands.** H08 is forward-only.

## Workflow A — evaluate pretrained models

Activate the lightweight environment (or use the full environment if already
active), then run:

```powershell
conda activate pinns-paper-repro

python -m unittest discover -s tests -v
python run.py catalog
python run.py validate-data

# Compare a pretrained pointwise ONNX model against a measured CSV.
python run.py evaluate --model periodic_mlp_harmonic --direction forward --csv data/polished_dataset/forward/25degree/100rpm/100.0rpm0.0Nm25.0deg.csv
```

For supported pointwise ONNX models, evaluation produces `metrics.json`,
`predictions.csv` and two PNG plots under the ignored `results/` directory.
The generic evaluator handles the six standard pointwise DirectML families
in both directions. The temporal DirectML models and Legacy RCIM coefficient
banks are also retained as ONNX archives, but need their own input/window or
harmonic-reconstruction logic; the generic `evaluate` command does not cover
them. K01/H08 require specialist state/analytical-anchor inputs. These commands
reproduce predictions from pretrained models, not a full historical training
campaign or published aggregate metrics.

## Workflow B — retrain supported models

```powershell
conda activate pinns-paper-train

# Preview a run without fitting.
python run.py train --pipeline direct_ml --model periodic_mlp_harmonic --direction forward --profile paired --dry-run

# Train one DirectML model (remove --dry-run only when ready).
python run.py train --pipeline direct_ml --model feedforward --direction backward --profile paired

# Legacy RCIM: choose input mode and direction.
python run.py train --pipeline legacy --direction forward --input-mode setpoints --profile historical
python run.py train --pipeline legacy --direction backward --input-mode actual_values --profile historical
```

Use `python run.py catalog` and `python run.py train --help` to select models and
directions. The full workflow supports the ten standard DirectML families and
the ten retained Legacy RCIM families. Run the desired direction(s) separately.
K01/H08 are archived pretrained specialists, not supported retraining targets
in this simplified branch.

Legacy uses the historical paper-style training search protocol. DirectML's
`historical` profile uses the archived training setup; `paired` uses the
**separate** condition-paired split manifest under `configs/splits/`. Results
from the two profiles are not interchangeable. A new dataset requires a
compatible replacement manifest/config, not blindly reusing the archived
assignments. Full-density training can require substantial CPU/GPU time and
memory; inspect the selected config and use `--dry-run` first.

### Reduced dataset (one temperature and speed)

The original dataset must remain unchanged. Copy the selected paired CSVs into
a separate directory named `polished_dataset`, retaining the
`forward/<temperature>degree/<speed>rpm/` and matching `backward/` paths.
Set both `paths.dataset_root` and `paths.dataset_roots.polished_dataset` in
a separate dataset YAML to the new root; do not overwrite the canonical YAML.
For DirectML paired experiments, also create a matching split manifest with
both directional paths for every selected condition and nonempty train,
validation and test assignments. Use a separate training YAML pointing to
these two files. Legacy uses a new historical-style split on the selected
files, not the archived full-dataset split.

With the full training environment activated, the existing backend commands accept these explicit training configurations:

```powershell
# Prepare the config and inspect the backend options before any fitting.
python -m scripts.training.train_feedforward_network --help
python -m scripts.paper_reimplementation.rcim_ml_compensation.original_dataset_exact_model_bank.run_original_dataset_exact_model_bank_validation --help
```

The generic `run.py train` launcher still uses the checked-in configurations;
it does not automatically select or copy a subset. Use the backend's
`--config-path` with the explicitly prepared reduced training YAML only when
intentionally starting a separate training run. Subset preparation is not a
historical-paper result or permission to start a campaign.

Each invocation prepares a non-overwriting `results/` run directory with resolved config and an execution receipt. Original backend code may still emit supplementary files under `results/` and `output/`; these are ignored by Git. Training is **never** started by `catalog` or `validate-data`.

## Files

- `environment.yml`, `environment-full.yml`: lightweight inference and complete scientific environment definitions.
- `configs/legacy/`, `configs/direct_ml/`: source-backed configurations for direction-specific training.
- `scripts/paper_reimplementation/rcim_ml_compensation/`: faithful RCIM algorithm core with unchanged mathematical routines.
- `scripts/training/`, `scripts/models/`: trimmed backend supporting baseline DirectML architectures.
- `models/legacy/` and `models/direct_ml/`: published Python/ONNX artifacts and original provenance inventories.
- `tests/`: bounded logic checks; no paper numerical or PLC guarantee.

The 18 selected Lightning `.ckpt` model files are archived as actual Git blobs, restored from the original training runs in `main`; they are not Git LFS pointers or relative path placeholders. Always check the model input/output interface and preprocessing before inference; the generic evaluation command supports only **single-input pointwise ONNX tensors**. Sequence/stateful models require model-specific evaluation. Original archive inventory paths refer to **main** and are provenance, not absolute paths in this branch.

## Reproducibility and limits

Use consistent encoder angle, signed TE offset/A0, units, direction flag and torque/speed/temperature input source. The polished setpoint input order is **angle, speed, torque, temperature, direction**. The dataset's five measured columns are not the RCIM coefficient-bank input contract. Historical observations and training metrics are preserved on main; this branch does not automatically recreate them without rerunning the matching environment and protocol.

**A source/ONNX archive is not a TestRig or TwinCAT qualification.** Neither native XAE build, PLC RAM fingerprint, deterministic 500 Hz deadlines, nor physical encoder zero are established by this branch. No external machine experiment is automatically started. The publication should distinguish offline training, runtime feasibility and physical validation. Dataset and model rights should be checked before public redistribution.
