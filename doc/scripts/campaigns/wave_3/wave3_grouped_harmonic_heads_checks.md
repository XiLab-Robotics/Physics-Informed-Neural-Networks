# Wave 5.1 Grouped Harmonic Heads Checks

## Purpose

`run_wave3_grouped_harmonic_heads_checks.ps1` validates the `Wave 5.1` grouped
harmonic-heads skeleton. It is a dry-run check launcher only. It must not
enqueue or launch training.

## Command

```powershell
.\scripts\campaigns\wave_3\run_wave3_grouped_harmonic_heads_checks.ps1
```

## What It Runs

- Python compile check for the grouped-head model, model factory, and
  validator.
- Template metadata validation for `implementation-ready` and
  `not campaign-ready` status.
- Model factory construction for `wave3_grouped_harmonic_heads`.
- Point and sequence forward smoke checks.
- Auxiliary-output validation for low-order, stable-middle, high-order,
  grouped-harmonic, residual, and combined prediction tensors.

## Outputs

The validator writes a dry-run summary under:

```text
output/validation_checks/wave3_grouped_harmonic_heads/
```

The expected file is:

- `wave3_grouped_harmonic_heads_validation_summary.yaml`.

## Campaign Boundary

Real `Wave 5.1` grouped-head training remains blocked until the separate
`Wave 4.2` quantile / probabilistic campaign is closed out and a new campaign
plan explicitly approves queue size, surfaces, losses, branch weights,
regularization policy, and launch mode.
