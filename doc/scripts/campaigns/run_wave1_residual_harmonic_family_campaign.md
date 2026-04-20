# Wave 1 Residual Harmonic Family Campaign Launcher

## Overview

This launcher is the canonical short PowerShell wrapper for the residual
harmonic family optimization pass that belongs to the `Wave 1`
structured-baseline follow-up scope.

It exists so future repository-facing instructions use the corrected `Wave 1`
taxonomy for the residual-harmonic family optimization pass.

## Main Role

The launcher:

1. keeps `Wave 1` as the canonical user-facing label for the residual-family
   optimization pass;
2. assembles the approved residual-family YAML list in stable order;
3. preserves the same queue handling, terminal behavior, log files, and
   campaign artifact generation as the underlying runner.

## Practical Use

Run the canonical residual-family launcher from the repository root:

```powershell
.\scripts\\campaigns\\wave1\\run_wave1_residual_harmonic_family_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\wave1\\run_wave1_residual_harmonic_family_campaign.ps1 -PythonExecutable python
```
