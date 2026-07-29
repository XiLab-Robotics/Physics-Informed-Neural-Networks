# Run Wave 5.2R Stage 5 Complex Harmonic Coefficient Residuals

## Purpose

This launcher prepares, validates, and executes the eighteen-run Stage 5
campaign on `polished_dataset`, setpoint inputs, and `Fw` curves.

The campaign replaces Stage 4 point-payload training with one shared canonical
representation:

- `966` accepted forward curves;
- `2048` uniform angular samples per curve;
- explicit offset and sine/cosine coefficients;
- matched direct and PF-A-anchored coefficient candidates;
- training-only order selection, scaling, bounds, and neighbor topology.

It does not run the heavy TE Curve Verification Pipeline.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 -PreflightOnly
```

The preflight regenerates the representation evidence and all eighteen queue
YAML files, then validates full output shapes, finite gradients, exact
zero-correction PF-A replay, coefficient bounds, and NumPy/PyTorch
reconstruction parity.

## Local Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 -Run
```

## Conditional Stability Continuation

After the first-screen closeout selects the candidate, run its two additional
seeds with:

```powershell
conda run --no-capture-output -n pinns_env python -B `
  scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.py `
  --run-stability
```

The completed Stage 5 campaign used this command for H04 at seeds `271828`
and `161803`, producing four successful continuation runs: H04 and its
parameter-matched C04 control at both seeds.

## Remote-Compatible Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 -Remote -PreflightOnly
```

This validates the complete local package while selecting the remote-compatible
launcher branch. It does not contact the remote workstation.

## Remote Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1 -Remote -Run
```

The remote branch packages and synchronizes source, configuration,
documentation, split evidence, PF-A anchor evidence, and analysis inputs. It
then runs the same repository-owned Python campaign on the remote conda
environment and synchronizes campaign outputs, per-run checkpoints and
predictions, Stage 5 analysis artifacts, generated configurations, and
persistent campaign state back into the local repository.

## Expected Outputs

- representation and preflight evidence under
  `output/analysis/wave_5_2r/stage5_complex_harmonic_coefficient_residuals/`;
- immutable run instances under
  `output/training_runs/complex_harmonic_coefficient_residuals/`;
- campaign package under `output/training_campaigns/`;
- generated queue YAML files under
  `config/training/complex_harmonic_coefficient_residuals/`;
- campaign leaderboard and explicit best-run YAML and Markdown;
- post-campaign Stage 5 bounded curve-first closeout report and PDF.

## Stop Conditions

The launcher stops on:

- missing technical, plan, model, split, or anchor evidence;
- uniform-representation mismatch;
- coefficient reconstruction or bound failure;
- non-finite forward or gradient behavior;
- target leakage or measured-runtime input use;
- any candidate-run failure;
- remote synchronization or execution failure.
