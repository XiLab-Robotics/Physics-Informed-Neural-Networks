# Run Wave 5.2R Stage 6 Spectral And Sobolev Guidance

## Purpose

This launcher prepares, validates, and executes the fifteen-run Stage 6
campaign on `polished_dataset`, setpoint inputs, and `Fw`.

It compares the qualified Stage 5 H04 component with:

- circular first-derivative Sobolev guidance;
- uniform and fragile-band complex spectral guidance;
- combined and curriculum objectives;
- failure-informed angular weighting;
- Fourier-feature and matched raw-coordinate residuals;
- SIREN and matched tanh coordinate residuals;
- local Fourier-moment weak-form guidance.

The launcher does not run the heavy TE Curve Verification Pipeline.

## Local Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -PreflightOnly
```

## Local Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Run
```

## Remote-Compatible Preflight

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Remote -PreflightOnly
```

This selects the remote-compatible launcher path while validating locally. It
does not contact the remote workstation.

## Remote Campaign

```powershell
.\scripts\campaigns\wave_5_2\run_wave52r_stage6_spectral_sobolev_guidance.ps1 `
  -Remote -Run
```

The remote branch synchronizes source, configuration, documentation, frozen
split evidence, Stage 5 guidance evidence, and the four required Stage 5
checkpoints. After completion it synchronizes the campaign package, immutable
runs, Stage 6 analysis, generated configurations, and persistent campaign
state.

## Expected Outputs

- derivative, spectral, weak-form, and preflight evidence under
  `output/analysis/wave_5_2r/stage6_spectral_sobolev_guidance/`;
- immutable runs under
  `output/training_runs/spectral_sobolev_guidance/`;
- campaign package under `output/training_campaigns/`;
- generated YAML under `config/training/spectral_sobolev_guidance/`;
- explicit best-run, first-screen gate, and stability artifacts;
- Stage 6 results report and validated PDF.

## Stop Conditions

The launcher stops on:

- missing technical, plan, model, checkpoint, split, or anchor evidence;
- derivative estimator or SciPy/PyTorch parity failure;
- non-finite model or gradient behavior;
- coordinate residual bound failure;
- parameter-matching failure;
- target leakage or measured-runtime input use;
- any candidate-run failure;
- remote synchronization or execution failure.
