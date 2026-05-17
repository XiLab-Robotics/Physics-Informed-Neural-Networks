# Track 1 Bidirectional Paper-Faithful Grid-Search Campaign Launcher

## Overview

This launcher executes the prepared `Track 1` bidirectional paper-faithful
campaign that replaces the old `400`-run literal-refresh wave.

The forward and backward campaign surfaces have both completed for the current
full-dataset Track 1 closeout. Keep this launcher documented because it remains
the canonical rerun path on Windows and Linux, but treat new reruns as new
approved campaigns rather than as unfinished closure work.

The script is stored in:

- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1`
- `scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh`

The Linux launcher uses the shared Bash streaming helper:

- `scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh`

The exact-paper local and remote helper equivalents are:

- `scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.sh`
- `scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.sh`

## Main Role

The launcher reads the prepared queue from
`doc/running/active_training_campaign.yaml` and launches the exact-paper queue
through the canonical remote wrapper when `-Remote` is used.

The prepared package covers:

- `forward` and `backward`;
- all `11` operational exact-paper families, including `ELM`;
- exactly `1` grid-search run per family-direction surface;
- total queue size `22`.

The completed closure used this paper-faithful sizing rule instead of widening
the grid search to chase all-green benchmark cells. Later all-green or
restricted-dataset studies must document their changed objective separately.

This campaign also depends on the restored historical search protocol in the
shared exact-paper training path:

- `GridSearchCV` fit on the prepared training split;
- global `cross_validate(...)` replay on the search wrapper;
- target-wise `cross_validate(...)` replay on the best wrapped estimators.

Each prepared campaign instance writes to a fresh campaign-specific output root
under:

- `output/training_campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/<campaign_name>/`

## Preparation Step

Generate the package and update the active campaign state with:

```powershell
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py
```

On Linux, prepare a new package with Linux-formatted repository-relative path
surfaces:

```bash
conda run -n standard_ml_codex_env python scripts/campaigns/track1/exact_paper/prepare_track1_bidirectional_paper_faithful_grid_search_campaign.py --linux
```

## Launch Command

Windows PowerShell:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 -Remote
```

Linux Bash on the Unimore Aries clone:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh --linux
```

Linux Bash remote dry run:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh \
  --direction Forward \
  --families MLP \
  --stage Search \
  --linux \
  --remote \
  --remote-repository-path /path/to/remote/standardml \
  --dry-run
```

## Operator View

The remote operator console remains compact:

- the progress bar advances on real config boundaries;
- the active run log remains visible under `output/training_campaigns/.../logs/`;
- the queue is intentionally small because the paper-faithful design uses one
  search pass per family-direction surface instead of a seed-sweep campaign.

The launcher now also exposes the exact-paper stage-control and verbosity
surface inherited from the shared runner:

- `-Direction Forward|Backward|Both`
- `-Family All|SVR|MLP|RF|DT|ET|ERT|GBM|HGBM|XGBM|LGBM|ELM`
- `-Families "MLP"` or `-Families "MLP,RF,GBM"`
- `-Stage Search|Eval|Export|LoadBest`
- `-BestParameterSummaryPath <path>`
- `-NoEval`
- `-NoExport`
- `-GridSearchVerboseOverride <int>`
- `-HistoricalCrossValidateVerboseOverride <int>`

The Bash launcher exposes the same local execution surface with GNU-style
arguments:

- `--direction Forward|Backward|Both`
- `--family All|SVR|MLP|RF|DT|ET|ERT|GBM|HGBM|XGBM|LGBM|ELM`
- `--families "MLP,RF,GBM"`
- `--stage Search|Eval|Export|LoadBest`
- `--best-parameter-summary-path <path>`
- `--no-eval`
- `--no-export`
- `--grid-search-verbose-override <int>`
- `--historical-cross-validate-verbose-override <int>`
- `--conda-environment-name <name>`
- `--python-executable <command>`
- `--linux` or `--windows`
- `--dry-run`
- `--remote`
- `--remote-host-alias <host>`
- `--remote-repository-path <path>`
- `--remote-conda-environment-name <name>`

Examples:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "MLP" `
  -Stage Search `
  -GridSearchVerboseOverride 3 `
  -HistoricalCrossValidateVerboseOverride 10 `
  -Remote
```

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "RF" `
  -Stage LoadBest `
  -NoExport `
  -Remote
```

Multiple families in one sliced invocation:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "MLP,RF,GBM" `
  -Stage Search `
  -Remote
```

Linux equivalent:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh \
  --direction Forward \
  --families "MLP,RF,GBM" \
  --stage Search \
  --linux
```

Queue-selection dry run without launching training:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh \
  --direction Forward \
  --families "MLP,RF" \
  --stage Search \
  --linux \
  --dry-run
```

Remote command dry run without SSH, sync, or training:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh \
  --direction Forward \
  --families "MLP" \
  --stage Search \
  --linux \
  --remote \
  --remote-host-alias aries-login \
  --remote-repository-path /home/<user>/StandardML-Codex \
  --remote-conda-environment-name standard_ml_codex_env \
  --dry-run
```

Full forward operational family queue, including `ELM`:

```powershell
.\scripts\campaigns\track1\exact_paper\run_track1_bidirectional_paper_faithful_grid_search_campaign.ps1 `
  -Direction Forward `
  -Families "SVR, MLP, RF, DT, ET, ERT, GBM, HGBM, LGBM, XGBM, ELM" `
  -Stage Search `
  -GridSearchVerboseOverride 3 `
  -HistoricalCrossValidateVerboseOverride 10 `
  -Remote
```

Linux equivalent:

```bash
bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh \
  --direction Forward \
  --families "SVR,MLP,RF,DT,ET,ERT,GBM,HGBM,LGBM,XGBM,ELM" \
  --stage Search \
  --grid-search-verbose-override 3 \
  --historical-cross-validate-verbose-override 10 \
  --linux
```

`Search` keeps the current default behavior and can still chain evaluation and
export automatically. `LoadBest` reuses the repository-owned exact-paper
best-parameter registry when coverage exists, or one explicit
`-BestParameterSummaryPath` when the operator wants a specific saved run.

`Direction` plus `Family` or `Families` now let the operator slice the
prepared `22`-run package into one branch, one family, or one small
family subset without changing the paper-faithful search protocol itself.

The launcher and remote wrapper now also keep the operator surface much more
alive during long-running searches:

- frequent Python-side stage markers;
- summarized grid-search heartbeat lines with completed versus expected CV-fit
  counts;
- target-wise historical cross-validation progress markers;
- a second remote progress bar for substage counters when the runner emits
  them.

The Bash path mirrors the same queue selection and command construction without
requiring PowerShell. The remote Bash wrapper is Linux-to-Linux oriented: it
uses `ssh` and `tar`, syncs the requested source roots, verifies the selected
launcher and campaign configs, and then launches the canonical Bash campaign
entry point on the remote repository clone. Use `--dry-run` first on Aries to
inspect the resolved command before allowing any training process to start.
